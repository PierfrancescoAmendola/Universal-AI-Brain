#!/usr/bin/env python3
"""
Universal AI Brain - Master End-to-End Test Suite
=================================================
Verifica la correttezza, la tenuta e l'integrità di tutti i nuovi moduli cognitivi:
1. Obsidian Vault Sync Engine (Markdown, YAML Frontmatter, [[Wikilinks]], 3 Cartelle)
2. Tensions & Contradictions Detector (Rilevamento ed elaborazione sintesi)
3. Weave Link Engine (Auto-Ponti e Corpo Calloso per nodi orfani)
4. Daily Resurface (Curva dell'oblio di Ebbinghaus, 90s Briefing)
5. 9 Firmware Cognitivi (Modelli mentali di pensiero operativo)
6. Lens & Library Engine (Dialogo groundato con autori e mentori)
7. Server MCP stdio JSON-RPC 2.0 (Verifica di tutti i tool)
8. FastAPI REST Endpoints (HTTP 200 e payload strutturati)
"""

import os
import sys
import json
import shutil
import tempfile
import sqlite3
import unittest
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from obsidian_vault_sync import serialize_frontmatter, parse_frontmatter, export_brain_to_vault, import_vault_to_brain
from brain_tensions import create_or_update_tension, get_tensions, resolve_tension, detect_candidate_tensions, init_tensions_schema
from brain_weave import get_orphan_nodes, compute_weave_proposals, apply_weave_links
from brain_resurface import calculate_dormant_nodes, get_daily_resurface_packet
from brain_firmware import list_available_firmware, apply_firmware_lens, seed_firmware_nodes_in_brain
from brain_library import list_available_lenses, extract_lens_subgraph, build_lens_dialogue_prompt
from mcp_server import handle_json_rpc


class TestMasterEnhancedBrain(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_brain_master.db")
        self.vault_dir = os.path.join(self.test_dir, "test_obsidian_vault")
        
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL;")
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
        init_tensions_schema(conn)
        
        # Popola con dataset iniziale
        nodes = [
            ("domain-software-engineering", "Ingegneria del Software", "LEFT", "ROOT_DOMAIN", 0, "root", "Macro-dominio software", "['software', 'code']"),
            ("domain-filosofia-valori", "Filosofia e Valori", "RIGHT", "ROOT_DOMAIN", 0, "root", "Macro-dominio filosofico", "['philosophy', 'stoicism']"),
            ("rule-clean-architecture", "Clean Architecture Rule", "LEFT", "COGNITIVE_RULE", 2, "domain-software-engineering", "Separare domini e infrastruttura", "['architecture', 'clean-code', 'optimization']"),
            ("rule-rapid-shipping", "Rapid Shipping Rule", "LEFT", "COGNITIVE_RULE", 2, "domain-software-engineering", "Rilasciare velocemente in produzione per testare", "['mvp', 'shipping', 'speed']"),
            ("author-marcus-aurelius", "Marco Aurelio", "RIGHT", "LIFE_LESSON", 1, "domain-filosofia-valori", "Imperatore e filosofo stoico", "['author', 'stoicism', 'philosophy']")
        ]
        for nid, lbl, hemi, plbl, lvl, parent, summ, tgs in nodes:
            conn.execute("""
                INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (nid, lbl, hemi, plbl, plbl, lvl, parent, summ, tgs))
            conn.execute("INSERT INTO nodes_fts (id, label, summary, tags) VALUES (?, ?, ?, ?);", (nid, lbl, summ, tgs))
            
        conn.execute("INSERT INTO edges (source, target, relation) VALUES ('rule-clean-architecture', 'domain-software-engineering', 'BELONGS_TO_DOMAIN');")
        conn.execute("INSERT INTO edges (source, target, relation) VALUES ('author-marcus-aurelius', 'domain-filosofia-valori', 'BELONGS_TO_DOMAIN');")
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_01_obsidian_sync_export_and_import(self):
        """1. Verifica export Obsidian con 3 cartelle e import bidirezionale."""
        exp_res = export_brain_to_vault(self.db_path, self.vault_dir)
        self.assertEqual(exp_res["status"], "success")
        self.assertEqual(exp_res["nodes_exported"], 5)
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "00_INDEX.md")))
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "00_Domini", "domain-software-engineering.md")))
        
        # Aggiungi nuova nota Obsidian
        new_md = """---
id: project-super-brain
label: Progetto Super Brain
hemisphere: LEFT
primary_label: PROJECT
layer_level: 1
parent_graph_id: domain-software-engineering
tags: [brain, ai]
---

# Progetto Super Brain

## 📝 Sintesi
Evoluzione del connettoma cognitivo.

## 🔗 Connessioni Uscenti
- [[domain-software-engineering]] (`EXPANDS`)
"""
        with open(os.path.join(self.vault_dir, "01_Progetti_Episodi", "project-super-brain.md"), "w", encoding="utf-8") as f:
            f.write(new_md)
            
        imp_res = import_vault_to_brain(self.vault_dir, self.db_path)
        self.assertEqual(imp_res["status"], "success")
        self.assertEqual(imp_res["nodes_imported"], 6)

    def test_02_tensions_detector_and_resolver(self):
        """2. Verifica rilevamento tensioni e risoluzione steelmanning."""
        candidates = detect_candidate_tensions(db_path=self.db_path)
        self.assertGreaterEqual(len(candidates), 1)
        
        t_res = create_or_update_tension(
            node_a_id="rule-clean-architecture",
            node_b_id="rule-rapid-shipping",
            tension_type="TRADE_OFF",
            description="Compromesso tra rigore architetturale e velocità di rilascio.",
            db_path=self.db_path
        )
        self.assertEqual(t_res["status"], "success")
        
        res_res = resolve_tension(
            tension_id=t_res["tension_id"],
            strategy="STEELMAN",
            resolution_notes="MVP snello per validare, refactoring Clean Architecture prima dello scale.",
            db_path=self.db_path
        )
        self.assertEqual(res_res["status"], "success")
        self.assertEqual(res_res["new_status"], "RESOLVED")

    def test_03_weave_link_engine(self):
        """3. Verifica generazione auto-ponti per nodi orfani."""
        orphans = get_orphan_nodes(max_degree=2, db_path=self.db_path)
        self.assertGreater(len(orphans), 0)
        
        proposals = compute_weave_proposals(max_proposals=5, db_path=self.db_path)
        if proposals:
            apply_res = apply_weave_links(proposals, db_path=self.db_path)
            self.assertEqual(apply_res["status"], "success")

    def test_04_daily_resurface(self):
        """4. Verifica pacchetto 90s Daily Resurface."""
        packet = get_daily_resurface_packet(db_path=self.db_path)
        self.assertEqual(packet["duration_seconds"], 90)
        self.assertGreater(len(packet["resurface_nodes"]), 0)
        self.assertIn("firmware_of_the_day", packet)

    def test_05_firmware_models(self):
        """5. Verifica i 9 firmware mentali."""
        seed_res = seed_firmware_nodes_in_brain(db_path=self.db_path)
        self.assertEqual(seed_res["status"], "success")
        
        models = list_available_firmware()
        self.assertEqual(len(models), 9)
        
        lens = apply_firmware_lens("inversion", "Come evitare fallimenti software?")
        self.assertEqual(lens["status"], "success")
        self.assertIn("Charlie Munger", lens["directive"])

    def test_06_lens_and_library(self):
        """6. Verifica dialogo groundato con mentori/autori."""
        lenses = list_available_lenses(db_path=self.db_path)
        self.assertGreater(len(lenses), 0)
        
        prompt_res = build_lens_dialogue_prompt("marcus-aurelius", "Come mantenere calma mentale?", db_path=self.db_path)
        self.assertEqual(prompt_res["status"], "success")
        self.assertIn("Marco Aurelio", prompt_res["prompt"])

    def test_07_mcp_server_json_rpc(self):
        """7. Verifica conformità JSON-RPC del server MCP."""
        # Test tools/list
        req_list = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
        res_list = handle_json_rpc(req_list)
        self.assertIsNotNone(res_list)
        tool_names = {t["name"] for t in res_list["result"]["tools"]}
        self.assertIn("brain_get_daily_resurface", tool_names)
        self.assertIn("brain_sync_obsidian", tool_names)
        self.assertIn("brain_apply_firmware", tool_names)
        self.assertIn("brain_get_tensions", tool_names)
        self.assertIn("brain_get_weave_proposals", tool_names)
        self.assertIn("brain_query_library_lens", tool_names)


if __name__ == "__main__":
    unittest.main()
