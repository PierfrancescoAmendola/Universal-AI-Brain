#!/usr/bin/env python3
"""
Cognitive Firmware Engine (9 Mental Models) - Universal AI Brain
===============================================================
Fornisce 9 framework mentali di ragionamento operativo (Firmware Cognitivo)
per analizzare decisioni, codice, architetture e strategie senza bias.

I 9 Firmware:
1. INVERSION (Munger / Jacobi)
2. SECOND_ORDER (Howard Marks)
3. FIRST_PRINCIPLES (Aristotele / Musk)
4. CIRCLE_OF_COMPETENCE (Buffett)
5. OPPORTUNITY_COST (Economia Classica)
6. ANTIFRAGILITY (Taleb)
7. BAYESIAN_UPDATING (Bayes)
8. PARETO (Pareto 80/20)
9. FEYNMAN (Feynman)
"""

import os
import json
import sqlite3
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


FIRMWARE_REGISTRY: Dict[str, Dict[str, Any]] = {
    "inversion": {
        "id": "firmware-inversion",
        "name": "Inversion (Inversione)",
        "author": "Charlie Munger & Carl Jacobi",
        "hemisphere": "LEFT",
        "parent_domain": "domain-ai-cognitive-systems",
        "tagline": "Non cercare solo come vincere; definisci come perdere e poi evitalo rigorosamente.",
        "steps": [
            "1. Definisci il fallimento catastrofico o lo scenario peggiore per questo problema.",
            "2. Elenca le 3-5 azioni o assunzioni che causerebbero direttamente quel disastro.",
            "3. Trasforma ciascuna causa di fallimento in una guardia difensiva o vincolo vincolante.",
            "4. Riorganizza il piano d'azione per eliminare prima i punti di rottura irreversibili."
        ]
    },
    "second_order": {
        "id": "firmware-second-order",
        "name": "Second-Order Thinking (Pensiero del Secondo Ordine)",
        "author": "Howard Marks",
        "hemisphere": "LEFT",
        "parent_domain": "domain-ai-cognitive-systems",
        "tagline": "E poi cosa succede? Valuta le conseguenze delle conseguenze a medio-lungo termine.",
        "steps": [
            "1. Individua l'effetto immediato di 1° ordine (es. aumento velocità o riduzione costi).",
            "2. Domanda: 'E poi cosa accade a cascata?' (Effetti di 2° ordine su complessità, debito tecnico, carico cognitivo).",
            "3. Proietta gli effetti di 3° ordine (incentivi perversi, reazioni del sistema, scalabilità nel tempo).",
            "4. Valuta se il guadagno a breve termine giustifica l'entropia a lungo termine."
        ]
    },
    "first_principles": {
        "id": "firmware-first-principles",
        "name": "First Principles (Primi Principi)",
        "author": "Aristotele & Elon Musk",
        "hemisphere": "LEFT",
        "parent_domain": "domain-ai-cognitive-systems",
        "tagline": "Riduci il problema ai suoi assiomi fisici/logici essenziali senza affidarti all'analogia.",
        "steps": [
            "1. Isola le credenze convenzionali o le pratiche 'standard' accettate per abitudine.",
            "2. Riduci il problema alle uniche verità indiscutibili e non negoziabili (leggi fisiche, logica, risorse atomiche).",
            "3. Ricostruisci una soluzione da zero (bottom-up) partendo solo da quegli assiomi.",
            "4. Elimina ogni strato superfluo derivato da conformismo o abitudine storica."
        ]
    },
    "circle_of_competence": {
        "id": "firmware-circle-of-competence",
        "name": "Circle of Competence (Cerchio di Competenza)",
        "author": "Warren Buffett & Charlie Munger",
        "hemisphere": "LEFT",
        "parent_domain": "domain-produttivita-sistemi",
        "tagline": "Definisci con precisione chirurgica ciò che sai e ammetti ciò che ignori.",
        "steps": [
            "1. Traccia il confine esatto: quali parti di questo problema padroneggi con certezza empirica?",
            "2. Dichiara esplicitamente le zone d'ombra, le dipendenze da terze parti e le incognite.",
            "3. Rifiuta di prendere decisioni definitive al di fuori del perimetro senza aver prima acquisito evidenza verificabile.",
            "4. Affidati a esperti, fallback difensivi o isolamento modulare per la parte sconosciuta."
        ]
    },
    "opportunity_cost": {
        "id": "firmware-opportunity-cost",
        "name": "Opportunity Cost (Costo Opportunità)",
        "author": "Economia Classica",
        "hemisphere": "LEFT",
        "parent_domain": "domain-finanza-economia",
        "tagline": "Il vero costo di una scelta è il valore della migliore alternativa a cui rinunci.",
        "steps": [
            "1. Identifica l'azione proposta e le risorse richieste (tempo, concentrazione, CPU, budget).",
            "2. Elenca le 2 migliori alternative escluse se dedichi le risorse a questa scelta.",
            "3. Calcola il ROI differenziale tra la scelta e le alternative.",
            "4. Procedi solo se il valore netto atteso supera la migliore alternativa sacrificata."
        ]
    },
    "antifragility": {
        "id": "firmware-antifragility",
        "name": "Antifragility (Antifragilità)",
        "author": "Nassim Nicholas Taleb",
        "hemisphere": "RIGHT",
        "parent_domain": "domain-filosofia-valori",
        "tagline": "Trarre vantaggio dal disordine, dagli errori e dalla volatilità anziché limitarsi a resistervi.",
        "steps": [
            "1. Isola le asimmetrie: dove hai un limite di perdita noto (downside cappato) e un potenziale di guadagno illimitato (upside aperto)?",
            "2. Progetta un meccanismo di feedback loop che trasformi ogni bug, errore o fallimento in una regola/test automatizzato permanente.",
            "3. Elimina le fragilità da singolo punto di rottura (Single Point of Failure).",
            "4. Aggiungi ridondanza strategica e modularità disaccoppiata."
        ]
    },
    "bayesian_updating": {
        "id": "firmware-bayesian-updating",
        "name": "Bayesian Updating (Aggiornamento Bayesiano)",
        "author": "Thomas Bayes",
        "hemisphere": "LEFT",
        "parent_domain": "domain-scienza-matematica",
        "tagline": "Aggiorna la probabilità della tua tesi iniziale in proporzione alle nuove evidenze.",
        "steps": [
            "1. Dichiara la tua ipotesi/credenza a priori (Prior Probability P(H)).",
            "2. Valuta la forza e la veridicità delle nuove prove osservate (Likelihood P(E|H)).",
            "3. Ricalibra la probabilità a posteriori (Posterior P(H|E)) senza arroccarsi su dogmi pregressi.",
            "4. Modifica la rotta d'azione se la probabilità aggiornata scende sotto la soglia di sicurezza."
        ]
    },
    "pareto": {
        "id": "firmware-pareto",
        "name": "Pareto Principle (80/20)",
        "author": "Vilfredo Pareto",
        "hemisphere": "LEFT",
        "parent_domain": "domain-produttivita-sistemi",
        "tagline": "Il 20% delle cause genera l'80% degli effetti. Trova quel 20% vitale ed elimina l'80% banale.",
        "steps": [
            "1. Isola l'elenco di tutte le feature, componenti o task sul tavolo.",
            "2. Identifica il 20% che sblocca direttamente l'80% del valore percepito o delle prestazioni.",
            "3. Esegui subito quel 20% critico con massima dedizione.",
            "4. Taglia, rimanda o automatizza il restante 80% secondario."
        ]
    },
    "feynman": {
        "id": "firmware-feynman",
        "name": "Feynman Technique (Tecnica di Feynman)",
        "author": "Richard Feynman",
        "hemisphere": "RIGHT",
        "parent_domain": "domain-crescita-personale",
        "tagline": "Se non riesci a spiegarlo in termini semplici a un profano, non lo hai compreso a fondo.",
        "steps": [
            "1. Spiega il concetto, architettura o bug in linguaggio naturale chiarissimo, come a un bambino di 10 anni.",
            "2. Individua i passaggi in cui sei costretto a ricorrere a gergo tecnico complicato per mascherare un vuoto concettuale.",
            "3. Torna alla sorgente per chiarire quel punto esatto finché non diventa trasparente.",
            "4. Usa analogie intuitive e riduci la spiegazione alla sua pura essenza."
        ]
    }
}


def get_db_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def seed_firmware_nodes_in_brain(db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """
    Assicura che tutti i 9 modelli mentali siano nodi permanenti del Palazzo Cognitivo.
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        count = 0
        for key, fw in FIRMWARE_REGISTRY.items():
            node_id = fw["id"]
            label = fw["name"]
            hemi = fw["hemisphere"]
            parent = fw["parent_domain"]
            summary = fw["tagline"]
            details_json = json.dumps({
                "author": fw["author"],
                "reasoning_steps": fw["steps"]
            }, ensure_ascii=False)
            tags_json = json.dumps(["firmware", "mental-model", key], ensure_ascii=False)
            
            now_iso = datetime.now(timezone.utc).isoformat()
            cursor.execute("""
                INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, details, tags, confidence, created_at, updated_at)
                VALUES (?, ?, ?, 'MENTAL_MODEL', 'MENTAL_MODEL', 2, ?, ?, ?, ?, 'EXTRACTED', ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    label = excluded.label,
                    summary = excluded.summary,
                    details = excluded.details,
                    tags = excluded.tags,
                    updated_at = excluded.updated_at;
            """, (node_id, label, hemi, parent, summary, details_json, tags_json, now_iso, now_iso))
            
            # Collega al dominio genitore
            cursor.execute("""
                INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning)
                VALUES (?, ?, 'BELONGS_TO_DOMAIN', 'EXTRACTED', 'Modello mentale del dominio');
            """, (node_id, parent))
            count += 1
            
        conn.commit()
        return {"status": "success", "firmware_seeded": count}


def list_available_firmware() -> List[Dict[str, Any]]:
    """Restituisce la lista di tutti i 9 modelli mentali registrati."""
    return [
        {
            "key": k,
            "id": v["id"],
            "name": v["name"],
            "author": v["author"],
            "hemisphere": v["hemisphere"],
            "tagline": v["tagline"],
            "steps": v["steps"]
        }
        for k, v in FIRMWARE_REGISTRY.items()
    ]


def apply_firmware_lens(mode: str, problem: str, context: Optional[str] = None) -> Dict[str, Any]:
    """
    Applica una delle 9 lenti cognitive ad un problema o decisione,
    restituendo le direttive formali di ragionamento per l'agente AI.
    """
    clean_mode = mode.strip().lower().replace("-", "_").replace(" ", "_")
    if clean_mode not in FIRMWARE_REGISTRY:
        # Cerca per corrispondenza parziale
        for k in FIRMWARE_REGISTRY:
            if clean_mode in k or k in clean_mode:
                clean_mode = k
                break
        else:
            return {
                "status": "error",
                "message": f"Modello firmware '{mode}' non trovato. Disponibili: {list(FIRMWARE_REGISTRY.keys())}"
            }
            
    fw = FIRMWARE_REGISTRY[clean_mode]
    
    prompt_directive = f"""
# 🧭 APPLICAZIONE FIRMWARE COGNITIVO: {fw['name'].upper()}
> **Autore/Origine:** {fw['author']}  
> **Principio Guida:** _{fw['tagline']}_

## 🎯 Problema / Decisione da Esaminare:
{problem}
"""
    if context:
        prompt_directive += f"\n## 📋 Contesto Aggiuntivo:\n{context}\n"

    prompt_directive += "\n## ⚡ Protocollo di Ragionamento a 4 Passi:\n"
    for step in fw["steps"]:
        prompt_directive += f"- {step}\n"
        
    return {
        "status": "success",
        "firmware_key": clean_mode,
        "firmware_name": fw["name"],
        "author": fw["author"],
        "directive": prompt_directive,
        "steps": fw["steps"]
    }


if __name__ == "__main__":
    res = seed_firmware_nodes_in_brain()
    print(f"Firmware registrati in brain.db: {res}")
    app = apply_firmware_lens("inversion", "Come progettare un'app mobile a prova di bug e senza latenza?")
    print(app["directive"])
