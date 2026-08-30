"""
FastAPI Routes Ottimizzate - Backend Performance Boost
Implementa endpoint sincroni (def) per non bloccare event loop,
con integrazione del database ottimizzato.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
import logging

from optimized_brain_db import create_optimized_brain_db, OptimizedBrainDB

logger = logging.getLogger(__name__)
router = APIRouter()

# Singleton DB instance (inizializzata all'avvio)
db: OptimizedBrainDB = None


def init_db(db_path: str = "universal_brain.db"):
    """Inizializza il database ottimizzato all'avvio."""
    global db
    db = create_optimized_brain_db(db_path)
    logger.info("🧠 Database ottimizzato inizializzato")


class NodeInput(BaseModel):
    id: str
    label: str
    hemisphere: str = "LEFT"
    primary_label: str = "CONCEPT"
    category: str = "GENERAL"
    layer_level: int = 2
    summary: str = ""
    details: Dict[str, Any] = {}
    confidence: str = "EXTRACTED"
    parent_graph_id: str = "root"


class EdgeInput(BaseModel):
    source: str
    target: str
    relation: str = "RELATED_TO"
    confidence: str = "EXTRACTED"
    weight: float = 1.0


class CrossLinkInput(BaseModel):
    """Modello per ponti callosali tra emisferi."""
    left_node: str
    right_node: str


class IngestRequest(BaseModel):
    nodes: List[NodeInput]
    edges: List[EdgeInput]
    cross_links: Optional[List[CrossLinkInput]] = None


class CrossLinkInput(BaseModel):
    """Modello per ponti callosali tra emisferi."""
    left_node: str
    right_node: str
    cross_links: Optional[List[CrossLinkInput]] = None


@router.get("/api/graph/stats")
def get_graph_stats():
    """
    Endpoint SINCRONO (def) - Non blocca event loop.
    Restituisce statistiche del grafo in tempo reale.
    """
    try:
        stats = db.get_full_graph_stats()
        return {
            "success": True,
            "data": stats,
            "cache_status": "active" if not db._cache_dirty else "dirty"
        }
    except Exception as e:
        logger.error(f"Errore stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/memory/ingest")
def ingest_memory(request: IngestRequest, background_tasks: BackgroundTasks):
    """
    Endpoint SINCRONO per bulk ingest con executemany.
    Supporta cross_links per ponti callosali (CORPUS_CALLOSUM_LINK).
    Compatibile con Graphify Protocol.
    """
    try:
        nodes_dict = [n.dict() for n in request.nodes]
        edges_dict = [e.dict() for e in request.edges]
        cross_links_dict = None
        if request.cross_links:
            cross_links_dict = [cl.dict() for cl in request.cross_links]

        result = db.bulk_ingest(nodes_dict, edges_dict, cross_links_dict)

        return {
            "success": True,
            "message": f"Inseriti {result[\'nodes_inserted\']} nodi, {result[\'edges_inserted\']} archi, {result.get(\'cross_links_inserted\', 0)} cross-link",
            "data": result
        }
    except Exception as e:
        logger.error(f"Errore ingest: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/graph/subgraph/{node_id}")
def get_subgraph(node_id: str, depth: int = 2):
    """
    Estrae sotto-grafo usando Recursive CTE (ZERO round-trip Python).
    Profondità configurabile (default: 2 hop).
    """
    try:
        # Verifica esistenza nodo
        node = db.get_node_by_id_cached(node_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Nodo {node_id} non trovato")
        
        nodes, edges = db.bfs_subgraph_cte(node_id, max_depth=depth)
        
        return {
            "success": True,
            "data": {
                "focal_node": node,
                "subgraph_nodes": nodes,
                "subgraph_edges": edges,
                "depth": depth,
                "total_nodes": len(nodes),
                "total_edges": len(edges)
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Errore subgraph: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/graph/path/{start}/{end}")
def find_shortest_path(start: str, end: str):
    """
    Trova cammino minimo con BFS nativo SQL (CTE ricorsiva).
    Restituisce percorso ordinato o 404 se nessun path.
    """
    try:
        # Verifica esistenza nodi
        start_node = db.get_node_by_id_cached(start)
        end_node = db.get_node_by_id_cached(end)
        
        if not start_node:
            raise HTTPException(status_code=404, detail=f"Nodo {start} non trovato")
        if not end_node:
            raise HTTPException(status_code=404, detail=f"Nodo {end} non trovato")
        
        path = db.shortest_path_cte(start, end)
        
        if not path:
            raise HTTPException(
                status_code=404, 
                detail=f"Nessun percorso tra {start} e {end}"
            )
        
        return {
            "success": True,
            "data": {
                "start": start,
                "end": end,
                "path": path,
                "length": len(path) - 1,  # Numero di archi
                "algorithm": "BFS via Recursive CTE"
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Errore pathfinding: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/graph/neighbors/{node_id}")
def get_neighbors(node_id: str):
    """
    Ottiene vicini da cache in memoria (0.5ms).
    Cache invalidata automaticamente dopo scritture.
    """
    try:
        node = db.get_node_by_id_cached(node_id)
        if not node:
            raise HTTPException(status_code=404, detail=f"Nodo {node_id} non trovato")
        
        neighbors_ids = db.get_neighbors(node_id)
        
        # Recupera dettagli vicini
        neighbors = []
        for neighbor_id in neighbors_ids:
            neighbor_data = db.get_node_by_id_cached(neighbor_id)
            if neighbor_data:
                neighbors.append(neighbor_data)
        
        return {
            "success": True,
            "data": {
                "node_id": node_id,
                "neighbors": neighbors,
                "count": len(neighbors),
                "from_cache": True
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Errore neighbors: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.on_event("shutdown")
def shutdown_db():
    """Chiude connessione DB allo shutdown."""
    if db:
        db.close()
        logger.info("🔒 Database chiuso correttamente")
