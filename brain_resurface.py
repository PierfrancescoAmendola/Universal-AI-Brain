#!/usr/bin/env python3
"""
Daily Resurface & Spaced Repetition Engine - Universal AI Brain
==============================================================
Calcola il briefing cognitivo giornaliero di 90 secondi:
1. 3 Nodi storici o dormienti selezionati tramite la curva dell'oblio di Ebbinghaus.
2. 1 Tensione o contraddizione aperta da esaminare/risolvere.
3. 1 Modello mentale / Firmware cognitivo da applicare nella giornata.

Algoritmo di Oblio:
Score(v) = ln(1 + delta_days) * weight(layer) * (1 + 0.1 * degree) + random_jitter
"""

import os
import math
import json
import random
import sqlite3
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple
from contextlib import contextmanager

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


FIRMWARE_DAILY_ROTATION = [
    {
        "id": "firmware-first-principles",
        "name": "First Principles (Primi Principi)",
        "author": "Aristotele / Elon Musk",
        "question": "Quale problema complesso puoi ridurre ai suoi assiomi fisici ed economici fondamentali senza affidarti all'analogia?"
    },
    {
        "id": "firmware-inversion",
        "name": "Inversion (Inversione)",
        "author": "Charlie Munger / Carl Jacobi",
        "question": "Invece di chiederti come avere successo, chiediti: come potrei garantire il fallimento totale di questo progetto? Poi evita quelle cose."
    },
    {
        "id": "firmware-second-order",
        "name": "Second-Order Thinking (Pensiero del Secondo Ordine)",
        "author": "Howard Marks",
        "question": "E poi cosa succede? Quali sono le conseguenze a lungo termine non ovvie della decisione che stai per prendere oggi?"
    },
    {
        "id": "firmware-antifragility",
        "name": "Antifragility (Antifragilità)",
        "author": "Nassim Nicholas Taleb",
        "question": "Come può questo sistema/progetto non solo resistere al disordine e allo stress, ma trarne un vantaggio competitivo?"
    },
    {
        "id": "firmware-circle-of-competence",
        "name": "Circle of Competence (Cerchio di Competenza)",
        "author": "Warren Buffett",
        "question": "Sei dentro il tuo cerchio di vera competenza o stai operando nell'illusione della conoscenza?"
    },
    {
        "id": "firmware-opportunity-cost",
        "name": "Opportunity Cost (Costo Opportunità)",
        "author": "Economia Classica",
        "question": "A cosa stai rinunciando in questo preciso momento dicendo di sì a questa specifica attività o richiesta?"
    },
    {
        "id": "firmware-bayesian-updating",
        "name": "Bayesian Updating (Aggiornamento Bayesiano)",
        "author": "Thomas Bayes",
        "question": "Quale nuova prova o dato recente dovrebbe farti aggiornare la probabilità di successo della tua tesi iniziale?"
    },
    {
        "id": "firmware-pareto",
        "name": "Pareto Principle 80/20",
        "author": "Vilfredo Pareto",
        "question": "Qual è il 20% delle cause o del codice che genera l'80% del valore e dei risultati in questo progetto?"
    },
    {
        "id": "firmware-feynman",
        "name": "Feynman Technique (Tecnica di Feynman)",
        "author": "Richard Feynman",
        "question": "Riusciresti a spiegare questo concetto tecnico o decisione a un bambino di 10 anni senza usare gergo?"
    }
]


@contextmanager
def get_db_connection(db_path: str = DEFAULT_DB_PATH):
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    try:
        yield conn
    finally:
        conn.close()


def calculate_dormant_nodes(limit: int = 3, db_path: str = DEFAULT_DB_PATH) -> List[Dict[str, Any]]:
    """
    Calcola e seleziona i nodi storici più rilevanti da far riaffiorare (Daily Resurface).
    """
    with get_db_connection(db_path) as conn:
        query = """
            SELECT n.id, n.label, n.hemisphere, n.primary_label, n.layer_level, n.parent_graph_id, 
                   n.summary, n.details, n.tags, n.created_at, n.updated_at,
                   (
                       (SELECT COUNT(*) FROM edges WHERE source = n.id) +
                       (SELECT COUNT(*) FROM edges WHERE target = n.id)
                   ) AS degree
            FROM nodes n
            WHERE n.id != 'person-pierfrancesco' AND n.id != 'root'
            AND n.primary_label NOT IN ('ROOT_DOMAIN', 'DOMAIN');
        """
        rows = [dict(r) for r in conn.execute(query).fetchall()]
        if not rows:
            return []
            
        now = datetime.now(timezone.utc)
        scored_nodes = []
        
        for r in rows:
            up_str = r.get("updated_at") or r.get("created_at")
            days_dormant = 1.0
            if up_str:
                try:
                    # Gestione formati ISO standard e SQLite datetime
                    clean_str = up_str.replace("Z", "+00:00")
                    if "T" not in clean_str and " " in clean_str:
                        clean_str = clean_str.replace(" ", "T")
                    dt = datetime.fromisoformat(clean_str)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    days_dormant = max(0.5, (now - dt).total_seconds() / 86400.0)
                except Exception:
                    days_dormant = 7.0
                    
            layer = int(r.get("layer_level") or 2)
            layer_weight = 1.4 if layer == 1 else (1.1 if layer == 2 else 0.9)
            degree = int(r.get("degree") or 0)
            
            # Ebbinghaus score + degree + stochastic jitter
            score = (math.log(1.0 + days_dormant) * layer_weight * (1.0 + 0.08 * degree)) + random.uniform(0.0, 0.4)
            
            r["days_dormant"] = round(days_dormant, 1)
            r["resurface_score"] = round(score, 3)
            scored_nodes.append(r)
            
        scored_nodes.sort(key=lambda x: x["resurface_score"], reverse=True)
        return scored_nodes[:limit]


def get_daily_resurface_packet(db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """
    Costruisce l'intero pacchetto giornaliero per la Web Dashboard, Telegram e gli Agenti.
    """
    dormant_nodes = calculate_dormant_nodes(limit=3, db_path=db_path)
    
    # 1 Tensione aperta
    open_tension = None
    with get_db_connection(db_path) as conn:
        try:
            cur = conn.execute("""
                SELECT t.*, na.label as node_a_label, nb.label as node_b_label
                FROM tensions t
                LEFT JOIN nodes na ON t.node_a_id = na.id
                LEFT JOIN nodes nb ON t.node_b_id = nb.id
                WHERE t.status = 'OPEN'
                ORDER BY t.created_at ASC
                LIMIT 1;
            """)
            row = cur.fetchone()
            if row:
                open_tension = dict(row)
        except Exception:
            open_tension = None
            
    # Se non c'è una tensione aperta registrata, genera un candidato live
    if not open_tension:
        from brain_tensions import detect_candidate_tensions
        candidates = detect_candidate_tensions(db_path=db_path, limit=1)
        if candidates:
            c = candidates[0]
            open_tension = {
                "id": "candidate-tension",
                "node_a_label": c["node_a_label"],
                "node_b_label": c["node_b_label"],
                "tension_type": c["tension_type"],
                "description": c["description"],
                "status": "CANDIDATE"
            }
            
    # Seleziona il modello mentale del giorno (rotazione deterministica per giorno dell'anno)
    day_of_year = datetime.now().timetuple().tm_yday
    firmware_today = FIRMWARE_DAILY_ROTATION[day_of_year % len(FIRMWARE_DAILY_ROTATION)]
    
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "duration_seconds": 90,
        "resurface_nodes": dormant_nodes,
        "tension_of_the_day": open_tension,
        "firmware_of_the_day": firmware_today
    }


def format_telegram_morning_pulse(packet: Dict[str, Any]) -> str:
    """
    Formatta il briefing mattutino per Telegram in HTML conforme alle Bot API.
    """
    date_str = packet.get("date", datetime.now().strftime("%Y-%m-%d"))
    lines = [
        f"🧠 <b>DAILY BRAIN PULSE</b> · <i>{date_str}</i>",
        "<blockquote>⏱️ <b>Briefing Cognitivo di 90 Secondi</b></blockquote>",
        "\n📜 <b>3 NODI DALLA CURVA DELL'OBLIO:</b>"
    ]

    for i, n in enumerate(packet.get("resurface_nodes", []), 1):
        hemi_icon = "⚡" if n.get("hemisphere") == "LEFT" else "🌸"
        label = n.get("label", "Senza Titolo")
        node_id = n.get("id", "")
        summary = (n.get("summary") or "").strip()
        days = n.get("days_dormant", 0)
        lines.append(f"{i}. {hemi_icon} <b>{label}</b> (<code>{node_id}</code>)")
        lines.append(f"   <i>Dormiente da {days:.0f}gg:</i> {summary[:180]}...")

    tension = packet.get("tension_of_the_day")
    if tension:
        lines.append("\n⚡ <b>TENSIONE COGNITIVA DA ESAMINARE:</b>")
        lines.append(f"• <b>{tension.get('node_a_label', 'A')}</b> ⚔️ <b>{tension.get('node_b_label', 'B')}</b>")
        lines.append(f"  <i>{tension.get('description', '')}</i>")

    firmware = packet.get("firmware_of_the_day")
    if firmware:
        lines.append("\n🧭 <b>MODELLO MENTALE DEL GIORNO:</b>")
        lines.append(f"• <b>{firmware.get('name')}</b> (<i>{firmware.get('author')}</i>)")
        lines.append(f"  ❓ <code>{firmware.get('question')}</code>")

    lines.append("\n<i>Buona giornata produttiva, Pierfrancesco! 🚀</i>")
    return "\n".join(lines)


if __name__ == "__main__":
    packet = get_daily_resurface_packet()
    print(format_telegram_morning_pulse(packet))

