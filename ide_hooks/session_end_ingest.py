#!/usr/bin/env python3
"""
Session End Autonomous Ingest Hook - Universal AI Brain
======================================================
Analizza le modifiche apportate durante la sessione di lavoro (file modificati, git status)
e genera ed ingerisce automaticamente la Triade Obbligatoria di Sessione:
- USER_INTENT (Emisfero Sinistro)
- AI_REASONING (Emisfero Sinistro)
- CONVERSATION_EPISODE (Emisfero Destro)
- 7 Sinapsi di collegamento
"""

import sys
import os
import re
import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Optional

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.expanduser("~/Desktop/CervelloArtificiale/brain.db"))


def get_git_diff_summary(cwd: str = None) -> Tuple[str, List[str]]:
    """Estrae l'elenco dei file modificati e la statistica dei cambiamenti dal repository locale."""
    target_dir = cwd or os.getcwd()
    modified_files = []
    diff_stat = ""

    try:
        status_res = subprocess.run(
            ["git", "status", "--short"],
            cwd=target_dir,
            capture_output=True,
            text=True,
            timeout=4.0
        )
        if status_res.returncode == 0 and status_res.stdout.strip():
            for line in status_res.stdout.strip().split("\n"):
                parts = line.strip().split()
                if len(parts) >= 2:
                    modified_files.append(parts[-1])

        diff_res = subprocess.run(
            ["git", "diff", "--stat"],
            cwd=target_dir,
            capture_output=True,
            text=True,
            timeout=4.0
        )
        if diff_res.returncode == 0:
            diff_stat = diff_res.stdout.strip()
    except Exception:
        pass

    return diff_stat, modified_files


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text[:50].strip('-')


def auto_ingest_session(
    task_title: str,
    reasoning_summary: str = "",
    project_id: str = "proj-cervelloartificiale",
    model_name: str = "IDE Assistant",
    db_path: str = DEFAULT_DB_PATH
) -> Dict[str, Any]:
    """Crea e registra la Triade Cognitiva di Sessione nel connettoma."""
    now = datetime.now(timezone.utc).isoformat()
    ts_suffix = str(int(datetime.now().timestamp()))[-4:]
    slug_base = slugify(task_title)

    intent_id = f"user-intent-{slug_base}-{ts_suffix}"
    reasoning_id = f"reasoning-{slug_base}-{ts_suffix}"
    episode_id = f"episode-{slug_base}-{ts_suffix}"

    diff_stat, modified_files = get_git_diff_summary()
    files_str = ", ".join(modified_files[:8]) if modified_files else "File di progetto"

    full_reasoning = reasoning_summary or f"Implementazione e verifica per {task_title}. File coinvolti: {files_str}."

    nodes = [
        {
            "id": intent_id,
            "label": f"Intento: {task_title}",
            "hemisphere": "LEFT",
            "primary_label": "USER_INTENT",
            "category": "USER_INTENT",
            "tags": ["ide-hook", "session-intent", slug_base],
            "summary": f"Obiettivo operativo: {task_title}.",
            "details": json.dumps({
                "user_prompt": task_title,
                "modified_files": modified_files,
                "diff_stat": diff_stat
            }),
            "parent_graph_id": project_id,
            "layer_level": 1
        },
        {
            "id": reasoning_id,
            "label": f"Ragionamento: {task_title}",
            "hemisphere": "LEFT",
            "primary_label": "AI_REASONING",
            "category": "AI_REASONING",
            "tags": ["ide-hook", "ai-reasoning", slug_base],
            "summary": full_reasoning[:300],
            "details": json.dumps({
                "model": model_name,
                "actions_taken": modified_files,
                "outcome": "Session completed and verified"
            }),
            "parent_graph_id": project_id,
            "layer_level": 1
        },
        {
            "id": episode_id,
            "label": f"Episodio: {task_title}",
            "hemisphere": "RIGHT",
            "primary_label": "CONVERSATION_EPISODE",
            "category": "CONVERSATION_EPISODE",
            "tags": ["ide-hook", "dialogue-episode"],
            "summary": f"Sessione di sviluppo dedicata a: {task_title}.",
            "details": json.dumps({
                "participants": ["Pierfrancesco Amendola", model_name],
                "topic": task_title,
                "key_takeaways": "Task implementato e verificato con successo."
            }),
            "parent_graph_id": "root",
            "layer_level": 1
        }
    ]

    edges = [
        (intent_id, "person-pierfrancesco", "EXPRESSED_BY", "EXTRACTED", "Espresso da Pierfrancesco"),
        (intent_id, project_id, "TARGETS_PROJECT", "EXTRACTED", "Riferito al progetto target"),
        (reasoning_id, intent_id, "FULFILLS", "INFERRED", "Soddisfa la richiesta"),
        (reasoning_id, project_id, "OPTIMIZES", "INFERRED", "Ottimizza il progetto"),
        (episode_id, "person-pierfrancesco", "INTERACTION_WITH", "EXTRACTED", "Interazione con Pierfrancesco"),
        (episode_id, intent_id, "RECORDS_INTENT", "EXTRACTED", "Registra l'intento"),
        (episode_id, reasoning_id, "RECORDS_REASONING", "EXTRACTED", "Registra il ragionamento")
    ]

    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database {db_path} non trovato.")

    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")

    with conn:
        for n in nodes:
            conn.execute("""
                INSERT OR REPLACE INTO nodes
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', ?, ?, ?, ?)
            """, (
                n["id"], n["label"], n["hemisphere"], n["primary_label"], n["category"],
                json.dumps(n["tags"]), n["summary"], n["details"], n["parent_graph_id"],
                n["layer_level"], now, now
            ))

        # Inserimento delle 7 sinapsi
        for src, tgt, rel, conf, reason in edges:
            # Assicura esistenza nodo target
            tgt_exists = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (tgt,)).fetchone()
            if tgt_exists:
                conn.execute("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (src, tgt, rel, conf, reason, now))

    return {
        "status": "success",
        "intent_id": intent_id,
        "reasoning_id": reasoning_id,
        "episode_id": episode_id,
        "modified_files_count": len(modified_files)
    }


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Uso: python3 session_end_ingest.py \"Titolo del Task Svolto\" [\"Sintesi Ragionamento\"]")
        sys.exit(1)

    task_title = sys.argv[1].strip()
    reasoning = sys.argv[2].strip() if len(sys.argv) > 2 else ""

    res = auto_ingest_session(task_title, reasoning_summary=reasoning)
    print(f"✅ Triade Cognitiva registrata nel Connettoma:")
    print(f"  • USER_INTENT:          {res['intent_id']}")
    print(f"  • AI_REASONING:         {res['reasoning_id']}")
    print(f"  • CONVERSATION_EPISODE: {res['episode_id']}")
    print(f"  • File tracciati:       {res['modified_files_count']}")


if __name__ == "__main__":
    main()
