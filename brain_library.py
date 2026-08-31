#!/usr/bin/env python3
"""
Lens & Library Engine - Universal AI Brain
==========================================
Permette il dialogo isolato e rigorosamente 'groundato' con specifici
libri, autori, mentori o cluster concettuali memorizzati nel connettoma.

Caratteristiche:
1. Estrazione del sottografo dell'entità (nodi, sintesi, dettagli e relazioni).
2. Costruzione del system prompt per la persona con divieto di allucinazione.
3. Obbligo di citazione fedele dei nodi sorgente via wikilinks [[node-id]].
"""

import os
import json
import sqlite3
from typing import Dict, Any, List, Optional, Set

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


def get_db_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def list_available_lenses(db_path: str = DEFAULT_DB_PATH) -> List[Dict[str, Any]]:
    """
    Individua le lenti primarie disponibili: Autori, Libri, Progetti cardine e Macro-Domini.
    """
    with get_db_connection(db_path) as conn:
        # Cerca nodi con etichette o tag rilevanti
        query = """
            SELECT n.id, n.label, n.hemisphere, n.primary_label, n.summary, n.tags,
                   (
                       (SELECT COUNT(*) FROM edges WHERE source = n.id) +
                       (SELECT COUNT(*) FROM edges WHERE target = n.id)
                   ) AS degree
            FROM nodes n
            WHERE n.primary_label IN ('ROOT_DOMAIN', 'PROJECT', 'MENTAL_MODEL', 'COGNITIVE_RULE', 'LIFE_LESSON')
               OR n.id LIKE 'book-%' OR n.id LIKE 'author-%' OR n.id LIKE 'mentor-%' OR n.id LIKE 'firmware-%'
               OR n.tags LIKE '%book%' OR n.tags LIKE '%author%' OR n.tags LIKE '%mentor%'
            ORDER BY degree DESC, n.layer_level ASC
            LIMIT 40;
        """
        rows = [dict(r) for r in conn.execute(query).fetchall()]
        return rows


def extract_lens_subgraph(
    lens_id: str,
    max_depth: int = 2,
    db_path: str = DEFAULT_DB_PATH
) -> Dict[str, Any]:
    """
    Estrae il sottografo completo centrato su una lente/entità.
    """
    with get_db_connection(db_path) as conn:
        # Trova il nodo radice della lente (con fallback di ricerca se l'ID non è esatto)
        root_row = conn.execute("SELECT * FROM nodes WHERE id = ?", (lens_id,)).fetchone()
        if not root_row:
            search_like = f"%{lens_id}%"
            root_row = conn.execute(
                "SELECT * FROM nodes WHERE id LIKE ? OR label LIKE ? LIMIT 1",
                (search_like, search_like)
            ).fetchone()
            
        if not root_row:
            return {"status": "error", "message": f"Nessuna lente o entità trovata per '{lens_id}'"}
            
        root_node = dict(root_row)
        root_id = root_node["id"]
        
        visited_nodes: Dict[str, Dict[str, Any]] = {root_id: root_node}
        visited_edges: List[Dict[str, Any]] = []
        current_frontier = {root_id}
        
        for _ in range(max_depth):
            if not current_frontier:
                break
            placeholders = ",".join(["?"] * len(current_frontier))
            edge_query = f"""
                SELECT source, target, relation, confidence, reasoning
                FROM edges
                WHERE source IN ({placeholders}) OR target IN ({placeholders});
            """
            edge_rows = [dict(r) for r in conn.execute(edge_query, list(current_frontier) * 2).fetchall()]
            
            next_frontier: Set[str] = set()
            for e in edge_rows:
                visited_edges.append(e)
                for nid in (e["source"], e["target"]):
                    if nid not in visited_nodes:
                        next_frontier.add(nid)
                        
            if next_frontier:
                node_placeholders = ",".join(["?"] * len(next_frontier))
                new_nodes_rows = conn.execute(
                    f"SELECT * FROM nodes WHERE id IN ({node_placeholders})",
                    list(next_frontier)
                ).fetchall()
                for nr in new_nodes_rows:
                    visited_nodes[nr["id"]] = dict(nr)
                    
            current_frontier = next_frontier
            
        # Deduplica archi
        unique_edges = []
        seen_edge_keys = set()
        for e in visited_edges:
            k = f"{e['source']}->{e['target']}:{e['relation']}"
            if k not in seen_edge_keys:
                seen_edge_keys.add(k)
                unique_edges.append(e)
                
        return {
            "status": "success",
            "lens_id": root_id,
            "lens_label": root_node["label"],
            "hemisphere": root_node.get("hemisphere", "LEFT"),
            "nodes_count": len(visited_nodes),
            "edges_count": len(unique_edges),
            "nodes": list(visited_nodes.values()),
            "edges": unique_edges
        }


def build_lens_dialogue_prompt(
    lens_id_or_keyword: str,
    question: str,
    db_path: str = DEFAULT_DB_PATH
) -> Dict[str, Any]:
    """
    Costruisce il prompt contestuale blindato per dialogare con la lente / autore / libro.
    """
    subgraph = extract_lens_subgraph(lens_id_or_keyword, max_depth=2, db_path=db_path)
    if subgraph.get("status") == "error":
        return subgraph
        
    lens_label = subgraph["lens_label"]
    nodes = subgraph["nodes"]
    
    corpus_blocks = []
    for n in nodes:
        details_txt = ""
        if n.get("details"):
            try:
                d = json.loads(n["details"]) if isinstance(n["details"], str) else n["details"]
                if isinstance(d, dict):
                    details_txt = " | " + ", ".join([f"{k}: {v}" for k, v in d.items() if not isinstance(v, (dict, list))])
            except Exception:
                pass
        corpus_blocks.append(f"- [[{n['id']}]] **{n['label']}** ({n.get('primary_label', 'NODE')}): {n.get('summary', '')}{details_txt}")
        
    corpus_str = "\n".join(corpus_blocks)
    
    dialogue_prompt = f"""
# 📚 LENS & LIBRARY DIALOGUE: {lens_label.upper()}
> Sei la voce e l'essenza incarnata di **{lens_label}**, basata rigorosamente sul Connettoma Cognitivo.
> Rispondi alla domanda dell'utente parlando in prima persona ('Io...') con il tono, il rigore e i principi estratti.
> **REGOLA AUREA:** Ogni affermazione, consiglio o principio deve citare esplicitamente le note sorgente tra doppie quadre (es. [[{subgraph['lens_id']}]]). Non allucinare fatti esterni non presenti nel connettoma.

---

## 🏛️ Corpus Cognitivo Groundato ({len(nodes)} Nodi):
{corpus_str}

---

## ❓ Domanda dell'Utente:
{question}
"""
    return {
        "status": "success",
        "lens_id": subgraph["lens_id"],
        "lens_label": lens_label,
        "nodes_grounded": len(nodes),
        "prompt": dialogue_prompt.strip()
    }


if __name__ == "__main__":
    lenses = list_available_lenses()
    print(f"Lenti disponibili: {len(lenses)}")
    if lenses:
        sample_lens = lenses[0]["id"]
        res = build_lens_dialogue_prompt(sample_lens, "Quali sono i principi chiave che dovrei applicare oggi?")
        print(f"\n--- PROMPT GENERATO PER LENS '{lenses[0]['label']}' ---")
        print(res["prompt"][:500] + "...\n")
