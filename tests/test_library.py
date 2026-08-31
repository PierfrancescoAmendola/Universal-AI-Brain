#!/usr/bin/env python3
"""
Test Suite per Lens & Library Engine
Verifica:
1. Rilevamento e listing delle lenti/entità disponibili.
2. Estrazione del sottografo di una lente con profondità regolabile.
3. Costruzione del prompt di dialogo con grounding sui nodi e citazioni [[...]].
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from brain_library import (
    list_available_lenses,
    extract_lens_subgraph,
    build_lens_dialogue_prompt
)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_library.db")
        
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
        
        # Inserisci un libro/autore e 2 concetti figli
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, summary, tags)
            VALUES ('book-meditations-marcus-aurelius', 'Colloqui con se stesso - Marco Aurelio', 'RIGHT', 'LIFE_LESSON', 'Trattato stoico sulla disciplina interiore e il dovere razionale.', '["book", "stoicism", "philosophy"]');
        """)
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, summary, tags)
            VALUES ('principle-dichotomy-of-control', 'Dicotomia del Controllo', 'RIGHT', 'LIFE_LESSON', 'Distingui ciò che è in tuo potere da ciò che non lo è.', '["stoicism", "mental-model"]');
        """)
        conn.execute("""
            INSERT INTO edges (source, target, relation)
            VALUES ('principle-dichotomy-of-control', 'book-meditations-marcus-aurelius', 'DERIVED_FROM');
        """)
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_list_available_lenses(self):
        lenses = list_available_lenses(db_path=self.db_path)
        self.assertGreaterEqual(len(lenses), 1)
        self.assertEqual(lenses[0]["id"], "book-meditations-marcus-aurelius")

    def test_extract_lens_subgraph(self):
        subgraph = extract_lens_subgraph("book-meditations-marcus-aurelius", max_depth=2, db_path=self.db_path)
        self.assertEqual(subgraph["status"], "success")
        self.assertEqual(subgraph["nodes_count"], 2)
        self.assertEqual(subgraph["edges_count"], 1)

    def test_build_lens_dialogue_prompt(self):
        res = build_lens_dialogue_prompt("marcus-aurelius", "Come affrontare una giornata caotica?", db_path=self.db_path)
        self.assertEqual(res["status"], "success")
        self.assertIn("LENS & LIBRARY DIALOGUE", res["prompt"])
        self.assertIn("[[book-meditations-marcus-aurelius]]", res["prompt"])
        self.assertIn("Dicotomia del Controllo", res["prompt"])


if __name__ == "__main__":
    unittest.main()
