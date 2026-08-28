#!/usr/bin/env python3
"""
Universal AI Brain - Cloud Sync Engine
Automatically pulls all nodes and edges from the live Render instance
and merges them losslessly into the local SQLite brain.db.
"""

import sys
import json
import sqlite3
import urllib.request
from datetime import datetime, timezone

RENDER_URL = "https://universal-ai-brain.onrender.com/brain.json"
LOCAL_DB = "brain.db"


def sync():
    print(f"📡 Recupero dati live da {RENDER_URL}...")
    try:
        req = urllib.request.Request(
            RENDER_URL, 
            headers={"User-Agent": "UniversalBrainSync/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"⚠️ Impossibile contattare Render ({e}). Uso il database locale.")
        return False

    nodes = data.get("nodes", [])
    links = data.get("links", [])
    print(f"📦 Trovati su Render: {len(nodes)} nodi e {len(links)} archi.")

    conn = sqlite3.connect(LOCAL_DB)
    now = datetime.now(timezone.utc).isoformat()
    nodes_upserted = 0
    edges_upserted = 0

    for n in nodes:
        slug = n["id"]
        label = n["label"]
        hemi = n.get("hemisphere", "LEFT")
        pl = n.get("primary_label", n.get("category", "ARCHITECTURE"))
        cat = n.get("category", pl)
        tags_str = json.dumps(n.get("tags", []))
        summary = n.get("summary", "")
        details_str = json.dumps(n.get("details", {}))
        created_at = n.get("created_at", now)
        updated_at = n.get("updated_at", now)
        confidence = n.get("confidence", "EXTRACTED")
        parent_graph_id = n.get("parent_graph_id", "root")
        layer_level = n.get("layer_level", 0)

        conn.execute("""
            INSERT OR REPLACE INTO nodes 
            (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (slug, label, hemi, pl, cat, tags_str, summary, details_str, confidence, parent_graph_id, layer_level, created_at, updated_at))
        nodes_upserted += 1

    for l in links:
        src = l["source"]
        tgt = l["target"]
        rel = l.get("relation", "CONNECTS_TO")
        edge_conf = l.get("confidence", "EXTRACTED")
        edge_reason = l.get("reasoning", None)
        conn.execute("""
            INSERT OR REPLACE INTO edges 
            (source, target, relation, confidence, reasoning, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (src, tgt, rel, edge_conf, edge_reason, now))
        edges_upserted += 1

    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
    conn.close()

    conn2 = sqlite3.connect(LOCAL_DB)
    c_n = conn2.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    c_e = conn2.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    conn2.close()

    print(f"✅ Sincronizzazione completata! brain.db locale aggiornato: {c_n} nodi, {c_e} archi.")
    return True


if __name__ == "__main__":
    sync()
