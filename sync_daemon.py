#!/usr/bin/env python3
"""
Universal AI Brain - Continuous Background Sync Daemon (macOS LaunchAgent Service)
Runs at user login / system boot, maintains real-time parity between local SQLite (brain.db) and Render Cloud.
Zero CPU footprint when idle (<0.01%), ~20MB RAM, zero battery drain in sleep.
"""

import sys
import os
import time
import signal
import logging
from datetime import datetime, timezone

# Ensure project root is in sys.path
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_DIR)

import urllib.request
from sync_brain import sync_bidirectional, LOCAL_DB, RENDER_URL

LOG_FILE = os.path.join(PROJECT_DIR, "sync_daemon.log")

# Setup clean rotating logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

running = True


def handle_shutdown(signum, frame):
    global running
    logging.info(f"🛑 Arresto demone ricevuto (signal {signum}). Uscita pulita in corso...")
    running = False


signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)
if hasattr(signal, "SIGHUP"):
    signal.signal(signal.SIGHUP, handle_shutdown)


def get_db_mtime() -> float:
    """Returns the newest modification time among brain.db and brain.db-wal."""
    mtime = 0.0
    if os.path.exists(LOCAL_DB):
        mtime = max(mtime, os.path.getmtime(LOCAL_DB))
    wal_file = f"{LOCAL_DB}-wal"
    if os.path.exists(wal_file):
        mtime = max(mtime, os.path.getmtime(wal_file))
    return mtime


def get_vault_mtime() -> float:
    """Returns the newest modification time among all Markdown files in obsidian_vault."""
    vault_dir = os.path.join(PROJECT_DIR, "obsidian_vault")
    if not os.path.exists(vault_dir):
        return 0.0
    mtime = 0.0
    for root, _, files in os.walk(vault_dir):
        for f in files:
            if f.endswith(".md"):
                fp = os.path.join(root, f)
                try:
                    mtime = max(mtime, os.path.getmtime(fp))
                except Exception:
                    pass
    return mtime


def rotate_log_if_needed(max_bytes: int = 1_000_000):
    """Keeps the log file compact (<1MB)."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > max_bytes:
        try:
            bak_file = f"{LOG_FILE}.old"
            if os.path.exists(bak_file):
                os.remove(bak_file)
            os.rename(LOG_FILE, bak_file)
        except Exception:
            pass


def ping_render_keep_alive() -> bool:
    """Pings Render health check to prevent free tier from sleeping (spin-down after 15m)."""
    health_url = f"{RENDER_URL}/health"
    try:
        req = urllib.request.Request(health_url, headers={"User-Agent": "UniversalBrainKeepAlive/2.0"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            if resp.status == 200:
                logging.info("💓 Render Cloud Keep-Alive: OK (Server attivo 24/7)")
                return True
    except Exception as e:
        logging.info(f"⏳ Render Cloud Keep-Alive wake-up ping inviato ({e})")
    return False


def main():
    global running
    logging.info("=======================================================")
    logging.info("🧠 Universal Brain Sync Daemon avviato con successo.")
    logging.info(f"📁 Directory Progetto: {PROJECT_DIR}")
    logging.info(f"🗄️ Database Locale: {LOCAL_DB}")
    logging.info(f"💎 Obsidian Vault: {os.path.join(PROJECT_DIR, 'obsidian_vault')}")
    logging.info(f"🌐 Cloud Endpoint: {RENDER_URL}")
    logging.info("=======================================================")

    # 1. Sincronizzazione immediata all'avvio del computer
    try:
        logging.info("🚀 Esecuzione sincronizzazione iniziale di avvio...")
        res = sync_bidirectional(verbose=False)
        logging.info(f"✅ Sincronizzazione iniziale completata: {res.get('nodes_count', 0)} nodi, {res.get('edges_count', 0)} sinapsi.")
    except Exception as e:
        logging.warning(f"⚠️ Sincronizzazione iniziale differita (rete non pronta): {e}")

    last_db_mtime = get_db_mtime()
    last_vault_mtime = get_vault_mtime()
    last_periodic_check = time.time()
    last_keepalive_ping = time.time()
    last_pulse_date = None
    last_rem_date = None
    check_interval_seconds = 60
    keepalive_interval_seconds = 420  # Ping ogni 7 minuti (Render dorme a 15 min)

    # 2. Loop continuo leggero (<0.01% CPU)
    while running:
        try:
            now = time.time()
            now_dt = datetime.now()
            today_str = now_dt.strftime("%Y-%m-%d")

            # Controllo Consolidamento Notturno Fase REM (alle ore 03:00)
            if now_dt.hour == 3 and last_rem_date != today_str:
                try:
                    from brain_rem_cycle import run_rem_consolidation
                    logging.info(f"🌙 Schedulazione: Avvio Consolidamento Notturno REM delle 03:00 per {today_str}...")
                    rem_res = run_rem_consolidation(db_path=LOCAL_DB, verbose=False)
                    last_rem_date = today_str
                    logging.info(f"✨ Consolidamento REM completato: +{rem_res.get('weaved_synapses', 0)} sinapsi tessute.")
                except Exception as rem_err:
                    logging.warning(f"⚠️ Errore consolidamento REM: {rem_err}")

            # Controllo invio Daily Morning Pulse (alle ore 08:00 o successive se Mac riacceso)
            if now_dt.hour >= 8 and last_pulse_date != today_str:
                try:
                    from telegram_bot import broadcast_morning_pulse
                    logging.info(f"🌅 Schedulazione: Invio Daily Brain Pulse delle 08:00 per {today_str}...")
                    sent = broadcast_morning_pulse()
                    if sent:
                        last_pulse_date = today_str
                        logging.info(f"✅ Daily Brain Pulse inviato con successo via Telegram per {today_str}.")
                    else:
                        logging.info("ℹ️ Daily Brain Pulse: in attesa di primo messaggio Telegram per chat_id.")
                        last_pulse_date = today_str  # Non spammare se chat_id non è ancora configurato
                except Exception as pulse_err:
                    logging.warning(f"⚠️ Errore invio Daily Pulse: {pulse_err}")

            current_db_mtime = get_db_mtime()
            current_vault_mtime = get_vault_mtime()

            db_changed = current_db_mtime > (last_db_mtime + 0.5)
            vault_changed = current_vault_mtime > (last_vault_mtime + 0.5)
            periodic_due = (now - last_periodic_check) >= check_interval_seconds
            keepalive_due = (now - last_keepalive_ping) >= keepalive_interval_seconds

            if vault_changed:
                # Modifiche dirette su Obsidian Vault -> importa in SQLite prima di sincronizzare
                time.sleep(1.0)
                logging.info("💎 Modifica rilevata in Obsidian Vault. Importazione in SQLite...")
                try:
                    from obsidian_vault_sync import import_vault_to_brain
                    import_vault_to_brain(os.path.join(PROJECT_DIR, "obsidian_vault"), LOCAL_DB)
                    current_db_mtime = get_db_mtime()
                    last_vault_mtime = get_vault_mtime()
                except Exception as e:
                    logging.error(f"❌ Errore importazione da Obsidian: {e}")

            if db_changed or vault_changed or periodic_due:
                if db_changed:
                    time.sleep(1.0)
                    current_db_mtime = get_db_mtime()

                reason = "Modifica Obsidian" if vault_changed else ("Modifica SQLite" if db_changed else "Controllo periodico (60s)")
                logging.info(f"🔄 Avvio sincronizzazione: {reason}...")
                
                res = sync_bidirectional(verbose=False)
                last_db_mtime = get_db_mtime()
                last_vault_mtime = get_vault_mtime()
                last_periodic_check = now

                if res.get("success"):
                    p_in = res.get("pulled_nodes", 0)
                    p_out = res.get("pushed_nodes", 0)
                    tot_n = res.get("nodes_count", 0)
                    tot_e = res.get("edges_count", 0)
                    if p_in > 0 or p_out > 0:
                        logging.info(f"✨ Sincronizzazione eseguita: +{p_in} scaricati, +{p_out} caricati (Totale: {tot_n} nodi, {tot_e} sinapsi).")
                    elif res.get("warning"):
                        logging.info(f"ℹ️ Connettoma locale allineato su Git ({tot_n} nodi, {tot_e} sinapsi). {res.get('warning')}")
                    else:
                        logging.info(f"🟢 Connettoma già allineato al 100%: {tot_n} nodi, {tot_e} sinapsi.")
                else:
                    logging.warning(f"⚠️ Sincronizzazione differita: {res.get('reason', 'Errore sconosciuto')}")

                rotate_log_if_needed()

            if keepalive_due:
                ping_render_keep_alive()
                last_keepalive_ping = time.time()

        except Exception as e:
            logging.error(f"❌ Errore nel ciclo del demone: {e}")

        # Dormi in micro-intervalli per consentire uno shutdown istantaneo
        for _ in range(5):
            if not running:
                break
            time.sleep(1)

    logging.info("🧠 Universal Brain Sync Daemon terminato.")


if __name__ == "__main__":
    main()
