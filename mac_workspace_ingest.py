#!/usr/bin/env python3
"""
Universal AI Brain - Mac Workspace Ingestion Engine (100% Safe & Read-Only Source)
=================================================================================
Scansiona in sola lettura i progetti sul Mac, li trasforma in nodi di conoscenza
strutturati (Piano 1 & Piano 2) e li inserisce in SQLite WAL con indice FTS5 e sinapsi.
"""

import os
import sys
import json
import sqlite3
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(PROJECT_ROOT, "brain.db"))

from mac_workspace_scanner import find_project_roots
from mac_stack_extractor import extract_project_semantics


def ingest_mac_workspace(
    search_paths: Optional[List[str]] = None,
    db_path: str = DEFAULT_DB_PATH,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Esegue la scansione dei progetti sul Mac e li ingerisce atomicamente in SQLite WAL.
    """
    if verbose:
        print("🔍 Scansione progetti Mac in corso...")

    raw_projects = find_project_roots(search_paths=search_paths)
    if verbose:
        print(f"📦 Trovati {len(raw_projects)} progetti. Estrazione semantica in corso...")

    semantic_projects = [extract_project_semantics(p) for p in raw_projects]
    
    now = datetime.now(timezone.utc).isoformat()
    nodes_upserted = 0
    edges_upserted = 0

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")

    try:
        for p in semantic_projects:
            # 1. Inserimento Nodo Progetto (Piano 1)
            details_str = json.dumps(p["details"], ensure_ascii=False)
            tags_str = json.dumps(p["tags"], ensure_ascii=False)

            existing = conn.execute("SELECT created_at FROM nodes WHERE id = ?", (p["id"],)).fetchone()
            created_at = existing["created_at"] if existing else now

            conn.execute("""
                INSERT OR REPLACE INTO nodes (
                    id, label, hemisphere, primary_label, category,
                    layer_level, parent_graph_id, summary, details, tags,
                    confidence, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                p["id"], p["label"], p["hemisphere"], p["primary_label"], p["category"],
                p["layer_level"], p["parent_graph_id"], p["summary"], details_str, tags_str,
                "EXTRACTED", created_at, now
            ))
            nodes_upserted += 1

            # Aggiornamento FTS5 BM25 (incluso slug e tag)
            conn.execute("DELETE FROM nodes_fts WHERE id = ?;", (p["id"],))
            fts_tags = f"{tags_str} {p['id']} {p.get('details', {}).get('local_path', '')}"
            conn.execute("""
                INSERT INTO nodes_fts (id, label, summary, tags)
                VALUES (?, ?, ?, ?);
            """, (p["id"], p["label"], p["summary"], fts_tags))

            # 2. Sinapsi con il Macro-Dominio Fondativo (Piano 0)
            domain_id = p["parent_graph_id"]
            if not conn.execute("SELECT 1 FROM nodes WHERE id = ?", (domain_id,)).fetchone():
                domain_id = "domain-software-engineering"
                
            if conn.execute("SELECT 1 FROM nodes WHERE id = ?", (domain_id,)).fetchone():
                conn.execute("""
                    INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'BELONGS_TO_DOMAIN', 'EXTRACTED', 'Progetto Mac catalogato nel suo macro-dominio di riferimento', ?);
                """, (p["id"], domain_id, now))
                edges_upserted += 1

            # 3. Sinapsi con Pierfrancesco Amendola (Creator)
            if conn.execute("SELECT 1 FROM nodes WHERE id = 'person-pierfrancesco'").fetchone():
                conn.execute("""
                    INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, 'person-pierfrancesco', 'CREATED_BY', 'EXTRACTED', 'Progetto ideato e sviluppato da Pierfrancesco Amendola', ?);
                """, (p["id"], now))
                edges_upserted += 1

            # 4. Inserimento Moduli Atomici (Piano 2)
            for m in p.get("atomic_modules", []):
                m_details = json.dumps({"parent_project": p["id"], "file_uri": p["details"]["file_uri"]})
                m_tags = json.dumps(m.get("tags", []))
                
                conn.execute("""
                    INSERT OR REPLACE INTO nodes (
                        id, label, hemisphere, primary_label, category,
                        layer_level, parent_graph_id, summary, details, tags,
                        confidence, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, (
                    m["id"], m["label"], m["hemisphere"], m["primary_label"], "MODULE",
                    m["layer_level"], p["id"], m["summary"], m_details, m_tags,
                    "EXTRACTED", now, now
                ))
                nodes_upserted += 1

                conn.execute("DELETE FROM nodes_fts WHERE id = ?;", (m["id"],))
                conn.execute("""
                    INSERT INTO nodes_fts (id, label, summary, tags)
                    VALUES (?, ?, ?, ?);
                """, (m["id"], m["label"], m["summary"], m_tags))

                conn.execute("""
                    INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'PART_OF_PROJECT', 'EXTRACTED', 'Modulo architetturale del progetto', ?);
                """, (m["id"], p["id"], now))
                edges_upserted += 1

        conn.commit()
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")

    finally:
        conn.close()

    if verbose:
        print(f"✨ Ingestion completata: +{nodes_upserted} nodi inseriti/aggiornati, +{edges_upserted} sinapsi create.")

    return {
        "status": "success",
        "projects_scanned": len(raw_projects),
        "nodes_upserted": nodes_upserted,
        "edges_upserted": edges_upserted
    }


if __name__ == "__main__":
    res = ingest_mac_workspace()
    print(json.dumps(res, indent=2))
