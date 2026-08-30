"""
Database Manager Ottimizzato - Opzione C (Ibrida)
Implementa:
1. In-Memory Adjacency Cache per letture ultra-veloci
2. Recursive CTE per BFS/Subgraph nativi in SQL
3. Bulk ingest con executemany
4. Endpoint sincroni (def) per non bloccare event loop
5. LRU Cache per query frequenti
"""

import sqlite3
import logging
from typing import List, Dict, Any, Optional, Tuple, Set
from collections import defaultdict
from functools import lru_cache
from datetime import datetime
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OptimizedBrainDB:
    """Gestione database ottimizzata con cache in memoria e CTE ricorsive."""
    
    def __init__(self, db_path: str = "universal_brain.db"):
        self.db_path = db_path
        self._adjacency_cache: Dict[str, Set[str]] = defaultdict(set)
        self._cache_dirty = True
        self._init_connection()
    
    def _init_connection(self):
        """Inizializza connessione con PRAGMA ottimizzati."""
        self.conn = sqlite3.connect(
            self.db_path,
            check_same_thread=False,
            isolation_level=None  # Auto-commit per WAL
        )
        self._apply_pragmas()
    
    def _apply_pragmas(self):
        """Applica configurazioni SQLite ad alte prestazioni."""
        pragmas = [
            "PRAGMA journal_mode=WAL",
            "PRAGMA synchronous=NORMAL",
            "PRAGMA cache_size=-64000",  # 64MB
            "PRAGMA temp_store=MEMORY",
            "PRAGMA busy_timeout=5000",
            "PRAGMA foreign_keys=ON"
        ]
        cursor = self.conn.cursor()
        for pragma in pragmas:
            cursor.execute(pragma)
        self.conn.commit()
    
    @contextmanager
    def get_cursor(self):
        """Context manager per cursori con gestione errori."""
        cursor = self.conn.cursor()
        try:
            yield cursor
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Errore transazione: {e}")
            raise
        finally:
            cursor.close()
    
    def _refresh_adjacency_cache(self):
        """Carica il grafo in memoria (da chiamare dopo scritture)."""
        logger.info("🔄 Aggiornamento adjacency cache in memoria...")
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT source, target FROM edges
            """)
            self._adjacency_cache.clear()
            for source, target in cursor.fetchall():
                self._adjacency_cache[source].add(target)
                self._adjacency_cache[target].add(source)  # Grafo non orientato
            self._cache_dirty = False
            logger.info(f"✅ Cache caricata: {len(self._adjacency_cache)} nodi")
    
    def get_neighbors(self, node_id: str) -> Set[str]:
        """Ottiene vicini da cache in memoria (0.5ms)."""
        if self._cache_dirty:
            self._refresh_adjacency_cache()
        return self._adjacency_cache.get(node_id, set())
    
    def bfs_subgraph_cte(self, start_node: str, max_depth: int = 2) -> Tuple[List[Dict], List[Dict]]:
        """
        Esegue BFS usando Recursive CTE di SQLite (ZERO round-trip Python).
        Restituisce nodi e archi del sotto-grafo.
        """
        with self.get_cursor() as cursor:
            # Query CTE ricorsiva nativa
            cte_query = """
            WITH RECURSIVE bfs(node_id, depth, path) AS (
                -- Caso base: nodo iniziale
                SELECT ?, 0, ?
                UNION ALL
                -- Passo ricorsivo: espandi vicini
                SELECT 
                    CASE WHEN e.source = b.node_id THEN e.target ELSE e.source END,
                    b.depth + 1,
                    b.path || ',' || CASE WHEN e.source = b.node_id THEN e.target ELSE e.source END
                FROM edges e
                JOIN bfs b ON (e.source = b.node_id OR e.target = b.node_id)
                WHERE b.depth < ?
                  AND b.path NOT LIKE '%,' || CASE WHEN e.source = b.node_id THEN e.target ELSE e.source END || ',%'
            )
            SELECT DISTINCT node_id, depth FROM bfs
            """
            
            cursor.execute(cte_query, (start_node, start_node, max_depth))
            visited_nodes = {row[0]: row[1] for row in cursor.fetchall()}
            
            # Recupera dettagli nodi
            if not visited_nodes:
                return [], []
            
            placeholders = ','.join('?' * len(visited_nodes))
            nodes_query = f"""
                SELECT id, label, primary_label, hemisphere, category, layer_level, summary
                FROM nodes
                WHERE id IN ({placeholders})
            """
            cursor.execute(nodes_query, list(visited_nodes.keys()))
            nodes = [
                {
                    "id": row[0],
                    "label": row[1],
                    "primary_label": row[2],
                    "hemisphere": row[3],
                    "category": row[4],
                    "layer_level": row[5],
                    "summary": row[6],
                    "depth": visited_nodes[row[0]]
                }
                for row in cursor.fetchall()
            ]
            
            # Recupera archi tra i nodi visitati
            edges_query = f"""
                SELECT source, target, relation, confidence
                FROM edges
                WHERE source IN ({placeholders}) AND target IN ({placeholders})
            """
            params = list(visited_nodes.keys()) * 2
            cursor.execute(edges_query, params)
            edges = [
                {"source": row[0], "target": row[1], "relation": row[2], "confidence": row[3]}
                for row in cursor.fetchall()
            ]
            
            return nodes, edges
    
    def shortest_path_cte(self, start: str, end: str) -> Optional[List[str]]:
        """
        Trova il cammino minimo usando BFS in memoria (cache adjacency list).
        Molto più efficiente per grafi piccoli/medi (<10000 nodi).
        Restituisce la lista di nodi nel percorso o None se nessun path.
        """
        # Assicura che la cache sia caricata
        if self._cache_dirty:
            self._refresh_adjacency_cache()
        
        if start not in self._adjacency_cache or end not in self._adjacency_cache:
            return None
        
        # BFS standard in memoria
        from collections import deque
        queue = deque([(start, [start])])
        visited = {start}
        
        while queue:
            current, path = queue.popleft()
            
            if current == end:
                return path
            
            for neighbor in self._adjacency_cache.get(current, set()):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def bulk_ingest(self, nodes: List[Dict], edges: List[Dict]) -> Tuple[int, int]:
        """
        Inserimento massivo con executemany (5-10x più veloce).
        Gestisce duplicati con INSERT OR REPLACE.
        """
        import json
        nodes_inserted = 0
        edges_inserted = 0
        
        with self.get_cursor() as cursor:
            # Bulk insert nodi
            if nodes:
                node_data = [
                    (
                        n["id"], n["label"], n.get("hemisphere", "LEFT"),
                        n.get("primary_label", "CONCEPT"), n.get("category", "GENERAL"),
                        n.get("layer_level", 2), n.get("summary", ""),
                        json.dumps(n.get("details", {})),  # Serializza dict in JSON
                        datetime.now().isoformat(),  # created_at
                        datetime.now().isoformat(),  # updated_at
                        n.get("confidence", "EXTRACTED"),
                        n.get("parent_graph_id", "root")
                    )
                    for n in nodes
                ]
                
                cursor.executemany("""
                    INSERT OR REPLACE INTO nodes 
                    (id, label, hemisphere, primary_label, category, layer_level, 
                     summary, details, created_at, updated_at, confidence, parent_graph_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, node_data)
                nodes_inserted = len(node_data)
            
            # Bulk insert archi
            if edges:
                edge_data = [
                    (
                        e["source"], e["target"], e.get("relation", "RELATED_TO"),
                        datetime.now().isoformat(),
                        e.get("confidence", "EXTRACTED"),
                        ""  # reasoning vuoto di default
                    )
                    for e in edges
                ]
                
                cursor.executemany("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, created_at, confidence, reasoning)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, edge_data)
                edges_inserted = len(edge_data)
        
        # Invalida cache dopo scrittura
        self._cache_dirty = True
        
        logger.info(f"✅ Bulk ingest: {nodes_inserted} nodi, {edges_inserted} archi")
        return nodes_inserted, edges_inserted
    
    @lru_cache(maxsize=128)
    def get_node_by_id_cached(self, node_id: str) -> Optional[Dict]:
        """Cache LRU per lookup nodi frequenti."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT id, label, primary_label, hemisphere, category, 
                       layer_level, summary, details, confidence
                FROM nodes WHERE id = ?
            """, (node_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0], "label": row[1], "primary_label": row[2],
                    "hemisphere": row[3], "category": row[4], "layer_level": row[5],
                    "summary": row[6], "details": row[7], "confidence": row[8]
                }
            return None
    
    def get_full_graph_stats(self) -> Dict[str, Any]:
        """Ottiene statistiche rapide del grafo."""
        with self.get_cursor() as cursor:
            stats = {}
            
            cursor.execute("SELECT COUNT(*) FROM nodes")
            stats["total_nodes"] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM edges")
            stats["total_edges"] = cursor.fetchone()[0]
            
            cursor.execute("""
                SELECT hemisphere, COUNT(*) 
                FROM nodes GROUP BY hemisphere
            """)
            stats["nodes_by_hemisphere"] = dict(cursor.fetchall())
            
            cursor.execute("""
                SELECT primary_label, COUNT(*) 
                FROM nodes 
                GROUP BY primary_label 
                ORDER BY COUNT(*) DESC 
                LIMIT 10
            """)
            stats["top_labels"] = [
                {"label": row[0], "count": row[1]} 
                for row in cursor.fetchall()
            ]
            
            # Recupera un nodo di esempio per i benchmark
            cursor.execute("SELECT id FROM nodes LIMIT 1")
            row = cursor.fetchone()
            stats["sample_node_id"] = row[0] if row else None
            
            return stats
    
    def close(self):
        """Chiude connessione pulitamente."""
        if self.conn:
            self.conn.close()
            logger.info("🔒 Connessione database chiusa")


# Factory function per creare istanza
def create_optimized_brain_db(db_path: str = "universal_brain.db") -> OptimizedBrainDB:
    """Factory per creare istanza ottimizzata del database."""
    return OptimizedBrainDB(db_path)
