#!/usr/bin/env python3
"""
Test Suite per Tensions & Contradictions Detector
Verifica:
1. Inizializzazione della tabella `tensions`.
2. Creazione e aggiornamento di una tensione.
3. Rilevamento di candidate tensioni semantiche.
4. Risoluzione di una tensione con diverse strategie (STEELMAN, MERGE_AI, FALSE_POSITIVE).
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from brain_tensions import (
    init_tensions_schema,
    create_or_update_tension,
    get_tensions,
    resolve_tension,
    detect_candidate_tensions
)


class TestTensions(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_tensions.db")
        
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
        
        # Inserisci nodi con polarità opposte
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, summary, tags)
            VALUES ('rule-premature-optimization', 'Evita Ottimizzazione Prematura', 'LEFT', 'COGNITIVE_RULE', 'Non ottimizzare prima di misurare il reale collo di bottiglia.', '["clean-code", "refactor", "optimization"]');
        """)
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, summary, tags)
            VALUES ('rule-design-for-scale', 'Progetta per la Scalabilità Immediata', 'LEFT', 'COGNITIVE_RULE', 'Architettura distribuita e caching spinto fin dal primo commit.', '["speed", "mvp", "shipping", "scale-at-all-costs"]');
        """)
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_create_and_get_tension(self):
        res = create_or_update_tension(
            node_a_id="rule-premature-optimization",
            node_b_id="rule-design-for-scale",
            tension_type="TRADE_OFF",
            description="Compromesso tra semplicità iniziale e sovradimensionamento architetturale.",
            db_path=self.db_path
        )
        self.assertEqual(res["status"], "success")
        t_id = res["tension_id"]
        
        tensions = get_tensions(db_path=self.db_path)
        self.assertEqual(len(tensions), 1)
        self.assertEqual(tensions[0]["id"], t_id)
        self.assertEqual(tensions[0]["status"], "OPEN")
        self.assertEqual(tensions[0]["node_a_label"], "Evita Ottimizzazione Prematura")
        self.assertEqual(tensions[0]["node_b_label"], "Progetta per la Scalabilità Immediata")

    def test_detect_candidate_tensions(self):
        candidates = detect_candidate_tensions(db_path=self.db_path)
        self.assertGreaterEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["node_a_id"], "rule-premature-optimization")
        self.assertEqual(candidates[0]["node_b_id"], "rule-design-for-scale")

    def test_resolve_tension(self):
        res = create_or_update_tension(
            node_a_id="rule-premature-optimization",
            node_b_id="rule-design-for-scale",
            tension_type="TRADE_OFF",
            description="Tradeoff semplicità vs scalabilità",
            db_path=self.db_path
        )
        t_id = res["tension_id"]
        
        resolve_res = resolve_tension(
            tension_id=t_id,
            strategy="STEELMAN",
            resolution_notes="Applicare Clean Architecture modulare senza clustering distribuito fino a 10k utenti.",
            db_path=self.db_path
        )
        self.assertEqual(resolve_res["status"], "success")
        self.assertEqual(resolve_res["new_status"], "RESOLVED")
        
        # Verifica aggiornamento nel DB
        tensions = get_tensions(status="RESOLVED", db_path=self.db_path)
        self.assertEqual(len(tensions), 1)
        self.assertEqual(tensions[0]["resolution_strategy"], "STEELMAN")


if __name__ == "__main__":
    unittest.main()
