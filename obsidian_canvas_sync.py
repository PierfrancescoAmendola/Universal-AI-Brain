#!/usr/bin/env python3
"""
Obsidian Canvas Bidirectional Sync Engine - Universal AI Brain
==============================================================
Sincronizza in modo bidirezionale il Connettoma Cognitivo (SQLite WAL)
con il formato visivo infinito a schede di Obsidian Canvas (.canvas).

Caratteristiche:
1. Esportazione con Layout Bi-Emisferico Spaziale:
   - Emisfero Sinistro a sinistra (X < 0, colore Ciano).
   - Emisfero Destro a destra (X > 0, colore Magenta).
   - Archi e ponti del Corpo Calloso collegati con etichette di relazione.
2. Importazione bidirezionale da Canvas modificati a mano verso SQLite.
3. 100% Zero Dipendenze Esterne (Pure Python Standard Library).
"""

import sys
import os
import json
import sqlite3
import hashlib
import argparse
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Optional, Set

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))
DEFAULT_CANVAS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "obsidian_vault", "00_CONNETOMA_CANVAS.canvas")


def export_brain_to_canvas(db_path: str = DEFAULT_DB_PATH, canvas_path: str = DEFAULT_CANVAS_PATH, limit_nodes: int = 150) -> Dict[str, Any]:
    """Esporta i nodi e le sinapsi del connettoma in un file .canvas per Obsidian."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database {db_path} non trovato.")

    os.makedirs(os.path.dirname(canvas_path), exist_ok=True)

    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")

    with conn:
        # Seleziona i nodi principali (P0, P1 e P2 più connessi)
        nodes_rows = conn.execute("""
            SELECT n.id, n.label, n.hemisphere, n.primary_label, n.category, n.summary, n.tags, n.layer_level,
                   (
                       (SELECT COUNT(*) FROM edges WHERE source = n.id) +
                       (SELECT COUNT(*) FROM edges WHERE target = n.id)
                   ) AS degree
            FROM nodes n
            ORDER BY n.layer_level ASC, degree DESC
            LIMIT ?
        """, (limit_nodes,)).fetchall()

        all_node_ids = {r["id"] for r in nodes_rows}
        placeholders = ",".join("?" for _ in all_node_ids)
        
        edges_rows = conn.execute(f"""
            SELECT source, target, relation
            FROM edges
            WHERE source IN ({placeholders}) AND target IN ({placeholders})
        """, list(all_node_ids) * 2).fetchall()

    canvas_nodes = []
    canvas_edges = []

    # Layout spaziale Bi-Emisferico
    left_y = 0
    right_y = 0
    card_width = 300
    card_height = 140
    gap_y = 170

    for r in nodes_rows:
        nid = r["id"]
        hemi = r["hemisphere"]
        label = r["label"]
        pl = r["primary_label"]
        summary = (r["summary"] or "")[:140]
        layer = r["layer_level"]

        if hemi == "LEFT":
            x = -450 if layer == 1 else (-800 if layer == 2 else -150)
            y = left_y
            left_y += gap_y
            color = "4"  # Ciano / Blu in Obsidian Canvas
            hemi_icon = "⚡"
        else:
            x = 450 if layer == 1 else (800 if layer == 2 else 150)
            y = right_y
            right_y += gap_y
            color = "1"  # Rosso / Magenta in Obsidian Canvas
            hemi_icon = "🌸"

        markdown_body = f"### {hemi_icon} {label}\n`{pl}` · `P{layer}`\n\n> {summary}"

        canvas_nodes.append({
            "id": nid,
            "type": "text",
            "text": markdown_body,
            "x": x,
            "y": y,
            "width": card_width,
            "height": card_height,
            "color": color
        })

    for e in edges_rows:
        edge_id = hashlib.md5(f"{e['source']}->{e['target']}->{e['relation']}".encode("utf-8")).hexdigest()[:10]
        is_callosum = (e["relation"] == "CORPUS_CALLOSUM_LINK")
        canvas_edges.append({
            "id": edge_id,
            "fromNode": e["source"],
            "toNode": e["target"],
            "label": e["relation"],
            "color": "6" if is_callosum else "3"
        })

    canvas_data = {
        "nodes": canvas_nodes,
        "edges": canvas_edges
    }

    with open(canvas_path, "w", encoding="utf-8") as f:
        json.dump(canvas_data, f, indent=2, ensure_ascii=False)

    print(f"🎨 Obsidian Canvas generato con successo in: {canvas_path}")
    print(f"  • Schede visive esportate: {len(canvas_nodes)}")
    print(f"  • Connessioni grafiche:     {len(canvas_edges)}")

    return {
        "status": "success",
        "nodes_count": len(canvas_nodes),
        "edges_count": len(canvas_edges),
        "canvas_file": canvas_path
    }


def import_canvas_to_brain(canvas_path: str = DEFAULT_CANVAS_PATH, db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """Importa modifiche e nuovi archi tracciati visivamente in Obsidian Canvas verso SQLite."""
    if not os.path.exists(canvas_path):
        raise FileNotFoundError(f"File Canvas non trovato in {canvas_path}")

    with open(canvas_path, "r", encoding="utf-8") as f:
        canvas_data = json.load(f)

    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")

    new_edges_count = 0
    now = datetime.now(timezone.utc).isoformat()

    with conn:
        existing_nodes = {r[0] for r in conn.execute("SELECT id FROM nodes").fetchall()}
        
        for edge in canvas_data.get("edges", []):
            src = edge.get("fromNode")
            tgt = edge.get("toNode")
            rel = (edge.get("label") or "CANVAS_CONNECTED").strip().upper().replace(" ", "_")

            if src in existing_nodes and tgt in existing_nodes:
                conn.execute("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, ?, 'EXTRACTED', 'Disegnato su Obsidian Canvas', ?)
                """, (src, tgt, rel, now))
                new_edges_count += 1

    print(f"📥 Canvas Import: {new_edges_count} connessioni aggiornate/importate in SQLite.")
    return {
        "status": "success",
        "synapses_synced": new_edges_count
    }


def main():
    parser = argparse.ArgumentParser(description="Obsidian Canvas Sync Engine")
    parser.add_argument("--export", action="store_true", help="Esporta il connettoma in file .canvas")
    parser.add_argument("--import-canvas", action="store_true", help="Importa le modifiche dal file .canvas a SQLite")
    parser.add_argument("--canvas", default=DEFAULT_CANVAS_PATH, help="Percorso del file .canvas")
    parser.add_argument("--db", default=DEFAULT_DB_PATH, help="Percorso database SQLite")
    args = parser.parse_args()

    if args.import_canvas:
        import_canvas_to_brain(args.canvas, args.db)
    else:
        export_brain_to_canvas(args.db, args.canvas)


if __name__ == "__main__":
    main()
