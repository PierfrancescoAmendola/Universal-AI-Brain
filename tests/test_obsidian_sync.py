#!/usr/bin/env python3
"""
Test Suite per Obsidian Vault Sync Engine
Verifica:
1. Serializzazione e parsing del frontmatter YAML (zero external deps).
2. Esportazione completa da SQLite a cartelle del Palazzo Cognitivo (00, 01, 02).
3. Presenza di wikilinks [[...]] e sezioni Markdown.
4. Importazione dal Vault a SQLite con preservazione nodi e archi.
5. Round-trip completo con aggiunta di una nuova nota in Markdown e verifica nel DB.
"""

import os
import sys
import shutil
import tempfile
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from obsidian_vault_sync import (
    serialize_frontmatter,
    parse_frontmatter,
    export_brain_to_vault,
    import_vault_to_brain,
    sync_bidirectional
)


class TestObsidianSync(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_brain.db")
        self.vault_dir = os.path.join(self.test_dir, "test_vault")
        
        # Inizializza un DB di test con schema completo
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
        
        # Popola con nodi campione su 3 piani
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, details, tags)
            VALUES ('domain-software-engineering', 'Ingegneria del Software', 'LEFT', 'ROOT_DOMAIN', 'ROOT_DOMAIN', 0, 'root', 'Macro-dominio del software', '{"scope": "architetture"}', '["tech", "code"]');
        """)
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, details, tags)
            VALUES ('project-royal-gambit', 'Royal Gambit Chess', 'LEFT', 'PROJECT', 'PROJECT', 1, 'domain-software-engineering', 'Progetto scacchi Duolingo style', '{"status": "in_progress"}', '["chess", "flutter"]');
        """)
        conn.execute("""
            INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, details, tags)
            VALUES ('ui-component-chess-board', 'Scacchiera 2D Component', 'RIGHT', 'UI_COMPONENT', 'UI_COMPONENT', 2, 'project-royal-gambit', 'Componente grafico scacchiera interattiva', '{"framework": "flutter"}', '["ui", "graphics"]');
        """)
        
        # Inserisci archi
        conn.execute("""
            INSERT INTO edges (source, target, relation, reasoning)
            VALUES ('project-royal-gambit', 'domain-software-engineering', 'BELONGS_TO_DOMAIN', 'Fa parte del dominio software');
        """)
        conn.execute("""
            INSERT INTO edges (source, target, relation, reasoning)
            VALUES ('ui-component-chess-board', 'project-royal-gambit', 'PART_OF_PROJECT', 'Componente della scacchiera');
        """)
        conn.commit()
        conn.close()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
    def test_frontmatter_parse_serialize(self):
        meta = {
            "id": "node-1",
            "label": "Test Label",
            "hemisphere": "LEFT",
            "layer_level": 1,
            "tags": ["alpha", "beta"],
            "confidence": "EXTRACTED"
        }
        serialized = serialize_frontmatter(meta)
        self.assertTrue(serialized.startswith("---"))
        self.assertTrue(serialized.endswith("---"))
        
        content = serialized + "\n\n# Body content\nTest body"
        parsed_meta, body = parse_frontmatter(content)
        self.assertEqual(parsed_meta["id"], "node-1")
        self.assertEqual(parsed_meta["label"], "Test Label")
        self.assertEqual(parsed_meta["layer_level"], 1)
        self.assertEqual(parsed_meta["tags"], ["alpha", "beta"])
        self.assertIn("# Body content", body)

    def test_export_to_obsidian_vault(self):
        res = export_brain_to_vault(self.db_path, self.vault_dir)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["nodes_exported"], 3)
        
        # Verifica esistenza cartelle e file
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "00_INDEX.md")))
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "00_Domini", "domain-software-engineering.md")))
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "01_Progetti_Episodi", "project-royal-gambit.md")))
        self.assertTrue(os.path.exists(os.path.join(self.vault_dir, "02_Moduli_Atomici", "ui-component-chess-board.md")))
        
        # Verifica contenuto wikilinks
        with open(os.path.join(self.vault_dir, "01_Progetti_Episodi", "project-royal-gambit.md"), "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("[[domain-software-engineering]]", content)
            self.assertIn("## 🔗 Connessioni Uscenti", content)

    def test_import_from_vault_and_roundtrip(self):
        # Esporta prima
        export_brain_to_vault(self.db_path, self.vault_dir)
        
        # Crea una nuova nota manualmente nel vault (simulando utente o AI su Obsidian)
        new_note_content = """---
id: rule-clean-architecture
label: Regola Clean Architecture
hemisphere: LEFT
primary_label: COGNITIVE_RULE
category: COGNITIVE_RULE
layer_level: 2
parent_graph_id: domain-software-engineering
tags: [architecture, clean-code]
confidence: EXTRACTED
---

# Regola Clean Architecture

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `COGNITIVE_RULE` | **Piano:** 2 | **Padre:** [[domain-software-engineering]]

## 📝 Sintesi
Mantenere separati domain layer, use cases e data sources.

## 🔗 Connessioni Uscenti
- [[domain-software-engineering]] (`GUIDED_BY`) — _Principio fondamentale_
"""
        new_note_path = os.path.join(self.vault_dir, "02_Moduli_Atomici", "rule-clean-architecture.md")
        with open(new_note_path, "w", encoding="utf-8") as f:
            f.write(new_note_content)
            
        # Esegui import
        imp_res = import_vault_to_brain(self.vault_dir, self.db_path)
        self.assertEqual(imp_res["status"], "success")
        self.assertEqual(imp_res["nodes_imported"], 4)
        
        # Verifica che il nuovo nodo e il nuovo arco siano presenti nel DB SQLite
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        node = conn.execute("SELECT * FROM nodes WHERE id = 'rule-clean-architecture'").fetchone()
        self.assertIsNotNone(node)
        self.assertEqual(node["label"], "Regola Clean Architecture")
        self.assertEqual(node["primary_label"], "COGNITIVE_RULE")
        self.assertEqual(node["layer_level"], 2)
        
        edge = conn.execute("SELECT * FROM edges WHERE source = 'rule-clean-architecture' AND target = 'domain-software-engineering'").fetchone()
        self.assertIsNotNone(edge)
        self.assertEqual(edge["relation"], "GUIDED_BY")
        conn.close()


if __name__ == "__main__":
    unittest.main()
