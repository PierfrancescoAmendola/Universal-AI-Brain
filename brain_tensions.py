#!/usr/bin/env python3
"""
Tensions & Contradictions Detector - Universal AI Brain
======================================================
Identifica, gestisce e risolve attivamente le tensioni cognitive,
i compromessi (trade-offs), i paradossi e le contraddizioni tra nodi del connettoma.

Caratteristiche:
1. Rilevamento semantico di concetti o principi polarizzanti/opposti.
2. Memorizzazione persistente nella tabella `tensions` e archi `TENSION_CONTRADICTION`.
3. Strategie di risoluzione guidate:
   - 'MERGE_AI': Sintesi hegeliana automatica (Tesi + Antitesi ➔ Sintesi).
   - 'RECONCILE_MANUAL': Risoluzione esplicita fornita dall'utente.
   - 'STEELMAN': Rafforzamento contestuale di entrambe le posizioni (in quali condizioni vale A e in quali B).
   - 'FALSE_POSITIVE': Segna come non in conflitto.
   - 'IGNORED': Archivia senza azione.
"""

import os
import re
import json
import sqlite3
import hashlib
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


def init_tensions_schema(conn: sqlite3.Connection):
    """Inizializza la tabella tensions e gli indici se non esistono."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tensions (
            id TEXT PRIMARY KEY,
            node_a_id TEXT NOT NULL,
            node_b_id TEXT NOT NULL,
            tension_type TEXT NOT NULL DEFAULT 'CONTRADICTION',
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'OPEN',
            resolution_strategy TEXT,
            resolution_notes TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            resolved_at TEXT,
            FOREIGN KEY (node_a_id) REFERENCES nodes(id) ON DELETE CASCADE,
            FOREIGN KEY (node_b_id) REFERENCES nodes(id) ON DELETE CASCADE
        );
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tensions_status ON tensions(status);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tensions_nodes ON tensions(node_a_id, node_b_id);")
    conn.commit()


@contextmanager
def get_db_connection(db_path: str = DEFAULT_DB_PATH):
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    init_tensions_schema(conn)
    try:
        yield conn
    finally:
        conn.close()



def generate_tension_id(node_a_id: str, node_b_id: str, tension_type: str) -> str:
    """Genera un ID deterministico per una tensione tra due nodi."""
    pair = sorted([node_a_id, node_b_id])
    raw = f"{pair[0]}:{pair[1]}:{tension_type}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return f"tension-{digest}"


def create_or_update_tension(
    node_a_id: str,
    node_b_id: str,
    tension_type: str = "CONTRADICTION",
    description: str = "",
    status: str = "OPEN",
    db_path: str = DEFAULT_DB_PATH
) -> Dict[str, Any]:
    """Crea o aggiorna una tensione cognitiva tra due nodi."""
    with get_db_connection(db_path) as conn:
        # Verifica esistenza dei nodi
        cur = conn.execute("SELECT id FROM nodes WHERE id IN (?, ?)", (node_a_id, node_b_id))
        found_ids = {row["id"] for row in cur.fetchall()}
        if node_a_id not in found_ids or node_b_id not in found_ids:
            return {
                "status": "error",
                "message": f"Uno o entrambi i nodi non esistono ({node_a_id}, {node_b_id})"
            }
            
        t_id = generate_tension_id(node_a_id, node_b_id, tension_type)
        now = datetime.now(timezone.utc).isoformat()
        
        conn.execute("""
            INSERT INTO tensions (id, node_a_id, node_b_id, tension_type, description, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                description = excluded.description,
                status = CASE WHEN tensions.status = 'RESOLVED' THEN tensions.status ELSE excluded.status END;
        """, (t_id, node_a_id, node_b_id, tension_type, description, status, now))
        
        # Crea anche l'arco bidirezionale TENSION_CONTRADICTION nel grafo
        conn.execute("""
            INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning)
            VALUES (?, ?, 'TENSION_CONTRADICTION', 'INFERRED', ?);
        """, (node_a_id, node_b_id, description))
        
        conn.commit()
        return {
            "status": "success",
            "tension_id": t_id,
            "node_a_id": node_a_id,
            "node_b_id": node_b_id,
            "tension_type": tension_type,
            "description": description
        }


def get_tensions(
    status: Optional[str] = None,
    limit: int = 50,
    db_path: str = DEFAULT_DB_PATH
) -> List[Dict[str, Any]]:
    """Recupera le tensioni registrate con i dettagli completi dei due nodi coinvolti."""
    with get_db_connection(db_path) as conn:
        query = """
            SELECT 
                t.*,
                na.label as node_a_label,
                na.hemisphere as node_a_hemisphere,
                na.summary as node_a_summary,
                na.primary_label as node_a_type,
                nb.label as node_b_label,
                nb.hemisphere as node_b_hemisphere,
                nb.summary as node_b_summary,
                nb.primary_label as node_b_type
            FROM tensions t
            LEFT JOIN nodes na ON t.node_a_id = na.id
            LEFT JOIN nodes nb ON t.node_b_id = nb.id
        """
        params = []
        if status:
            query += " WHERE t.status = ?"
            params.append(status)
            
        query += " ORDER BY t.created_at DESC LIMIT ?"
        params.append(limit)
        
        rows = conn.execute(query, tuple(params)).fetchall()
        return [dict(r) for r in rows]


def resolve_tension(
    tension_id: str,
    strategy: str,
    resolution_notes: str,
    db_path: str = DEFAULT_DB_PATH
) -> Dict[str, Any]:
    """
    Risolve una tensione cognitiva archiviando la sintesi / decisione.
    Strategie valide: MERGE_AI, RECONCILE_MANUAL, STEELMAN, FALSE_POSITIVE, IGNORED.
    """
    valid_strategies = {"MERGE_AI", "RECONCILE_MANUAL", "STEELMAN", "FALSE_POSITIVE", "IGNORED"}
    if strategy not in valid_strategies:
        return {"status": "error", "message": f"Strategia non valida. Scegli tra: {valid_strategies}"}
        
    with get_db_connection(db_path) as conn:
        row = conn.execute("SELECT * FROM tensions WHERE id = ?", (tension_id,)).fetchone()
        if not row:
            return {"status": "error", "message": f"Tensione {tension_id} non trovata"}
            
        status = "FALSE_POSITIVE" if strategy == "FALSE_POSITIVE" else ("IGNORED" if strategy == "IGNORED" else "RESOLVED")
        now = datetime.now(timezone.utc).isoformat()
        
        conn.execute("""
            UPDATE tensions 
            SET status = ?, resolution_strategy = ?, resolution_notes = ?, resolved_at = ?
            WHERE id = ?
        """, (status, strategy, resolution_notes, now, tension_id))
        
        # Se risolto con sintesi hegeliana o manuale, possiamo aggiornare il reasoning dell'arco
        if status == "RESOLVED":
            conn.execute("""
                UPDATE edges
                SET reasoning = ?
                WHERE relation = 'TENSION_CONTRADICTION' AND (
                    (source = ? AND target = ?) OR (source = ? AND target = ?)
                )
            """, (f"Risolto ({strategy}): {resolution_notes}", row["node_a_id"], row["node_b_id"], row["node_b_id"], row["node_a_id"]))
            
        conn.commit()
        return {
            "status": "success",
            "tension_id": tension_id,
            "strategy": strategy,
            "new_status": status,
            "resolution_notes": resolution_notes
        }


# Coppie di concetti/tag dialettici polari per il rilevatore euristico
DIALECTICAL_POLARITIES = [
    ({"premature", "optimization", "clean-code", "refactor"}, {"speed", "mvp", "shipping", "fast", "hack"}),
    ({"centralized", "monolith", "unified"}, {"distributed", "microservices", "modular", "decoupled"}),
    ({"deterministic", "strict", "exact", "type-safe"}, {"probabilistic", "dynamic", "flexible", "fuzzy"}),
    ({"internal-drive", "burning-desire", "willpower"}, {"mimetic", "social-proof", "external-cue", "desire"}),
    ({"cost-reduction", "frugal", "lean"}, {"scale-at-all-costs", "growth", "aggressive"}),
    ({"top-down", "hierarchical", "governance"}, {"bottom-up", "emergent", "grassroots"}),
    ({"immutable", "stateless", "pure"}, {"stateful", "mutable", "reactive"})
]


def detect_candidate_tensions(db_path: str = DEFAULT_DB_PATH, limit: int = 15) -> List[Dict[str, Any]]:
    """
    Analizza i nodi del connettoma alla ricerca di potenziali contraddizioni o compromessi non ancora catalogati.
    Combina l'analisi dei tag, le relazioni semantiche e le coppie polari.
    """
    with get_db_connection(db_path) as conn:
        nodes = [dict(r) for r in conn.execute("SELECT id, label, hemisphere, primary_label, tags, summary FROM nodes").fetchall()]
        existing_tensions = {f"{r['node_a_id']}:{r['node_b_id']}" for r in conn.execute("SELECT node_a_id, node_b_id FROM tensions").fetchall()}
        existing_tensions.update({f"{r['node_b_id']}:{r['node_a_id']}" for r in conn.execute("SELECT node_a_id, node_b_id FROM tensions").fetchall()})
        
        candidates: List[Dict[str, Any]] = []
        
        # Parsifica i tag per ogni nodo
        node_tags_map = {}
        for n in nodes:
            raw_tags = n.get("tags")
            tags_set = set()
            if raw_tags:
                try:
                    loaded = json.loads(raw_tags) if isinstance(raw_tags, str) else list(raw_tags)
                    tags_set = {re.sub(r'^[\[\'"]+|[\]\'"]+$', '', str(t)).lower() for t in loaded}
                except Exception:
                    tags_set = {re.sub(r'^[\[\'"]+|[\]\'"]+$', '', t.strip()).lower() for t in str(raw_tags).split(",") if t.strip()}
            # Aggiungi anche parole chiave dalla summary e label
            words = set(re.findall(r'[a-zA-Z0-9_\-]+', (n.get("label", "") + " " + n.get("summary", "")).lower()))
            node_tags_map[n["id"]] = {w for w in tags_set.union(words) if w}
            
        # Trova collisioni dialettiche
        for i in range(len(nodes)):
            if len(candidates) >= limit:
                break
            n_a = nodes[i]
            words_a = node_tags_map[n_a["id"]]
            
            for j in range(i + 1, len(nodes)):
                n_b = nodes[j]
                if n_a["id"] == n_b["id"]:
                    continue
                pair_key = f"{n_a['id']}:{n_b['id']}"
                if pair_key in existing_tensions:
                    continue
                    
                words_b = node_tags_map[n_b["id"]]
                
                # Controlla polarità dialettiche
                for pol_a, pol_b in DIALECTICAL_POLARITIES:
                    if (words_a & pol_a and words_b & pol_b) or (words_a & pol_b and words_b & pol_a):
                        desc = f"Tensione dialettica rilevata tra '{n_a['label']}' e '{n_b['label']}' (focus opposti: {list(words_a & (pol_a | pol_b))} vs {list(words_b & (pol_a | pol_b))})."
                        candidates.append({
                            "node_a_id": n_a["id"],
                            "node_a_label": n_a["label"],
                            "node_b_id": n_b["id"],
                            "node_b_label": n_b["label"],
                            "tension_type": "TRADE_OFF",
                            "description": desc,
                            "confidence": "INFERRED"
                        })
                        break
                        
        return candidates


if __name__ == "__main__":
    tensions = get_tensions()
    print(f"Tensioni attive nel DB: {len(tensions)}")
    candidates = detect_candidate_tensions(limit=5)
    print(f"Candidate tensioni rilevate: {len(candidates)}")
    for c in candidates:
        print(f"- {c['node_a_label']} <--> {c['node_b_label']}: {c['description']}")
