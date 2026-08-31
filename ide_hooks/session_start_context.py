#!/usr/bin/env python3
"""
Session Start Context Hook - Universal AI Brain
================================================
Genera un contesto sintetico ultra-compatto (<400 token) all'avvio di una sessione IDE
(Cursor, Claude Code, Antigravity, Terminale) contenente preferenze utente e architettura del progetto attivo.
"""

import sys
import os
import json
import sqlite3
from typing import Dict, Any, Optional, List

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.expanduser("~/Desktop/CervelloArtificiale/brain.db"))


def detect_project_context(cwd: str = None, db_path: str = DEFAULT_DB_PATH) -> str:
    current_dir = cwd or os.getcwd()
    dir_name = os.path.basename(current_dir).lower()

    if not os.path.exists(db_path):
        return "# 🧠 Universal Brain Context: Database not found."

    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")

    context_lines = [
        "═══════════════════════════════════════════════════════════════",
        "🧠 UNIVERSAL AI BRAIN - CONTESTO COGNITIVO ATTIVO",
        "═══════════════════════════════════════════════════════════════",
        "👤 UTENTE: Pierfrancesco Amendola",
        "🌐 PRINCIPI: 100% Zero-Cost (0,00€ Forever), Local-First, Alta Efficienza",
        "🇮🇹 LINGUA: Italiano obbligatorio (termini tecnici internazionali in Inglese)"
    ]

    with conn:
        # 1. Trova il progetto correlato alla directory corrente
        cur = conn.cursor()
        cur.execute("""
            SELECT id, label, summary, tags, details
            FROM nodes
            WHERE (id LIKE ? OR label LIKE ? OR summary LIKE ?)
              AND primary_label IN ('PROJECT', 'MODULE', 'ARCHITECTURE')
            ORDER BY layer_level ASC
            LIMIT 1
        """, (f"%{dir_name}%", f"%{dir_name}%", f"%{dir_name}%"))
        proj = cur.fetchone()

        if proj:
            context_lines.append(f"\n📦 PROGETTO ATTIVO: {proj['label']} (`{proj['id']}`)")
            context_lines.append(f"📝 SINTESI: {proj['summary']}")
        else:
            context_lines.append(f"\n📦 AMBIENTE: {dir_name}")

        # 2. Recupera 2 recenti episodi conversazionali
        cur.execute("""
            SELECT id, label, summary, updated_at
            FROM nodes
            WHERE primary_label IN ('USER_INTENT', 'AI_REASONING', 'CONVERSATION_EPISODE')
            ORDER BY datetime(updated_at) DESC
            LIMIT 2
        """)
        episodes = cur.fetchall()
        if episodes:
            context_lines.append("\n📜 RECENTI DECISIONI & INTENTI REGISTRATI:")
            for ep in episodes:
                context_lines.append(f"  • [{ep['id']}] {ep['label']}: {ep['summary'][:120]}...")

        # 3. Protocollo di Chiusura
        context_lines.append("\n🎯 AL TERMINE DEL LAVORO: Esegui l'ingestione della sessione via tool MCP brain_ingest o /api/memory/ingest.")
        context_lines.append("═══════════════════════════════════════════════════════════════\n")

    return "\n".join(context_lines)


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    ctx = detect_project_context(target_dir)
    print(ctx)


if __name__ == "__main__":
    main()
