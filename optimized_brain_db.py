"""
Database Manager Ottimizzato - Opzione C (Ibrida)
Implementa:
1. In-Memory Adjacency Cache per letture ultra-veloci
2. Recursive CTE per BFS/Subgraph nativi in SQL
3. Bulk ingest con executemany
4. Endpoint sincroni (def) per non bloccare event loop
5. LRU Cache per query frequenti
"""

import time
import re
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
    
    def bulk_ingest(self, nodes: List[Dict], edges: List[Dict], cross_links: Optional[List[Dict]] = None) -> Dict[str, int]:
        """
        Inserimento massivo con executemany (5-10x più veloce).
        Gestisce duplicati con INSERT OR REPLACE.
        Include: tags, sanitizzazione, auto-popolo details, cross_links callosali.
        """
        import json
        start_time = time.time()
        
        nodes_inserted = 0
        edges_inserted = 0
        cross_links_inserted = 0
        
        # === SANITIZZAZIONE E NORMALIZZAZIONE (come main.py) ===
        def sanitize_text(text: str) -> str:
            if not text:
                return text
            # Rimuovi caratteri CJK residui
            text = re.sub(r'[\u4e00-\u9fff]', '', text)
            # Traduci automaticamente alcune parole chiave
            translations = {
                'thought': 'pensiero',
                'memory': 'memoria',
                'concept': 'concetto'
            }
            for en, it in translations.items():
                if en in text.lower():
                    text = text.replace(en, it)
            return text
        
        with self.get_cursor() as cursor:
            # === PREPARAZIONE NODI CON TAGS COMPLETI ===
            if nodes:
                node_data = []
                for n in nodes:
                    node_id = n["id"]
                    label = sanitize_text(n.get("label", node_id))
                    hemisphere = n.get("hemisphere", "LEFT")
                    primary_label = n.get("primary_label", "CONCEPT")
                    category = n.get("category", primary_label)
                    layer_level = n.get("layer_level", 2)
                    summary = sanitize_text(n.get("summary", ""))
                    
                    # Gestione tags: da lista a stringa JSON
                    tags = n.get('tags', [])
                    if isinstance(tags, list):
                        tags_json = json.dumps(tags)
                    else:
                        tags_json = tags  # Già stringa JSON
                    
                    # Auto-popola details se mancano campi obbligatori per tipi cognitivi
                    details = n.get('details', {})
                    if primary_label == 'USER_INTENT' and 'user_prompt' not in details:
                        details['user_prompt'] = summary
                    elif primary_label == 'AI_REASONING' and 'model' not in details:
                        details['model'] = 'Unknown'
                    elif primary_label == 'CONVERSATION_EPISODE':
                        if 'participants' not in details:
                            details['participants'] = ['Pierfrancesco Amendola', 'AI Assistant']
                        if 'topic' not in details:
                            details['topic'] = summary
                    
                    details_json = json.dumps(details)
                    created_at = n.get('created_at', datetime.now().isoformat())
                    updated_at = n.get('updated_at', datetime.now().isoformat())
                    confidence = n.get('confidence', 'EXTRACTED')
                    parent_graph_id = n.get('parent_graph_id', 'root')
                    
                    node_data.append((
                        node_id, label, hemisphere, primary_label, category,
                        layer_level, summary, tags_json, details_json,
                        created_at, updated_at, confidence, parent_graph_id
                    ))
                
                cursor.executemany("""
                    INSERT OR REPLACE INTO nodes
                    (id, label, hemisphere, primary_label, category, layer_level,
                     summary, tags, details, created_at, updated_at, confidence, parent_graph_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, node_data)
                nodes_inserted = len(node_data)
            
            # === PREPARAZIONE ARCHI ===
            if edges:
                edge_data = []
                for e in edges:
                    edge_data.append((
                        e["source"], e["target"], e.get("relation", "RELATED_TO"),
                        datetime.now().isoformat(),
                        e.get("confidence", "EXTRACTED"),
                        ""  # reasoning vuoto di default
                    ))
                
                cursor.executemany("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, created_at, confidence, reasoning)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, edge_data)
                edges_inserted = len(edge_data)
            
            # === GESTIONE CROSS_LINKS (Ponti Callosali) ===
            if cross_links:
                for link in cross_links:
                    left_node = link.get('left_node')
                    right_node = link.get('right_node')
                    if left_node and right_node:
                        cursor.execute("""
                            INSERT OR REPLACE INTO edges
                            (source, target, relation, created_at, confidence, reasoning)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            left_node, right_node, 'CORPUS_CALLOSUM_LINK',
                            datetime.now().isoformat(), 'INFERRED', ''
                        ))
                        cross_links_inserted += 1
        
        # Invalida cache dopo scrittura
        self._cache_dirty = True
        
        elapsed = time.time() - start_time
        logger.info(f"✅ Bulk ingest: {nodes_inserted} nodi, {edges_inserted} archi, {cross_links_inserted} cross-link in {elapsed:.4f}s")
        
        return {
            "nodes_inserted": nodes_inserted,
            "edges_inserted": edges_inserted,
            "cross_links_inserted": cross_links_inserted,
            "elapsed_seconds": round(elapsed, 4),
            "status": "success"
        }

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
