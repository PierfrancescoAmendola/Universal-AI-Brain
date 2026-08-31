#!/usr/bin/env python3
"""
Obsidian Vault Bidirectional Sync Engine - Universal AI Brain
=============================================================
Sincronizza in modo trasparente e bidirezionale il Connettoma Cognitivo (SQLite WAL)
con un Vault Obsidian locale strutturato a note atomiche Markdown.

Caratteristiche:
1. Gerarchia del Palazzo Cognitivo a 3 Cartelle:
   - 00_Domini/           (Piano 0: Macro-Domini immutabili)
   - 01_Progetti_Episodi/ (Piano 1: Progetti, USER_INTENT, AI_REASONING, CONVERSATION_EPISODE)
   - 02_Moduli_Atomici/   (Piano 2: Funzioni, Algoritmi, Regole, Token, Note)
2. Frontmatter YAML standard (id, label, hemisphere, primary_label, layer_level, parent_graph_id, tags, confidence, updated_at).
3. Wikilinks bidirezionali nativi di Obsidian: [[target-node-id]] con relazione sinaptica.
4. Parsing ed esportazione ad altissima velocità con zero dipendenze esterne obbligatorie.
5. Indice centrale 00_INDEX.md con visuale bi-emisferica e mappa di navigazione rapida.
"""

import os
import re
import sys
import json
import sqlite3
import argparse
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Optional, Set

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))
DEFAULT_VAULT_DIR = os.getenv("OBSIDIAN_VAULT_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "obsidian_vault"))


# -----------------------------------------------------------------------------
# YAML Frontmatter Serialization & Parsing (Zero External Dependencies)
# -----------------------------------------------------------------------------

def serialize_frontmatter(meta: Dict[str, Any]) -> str:
    """Serializza un dizionario in un blocco YAML frontmatter pulito."""
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, list):
            items_str = ", ".join([f'"{item}"' if any(c in str(item) for c in ':,[]{}#') else str(item) for item in v])
            lines.append(f"{k}: [{items_str}]")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, str):
            if "\n" in v or any(c in v for c in ':"{}[]#@|'):
                escaped = v.replace('"', '\\"')
                lines.append(f'{k}: "{escaped}"')
            else:
                lines.append(f"{k}: {v}")
        elif isinstance(v, dict):
            compact_json = json.dumps(v, ensure_ascii=False)
            lines.append(f'{k}: \'{compact_json}\'')
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Estrae il blocco frontmatter YAML e il corpo Markdown dal contenuto di una nota."""
    if not content.startswith("---"):
        return {}, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    fm_raw = parts[1].strip()
    body = parts[2].strip()
    meta: Dict[str, Any] = {}
    
    for line in fm_raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        
        # Gestione booleani e numeri
        if val.lower() == "true":
            meta[key] = True
        elif val.lower() == "false":
            meta[key] = False
        elif val.isdigit():
            meta[key] = int(val)
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                meta[key] = []
            else:
                items = [re.sub(r'^["\']|["\']$', '', item.strip()) for item in inner.split(",") if item.strip()]
                meta[key] = items
        elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            meta[key] = val[1:-1].replace('\\"', '"').replace("\\'", "'")
        else:
            meta[key] = val
            
    return meta, body


def sanitize_filename(name: str) -> str:
    """Rende sicuro un nome di file per il filesystem preservando i caratteri leggibili."""
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
    return cleaned.strip().strip('.') or "untitled"


# -----------------------------------------------------------------------------
# Cartelle del Palazzo Cognitivo
# -----------------------------------------------------------------------------

def get_folder_for_node(layer_level: int, primary_label: str, category: str) -> str:
    """Mappa un nodo nella cartella corrispondente del Palazzo Cognitivo."""
    if layer_level == 0 or category == "ROOT_DOMAIN" or primary_label in ("ROOT_DOMAIN", "DOMAIN"):
        return "00_Domini"
    elif layer_level == 1 or primary_label in ("USER_INTENT", "AI_REASONING", "CONVERSATION_EPISODE", "PROJECT"):
        return "01_Progetti_Episodi"
    else:
        return "02_Moduli_Atomici"


# -----------------------------------------------------------------------------
# Esportazione da SQLite a Vault Obsidian
# -----------------------------------------------------------------------------

def export_brain_to_vault(db_path: str = DEFAULT_DB_PATH, vault_dir: str = DEFAULT_VAULT_DIR) -> Dict[str, Any]:
    """
    Esporta l'intero connettoma SQLite WAL in una directory Obsidian Vault
    con note atomiche, frontmatter YAML, wikilinks [[...]] e gerarchia.
    """
    if not os.path.exists(db_path):
        return {"status": "error", "message": f"Database non trovato in {db_path}"}
    
    os.makedirs(vault_dir, exist_ok=True)
    folders = ["00_Domini", "01_Progetti_Episodi", "02_Moduli_Atomici"]
    for f in folders:
        os.makedirs(os.path.join(vault_dir, f), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    try:
        # Carica tutti i nodi
        nodes_cursor = conn.execute("SELECT * FROM nodes ORDER BY layer_level, id")
        nodes = [dict(r) for r in nodes_cursor.fetchall()]
        
        # Carica tutti gli archi
        edges_cursor = conn.execute("SELECT * FROM edges")
        edges = [dict(r) for r in edges_cursor.fetchall()]
        
        # Raggruppa archi per source e target
        outgoing_edges: Dict[str, List[Dict[str, Any]]] = {}
        incoming_edges: Dict[str, List[Dict[str, Any]]] = {}
        
        for e in edges:
            src = e["source"]
            tgt = e["target"]
            outgoing_edges.setdefault(src, []).append(e)
            incoming_edges.setdefault(tgt, []).append(e)
            
        exported_count = 0
        
        for node in nodes:
            node_id = node["id"]
            label = node["label"] or node_id
            hemisphere = node["hemisphere"] or "LEFT"
            primary_label = node["primary_label"] or "CONCEPT"
            category = node["category"] or primary_label
            layer_level = int(node["layer_level"] if node["layer_level"] is not None else 2)
            parent_graph_id = node["parent_graph_id"] or "root"
            summary = node["summary"] or ""
            confidence = node["confidence"] or "EXTRACTED"
            updated_at = node.get("updated_at") or node.get("created_at") or datetime.now(timezone.utc).isoformat()
            
            # Gestione tags
            raw_tags = node.get("tags")
            tags: List[str] = []
            if raw_tags:
                try:
                    tags = json.loads(raw_tags) if isinstance(raw_tags, str) else list(raw_tags)
                except Exception:
                    tags = [t.strip() for t in str(raw_tags).split(",") if t.strip()]
            
            # Gestione details
            details_dict: Dict[str, Any] = {}
            raw_details = node.get("details")
            if raw_details:
                try:
                    details_dict = json.loads(raw_details) if isinstance(raw_details, str) else dict(raw_details)
                except Exception:
                    details_dict = {"raw": str(raw_details)}
                    
            folder_name = get_folder_for_node(layer_level, primary_label, category)
            file_name = f"{sanitize_filename(node_id)}.md"
            file_path = os.path.join(vault_dir, folder_name, file_name)
            
            # Costruisci frontmatter
            frontmatter_data = {
                "id": node_id,
                "label": label,
                "hemisphere": hemisphere,
                "primary_label": primary_label,
                "category": category,
                "layer_level": layer_level,
                "parent_graph_id": parent_graph_id,
                "tags": tags,
                "confidence": confidence,
                "updated_at": updated_at
            }
            
            # Costruisci corpo markdown
            body_lines = [
                f"# {label}",
                "",
                f"> **Emisfero:** {'⚡ Sinistro (Logic & Tech)' if hemisphere == 'LEFT' else '🌸 Destro (Art & Values)'}  ",
                f"> **Categoria:** `{primary_label}` | **Piano:** {layer_level} | **Padre:** [[{parent_graph_id}]]",
                "",
                "## 📝 Sintesi",
                summary if summary else "_Nessuna sintesi disponibile._",
                ""
            ]
            
            if details_dict:
                body_lines.append("## 📋 Dettagli Strutturati")
                # Se presente percorso locale, metti subito il link cliccabile
                if "file_uri" in details_dict or "local_path" in details_dict:
                    uri = details_dict.get("file_uri") or f"file://{details_dict.get('local_path')}"
                    body_lines.append(f"- **📂 Percorso Mac:** [{uri}]({uri})")
                for k, v in details_dict.items():
                    if k in ("file_uri", "local_path"):
                        continue
                    if isinstance(v, list):
                        body_lines.append(f"- **{k}:**")
                        for item in v:
                            body_lines.append(f"  - {item}")
                    elif isinstance(v, dict):
                        body_lines.append(f"- **{k}:**")
                        for sub_k, sub_v in v.items():
                            body_lines.append(f"  - `{sub_k}`: {sub_v}")
                    else:
                        body_lines.append(f"- **{k}:** {v}")
                body_lines.append("")
                
            # Sinapsi Uscenti
            out_list = outgoing_edges.get(node_id, [])
            if out_list:
                body_lines.append("## 🔗 Connessioni Uscenti")
                for oe in out_list:
                    rel = oe.get("relation", "CONNECTS_TO")
                    tgt = oe.get("target", "")
                    reason = oe.get("reasoning", "")
                    reason_text = f" — _{reason}_" if reason else ""
                    body_lines.append(f"- [[{tgt}]] (`{rel}`){reason_text}")
                body_lines.append("")
                
            # Sinapsi Entranti (Backlinks)
            in_list = incoming_edges.get(node_id, [])
            if in_list:
                body_lines.append("## 📥 Connessioni Entranti (Backlinks)")
                for ie in in_list:
                    rel = ie.get("relation", "CONNECTS_TO")
                    src = ie.get("source", "")
                    reason = ie.get("reasoning", "")
                    reason_text = f" — _{reason}_" if reason else ""
                    body_lines.append(f"- [[{src}]] (`{rel}`){reason_text}")
                body_lines.append("")
                
            full_content = serialize_frontmatter(frontmatter_data) + "\n\n" + "\n".join(body_lines)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(full_content)
                
            exported_count += 1
            
        # Genera Indice 00_INDEX.md
        index_path = os.path.join(vault_dir, "00_INDEX.md")
        left_nodes = [n for n in nodes if (n.get("hemisphere") or "LEFT") == "LEFT"]
        right_nodes = [n for n in nodes if (n.get("hemisphere") or "LEFT") == "RIGHT"]
        domains = [n for n in nodes if int(n.get("layer_level") or 2) == 0]
        projects = [n for n in nodes if int(n.get("layer_level") or 2) == 1 and n.get("primary_label") in ("PROJECT", "APP", "SCRIPT_TOOL", "REPOSITORY")]
        
        index_lines = [
            "# 🧠 Universal AI Brain — Obsidian Knowledge Vault",
            "> **Persistent Bi-Hemispheric Knowledge Graph & Cognitive Palace**",
            "",
            f"**Totale Nodi:** {len(nodes)} | **Emisfero Sinistro (⚡):** {len(left_nodes)} | **Emisfero Destro (🌸):** {len(right_nodes)} | **Sinapsi:** {len(edges)}",
            f"_Ultima Sincronizzazione: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}_",
            "",
            "---",
            "",
            "## 🏛️ Piano 0: I 12 Macro-Domini Fondativi (Attico)",
            ""
        ]
        
        for d in domains:
            icon = "⚡" if d.get("hemisphere") == "LEFT" else "🌸"
            index_lines.append(f"- {icon} [[{d['id']}]] — **{d['label']}**: {d.get('summary', '')}")
            
        if projects:
            index_lines.extend([
                "",
                "---",
                "",
                "## 💻 Piano 1: I Tuoi Progetti & App sul Mac",
                ""
            ])
            for p in projects:
                icon = "⚡" if p.get("hemisphere") == "LEFT" else "🌸"
                index_lines.append(f"- {icon} [[{p['id']}]] — **{p['label']}** (`{p.get('primary_label')}`): {p.get('summary', '')}")

        index_lines.extend([
            "",
            "---",
            "",
            "## 📂 Mappa delle Cartelle",
            "- `00_Domini/`: I Macro-Domini Fondativi (Piano 0).",
            "- `01_Progetti_Episodi/`: Progetti attivi, Intenti Utente (`USER_INTENT`), Ragionamenti AI (`AI_REASONING`) ed Episodi di Dialogo (`CONVERSATION_EPISODE`).",
            "- `02_Moduli_Atomici/`: Funzioni, Algoritmi, Regole Cognitive, Token di Design e componenti atomici.",
            "",
            "---",
            "_Sincronizzato automaticamente dal demone Universal AI Brain._"
        ])
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(index_lines))
            
        return {
            "status": "success",
            "nodes_exported": exported_count,
            "edges_indexed": len(edges),
            "vault_dir": vault_dir
        }
    finally:
        conn.close()


# -----------------------------------------------------------------------------
# Importazione da Vault Obsidian a SQLite
# -----------------------------------------------------------------------------

def import_vault_to_brain(vault_dir: str = DEFAULT_VAULT_DIR, db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """
    Scansiona tutte le note Markdown nel vault Obsidian ed esegue l'upsert
    nel database SQLite WAL, ricostruendo nodi, dettagli e archi dai wikilink [[...]].
    """
    if not os.path.exists(vault_dir):
        return {"status": "error", "message": f"Vault Obsidian non trovato in {vault_dir}"}
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    
    try:
        nodes_to_upsert: List[Dict[str, Any]] = []
        edges_to_upsert: List[Dict[str, Any]] = []
        wikilink_pattern = re.compile(r'\[\[([a-zA-Z0-9_\-\.\s]+)\]\](?:\s*\(`?([A-Z_]+)`?\))?(?:\s*—\s*_([^_]+)_)?')
        
        for root, _, files in os.walk(vault_dir):
            for file in files:
                if not file.endswith(".md") or file == "00_INDEX.md":
                    continue
                    
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                meta, body = parse_frontmatter(content)
                node_id = meta.get("id") or os.path.splitext(file)[0]
                label = meta.get("label") or node_id
                hemisphere = meta.get("hemisphere") or "LEFT"
                primary_label = meta.get("primary_label") or "CONCEPT"
                category = meta.get("category") or primary_label
                layer_level = int(meta.get("layer_level", 2))
                parent_graph_id = meta.get("parent_graph_id") or "root"
                confidence = meta.get("confidence") or "EXTRACTED"
                tags = meta.get("tags") or []
                
                # Estrazione sintesi dal body
                summary = ""
                summary_match = re.search(r'##\s*📝\s*Sintesi\s*\n(.*?)(?=\n##|$)', body, re.DOTALL)
                if summary_match:
                    summary = summary_match.group(1).strip()
                elif meta.get("summary"):
                    summary = meta["summary"]
                else:
                    # Fallback prime righe dopo header
                    lines_after_h1 = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#") and not l.startswith(">")]
                    summary = lines_after_h1[0] if lines_after_h1 else label
                    
                # Estrazione dettagli strutturati dal body
                details_dict: Dict[str, Any] = {}
                details_match = re.search(r'##\s*📋\s*Dettagli Strutturati\s*\n(.*?)(?=\n##|$)', body, re.DOTALL)
                if details_match:
                    for d_line in details_match.group(1).splitlines():
                        kv = re.match(r'^\s*-\s*\*\*([^\*]+)\*\*:\s*(.*)$', d_line)
                        if kv:
                            k = kv.group(1).strip()
                            v = kv.group(2).strip()
                            details_dict[k] = v
                elif meta.get("details"):
                    try:
                        details_dict = json.loads(meta["details"]) if isinstance(meta["details"], str) else meta["details"]
                    except Exception:
                        details_dict = {"raw": str(meta["details"])}
                        
                nodes_to_upsert.append({
                    "id": node_id,
                    "label": label,
                    "hemisphere": hemisphere,
                    "primary_label": primary_label,
                    "category": category,
                    "layer_level": layer_level,
                    "parent_graph_id": parent_graph_id,
                    "summary": summary,
                    "details": json.dumps(details_dict, ensure_ascii=False),
                    "tags": json.dumps(tags, ensure_ascii=False) if isinstance(tags, list) else str(tags),
                    "confidence": confidence,
                    "updated_at": datetime.now(timezone.utc).isoformat()
                })
                
                # Estrazione wikilink per archi uscenti
                out_match = re.search(r'##\s*🔗\s*Connessioni Uscenti\s*\n(.*?)(?=\n##|$)', body, re.DOTALL)
                if out_match:
                    for link_line in out_match.group(1).splitlines():
                        for match in wikilink_pattern.finditer(link_line):
                            tgt = match.group(1).strip()
                            rel = match.group(2) or "CONNECTS_TO"
                            reasoning = match.group(3) or ""
                            edges_to_upsert.append({
                                "source": node_id,
                                "target": tgt,
                                "relation": rel,
                                "confidence": "EXTRACTED",
                                "reasoning": reasoning
                            })
                            
        # Inserimento atomico nel DB SQLite
        cursor = conn.cursor()
        for n in nodes_to_upsert:
            cursor.execute("""
                INSERT INTO nodes (id, label, hemisphere, primary_label, category, layer_level, parent_graph_id, summary, details, tags, confidence, updated_at)
                VALUES (:id, :label, :hemisphere, :primary_label, :category, :layer_level, :parent_graph_id, :summary, :details, :tags, :confidence, :updated_at)
                ON CONFLICT(id) DO UPDATE SET
                    label = excluded.label,
                    hemisphere = excluded.hemisphere,
                    primary_label = excluded.primary_label,
                    category = excluded.category,
                    layer_level = excluded.layer_level,
                    parent_graph_id = excluded.parent_graph_id,
                    summary = excluded.summary,
                    details = excluded.details,
                    tags = excluded.tags,
                    confidence = excluded.confidence,
                    updated_at = excluded.updated_at;
            """, n)
            
            # Sincronizza anche FTS5
            try:
                cursor.execute("DELETE FROM nodes_fts WHERE id = ?", (n["id"],))
                cursor.execute("""
                    INSERT INTO nodes_fts (id, label, summary, tags)
                    VALUES (?, ?, ?, ?);
                """, (n["id"], n["label"], n["summary"], n["tags"]))
            except Exception:
                pass
                
        # Inserisci archi estratti
        for e in edges_to_upsert:
            cursor.execute("""
                INSERT OR IGNORE INTO edges (source, target, relation, confidence, reasoning)
                VALUES (:source, :target, :relation, :confidence, :reasoning);
            """, e)
            
        conn.commit()
        return {
            "status": "success",
            "nodes_imported": len(nodes_to_upsert),
            "edges_imported": len(edges_to_upsert),
            "vault_dir": vault_dir
        }
    finally:
        conn.close()


# -----------------------------------------------------------------------------
# Sincronizzazione Bidirezionale Intelligente
# -----------------------------------------------------------------------------

def sync_bidirectional(vault_dir: str = DEFAULT_VAULT_DIR, db_path: str = DEFAULT_DB_PATH) -> Dict[str, Any]:
    """
    Esegue una sincronizzazione bidirezionale:
    1. Se il vault non esiste o il DB è più recente, esporta dal DB al Vault.
    2. Se ci sono file modificati nel Vault, importa nel DB e riesporta l'indice.
    """
    if not os.path.exists(vault_dir):
        return export_brain_to_vault(db_path, vault_dir)
        
    db_mtime = os.path.getmtime(db_path) if os.path.exists(db_path) else 0
    
    # Trova il file più recente nel vault
    vault_mtime = 0
    for root, _, files in os.walk(vault_dir):
        for file in files:
            if file.endswith(".md"):
                fp = os.path.join(root, file)
                mt = os.path.getmtime(fp)
                if mt > vault_mtime:
                    vault_mtime = mt
                    
    if vault_mtime > db_mtime + 2.0:
        # Il vault ha modifiche più recenti del DB: importa
        imp_res = import_vault_to_brain(vault_dir, db_path)
        # Riesporta per mantenere consistente la formattazione
        exp_res = export_brain_to_vault(db_path, vault_dir)
        return {
            "action": "imported_from_vault_then_exported",
            "import_result": imp_res,
            "export_result": exp_res
        }
    else:
        # Il DB è più recente o allineato: esporta
        exp_res = export_brain_to_vault(db_path, vault_dir)
        return {
            "action": "exported_from_db",
            "export_result": exp_res
        }


# -----------------------------------------------------------------------------
# CLI Entrypoint
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obsidian Vault Sync Engine for Universal AI Brain")
    parser.add_argument("--export", action="store_true", help="Esporta SQLite in Obsidian Vault")
    parser.add_argument("--import", dest="import_mode", action="store_true", help="Importa Obsidian Vault in SQLite")
    parser.add_argument("--sync", action="store_true", help="Esegui sincronizzazione bidirezionale")
    parser.add_argument("--vault-dir", default=DEFAULT_VAULT_DIR, help="Percorso directory del Vault Obsidian")
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH, help="Percorso file brain.db")
    
    args = parser.parse_args()
    
    if args.export:
        res = export_brain_to_vault(args.db_path, args.vault_dir)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.import_mode:
        res = import_vault_to_brain(args.vault_dir, args.db_path)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        res = sync_bidirectional(args.vault_dir, args.db_path)
        print(json.dumps(res, indent=2, ensure_ascii=False))
