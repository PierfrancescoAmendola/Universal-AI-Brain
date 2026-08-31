#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Cerca nel Cervello
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🧠
# @raycast.packageName Universal AI Brain
# @raycast.argument1 { "type": "text", "placeholder": "Cerca nel connettoma..." }
# @raycast.argument2 { "type": "text", "placeholder": "Emisfero (LEFT/RIGHT/ALL)", "optional": true }

# Documentation:
# @raycast.description Ricerca ultra-veloce nel connettoma cognitivo bi-emisferico con FTS5 BM25.
# @raycast.author Pierfrancesco Amendola


import sys
import os
import re
import json
import sqlite3
from typing import List, Dict, Any, Optional

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.expanduser("~/Desktop/CervelloArtificiale/brain.db"))


def get_db_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    if not os.path.exists(db_path):
        print(f"❌ Errore: Database del Cervello non trovato in `{db_path}`")
        sys.exit(1)
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA query_only=ON;")
    return conn


def search_brain(query: str, hemisphere_filter: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
    """Esegue una ricerca FTS5 ad alte prestazioni su nodi e metadati."""
    q_clean = query.strip()
    if not q_clean:
        return []

    hemi = hemisphere_filter.upper().strip() if hemisphere_filter else None
    if hemi not in ("LEFT", "RIGHT"):
        hemi = None

    with get_db_connection() as conn:
        cursor = conn.cursor()
        # 1. Prova con FTS5 BM25 Match
        fts_query = re.sub(r'[^\w\s-]', '', q_clean).strip()
        results = []

        if fts_query:
            try:
                # Match su tabella FTS5 se presente
                fts_tokens = fts_query.split()
                fts_match_expr = " OR ".join([f'"{token}"*' for token in fts_tokens])
                
                sql = """
                    SELECT n.id, n.label, n.hemisphere, n.primary_label, n.category, n.layer_level,
                           n.summary, n.tags, n.parent_graph_id, n.confidence, n.updated_at
                    FROM nodes_fts f
                    JOIN nodes n ON f.id = n.id
                    WHERE nodes_fts MATCH ?
                """
                params = [fts_match_expr]
                if hemi:
                    sql += " AND n.hemisphere = ?"
                    params.append(hemi)
                sql += " ORDER BY rank LIMIT ?"
                params.append(limit)

                cursor.execute(sql, params)
                results = [dict(r) for r in cursor.fetchall()]
            except Exception:
                results = []

        # 2. Fallback con LIKE se FTS5 non produce risultati o fallisce
        if not results:
            like_pattern = f"%{q_clean}%"
            sql = """
                SELECT id, label, hemisphere, primary_label, category, layer_level,
                       summary, tags, parent_graph_id, confidence, updated_at
                FROM nodes
                WHERE (label LIKE ? OR summary LIKE ? OR id LIKE ? OR tags LIKE ?)
            """
            params = [like_pattern, like_pattern, like_pattern, like_pattern]
            if hemi:
                sql += " AND hemisphere = ?"
                params.append(hemi)
            sql += " ORDER BY layer_level ASC, updated_at DESC LIMIT ?"
            params.append(limit)

            cursor.execute(sql, params)
            results = [dict(r) for r in cursor.fetchall()]

        return results


def format_clean_output(query: str, results: List[Dict[str, Any]], hemi: Optional[str] = None):
    """Formatta i risultati per una visualizzazione pulita, elegante e naturale in Raycast."""
    hemi_info = f" [Filtro: {hemi}]" if hemi else ""
    print(f"🧠 RISULTATI RICERCA: \"{query}\"{hemi_info}")
    print("═" * 58)

    if not results:
        print("\nNessun nodo trovato nel connettoma per questa ricerca.")
        print("Suggerimento: Prova con parole chiave più generiche o senza filtri.")
        return

    print(f"Trovati {len(results)} elementi pertinenti:\n")

    for i, n in enumerate(results, 1):
        hemi_icon = "⚡" if n.get("hemisphere") == "LEFT" else "🌸"
        hemi_label = "Sinistro" if n.get("hemisphere") == "LEFT" else "Destro"
        layer = n.get("layer_level", 2)
        layer_name = "P0 Attico" if layer == 0 else ("P1 Progetto/Episodio" if layer == 1 else "P2 Modulo Atomico")
        
        tags_raw = n.get("tags")
        if isinstance(tags_raw, str):
            try:
                tags_list = json.loads(tags_raw)
            except Exception:
                tags_list = [t.strip() for t in tags_raw.split(",") if t.strip()]
        elif isinstance(tags_raw, list):
            tags_list = tags_raw
        else:
            tags_list = []
        tags_str = " ".join([f"#{t}" for t in tags_list[:5]])
        raw_summary = (n.get("summary") or "Nessuna sintesi disponibile.").strip()
        # Rimuovi eventuali residui di formattazione markdown (**, *, `, #, ecc.)
        clean_summary = re.sub(r'[*_`#>]', '', raw_summary).strip()
        updated = str(n.get("updated_at", "")).split("T")[0]

        print(f"{i}. {hemi_icon} {n.get('label')}")
        print(f"   • Tipo:       Emisfero {hemi_label} ({n.get('primary_label')}) | {layer_name}")
        if tags_str:
            print(f"   • Tag:        {tags_str}")
        print(f"   • Contenuto:  {clean_summary}")
        print(f"   • Riferimento:{n.get('id')} (Parent: {n.get('parent_graph_id')} | Aggiornato: {updated})")
        print("─" * 58)


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("❌ Specifica un termine di ricerca.")
        print("Uso: brain_search.py <query> [LEFT|RIGHT|ALL]")
        sys.exit(1)

    query = sys.argv[1]
    hemi_arg = sys.argv[2] if len(sys.argv) > 2 else None
    
    results = search_brain(query, hemi_arg, limit=10)
    format_clean_output(query, results, hemi_arg)


if __name__ == "__main__":
    main()
