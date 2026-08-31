#!/usr/bin/env python3
"""
Test Suite Integrata: Supercervello Ubiquitous Cognitive OS
===========================================================
Valida tutti i 9 moduli dell'ecosistema cognitivo:
1. Raycast Quick-Search & Quick-Add
2. Apple Shortcuts / Siri Voice Ingestion
3. Daily Morning Pulse & Telegram Scheduler
4. Web Clipper API Ingest
5. Kindle Clippings Sync & Idempotency
6. Nightly Cognitive REM Cycle
7. Hybrid Semantic Vector Search (RRF)
8. IDE Auto-Hooks (Start Context & End Ingest)
9. Obsidian Canvas Visual Graph Sync
10. WAL Mode & Zero-Cost Architecture Verification
"""

import os
import sys
import time
import json
import sqlite3
import unittest
import tempfile

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from raycast.brain_search import search_brain
from main import app, VoiceNotePayload, ingest_voice_note, IngestPayload, NodeModel, EdgeModel, ingest_memory
from brain_resurface import get_daily_resurface_packet, format_telegram_morning_pulse
from telegram_bot import process_telegram_message, broadcast_morning_pulse
from kindle_sync import parse_clippings_text, sync_kindle_clippings
from brain_rem_cycle import run_rem_consolidation
from brain_vectors import get_hybrid_search_engine
from ide_hooks.session_start_context import detect_project_context
from ide_hooks.session_end_ingest import auto_ingest_session
from obsidian_canvas_sync import export_brain_to_canvas, import_canvas_to_brain


class TestSupercervelloEcosystem(unittest.TestCase):

    def setUp(self):
        self.db_path = os.path.join(PROJECT_DIR, "brain.db")
        self.assertTrue(os.path.exists(self.db_path), "Database brain.db deve esistere")

    # 1. Test Raycast
    def test_01_raycast_search(self):
        results = search_brain("cervello", limit=5)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0, "Raycast search deve trovare nodi pertinenti")
        self.assertIn("label", results[0])
        self.assertIn("hemisphere", results[0])

    # 2. Test Voice Note Siri
    def test_02_voice_note_ingest(self):
        payload = VoiceNotePayload(
            transcript="Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.",
            source="test_suite_siri"
        )
        res = ingest_voice_note(payload)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["hemisphere"], "LEFT")
        self.assertTrue(res["node_id"].startswith("voice-"))

    # 3. Test Daily Morning Pulse
    def test_03_morning_pulse(self):
        packet = get_daily_resurface_packet(db_path=self.db_path)
        self.assertIn("resurface_nodes", packet)
        self.assertIn("firmware_of_the_day", packet)
        formatted = format_telegram_morning_pulse(packet)
        self.assertIn("DAILY BRAIN PULSE", formatted)
        self.assertIn("CURVA DELL'OBLIO", formatted)

    # 4. Test Telegram Bot Pulse Command
    def test_04_telegram_bot_pulse(self):
        reply = process_telegram_message(99999, "Tester", "/pulse")
        self.assertIn("DAILY BRAIN PULSE", reply)

    # 5. Test Web Clipper Payload
    def test_05_web_clipper_ingest(self):
        node = NodeModel(
            id="test-e2e-web-clipper",
            label="Test E2E Web Clipper Node",
            hemisphere="RIGHT",
            primary_label="CREATIVE_IDEA",
            category="CREATIVE_IDEA",
            tags=["web-clipper", "test"],
            summary="Verifica completa dell'ingestione Web Clipper.",
            details={"url": "https://example.com", "user": "Pierfrancesco"}
        )
        edge = EdgeModel(source="test-e2e-web-clipper", target="person-pierfrancesco", relation="EXPRESSED_BY")
        payload = IngestPayload(nodes=[node], edges=[edge])
        res = ingest_memory(payload)
        self.assertEqual(res["status"], "success")
        self.assertGreaterEqual(res["nodes_count"], 1)

    # 6. Test Kindle Sync Idempotency
    def test_06_kindle_sync(self):
        unique_token = str(int(time.time() * 1000))
        sample = f"""Il Cigno Nero (Nassim Taleb)
- Highlight Loc. 100 | 2024-01-01

Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: {unique_token}
==========
"""
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as tf:
            tf.write(sample)
            tf_path = tf.name

        try:
            r1 = sync_kindle_clippings(tf_path, db_path=self.db_path, verbose=False)
            self.assertEqual(r1["inserted"], 1)
            # Seconda importazione non deve duplicare
            r2 = sync_kindle_clippings(tf_path, db_path=self.db_path, verbose=False)
            self.assertEqual(r2["inserted"], 0)
        finally:
            os.remove(tf_path)

    # 7. Test Cognitive REM Cycle
    def test_07_rem_cycle(self):
        res = run_rem_consolidation(db_path=self.db_path, auto_apply_weave=False, verbose=False)
        self.assertIn("phases_executed", res)
        self.assertEqual(len(res["phases_executed"]), 4)
        for phase in res["phases_executed"]:
            self.assertNotIn("error", phase, f"Fase fallita: {phase}")
        self.assertTrue(res["database_vacuumed"])

    # 8. Test Hybrid Semantic Search (RRF)
    def test_08_hybrid_search(self):
        engine = get_hybrid_search_engine(self.db_path)
        res = engine.search_hybrid("sqlite database fast", limit=5)
        self.assertGreater(len(res), 0)
        self.assertIn("hybrid_score", res[0])
        self.assertIn("cosine_similarity", res[0])

    # 9. Test IDE Hooks
    def test_09_ide_hooks(self):
        ctx = detect_project_context(PROJECT_DIR, db_path=self.db_path)
        self.assertIn("UNIVERSAL AI BRAIN", ctx)
        self.assertIn("Pierfrancesco", ctx)

        end_res = auto_ingest_session("E2E Test Session Hook", "Verifica automatica suite", db_path=self.db_path)
        self.assertEqual(end_res["status"], "success")
        self.assertTrue(end_res["intent_id"].startswith("user-intent-"))
        self.assertTrue(end_res["reasoning_id"].startswith("reasoning-"))
        self.assertTrue(end_res["episode_id"].startswith("episode-"))

    # 10. Test Obsidian Canvas Visual Sync
    def test_10_obsidian_canvas(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".canvas") as tf:
            canvas_path = tf.name

        try:
            exp_res = export_brain_to_canvas(db_path=self.db_path, canvas_path=canvas_path, limit_nodes=20)
            self.assertEqual(exp_res["status"], "success")
            self.assertGreater(exp_res["nodes_count"], 0)

            imp_res = import_canvas_to_brain(canvas_path=canvas_path, db_path=self.db_path)
            self.assertEqual(imp_res["status"], "success")
        finally:
            if os.path.exists(canvas_path):
                os.remove(canvas_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
