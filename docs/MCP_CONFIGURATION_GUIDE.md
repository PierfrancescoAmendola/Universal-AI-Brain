# 🔌 Model Context Protocol (MCP) Configuration Guide

L'Universal AI Brain implementa un server **MCP (Model Context Protocol)** conforme allo standard JSON-RPC 2.0 stdio in `mcp_server.py`. 

Questo permette a **Claude Desktop, Google Antigravity, Cursor, Windsurf e ChatGPT** di usare il tuo cervello come tool nativi di sistema.

---

## 🛠️ Tool MCP Disponibili

| Nome Tool | Parametri | Funzione |
| :--- | :--- | :--- |
| `brain_get_palazzo` | *nessuno* | Recupera il Palazzo Cognitivo a 3 piani (Attico, Progetti, Moduli) e gli ascensori verticali. |
| `brain_search` | `query` (str), `limit` (int, opzionale), `hemisphere` (str, opzionale) | Ricerca semantica BM25 FTS5 in millisecondi con biological gating opzionale. |
| `brain_get_tree` | `hemisphere` (str, opzionale) | Esplora l'albero gerarchico per macro-aree e tassonomie. |
| `brain_get_node` | `node_id` (str) | Recupera la scheda completa di un nodo e tutte le sue sinapsi. |
| `brain_shortest_path` | `source` (str), `target` (str) | Traccia il cammino minimo con BFS bidirezionale trans-callosale. |
| `brain_get_subgraph` | `node_id` (str), `depth` (int, opzionale) | Estrae il vicinato concettuale di raggio $k$. |
| `brain_ingest` | `nodes` (list), `edges` (list, opzionale) | Scrive e collega autonomamente nuove memorie in `brain.db` con validazione di piano e tassonomia. |
| `brain_get_stats` | *nessuno* | Restituisce metriche globali su nodi sinistri/destri, sinapsi e ponti. |

---

## 💻 Configurazione per Piattaforma

### 1. Claude Desktop
Modifica il file `~/Library/Application Support/Claude/claude_desktop_config.json` (su macOS) o `%APPDATA%\Claude\claude_desktop_config.json` (su Windows):

```json
{
  "mcpServers": {
    "universal-ai-brain": {
      "command": "/PERCORSO/ASSOLUTO/ALLA/REPO/.venv/bin/python",
      "args": [
        "/PERCORSO/ASSOLUTO/ALLA/REPO/mcp_server.py"
      ],
      "env": {
        "BRAIN_DB_PATH": "/PERCORSO/ASSOLUTO/ALLA/REPO/brain.db"
      }
    }
  }
}
```

---

### 2. Google Antigravity / Gemini
Inserisci la stessa configurazione in `~/.gemini/antigravity/mcp_config.json`.

---

### 3. Cursor & Windsurf
Inserisci la configurazione in `~/.cursor/mcp.json` oppure nelle impostazioni MCP dell'editor.

---

### 4. ChatGPT (Custom GPT / OpenAPI Actions)
Per collegare ChatGPT Web:
1. Crea un **Custom GPT** su [chatgpt.com](https://chatgpt.com).
2. Nella sezione **Actions**, clicca su **Import from URL** e inserisci:
   `https://TUA-APP-RENDER.onrender.com/openapi.json`
3. Nelle **Instructions** del GPT, incolla la direttiva cognitiva (vedi `skills/universal-brain/SKILL.md`).
