#!/usr/bin/env python3
"""
Script di Migrazione Backend - Opzione C (Ibrida con Backup)
Esegue:
1. Backup automatico del DB esistente
2. Applicazione PRAGMA avanzati (WAL, Busy Timeout, Synchronous)
3. Creazione Indici Critici (Edges source/target, Nodes hemisphere)
4. Analisi statistica per l'ottimizzatore di query
"""

import sqlite3
import shutil
import os
from datetime import datetime
from pathlib import Path

DB_PATH = "brain.db"
BACKUP_DIR = Path("backups")

def create_backup(db_path: str) -> str:
    """Crea un backup timestampato del database."""
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"brain_backup_{timestamp}.db"
    backup_path = BACKUP_DIR / backup_name
    
    print(f"🔄 Creazione backup in corso: {backup_path}...")
    shutil.copy2(db_path, backup_path)
    print(f"✅ Backup creato con successo: {backup_path}")
    return str(backup_path)

def optimize_database(db_path: str):
    """Applica ottimizzazioni SQLite critiche."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\n🚀 Applicazione PRAGMA avanzati...")
    pragmas = [
        ("journal_mode", "WAL"),
        ("synchronous", "NORMAL"),
        ("cache_size", "-64000"),  # 64MB cache
        ("temp_store", "MEMORY"),
        ("busy_timeout", "5000"),
        ("foreign_keys", "ON")
    ]
    
    for pragma, value in pragmas:
        cursor.execute(f"PRAGMA {pragma} = {value};")
        print(f"  ⚙️  PRAGMA {pragma} = {value}")
    
    print("\n📈 Creazione indici critici (se non esistenti)...")
    indices = [
        ("idx_edges_source", "edges", "source"),
        ("idx_edges_target", "edges", "target"),
        ("idx_nodes_hemisphere", "nodes", "hemisphere"),
        ("idx_nodes_primary_label", "nodes", "primary_label"),
        ("idx_edges_relation", "edges", "relation"),
        # Indice composito per query di adiacenza veloci
        ("idx_edges_source_relation", "edges", "source, relation"),
        ("idx_edges_target_relation", "edges", "target, relation"),
    ]
    
    for idx_name, table, column in indices:
        try:
            sql = f"CREATE INDEX IF NOT EXISTS {idx_name} ON {table}({column});"
            cursor.execute(sql)
            print(f"  📑 Indice creato: {idx_name} su {table}({column})")
        except Exception as e:
            print(f"  ⚠️  Errore creazione indice {idx_name}: {e}")
    
    print("\n🔍 Esecuzione ANALYZE per aggiornare statistiche query planner...")
    cursor.execute("ANALYZE;")
    print("  ✅ Statistiche aggiornate.")
    
    conn.commit()
    
    # Verifica finale
    print("\n📊 Verifica configurazione finale...")
    checks = ["journal_mode", "synchronous", "busy_timeout"]
    for check in checks:
        res = cursor.execute(f"PRAGMA {check};").fetchone()[0]
        print(f"  ✔️  {check}: {res}")
    
    conn.close()
    print("\n🎉 Migrazione completata con successo!")

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print(f"❌ Errore: Database {DB_PATH} non trovato.")
        exit(1)
    
    try:
        backup_file = create_backup(DB_PATH)
        optimize_database(DB_PATH)
        print(f"\n💾 Backup sicuro disponibile in: {backup_file}")
    except Exception as e:
        print(f"\n❌ Errore critico durante la migrazione: {e}")
        print("Il database originale è intatto. Ripristina dal backup se necessario.")
        exit(1)
