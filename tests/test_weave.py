#!/usr/bin/env python3
"""
Test Suite per Weave Link Engine
Verifica:
1. Rilevamento di nodi orfani (degree <= 2).
2. Generazione di proposte di collegamento basate su affinità semantica.
3. Riconoscimento di ponti cross-emisferici (CORPUS_CALLOSUM_LINK).
4. Applicazione atomica dei link accettati nel database SQLite.
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from brain_weave import (
    get_orphan_nodes,
    compute_weave_proposals,
    apply_weave_links
)


class TestWeave(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_weave.db")
        
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE nodes (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                hemisphere TEXT,
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
        
        # Inserisci nodi (due isolati che condividono il tema "scacchi")
        nodes_data = [
            ("tech-minimax-engine", "Motore Minimax Scacchi", "LEFT", "ALGORITHM", "Implementazione algoritmo Minimax per scacchi con alpha-beta pruning.", "['chess', 'algorithm']"),
            ("design-chess-ui", "Design Sistema Scacchi Minimal", "RIGHT", "UI_COMPONENT", "Interfaccia utente minimalista e palette per scacchi.", "['chess', 'design', 'ui']"),
            ("domain-software-engineering", "Ingegneria Software", "LEFT", "ROOT_DOMAIN", "Macro-dominio software.", "['software']")
        ]
        for nid, lbl, hemi, plbl, summ, tgs in nodes_data:
            conn.execute("INSERT INTO nodes (id, label, hemisphere, primary_label, summary, tags) VALUES (?, ?, ?, ?, ?, ?)", (nid, lbl, hemi, plbl, summ, tgs))
            conn.execute("INSERT INTO nodes_fts (id, label, summary, tags) VALUES (?, ?, ?, ?)", (nid, lbl, summ, tgs))
            
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_get_orphans(self):
        orphans = get_orphan_nodes(max_degree=2, db_path=self.db_path)
        self.assertEqual(len(orphans), 3)

    def test_compute_proposals(self):
        proposals = compute_weave_proposals(max_proposals=5, db_path=self.db_path)
        self.assertGreaterEqual(len(proposals), 1)
        
        # Uno dei link deve collegare minimax e design-chess-ui come cross-hemisphere
        cross_links = [p for p in proposals if p["is_cross_hemisphere"]]
        self.assertGreaterEqual(len(cross_links), 1)
        self.assertEqual(cross_links[0]["relation"], "CORPUS_CALLOSUM_LINK")

    def test_apply_weave_links(self):
        proposals = compute_weave_proposals(max_proposals=5, db_path=self.db_path)
        res = apply_weave_links(proposals, db_path=self.db_path)
        self.assertEqual(res["status"], "success")
        self.assertGreater(res["applied_count"], 0)
        
        # Verifica che l'arco sia presente nel DB
        conn = sqlite3.connect(self.db_path)
        edges = conn.execute("SELECT * FROM edges").fetchall()
        self.assertGreater(len(edges), 0)
        conn.close()


if __name__ == "__main__":
    unittest.main()
