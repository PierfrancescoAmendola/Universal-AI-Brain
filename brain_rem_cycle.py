#!/usr/bin/env python3
"""
Nightly Cognitive REM Engine - Universal AI Brain
=================================================
Esegue autonomamente durante la notte (alle 03:00) il consolidamento della memoria,
la tessitura di sinapsi e ponti del Corpo Calloso, l'identificazione delle contraddizioni
e l'ottimizzazione del database SQLite WAL (100% Zero-Cost & Locale).

Ciclo a 4 Fasi:
1. 🕸️ Weave Consolidation: Identificazione e collegamento di nodi orfani e ponti callosali.
2. ⚡ Tension Sentinel: Rilevamento di tensioni e trade-off tra decisioni/principi opposti.
3. 📜 Memory Weights Refinement: Ricalcolo della freschezza e dei punteggi di riaffioramento.
4. 🧹 Vacuum & Health Audit: Manutenzione indici, pulizia e ottimizzazione dello storage.
"""

import sys
import os
import time
import json
import sqlite3
import logging
from datetime import datetime, timezone
from typing import Dict, Any, List

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


def run_rem_consolidation(db_path: str = DEFAULT_DB_PATH, auto_apply_weave: bool = True, verbose: bool = True) -> Dict[str, Any]:
    """Esegue l'intero ciclo REM di consolidamento cognitivo notturno."""
    start_time = time.perf_counter()
    report: Dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "phases_executed": [],
        "weaved_synapses": 0,
        "tensions_found": 0,
        "database_vacuumed": False,
        "elapsed_seconds": 0.0
    }

    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database brain.db non trovato in {db_path}")

    # -------------------------------------------------------------------------
    # FASE 1: Tessitura Sinaptica & Ponti Corpo Calloso (brain_weave.py)
    # -------------------------------------------------------------------------
    try:
        from brain_weave import compute_weave_proposals, apply_weave_links
        proposals = compute_weave_proposals(max_proposals=15, max_degree=2, db_path=db_path)
        
        applied_count = 0
        if auto_apply_weave and proposals:
            # Filtra solo le proposte con score elevato (score >= 2.0)
            high_conf = [p for p in proposals if p.get("score", 0) >= 2.0]
            if high_conf:
                apply_res = apply_weave_links(high_conf, db_path=db_path)
                applied_count = apply_res.get("links_applied", 0)

        report["weaved_synapses"] = applied_count
        report["phases_executed"].append({
            "name": "Phase 1: Weave Consolidation",
            "proposals_computed": len(proposals),
            "synapses_forged": applied_count
        })
    except Exception as e:
        report["phases_executed"].append({"name": "Phase 1: Weave Consolidation", "error": str(e)})

    # -------------------------------------------------------------------------
    # FASE 2: Rilevamento Tensioni Cognitive (brain_tensions.py)
    # -------------------------------------------------------------------------
    try:
        from brain_tensions import init_tensions_schema, detect_candidate_tensions
        conn = sqlite3.connect(db_path, timeout=5.0)
        conn.row_factory = sqlite3.Row
        init_tensions_schema(conn)
        conn.close()

        candidates = detect_candidate_tensions(db_path=db_path, limit=3)
        report["tensions_found"] = len(candidates)
        report["phases_executed"].append({
            "name": "Phase 2: Tension Sentinel",
            "candidate_tensions_detected": len(candidates)
        })
    except Exception as e:
        report["phases_executed"].append({"name": "Phase 2: Tension Sentinel", "error": str(e)})

    # -------------------------------------------------------------------------
    # FASE 3: Calcolo Punteggi di Riaffioramento Ebbinghaus (brain_resurface.py)
    # -------------------------------------------------------------------------
    try:
        from brain_resurface import get_daily_resurface_packet
        packet = get_daily_resurface_packet(db_path=db_path)
        report["phases_executed"].append({
            "name": "Phase 3: Ebbinghaus Scoring",
            "resurface_candidates": len(packet.get("resurface_nodes", [])),
            "active_firmware": packet.get("firmware_of_the_day", {}).get("name")
        })
    except Exception as e:
        report["phases_executed"].append({"name": "Phase 3: Ebbinghaus Scoring", "error": str(e)})

    # -------------------------------------------------------------------------
    # FASE 4: Manutenzione Indici SQLite WAL & Ottimizzazione Storage
    # -------------------------------------------------------------------------
    try:
        conn = sqlite3.connect(db_path, timeout=10.0)
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        conn.execute("ANALYZE;")
        conn.close()
        report["database_vacuumed"] = True
        report["phases_executed"].append({
            "name": "Phase 4: SQLite WAL Optimization",
            "status": "Checkpoint & Analyze Completed"
        })
    except Exception as e:
        report["phases_executed"].append({"name": "Phase 4: SQLite WAL Optimization", "error": str(e)})

    elapsed = time.perf_counter() - start_time
    report["elapsed_seconds"] = round(elapsed, 3)

    if verbose:
        print(f"🌙 [Fase REM Notturna] Ciclo completato in {elapsed:.3f}s:")
        print(f"  • Sinapsi tessute: +{report['weaved_synapses']}")
        print(f"  • Tensioni identificate: {report['tensions_found']}")
        print(f"  • Database ottimizzato: {'Sì' if report['database_vacuumed'] else 'No'}")

    return report


def main():
    print("🌙 Avvio manuale del Ciclo REM Notturno per Universal AI Brain...")
    res = run_rem_consolidation()
    print("✅ Risultato consolidamento:")
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
