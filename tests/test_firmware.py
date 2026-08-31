#!/usr/bin/env python3
"""
Test Suite per Cognitive Firmware Engine (9 Mental Models)
Verifica:
1. Disponibilità e completezza di tutti i 9 modelli registrati.
2. Ingestione automatica dei nodi MENTAL_MODEL nel DB.
3. Applicazione della lente e generazione del protocollo a 4 passi.
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from brain_firmware import (
    FIRMWARE_REGISTRY,
    list_available_firmware,
    seed_firmware_nodes_in_brain,
    apply_firmware_lens
)


class TestFirmware(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_firmware.db")
        
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
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_registry_has_nine_models(self):
        models = list_available_firmware()
        self.assertEqual(len(models), 9)
        keys = {m["key"] for m in models}
        expected = {
            "inversion", "second_order", "first_principles", "circle_of_competence",
            "opportunity_cost", "antifragility", "bayesian_updating", "pareto", "feynman"
        }
        self.assertEqual(keys, expected)

    def test_seed_firmware_nodes(self):
        res = seed_firmware_nodes_in_brain(db_path=self.db_path)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["firmware_seeded"], 9)
        
        conn = sqlite3.connect(self.db_path)
        count = conn.execute("SELECT COUNT(*) FROM nodes WHERE primary_label = 'MENTAL_MODEL'").fetchone()[0]
        self.assertEqual(count, 9)
        conn.close()

    def test_apply_firmware_lens(self):
        res = apply_firmware_lens(
            mode="antifragility",
            problem="Come gestire i crash imprevedibili di container terzi?",
            context="Sistema in cloud con microservizi distribuiti."
        )
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["firmware_key"], "antifragility")
        self.assertIn("Nassim Nicholas Taleb", res["directive"])
        self.assertEqual(len(res["steps"]), 4)


if __name__ == "__main__":
    unittest.main()
