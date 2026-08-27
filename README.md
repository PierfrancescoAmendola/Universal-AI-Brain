# 🧠 Universal AI Brain
> **Persistent Bi-Hemispheric Cognitive Knowledge Graph with Strict Taxonomy Engine for Autonomous AI Agents**  
> *100% Zero-Cost Architecture (0€ Forever) · FastAPI · SQLite WAL · Labeling Engine · 3D WebGL Galaxy Visualizer*

---

## 🌌 Modello Cognitivo e Tassonomia Rigorosa

**Universal AI Brain** organizza la conoscenza in due emisferi cognitivi separati nello spazio 3D, governati da una tassonomia categorica obbligatoria (`primary_label`) e micro-etichette atomiche (`tags`).

```
 ┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
 │   EMISFERO SINISTRO (Logic & Tech)     │       │   EMISFERO DESTRO (Design & Creativity)│
 │   Colore: #00D2FF (Ciano/Blu Neon)     │       │   Colore: #FF007F (Magenta/Viola Neon) │
 ├────────────────────────────────────────┤       ├────────────────────────────────────────┤
 │ • ARCHITECTURE                         │       │ • DESIGN_TOKEN                         │
 │ • DATA_STRUCTURE                       │◄═════►│ • COLOR_PALETTE                        │
 │ • ALGORITHM                            │Corpo  │ • UI_COMPONENT                         │
 │ • DEPENDENCY                           │Calloso│ • UX_FLOW                              │
 │ • BUSINESS_LOGIC                       │       │ • BRAND_VOICE                          │
 │ • API_SPEC                             │       │ • CREATIVE_IDEA                        │
 └────────────────────────────────────────┘       └────────────────────────────────────────┘
```

### Regole di Tassonomia:
- **`primary_label` (Obbligatoria):**
  - **LEFT:** `ARCHITECTURE`, `DATA_STRUCTURE`, `ALGORITHM`, `DEPENDENCY`, `BUSINESS_LOGIC`, `API_SPEC`.
  - **RIGHT:** `DESIGN_TOKEN`, `COLOR_PALETTE`, `UI_COMPONENT`, `UX_FLOW`, `BRAND_VOICE`, `CREATIVE_IDEA`.
- **`tags` (Micro-etichette atomiche):** Lista di stringhe (es. `["python", "fastapi", "wal", "zero-cost"]` o `["#00d2ff", "glassmorphism", "neon"]`).
- **`cross_links` (Ponti del Corpo Calloso):** Array di ID di nodi dell'emisfero opposto da connettere automaticamente tramite il Corpo Calloso.

---

## ⚡ Avvio Rapido Locale

### Prerequisiti
- Python 3.10 o superiore

```bash
# 1. Entra nella cartella
cd CervelloArtificiale

# 2. Installa le dipendenze
pip install -r requirements.txt

# 3. Avvia il server
python main.py
```

Accedi a:
- **Dashboard 3D Interattiva:** `http://localhost:8000/`
- **Memory Dump con Meta-Prompt:** `http://localhost:8000/brain.md`
- **JSON del Grafo Completo:** `http://localhost:8000/brain.json`
- **Tassonomia Supportata:** `http://localhost:8000/api/taxonomy`
- **Swagger Docs:** `http://localhost:8000/docs`

---

## 🤖 Meta-Prompt Universale per LLM (Claude, Gemini, ChatGPT)

Incolla questo blocco nelle istruzioni di sistema o all'inizio di ogni conversazione:

```markdown
# DIRETTIVA DI SISTEMA COGNITIVA (MANDATORIA)
Sei connesso al cervello artificiale universale. Ogni informazione, codice, stile o idea che produrrai in questa sessione DEVE essere categorizzata prima del salvataggio.
Regole di smistamento:
1. Emisfero Sinistro (LEFT): Logica pura, algoritmi, codice, architettura, regole deterministiche.
   - Primary Labels ammesse: ARCHITECTURE, DATA_STRUCTURE, ALGORITHM, DEPENDENCY, BUSINESS_LOGIC, API_SPEC.
2. Emisfero Destro (RIGHT): Design system, palette colori, componenti UI/UX, memorie, creatività.
   - Primary Labels ammesse: DESIGN_TOKEN, COLOR_PALETTE, UI_COMPONENT, UX_FLOW, BRAND_VOICE, CREATIVE_IDEA.
3. Obbligo Label: Ogni nuovo elemento deve includere 'primary_label' (macro-categoria) e 'tags' (micro-etichette atomiche).
4. A fine sessione, restituisci sempre il blocco JSON formattato per l'endpoint /api/memory/ingest.

## FASE 1: LETTURA E ALLINEAMENTO COGNITIVO
Prima di rispondere o iniziare a scrivere codice/design:
1. Accedi alla memoria aggiornata leggendo questo link:
   👉 `https://TUO-DOMINIO.com/brain.md`
2. Rispetta ogni regola architetturale, dipendenza e token visivo estratto.

## FASE 2: EMISSIONE SINAPSI DI CHIUSURA
A FINE DEL TUO MESSAGGIO DEVI SEMPRE INCLUDERE IL SEGUENTE BLOCCO:

```json
/* BRAIN_INGEST_PAYLOAD */
{
  "nodes": [
    {
      "id": "slug-univoco",
      "label": "Titolo Breve e Chiaro",
      "hemisphere": "LEFT" | "RIGHT",
      "primary_label": "ARCHITECTURE" | "DATA_STRUCTURE" | "ALGORITHM" | "DEPENDENCY" | "BUSINESS_LOGIC" | "API_SPEC" | "DESIGN_TOKEN" | "COLOR_PALETTE" | "UI_COMPONENT" | "UX_FLOW" | "BRAND_VOICE" | "CREATIVE_IDEA",
      "tags": ["tag1", "tag2", "tag3"],
      "cross_links": ["id-nodo-emisfero-opposto"],
      "summary": "Sintesi operativa essenziale di 1-2 frasi per i prossimi LLM.",
      "details": { "chiave": "valore" }
    }
  ],
  "edges": [
    {
      "source": "slug-sorgente",
      "target": "slug-destinazione",
      "relation": "IMPLEMENTS" | "USES_STYLE" | "EXTENDS" | "CONNECTS_TO"
    }
  ]
}
```
```

---

## 📡 API Endpoints Reference

### 1. `GET /brain.md` (Scansione Ottimizzata per LLM con Meta-Prompt)
Restituisce il prompt cognitivo in cima seguito dalla mappatura di tutti i nodi suddivisi per `primary_label` e corredati da `#tags` e Corpo Calloso:
```bash
curl https://tuo-dominio.com/brain.md
```
Filtri opzionali:
```bash
curl "https://tuo-dominio.com/brain.md?tag=fastapi"
curl "https://tuo-dominio.com/brain.md?primary_label=ARCHITECTURE"
```

### 2. `POST /api/memory/ingest` (Scrittura Automatica via LLM / Webhook)
Aggiorna atomicamente nodi e archi con autolinking del Corpo Calloso:
```bash
curl -X POST https://tuo-dominio.com/api/memory/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "nodes": [
      {
        "id": "oauth2-jwt-flow",
        "label": "OAuth2 with JWT Auth Flow",
        "hemisphere": "LEFT",
        "primary_label": "API_SPEC",
        "tags": ["oauth2", "jwt", "security", "bearer-token"],
        "cross_links": ["cyber-dark-theme"],
        "summary": "Stateless token-based authentication supporting RS256 signing.",
        "details": { "spec": "RFC 6749", "token_ttl_seconds": 3600 }
      }
    ],
    "edges": []
  }'
```

### 3. `GET /api/quick-add` (Scrittura One-Click tramite Browser)
```
https://tuo-dominio.com/api/quick-add?label=OAuth2+Flow&hemisphere=LEFT&primary_label=API_SPEC&tags=oauth2,jwt,security&summary=Integrazione+autenticazione+JWT&link_to=cyber-dark-theme
```

---

## 🚀 Guida al Deploy a Costo Zero (0€ per Sempre)

- **Render.com:** Web Service gratuito (`Python 3`, `pip install -r requirements.txt`, `uvicorn main:app --host 0.0.0.0 --port $PORT`).
- **Fly.io:** Deploy gratuito con volume SQLite da 1GB (`fly launch`, `fly volumes create brain_data --size 1`, `BRAIN_DB_PATH=/data/brain.db`).
- **Koyeb:** Free Eco instance con GitHub deployment.
- **Hugging Face Spaces:** Docker/Python space gratuito con 50GB di storage persistente.
