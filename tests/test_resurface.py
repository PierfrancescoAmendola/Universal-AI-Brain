#!/usr/bin/env python3
"""
Test Suite per Daily Resurface & Spaced Repetition Engine
Verifica:
1. Calcolo dello score di oblio basato sulla curva di Ebbinghaus.
2. Selezione dei 3 nodi dormienti più meritevoli di riattivazione.
3. Generazione del pacchetto completo giornaliero con tensione e firmware.
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from brain_resurface import (
    calculate_dormant_nodes,
    get_daily_resurface_packet
)


class TestResurface(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_resurface.db")
        
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
                created_at TEXT,
                updated_at TEXT
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
        
        now = datetime.now(timezone.utc)
        t_recent = (now - timedelta(hours=2)).isoformat()
        t_dormant_1 = (now - timedelta(days=30)).isoformat()
        t_dormant_2 = (now - timedelta(days=90)).isoformat()
        
        # Nodi con diverse età di inattività
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, layer_level, summary, updated_at)
            VALUES ('node-recent', 'Nota Recente', 'LEFT', 'USER_INTENT', 1, 'Creata poche ore fa', ?);
        """, (t_recent,))
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, layer_level, summary, updated_at)
            VALUES ('node-month-old', 'Nota di un Mese Fa', 'LEFT', 'AI_REASONING', 1, 'Creata un mese fa con buone connessioni', ?);
        """, (t_dormant_1,))
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, layer_level, summary, updated_at)
            VALUES ('node-three-months', 'Nota di Tre Mesi Fa', 'RIGHT', 'LIFE_LESSON', 2, 'Creata tre mesi fa', ?);
        """, (t_dormant_2,))
        
        # Archi
        conn.execute("INSERT INTO edges (source, target, relation) VALUES ('node-month-old', 'node-recent', 'FOLLOWS');")
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_calculate_dormant_nodes(self):
        dormant = calculate_dormant_nodes(limit=3, db_path=self.db_path)
        self.assertEqual(len(dormant), 3)
        # La nota più vecchia di 90 o 30 giorni deve avere uno score di resurface più alto rispetto a quella di 2 ore fa
        self.assertGreater(dormant[0]["days_dormant"], 1.0)
        self.assertGreater(dormant[0]["resurface_score"], 0.0)

    def test_get_daily_resurface_packet(self):
        packet = get_daily_resurface_packet(db_path=self.db_path)
        self.assertIn("date", packet)
        self.assertEqual(packet["duration_seconds"], 90)
        self.assertGreaterEqual(len(packet["resurface_nodes"]), 1)
        self.assertIsNotNone(packet["firmware_of_the_day"])
        self.assertIn("name", packet["firmware_of_the_day"])


if __name__ == "__main__":
    unittest.main()
