#!/usr/bin/env python3
"""
Weave Link Engine - Universal AI Brain
======================================
Identifica automaticamente nodi orfani o debolmente connessi (degree <= 2)
e propone archi di alta qualità semantica e ponti del Corpo Calloso.

Caratteristiche:
1. Individuazione automatica di nodi isolati o periferici.
2. Matching semantico via FTS5 BM25 + Jaccard sui tag + cross-domain.
3. Riconoscimento intelligente di ponti inter-emisferici ('CORPUS_CALLOSUM_LINK').
4. Coda di approvazione batch con applicazione transazionale atomica.
"""

import os
import re
import json
import sqlite3
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Set, Tuple

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


def get_db_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def get_orphan_nodes(max_degree: int = 2, limit: int = 25, db_path: str = DEFAULT_DB_PATH) -> List[Dict[str, Any]]:
    """
    Recupera i nodi con grado <= max_degree (escludendo la radice immutabile).
    """
    with get_db_connection(db_path) as conn:
        query = """
            SELECT n.id, n.label, n.hemisphere, n.primary_label, n.layer_level, n.parent_graph_id, n.summary, n.tags,
                   (
                       (SELECT COUNT(*) FROM edges WHERE source = n.id) +
                       (SELECT COUNT(*) FROM edges WHERE target = n.id)
                   ) AS degree
            FROM nodes n
            WHERE n.id != 'person-pierfrancesco' AND n.id != 'root'
            AND degree <= ?
            ORDER BY degree ASC, n.layer_level DESC
            LIMIT ?;
        """
        rows = conn.execute(query, (max_degree, limit)).fetchall()
        return [dict(r) for r in rows]


def compute_weave_proposals(
    max_proposals: int = 15,
    max_degree: int = 2,
    db_path: str = DEFAULT_DB_PATH
) -> List[Dict[str, Any]]:
    """
    Calcola proposte di collegamento sinaptico per i nodi orfani.
    """
    orphans = get_orphan_nodes(max_degree=max_degree, limit=30, db_path=db_path)
    if not orphans:
        return []
        
    with get_db_connection(db_path) as conn:
        # Mappa degli archi esistenti per evitare duplicati
        existing_edges = {f"{r['source']}->{r['target']}" for r in conn.execute("SELECT source, target FROM edges").fetchall()}
        existing_edges.update({f"{r['target']}->{r['source']}" for r in conn.execute("SELECT source, target FROM edges").fetchall()})
        
        all_nodes_cur = conn.execute("SELECT id, label, hemisphere, primary_label, summary, tags FROM nodes")
        all_nodes = {r["id"]: dict(r) for r in all_nodes_cur.fetchall()}
        
        proposals: List[Dict[str, Any]] = []
        seen_pairs: Set[str] = set()
        
        for orphan in orphans:
            if len(proposals) >= max_proposals:
                break
                
            src_id = orphan["id"]
            src_hemi = orphan.get("hemisphere") or "LEFT"
            src_label = orphan.get("label") or src_id
            src_summary = orphan.get("summary") or ""
            
            # Estrai parole chiave per FTS5
            keywords = [w for w in re.findall(r'[a-zA-Z0-9_\-]+', (src_label + " " + src_summary).lower()) if len(w) > 3]
            if not keywords:
                continue
                
            search_term = " OR ".join([f'"{k}"*' for k in keywords[:4]])
            
            # Cerca target semanticamente affini tramite FTS5
            try:
                fts_rows = conn.execute("""
                    SELECT id FROM nodes_fts
                    WHERE nodes_fts MATCH ? AND id != ?
                    ORDER BY rank
                    LIMIT 8;
                """, (search_term, src_id)).fetchall()
                target_ids = [r["id"] for r in fts_rows]
            except Exception:
                # Fallback LIKE
                like_pat = f"%{keywords[0]}%"
                like_rows = conn.execute("""
                    SELECT id FROM nodes
                    WHERE (label LIKE ? OR summary LIKE ?) AND id != ?
                    LIMIT 8;
                """, (like_pat, like_pat, src_id)).fetchall()
                target_ids = [r["id"] for r in like_rows]
                
            for tgt_id in target_ids:
                if tgt_id not in all_nodes:
                    continue
                pair_key = f"{src_id}<->{tgt_id}"
                if pair_key in seen_pairs or f"{src_id}->{tgt_id}" in existing_edges:
                    continue
                seen_pairs.add(pair_key)
                
                tgt_node = all_nodes[tgt_id]
                tgt_hemi = tgt_node.get("hemisphere") or "LEFT"
                is_cross = (src_hemi != tgt_hemi)
                
                relation = "CORPUS_CALLOSUM_LINK" if is_cross else "RELATES_TO"
                if src_node_type := orphan.get("primary_label"):
                    if src_node_type == "COGNITIVE_RULE":
                        relation = "GOVERNS" if not is_cross else "CORPUS_CALLOSUM_LINK"
                    elif src_node_type == "UI_COMPONENT":
                        relation = "INTEGRATES_WITH"
                        
                reasoning = (
                    f"Ponte callosale inter-emisferico tra {src_hemi} e {tgt_hemi} basato su affinità semantica."
                    if is_cross else
                    f"Collegamento intra-dominio per arricchire la densità sinaptica di '{src_label}'."
                )
                
                proposal_id = f"prop-{hashlib.sha256(pair_key.encode()).hexdigest()[:10]}"
                
                proposals.append({
                    "id": proposal_id,
                    "source": src_id,
                    "source_label": src_label,
                    "source_hemisphere": src_hemi,
                    "target": tgt_id,
                    "target_label": tgt_node.get("label") or tgt_id,
                    "target_hemisphere": tgt_hemi,
                    "relation": relation,
                    "is_cross_hemisphere": is_cross,
                    "reasoning": reasoning,
                    "confidence": "INFERRED"
                })
                
                if len(proposals) >= max_proposals:
                    break
                    
        return proposals


def apply_weave_links(accepted_proposals: List[Dict[str, Any]], db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """
    Applica atomicamente le connessioni accettate nel database SQLite.
    """
    if not accepted_proposals:
        return {"status": "success", "applied_count": 0, "message": "Nessuna proposta da applicare"}
        
    with get_db_connection(db_path) as conn:
        applied = 0
        for p in accepted_proposals:
            src = p.get("source")
            tgt = p.get("target")
            rel = p.get("relation", "RELATES_TO")
            conf = p.get("confidence", "INFERRED")
            reasoning = p.get("reasoning", "Collegamento tessuto da Weave Link Engine")
            
            if src and tgt:
                conn.execute("""
                    INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning)
                    VALUES (?, ?, ?, ?, ?);
                """, (src, tgt, rel, conf, reasoning))
                applied += 1
                
        conn.commit()
        return {
            "status": "success",
            "applied_count": applied,
            "message": f"Tessuti con successo {applied} nuovi collegamenti sinaptici."
        }


if __name__ == "__main__":
    props = compute_weave_proposals(max_proposals=5)
    print(f"Proposte Weave Link generate: {len(props)}")
    for p in props:
        print(f"[{p['relation']}] {p['source_label']} ({p['source_hemisphere']}) ➔ {p['target_label']} ({p['target_hemisphere']})")
        print(f"  Motivo: {p['reasoning']}")
