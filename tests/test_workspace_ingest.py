#!/usr/bin/env python3
"""
Unit tests for mac_workspace_ingest.py
"""

import os
import shutil
import tempfile
import sqlite3
import unittest

from mac_workspace_ingest import ingest_mac_workspace


class TestWorkspaceIngest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_ingest.db")
        
        # Inizializza schema SQLite
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE nodes (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                hemisphere TEXT CHECK(hemisphere IN ('LEFT', 'RIGHT')),
                primary_label TEXT,
                category TEXT,
                layer_level INTEGER DEFAULT 2,
                parent_graph_id TEXT DEFAULT 'root',
                summary TEXT,
                details TEXT,
                tags TEXT,
                confidence TEXT DEFAULT 'EXTRACTED',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.execute("""
            CREATE TABLE edges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                target TEXT NOT NULL,
                relation TEXT NOT NULL,
                confidence TEXT DEFAULT 'EXTRACTED',
                reasoning TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(source, target, relation)
            );
        """)
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS nodes_fts USING fts5(
                id UNINDEXED,
                label,
                summary,
                tags,
                tokenize='unicode61'
            );
        """)
        # Aggiungi nodo radice pierfrancesco e domini
        conn.execute("INSERT INTO nodes (id, label, hemisphere) VALUES ('person-pierfrancesco', 'Pierfrancesco Amendola', 'LEFT');")
        conn.execute("INSERT INTO nodes (id, label, hemisphere) VALUES ('domain-software-engineering', 'Ingegneria del Software', 'LEFT');")
        conn.commit()
        conn.close()

        # Crea un mock project da scansionare
        self.mock_proj_dir = os.path.join(self.test_dir, "MockProjects", "StreaksUpTestApp")
        os.makedirs(self.mock_proj_dir, exist_ok=True)
        with open(os.path.join(self.mock_proj_dir, "project.yml"), "w") as f:
            f.write("name: StreaksUpTestApp\n")
        with open(os.path.join(self.mock_proj_dir, "App.swift"), "w") as f:
            f.write("import SwiftUI\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_ingest_mac_workspace(self):
        """Verifica che l'ingestion crei correttamente nodi, sinapsi e indici FTS5."""
        res = ingest_mac_workspace(
            search_paths=[os.path.join(self.test_dir, "MockProjects")],
            db_path=self.db_path,
            verbose=False
        )
        self.assertEqual(res["status"], "success")
        self.assertGreaterEqual(res["nodes_upserted"], 1)
        self.assertGreaterEqual(res["edges_upserted"], 1)

        # Verifica nel DB
        conn = sqlite3.connect(self.db_path)
        row = conn.execute("SELECT * FROM nodes WHERE id = 'proj-streaksuptestapp'").fetchone()
        self.assertIsNotNone(row)
        
        # Verifica FTS5
        fts_match = conn.execute("SELECT id FROM nodes_fts WHERE nodes_fts MATCH 'Streaks'").fetchone()
        self.assertIsNotNone(fts_match)
        self.assertEqual(fts_match[0], "proj-streaksuptestapp")
        conn.close()


if __name__ == "__main__":
    unittest.main()
