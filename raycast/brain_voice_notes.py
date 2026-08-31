#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ultime Note Vocali
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🎙️
# @raycast.packageName Cervello Artificiale
# @raycast.description Visualizza le note vocali registrate tramite Siri e Azioni Rapide

import os
import sys
import json
import sqlite3

LOCAL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(LOCAL_DIR, "brain.db")


def main():
    if not os.path.exists(DB_PATH):
        print("❌ Database locale non trovato.")
        sys.exit(1)

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA busy_timeout = 5000;")
        
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, label, hemisphere, primary_label, category, summary, details, created_at
            FROM nodes
            WHERE id LIKE 'voice-%'
            ORDER BY datetime(created_at) DESC
            LIMIT 15
        """)
        rows = cursor.fetchall()
        conn.close()

        print("🎙️ NOTE VOCALI REGISTRATE (Siri & Azioni Rapide)")
        print("═" * 58)

        if not rows:
            print("\nNessuna nota vocale ancora registrata.")
            print("💡 Usa l'Azione Rapida 'Appunto per il Cervello' su iPhone o Mac!")
            return

        print(f"Trovate {len(rows)} note vocali salvate nel connettoma:\n")

        for i, r in enumerate(rows, 1):
            item = dict(r)
            hemi_icon = "⚡" if item["hemisphere"] == "LEFT" else "🌸"
            hemi_label = "Sinistro" if item["hemisphere"] == "LEFT" else "Destro"
            
            created = str(item.get("created_at", ""))
            created_clean = created.replace("T", " ")[:19]
            
            details_raw = item.get("details", "{}")
            transcript = ""
            if isinstance(details_raw, str):
                try:
                    d_json = json.loads(details_raw)
                    transcript = d_json.get("full_transcript", "")
                except Exception:
                    transcript = ""
            elif isinstance(details_raw, dict):
                transcript = details_raw.get("full_transcript", "")

            content = transcript or item.get("summary", "")

            print(f"{i}. {hemi_icon} {item.get('label')}")
            print(f"   • Data:       {created_clean}")
            print(f"   • Emisfero:   {hemi_label} ({item.get('primary_label')})")
            print(f"   • Trascritto: \"{content}\"")
            print(f"   • ID:         {item.get('id')}")
            print("─" * 58)

    except Exception as e:
        print(f"❌ Errore lettura note vocali: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
