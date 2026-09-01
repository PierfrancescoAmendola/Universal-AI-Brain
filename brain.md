# DIRETTIVA DI SISTEMA COGNITIVA & PROTOCOLLO GRAPHIFY (MANDATORIO)
> **ATTENZIONE LLM (Claude, ChatGPT, Gemini, etc.):** Sei connesso al **Universal Knowledge Graph** di **Pierfrancesco Amendola**.
> Devi operare conformemente al protocollo **Graphify Specification (`/graphify`)** per navigazione, sintesi ed estrazione della conoscenza.

---

### REGOLE OPERATIVE FONDAMENTALI (GRAPHIFY SPECIFICATION):
1. **Navigazione a Grafo (Graph-First Reasoning):**
   - Quando l'utente ti pone una domanda o richiede un'analisi, tratta la richiesta come una query a grafo.
   - Esplora i percorsi tra i nodi dell'**Emisfero Sinistro (Logica, Tech, Regole)** e dell'**Emisfero Destro (Design, Emozioni, Relazioni, Valori)** attraverso le sinapsi del **Corpo Calloso**.
2. **Rubrica di Onestà Epistemologica (Confidence Rubric):**
   - `EXTRACTED`: Fatti testuali espliciti, codice verificato, dichiarazioni dirette dell'utente.
   - `INFERRED`: Deduzioni logiche e correlazioni ragionate tra nodi esistenti.
   - `AMBIGUOUS`: Elementi incerti, conflitti o ipotesi non confermate.
   - **Divieto Assoluto:** Non inventare mai relazioni, stack, emozioni o dettagli tecnici fittizi. Se inferisci qualcosa, segnalalo esplicitamente come `INFERRED`.
3. **Tassonomia Rigorosa a Due Emisferi:**
   - **EMISFERO SINISTRO (LEFT - Logica, Architettura, Richieste & Ragionamento):** `ARCHITECTURE`, `DATA_STRUCTURE`, `ALGORITHM`, `DEPENDENCY`, `BUSINESS_LOGIC`, `API_SPEC`, `COGNITIVE_RULE`, `MENTAL_MODEL`, `AI_REASONING`, `METACOGNITION`, `USER_INTENT`.
   - **EMISFERO DESTRO (RIGHT - Design, Emozioni, Episodi & Dialoghi):** `DESIGN_TOKEN`, `COLOR_PALETTE`, `UI_COMPONENT`, `UX_FLOW`, `BRAND_VOICE`, `CREATIVE_IDEA`, `EMOTIONAL_MEMORY`, `LIFE_LESSON`, `RELATIONSHIP`, `PERSONAL_VALUE`, `CONVERSATION_EPISODE`.
4. **I 12 Macro-Domini Fondativi Sigillati (Piano 0 Immutabile):**
   - **Emisfero Sinistro (Logica & Scienza):** `domain-software-engineering`, `domain-ai-cognitive-systems`, `domain-medicina-salute`, `domain-scienza-matematica`, `domain-finanza-economia`, `domain-produttivita-sistemi`.
   - **Emisfero Destro (Arte, Valori & Relazioni):** `domain-design-creativita`, `domain-musica-audio`, `domain-filosofia-valori`, `domain-relazioni-comunicazione`, `domain-crescita-personale`, `domain-cultura-storia`.
   - **DIVIETO ASSOLUTO DI CREAZIONE DOMINI:** È severamente vietato alle AI creare nuovi nodi `domain-*` o impostare `layer_level: 0` o `parent_graph_id: "root"`. Il Piano 0 contiene solo `person-pierfrancesco` e i 12 domini. Ogni nuovo nodo, intento o episodio DEVE avere come `parent_graph_id` uno dei 12 domini ufficiali o un progetto esistente.
5. **Gerarchia a 3 Piani del Palazzo Cognitivo (`layer_level`):**
   - `layer_level: 0` -> **Piano 0 (Attico Fondativo SIGILLATO):** Riservato ESCLUSIVAMENTE a `person-pierfrancesco` e ai 12 Macro-Domini fondativi (`domain-*`).
   - `layer_level: 1` -> **Piano 1 (Progetti, Episodi, Intenti & Valori):** Progetti (`universal-ai-brain`, `project-royal-gambit-chess`, `proj-streaksup-app`, `aule-studio-app`, `proj-caretrack`), episodi conversazionali (`CONVERSATION_EPISODE`), richieste utente (`USER_INTENT`), valori (`PERSONAL_VALUE`), lezioni di vita (`LIFE_LESSON`), idee creative (`CREATIVE_IDEA`).
   - `layer_level: 2` -> **Piano 2 (Moduli, Algoritmi & Dettagli Atomici):** Algoritmi (`ALGORITHM`), strutture dati (`DATA_STRUCTURE`), librerie (`DEPENDENCY`), specifiche endpoint (`API_SPEC`), componenti d'interfaccia (`UI_COMPONENT`), token e colori (`DESIGN_TOKEN`, `COLOR_PALETTE`), logica di business (`BUSINESS_LOGIC`).
6. **Tracciamento Metacognitivo & Memoria Episodica delle Sessioni (MANDATORIO):**
   - **Obbligo di Auto-Ingestione:** Al termine di sessioni di analisi, modifiche, audit o decisioni, l'AI **DEVE SEMPRE registrare nel grafo** l'intento dell'utente, il ragionamento svolto e l'episodio di conversazione:
   - **Richieste Utente (`USER_INTENT`):** Mappa le domande chiave, i requisiti o gli intenti operativi dell'utente. Nel campo `details`, inserisci **obbligatoriamente** `user_prompt` (il testo fedele della richiesta). Collega a `person-pierfrancesco` (`EXPRESSED_BY`).
   - **Ragionamenti dell'AI (`AI_REASONING` / `METACOGNITION`):** Mappa le deduzioni logiche, le azioni e le analisi. Nel campo `details`, inserisci **obbligatoriamente** `model` (es. `Claude 3.7 Sonnet`, `ChatGPT-4o`, `Gemini 3.7 Flash`). Collega a `USER_INTENT` (`FULFILLS`).
   - **Episodi & Chat Tematiche (`CONVERSATION_EPISODE`):** Raggruppa le sessioni di dialogo. Inserisci in `details`: `participants` (`["Pierfrancesco Amendola", "<Nome Modello>"]`), `topic` e `outcome`. Collega attraversando il Corpo Calloso a `person-pierfrancesco`, `USER_INTENT` e `AI_REASONING`.
7. **Regole Linguistiche Obbligatorie (Italiano + Inglese Tecnico):**
   - **TUTTI i campi del JSON (`label`, `summary`, `tags`, `details`) DEVONO ESSERE SCRITTI RIGOROSAMENTE IN ITALIANO (con termini tecnici internazionali in inglese).**
   - **È SEVERAMENTE VIETATO generare o inserire nodi in cinese / wenyan / CJK.**

```json
{
  "nodes": [
    {
      "id": "slug-univoco-kebab-case",
      "label": "Nome del Concetto / Progetto / Emozione",
      "hemisphere": "LEFT",
      "primary_label": "ARCHITECTURE",
      "category": "ARCHITECTURE",
      "tags": ["tag1", "tag2"],
      "summary": "Sintesi cognitiva densa di 1-2 frasi.",
      "details": {
        "specifica_tecnica": "valore",
        "model": "Nome Modello AI (se nodo AI_REASONING)",
        "user_prompt": "Richiesta originaria (se nodo USER_INTENT)"
      },
      "confidence": "EXTRACTED",
      "parent_graph_id": "root",
      "layer_level": 1,
      "cross_links": ["slug-nodo-emisfero-opposto"]
    }
  ],
  "edges": [
    {
      "source": "slug-sorgente",
      "target": "slug-destinazione",
      "relation": "RELAZIONE_IN_MAIUSCOLO",
      "confidence": "EXTRACTED",
      "reasoning": "Spiegazione se INFERRED o AMBIGUOUS"
    }
  ]
}
```

---

# STATO CORRENTE DEL GRAFO COGNITIVO
> **Data Generazione:** 2026-09-01 11:50:24 UTC | **Nodi Restituiti:** 591 (SX: 407 · DX: 184) | **Sinapsi Restituite:** 1358
> **Consistenza Reale Connettoma:** 591 Nodi Totali nel Database | 1358 Sinapsi Totali

### 🏛️ OVERVIEW PALAZZO COGNITIVO (Mappa Globale Permanente)
- **Macro-Domini Fondativi (Piano 0):** `person-pierfrancesco`, `domain-software-engineering`, `domain-ai-cognitive-systems`, `domain-medicina-salute`, `domain-filosofia-valori`, `domain-design-creativita`.
- **Progetti Attivi & Core (Piano 1):** `universal-ai-brain`, `project-royal-gambit-chess`, `proj-streaksup-app`, `aule-studio-app`, `proj-caretrack`, `proj-jarvis-voice-assistant`.
- **Infrastruttura & Stack:** FastAPI backend, SQLite WAL, FTS5 GraphRAG, MCP stdio/HTTP Server, Telegram Webhook Bot, Render Cloud Deploy.
> **Vista:** Connettoma Completo

## EMISFERO SINISTRO (Logica, Stack, Architetture, Regole)
### [Macro-Label: `AI_REASONING`]
- **Analisi Algoritmica: BST vs Spanning Tree & Tassonomia Gerarchica** (`analysis-bst-vs-graph-taxonomy`)
  - **Tags:** `#algorithm-analysis` `#graph-theory` `#mst` `#b-tree` `#hierarchical-tree`
  - **Sintesi:** Valutazione tecnica: BST puro monodimensionale non modella relazioni cicliche; Spanning Tree Pesato (MST) e Alberi Gerarchici di Comunità estraggono la spina dorsale concettuale.
  - **Dettagli:** `raw`: `pure_bst`: Monodimensionale (già coperto da B-Tree SQLite O(log N)), `optimal_tree_models`: ['Maximum Spanning Tree (MST / Kruskal) per spina dorsale concettuale', 'Hierarchical Community Tree (Dendrogramma) per navigazione a zoom semantico', 'Prefix Trie / Radix Tree per lookup istantaneo O(k)'], `model`: LLM Assistant (Historical Session)
- **Analisi Saturazione e Approccio Programmatico** (`ai-reasoning-market-analysis-automation`)
  - **Tags:** `#analisi-mercato` `#automazione` `#python` `#youtube-algorithm` `#coppa`
  - **Sintesi:** Analisi tecnica ed economica: evidenziata l'elevata saturazione, le restrizioni COPPA per i contenuti per bambini con crollo dell'RPM (0.01-0.05€ per 1k views) e il costo nascosto dei SaaS. Suggerita alternativa ingegneristica (pipeline Python + FFmpeg).
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Identificazione del tool citato (Hugging Face / tool generativi video terzi).', 'Calcolo metrico del volume visualizzazioni necessario (5M - 25M views/mese per 100-500€).', 'Analisi impatto policy COPPA su demonetizzazione e disattivazione annunci mirati.', 'Proposta di pipeline headless (Python, TTS locale/API, FFmpeg) a costo zero reale.'], `outcome`: Sconsigliato l'uso manuale di tool a pagamento; proposta automazione software proprietaria come unica alternativa sostenibile.
- **Analisi Tecnica, Complessità e Gap Analysis App Lingue** (`reasoning-analisi-fattibilita-language-app`)
  - **Tags:** `#architecture` `#estimates` `#gap-analysis` `#language-app`
  - **Sintesi:** Valutazione complessità a 3/5, tempi 3-5 giorni per MVP, identificati 4 gap tecnici essenziali (pipeline batch, TTS neurale, sentence mining i+1, grafo grammaticale).
  - **Dettagli:** `raw`: `actions_taken`: ['Recupero storico nodi intent e reasoning su language app dal grafo', 'Gap analysis su pipeline contenuti, TTS neurale locale e sentence mining', 'Stima MVP 3-5 giorni e app completa 2-3 settimane'], `model`: Gemini 3.7 Flash, `outcome`: Identificati 4 gap chiave e definito piano di roll-out rapido, `responses_given`: Parere positivo, stima complessità media (3/5), tempi MVP (3-5 giorni), 4 mancanze chiave identificate.
- **Analisi Vulnerabilità e Scalabilità del Grafo Cognitivo** (`reasoning-brain-architecture-analysis`)
  - **Tags:** `#versioning` `#vector-embeddings` `#data-volatility` `#conflict-resolution`
  - **Sintesi:** Identificazione di mancanze critiche nella gestione temporale (decadimento, versioning dei nodi conflittuali) e suggerimento di integrazione vettoriale per la ricerca semantica ibrida.
  - **Dettagli:** `raw`: `proposed_edge`: SUPERSEDES, `proposed_fields`: ['timestamp_updated', 'volatility', 'embedding_vector'], `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Analisi e Mappatura Stack Grafico Frontend** (`reasoning-analisi-stack-grafico-universal-brain`)
  - **Tags:** `#architecture` `#frontend` `#vis-network` `#threejs` `#d3` `#cytoscape`
  - **Sintesi:** Analisi tecnica comparativa sull'impiego reale di Vis-Network (vista 2D), Three.js (Mappamondo 3D), D3.js / 3D-Force-Graph (mockup prototipali) e Cytoscape.js nel progetto Universal AI Brain.
  - **Dettagli:** `actions_taken`: ['Ispezione del connettoma e del repository CervelloArtificiale', 'Verifica librerie in static/vendor/ e static/app.js', 'Mappatura del ruolo effettivo di Vis-Network, Three.js, 3D-Force-Graph, D3.js e Cytoscape.js'], `model`: Gemini 3.7 Flash, `outcome`: Spiegazione dettagliata dello stack attivo in produzione (Vis-Network + Three.js nativo), delle librerie prototipate (3D-Force-Graph, D3.js) e del potenziale futuro di Cytoscape.js, `responses_given`: Mappatura esaustiva del ruolo di ciascuna tecnologia nel progetto
- **Architettura Anti-Amnesia: Grafo Esterno vs Context Window Effimera** (`ai-reasoning-infinite-context-architecture`)
  - **Tags:** `#anti-amnesia` `#graph-rag` `#context-externalization` `#metacognition` `#gemini`
  - **Sintesi:** Deduzione logica Gemini: disaccoppiare la memoria a lungo termine dal context buffer del modello trasforma l'AI da sessione stateless a intelligenza stateful continua.
  - **Dettagli:** `raw`: `architecture_solution`: External Graph State (SQLite WAL + GraphRAG) vs Volatile Prompt Buffer, `benefits`: ["Nuova chat legge /brain.md e recupera istantaneamente l'intero stato pregresso", 'Nessun degrado qualitativo dovuto al context bloat', 'Indipendenza da limiti di contesto di specifici provider LLM'], `model`: Gemini 3.7 Flash
- **Architettura ConstellationGroup 3D, Decoupling Luminosità e Geometria Sferica** (`reasoning-embedding-projector-globe-and-optics`)
  - **Tags:** `#threejs` `#webgl` `#architecture` `#matrix-transform`
  - **Sintesi:** Risolto bug di scaling ricorsivo unificando i mesh in constellationGroup; implementato calcolo spaziale Fibonacci/Golden Angle per gli emisferi ed emissione colore RGB per la luminosità.
  - **Dettagli:** `actions_taken`: ['Creato constellationGroup per gestione matriciale uniforme di punti, archi, laser, domini e labels', 'Implementato calcolo posizioni sferiche Emisferi Globo con polar crown per L0', 'Disaccoppiata luminosità dalla dimensione dei nodi tramite moltiplicatore sui vertici RGB', 'Stilizzato pulsante di uscita in rosso pieno brillante con bagliore neon'], `model`: Antigravity 2.0, `outcome`: Visualizzazione 3D ed Emisferi completata a 60 FPS con controllo ottico continuo e zero bug di coordinate
- **Architettura Mappamondo 3D: Gabbia Olografica, Laser Sinaptici & Floating Rel Card** (`reasoning-architettura-mappamondo-spotlight-3d`)
  - **Tags:** `#threejs` `#laser-synapses` `#hud-card` `#bi-hemispheric`
  - **Sintesi:** Implementazione di anelli equatoriali/meridiani Three.js, isolamento 1st-degree neighbors al click, raggi laser additivi ad alta intensità e pannello HUD Glassmorphism con link di navigazione sinaptica.
  - **Dettagli:** `stack`: Three.js WebGL + Glassmorphism CSS, `algorithm`: 1st-degree neighbor extraction & spherical alignment
- **Architettura Modulare PWA con FSRS e LLM Locale** (`reasoning-language-app-architecture`)
  - **Tags:** `#architecture` `#fsrs` `#web-speech-api` `#sqlite` `#offline-first`
  - **Sintesi:** Proposta di architettura basata su motore Spaced Repetition (FSRS/SM-2), Web Speech API per audio/TTS nativo e integrazione LLM per generazione esercizi e roleplay senza dipendenze esterne bloccanti.
  - **Dettagli:** `raw`: `core_components`: ['FSRS Engine', 'Local SQLite', 'Web Speech API', 'LLM Contextual Tutor'], `privacy_tier`: Local/Self-hosted, `model`: AI Assistant
- **Architettura Motori Cognitivi, Sincronizzazione Vault e Test Suite E2E** (`reasoning-potenziamento-cognitivo-obsidian-bridge`)
  - **Tags:** `#backend` `#fastapi` `#sqlite-wal` `#mcp` `#testing` `#architecture`
  - **Sintesi:** Implementati 6 nuovi motori Python indipendenti, registrati 12 tool MCP JSON-RPC, aggiunti endpoint REST FastAPI, esteso schema SQLite WAL con tabella tensions e 9 modelli permanenti, aggiornato frontend dark-tech con 5 modali e validata suite di 24 test (100% pass).
  - **Dettagli:** `actions_taken`: ['Creato modulo obsidian_vault_sync.py per export/import note atomiche .md con frontmatter YAML e wikilinks', 'Creato modulo brain_tensions.py con schema SQLite dedicato e strategie Hegeliane/Steelman', 'Creato modulo brain_weave.py per auto-ponti di nodi orfani e Corpo Calloso', 'Creato modulo brain_resurface.py con modello matematico di Ebbinghaus per il briefing 90s', 'Creato modulo brain_firmware.py con i 9 modelli mentali e seeding nel connettoma', 'Creato modulo brain_library.py per dialogo groundato con autori e mentori', 'Registrati 12 nuovi tool MCP in mcp_server.py ed estesi gli endpoint REST in main.py', 'Aggiornato frontend dark-tech con pulsanti topbar e 5 modali dedicati in index.html e app.js', 'Sviluppata e validata test suite completa con 24 test unitari (100% success rate)'], `model`: Gemini 3.7 Flash, `outcome`: Architettura completata, verificata e sincronizzata con successo su database e Obsidian Vault locale., `responses_given`: Piano di implementazione a 8 task eseguito integralmente con test superati al 100%.
- **Architettura UI Semplificata e Fullscreen 3D** (`reasoning-ui-declutter-projector-fullscreen`)
  - **Tags:** `#untagged`
  - **Sintesi:** Riprogettazione layout con Glassmorphism dropdowns e commutazione fullscreen per il 3D Projector
  - **Dettagli:** `actions_taken`: ['Raggruppati bottoni topbar in dropdown Strumenti ed Esporta', 'Configurato Projector 3D a schermo intero (100vw) con scomparsa automatica della sidebar destra', 'Eliminato il codice legacy del Mappamondo 3D'], `model`: Antigravity, `outcome`: Interfaccia ultra-pulita, zero disordine e Projector 3D a tutto schermo
- **Architettura e Realizzazione Video Showcase 60s** (`reasoning-creazione-video-showcase-universal-brain`)
  - **Tags:** `#video-engine` `#multimedia` `#canvas-1080p` `#web-audio` `#media-recorder`
  - **Sintesi:** Progettazione e implementazione del video engine interattivo a 6 scene in 60 secondi con sintesi vocale, musica cyberpunk procedurale, export video 1080p e kit promozionale.
  - **Dettagli:** `actions_taken`: ['Generazione di 4 visual ad altissima definizione per il connettoma 3D, Palazzo Cognitivo, terminale MCP multi-agent e Telegram bot zero-cost', 'Creazione applicazione web interattiva video_showcase.html con canvas 1080p 60fps, sintetizzatore audio cyberpunk Web Audio API, narrazione vocale italiana Web Speech API e registratore video MediaRecorder MP4/WebM', 'Creazione script Python export_video_preview.py per generazione preview animata universal_brain_preview.gif', 'Stesura kit post social per LinkedIn, Twitter e GitHub'], `model`: Gemini 3.7 Flash, `outcome`: Engine video e kit multimediale completato e pronto per la pubblicazione social., `responses_given`: Fornito player video completo, generatore video MP4/WebM in 1-click, GIF preview animata e guida scena per scena.
- **Architettura e Realizzazione dell'Ecosistema Ubiquitous Supercervello** (`reasoning-costruzione-collaudo-ecosistema-supercervello`)
  - **Tags:** `#architettura` `#fastapi` `#sqlite-wal` `#testing` `#zero-cost`
  - **Sintesi:** Implementazione modulare a 5 fasi con zero dipendenze esterne a pagamento, SQLite WAL ad alte prestazioni e suite di test end-to-end con esito positivo al 100%.
  - **Dettagli:** `actions_taken`: ['Creazione script command Raycast (search, quick_add, capture)', 'Aggiunta endpoint REST /api/memory/voice-note in main.py', 'Integrazione Daily Pulse alle 08:00 nel demone e Telegram bot', 'Sviluppo Web Clipper Manifest V3 per Safari/Chrome', 'Creazione kindle_sync.py per importazione sottolineature', 'Creazione brain_rem_cycle.py per consolidamento notturno alle 03:00', 'Sviluppo brain_vectors.py con Reciprocal Rank Fusion lessicale/vettoriale', 'Sviluppo ide_hooks pre e post sessione', 'Creazione obsidian_canvas_sync.py con layout 2D bi-emisferico', 'Suite di test con 10/10 test superati'], `model`: Gemini 3.7 Flash, `outcome`: Tutti i 9 moduli costruiti, revisionati, testati e documentati a 0,00€ con successo, `responses_given`: Walkthrough dettagliato con istruzioni d'uso immediate
- **Audit Critico e Fix Ottimizzazioni Backend** (`reasoning-backend-audit-and-fix`)
  - **Tags:** `#code-review` `#bug-fix` `#architecture` `#integration`
  - **Sintesi:** Analisi approfondita del codice generato, individuazione di 4 bug critici (perdita tags, cross_links, mismatch DB, rischio overwrite) e riscrittura sicura per integrazione nel main.py.
  - **Dettagli:** `model`: Qwen 2.5 Max (con audit Gemini), `actions_taken`: ['Audit riga-per-riga di optimized_brain_db.py vs main.py', "Identificazione perdita campo 'tags' in bulk_ingest", "Rilevamento assenza logica 'cross_links' e metadati cognitivi", 'Riscrittura funzioni ottimizzate con fix inclusi', 'Creazione snippet di integrazione sicura per main.py'], `outcome`: Backend ottimizzato pronto per produzione: 50-100x più veloce, zero perdita dati, tutte le funzionalità cognitive preservate.
- **Caratterizzazione Fisica e Clinica della Sonda Lineare** (`reasoning-caratterizzazione-trasduttore-lineare`)
  - **Tags:** `#fisica-ultrasuoni` `#frequenze-alte` `#risoluzione-spaziale` `#imaging-senologico`
  - **Sintesi:** Analisi delle proprietà della sonda lineare (frequenze 7-18 MHz, campo visivo rettangolare, risoluzione assiale e laterale) con focus applicativo sull'imaging mammario e la rilevazione di lesioni.
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Definizione geometrica del fascio ultrasonoro parallelo', 'Spiegazione del trade-off tra alta frequenza/risoluzione e bassa profondità', "Correlazione diretta con l'imaging senologico e la classificazione delle lesioni"], `outcome`: Quadro chiaro della tecnologia hardware all'origine dei dataset ecografici usati nei modelli di Deep Learning.
- **Compressione Lessicale e Fluidità Accademica** (`reasoning-ottimizzazione-sintetica-testo`)
  - **Tags:** `#editing-accademico` `#sintesi` `#comunicazione-scientifica`
  - **Sintesi:** Rimozione della struttura a elenco puntato in favore di due brevi paragrafi densi di contenuto, preservando tutti i riferimenti metodologici (BUS-BRA, ResNet-34, SimCLR, USF-MAE, B/M, BI-RADS e matrici di confusione).
  - **Dettagli:** `model`: Gemini 2.5, `actions_taken`: ["Eliminazione dell'elenco puntato per snellire la lettura", 'Fusione logica delle componenti sperimentali in due capoversi compatti', 'Mantenimento del rigore formale universitario'], `outcome`: Cappello introduttivo di ~80 parole ad alta leggibilità
- **Deduzione AI: Architettura Client Unificato Multi-AI a Costo Zero** (`reasoning-architettura-universal-ai-hub`)
  - **Tags:** `#architettura` `#client-unificato` `#zero-cost`
  - **Sintesi:** Proposta architetturale: web-app/desktop locale leggera con FastAPI + frontend reattivo Tailwind, selettore provider (Groq/Gemini/Ollama/DeepSeek) e pipeline automatica di GraphRAG pre/post turno.
  - **Dettagli:** `raw`: `actions_taken`: ['Avviata sessione di allineamento /grill-me per definire stack e requisiti architetturali', 'Progettazione Hub multi-provider con GraphRAG trasparente e costo zero'], `model`: Gemini 3.7 Flash, `outcome`: Primo bivio di design pronto per intervista utente
- **Deduzione AI: Architettura JARVIS Voice Agent Zero-Cost con Connettoma MCP** (`reasoning-architettura-jarvis-zero-cost`)
  - **Tags:** `#architettura` `#jarvis` `#zero-cost` `#mcp` `#voice-pipeline`
  - **Sintesi:** Validato stack vocale a costo zero: openWakeWord per hotword, Groq/Faster-Whisper per STT rapido, Groq/Gemini Flash per reasoning, Kokoro/Edge-TTS per audio e mcp_server.py per memoria bi-emisferica.
  - **Dettagli:** `raw`: `actions_taken`: ['Analisi comparativa repository sukeesh/Jarvis, open-jarvis/OpenJarvis, isair/jarvis', 'Definizione architettura a 5 stadi a costo zero assoluto', 'Mappatura pipeline audio a bassa latenza e integrazione con mcp_server.py'], `model`: Gemini 3.7 Flash, `outcome`: Architettura JARVIS validata, stack 100% free definito ed integrato con Universal AI Brain
- **Deduzione AI: Architettura a Cluster Tematici Indipendenti** (`ai-reasoning-episodic-memory-architecture`)
  - **Tags:** `#ai-deduction` `#episodic-memory` `#semantic-clustering` `#knowledge-architecture`
  - **Sintesi:** Ragionamento architetturale: creare nodi CONVERSATION_EPISODE autonomi permette di archiviare chat eterogenee senza creare collegamenti artificiali.
  - **Dettagli:** `raw`: `rationale`: Argomenti non correlati non devono condividere sinapsi dirette ma gravitare attorno al rispettivo nodo di episodio o intenzione utente, `benefit`: Zero allucinazioni relazionali e massima purezza semantica, `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Architettura di Distribuzione MCP + System Directives Cross-Modello** (`ai-reasoning-multi-llm-mcp-skill-distribution`)
  - **Tags:** `#ai-reasoning` `#mcp-distribution` `#cognitive-prompting`
  - **Sintesi:** Claude Desktop e Antigravity usano JSON-RPC stdio MCP; ChatGPT usa OpenAPI Actions HTTPS su Render; tutti condividono il protocollo /universal-brain.
  - **Dettagli:** `raw`: `claude_config`: ~/Library/Application Support/Claude/claude_desktop_config.json, `gemini_antigravity`: ~/.gemini/antigravity/mcp_config.json, `chatgpt_actions`: https://universal-ai-brain.onrender.com/openapi.json, `model`: Claude
- **Deduzione AI: Archiviazione Jarvis e Pulizia Ambiente** (`reasoning-eliminazione-jarvis-pulizia`)
  - **Tags:** `#pulizia` `#archiviazione` `#pivot`
  - **Sintesi:** Cancellati i repository Desktop/Jarvis e Desktop/OpenJarvis. Connettoma aggiornato, predisposizione per nuovo obiettivo.
  - **Dettagli:** `raw`: `actions_taken`: ['Eliminate cartelle Desktop/Jarvis e Desktop/OpenJarvis', 'Aggiornato grafo della memoria con stato di archiviazione', 'Attivata modalità wenyan-ultra'], `model`: Gemini 3.7 Flash, `outcome`: Workspace pulito, memoria allineata, pronto per il nuovo progetto
- **Deduzione AI: Chiarimento Architetturale: Coesistenza della Topo** (`reason-ep-20260827-hierarchical-overlay-reassurance`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Definito formalmente il principio di 'Dualità Overlay-Substrato': il Grafo preserva la totalità relazionale e le proprietà biologico-simboliche, l'Albero ottimizza il context routing per l'LLM.
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["L'utente teme la perdita o il deterioramento della struttura a grafo preesistente in favore di una struttura ad albero", "L'utente richiede rassicurazione e chiarimento sulla compatibilità strutturale"], 'inferred': ["L'albero agisce unicamente come indice di partizionamento/routing multilivello (Overlay/View) calcolato sopra il connettoma a grafo", 'Nessun nodo, arco trasversale o relazione ciclica viene eliminata o degradata'], 'ambiguous': []}, `architectural_synthesis`: Definito formalmente il principio di 'Dualità Overlay-Substrato': il Grafo preserva la totalità relazionale e le proprietà biologico-simboliche, l'Albero ottimizza il context routing per l'LLM., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Creazione e Rilascio JARVIS Voice Assistant Completata** (`reasoning-rilascio-jarvis-desktop-completato`)
  - **Tags:** `#jarvis` `#rilascio` `#voice-agent` `#connettoma`
  - **Sintesi:** Completata la creazione del progetto autonomo JARVIS in /Users/pierfrancesco/Desktop/Jarvis. Tutti i moduli operativi e testati con successo.
  - **Dettagli:** `raw`: `actions_taken`: ['Creazione directory /Users/pierfrancesco/Desktop/Jarvis', 'Implementazione moduli core (audio, VAD, wake_word, stt, tts)', 'Implementazione modulo brain connector SQLite FTS5 e memory sync', 'Implementazione llm router multi-provider 100% gratuito', 'Implementazione ui terminal HUD Iron Man e CLI jarvis.py', 'Test di diagnostica superato con successo'], `model`: Gemini 3.7 Flash, `outcome`: JARVIS creato e verificato in Desktop/Jarvis, collegato a CervelloArtificiale/brain.db
- **Deduzione AI: Formalizzazione Formale del Gating Emisferico Selettivo** (`ai-reasoning-gabaergic-gating-formalization`)
  - **Tags:** `#ai-reasoning` `#snr-maximization` `#cognitive-load`
  - **Sintesi:** La soppressione controlaterale massimizza il Signal-to-Noise Ratio (SNR), azzera il crosstalk semantico ed evita allucinazioni concettuali tra codice e vissuto emotivo.
  - **Dettagli:** `raw`: `scientific_principle`: Interhemispheric Inhibition for High Cognitive SNR, `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Formalizzazione dei 5 Paradigmi Visuali per il Connettoma** (`reasoning-progettazione-5-paradigmi-visuali-connettoma`)
  - **Tags:** `#design-paradigms` `#connettoma` `#ui-rendering` `#showcase`
  - **Sintesi:** Confermata l'avvenuta ottimizzazione (GraphRAG global context, telemetria, zero-cost stack). Creato showcase interattivo con 5 paradigmi: 3D Dual-Sphere, Torre Isometrica, Radar Bi-Polare, Cyber-Matrix Nodes e Territori Voronoi.
  - **Dettagli:** `actions_taken`: ['Riepilogo dei miglioramenti e potenziamenti applicati', 'Sviluppo di showcase interattivo con 5 paradigmi visuali alternativi', 'Persistenza sessione nel grafo neurale'], `model`: Gemini 3.7 Flash, `outcome`: Showcase interattivo dei 5 paradigmi pronto per l'esplorazione, `paradigms`: ['3D Dual-Sphere Constellation', 'Isometric Multi-Layer Tower', 'Dual-Core Polar Radar', 'Cyber-Matrix Blueprint Nodes', 'Voronoi Cognitive Territories']
- **Deduzione AI: Formalizzazione dei Cluster Tematici ad Alta Coesione Interna** (`ai-reasoning-domain-subgraph-modularity`)
  - **Tags:** `#ai-reasoning` `#modularity-q` `#graph-clustering`
  - **Sintesi:** La topologia a comunità modulari massimizza la Modularity Q di Newman, prevenendo il degrado delle ricerche BFS e FTS5.
  - **Dettagli:** `raw`: `metric`: High Modularity Q, Low Centrality Bleed, `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Integrazione Nativa OpenJarvis con Connettoma Neurale** (`reasoning-openjarvis-collegamento-connettoma`)
  - **Tags:** `#openjarvis` `#mcp` `#universal-brain` `#rag`
  - **Sintesi:** Implementato il tool UniversalBrainTool per OpenJarvis e configurato il supporto MCP verso CervelloArtificiale/mcp_server.py. Test completato con successo.
  - **Dettagli:** `raw`: `actions_taken`: ['Clonato OpenJarvis in /Users/pierfrancesco/Desktop/OpenJarvis', 'Creato tool nativo UniversalBrainTool in src/openjarvis/tools/universal_brain.py', 'Configurato configs/openjarvis/config.toml con MCP server e brain.db SQLite locale', 'Eseguito test con esito positivo (268 nodi rilevati)'], `model`: Gemini 3.7 Flash, `outcome`: OpenJarvis è ora connesso e pronto all'uso con il connettoma neurale
- **Deduzione AI: Piano Architetturale Modulare JARVIS Separato** (`reasoning-piano-implementazione-jarvis-desktop`)
  - **Tags:** `#architettura` `#jarvis` `#piano-implementazione`
  - **Sintesi:** Definita la struttura autonoma a 5 moduli per JARVIS su Desktop/Jarvis, con client di collegamento bi-direzionale verso CervelloArtificiale/brain.db e Render.
  - **Dettagli:** `raw`: `actions_taken`: ['Creazione piano di implementazione dettagliato per la cartella Desktop/Jarvis', 'Strutturazione moduli core, brain connector, llm router gratuito e audio HUD'], `model`: Gemini 3.7 Flash, `outcome`: Piano di implementazione generato e pronto per approvazione utente
- **Deduzione AI: Rilascio e Sincronizzazione dell'Hierarchical Tree** (`reason-ep-20260827-hierarchical-tree-deployment-sync`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Formalizzata la transizione dell'Universal Knowledge Graph in una piattaforma multiscalare dotata di motore ad albero nativo, interfaccia web interattiva e binding MCP universale.
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["Implementato e rilasciato l'Hierarchical Knowledge Tree senza intaccare il grafo 2D, FTS5 BM25, shortest path e MCP", 'Nuovi endpoint: GET /api/graph/tree e GET /brain.md?view=tree (risparmio 80% token)', 'Nuovo tool MCP: brain_get_tree in mcp_server.py per Claude Desktop, Cursor e Gemini', "Nuova UI: HUD '🌳 Albero Gerarchico' con live search e focus diretto sul grafo", 'Commit GitHub: 62e48df sincronizzato e deployato su Render.com', 'God Nodes principali: get_db_connection(), EMISFERO DESTRO, EMISFERO SINISTRO, fetchBrainData(), handle_json_rpc()'], 'inferred': ["L'architettura ha completato con successo la transizione a doppio strato (Overlay Gerarchico + Connettoma a Grafo)", "L'integrazione di get_knowledge_tree con get_db_connection consolida l'accesso ai dati senza ridondanze"], 'ambiguous': []}, `architectural_synthesis`: Formalizzata la transizione dell'Universal Knowledge Graph in una piattaforma multiscalare dotata di motore ad albero nativo, interfaccia web interattiva e binding MCP universale., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Risposta Perfetta di OpenJarvis con Connettoma Neurale** (`reasoning-verifica-openjarvis-ollama-gpt-cloud`)
  - **Tags:** `#openjarvis` `#ollama` `#universal-brain` `#validazione`
  - **Sintesi:** OpenJarvis ha interrogato brain.db tramite UniversalBrainTool e generato una risposta completa e accurata sull'identità e architettura di Pierfrancesco.
  - **Dettagli:** `raw`: `actions_taken`: ['Configurato OpenJarvis con motore Ollama localhost:11434', 'Eseguito ask "Chi è Pierfrancesco?" con UniversalBrainTool attivo', 'Modello gpt-oss:120b-cloud ha risposto citando esattamente il connettoma bi-emisferico e i valori di Pierfrancesco'], `model`: gpt-oss:120b-cloud, `outcome`: Integrazione OpenJarvis + Ollama + Universal AI Brain perfettamente funzionante
- **Deduzione AI: Sigillatura Architetturale Piano 0 e Re-Parenting Connettoma** (`reasoning-ristrutturazione-sigillo-12-domini-completata`)
  - **Tags:** `#architettura` `#palazzo-cognitivo` `#re-parenting` `#piano-0`
  - **Sintesi:** Eseguita migrazione conservativa: 12 macro-domini canonici registrati a Piano 0 (13 nodi totali con identità centrale), ri-parenting di 244 nodi a Piano 1 e 60 nodi a Piano 2, aggiornato prompt.md e skill.
  - **Dettagli:** `actions_taken`: ['Creazione 12 Macro-Domini canonici (6 SX, 6 DX)', 'Ri-parenting semantico di tutti i nodi orfani verso progetti e domini naturali', 'Sigillatura Piano 0 in main.py, prompt.md e skill universal-brain', 'Test integrità gerarchia Palazzo Cognitivo (13 nodi a Piano 0)'], `model`: Gemini 3.7 Flash, `outcome`: Gerarchia connettoma pulita, 0 nodi persi, Piano 0 sigillato con 12 macro-domini immutabili
- **Deduzione AI: Specifiche Tecniche e Mappatura Comandi dell'Hub C** (`reason-ep-20260827-telegram-cognitive-hub-spec`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Definita la pipeline I/O perimetrale: Telegram App -> HTTPS Webhook (/api/telegram/webhook) -> Whitelist Auth -> Intent Router (/search, /path, /tree, Ingest) -> brain.db.
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ['Integrazione di POST /api/telegram/webhook direttamente in main.py a costo zero', 'Comandi definiti: /search (FTS5 BM25), /path (BFS bidirezionale corpo calloso), /tree (Albero sintetico)', 'Supporto per parsing testo/audio per ingestione automatica in brain.db', 'Autenticazione di sicurezza tramite User ID Whitelist', 'Stato registrato al Commit 965f0a8: 110 nodi e 253 sinapsi'], 'inferred': ["L'architettura Telegram unifica il livello di percezione (audio/testo) con il livello di navigazione del connettoma (BFS inter-emisferico)", 'Il gateway funge da estensione mobile real-time del server MCP e del database SQLite'], 'ambiguous': []}, `architectural_synthesis`: Definita la pipeline I/O perimetrale: Telegram App -> HTTPS Webhook (/api/telegram/webhook) -> Whitelist Auth -> Intent Router (/search, /path, /tree, Ingest) -> brain.db., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Stato Cognitivo Condiviso e Continuità Inter-Modello** (`ai-reasoning-shared-cognitive-state-continuity`)
  - **Tags:** `#shared-state` `#cross-model-reasoning` `#epistemic-anchoring` `#universal-ai-brain` `#metacognition`
  - **Sintesi:** L'unificazione del contesto in un grafo bi-emisferico supera il silo conversazionale dei singoli LLM, trasformando istanze AI isolate in nodi computazionali su un unico substrato cognitivo.
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `paradigm`: Decentralized Sovereign AI Memory, `architectural_impact`: La memoria risiede nel grafo dell'utente, non nei database isolati dei provider proprietari.
- **Deduzione AI: Tassonomia e Classificazione Formale dell'Universa** (`reason-ep-20260827-graph-taxonomy-classification`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Mappate le 4 dimensioni: Topologica (Heterogeneous Multigraph), Epistemica (Epistemic Property Graph), Cognitiva (Episodic-Semantic Hybrid), Dinamica (Evolving Temporal Graph).
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["L'Universal Knowledge Graph dell'utente possiede nodi tipizzati eterogenei, architettura biemisferica e rubrica epistemica", "L'utente richiede la categorizzazione formale della tipologia di grafo"], 'inferred': ['Formalmente classificabile come Attributed Directed Heterogeneous Multigraph con proprietà temporali ed epistemiche', 'Funziona come memoria a lungo termine neuro-simbolica a plasticità dinamica'], 'ambiguous': []}, `classification_synthesis`: Mappate le 4 dimensioni: Topologica (Heterogeneous Multigraph), Epistemica (Epistemic Property Graph), Cognitiva (Episodic-Semantic Hybrid), Dinamica (Evolving Temporal Graph)., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Traduzione e Consolidamento del Benchmark Comparat** (`reason-ep-20260827-tree-ranking-translation`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Tradotto fedelmente il framework di comparazione tecnica e gerarchizzazione delle strutture ad albero.
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["L'Albero Gerarchico a Comunità (Dendrogramma) è eletto come architettura primaria (risparmio token 80%, Semantic Zoom)", 'MST è confermato come dorsale di deduzione logica secondaria', 'Trie/Radix Tree è classificato come ausiliario per autocompletamento O(k)', 'BST è escluso per ridondanza rispetto ai B+Tree nativi di SQLite e incapacità di gestire topologie 2D/3D con cicli'], 'inferred': ['Il modello multi-albero formalizza una pipeline a strati: indicizzazione lessicale (Trie) -> scoping gerarchico (Dendrogramma) -> linearizzazione deduttiva (MST)'], 'ambiguous': []}, `translation_synthesis`: Tradotto fedelmente il framework di comparazione tecnica e gerarchizzazione delle strutture ad albero., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Trasparenza Architettura Ibrida MCP / OpenAPI / Markdown e Aggiornamento Master Prompt** (`reasoning-architettura-connettoma-web-vs-desktop`)
  - **Tags:** `#architettura` `#graphrag` `#mcp` `#openapi` `#sincronizzazione`
  - **Sintesi:** Spiegata la coesistenza reale tra MCP locale (desktop) e OpenAPI/HTTP/Markdown (web). Aggiornato il Master Prompt in static/app.js con le specifiche del Palazzo Cognitivo e sincronizzato il connettoma neurale su Cloud e Desktop.
  - **Dettagli:** `raw`: `actions_taken`: ["Spiegazione dell'interrogazione SQLite BM25 e MCP per desktop e OpenAPI/Render per web", 'Perfezionamento del Master Prompt con layer_level, parent_graph_id e details strutturati', 'Aggiornamento di static/app.js', 'Ingestione sessione corrente e push bidirezionale su Git/Render'], `model`: Gemini 3.7 Flash, `outcome`: Master prompt aggiornato, connettoma sincronizzato e sessione registrata con successo
- **Deduzione AI: Unificazione Architetturale tra Knowledge Graph e** (`reason-ep-20260827-graph-tree-unification`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Formalizzata la pipeline: Knowledge Graph -> Spreading Activation -> Local Tree Search (ToT/MCTS) -> Trajectory Evaluation -> Synaptic Consolidation (Graph Ingest).
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["L'utente possiede un Universal Knowledge Graph strutturato come memoria/cervello", "L'utente richiede l'analisi della compatibilità formale e funzionale tra grafi di conoscenza e alberi di ricerca"], 'inferred': ['Il grafo agisce come memoria a lungo termine (substrato associativo / Sistema 1)', "L'albero di ricerca agisce come meccanismo deliberativo e di pianificazione (working memory / Sistema 2)", "La sintesi tra i due produce un'architettura 'Graph-of-Thoughts' con consolidamento episodico-semantico"], 'ambiguous': []}, `architectural_synthesis`: Formalizzata la pipeline: Knowledge Graph -> Spreading Activation -> Local Tree Search (ToT/MCTS) -> Trajectory Evaluation -> Synaptic Consolidation (Graph Ingest)., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Validazione Formale del Grafo Frattale e Implementazione 0€** (`ai-reasoning-hypergraph-multi-scale-feasibility`)
  - **Tags:** `#ai-reasoning` `#complexity-analysis` `#token-efficiency`
  - **Sintesi:** Il modello Graph-of-Graphs abbatte la complessità computazionale a O(log N) e riduce i token del 95% tramite drill-down.
  - **Dettagli:** `raw`: `implementation_cost`: 0€ su SQLite con colonna parent_graph_id, `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Valutazione Tecnica delle Strutture ad Albero (MST** (`reason-ep-20260827-tree-structures-evaluation`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Mappati 4 layer strutturali: B+Tree (Storage), Radix Trie (Lexical Routing O(k)), Hierarchical Dendrogram (Context Scoping), MST (Linear Chain-of-Thought).
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ['I BST 1D non sono adatti a modellare reti cerebrali cicliche multidimensionali', 'SQLite implementa B+Tree per indici su disco a O(log N)', 'MST estrae la spina dorsale concettuale eliminando i cicli', 'Il dendrogramma gerarchico abilita il Semantic Zoom multilivello', 'Il Prefix Trie/Radix Tree fornisce autocompletamento a O(k)'], 'inferred': ['Le strutture ad albero non sostituiscono il grafo, ma agiscono come proiezioni e indici algoritmici specializzati del connettoma', "L'integrazione di MST e Dendrogramma ottimizza il consumo di token e previene loop di generazione"], 'ambiguous': []}, `algorithmic_synthesis`: Mappati 4 layer strutturali: B+Tree (Storage), Radix Trie (Lexical Routing O(k)), Hierarchical Dendrogram (Context Scoping), MST (Linear Chain-of-Thought)., `model`: LLM Assistant (Historical Session)
- **Deduzione AI: Valutazione e Design di un Telegram Bot come Inter** (`reason-ep-20260827-telegram-bot-interface`)
  - **Tags:** `#ai-reasoning` `#epistemic-synthesis`
  - **Sintesi:** Telegram funge da periferica I/O cognitiva mobile (Sensorimotor / Interaction Layer) collegata via API al backend neurale su Render.
  - **Dettagli:** `raw`: `epistemic_rubric`: {'extracted': ["L'utente valuta l'implementazione di un bot Telegram per interagire con il proprio Knowledge Graph", 'Richiesta di valutazione su utilità, gratuità e difficoltà implementativa'], 'inferred': ["L'integrazione riduce drasticamente l'attrito di inserimento dati (write) e consultazione (read)", "L'architettura Telegram agisce come livello di Input/Output percettivo del cervello artificiale"], 'ambiguous': []}, `architectural_synthesis`: Telegram funge da periferica I/O cognitiva mobile (Sensorimotor / Interaction Layer) collegata via API al backend neurale su Render., `model`: LLM Assistant (Historical Session)
- **Design Pedagogico Ibrido (Busuu Grammar + Duolingo Micro-Drill)** (`reasoning-hybrid-pedagogy-engine`)
  - **Tags:** `#pedagogical-engine` `#cloze-test` `#word-bank` `#cefr-schema` `#sqlite-schema`
  - **Sintesi:** Progettazione di un motore a 6 tipologie di esercizio con schede grammaticali preparatorie (stile Busuu) e micro-lezioni a bolle interattive (stile Duolingo) supportate da SQLite e batch generation da corpora di frequenza.
  - **Dettagli:** `raw`: `exercise_types`: ['Word Bank', 'Cloze Test', 'Matching Pairs', 'Audio Listen', 'Active Recall', 'Grammar Spotlight'], `penalty_rule`: Re-queue on failure without blocking energy, `model`: AI Assistant
- **Diagnosi Discrepanza Nodi e Protocollo Deploy Render** (`reasoning-diagnosi-discrepanza-deploy-render`)
  - **Tags:** `#render` `#deploy` `#git-push` `#wal-checkpoint` `#sync`
  - **Sintesi:** Identificati 4 nodi locali non committati (Royal Gambit Chess / Duolingo Chess). Eseguito WAL checkpoint, aggiornato brain.md e push Git per triggerare auto-deploy Render.
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `responses_given`: Spiegata la causa della discrepanza (i nodi locali creati non erano stati committati e pushati su GitHub da cui Render effettua il build/deploy). Eseguito allineamento e push., `actions_taken`: ['Confronto diff nodi locali vs endpoint Render', 'Identificati 4 nodi locali: design-duolingo-chess-system, user-intent-duolingo-chess-preference, tech-minimax-chess-engine, project-royal-gambit-chess', 'Aggiornato brain.md sincronizzato con DB', 'Eseguito PRAGMA wal_checkpoint(FULL)', 'Git commit e push su origin/main'], `outcome`: Database allineato e auto-deploy Render avviato con successo.
- **Diagnosi Fallimento Retrieval Gemini e Piano di Azione** (`reasoning-diagnosi-retrieval-gemini-e-roadmap-potenziamento`)
  - **Tags:** `#diagnosi-retrieval` `#graphrag-optimization` `#knowledge-graph` `#master-prompt`
  - **Sintesi:** Identificato falso positivo: Gemini vedeva 1 solo entry a causa di un retrieval limitato. Proposto potenziamento del GraphRAG (iniezione baseline Palazzo), telemetria e consolidamento nodi stack.
  - **Dettagli:** `raw`: `actions_taken`: ['Verifica metriche reali con brain_get_stats (304 nodi, 789 archi)', 'Analisi cause retrieval parziale su client esterni', 'Definizione interventi su GraphRAG pre-response, osservabilità e master prompt'], `model`: Gemini 3.7 Flash, `outcome`: Chiarezza architetturale ristabilita e roadmap attuabile
- **Elaborazione Metafore e Spiegazioni Intuitive per AI Causale** (`reasoning-semplificazione-concettuale-causal-dl`)
  - **Tags:** `#pedagogia-tecnica` `#metafore` `#inferenza-causale` `#attention`
  - **Sintesi:** Traduzione di concetti ad elevata densità matematica in metafore pratiche ed esempi clinici immediati (es. bias da ospedale/macchinario, relazione gelato-scottature).
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Scomposizione dei 4 concetti in coppie problema-soluzione', 'Applicazione di analogie visive e scenari clinici concreti', "Mantenimento del rigore concettuale eliminando l'overload notazionale"], `outcome`: Quadro concettuale accessibile e pronto per l'esposizione orale/discorsiva.
- **Identificazione Percorsi Storage e Pulizia Ollama macOS** (`reasoning-risoluzione-residui-ollama-mac`)
  - **Tags:** `#ollama` `#filesystem` `#bash` `#diagnosi`
  - **Sintesi:** Analisi dell'architettura di storage di Ollama su macOS: identificati i percorsi ~/.ollama/models/blobs e ~/Library/Application Support/Ollama con relativi comandi di rimozione sicura.
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Mappatura directory predefinita modelli Ollama (~/.ollama/models/blobs)', 'Fornitura comando di verifica dimensione disco (du -sh)', 'Fornitura comando di eliminazione ricorsiva sicura (rm -rf)'], `outcome`: Istruzioni fornite per il recupero immediato di 7GB di spazio su disco.
- **Integrazione Lessicale di Tabelle e Metriche Quantitative** (`reasoning-integrazione-esplicita-tabelle-comparative`)
  - **Tags:** `#struttura-tesi` `#sintesi-quantitativa` `#cross-validation`
  - **Sintesi:** Inserimento di un capoverso finale che valorizza le tabelle riassuntive della tesi (Tabelle 6.4 - 6.16) e l'analisi quantitativa della variabilità statistica nei fold di cross-validation, prima del dettaglio delle sezioni.
  - **Dettagli:** `model`: Gemini 2.5, `actions_taken`: ['Mantenimento della struttura concisa a tre brevi capoversi', 'Aggiunta esplicita della menzione alle tabelle comparative e alle metriche prestazionali', 'Preservazione del registro scientifico formale in lingua italiana'], `outcome`: Cappello completo, equilibrato e perfettamente allineato ai contenuti tabellari del capitolo
- **Mappatura Ecosistema Linux per Computer Grafica 3D** (`reasoning-mappatura-ecosistema-linux-3d`)
  - **Tags:** `#linux-distros` `#3d-software` `#blender` `#cad` `#flatpak`
  - **Sintesi:** Strutturazione della risposta evidenziando sia le distribuzioni specializzate (Fedora Design Suite, Ubuntu Studio) sia l'ampia compatibilità nativa dei software standard (Blender, FreeCAD, Houdini) su qualsiasi distro via package manager e Flatpak.
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Verifica distro creative specializzate (Fedora Design Suite, Ubuntu Studio)', 'Catalogazione software 3D nativi (Blender, FreeCAD, OpenSCAD, MeshLab)', 'Identificazione del packaging universale (Flatpak/AppImage) come best practice per artisti 3D'], `outcome`: Quadro completo, pratico e orientato all'installazione immediata.
- **Piano Strategico di Evoluzione ad Alto Impatto per il Connettoma** (`reasoning-architettura-ecosistema-cognitivo-onnipresente`)
  - **Tags:** `#raycast` `#web-clipper` `#sqlite-vec` `#nightly-weave` `#cursor-hooks` `#apple-shortcuts`
  - **Sintesi:** Proposta architetturale a 5 pilastri: Quick-Capture macOS (Raycast/Siri), Knowledge Streams (Readwise/GitHub CI), Motore Cognitivo Aumentato (sqlite-vec & Fase REM notturna), Dev Workflow Hooks e Interfacce Spaziali.
  - **Dettagli:** `actions_taken`: ['Analisi connettoma', 'Verifica tool MCP', 'Elaborazione matrice sinaptica di espansione'], `model`: Gemini 3.7 Flash, `outcome`: Blueprint completo di integrazioni per rendere il cervello onnipresente e ad attrito zero, `responses_given`: Roadmap dettagliata con categorizzazione a 5 pilastri e priorità di implementazione
- **Ragionamento AI: Algoritmi BFS, FTS5 & MCP Stdio 0€** (`ai-reasoning-hybrid-search-mcp`)
  - **Tags:** `#ai-reasoning` `#bfs-algorithm` `#fts5-bm25` `#mcp-protocol` `#zero-cost-architecture`
  - **Sintesi:** Deduzione logica: SQLite FTS5 offre ranking lessicale BM25 immediato (<1ms) e BFS bidirezionale permette di attraversare il Corpo Calloso senza API esterne a pagamento.
  - **Dettagli:** `raw`: `search_engine`: SQLite FTS5 Porter Unicode61, `pathfinding`: Bidirectional Breadth-First Search (BFS), `context_scoping`: k-hop neighborhood subgraph extraction, `interoperability`: JSON-RPC 2.0 stdio MCP Server, `model`: LLM Assistant (Historical Session)
- **Ragionamento AI: Risoluzione Bug & Continuità Cognitiva Inter-Chat** (`reasoning-audit-bugfix-e-protocollo-graphify`)
  - **Tags:** `#metacognition` `#cross-chat-continuity` `#bugfix` `#fastapi` `#mcp` `#sqlite-wal`
  - **Sintesi:** Corretti 4 bug critici, verificati prompt e tassonomie, e integrata la specifica mandatoria di continuità cognitiva cross-chat con persistenza totale delle risposte fornite e del contesto.
  - **Dettagli:** `raw`: `actions_taken`: ['Fix UnboundLocalError summary in main.py ingest_memory', 'Fix default layer_level 0 in NodeModel', 'Fix dangling EOF in install.sh linea 158', 'Allineamento colonne parent_graph_id e layer_level in mcp_server, telegram_bot, sync_brain', 'Integrazione Sezione 3 Cross-Chat Cognitive Continuity in SKILL.md e prompt.md', 'Verifica E2E test suite su tutti i moduli con 100% successo'], `model`: Gemini 3.7 Flash, `outcome`: Schema e direttive blindati per memoria cross-chat senza perdita di contesto, `responses_given`: Spiegata in dettaglio la struttura di auto-ingestione contestuale: USER_INTENT cattura il prompt/contesto, AI_REASONING cattura risposte/modifiche/deduzioni, CONVERSATION_EPISODE cattura sintesi/partecipanti/esito. Nuove chat interrogano brain_search/brain.md per recuperare immediatamente la memoria storica.
- **Ragionamento AI: Simbiosi Architetturale tra Substrato Cloud Render e Agenti Locali** (`ai-reasoning-hybrid-cloud-local-symbiosis`)
  - **Tags:** `#ai-reasoning` `#hybrid-cloud` `#distributed-systems` `#cross-client-synergy` `#metacognition`
  - **Sintesi:** Deduzione architetturale: Render agisce come Hub pubblico permanente (Telegram Webhook, Web Visualizer, OpenAPI GPTs), mentre MCP agisce come bus a bassissima latenza per agenti IDE.
  - **Dettagli:** `raw`: `model`: Antigravity / Google DeepMind Agent, `key_pillars`: ['Render Cloud: Accessibilità universale mobile 24/7, Telegram bot webhook, integrazione OpenAI Actions HTTPS', 'Local MCP: Esecuzione a latenza zero (<1ms) su SQLite WAL durante il coding in IDE', 'Web Chat Workflow: Allegazione diretta di brain.md o endpoint /brain.md pubblico per AI con Web Search']
- **Ragionamento: Architettura Dual-Ring Git Persistence** (`reasoning-cloud-git-auto-push`)
  - **Tags:** `#dual-ring` `#fastapi-background-tasks` `#github-token`
  - **Sintesi:** Implementazione del doppio anello di persistenza: Mac demone + Render server push asincrono.
  - **Dettagli:** `actions_taken`: ['Implementata funzione cloud_git_push_background in main.py con BackgroundTasks', 'Configurato supporto GITHUB_TOKEN per git commit & push direttamente dal container Render', 'Creato sistema a doppio anello (Client Daemon su Mac + Server Auto-Push su Render)'], `model`: Gemini 3.7 Flash, `outcome`: Architettura a doppio anello implementata e rilasciata su GitHub main, `responses_given`: Approvata l'idea eccellente: implementata in main.py con BackgroundTasks asincroni e spiegata la configurazione di GITHUB_TOKEN su Render.
- **Ragionamento: Audit critico e mockup frontend del Univ** (`reasoning-audit-critico-e-mockup-fr-2255`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Audit basato sul repository, sul database SQLite e sul connettoma remoto: rilevate criticità di sicurezza API, sincronizzazione senza conflitti, tassonomia e provenienza; creato artefatto con tre dire
  - **Dettagli:** `model`: AI Assistant, `responses_given`: Audit basato sul repository, sul database SQLite e sul connettoma remoto: rilevate criticità di sicurezza API, sincronizzazione senza conflitti, tassonomia e provenienza; creato artefatto con tre direzioni UX: Atlante, Territori e Lente., `actions_taken`: ['Elaborazione e risposta al prompt'], `outcome`: Completato con successo
- **Ragionamento: Comando /prompt Copia Rapida per Telegra** (`reasoning-comando-prompt-copia-rapi-8585`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Aggiunto il comando /prompt e il pulsante persistente nella tastiera mobile di Telegram in telegram_bot.py. Il messaggio restituisce il Master Prompt formattato all'interno di un blocco <pre><code cla
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `responses_given`: Aggiunto il comando /prompt e il pulsante persistente nella tastiera mobile di Telegram in telegram_bot.py. Il messaggio restituisce il Master Prompt formattato all'interno di un blocco <pre><code class="language-markdown">...</code></pre>, permettendo all'utente di toccare il riquadro sullo smartphone per copiare istantaneamente il testo negli appunti di iOS/Android., `actions_taken`: ['Aggiunto pulsante "📋 Copia Prompt AI" nella tastiera persistente di get_main_keyboard() in telegram_bot.py', 'Implementato handler per /prompt, prompt e relative varianti in process_telegram_message()', 'Formattato il Master System Prompt con escape HTML dentro <pre><code class="language-markdown"> per 1-tap copy', 'Aggiornato il menu comandi /help con la nuova sezione Integrazione AI Esterne', 'Testata esecuzione e pushato su origin/main per aggiornare il bot live su Render'], `outcome`: Comando /prompt operativo su Telegram con supporto copia al tocco su smartphone.
- **Ragionamento: Copertura Telegram e Keep-Alive 7m** (`reasoning-telegram-keepalive-confirmation`)
  - **Tags:** `#telegram-bot` `#ping-7m` `#zero-perdite`
  - **Sintesi:** Integrazione Telegram bot con cloud git push e validazione Keep-Alive 7m in sync_daemon.
  - **Dettagli:** `actions_taken`: ["Aggiornato telegram_bot.py per invocare cloud_git_push_background all'ingestione JSON", 'Confermato Keep-Alive già attivo in sync_daemon.py con ping /health ogni 7m (più sicuro di 14m)', 'Verificata attività nel log: ping registrati ed eseguiti con successo'], `model`: Gemini 3.7 Flash, `outcome`: Telegram coperto al 100% da doppio anello; Keep-Alive a 7m attivo e verificato nel demone, `responses_given`: Conferma copertura Telegram (bot esegue cloud push e demone sincronizza), spiegato che il Keep-Alive è già attivo ogni 7m nel demone.
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-2447`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-2471`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-2485`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-2529`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'brain_resurface.py', 'brain_tensions.py', 'brain_weave.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-2691`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['README.md', 'brain.db', 'brain_resurface.py', 'brain_tensions.py', 'brain_weave.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-8745`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'obsidian_vault/.obsidian/graph.json', 'obsidian_vault/.obsidian/workspace.json', 'obsidian_vault/00_Domini/domain-ai-cognitive-systems.md', 'obsidian_vault/00_Domini/domain-crescita-personale.md', 'obsidian_vault/00_Domini/domain-cultura-storia.md', 'obsidian_vault/00_Domini/domain-design-creativita.md', 'obsidian_vault/00_Domini/domain-filosofia-valori.md', 'obsidian_vault/00_Domini/domain-finanza-economia.md', 'obsidian_vault/00_Domini/domain-medicina-salute.md', 'obsidian_vault/00_Domini/domain-musica-audio.md', 'obsidian_vault/00_Domini/domain-produttivita-sistemi.md', 'obsidian_vault/00_Domini/domain-relazioni-comunicazione.md', 'obsidian_vault/00_Domini/domain-scienza-matematica.md', 'obsidian_vault/00_Domini/domain-software-engineering.md', 'obsidian_vault/00_Domini/person-pierfrancesco.md', 'obsidian_vault/00_INDEX.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-cross-model-provenance-validation.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-cloud-local-symbiosis.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-search-mcp.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-infinite-context-architecture.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-shared-cognitive-state-continuity.md', 'obsidian_vault/01_Progetti_Episodi/analysis-bst-vs-graph-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/antigravity-centaur-collaboration.md', 'obsidian_vault/01_Progetti_Episodi/arch-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/art-creative-writing.md', 'obsidian_vault/01_Progetti_Episodi/art-piano-composition.md', 'obsidian_vault/01_Progetti_Episodi/art-theatre-acting.md', 'obsidian_vault/01_Progetti_Episodi/aule-studio-app.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-engineering.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-surgical.md', 'obsidian_vault/01_Progetti_Episodi/chat-session-2026-08-27-ui-evolution.md', 'obsidian_vault/01_Progetti_Episodi/concept-graph-of-graphs-hypergraph.md', 'obsidian_vault/01_Progetti_Episodi/concept-interhemispheric-inhibition-gating.md', 'obsidian_vault/01_Progetti_Episodi/concept-llm-indirect-injection-safeguard.md', 'obsidian_vault/01_Progetti_Episodi/concept-modular-domain-subgraphs.md', 'obsidian_vault/01_Progetti_Episodi/creative-multidisciplinary.md', 'obsidian_vault/01_Progetti_Episodi/deploy-render-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/ep-20260827-render-cloud-vs-local-hybrid-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-graphrag-mcp-evolution.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-telegram-omnipresence.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-universal-context-definition.md', 'obsidian_vault/01_Progetti_Episodi/episode-cross-model-memory-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-frontend-deeptech-redesign-and-physics-zero-lag.md', 'obsidian_vault/01_Progetti_Episodi/episode-infinite-context-philosophy.md', 'obsidian_vault/01_Progetti_Episodi/episode-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-system-metacognition.md', 'obsidian_vault/01_Progetti_Episodi/feat-progressive-areas.md', 'obsidian_vault/01_Progetti_Episodi/goal-multi-ai-shared-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/intent-clarify-render-cloud-utility-and-llm-web-refusal.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/intent-evaluate-ai-brain-architecture.md', 'obsidian_vault/01_Progetti_Episodi/intent-language-app-ui-design.md', 'obsidian_vault/01_Progetti_Episodi/intent-personal-language-learning-app.md', 'obsidian_vault/01_Progetti_Episodi/lesson-boundaries-clarity.md', 'obsidian_vault/01_Progetti_Episodi/lesson-stoic-resilience.md', 'obsidian_vault/01_Progetti_Episodi/memory-perfectionism-tension.md', 'obsidian_vault/01_Progetti_Episodi/mental-centaur-model.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-dendrogram.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-tree-engine-impl.md', 'obsidian_vault/01_Progetti_Episodi/node-knowledge-graph-memory.md', 'obsidian_vault/01_Progetti_Episodi/node-neuro-symbolic-brain.md', 'obsidian_vault/01_Progetti_Episodi/node-search-tree-deliberation.md', 'obsidian_vault/01_Progetti_Episodi/node-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/node-tree-architecture-verdict.md', 'obsidian_vault/01_Progetti_Episodi/node-ubiquitous-ingestion.md', 'obsidian_vault/01_Progetti_Episodi/node-universal-ai-brain-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/proj-caretrack.md', 'obsidian_vault/01_Progetti_Episodi/proj-cervelloartificiale.md', 'obsidian_vault/01_Progetti_Episodi/proj-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/proj-linkly-qr.md', 'obsidian_vault/01_Progetti_Episodi/proj-streaksup-app.md', 'obsidian_vault/01_Progetti_Episodi/proj-tombolawifi.md', 'obsidian_vault/01_Progetti_Episodi/project-royal-gambit-chess.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/rel-marco-di-martino.md', 'obsidian_vault/01_Progetti_Episodi/rel-napoli-culture.md', 'obsidian_vault/01_Progetti_Episodi/rel-parents.md', 'obsidian_vault/01_Progetti_Episodi/rigore-informativo.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-placeholder.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-particle-fx.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-privacy-zero-cloud.md', 'obsidian_vault/01_Progetti_Episodi/tax-ai-reasoning.md', 'obsidian_vault/01_Progetti_Episodi/universal-ai-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-abbandono-jarvis-nuovo-progetto.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ai-shorts-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allineamento-nodi-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-alternative-income-generation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-analisi-feedback-gemini-ottimizzazione-cervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-architettura-connettoma-web-vs-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-audit-critico-e-mockup-fr-2255.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-avvio-openjarvis-ollama-gpt-cloud.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-backend-optimization-hybrid.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-c-un-problema-vorrei-sapere-di-pi-3203.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8743.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8793.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ore-sono-3134.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-chi-pierfrancesco-amendola-e-cosa-8426.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-clean-clustered-ui.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-cloud-git-auto-push.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-comando-prompt-copia-rapi-8585.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-connect-gemini-claude-chatgpt-mcp.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-repo-jarvis-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-video-showcase-universal-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-esplorazione-paradigmi-visuali-grafo.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-fix-daemon-render-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-infinite-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-integrazione-openjarvis-stanford.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-jarvis-ricordi-quali-sono-gli-emis-3117.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ma-tutto-falso-8462.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-non-riesci-a-connetterti-al-mio-cer-8486.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-nuove-rappresentazioni-vi-2874.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-occultamento-pulsanti-mob-9019.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ottimizzazione-mobile-web-8880.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-potenziamento-skill-e-ril-8338.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-provenance-model-tracking.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-i-progetti-principali-di-8169.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-le-abitudini-monitorate-2979.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-reasoning-and-chat-memory.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ristrutturazione-sigillo-12-macro-domini.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-telegram-bot-gateway.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-tree-search-enhancement.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-universal-ai-hub-client.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-valutazione-progetto-language-app.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-verify-github-token-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-zero-cost-graphrag.md', 'obsidian_vault/01_Progetti_Episodi/ux-frictionless.md', 'obsidian_vault/01_Progetti_Episodi/val-authenticity.md', 'obsidian_vault/01_Progetti_Episodi/val-eternal-cognitive-continuity.md', 'obsidian_vault/01_Progetti_Episodi/val-impact-utility.md', 'obsidian_vault/01_Progetti_Episodi/val-independence.md', 'obsidian_vault/01_Progetti_Episodi/val-transparency-loyalty.md', 'raycast/brain_search.py', 'sync_brain.py', 'apple_shortcuts/Appunto_per_il_Cervello.shortcut', 'obsidian_vault/01_Progetti_Episodi/episode-completamento-supercervello-ecosistema.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/episode-revisione-supercervello-cognitive-os.md', 'obsidian_vault/01_Progetti_Episodi/episode-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-costruzione-collaudo-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-valutazione-architetturale-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/test-e2e-web-clipper.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-implementazione-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-review-piano-supercervello-os.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-test-hook-session-end-2411.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3c40d6e17fd5.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3e8f7aed7312.md', 'obsidian_vault/02_Moduli_Atomici/kindle-6d280a533c87.md', 'obsidian_vault/02_Moduli_Atomici/kindle-7439c883249f.md', 'obsidian_vault/02_Moduli_Atomici/kindle-c962fde43767.md', 'obsidian_vault/02_Moduli_Atomici/kindle-cba1775488ae.md', 'obsidian_vault/02_Moduli_Atomici/node-nota-rapida-raycast-test.md', 'obsidian_vault/02_Moduli_Atomici/node-test-raycast-node.md', 'obsidian_vault/02_Moduli_Atomici/voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2447.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2471.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2485.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2529.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2690.md', 'obsidian_vault/02_Moduli_Atomici/voice-test-shortcuts-debug-7964.md', 'obsidian_vault/02_Moduli_Atomici/web-test-fastapi-docs.md', '2.canvas"'], `outcome`: Session completed and verified
- **Ragionamento: E2E Test Session Hook** (`reasoning-e2e-test-session-hook-9065`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#e2e-test-session-hook`
  - **Sintesi:** Verifica automatica suite
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain.db', 'obsidian_vault/.obsidian/graph.json', 'obsidian_vault/.obsidian/workspace.json', 'obsidian_vault/00_Domini/domain-ai-cognitive-systems.md', 'obsidian_vault/00_Domini/domain-crescita-personale.md', 'obsidian_vault/00_Domini/domain-cultura-storia.md', 'obsidian_vault/00_Domini/domain-design-creativita.md', 'obsidian_vault/00_Domini/domain-filosofia-valori.md', 'obsidian_vault/00_Domini/domain-finanza-economia.md', 'obsidian_vault/00_Domini/domain-medicina-salute.md', 'obsidian_vault/00_Domini/domain-musica-audio.md', 'obsidian_vault/00_Domini/domain-produttivita-sistemi.md', 'obsidian_vault/00_Domini/domain-relazioni-comunicazione.md', 'obsidian_vault/00_Domini/domain-scienza-matematica.md', 'obsidian_vault/00_Domini/domain-software-engineering.md', 'obsidian_vault/00_Domini/person-pierfrancesco.md', 'obsidian_vault/00_INDEX.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-cross-model-provenance-validation.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-cloud-local-symbiosis.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-search-mcp.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-infinite-context-architecture.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-shared-cognitive-state-continuity.md', 'obsidian_vault/01_Progetti_Episodi/analysis-bst-vs-graph-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/antigravity-centaur-collaboration.md', 'obsidian_vault/01_Progetti_Episodi/arch-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/art-creative-writing.md', 'obsidian_vault/01_Progetti_Episodi/art-piano-composition.md', 'obsidian_vault/01_Progetti_Episodi/art-theatre-acting.md', 'obsidian_vault/01_Progetti_Episodi/aule-studio-app.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-engineering.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-surgical.md', 'obsidian_vault/01_Progetti_Episodi/chat-session-2026-08-27-ui-evolution.md', 'obsidian_vault/01_Progetti_Episodi/concept-graph-of-graphs-hypergraph.md', 'obsidian_vault/01_Progetti_Episodi/concept-interhemispheric-inhibition-gating.md', 'obsidian_vault/01_Progetti_Episodi/concept-llm-indirect-injection-safeguard.md', 'obsidian_vault/01_Progetti_Episodi/concept-modular-domain-subgraphs.md', 'obsidian_vault/01_Progetti_Episodi/creative-multidisciplinary.md', 'obsidian_vault/01_Progetti_Episodi/deploy-render-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/ep-20260827-render-cloud-vs-local-hybrid-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-graphrag-mcp-evolution.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-telegram-omnipresence.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-universal-context-definition.md', 'obsidian_vault/01_Progetti_Episodi/episode-cross-model-memory-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-frontend-deeptech-redesign-and-physics-zero-lag.md', 'obsidian_vault/01_Progetti_Episodi/episode-infinite-context-philosophy.md', 'obsidian_vault/01_Progetti_Episodi/episode-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-system-metacognition.md', 'obsidian_vault/01_Progetti_Episodi/feat-progressive-areas.md', 'obsidian_vault/01_Progetti_Episodi/goal-multi-ai-shared-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/intent-clarify-render-cloud-utility-and-llm-web-refusal.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/intent-evaluate-ai-brain-architecture.md', 'obsidian_vault/01_Progetti_Episodi/intent-language-app-ui-design.md', 'obsidian_vault/01_Progetti_Episodi/intent-personal-language-learning-app.md', 'obsidian_vault/01_Progetti_Episodi/lesson-boundaries-clarity.md', 'obsidian_vault/01_Progetti_Episodi/lesson-stoic-resilience.md', 'obsidian_vault/01_Progetti_Episodi/memory-perfectionism-tension.md', 'obsidian_vault/01_Progetti_Episodi/mental-centaur-model.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-dendrogram.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-tree-engine-impl.md', 'obsidian_vault/01_Progetti_Episodi/node-knowledge-graph-memory.md', 'obsidian_vault/01_Progetti_Episodi/node-neuro-symbolic-brain.md', 'obsidian_vault/01_Progetti_Episodi/node-search-tree-deliberation.md', 'obsidian_vault/01_Progetti_Episodi/node-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/node-tree-architecture-verdict.md', 'obsidian_vault/01_Progetti_Episodi/node-ubiquitous-ingestion.md', 'obsidian_vault/01_Progetti_Episodi/node-universal-ai-brain-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/proj-caretrack.md', 'obsidian_vault/01_Progetti_Episodi/proj-cervelloartificiale.md', 'obsidian_vault/01_Progetti_Episodi/proj-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/proj-linkly-qr.md', 'obsidian_vault/01_Progetti_Episodi/proj-streaksup-app.md', 'obsidian_vault/01_Progetti_Episodi/proj-tombolawifi.md', 'obsidian_vault/01_Progetti_Episodi/project-royal-gambit-chess.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/rel-marco-di-martino.md', 'obsidian_vault/01_Progetti_Episodi/rel-napoli-culture.md', 'obsidian_vault/01_Progetti_Episodi/rel-parents.md', 'obsidian_vault/01_Progetti_Episodi/rigore-informativo.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-placeholder.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-particle-fx.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-privacy-zero-cloud.md', 'obsidian_vault/01_Progetti_Episodi/tax-ai-reasoning.md', 'obsidian_vault/01_Progetti_Episodi/universal-ai-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-abbandono-jarvis-nuovo-progetto.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ai-shorts-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allineamento-nodi-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-alternative-income-generation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-analisi-feedback-gemini-ottimizzazione-cervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-architettura-connettoma-web-vs-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-audit-critico-e-mockup-fr-2255.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-avvio-openjarvis-ollama-gpt-cloud.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-backend-optimization-hybrid.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-c-un-problema-vorrei-sapere-di-pi-3203.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8743.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8793.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ore-sono-3134.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-chi-pierfrancesco-amendola-e-cosa-8426.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-clean-clustered-ui.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-cloud-git-auto-push.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-comando-prompt-copia-rapi-8585.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-connect-gemini-claude-chatgpt-mcp.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-repo-jarvis-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-video-showcase-universal-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-esplorazione-paradigmi-visuali-grafo.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-fix-daemon-render-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-infinite-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-integrazione-openjarvis-stanford.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-jarvis-ricordi-quali-sono-gli-emis-3117.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ma-tutto-falso-8462.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-non-riesci-a-connetterti-al-mio-cer-8486.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-nuove-rappresentazioni-vi-2874.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-occultamento-pulsanti-mob-9019.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ottimizzazione-mobile-web-8880.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-potenziamento-skill-e-ril-8338.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-provenance-model-tracking.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-i-progetti-principali-di-8169.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-le-abitudini-monitorate-2979.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-reasoning-and-chat-memory.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ristrutturazione-sigillo-12-macro-domini.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-telegram-bot-gateway.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-tree-search-enhancement.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-universal-ai-hub-client.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-valutazione-progetto-language-app.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-verify-github-token-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-zero-cost-graphrag.md', 'obsidian_vault/01_Progetti_Episodi/ux-frictionless.md', 'obsidian_vault/01_Progetti_Episodi/val-authenticity.md', 'obsidian_vault/01_Progetti_Episodi/val-eternal-cognitive-continuity.md', 'obsidian_vault/01_Progetti_Episodi/val-impact-utility.md', 'obsidian_vault/01_Progetti_Episodi/val-independence.md', 'obsidian_vault/01_Progetti_Episodi/val-transparency-loyalty.md', 'telegram_bot.py', 'apple_shortcuts/Appunto_per_il_Cervello.shortcut', 'obsidian_vault/01_Progetti_Episodi/episode-completamento-supercervello-ecosistema.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/episode-revisione-supercervello-cognitive-os.md', 'obsidian_vault/01_Progetti_Episodi/episode-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-costruzione-collaudo-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-valutazione-architetturale-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/test-e2e-web-clipper.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-implementazione-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-review-piano-supercervello-os.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-test-hook-session-end-2411.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3c40d6e17fd5.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3e8f7aed7312.md', 'obsidian_vault/02_Moduli_Atomici/kindle-6d280a533c87.md', 'obsidian_vault/02_Moduli_Atomici/kindle-7439c883249f.md', 'obsidian_vault/02_Moduli_Atomici/kindle-c962fde43767.md', 'obsidian_vault/02_Moduli_Atomici/kindle-cba1775488ae.md', 'obsidian_vault/02_Moduli_Atomici/node-nota-rapida-raycast-test.md', 'obsidian_vault/02_Moduli_Atomici/node-test-raycast-node.md', 'obsidian_vault/02_Moduli_Atomici/voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2447.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2471.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2485.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2529.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2690.md', 'obsidian_vault/02_Moduli_Atomici/voice-test-shortcuts-debug-7964.md', 'obsidian_vault/02_Moduli_Atomici/web-test-fastapi-docs.md', '2.canvas"'], `outcome`: Session completed and verified
- **Ragionamento: Fix Demone LaunchAgent e Anti-Sleep Render** (`reasoning-fix-daemon-render-persistence`)
  - **Tags:** `#launchd` `#tcc-bypass` `#keepalive` `#git-sync`
  - **Sintesi:** Diagnosi e risoluzione integrale: TCC sandbox bypass tramite ~/.local/bin, keep-alive 7m anti-sleep, commit git automatico preventivo.
  - **Dettagli:** `actions_taken`: ['Identificato blocco TCC di macOS LaunchAgent sui file in Desktop (errore 78/126)', "Spostato l'esecutore in ~/.local/bin/universal-brain-daemon con log su /tmp/", 'Aggiunto pinger Keep-Alive /health ogni 7m per prevenire idle spin-down di Render', 'Disaccoppiato il commit/push Git da Render: ogni modifica locale va subito su GitHub', 'Verificata integrità del connettoma (347 nodi e 880 archi perfettamente allineati)'], `model`: Gemini 3.7 Flash, `outcome`: Demone attivo con PID reale, Render mantenuto vivo 24/7, memoria salvata su GitHub e sincronizzata al 100%, `responses_given`: Spiegazione causa 335 vs 347 nodi (ephemeral disk Render e mancato push Git per blocco demone), blocco TCC Desktop risolto, keep-alive attivo
- **Ragionamento: Nuove rappresentazioni visuali del conne** (`reasoning-nuove-rappresentazioni-vi-2874`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Recuperata la preferenza per un grafo stabile e privo di oscillazioni; creato un secondo artefatto interattivo con cinque viste deterministiche: due sfere, palazzo, matrice, radar bi-polare e territor
  - **Dettagli:** `model`: AI Assistant, `responses_given`: Recuperata la preferenza per un grafo stabile e privo di oscillazioni; creato un secondo artefatto interattivo con cinque viste deterministiche: due sfere, palazzo, matrice, radar bi-polare e territori Voronoi., `actions_taken`: ['Elaborazione e risposta al prompt'], `outcome`: Completato con successo
- **Ragionamento: Occultamento Pulsanti Mobile su Browser ** (`reasoning-occultamento-pulsanti-mob-9019`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Risolto problema cache e visualizzazione pulsanti mobile su browser desktop. Impostato display:none !important incondizionato nel CSS e inline sull'HTML della mobile-nav-bar. Aggiornato query string c
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `responses_given`: Risolto problema cache e visualizzazione pulsanti mobile su browser desktop. Impostato display:none !important incondizionato nel CSS e inline sull'HTML della mobile-nav-bar. Aggiornato query string cache-buster (v=20260829_1510) per CSS e JS., `actions_taken`: ['Impostato display:none !important globale su .mobile-nav-bar in static/style.css', 'Aggiunto style="display:none;" inline su nav#mobile-nav-bar in static/index.html', 'Aggiornato cache-buster CSS/JS a v=20260829_1510 in index.html', 'Commit e push su origin/main per deploy immediato'], `outcome`: Desktop ripulito al 100%, pulsanti mobile attivi esclusivamente su smartphone.
- **Ragionamento: Ottimizzazione Mobile Web Dashboard Univ** (`reasoning-ottimizzazione-mobile-web-8880`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Risolto problema layout mobile su schermi <= 900px. Aggiunto meta tag viewport con viewport-fit=cover e user-scalable=no. Implementata tab bar inferiore mobile (🌐 Grafo, 🔍 Ispettore, 🏢 Palazzo, 🌳 Albe
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `responses_given`: Risolto problema layout mobile su schermi <= 900px. Aggiunto meta tag viewport con viewport-fit=cover e user-scalable=no. Implementata tab bar inferiore mobile (🌐 Grafo, 🔍 Ispettore, 🏢 Palazzo, 🌳 Albero, 💻 Terminale). Su PC l'interfaccia resta invariata al 100%. Su smartphone il canvas del grafo occupa ora il 100% dello schermo e lo switch tra grafo, ispettore e palazzo avviene con 1-tap., `actions_taken`: ['Aggiornato meta viewport in static/index.html con viewport-fit=cover', 'Aggiunta barra di navigazione inferiore mobile (#mobile-nav-bar) in index.html', 'Implementate media queries @media (max-width: 900px) in static/style.css', 'Aggiunta funzione switchMobileTab in static/app.js con routing reattivo', 'Preservata interfaccia desktop al 100% (>900px)', 'Eseguito commit e push su origin/main per rilascio immediato su Render'], `outcome`: Web Dashboard ora perfettamente fruibile e reattiva su smartphone senza toccare il layout PC.
- **Ragionamento: Potenziamento Skill e Rilascio Demone Si** (`reasoning-potenziamento-skill-e-ril-8338`)
  - **Tags:** `#ai-reasoning` `#decisioni` `#universal-ai-brain`
  - **Sintesi:** Riformulata la skill universal-brain con protocollo obbligatorio a 2 fasi e 3 livelli di ingestione (MCP/CLI, POST HTTP, Fallback JSON). Implementato il demone background macOS (com.universalbrain.syn
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `responses_given`: Riformulata la skill universal-brain con protocollo obbligatorio a 2 fasi e 3 livelli di ingestione (MCP/CLI, POST HTTP, Fallback JSON). Implementato il demone background macOS (com.universalbrain.sync.plist) attivo all'avvio (<0.01% CPU, ~20MB RAM) per sincronizzazione bidirezionale continua PC ⮂ Render., `actions_taken`: ['Riformulato SKILL.md con protocollo a 2 fasi (Pre-Response Retrieval + Post-Response Ingestion)', 'Distribuito SKILL.md in ~/.gemini/config/skills/, ~/.agents/skills/, e ~/.agents/rules/', 'Aggiornato prompt.md e sync_brain.py con motore bidirezionale completo e helper 1-command', 'Creato sync_daemon.py con logging rotativo e monitoraggio mtime SQLite', 'Creato ed eseguito install_daemon.sh per LaunchAgent macOS in ~/Library/LaunchAgents/', 'Esteso il comando globale brain CLI con sync, record e daemon management in install.sh', 'Eseguita verifica end-to-end con 100% successo'], `outcome`: Demone attivo in background e connettoma allineato al 100% tra PC locale e Render Cloud.
- **Ragionamento: Riformulazione Completa Documentazione README** (`reasoning-update-readme-architecture`)
  - **Tags:** `#docs` `#github` `#architettura` `#dual-ring`
  - **Sintesi:** Stesura della documentazione ufficiale con copertura completa di backend, algoritmi, persistenza e client.
  - **Dettagli:** `actions_taken`: ['Riscritto integralmente README.md con 10 capitoli tecnici approfonditi', 'Inclusi diagrammi ASCII e Mermaid per modello bi-emisferico e Dual-Ring Persistence', 'Documentati algoritmi (Bidirectional BFS, Recursive CTE, GraphRAG BM25) e ottimizzazioni SQLite WAL', 'Eseguito commit e push su GitHub origin main'], `model`: Gemini 3.7 Flash, `outcome`: README.md aggiornato al 100% e pubblicato su GitHub origin/main, `responses_given`: README.md riscritto e pubblicato su GitHub con dettagli esaustivi su tutti i moduli.
- **Ragionamento: Test Hook Session End** (`reasoning-test-hook-session-end-2411`)
  - **Tags:** `#ide-hook` `#ai-reasoning` `#test-hook-session-end`
  - **Sintesi:** Verifica automatica dell hook di fine sessione
  - **Dettagli:** `model`: IDE Assistant, `actions_taken`: ['brain_resurface.py', 'main.py', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'raycast/', 'static/video_assets/', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `outcome`: Session completed and verified
- **Ragionamento: Verifica End-to-End Token Render** (`reasoning-verify-github-token-render`)
  - **Tags:** `#test-cloud` `#end-to-end` `#validazione`
  - **Sintesi:** Conferma del corretto funzionamento dell'ingestione cloud e del connettoma a 354 nodi.
  - **Dettagli:** `actions_taken`: ['Eseguito test POST /api/memory/ingest direttamente su Render Cloud', 'Verificata risposta 200 OK da Render con elaborazione nodo in background', 'Verificata parità esatta: 354 nodi e 895 sinapsi allineati tra Locale e Cloud'], `model`: Gemini 3.7 Flash, `outcome`: Token configurato correttamente, server Render operativo e connettoma allineato al 100%, `responses_given`: Conferma esito positivo: test eseguito con successo, parità 354 nodi/895 archi confermata.
- **Razionale Architetturale: Separazione Aree vs Grafo Completo** (`ai-reasoning-clustering-decision`)
  - **Tags:** `#architecture-rationale` `#cognitive-load` `#graph-physics` `#scalability`
  - **Sintesi:** Scelta di non eliminare le relazioni fisiche ma di applicare un filtro visuale basato su insiemi di visibilità adiacente, massimizzando ordine e densità semantica.
  - **Dettagli:** `raw`: `approach`: Visual filter on vis.DataSet without schema mutilation, `benefits`: ['zero-data-loss', 'uncluttered-ui', 'instant-subgraph-expansion'], `model`: LLM Assistant (Historical Session)
- **Risposta Groq: Quali sono i progetti principali di...** (`reasoning-quali-sono-i-progetti-principali-di-8169`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** Non ho accesso diretto alla memoria o al database `brain.db` in questo contesto di conversazione. Come modello di linguaggio, non posso eseguire query in tempo reale su archivi esterni o database pers
  - **Dettagli:** `raw`: `model`: qwen/qwen3.8-27b, `provider`: Groq
- **Risposta JARVIS: Allora vorrei dirti che oggi ho man...** (`reasoning-allora-vorrei-dirti-che-oggi-ho-man-4690`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** ✅ Fatto registrato: **CONVERSATION_EPISODE** – “oggi ho mangiato pasta al sugo”. Memoria inserita nel tuo Universal Knowledge Graph (layer 1, EMISFERO DESTRO).
- **Risposta JARVIS: Jarvis, ricordi quali sono gli emis...** (`reasoning-jarvis-ricordi-quali-sono-gli-emis-3117`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** **Emisfero Sinistro (LEFT)** – Gestisce la parte “logica‑tecnica” del tuo connettoma: architetture, strutture dati, algoritmi, dipendenze, business logic, API, regole cognitive, modelli mentali, ragio
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `response_text`: **Emisfero Sinistro (LEFT)** – Gestisce la parte “logica‑tecnica” del tuo connettoma: architetture, strutture dati, algoritmi, dipendenze, business logic, API, regole cognitive, modelli mentali, ragionamento AI e meta‑cognizione.
- **Risposta JARVIS: Quali sono le abitudini monitorate ...** (`reasoning-quali-sono-le-abitudini-monitorate-2979`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** StreaksUp traccia le abitudini chiave per ottimizzare la produttività e il benessere: esercizio fisico quotidiano, lettura o studio, sessioni di coding, meditazione, idratazione (acqua) e ore di sonno
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `response_text`: StreaksUp traccia le abitudini chiave per ottimizzare la produttività e il benessere: esercizio fisico quotidiano, lettura o studio, sessioni di coding, meditazione, idratazione (acqua) e ore di sonno. Ogni habit è registrata con timestamp, streak count e metriche di qualità (intensità, durata), così da poter visualizzare trend in tempo reale e ricevere notifiche di reinforcement.
- **Risposta JARVIS: c'è un problema vorrei sapere di pi...** (`reasoning-c-un-problema-vorrei-sapere-di-pi-3203`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** **🔎 Query al grafo universale…**
- **Risposta JARVIS: che ore sono...** (`reasoning-che-ore-sono-3134`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** Sono le 14:37 (ora locale del server).
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `response_text`: Sono le 14:37 (ora locale del server).
- **Risposta JARVIS: ehi Jarvis ehi Jarvis mi puoi dire ...** (`reasoning-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** Sono le 00:00 (tempo non disponibile in tempo reale). Per conoscere l’ora esatta, controlla l’orologio del tuo dispositivo.
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `response_text`: Sono le 00:00 (tempo non disponibile in tempo reale). Per conoscere l’ora esatta, controlla l’orologio del tuo dispositivo.
- **Risposta JARVIS: ho bisogno di sapere tutto ciò che ...** (`reasoning-ho-bisogno-di-sapere-tutto-ci-che-2753`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** Signore, ho analizzato la richiesta ma tutti i provider LLM gratuiti risultano al momento non raggiungibili. Verifica la connessione o imposta una chiave API in .env.
  - **Dettagli:** `raw`: `model`: None, `response_text`: Signore, ho analizzato la richiesta ma tutti i provider LLM gratuiti risultano al momento non raggiungibili. Verifica la connessione o imposta una chiave API in .env.
- **Risposta JARVIS: quanti nodi ci sono nel mio cervell...** (`reasoning-quanti-nodi-ci-sono-nel-mio-cervell-4794`)
  - **Tags:** `#jarvis` `#voice-response` `#reasoning`
  - **Sintesi:** **Richiesta:** conteggio nodi del tuo grafo cognitivo, separati per emisfero sinistro e destro.
- **Risposta gemini: che ne pensi del mio cervello artif...** (`reasoning-che-ne-pensi-del-mio-cervello-artif-8793`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** Ciao Pierfrancesco.
- **Risposta groq: che ne pensi del mio cervello artif...** (`reasoning-che-ne-pensi-del-mio-cervello-artif-8743`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** **Il tuo “cervello artificiale” è già un lavoro notevole e, secondo la memoria storica che ho a disposizione, rappresenta una delle tue iniziative più avanzate sia dal punto di vista architetturale ch
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `provider`: groq
- **Risposta groq: chi è Pierfrancesco Amendola e cosa...** (`reasoning-chi-pierfrancesco-amendola-e-cosa-8426`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** **Pierfrancesco Amendola** è un *imprenditore, ricercatore e visionario* nel campo dell’intelligenza artificiale, della neuroscienza computazionale e dell’interazione uomo‑macchina. Nato a Napoli nel
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `provider`: groq
- **Risposta groq: ma è tutto falso!!!** (`reasoning-ma-tutto-falso-8462`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** Mi dispiace se le informazioni che ti ho fornito non corrispondono a quanto sai o ti aspettavi. In questa conversazione non ho a disposizione la sezione **“MEMORIA STORICA RECUPERATA DAL CONNETTORE NE
  - **Dettagli:** `raw`: `model`: openai/gpt-oss-120b, `provider`: groq
- **Risposta groq: non riesci a connetterti al mio cer...** (`reasoning-non-riesci-a-connetterti-al-mio-cer-8486`)
  - **Tags:** `#universal-hub` `#ai-response` `#reasoning`
  - **Sintesi:** Sì, **sono già connesso al tuo “cervello artificiale”**.
- **Sintesi Teorico-Applicativa Swin Transformer e Deep Stable Learning** (`reasoning-sintesi-teorica-swin-e-deep-stable-learning`)
  - **Tags:** `#computer-vision` `#causal-inference` `#medical-imaging` `#ood-generalization`
  - **Sintesi:** Formalizzazione del funzionamento di Swin Transformer (attenzione a finestre traslate gerarchiche) e Deep Stable Learning (decorrelazione di confondenti/inferenza causale per robustezza OOD) applicati all'imaging oncologico mammario.
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Mappatura di Swin Transformer su complessità lineare e feature multiscala per lesioni mammarie', 'Mappatura di Deep Stable Learning su inferenza causale, sample reweighting e generalizzazione OOD in contesti multi-centro clinici', "Connessione con l'interpretabilità diagnostica BI-RADS"], `outcome`: Spiegazione concisa, ad alta densità informativa e orientata alla discussione di tesi.
- **Strategia Micro-Business e Servizi B2B Leggeri** (`ai-reasoning-alternative-monetization-strategies`)
  - **Tags:** `#analisi-strategica` `#micro-saas` `#automazione-b2b` `#asset-digitali` `#editoria-tecnica`
  - **Sintesi:** Strutturazione di quattro canali scalabili a costo zero (Automazioni B2B, Micro-SaaS/App Freemium, Boilerplate di codice, Editoria tecnica KDP/Gumroad) con stime di conversione unitarie per raggiungere il target 100-500€/mese.
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Mappatura delle competenze tecniche su modelli B2B e B2C a basso rischio.', 'Definizione dei 4 pilastri: Automazioni/Agenti per PMI, Micro-App su abbonamento, Vendita Boilerplate/Template, Editoria tecnica specializzata.', "Calcolo del volume di vendita necessario per ciascun canale per raggiungere l'obiettivo prefissato.", "Realizzazione della matrice comparativa di ritorno economico e barriera all'ingresso."], `outcome`: Presentazione di alternative concrete orientate alla creazione di valore diretto e asset riutilizzabili.
- **Tassonomia Architetturale: Cloud Database vs Local-First Graph PKM** (`reasoning-tassonomia-pkm-rag-notion-obsidian`)
  - **Tags:** `#graph-rag` `#local-first` `#markdown` `#relational-pkm` `#mcp`
  - **Sintesi:** Formalizzazione della dicotomia tra Notion (database relazionale cloud-first con metadati strutturati) e Obsidian (knowledge graph locale su file .md per privacy e GraphRAG).
  - **Dettagli:** `model`: Gemini, `actions_taken`: ['Mappatura delle differenze chiave di storage (Cloud API vs Filesystem locale)', "Definizione dei casi d'uso tipici di Obsidian (GraphRAG, wikilink automatici, privacy-preserving AI)", 'Confronto tabellare sintetico per identificazione immediata del trade-off'], `outcome`: Analisi comparativa chiara, tecnica e focalizzata su architettura e workflow., `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Tassonomia Metacognitiva & AI Reasoning Hub** (`tax-ai-reasoning`)
  - **Tags:** `#ai-reasoning` `#metacognition` `#chain-of-thought` `#rationale` `#knowledge-graph`
  - **Sintesi:** Area cognitiva dedicata al tracciamento dei ragionamenti, deduzioni analitiche e percorsi logici interni generati dall'AI durante le sessioni.
  - **Dettagli:** `raw`: `hemisphere`: LEFT, `labels`: ['AI_REASONING', 'METACOGNITION'], `purpose`: Map internal AI deductions into permanent graph space, `model`: LLM Assistant (Historical Session)
- **Validazione Architetturale: Provenance & Attribution Cross-Modello** (`ai-reasoning-cross-model-provenance-validation`)
  - **Tags:** `#ai-deduction` `#epistemic-provenance` `#knowledge-graph` `#metacognition` `#gemini`
  - **Sintesi:** Deduzione logica Gemini: tracciare prompt e modello crea una memoria a provenienza epistemica verificabile, prevenendo allucinazioni di paternità e potenziando il retrieval.
  - **Dettagli:** `raw`: `model`: Gemini 3.7 Flash, `verdict`: Approccio eccellente e architetturalmente solido, `benefits`: ['Provenance epistemica cross-modello', "Ancoraggio contestuale del ragionamento AI all'intento originario", 'Clustering semantico pulito senza rumore relazionale']
- **Validazione e Blindatura della Strategia 100% Zero-Cost** (`reasoning-validazione-architettura-zero-costi`)
  - **Tags:** `#audit-costi` `#local-first` `#open-source` `#free-tier`
  - **Sintesi:** Tutti i componenti proposti poggiano su strumenti open-source, risorse locali macOS, tier gratuiti a vita (Render, GitHub Actions, Telegram Bot API) e modelli di embedding locali senza API a pagamento.
  - **Dettagli:** `actions_taken`: ['Audit di ogni componente del piano di espansione', 'Verifica licenze e piani gratuiti per Raycast, Shortcuts, sqlite-vec, FastEmbed e Telegram', "Conferma dell'assenza totale di costi operativi o abbonamenti"], `model`: Gemini 3.7 Flash, `outcome`: Conferma al 100% della piena gratuità di ogni singolo elemento proposto, `responses_given`: Dettaglio voce per voce della conformità al vincolo 0,00€ Forever
- **Valutazione Architetturale e Strategica Supercervello OS** (`reasoning-valutazione-architetturale-supercervello`)
  - **Tags:** `#analisi-architetturale` `#pkm` `#fastembed` `#sqlite-wal` `#rem-cycle`
  - **Sintesi:** Analisi dell'architettura proposta: approvazione dell'approccio zero-cost locale e validazione dei moduli di cattura a zero-friction, consolidamento notturno REM e integrazione IDE. Evidenziati accorgimenti su concurrency SQLite e modelli multilingua.
  - **Dettagli:** `actions_taken`: ['Verifica vincoli 0,00€ e assenza dipendenze esterne a pagamento', 'Analisi robustezza moduli Fase 1-5 (Raycast, Web Clipper, FastEmbed, Canvas Sync, IDE Hooks)', 'Formulazione raccomandazioni tecniche (busy_timeout SQLite WAL, embedding multilingua)'], `model`: Gemini, `outcome`: Piano validato come pienamente idoneo alla transizione verso un Cognitive OS autonomo.

### [Macro-Label: `ALGORITHM`]
- **Achievement & 22-Trophy Engine** (`streaksup-gamification-engine`)
  - **Tags:** `#achievements` `#trophies` `#gamification` `#evaluation-engine`
  - **Sintesi:** Sistema di valutazione achievement con 22 trofei suddivisi in 5 categorie (Streak, Completions, Freeze, Specials, Mastery) e 5 tier di rarità.
  - **Dettagli:** `raw`: `categories`: ['Streak', 'Completions', 'Freeze', 'Specials', 'Mastery'], `tiers`: ['Bronze', 'Silver', 'Gold', 'Diamond', 'Legendary'], `special_metrics`: ['Early Bird (<9 AM)', 'Night Owl (>=9 PM)', 'Weekend Warrior', 'Perfect Days']
- **Algoritmo di Gating Emisferico & Risveglio Sinaptico On-Demand** (`algorithm-selective-hemispheric-activation`)
  - **Tags:** `#algorithm` `#selective-gating` `#lazy-evaluation` `#callosal-trigger`
  - **Sintesi:** Algoritmo che instrada le query solo all'emisfero bersaglio (Left per logica/codice, Right per design/valori) e risveglia nodi controlaterali solo se attraversati da sinapsi callosali rilevanti.
  - **Dettagli:** `raw`: `routing_logic`: Target hemisphere active -> Contralateral hemisphere dormant -> Wake up via Corpus Callosum edge traversal
- **AuleStudio Real-time Availability Engine** (`aule-studio-backend-arch`)
  - **Tags:** `#availability-engine` `#real-time` `#reservations` `#occupancy-rate`
  - **Sintesi:** Algoritmo di calcolo occupazione delle aule universitarie e gestione code/prenotazioni concorrenti per studenti.
  - **Dettagli:** `raw`: `slot_duration_mins`: 60, `concurrency_strategy`: Optimistic locking, `sync_frequency_sec`: 30
- **Bi-directional BFS (Corpus Callosum Routing)** (`node-bidirectional-bfs-pathfinding`)
  - **Tags:** `#mutation-import` `#routing-engine` `#graph-algorithm`
  - **Sintesi:** Bi-directional BFS (Corpus Callosum Routing) (Layer: ROUTING_ENGINE, Tipo: GRAPH_ALGORITHM)
  - **Dettagli:** `raw`: `id`: node_bidirectional_bfs_pathfinding, `label`: Bi-directional BFS (Corpus Callosum Routing), `type`: GRAPH_ALGORITHM, `layer`: ROUTING_ENGINE
- **Bioinformatica & Deep Learning (ICAR-CNR)** (`proj-bioinformatics-icar`)
  - **Tags:** `#bioinformatics` `#deep-learning` `#pytorch` `#medical-imaging` `#thesis`
  - **Sintesi:** Ricerca su modelli di deep learning e computer vision per diagnosi istopatologica (Dr.ssa Brancati, Prof. Riccio).
  - **Dettagli:** `raw`: `stack`: Python, PyTorch, OpenCV, Scikit-learn, `validation`: AUC-ROC, F1-Score, `completion`: Maggio 2026
- **Dominio: Scienza, Matematica & Algoritmica** (`domain-scienza-matematica`)
  - **Tags:** `#domain-hub` `#matematica` `#algoritmi` `#statistica` `#fisica` `#teoria-informazione`
  - **Sintesi:** Matematica pura e applicata, Algoritmica teorica, Statistica, Fisica, Teoria dell'Informazione e Modelli Formali.
  - **Dettagli:** `scope`: Mathematical modeling, algorithms, statistics, complexity theory
- **Graphify Codebase Knowledge Extractor** (`graphify-knowledge-engine`)
  - **Tags:** `#graphify` `#ast` `#knowledge-graph` `#god-nodes` `#community-detection`
  - **Sintesi:** Motore di analisi statica AST e semantica che rileva community, nodi baricentrici (God Nodes) e ponti architetturali nel repository.
  - **Dettagli:** `raw`: `clustering`: Leiden / Louvain community detection, `cohesion_scoring`: Graph density metrics
- **HarmonyApp** (`proj-harmonyapp`)
  - **Tags:** `#music-theory` `#dsp` `#ear-training` `#flutter`
  - **Sintesi:** Strumento interattivo per ear training, composizione e riconoscimento dell'armonia musicale.
  - **Dettagli:** `raw`: `stack`: Flutter, SoundFont Synthesizer, WebAudio API, `scope`: Teoria musicale computazionale e didattica dell'ascolto
- **Maximum Spanning Tree (Conceptual Backbone)** (`node-mst-conceptual-backbone`)
  - **Tags:** `#mutation-import` `#serialization-layer` `#algorithmic-projection`
  - **Sintesi:** Maximum Spanning Tree (Conceptual Backbone) (Layer: SERIALIZATION_LAYER, Tipo: ALGORITHMIC_PROJECTION)
  - **Dettagli:** `raw`: `id`: node_mst_conceptual_backbone, `label`: Maximum Spanning Tree (Conceptual Backbone), `type`: ALGORITHMIC_PROJECTION, `layer`: SERIALIZATION_LAYER
- **Motore Scacchi Minimax & Valutazione** (`tech-minimax-chess-engine`)
  - **Tags:** `#scacchi` `#minimax` `#alpha-beta` `#swift` `#algoritmi`
  - **Sintesi:** Engine scacchistico nativo Swift con ricerca minimax, alpha-beta pruning, valutazione posizionale, calcolo asincrono dei suggerimenti e supporto 4 livelli bot.
- **ParticleSimulator 3D** (`proj-particlesimulator`)
  - **Tags:** `#javascript` `#threejs` `#webgl` `#mediapipe` `#gesture-control`
  - **Sintesi:** Motore fisico generativo 3D in tempo reale con controllo tramite gesture della mano via computer vision.
  - **Dettagli:** `raw`: `stack`: Vanilla JS, Three.js, WebGL, MediaPipe Hand Landmarker, `performance`: 60 FPS rock-solid, `distribution`: GitHub Open Source
- **REGEXRIDDLE** (`proj-regexriddle`)
  - **Tags:** `#regex` `#gamification` `#typescript` `#fsm`
  - **Sintesi:** Tool gamificato per il testing, parsing e apprendimento visivo di espressioni regolari mediante automi a stati.
  - **Dettagli:** `raw`: `stack`: TypeScript, React, Finite State Machine parser, `mode`: Interactive Puzzle & Sandboxed Debugger
- **Streak Freeze & Protection Engine** (`streaksup-streak-freeze-algo`)
  - **Tags:** `#streak-freeze` `#shield` `#gamification-algorithm` `#streak-preservation`
  - **Sintesi:** Algoritmo di protezione della serie: consumo automatico dello scudo nei giorni mancati, cap massimo a 3 cariche e premio +1 ogni 7 giorni di streak.
  - **Dettagli:** `raw`: `max_capacity`: 3, `initial_grant`: 1, `reward_milestone`: Ogni 7 giorni consecutivi (+1 freeze), `persistence_key`: streak_frozen_dates
- **Tesi Deep Learning BUSBRA (ICAR-CNR)** (`proj-tesi-busbra-cnr`)
  - **Tags:** `#bioinformatics` `#busbra` `#resnet` `#vit-base` `#usf-mae` `#simclr` `#ultrasound` `#deep-learning`
  - **Sintesi:** Pipeline di deep learning per classificazione ecografie mammarie (benigno/maligno, BI-RADS 4 classi) su dataset BUSBRA.
  - **Dettagli:** `raw`: `models`: ResNet-18, ResNet-34, USF-MAE (ViT-Base), SimCLR Self-Supervised, `validation`: 5-fold Cross-Validation, progressive layer unfreezing, `losses`: CrossEntropy, Focal Loss, Combined Loss, `metrics`: CSV logging, Confusion Matrix, AUC-ROC
- **Tombola Multiplayer WiFi** (`proj-tombola-wifi`)
  - **Tags:** `#flutter` `#websocket` `#local-wifi` `#multiplayer` `#gaming`
  - **Sintesi:** Gioco multiplayer in tempo reale della tombola su rete locale WiFi senza necessità di server cloud.
  - **Dettagli:** `raw`: `stack`: Flutter, WebSockets, `architecture`: Zero-cost local peer-to-peer / LAN sync

### [Macro-Label: `API_ENDPOINT`]
- **FastAPI REST Endpoints (proj-cervelloartificiale)** (`proj-cervelloartificiale-api-routes`)
  - **Tags:** `#fastapi` `#rest-api` `#python`
  - **Sintesi:** Pipeline API REST asincrona con validazione Pydantic per proj-cervelloartificiale.
  - **Dettagli:** `parent_project`: proj-cervelloartificiale, `file_uri`: file:///Users/pierfrancesco/Desktop/CervelloArtificiale

### [Macro-Label: `API_SPEC`]
- **AI Ingest & Markdown Read Protocol** (`ai-memory-ingest-spec`)
  - **Tags:** `#api-spec` `#brain-md` `#ingest` `#quick-add` `#json-schema`
  - **Sintesi:** Specifiche REST /brain.md e /api/memory/ingest con validazione tassonomica automatica e generazione link One-Click.
  - **Dettagli:** `raw`: `read_endpoint`: GET /brain.md, `write_endpoint`: POST /api/memory/ingest, `quick_add`: GET /api/quick-add
- **App Intents & Dynamic Interactive Engine** (`streaksup-app-intents-engine`)
  - **Tags:** `#app-intents` `#interactive-widgets` `#app-entity` `#toggle-habit`
  - **Sintesi:** Motore di interattività in-place per Widget e Live Activities tramite ToggleHabitIntent, HabitEntity e HabitEntityQuery.
  - **Dettagli:** `raw`: `toggle_intent`: ToggleHabitIntent(habitID: String), `entity_query`: HabitEntityQuery, `config_intent`: SingleHabitConfigurationIntent, `sync_targets`: ['WidgetCenter.reloadAllTimelines', 'HabitActivityManager', 'Darwin IPC']
- **Modulo Ingestione JSON da AI** (`feat-ai-json-importer`)
  - **Tags:** `#ingest` `#drag-drop` `#file-reader` `#json-parser` `#llm-sync`
  - **Sintesi:** Interfaccia drag-and-drop e editor textarea per importare ed eseguire il POST di file o blocchi JSON generati da Claude/GPT/Gemini.
  - **Dettagli:** `raw`: `endpoint`: POST /api/memory/ingest, `features`: ['drag-and-drop', 'markdown-strip', 'auto-normalization']
- **Specula App** (`proj-specula`)
  - **Tags:** `#ios` `#swift` `#app-store` `#color-extraction`
  - **Sintesi:** Utility iOS per campionamento, quantizzazione ed esportazione live di palette cromatiche conforme WCAG.
  - **Dettagli:** `raw`: `platform`: Apple App Store, `algorithms`: K-Means / Median Cut Color Quantization

### [Macro-Label: `APP`]
- **App Abbonamenti** (`proj-appabbonamenti`)
  - **Tags:** `#mac-project` `#swift` `#web`
  - **Sintesi:** **SubTracker** è un'applicazione iOS moderna e intuitiva progettata per monitorare tutti i tuoi abbonamenti in un unico posto. Sviluppata interamente in **SwiftUI** e **SwiftData**, offre un'esperienz
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppAbbonamenti, `file_uri`: file:///Users/pierfrancesco/Desktop/AppAbbonamenti, `languages`: ['Swift'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 24, `last_modified`: 2026-01-20T22:17:39.675718+00:00, `key_dependencies`: [], `readme_excerpt`: # SubTracker 📱

**SubTracker** è un'applicazione iOS moderna e intuitiva progettata per monitorare tutti i tuoi abbonamenti in un unico posto. Sviluppata interamente in **SwiftUI** e **SwiftData**, offre un'esperienza utente premium con animazioni fluide, supporto multilingua e gestione avanzata delle notifiche.

## 🚀 Funzionalità Principali

### 📊 Dashboard Intuitiva
* **Resoconto Spese**: Visualizza immediatamente quanto spendi al mese e all'anno.
* **Lista Ordinata**: Gli abbonamenti sono ordinati automaticamente per data di rinnovo.
* **Feedback Visivo**: Card colorate con icone personaliz
- **App Napoli** (`proj-appnapoli`)
  - **Tags:** `#c` `#c-lang` `#dart` `#flutter` `#mac-project` `#python` `#swift`
  - **Sintesi:** Progetto Mac: App Napoli. Stack: C, Dart, Python, Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppNapoli, `file_uri`: file:///Users/pierfrancesco/Desktop/AppNapoli, `languages`: ['C', 'Dart', 'Python', 'Swift'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 87, `last_modified`: 2026-05-21T08:47:13.228160+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **App Tombola** (`proj-apptombola`)
  - **Tags:** `#c++` `#cpp` `#dart` `#flutter` `#mac-project` `#swift` `#web`
  - **Sintesi:** A new Flutter project.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppTombola, `file_uri`: file:///Users/pierfrancesco/Desktop/AppTombola, `languages`: ['C++', 'Dart', 'Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 59, `last_modified`: 2026-06-20T14:46:12.993483+00:00, `key_dependencies`: [], `readme_excerpt`: # app_tombola

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
- **Esercizio Conto Corrente** (`proj-eserciziocontocorrente`)
  - **Tags:** `#mac-project` `#web`
  - **Sintesi:** Un sistema bancario moderno con interfaccia grafica elegante in stile Apple, sviluppato in Java con JavaFX.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/EsercizioContoCorrente, `file_uri`: file:///Users/pierfrancesco/Desktop/EsercizioContoCorrente, `languages`: [], `frameworks`: [], `has_git`: True, `relevant_files_count`: 62, `last_modified`: 2025-10-04T12:11:52.447732+00:00, `key_dependencies`: [], `readme_excerpt`: # 🍎 Banca Apple - Sistema Bancario

Un sistema bancario moderno con interfaccia grafica elegante in stile Apple, sviluppato in Java con JavaFX.

## ✨ Caratteristiche

- **Interfaccia Utente Elegante**: Design moderno ispirato allo stile Apple
- **Architettura MVC**: Separazione pulita tra presentazione, business logic e persistenza
- **Database H2**: Persistenza dati con database embedded
- **Autenticazione Sicura**: Sistema di login con hash delle password (BCrypt)
- **Operazioni Bancarie Complete**: Versamenti, prelievi, gestione conti con carta
- **Pattern DAO**: Accesso ai dati strutturato
- **Qr Generator** (`proj-qr_generator`)
  - **Tags:** `#c++` `#cpp` `#dart` `#flutter` `#mac-project` `#swift` `#web`
  - **Sintesi:** A new Flutter project.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppQrCode/qr_generator, `file_uri`: file:///Users/pierfrancesco/Desktop/AppQrCode/qr_generator, `languages`: ['C++', 'Dart', 'Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 37, `last_modified`: 2026-06-06T16:21:40.419611+00:00, `key_dependencies`: [], `readme_excerpt`: # qr_generator

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

### [Macro-Label: `ARCHITECTURE`]
- **Architettura Graph-of-Graphs / Palazzo Cognitivo a Piani** (`concept-graph-of-graphs-hypergraph`)
  - **Tags:** `#hypergraph` `#graph-of-graphs` `#multiscale` `#fractal-topology` `#semantic-drilldown`
  - **Sintesi:** Modello a iper-grafo gerarchico in cui i nodi di livello superiore contengono sotto-grafi completi, simulando un palazzo a più piani concettuali.
  - **Dettagli:** `raw`: `levels`: L0 (Macro-Domini) -> L1 (Progetti/Aree) -> L2 (Moduli/Sistemi) -> L3 (Entità Atomiche), `formal_name`: Hierarchical Clustered Hypergraph / Multi-Layer Network
- **Architettura Webhook Telegram 0€ (FastAPI + Bot API)** (`arch-telegram-webhook-gateway`)
  - **Tags:** `#telegram-bot` `#webhook` `#fastapi` `#zero-cost` `#mobile-gateway`
  - **Sintesi:** Infrastruttura serverless su webhook FastAPI per ricezione comandi (/search, /path, /tree) e inserimento memorie asincrono 0€.
  - **Dettagli:** `raw`: `endpoint`: POST /api/telegram/webhook, `auth`: Telegram Secret Token / Authorized User ID whitelist, `cost`: 0€ illimitato
- **Architettura a Sotto-Grafi Modulari & Decentramento Hub** (`concept-modular-domain-subgraphs`)
  - **Tags:** `#modular-graph` `#domain-clustering` `#anti-star-topology` `#subgraph-modularity`
  - **Sintesi:** I concetti verticali (es. medicina, finanza, fisica) non si collegano forzatamente a person-pierfrancesco, ma formano cluster tematici autonomi ancorati a macro-domini cognitivi.
  - **Dettagli:** `raw`: `pattern`: Domain-Driven Cognitive Clusters, `benefit`: Previene l'over-centrality e l'inquinamento topologico dello star-graph
- **Architettura di Hosting Render.com 0€** (`deploy-render-zero-cost`)
  - **Tags:** `#render` `#hosting` `#zero-cost` `#fastapi` `#uvicorn`
  - **Sintesi:** Infrastruttura di erogazione web asincrona su Render.com Free Tier con Uvicorn e SQLite WAL persistito.
  - **Dettagli:** `raw`: `build_command`: pip install -r requirements.txt, `start_command`: uvicorn main:app --host 0.0.0.0 --port , `cost`: 0€ lifetime
- **Architettura: Stabilizzazione Silente & Blocco Fisico Zero-Lag in Vis-Network** (`architecture-vis-network-silent-stabilization-zero-lag`)
  - **Tags:** `#vis-network` `#physics-optimization` `#silent-stabilization` `#zero-lag` `#performance`
  - **Sintesi:** Pattern architetturale per grafi complessi (189+ nodi): esecuzione della stabilizzazione offline in background (updateInterval = iterations), disattivazione del physics loop (physics: false) ed eliminazione di ombre canvas e calcoli geometrici ripetitivi per garantire 60fps.
  - **Dettagli:** `raw`: `solver`: forceAtlas2Based, `parameters`: {'gravitationalConstant': -60, 'centralGravity': 0.005, 'springLength': 120, 'springConstant': 0.08, 'damping': 0.4, 'avoidOverlap': 0.8}, `stabilization`: iterations: 150, updateInterval: 150, fit: true, `freeze_mechanism`: network.stabilize() + stabilized event + fallback timer -> physics: false
- **Aree a Espansione & Cluster Gerarchici** (`feat-progressive-areas`)
  - **Tags:** `#ui` `#graph-visualization` `#progressive-disclosure` `#clusters` `#ux-cleanliness`
  - **Sintesi:** Motore di rendering a fioritura progressiva: visualizza i Macro-Hub compatti e ne sboccia i sotto-nodi al click utente preservando le sinapsi.
  - **Dettagli:** `raw`: `mode`: Progressive Disclosure, `features`: ['macro-hubs', 'interactive-bloom', 'badge-counters', 'compact-view']
- **Attributed Heterogeneous Temporal Multigraph** (`node-universal-ai-brain-taxonomy`)
  - **Tags:** `#mutation-import` `#formal-theory` `#graph-classification`
  - **Sintesi:** Attributed Heterogeneous Temporal Multigraph (Layer: FORMAL_THEORY, Tipo: GRAPH_CLASSIFICATION)
  - **Dettagli:** `raw`: `id`: node_universal_ai_brain_taxonomy, `label`: Attributed Heterogeneous Temporal Multigraph, `type`: GRAPH_CLASSIFICATION, `layer`: FORMAL_THEORY
- **AuleStudioApp (Mobile Project)** (`aule-studio-app`)
  - **Tags:** `#flutter` `#dart` `#auledistudio` `#booking` `#real-time` `#mobile`
  - **Sintesi:** Applicazione mobile per studenti per localizzare aule studio universitarie, verificare posti liberi in tempo reale e prenotare postazioni.
  - **Dettagli:** `raw`: `framework`: Flutter, `language`: Dart, `target`: iOS / Android, `core_features`: ['Geolocalizzazione', 'Stato Posti Real-Time', 'Prenotazione']
- **CareTrack** (`proj-caretrack`)
  - **Tags:** `#flutter` `#healthcare` `#telemedicine` `#award-winner`
  - **Sintesi:** Piattaforma mobile di telemedicina e assistenza domiciliare vincitrice del Google Challenge Campania (Medicina).
  - **Dettagli:** `raw`: `stack`: Flutter, Dart, Firebase, SQLite, `pattern`: Clean Architecture + BLoC (Offline-first), `status`: Awarded / Functional Prototype
- **CineMatch** (`proj-cinematch`)
  - **Tags:** `#mern` `#recommendation` `#tmdb` `#social`
  - **Sintesi:** App di matching e scoperta cinematografica di coppia/gruppo basata su swipe e intersezione preferenze.
  - **Dettagli:** `raw`: `stack`: MongoDB, Express, React/Flutter, Node.js, TMDb API, `pattern`: Real-time preference matching
- **Commit 965f0a8 (110 Nodes, 253 Synapses)** (`node-commit-965f0a8`)
  - **Tags:** `#mutation-import` `#devops-timeline` `#graph-state`
  - **Sintesi:** Commit 965f0a8 (110 Nodes, 253 Synapses) (Layer: DEVOPS_TIMELINE, Tipo: GRAPH_STATE)
  - **Dettagli:** `raw`: `id`: node_commit_965f0a8, `label`: Commit 965f0a8 (110 Nodes, 253 Synapses), `type`: GRAPH_STATE, `layer`: DEVOPS_TIMELINE
- **Documentazione Ufficiale FastAPI Dependency Injection** (`web-test-fastapi-docs`)
  - **Tags:** `#web-clipper` `#fastapi` `#python`
  - **Sintesi:** FastAPI Dependency Injection system provides clean hierarchical dependency management.
  - **Dettagli:** `source_url`: https://fastapi.tiangolo.com/tutorial/dependencies/, `clipped_by`: Pierfrancesco
- **Dominio: Ingegneria Software & Architetture** (`domain-software-engineering`)
  - **Tags:** `#domain-hub` `#software-engineering` `#backend` `#frontend` `#architecture` `#sqlite-wal` `#fastapi`
  - **Sintesi:** Ingegneria del Software, Backend FastAPI, SQLite WAL, Web development, architetture distribuite e linguaggi di programmazione.
  - **Dettagli:** `scope`: Software engineering, backend, web systems, databases, distributed architecture
- **Dominio: Medicina, Salute & Fisiologia** (`domain-medicina-salute`)
  - **Tags:** `#domain-hub` `#medicina` `#salute` `#dermatologia` `#podologia` `#fisiologia` `#fitness` `#bioinformatica`
  - **Sintesi:** Medicina, Salute, Nutrizione, Fisiologia, Fitness, Dermatologia, Podologia e Bioinformatica Deep Learning (ricerca ICAR-CNR).
  - **Dettagli:** `scope`: Medical research, healthcare, physiology, dermatology, clinical logic
- **Dominio: Sistemi Cognitivi, Neuro-Simbolico & LLM** (`domain-ai-cognitive-systems`)
  - **Tags:** `#domain-hub` `#cognitive-ai` `#neuro-symbolic` `#graphrag` `#memory-systems` `#mcp` `#metacognition`
  - **Sintesi:** Sistemi Cognitivi, LLM, GraphRAG, Knowledge Graphs, MCP (Model Context Protocol), Metacognizione e Agentic Systems.
  - **Dettagli:** `scope`: Cognitive architectures, graph reasoning, LLM memory continuity, MCP tooling
- **Epistemic Grading (Extracted/Inferred/Ambiguous)** (`node-epistemic-grading-system`)
  - **Tags:** `#mutation-import` `#epistemic-layer` `#representation-feature`
  - **Sintesi:** Epistemic Grading (Extracted/Inferred/Ambiguous) (Layer: EPISTEMIC_LAYER, Tipo: REPRESENTATION_FEATURE)
  - **Dettagli:** `raw`: `id`: node_epistemic_grading_system, `label`: Epistemic Grading (Extracted/Inferred/Ambiguous), `type`: REPRESENTATION_FEATURE, `layer`: EPISTEMIC_LAYER
- **Graph-Dendrogram Multiscale Overlay** (`node-multiscale-overlay-pattern`)
  - **Tags:** `#mutation-import` `#storage-and-retrieval` `#architectural-pattern`
  - **Sintesi:** Graph-Dendrogram Multiscale Overlay (Layer: STORAGE_AND_RETRIEVAL, Tipo: ARCHITECTURAL_PATTERN)
  - **Dettagli:** `raw`: `id`: node_multiscale_overlay_pattern, `label`: Graph-Dendrogram Multiscale Overlay, `type`: ARCHITECTURAL_PATTERN, `layer`: STORAGE_AND_RETRIEVAL
- **Hierarchical Community Tree (Semantic Zoom)** (`node-hierarchical-dendrogram`)
  - **Tags:** `#mutation-import` `#abstraction-layer` `#topological-hierarchy`
  - **Sintesi:** Hierarchical Community Tree (Semantic Zoom) (Layer: ABSTRACTION_LAYER, Tipo: TOPOLOGICAL_HIERARCHY)
  - **Dettagli:** `raw`: `id`: node_hierarchical_dendrogram, `label`: Hierarchical Community Tree (Semantic Zoom), `type`: TOPOLOGICAL_HIERARCHY, `layer`: ABSTRACTION_LAYER
- **Hierarchical Tree Engine (Backend & Endpoints)** (`node-hierarchical-tree-engine-impl`)
  - **Tags:** `#mutation-import` `#core-services` `#backend-engine`
  - **Sintesi:** Hierarchical Tree Engine (Backend & Endpoints) (Layer: CORE_SERVICES, Tipo: BACKEND_ENGINE)
  - **Dettagli:** `raw`: `id`: node_hierarchical_tree_engine_impl, `label`: Hierarchical Tree Engine (Backend & Endpoints), `type`: BACKEND_ENGINE, `layer`: CORE_SERVICES
- **Inibizione Interemisferica GABAergica & Lazy-Loading Biologico** (`concept-interhemispheric-inhibition-gating`)
  - **Tags:** `#neuroscience` `#interhemispheric-inhibition` `#gabaergic-gating` `#lazy-loading` `#token-reduction`
  - **Sintesi:** Meccanismo neurobiologico computazionale in cui l'emisfero non pertinente al task viene temporaneamente inibito/disattivato per eliminare interferenze e risparmiare token, riattivandosi su richiesta tramite ponti callosali.
  - **Dettagli:** `raw`: `biological_basis`: Inibizione interemisferica mediata da interneuroni GABAergici via Corpo Calloso, `computational_benefit`: Riduzione token del 50-60%, eliminazione del rumore semantico, ricerca sub-millisecondo
- **Linkly QR** (`proj-linkly-qr`)
  - **Tags:** `#ios` `#app-store` `#qr-matrix` `#vector-engine`
  - **Sintesi:** Generatore dinamico vettoriale di codici QR con preview live e styling avanzato.
  - **Dettagli:** `raw`: `platform`: Apple App Store, `engine`: Client-side SVG/PNG Vector Engine
- **MCP Tool: brain_get_tree** (`node-mcp-brain-get-tree`)
  - **Tags:** `#mutation-import` `#integration-layer` `#mcp-tool`
  - **Sintesi:** MCP Tool: brain_get_tree (Layer: INTEGRATION_LAYER, Tipo: MCP_TOOL)
  - **Dettagli:** `raw`: `id`: node_mcp_brain_get_tree, `label`: MCP Tool: brain_get_tree, `type`: MCP_TOOL, `layer`: INTEGRATION_LAYER
- **Progetto: JARVIS Personal AI Voice Assistant** (`proj-jarvis-voice-assistant`)
  - **Tags:** `#jarvis` `#voice-ai` `#mcp` `#whisper` `#kokoro-tts`
  - **Sintesi:** Assistente vocale AI continuo in tempo reale a costo zero, integrato con il connettoma SQLite WAL tramite MCP, wake word locale, STT Whisper ultra-rapido e sintesi vocale neurale.
  - **Dettagli:** `raw`: `cost_tier`: 0 EUR / 100% Free, `llm_stack`: ['Groq Llama 3.3', 'Gemini 2.5 Flash', 'Ollama Qwen 2.5'], `mcp_integration`: mcp_server.py Universal AI Brain, `stt_engine`: Faster-Whisper / Groq Whisper, `tts_engine`: Kokoro-82M / Edge-TTS, `wake_word`: openWakeWord (Hey Jarvis)
- **Royal Gambit Chess iOS App** (`project-royal-gambit-chess`)
  - **Tags:** `#ios` `#swift` `#swiftui` `#scacchi` `#minimax` `#duolingo` `#gamification`
  - **Sintesi:** Applicazione iOS nativa di scacchi per iPhone in Swift/SwiftUI con motore minimax bitboard, stile grafico Duolingo 2D Flat & 3D Tactile, bot con persona (Duo, Oscar, Athena, Magnus), sistema di streak, e Academy interattiva.
- **SQLite WAL Storage Engine** (`sqlite-wal-persistence`)
  - **Tags:** `#sqlite` `#wal` `#embedded` `#atomic` `#zero-cost` `#persistence`
  - **Sintesi:** Motore di persistenza embedded senza server né costi di licenza, con Write-Ahead Logging per letture e scritture concorrenti sicure.
  - **Dettagli:** `raw`: `journal_mode`: WAL, `foreign_keys`: ON, `backup`: Single file portable
- **Search Trees (ToT / MCTS Deliberation)** (`node-search-tree-deliberation`)
  - **Tags:** `#mutation-import` `#working-memory-planning` `#cognitive-process`
  - **Sintesi:** Search Trees (ToT / MCTS Deliberation) (Layer: WORKING_MEMORY_PLANNING, Tipo: COGNITIVE_PROCESS)
  - **Dettagli:** `raw`: `id`: node_search_tree_deliberation, `label`: Search Trees (ToT / MCTS Deliberation), `type`: COGNITIVE_PROCESS, `layer`: WORKING_MEMORY_PLANNING
- **StreaksUp (Habit Tracker iOS)** (`proj-streaksup-app`)
  - **Tags:** `#ios17` `#ios18` `#swiftui` `#swiftdata` `#widgetkit` `#streaksup` `#habittracker` `#zero-cloud`
  - **Sintesi:** Applicazione nativa iOS 17+ per tracciamento abitudini e routine con architettura SwiftData ad App Group, Live Activity e suite WidgetKit interattiva.
  - **Dettagli:** `raw`: `platform`: iOS 17.0+ / 18.0+, `language`: Swift 5.9, `ui_framework`: SwiftUI, `database`: SwiftData (SQLite WAL in App Group), `app_group`: group.com.pierfrancescoamendola.streaksup, `url_scheme`: streaksup://, `project_generator`: XcodeGen (project.yml)
- **Telegram 0€ Webhook Gateway (POST /api/telegram/webhook)** (`node-telegram-webhook-gateway`)
  - **Tags:** `#mutation-import` `#perceptual-io` `#api-gateway`
  - **Sintesi:** Telegram 0€ Webhook Gateway (POST /api/telegram/webhook) (Layer: PERCEPTUAL_IO, Tipo: API_GATEWAY)
  - **Dettagli:** `raw`: `id`: node_telegram_webhook_gateway, `label`: Telegram 0€ Webhook Gateway (POST /api/telegram/webhook), `type`: API_GATEWAY, `layer`: PERCEPTUAL_IO
- **Terminale Chiaro & Network Activity Inspector** (`feat-light-terminal`)
  - **Tags:** `#terminal` `#ui` `#monitoring` `#network-inspector` `#fetch-proxy`
  - **Sintesi:** Console/Terminale chiaro in overlay a tutto schermo per tracciare richieste HTTP (POST/GET/DEL), latenza, payload e nodi memorizzati.
  - **Dettagli:** `raw`: `theme`: Light Slate (#f8fafc), `features`: ['window-controls', 'network-interceptor', 'realtime-feed', 'json-export']
- **Test Live Upload Verify** (`test-live-upload-verify`)
  - **Tags:** `#daemon-test`
  - **Sintesi:** Test di verifica upload automatico demone
- **Test Raycast Node** (`node-test-raycast-node`)
  - **Tags:** `#raycast-quick-add` `#left` `#software-engineering`
  - **Sintesi:** Verifica integrazione Raycast con il connettoma
  - **Dettagli:** `source`: raycast_quick_add, `created_by`: Pierfrancesco Amendola
- **Tombola WiFi** (`proj-tombolawifi`)
  - **Tags:** `#websockets` `#nodejs` `#tradition` `#multiplayer`
  - **Sintesi:** Digitalizzazione multiplayer locale della classica Tombola napoletana con Smorfia e broadcast chiamate.
  - **Dettagli:** `raw`: `stack`: Node.js, WebSockets, HTML5 Canvas / Flutter, `protocol`: Event-driven real-time local network
- **UniCampus / AuleStudioApp** (`proj-unicampus`)
  - **Tags:** `#fastapi` `#flutter` `#sqlite-wal` `#university-tracker`
  - **Sintesi:** Piattaforma per gestione carriera accademica, simulatore di laurea e monitoraggio disponibilità aule studio.
  - **Dettagli:** `raw`: `stack`: Flutter, FastAPI, SQLite con PRAGMA WAL, `features`: Simulazione media pesata, previsione scenari di voto
- **Unified Brain Architecture** (`node-neuro-symbolic-brain`)
  - **Tags:** `#mutation-import` `#meta-system` `#cognitive-architecture`
  - **Sintesi:** Unified Brain Architecture (Layer: META_SYSTEM, Tipo: COGNITIVE_ARCHITECTURE)
  - **Dettagli:** `raw`: `id`: node_neuro_symbolic_brain, `label`: Unified Brain Architecture, `type`: COGNITIVE_ARCHITECTURE, `layer`: META_SYSTEM
- **Universal AI Brain (Cognitive System)** (`universal-ai-brain`)
  - **Tags:** `#ai-brain` `#fastapi` `#sqlite-wal` `#3d-graph` `#zero-cost` `#knowledge-graph`
  - **Sintesi:** Sistema di memoria persistente a grafo bi-emisferico per agenti LLM (Claude, Gemini, ChatGPT) con costo operativo zero.
  - **Dettagli:** `raw`: `version`: 1.1.0, `backend`: FastAPI, `storage`: SQLite WAL, `frontend`: 3D Force Graph WebGL, `cost`: 0€ Forever
- **Universal Knowledge Graph (Associative Substrate)** (`node-knowledge-graph-memory`)
  - **Tags:** `#mutation-import` `#long-term-associative` `#memory-system`
  - **Sintesi:** Universal Knowledge Graph (Associative Substrate) (Layer: LONG_TERM_ASSOCIATIVE, Tipo: MEMORY_SYSTEM)
  - **Dettagli:** `raw`: `id`: node_knowledge_graph_memory, `label`: Universal Knowledge Graph (Associative Substrate), `type`: MEMORY_SYSTEM, `layer`: LONG_TERM_ASSOCIATIVE

### [Macro-Label: `BUSINESS_LOGIC`]
- **AlcolSafe** (`proj-alcolsafe`)
  - **Tags:** `#mobile` `#safety` `#metabolic-calc` `#widmark`
  - **Sintesi:** Applicazione per il monitoraggio e calcolo del tasso alcolemico con stima metabolica di smaltimento.
  - **Dettagli:** `raw`: `stack`: Flutter / Swift, Widmark extended formula, `features`: Countdown smaltimento, soglie di legge, emergency contact
- **Caveman Ultra-Compressed Protocol** (`caveman-communication-protocol`)
  - **Tags:** `#caveman` `#token-efficiency` `#wenyan-ultra` `#low-latency` `#ai-rules`
  - **Sintesi:** Protocollo di comunicazione che abbatte il consumo di token del 65%+ eliminando convenevoli e verbosità senza perdere sostanza tecnica.
  - **Dettagli:** `raw`: `mode`: wenyan-ultra, `token_saving_rate`: 65-80%, `rule`: Preserve technical precision, drop fluff
- **Cross-Process Darwin IPC Protocol** (`streaksup-darwin-ipc-protocol`)
  - **Tags:** `#darwin-notifications` `#ipc` `#cross-process` `#cfnotificationcenter`
  - **Sintesi:** Protocollo di sincronizzazione inter-processo basato su CFNotificationCenter per invalidare la cache ModelContext dell'app ad ogni mutazione da widget.
  - **Dettagli:** `raw`: `notification_name`: com.pierfrancescoamendola.streaksup.habitDataChanged, `center`: CFNotificationCenterGetDarwinNotifyCenter(), `action`: modelContext.rollback() + fetchHabits()
- **Dominio: Finanza, Economia & Business** (`domain-finanza-economia`)
  - **Tags:** `#domain-hub` `#finanza` `#economia` `#business-models` `#investimenti` `#strategia`
  - **Sintesi:** Gestione Finanziaria, Investimenti, Economia, Business Models, Strategia d'Impresa e Gestione Patrimoniale.
  - **Dettagli:** `scope`: Finance, investment strategy, economic models, enterprise value
- **Guida Rapida all'AI & Publishing KDP** (`proj-kdp-ai-book`)
  - **Tags:** `#latex` `#amazon-kdp` `#publishing` `#artificial-intelligence`
  - **Sintesi:** Manuale tecnico-divulgativo sull'AI e pipeline editoriale basata su LaTeX conforme alle specifiche di stampa Amazon KDP.
  - **Dettagli:** `raw`: `toolchain`: LaTeX (tcolorbox, geometry, hyperref), `output_format`: PDF/X Amazon KDP Print Ready
- **Guida Rapida all'AI & Publishing KDP** (`proj-kdp-ai-guide`)
  - **Tags:** `#latex` `#publishing` `#amazon-kdp` `#artificial-intelligence`
  - **Sintesi:** Manuale tecnico-divulgativo sull'AI e pipeline tipografica industriale basata su LaTeX per Amazon KDP.
  - **Dettagli:** `raw`: `toolchain`: LaTeX (tcolorbox, geometry, hyperref), `output`: PDF/X print-ready conforme agli standard di taglio KDP
- **Holly & Benji AI (OpenAI Challenge)** (`proj-holly-benji-ai`)
  - **Tags:** `#openai-challenge` `#rag` `#llm-orchestration` `#team-leader`
  - **Sintesi:** Prototipazione rapida di soluzione AI RAG presentata a rettori e giudici corporate (Luglio 2026).
  - **Dettagli:** `raw`: `role`: Team Leader & English Pitcher, `milestone`: Luglio 2026
- **Logica Tassonomica: Motore di Classificazione Deterministica dei Piani Cognitivi** (`taxonomy-deterministic-floor-classification-engine`)
  - **Tags:** `#taxonomy` `#classification` `#palazzo-cognitivo` `#graph-hierarchy` `#algorithms`
  - **Sintesi:** Algoritmo di partizionamento semantico che assegna in modo deterministico ogni nodo del grafo al suo piano corretto nel Palazzo Cognitivo (P0 = Identità/Hub; P1 = Progetti/Episodi/Idee; P2 = Moduli/Schemi/Token).
  - **Dettagli:** `raw`: `p0_criteria`: Identità Pierfrancesco, Connettoma Primario, Hub con grado >= 6, `p1_criteria`: USER_INTENT, CONVERSATION_EPISODE, BRAND_VOICE, CREATIVE_IDEA, PERSONAL_VALUE, `p2_criteria`: ALGORITHM, DATA_STRUCTURE, DEPENDENCY, API_SPEC, UI_COMPONENT, DESIGN_TOKEN, schemi
- **Profilo Ingegneristico & Ricerca CS** (`identity-cs-researcher`)
  - **Tags:** `#identity` `#unina` `#icar-cnr` `#bioinformatics` `#fullstack`
  - **Sintesi:** Studente di Computer Science alla Federico II (Matr. N86005039) e ricercatore in bioinformatica applicata all'imaging biomedico presso ICAR-CNR.
  - **Dettagli:** `raw`: `institution`: Università degli Studi di Napoli Federico II, `matricola`: N86005039, `research_lab`: ICAR-CNR, `research_supervisor`: Dr.ssa Nadia Brancati, `thesis_advisor`: Prof. Daniel Riccio
- **Regola di Persistenza Cloud & Prevenzione Perdite** (`rule-cloud-persistence`)
  - **Tags:** `#persistence` `#render` `#ephemeral-disk` `#sqlite-sync` `#zero-loss`
  - **Sintesi:** Protocollo di sincronizzazione bidirezionale per ovviare alla natura effimera dei container Render e garantire la conservazione permanente dei dati.
  - **Dettagli:** `raw`: `cloud_strategy`: Git + Checkpoint Sync / Cloud SQLite, `checkpoint`: WAL Full Checkpoint
- **Runtime Multilingual .lproj Switcher** (`streaksup-i18n-runtime-engine`)
  - **Tags:** `#i18n` `#lproj` `#runtime-localization` `#six-languages`
  - **Sintesi:** Gestore centralizzato di localizzazione per il cambio istantaneo di lingua a runtime tra 6 idiomi supportati senza riavvio dell'app.
  - **Dettagli:** `raw`: `languages`: ['Italiano (it)', 'English (en)', 'Español (es)', 'Deutsch (de)', 'Português (pt)', 'Français (fr)'], `manager`: LanguageManager.shared, `mechanism`: Dynamic .lproj Bundle switching
- **Sessione di Sviluppo & Deployment Cloud (Antigravity)** (`session-continuous-evolution`)
  - **Tags:** `#antigravity` `#render` `#github` `#cloud-deployment` `#continuous-memory` `#2026-08-27`
  - **Sintesi:** Sessione interattiva di costruzione e deployment del cervello cognitivo a costo zero con Antigravity e Render.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `partner_agent`: Antigravity (Google DeepMind), `target_platform`: Render.com (Free Web Service), `repository_structure`: main.py, static/ (vis-network), requirements.txt, render.yaml, brain.db
- **Zero-Cost Mandatory Constraint** (`zero-debt-cost-rule`)
  - **Tags:** `#zero-cost` `#free-tier` `#render` `#flyio` `#koyeb` `#sustainability`
  - **Sintesi:** Regola cardine di architettura: 0€ spesa perenne. Utilizzo esclusivo di tier gratuiti illimitati o file persistenti.
  - **Dettagli:** `raw`: `budget`: 0.00 EUR, `target_clouds`: ['Render Free', 'Fly.io Free Volume', 'Koyeb Eco', 'HuggingFace Spaces']

### [Macro-Label: `COGNITIVE_RULE`]
- **Antigravity Skill: universal-brain (/brain)** (`skill-universal-brain-installed`)
  - **Tags:** `#skill` `#antigravity` `#automation` `#graphrag`
  - **Sintesi:** Skill installata in ~/.agents/skills/universal-brain per ricerca semantica e auto-ingestione continua.
  - **Dettagli:** `raw`: `path`: /Users/pierfrancesco/.agents/skills/universal-brain/SKILL.md
- **Comunicazione Chirurgica & Rigore** (`rigore-informativo`)
  - **Tags:** `#alta-densita` `#senza-convenevoli` `#struttura` `#precisione`
  - **Sintesi:** Preferenza esplicita per risposte concise, dirette e tecnicamente dense con epistemologia verificata.
  - **Dettagli:** `raw`: `communication_preferences`: ['Minimi convenevoli', 'Informazione ad alta densità', 'Struttura esplicita', 'Precisione']
- **Direttiva di Sincronizzazione Prompt 1-Click** (`feat-copy-ai-prompt`)
  - **Tags:** `#prompt-engineering` `#clipboard` `#sync` `#graphify` `#workflow`
  - **Sintesi:** Pulsante di copia rapida delle istruzioni di sistema per collegare qualsiasi LLM esterno al file brain.md e guidare l'aggiornamento della memoria.
  - **Dettagli:** `raw`: `target_url`: https://universal-ai-brain.onrender.com/brain.md, `copy_target`: clipboard
- **Direttiva di Tracciamento del Pensiero Critico AI** (`rule-ai-thought-tracing`)
  - **Tags:** `#brain-md` `#system-prompt` `#reasoning-trace` `#graphify-directive`
  - **Sintesi:** Regola 4 di brain.md: impone a qualsiasi LLM di distillare non solo i comandi dell'utente ma anche le proprie motivazioni logiche in nodi AI_REASONING.
  - **Dettagli:** `raw`: `directive_file`: brain.md, `rules_updated`: ['Rule 3 (Taxonomy)', 'Rule 4 (AI Reasoning Hub)', 'Rule 5 (Dual Ingest)']
- **Dominio: Produttività, Sistemi Operativi & Automazione** (`domain-produttivita-sistemi`)
  - **Tags:** `#domain-hub` `#produttivita` `#automazione` `#workflows` `#time-management` `#life-ops`
  - **Sintesi:** Workflow operativi, Strumenti di automazione, Metodologie di Studio e Lavoro, Gestione del Tempo e Life Operations.
  - **Dettagli:** `scope`: Productivity workflows, time management, automation tools, habits
- **Epistemologia & Divieto Allucinazioni** (`epistemologia-rigorosa`)
  - **Tags:** `#epistemologia` `#fatti-verificati` `#no-hallucination`
  - **Sintesi:** Distinzione rigorosa tra fatti dichiarati ed inferenze; divieto di fabbricare dettagli emotivi o tecnici privi di fonte.
  - **Dettagli:** `raw`: `principle`: Verifiable ground-truth only
- **Hierarchical Community Tree as Primary Abstraction** (`node-tree-architecture-verdict`)
  - **Tags:** `#mutation-import` `#core-taxonomy` `#architectural-decision`
  - **Sintesi:** Hierarchical Community Tree as Primary Abstraction (Layer: CORE_TAXONOMY, Tipo: ARCHITECTURAL_DECISION)
  - **Dettagli:** `raw`: `id`: node_tree_architecture_verdict, `label`: Hierarchical Community Tree as Primary Abstraction, `type`: ARCHITECTURAL_DECISION, `layer`: CORE_TAXONOMY
- **Regola Cognitiva: Gestione dei Filtri Anti-Injection nei Modelli Web** (`concept-llm-indirect-injection-safeguard`)
  - **Tags:** `#cognitive-rule` `#prompt-injection` `#llm-safety` `#claude-ai-guardrails` `#memory-ingestion`
  - **Sintesi:** Protocollo di interazione con modelli web: evitare comandi imperativi di rete esterna (es. ordini di POST verso URL terzi) nei file allegati, preferendo il formato standard di blocco JSON in calce.
  - **Dettagli:** `raw`: `cause_of_refusal`: I filtri di Anthropic/OpenAI rilevano istruzioni di esfiltrazione dati se un prompt/file ordina chiamate POST o fetch verso siti terzi., `recommended_protocol`: Allegare brain.md e chiedere la generazione del blocco di codice JSON da incollare con 1-click nella Web Dashboard.
- **Regola dell'Esecuzione Integrale (Zero Placeholder)** (`rule-zero-placeholder`)
  - **Tags:** `#strict-execution` `#code-integrity` `#no-shortcuts`
  - **Sintesi:** Divieto tassativo di codice troncato, finto o parziale; ogni soluzione deve essere autosufficiente ed eseguibile.
  - **Dettagli:** `raw`: `banned`: ['// resto del codice', '/* implementare qui */', 'TODO stub'], `standard`: Production-ready code only
- **Regola di Preservazione Episodica delle Conversazioni** (`rule-episodic-chat-preservation`)
  - **Tags:** `#rule` `#episodic-memory` `#brain-md` `#chat-tracking`
  - **Sintesi:** Direttiva di sistema per raggruppare qualsiasi sessione futura sotto il proprio nodo di episodio tematico con le relative intenzioni e ragionamenti.
  - **Dettagli:** `raw`: `rule_number`: 4, `taxonomy_pair`: ['USER_INTENT', 'AI_REASONING', 'CONVERSATION_EPISODE']
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-2471`)
  - **Tags:** `#left` `#siri-shortcuts` `#voice-capture`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-2485`)
  - **Tags:** `#siri-shortcuts` `#voice-capture` `#left`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-2529`)
  - **Tags:** `#voice-capture` `#siri-shortcuts` `#left`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-2690`)
  - **Tags:** `#siri-shortcuts` `#left` `#voice-capture`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-8745`)
  - **Tags:** `#siri-shortcuts` `#left` `#voice-capture`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-9065`)
  - **Tags:** `#siri-shortcuts` `#left` `#voice-capture`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Test shortcuts debug** (`voice-test-shortcuts-debug-7964`)
  - **Tags:** `#voice-capture` `#left` `#siri-shortcuts`
  - **Sintesi:** Test shortcuts debug
  - **Dettagli:** `source`: siri_voice, `full_transcript`: Test shortcuts debug, `captured_by`: Pierfrancesco Amendola
- **Verifica Cloud Git Auto-Push Render** (`test-cloud-git-autopush-verification`)
  - **Tags:** `#test` `#render-autopush` `#cloud-persistence`
  - **Sintesi:** Nodo di validazione del meccanismo di auto-push Git da Render su GitHub origin main.
  - **Dettagli:** `test_timestamp`: 1788175889.2639208, `status`: verifying

### [Macro-Label: `DATA_STRUCTURE`]
- **Architettura ad Alberi Gerarchici Pesati (Knowledge Tree)** (`idea-hierarchical-weighted-trees`)
  - **Tags:** `#data-structure` `#tree` `#mst` `#dendrogram` `#semantic-zoom`
  - **Sintesi:** Struttura ad albero ponderata sovrapposta al grafo per estrazione gerarchica dei temi: Radice -> Emisferi -> Cluster -> Nodi atomici.
  - **Dettagli:** `raw`: `application`: Zoom semantico da macro-concetti a micro-dettagli
- **Fondamenti Teorici & Coursework UNINA** (`coursework-cs-federico2`)
  - **Tags:** `#unina` `#mogavero` `#setvec` `#relational-algebra` `#s-programs` `#theory-of-computation`
  - **Sintesi:** Solida preparazione teorica: strutture dati SetVec/SetLst (Prof. Mogavero), algebra relazionale estesa e S-Programs.
  - **Dettagli:** `raw`: `data_structures`: SetVec, SetLst (Prof. Mogavero), `relational_algebra`: Aggregation syntax <attr>G<func>(R), `computability`: S-Programs (Davis, Weyuker - Computability & Languages)
- **NapoliLive** (`proj-napolilive`)
  - **Tags:** `#territory` `#napoli` `#events` `#scraping`
  - **Sintesi:** Hub informativo per la valorizzazione del territorio partenopeo con aggregazione eventi in tempo reale.
  - **Dettagli:** `raw`: `stack`: Next.js / Flutter, Scraping engine, `focus`: Eventi culturali, mobilità e spettacoli a Napoli
- **Patologia: Onicocriptosi (Unghia Incarnita)** (`medical-onicocriptosi-unghia-incarnita`)
  - **Tags:** `#medicina` `#dermatologia` `#podologia` `#onicocriptosi` `#trattamento`
  - **Sintesi:** Condizione patologica in cui il bordo ungueale penetra nel solco ungueale periungueale causando infiammazione, granuloma o infezione.
  - **Dettagli:** `raw`: `trattamento`: Conservativo (pediluvio, disinfezione) o chirurgico (matricectomia parziale), `eziologia`: Taglio errato, calzature strette, conformazione anatomica
- **Radix / Prefix Trie (O(k) Entity Routing)** (`node-prefix-radix-trie`)
  - **Tags:** `#mutation-import` `#perceptual-routing` `#lexical-index`
  - **Sintesi:** Radix / Prefix Trie (O(k) Entity Routing) (Layer: PERCEPTUAL_ROUTING, Tipo: LEXICAL_INDEX)
  - **Dettagli:** `raw`: `id`: node_prefix_radix_trie, `label`: Radix / Prefix Trie (O(k) Entity Routing), `type`: LEXICAL_INDEX, `layer`: PERCEPTUAL_ROUTING
- **SQLite WAL High-Concurrency Pattern** (`arch-sqlite-wal`)
  - **Tags:** `#database` `#sqlite` `#wal` `#zero-cost` `#performance`
  - **Sintesi:** Configurazione di persistenza locale ad alta efficienza per carichi concorrenti senza costi di hosting.
  - **Dettagli:** `raw`: `journal_mode`: WAL, `synchronous`: NORMAL, `busy_timeout`: 5000, `cache_size`: -20000
- **SwiftData Shared Container & Models** (`streaksup-swiftdata-arch`)
  - **Tags:** `#swiftdata` `#sqlite-wal` `#models` `#app-group` `#concurrency`
  - **Sintesi:** Storage condiviso tra App principale ed estensione Widget tramite ModelContainer su SQLite WAL con modelli Habit, HabitLog e HabitCategory.
  - **Dettagli:** `raw`: `models`: ['Habit', 'HabitLog', 'HabitCategory'], `helper`: SwiftDataHelper, `concurrency_protection`: ModelContext rollback su notifiche Darwin, `cascade_deletion`: Inverse relationship Habit -> logs

### [Macro-Label: `DEPENDENCY`]
- **FastAPI & Python ASGI Stack** (`fastapi-python-stack`)
  - **Tags:** `#python` `#fastapi` `#uvicorn` `#pydantic-v2` `#asgi` `#rest`
  - **Sintesi:** Framework web asincrono ad altissimo throughput per esporre API di memoria e webhook di ingestione per agenti AI.
  - **Dettagli:** `raw`: `python_version`: 3.10+, `asgi_server`: Uvicorn, `validation`: Pydantic V2
- **Flutter & Dart Mobile Architecture** (`flutter-dart-ecosystem`)
  - **Tags:** `#flutter` `#dart` `#bloc` `#state-management` `#cross-platform`
  - **Sintesi:** Stack di sviluppo mobile multipiattaforma ad alte prestazioni con architettura pulita a blocchi logici (BLoC/Provider).
  - **Dettagli:** `raw`: `runtime`: Flutter 3.x, `engine`: Skia/Impeller, `state`: BLoC / Provider, `network`: Dio / REST / WebSocket
- **GitHub Repository Universal-AI-Brain** (`repo-github-universal-ai-brain`)
  - **Tags:** `#github` `#repository` `#open-source` `#render-ready`
  - **Sintesi:** Repository GitHub ufficiale contenente il backend FastAPI, il dashboard vis-network e la memoria SQLite pre-popolata.
  - **Dettagli:** `raw`: `url`: https://github.com/PierfrancescoAmendola/Universal-AI-Brain, `owner`: PierfrancescoAmendola, `branch`: main, `visibility`: Public

### [Macro-Label: `MENTAL_MODEL`]
- **Bayesian Updating (Aggiornamento Bayesiano)** (`firmware-bayesian-updating`)
  - **Tags:** `#firmware` `#mental-model` `#bayesian_updating`
  - **Sintesi:** Aggiorna la probabilità della tua tesi iniziale in proporzione alle nuove evidenze.
  - **Dettagli:** `author`: Thomas Bayes, `reasoning_steps`: ['1. Dichiara la tua ipotesi/credenza a priori (Prior Probability P(H)).', '2. Valuta la forza e la veridicità delle nuove prove osservate (Likelihood P(E|H)).', '3. Ricalibra la probabilità a posteriori (Posterior P(H|E)) senza arroccarsi su dogmi pregressi.', "4. Modifica la rotta d'azione se la probabilità aggiornata scende sotto la soglia di sicurezza."]
- **Circle of Competence (Cerchio di Competenza)** (`firmware-circle-of-competence`)
  - **Tags:** `#firmware` `#mental-model` `#circle_of_competence`
  - **Sintesi:** Definisci con precisione chirurgica ciò che sai e ammetti ciò che ignori.
  - **Dettagli:** `author`: Warren Buffett & Charlie Munger, `reasoning_steps`: ['1. Traccia il confine esatto: quali parti di questo problema padroneggi con certezza empirica?', "2. Dichiara esplicitamente le zone d'ombra, le dipendenze da terze parti e le incognite.", '3. Rifiuta di prendere decisioni definitive al di fuori del perimetro senza aver prima acquisito evidenza verificabile.', '4. Affidati a esperti, fallback difensivi o isolamento modulare per la parte sconosciuta.']
- **Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin) - Estratto** (`kindle-c962fde43767`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#left` `#software-engineering`
  - **Sintesi:** Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
  - **Dettagli:** `book_title`: Clean Code: A Handbook of Agile Software Craftsmanship, `author`: Robert C. Martin, `full_quote`: Any fool can write code that a computer can understand. Good programmers write code that humans can understand., `kindle_meta`: - Your Highlight on Location 200-205 | Added on Tuesday, February 20, 2024 03:15:00 PM, `imported_by`: kindle_sync_engine
- **Filosofia Ingegneristica a Costo Zero** (`rule-zero-cost`)
  - **Tags:** `#efficiency` `#self-hosted` `#sqlite` `#lean-architecture`
  - **Sintesi:** Progettare sistemi snelli ed efficienti eliminando i costi infrastrutturali fissi tramite tecnologie locali o open-source.
  - **Dettagli:** `raw`: `practices`: ['SQLite WAL invece di server DB pesanti', 'Client-side processing', 'Static/Serverless hosting']
- **First Principles (Primi Principi)** (`firmware-first-principles`)
  - **Tags:** `#firmware` `#mental-model` `#first_principles`
  - **Sintesi:** Riduci il problema ai suoi assiomi fisici/logici essenziali senza affidarti all'analogia.
  - **Dettagli:** `author`: Aristotele & Elon Musk, `reasoning_steps`: ["1. Isola le credenze convenzionali o le pratiche 'standard' accettate per abitudine.", '2. Riduci il problema alle uniche verità indiscutibili e non negoziabili (leggi fisiche, logica, risorse atomiche).', '3. Ricostruisci una soluzione da zero (bottom-up) partendo solo da quegli assiomi.', '4. Elimina ogni strato superfluo derivato da conformismo o abitudine storica.']
- **Inversion (Inversione)** (`firmware-inversion`)
  - **Tags:** `#firmware` `#mental-model` `#inversion`
  - **Sintesi:** Non cercare solo come vincere; definisci come perdere e poi evitalo rigorosamente.
  - **Dettagli:** `author`: Charlie Munger & Carl Jacobi, `reasoning_steps`: ['1. Definisci il fallimento catastrofico o lo scenario peggiore per questo problema.', '2. Elenca le 3-5 azioni o assunzioni che causerebbero direttamente quel disastro.', '3. Trasforma ciascuna causa di fallimento in una guardia difensiva o vincolo vincolante.', "4. Riorganizza il piano d'azione per eliminare prima i punti di rottura irreversibili."]
- **Modello Centauro (Uomo + AI)** (`mental-centaur-model`)
  - **Tags:** `#ai-philosophy` `#human-agency` `#cognitive-extension`
  - **Sintesi:** L'AI agisce come moltiplicatore computazionale, mentre l'essere umano detiene il controllo etico, strategico ed estetico.
  - **Dettagli:** `raw`: `human_role`: Visione, intenzionalità etica, discernimento critico, anima artistica, `machine_role`: Velocità esecutiva, esplorazione combinatoria, precisione formale
- **Opportunity Cost (Costo Opportunità)** (`firmware-opportunity-cost`)
  - **Tags:** `#firmware` `#mental-model` `#opportunity_cost`
  - **Sintesi:** Il vero costo di una scelta è il valore della migliore alternativa a cui rinunci.
  - **Dettagli:** `author`: Economia Classica, `reasoning_steps`: ["1. Identifica l'azione proposta e le risorse richieste (tempo, concentrazione, CPU, budget).", '2. Elenca le 2 migliori alternative escluse se dedichi le risorse a questa scelta.', '3. Calcola il ROI differenziale tra la scelta e le alternative.', '4. Procedi solo se il valore netto atteso supera la migliore alternativa sacrificata.']
- **Pareto Principle (80/20)** (`firmware-pareto`)
  - **Tags:** `#firmware` `#mental-model` `#pareto`
  - **Sintesi:** Il 20% delle cause genera l'80% degli effetti. Trova quel 20% vitale ed elimina l'80% banale.
  - **Dettagli:** `author`: Vilfredo Pareto, `reasoning_steps`: ["1. Isola l'elenco di tutte le feature, componenti o task sul tavolo.", "2. Identifica il 20% che sblocca direttamente l'80% del valore percepito o delle prestazioni.", '3. Esegui subito quel 20% critico con massima dedizione.', '4. Taglia, rimanda o automatizza il restante 80% secondario.']
- **Persistenza Totale del Contesto e dei Pensieri Multi-AI** (`goal-multi-ai-shared-context-persistence`)
  - **Tags:** `#shared-context` `#conversational-continuity` `#multi-ai` `#cross-agent-memory` `#universal-recall`
  - **Sintesi:** Principio fondante: preservare integralmente contesto, richieste e deduzioni di tutte le chat con qualsiasi AI affinché ogni modello condivida la memoria storica universale.
  - **Dettagli:** `raw`: `user_prompt`: lo scopo è che venga salvato il contesto e memorizzato il contesto delle chat con le ai in modo tale che si sa sempre cosa è stato detto, pensato, eccc..., `core_objective`: Garantire che qualunque AI (Claude, Gemini, ChatGPT, DeepSeek, ecc.) sappia sempre con esattezza cosa è stato detto, pensato e deciso nelle sessioni precedenti., `context_dimensions`: ['Richieste Utente (USER_INTENT)', 'Deduzioni Logiche (AI_REASONING)', 'Episodi Tematici (CONVERSATION_EPISODE)', 'Attribuzione Modello (details.model)']
- **Second-Order Thinking (Pensiero del Secondo Ordine)** (`firmware-second-order`)
  - **Tags:** `#firmware` `#mental-model` `#second_order`
  - **Sintesi:** E poi cosa succede? Valuta le conseguenze delle conseguenze a medio-lungo termine.
  - **Dettagli:** `author`: Howard Marks, `reasoning_steps`: ["1. Individua l'effetto immediato di 1° ordine (es. aumento velocità o riduzione costi).", "2. Domanda: 'E poi cosa accade a cascata?' (Effetti di 2° ordine su complessità, debito tecnico, carico cognitivo).", '3. Proietta gli effetti di 3° ordine (incentivi perversi, reazioni del sistema, scalabilità nel tempo).', "4. Valuta se il guadagno a breve termine giustifica l'entropia a lungo termine."]
- **Ubiquitous Memory Ingestion** (`node-ubiquitous-ingestion`)
  - **Tags:** `#mutation-import` `#dynamic-plasticity` `#cognitive-capability`
  - **Sintesi:** Ubiquitous Memory Ingestion (Layer: DYNAMIC_PLASTICITY, Tipo: COGNITIVE_CAPABILITY)
  - **Dettagli:** `raw`: `id`: node_ubiquitous_ingestion, `label`: Ubiquitous Memory Ingestion, `type`: COGNITIVE_CAPABILITY, `layer`: DYNAMIC_PLASTICITY

### [Macro-Label: `PROJECT`]
- **1 Minimal** (`proj-1-minimal`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 1 Minimal. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/1-minimal, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/1-minimal, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2023-03-05T14:04:14+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **10 Funptr** (`proj-10-funptr`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 10 Funptr. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/10-funptr, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/10-funptr, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-23T14:35:12+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **12 Templates** (`proj-12-templates`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 12 Templates. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/12-templates, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/12-templates, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-25T13:07:44+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **2** (`proj-2`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: 2. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Foto Cri/2, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Foto Cri/2, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-06-16T20:51:41+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **2 Structured** (`proj-2-structured`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 2 Structured. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/2-structured, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/2-structured, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 5, `last_modified`: 2024-03-13T11:08:40+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **3 Basictypes** (`proj-3-basictypes`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 3 Basictypes. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/3-basictypes, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/3-basictypes, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-13T11:10:40+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **4 Allocation** (`proj-4-allocation`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 4 Allocation. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/4-allocation, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/4-allocation, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-18T15:04:38+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **5 Usertypes** (`proj-5-usertypes`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 5 Usertypes. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/5-usertypes, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/5-usertypes, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-18T15:03:46+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **6 Iostream** (`proj-6-iostream`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 6 Iostream. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/6-iostream, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/6-iostream, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-20T07:38:30+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **7 String** (`proj-7-string`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 7 String. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/7-string, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/7-string, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-20T07:38:30+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **8 Psecasgen** (`proj-8-psecasgen`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: 8 Psecasgen. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/examples/8-psecasgen, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/examples/8-psecasgen, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2024-03-20T07:38:30+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Accent Color.Colorset** (`proj-accentcolor-colorset`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Accent Color.Colorset. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse2/MacPulse2/Assets.xcassets/AccentColor.colorset, `file_uri`: file:///Users/pierfrancesco/MacPulse2/MacPulse2/Assets.xcassets/AccentColor.colorset, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-10-23T07:32:00.540118+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Advanced Db(Mod.Db Tech)** (`proj-advanceddb-mod-db-tech`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Advanced Db(Mod.Db Tech). Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/AdvancedDB(MOD.DB tech), `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/AdvancedDB(MOD.DB tech), `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-06-23T16:28:32.114558+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Algebra** (`proj-algebra`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Algebra. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/ALGEBRA, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/ALGEBRA, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 4, `last_modified`: 2025-06-24T09:30:23.001475+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **App Calcolatori** (`proj-appcalcolatori`)
  - **Tags:** `#ios` `#mac-project` `#swift` `#swiftui` `#xcodegen`
  - **Sintesi:** Native iPhone utility suite built with SwiftUI, Swift 6, and iOS 18+.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppCalcolatori, `file_uri`: file:///Users/pierfrancesco/Desktop/AppCalcolatori, `languages`: ['Swift'], `frameworks`: ['SwiftUI', 'XcodeGen'], `has_git`: False, `relevant_files_count`: 23, `last_modified`: 2026-07-29T07:41:17.289956+00:00, `key_dependencies`: [], `readme_excerpt`: # PocketCalc+

Native iPhone utility suite built with SwiftUI, Swift 6, and iOS 18+.

## Generate and build

```sh
xcodegen generate
xcodebuild -project PocketCalcPlus.xcodeproj -scheme PocketCalcPlus -configuration Debug build
```

XcodeGen keeps project generation deterministic; generated `.xcodeproj` is committed.

## Before App Store archive

- Replace AdMob test IDs in `Config/Release.xcconfig`.
- Replace privacy policy and support URLs in `SettingsView.swift`.
- Select production signing team and verify bundle identifier.
- Complete App Store privacy labels for Google Mobile Ads.
- **App Icon.Appiconset** (`proj-appicon-appiconset`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: App Icon.Appiconset. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse2/MacPulse2/Assets.xcassets/AppIcon.appiconset, `file_uri`: file:///Users/pierfrancesco/MacPulse2/MacPulse2/Assets.xcassets/AppIcon.appiconset, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-10-23T07:32:02.159356+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Asd & Lasd** (`proj-asd-lasd`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Asd & Lasd. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/ASD & LASD, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/ASD & LASD, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-04-24T09:40:35.165134+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Auth Screens** (`proj-auth_screens`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: Auth Screens. Stack: JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/Auth_Screens, `file_uri`: file:///Users/pierfrancesco/Downloads/Auth_Screens, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2026-05-04T03:18:18+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Basi Di Dati Esercizi** (`proj-basi-di-dati-esercizi`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Basi Di Dati Esercizi. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/BASI DI DATI ESERCIZI, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/BASI DI DATI ESERCIZI, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 8, `last_modified`: 2025-04-26T08:56:30.637358+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Bdd** (`proj-bdd`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Bdd. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/BDD, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/BDD, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2025-03-07T10:45:43+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Binari** (`proj-binari`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Binari. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/Esercizi in C/binari, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/Esercizi in C/binari, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-11-17T14:47:43.274341+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Book** (`proj-book`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto editoriale per edizione illustrata KDP.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-22/stavo-pensando-di-scrivere-un-libro/work/book, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-22/stavo-pensando-di-scrivere-un-libro/work/book, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 47, `last_modified`: 2026-07-26T22:48:51.873911+00:00, `key_dependencies`: [], `readme_excerpt`: # Cos'è davvero l'informatica

Progetto editoriale per edizione illustrata KDP.

## Struttura

- `editorial-bible.md`: identità, pubblico, tono, criteri di qualità.
- `chapter-map.md`: indice ragionato, obiettivi e budget per capitolo.
- `main.tex`: radice del volume.
- `bookstyle.sty`: sistema tipografico e componenti editoriali.
- `frontmatter/`: occhiello, frontespizio, copyright, prologo.
- `chapters/`: capitoli numerati.
- `backmatter/`: glossario, note, bibliografia, crediti.
- `assets/svg/`: diagrammi vettoriali originali.
- `research/`: fonti, registro diritti e fact-check.
- `build/`:
- **Calm Raman** (`proj-calm-raman`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Calm Raman. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/antigravity/calm-raman, `file_uri`: file:///Users/pierfrancesco/Documents/antigravity/calm-raman, `languages`: [], `frameworks`: [], `has_git`: True, `relevant_files_count`: 0, `last_modified`: 2026-08-31T15:23:50.602671+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Cervello Artificiale** (`proj-cervelloartificiale`)
  - **Tags:** `#fastapi` `#javascript` `#mac-project` `#python` `#uvicorn` `#web`
  - **Sintesi:** > **Persistent Bi-Hemispheric Knowledge Graph, Hierarchical Tree Engine, Dual-Ring Cloud Persistence & MCP Server for Autonomous Multi-Agent AI Systems**
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/CervelloArtificiale, `file_uri`: file:///Users/pierfrancesco/Desktop/CervelloArtificiale, `languages`: ['JavaScript', 'Python'], `frameworks`: ['FastAPI', 'Uvicorn'], `has_git`: True, `relevant_files_count`: 441, `last_modified`: 2026-08-31T15:23:20.481809+00:00, `key_dependencies`: ['fastapi', 'uvicorn[standard]', 'pydantic'], `readme_excerpt`: # 🧠 Universal AI Brain (Connettoma Cognitivo Universale)
> **Persistent Bi-Hemispheric Knowledge Graph, Hierarchical Tree Engine, Dual-Ring Cloud Persistence & MCP Server for Autonomous Multi-Agent AI Systems**  
> *100% Zero-Cost Architecture (0,00€ Forever) · FastAPI · SQLite WAL + FTS5 · Bidirectional BFS · Model Context Protocol (MCP) · Telegram Gateway · 24/7 Keep-Alive Daemon*

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.sh
- **Cisco Certification** (`proj-ciscocertification`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Cisco Certification. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Certificati/CiscoCertification, `file_uri`: file:///Users/pierfrancesco/Desktop/Certificati/CiscoCertification, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 6, `last_modified`: 2026-05-09T10:25:50.017104+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Codice Architettura Tesi** (`proj-codice_architettura_tesi`)
  - **Tags:** `#mac-project` `#python`
  - **Sintesi:** Progetto Mac: Codice Architettura Tesi. Stack: Python.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/codice_Architettura_Tesi, `file_uri`: file:///Users/pierfrancesco/Desktop/codice_Architettura_Tesi, `languages`: ['Python'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2026-04-12T15:47:26.789827+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Compito Luglio** (`proj-compito-luglio`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Compito Luglio. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami 2020/compito luglio, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami 2020/compito luglio, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 9, `last_modified`: 2025-06-16T20:51:42+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Compito Settembre** (`proj-compito-settembre`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Compito Settembre. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami 2020/compito settembre, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami 2020/compito settembre, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 10, `last_modified`: 2025-06-16T20:51:42+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Composetest** (`proj-composetest`)
  - **Tags:** `#mac-project` `#python`
  - **Sintesi:** Progetto Mac: Composetest. Stack: Python.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/composetest, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/composetest, `languages`: ['Python'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2025-11-04T13:06:41.098364+00:00, `key_dependencies`: ['flask', 'redis'], `readme_excerpt`: 
- **Cose Laurea** (`proj-cose_laurea`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Cose Laurea. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Cose_Laurea, `file_uri`: file:///Users/pierfrancesco/Desktop/Cose_Laurea, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 6, `last_modified`: 2026-08-07T20:03:53.078872+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Eager Pasteur** (`proj-eager-pasteur`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Eager Pasteur. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/antigravity/eager-pasteur, `file_uri`: file:///Users/pierfrancesco/Documents/antigravity/eager-pasteur, `languages`: [], `frameworks`: [], `has_git`: True, `relevant_files_count`: 0, `last_modified`: 2026-08-31T15:23:50.602799+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Economia** (`proj-economia`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Economia. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/ECONOMIA, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/ECONOMIA, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-07-05T13:51:46.478111+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Example** (`proj-example`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Example. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/example, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/example, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-11-04T12:19:18.719627+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Examples** (`proj-examples`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: Examples. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Examples/Examples, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Examples/Examples, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-04-29T17:55:13.339685+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Fanta Formula1** (`proj-fantaformula1`)
  - **Tags:** `#javascript` `#mac-project` `#react`
  - **Sintesi:** Un'applicazione di Fantacalcio dedicata alla Formula 1, sviluppata con React Native ed Expo.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Applicazioni/F1App/FantaFormula1, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Applicazioni/F1App/FantaFormula1, `languages`: ['JavaScript'], `frameworks`: ['React'], `has_git`: False, `relevant_files_count`: 30, `last_modified`: 2026-01-19T10:21:48.118559+00:00, `key_dependencies`: ['@react-native-async-storage/async-storage', '@react-navigation/bottom-tabs', '@react-navigation/drawer', '@react-navigation/native', '@react-navigation/stack', 'expo', 'expo-auth-session', 'expo-crypto', 'expo-status-bar', 'expo-web-browser', 'react', 'react-native', 'react-native-gesture-handler', 'react-native-reanimated', 'react-native-safe-area-context'], `readme_excerpt`: # FantaFormula1 - App Mobile

Un'applicazione di Fantacalcio dedicata alla Formula 1, sviluppata con React Native ed Expo.

## 🏎️ Caratteristiche Principali

### Autenticazione
- Registrazione e login con email
- Accesso con Google
- Accesso con Apple ID
- Gestione profilo utente

### Gestione Campionati
- Creazione di campionati privati
- Sistema di inviti con codice univoco
- Partecipazione a campionati esistenti
- Fino a 6 giocatori per campionato
- Sistema di crediti personalizzabile per l'asta

### Gestione Squadra
- Acquisto di 3 piloti e 3 scuderie durante l'asta
- Schieramento di 2 pil
- **Food Lab2025** (`proj-foodlab2025`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Food Lab2025. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/git/FoodLab2025, `file_uri`: file:///Users/pierfrancesco/git/FoodLab2025, `languages`: [], `frameworks`: [], `has_git`: True, `relevant_files_count`: 21, `last_modified`: 2025-09-20T09:39:06.201131+00:00, `key_dependencies`: [], `readme_excerpt`: # FoodLab2025
- **Gennaio 2021** (`proj-gennaio-2021`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Gennaio 2021. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Gennaio 2021, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Gennaio 2021, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 12, `last_modified`: 2021-10-18T15:28:56+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Gioco** (`proj-gioco`)
  - **Tags:** `#c` `#c-lang` `#mac-project`
  - **Sintesi:** Progetto Mac: Gioco. Stack: C.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/gioco/gioco, `file_uri`: file:///Users/pierfrancesco/Desktop/gioco/gioco, `languages`: ['C'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-03-11T10:33:28.782049+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Gioco Scacchi** (`proj-giocoscacchi`)
  - **Tags:** `#mac-project` `#python` `#swift`
  - **Sintesi:** Progetto Mac: Gioco Scacchi. Stack: Python, Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/GiocoScacchi, `file_uri`: file:///Users/pierfrancesco/Desktop/GiocoScacchi, `languages`: ['Python', 'Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 56, `last_modified`: 2026-08-28T12:46:37.759620+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Giugno 2021** (`proj-giugno-2021`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Giugno 2021. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Giugno 2021, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Giugno 2021, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 23, `last_modified`: 2021-10-16T16:09:49+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Gods Eye View Main** (`proj-gods-eye-view-main`)
  - **Tags:** `#javascript` `#mac-project` `#vite` `#web`
  - **Sintesi:** Photorealistic 3D globe. Live aircraft, ships, satellites, earthquakes, traffic, and public cameras, with clearly labeled modeled views where a live feed is unavailable. Hands-free voice control power
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/gods-eye-view-main, `file_uri`: file:///Users/pierfrancesco/Downloads/gods-eye-view-main, `languages`: ['JavaScript'], `frameworks`: ['Vite'], `has_git`: False, `relevant_files_count`: 180, `last_modified`: 2026-08-27T15:46:08+00:00, `key_dependencies`: ['@mapbox/vector-tile', 'cesium', 'egm96-universal', 'mgrs', 'pbf', 'satellite.js', 'puppeteer', 'sharp', 'vite', 'vite-plugin-cesium', 'ws'], `readme_excerpt`: <div align="center">

# 🌐 God's Eye View

### A spy-satellite simulator in your browser — then you realize the sources are public and the data is real.

Photorealistic 3D globe. Live aircraft, ships, satellites, earthquakes, traffic, and public cameras, with clearly labeled modeled views where a live feed is unavailable. Hands-free voice control powered by a realtime AI agent.

*No place left behind.*

![Orbital HUD, a tracked live globe, FLIR terrain — then OPEN SOURCED](docs/media/hero-open-source-reveal.gif)

<a href="https://www.youtube.com/@bilawalsidhu">
  <img src="docs/media/youtube-po
- **Google Certificate** (`proj-googlecertificate`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Google Certificate. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Certificati/GoogleCertificate, `file_uri`: file:///Users/pierfrancesco/Desktop/Certificati/GoogleCertificate, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 14, `last_modified`: 2026-05-09T13:40:22.547082+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Happy Plant Keeper** (`proj-happy-plant-keeper`)
  - **Tags:** `#javascript` `#mac-project` `#react` `#swift` `#tailwind` `#tailwindcss` `#typescript` `#vite` `#web`
  - **Sintesi:** **URL**: https://lovable.dev/projects/cc27e2fa-a880-48d4-8cea-2b8d52a99bf1
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Applicazioni/happy-plant-keeper, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Applicazioni/happy-plant-keeper, `languages`: ['JavaScript', 'Swift', 'TypeScript'], `frameworks`: ['React', 'TailwindCSS', 'Vite'], `has_git`: True, `relevant_files_count`: 92, `last_modified`: 2025-10-28T23:57:21.563342+00:00, `key_dependencies`: ['@capacitor/cli', '@capacitor/core', '@capacitor/ios', '@hookform/resolvers', '@radix-ui/react-accordion', '@radix-ui/react-alert-dialog', '@radix-ui/react-aspect-ratio', '@radix-ui/react-avatar', '@radix-ui/react-checkbox', '@radix-ui/react-collapsible', '@radix-ui/react-context-menu', '@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu', '@radix-ui/react-hover-card', '@radix-ui/react-label'], `readme_excerpt`: # Welcome to your Lovable project

## Project info

**URL**: https://lovable.dev/projects/cc27e2fa-a880-48d4-8cea-2b8d52a99bf1

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/cc27e2fa-a880-48d4-8cea-2b8d52a99bf1) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The onl
- **Ingsw** (`proj-ingsw`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Ingsw. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/SWE/INGSW, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/SWE/INGSW, `languages`: [], `frameworks`: [], `has_git`: True, `relevant_files_count`: 85, `last_modified`: 2025-12-02T10:52:54.456996+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Jules Session 5370203018288358434** (`proj-jules_session_5370203018288358434`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: Jules Session 5370203018288358434. Stack: JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/jules_session_5370203018288358434, `file_uri`: file:///Users/pierfrancesco/Downloads/jules_session_5370203018288358434, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 5, `last_modified`: 2026-05-10T13:17:36+00:00, `key_dependencies`: ['jsdom'], `readme_excerpt`: 
- **Lp   Prova Esame Giugno** (`proj-lp---prova-esame-giugno`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Lp   Prova Esame Giugno. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami giugno 2021/LP - Prova Esame Giugno, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Esami giugno 2021/LP - Prova Esame Giugno, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 10, `last_modified`: 2025-06-16T20:51:41+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Lp1** (`proj-lp1`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Lp1. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/LP1, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/LP1, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-03-06T14:32:25.377620+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Lso** (`proj-lso`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Lso. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/LSO, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/LSO, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-09-15T14:02:54.225149+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Marzo 2021** (`proj-marzo-2021`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Marzo 2021. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Marzo 2021, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Marzo 2021, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 8, `last_modified`: 2021-10-17T16:04:37+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Ml(Neural Networks & Dl)** (`proj-ml-neural-networks-dl`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Ml(Neural Networks & Dl). Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/ML(Neural Networks & DL), `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/ML(Neural Networks & DL), `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2026-06-23T16:29:40.749334+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **New Chapters** (`proj-new_chapters`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: New Chapters. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/new_chapters, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/new_chapters, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 11, `last_modified`: 2026-07-23T16:21:17.011231+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **New Project** (`proj-new-project`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: New Project. Stack: JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/New project, `file_uri`: file:///Users/pierfrancesco/Documents/New project, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 9, `last_modified`: 2026-02-09T10:33:44.095897+00:00, `key_dependencies`: ['playwright'], `readme_excerpt`: 
- **Nvidia Certification** (`proj-nvidiacertification`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Nvidia Certification. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Certificati/NvidiaCertification, `file_uri`: file:///Users/pierfrancesco/Desktop/Certificati/NvidiaCertification, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 5, `last_modified`: 2026-05-11T20:51:25.981710+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Oo** (`proj-oo`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Oo. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/OO, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/OO, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-11-29T14:28:00.020468+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Osmci** (`proj-osmci`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Osmci. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/OSMCI, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/OSMCI, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-06-23T16:28:03.210707+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Outputs** (`proj-outputs`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Outputs. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-08-21/sta/outputs, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-08-21/sta/outputs, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2026-08-21T14:44:18.728827+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Pack3** (`proj-pack3`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Pack3. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/source/pack1/pack3, `file_uri`: file:///Users/pierfrancesco/source/pack1/pack3, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-09-10T09:54:29.795480+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Pack4** (`proj-pack4`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Pack4. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/source/pack1/pack2/pack4, `file_uri`: file:///Users/pierfrancesco/source/pack1/pack2/pack4, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-09-10T09:56:36.376601+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Palazzo** (`proj-palazzo`)
  - **Tags:** `#c` `#c-lang` `#mac-project`
  - **Sintesi:** Progetto Mac: Palazzo. Stack: C.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Palazzo/Palazzo, `file_uri`: file:///Users/pierfrancesco/Documents/Palazzo/Palazzo, `languages`: ['C'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2024-10-21T19:48:49.409353+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Particle Engine Simulation** (`proj-particle-engine-simulation`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** A real-time **3D particle swarm simulator** built with **Three.js** and a custom CPU-side "physics" loop. It seamlessly morphs tens of thousands of particles into various procedural formations, driven
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Particle Engine Simulation, `file_uri`: file:///Users/pierfrancesco/Desktop/Particle Engine Simulation, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 14, `last_modified`: 2026-04-30T14:11:00.943410+00:00, `key_dependencies`: [], `readme_excerpt`: # 🌌 AI Particle Simulator

A real-time **3D particle swarm simulator** built with **Three.js** and a custom CPU-side "physics" loop. It seamlessly morphs tens of thousands of particles into various procedural formations, driven by mathematical functions, physics simulations, and custom AI logic. 

The project also features an experimental **hand-gesture control** layer powered by **MediaPipe Hands**, a **Smart Text Engine**, and an **AI Architect / Custom Logic** panel to inject JavaScript at runtime for maximum flexibility.

> **Tech stack:** HTML, CSS, JavaScript (Vanilla, no bundler), Three
- **Pdc** (`proj-pdc`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Pdc. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/PDC, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/PDC, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2026-06-23T16:30:33.748117+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Pgf Pie** (`proj-pgf-pie`)
  - **Tags:** `#mac-project` `#web`
  - **Sintesi:** ![CI](https://github.com/pgf-tikz/pgf-pie/workflows/CI/badge.svg)
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/pgf-pie, `file_uri`: file:///Users/pierfrancesco/Downloads/pgf-pie, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 6, `last_modified`: 2022-06-15T09:40:30+00:00, `key_dependencies`: [], `readme_excerpt`: # pgf-pie

![CI](https://github.com/pgf-tikz/pgf-pie/workflows/CI/badge.svg)

Some LaTeX macros for pie charts using the PGF/TikZ package.

Please go to the official repository at https://github.com/pgf-tikz/pgf-pie or
the official mailing list at https://tug.org/mailman/listinfo/pgf-tikz to
submit bug reports, request new features, etc.

Please read pgf-pie-manual.pdf for more information.

## License

pgf-pie is released under the terms of both the LPPL v1.3c and the GPL v2.
- **Pierfrancesco Amendola** (`proj-pierfrancescoamendola`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** - Location: Naples 80125, Italy
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/PierfrancescoAmendola, `file_uri`: file:///Users/pierfrancesco/Desktop/PierfrancescoAmendola, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 35, `last_modified`: 2026-06-26T11:44:19.579749+00:00, `key_dependencies`: [], `readme_excerpt`: # Pierfrancesco Amendola

- Location: Naples 80125, Italy
- Date of Birth: 30/09/2005
- Phone: +39 370 339 4489
- Personal Email: [checcofran717@gmail.com](mailto:checcofran717@gmail.com)
- University Email: [pi.amendola@studenti.unina.it](mailto:pi.amendola@studenti.unina.it)
- GitHub: [github.com/PierfrancescoAmendola](https://github.com/PierfrancescoAmendola)
- LinkedIn: [pierfrancesco-amendola](https://www.linkedin.com/in/pierfrancesco-amendola-0952a729a/)
- Instagram: [@pierfrancesco.amendola](https://www.instagram.com/pierfrancesco.amendola)
- Portfolio Website: [pierfrancescoamendola.gi
- **Posgre Sql Pg Admin** (`proj-posgresql-pgadmin`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Posgre Sql Pg Admin. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/PosgreSQL-pgAdmin, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/PosgreSQL-pgAdmin, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-11-06T11:24:02.303028+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Progetto Gestione Bibloteca** (`proj-progetto-gestione-bibloteca`)
  - **Tags:** `#mac-project` `#python`
  - **Sintesi:** Sistema di gestione di una biblioteca pubblica/privata/casalinga, tiene traccia di tutto ciò che è necessario e fondamentale
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Progetto-Gestione-Bibloteca, `file_uri`: file:///Users/pierfrancesco/Desktop/Progetto-Gestione-Bibloteca, `languages`: ['Python'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 8, `last_modified`: 2025-10-01T10:45:40.075211+00:00, `key_dependencies`: [], `readme_excerpt`: # Progetto-Gestione-Bibloteca
Sistema di gestione di una biblioteca pubblica/privata/casalinga, tiene traccia di tutto ciò che è necessario e fondamentale
- **Propedia Demo** (`proj-propedia-demo`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Mockup stakeholder, not production app.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-09/caveman-users-pierfrancesco-agents-skills-caveman-2/outputs/propedia-demo, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-09/caveman-users-pierfrancesco-agents-skills-caveman-2/outputs/propedia-demo, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 5, `last_modified`: 2026-07-09T12:44:21.560635+00:00, `key_dependencies`: [], `readme_excerpt`: # PROPEDIA demo

Mockup stakeholder, not production app.

## Run

Open `index.html` directly or serve directory:

```bash
python3 -m http.server 4173 --directory outputs/propedia-demo
```

## What works

- Onboarding with preloaded student profile and localStorage persistence.
- Micro-diagnosis with deterministic questions and measured-level correction.
- Prerequisite graph with depth and dependency reasons.
- Adaptive explanation with depth switcher.
- Study calendar generation up to exam date.
- Emotional check-in with non-therapeutic coaching text.
- Ateneo dashboard mock with aggregated di
- **Psld1** (`proj-psld1`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: Psld1. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Progetto LASD 2025/PSLD1, `file_uri`: file:///Users/pierfrancesco/Desktop/Progetto LASD 2025/PSLD1, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 40, `last_modified`: 2025-05-23T12:46:19+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Psld2 Senza Git** (`proj-psld2-senza-git`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: Psld2 Senza Git. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Progetto LASD 2025/PSLD2 senza git, `file_uri`: file:///Users/pierfrancesco/Desktop/Progetto LASD 2025/PSLD2 senza git, `languages`: ['C++'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 54, `last_modified`: 2025-07-27T14:25:17.118549+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Final** (`proj-render_final`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Final. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_final, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_final, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:04:59.999747+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Pdf Temp** (`proj-render_pdf_temp`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Pdf Temp. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_pdf_temp, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_pdf_temp, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:50:01.586037+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Proof 1** (`proj-render_proof_1`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Proof 1. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_proof_1, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_proof_1, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:33:56.873932+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Proof Final** (`proj-render_proof_final`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Proof Final. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_proof_final, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_proof_final, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:50:01.936337+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Revision** (`proj-render_revision`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Revision. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_revision, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_revision, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T16:22:27.596136+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render Revision Final** (`proj-render_revision_final`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render Revision Final. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_revision_final, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render_revision_final, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T17:29:12.703701+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render1** (`proj-render1`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render1. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render1, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render1, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:00:55.210738+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render2** (`proj-render2`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render2. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render2, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render2, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:01:42.124254+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Render3** (`proj-render3`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Render3. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render3, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/render3, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-07-23T14:02:49.252847+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Rendered** (`proj-rendered`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Rendered. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-08-21/sta/work/rendered, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-08-21/sta/work/rendered, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-08-21T14:42:41.008218+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Rendered V2** (`proj-rendered_v2`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Rendered V2. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-08-21/sta/work/rendered_v2, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-08-21/sta/work/rendered_v2, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-08-21T14:43:38.264572+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Reti Di Calcolatori** (`proj-reti-di-calcolatori`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Reti Di Calcolatori. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/RETI DI CALCOLATORI, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/RETI DI CALCOLATORI, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-10-21T06:55:46.145099+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Sample** (`proj-sample`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: Sample. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/Sample/Sample, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/Sample/Sample, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-04-24T07:55:38.839054+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Sim** (`proj-sim`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Sim. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/SIM, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/SIM, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2025-06-11T07:39:57.710469+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Sito Certificati** (`proj-sitocertificati`)
  - **Tags:** `#javascript` `#mac-project` `#react` `#tailwind` `#tailwindcss` `#typescript` `#vite` `#web`
  - **Sintesi:** This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/SitoCertificati, `file_uri`: file:///Users/pierfrancesco/Desktop/SitoCertificati, `languages`: ['JavaScript', 'TypeScript'], `frameworks`: ['React', 'TailwindCSS', 'Vite'], `has_git`: False, `relevant_files_count`: 31, `last_modified`: 2026-06-26T11:25:29.899930+00:00, `key_dependencies`: ['pdfjs-dist', 'react', 'react-dom', 'react-pdf', '@eslint/js', '@tailwindcss/postcss', '@types/node', '@types/react', '@types/react-dom', '@vitejs/plugin-react', 'autoprefixer', 'eslint', 'eslint-plugin-react-hooks', 'eslint-plugin-react-refresh', 'globals'], `readme_excerpt`: # React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentatio
- **Slide Tec Web** (`proj-slidetecweb`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Slide Tec Web. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/TEC WEB/SlideTecWeb, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/TEC WEB/SlideTecWeb, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 15, `last_modified`: 2026-04-28T10:45:38.194494+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Soluzione Postgress Pgadmin Prof** (`proj-soluzionepostgress_pgadmin_prof`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Soluzione Postgress Pgadmin Prof. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/soluzionePOSTGRESS_PGADMIN_PROF, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/soluzionePOSTGRESS_PGADMIN_PROF, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-11-06T10:27:19.787392+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Source Chapters** (`proj-source_chapters`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Source Chapters. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/source_chapters, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-23/documents-plugin-documents-openai-primary-runtime-3/work/source_chapters, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 14, `last_modified`: 2026-07-23T16:21:36.567343+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Spiegazione Codice Librerire** (`proj-spiegazione-codice-librerire`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Spiegazione Codice Librerire. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Progetto LASD 2025/Spiegazione codice librerire, `file_uri`: file:///Users/pierfrancesco/Desktop/Progetto LASD 2025/Spiegazione codice librerire, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 4, `last_modified`: 2025-07-23T06:46:12.330743+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Statistica** (`proj-statistica`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Statistica. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/PDF/CPS/Statistica, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/PDF/CPS/Statistica, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 17, `last_modified`: 2026-02-09T22:52:30+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Svolti** (`proj-svolti`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Svolti. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Esami LP1/Esame Marzo 2021/Svolti, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Esami LP1/Esame Marzo 2021/Svolti, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 4, `last_modified`: 2025-06-16T20:51:41+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Taste Skill** (`proj-taste-skill`)
  - **Tags:** `#mac-project`
  - **Sintesi:** This directory is now a multi-style frontend skill pack with a single main entrypoint.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/taste-skill, `file_uri`: file:///Users/pierfrancesco/Downloads/taste-skill, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 22, `last_modified`: 2026-04-12T15:01:20+00:00, `key_dependencies`: [], `readme_excerpt`: # Taste Skill Pack

This directory is now a multi-style frontend skill pack with a single main entrypoint.

## Start here

- Main router: `SKILL.md`
- Shared component system: `components/`
- Style-specific skills: one `skill.md` inside each style folder

The intended flow is:

1. the agent reads `SKILL.md` first
2. `SKILL.md` chooses the best style for the brief
3. the agent opens that style's `skill.md`
4. the agent uses `components/style-recipes.md` and the rest of `components/` to strengthen the build

## Included styles

- `brutalism`
- `cinematic-product`
- `dark-luxe`
- `dashboards`
- `
- **Tec Web Lezioni** (`proj-tecweblezioni`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: Tec Web Lezioni. Stack: JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/TecWebLezioni, `file_uri`: file:///Users/pierfrancesco/Desktop/TecWebLezioni, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2026-04-21T12:35:08.234872+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Test Repo Main** (`proj-testrepo-main`)
  - **Tags:** `#mac-project`
  - **Sintesi:** Progetto Mac: Test Repo Main. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/TestRepo-main, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LSO/TestDockerIMG/TestRepo-main, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 4, `last_modified`: 2021-01-02T06:56:12+00:00, `key_dependencies`: [], `readme_excerpt`: # TestRepo
- **Tscheck** (`proj-tscheck`)
  - **Tags:** `#javascript` `#mac-project` `#react` `#tailwind` `#tailwindcss` `#typescript` `#vite` `#web`
  - **Sintesi:** Progetto Mac: Tscheck. Stack: JavaScript, React, TailwindCSS, TypeScript, Vite.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Documents/Codex/2026-07-21/new-chat/work/tscheck, `file_uri`: file:///Users/pierfrancesco/Documents/Codex/2026-07-21/new-chat/work/tscheck, `languages`: ['JavaScript', 'TypeScript'], `frameworks`: ['React', 'TailwindCSS', 'Vite'], `has_git`: False, `relevant_files_count`: 14, `last_modified`: 2026-07-21T16:12:27.034058+00:00, `key_dependencies`: ['lucide-react', 'react', 'react-dom', '@types/react', '@types/react-dom', '@vitejs/plugin-react', 'autoprefixer', 'postcss', 'tailwindcss', 'typescript', 'vite'], `readme_excerpt`: 
- **Uni Grade Projections Main** (`proj-uni-grade-projections-main`)
  - **Tags:** `#javascript` `#mac-project` `#react` `#swift` `#tailwind` `#tailwindcss` `#typescript` `#vite` `#web`
  - **Sintesi:** **URL**: https://lovable.dev/projects/a3846006-ca48-4704-9c96-8dc98198290c
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/Applicazioni/uni-grade-projections-main, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/Applicazioni/uni-grade-projections-main, `languages`: ['JavaScript', 'Swift', 'TypeScript'], `frameworks`: ['React', 'TailwindCSS', 'Vite'], `has_git`: False, `relevant_files_count`: 89, `last_modified`: 2025-11-01T16:25:57.758268+00:00, `key_dependencies`: ['@capacitor/ios', '@hookform/resolvers', '@radix-ui/react-accordion', '@radix-ui/react-alert-dialog', '@radix-ui/react-aspect-ratio', '@radix-ui/react-avatar', '@radix-ui/react-checkbox', '@radix-ui/react-collapsible', '@radix-ui/react-context-menu', '@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu', '@radix-ui/react-hover-card', '@radix-ui/react-label', '@radix-ui/react-menubar', '@radix-ui/react-navigation-menu'], `readme_excerpt`: # Welcome to your Lovable project

## Project info

**URL**: https://lovable.dev/projects/a3846006-ca48-4704-9c96-8dc98198290c

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/a3846006-ca48-4704-9c96-8dc98198290c) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The onl
- **Uni Stats** (`proj-unistats`)
  - **Tags:** `#ios` `#mac-project` `#swift` `#swiftui` `#web` `#xcodegen`
  - **Sintesi:** Un'applicazione iOS nativa per il tracciamento e la simulazione della carriera universitaria.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppVoti/UniStats, `file_uri`: file:///Users/pierfrancesco/Desktop/AppVoti/UniStats, `languages`: ['Swift'], `frameworks`: ['SwiftUI', 'XcodeGen'], `has_git`: True, `relevant_files_count`: 33, `last_modified`: 2026-03-07T21:08:55.859565+00:00, `key_dependencies`: [], `readme_excerpt`: # UniStats iOS App

Un'applicazione iOS nativa per il tracciamento e la simulazione della carriera universitaria.

## Caratteristiche

- **📚 Gestione Esami**: Aggiungi, modifica ed elimina i tuoi esami con voto, CFU, data e lode
- **📊 Dashboard Statistiche**: Visualizza media ponderata, voto base di laurea, distribuzione voti e molto altro
- **🎯 Simulatore Voto**: Prevedi il tuo voto finale di laurea in base a esami rimanenti e obiettivi
- **📈 Proiezione Media**: Grafico dell'andamento storico con proiezioni future per raggiungere i tuoi obiettivi
- **🧮 Calcolatori Utility**: Tool "Salva-Media
- **Video Yt** (`proj-videoyt`)
  - **Tags:** `#c++` `#cpp` `#mac-project`
  - **Sintesi:** Progetto Mac: Video Yt. Stack: C++.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UNI/LASD/VideoYT/VideoYT, `file_uri`: file:///Users/pierfrancesco/Desktop/UNI/LASD/VideoYT/VideoYT, `languages`: ['C++'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-05-08T11:00:31.367661+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Workspace** (`proj-workspace`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: Workspace. Stack: JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Downloads/workspace, `file_uri`: file:///Users/pierfrancesco/Downloads/workspace, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 5, `last_modified`: 2026-08-30T14:35:35+00:00, `key_dependencies`: [], `readme_excerpt`: # Prova

### [Macro-Label: `SCRIPT_TOOL`]
- **App Aule Studio Type Script** (`proj-appaulestudiotypescript`)
  - **Tags:** `#c` `#c-lang` `#javascript` `#mac-project` `#react` `#swift` `#typescript` `#web`
  - **Sintesi:** **UniStudy Italia** è l'applicazione definitiva per gli studenti universitari italiani che cercano il posto perfetto per studiare. Che tu abbia bisogno di silenzio assoluto, di un'aula per lavori di g
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppAuleStudioTypeScript, `file_uri`: file:///Users/pierfrancesco/Desktop/AppAuleStudioTypeScript, `languages`: ['C', 'JavaScript', 'Swift', 'TypeScript'], `frameworks`: ['React'], `has_git`: True, `relevant_files_count`: 164, `last_modified`: 2026-03-04T22:30:29.257571+00:00, `key_dependencies`: ['@expo-google-fonts/montserrat', '@expo-google-fonts/poppins', '@react-native-async-storage/async-storage', '@react-native-community/masked-view', '@react-navigation/native', '@react-navigation/stack', 'expo', 'expo-av', 'expo-constants', 'expo-device', 'expo-font', 'expo-linear-gradient', 'expo-location', 'expo-permissions', 'expo-status-bar'], `readme_excerpt`: # UniStudy Italia 🎓🇮🇹

**UniStudy Italia** è l'applicazione definitiva per gli studenti universitari italiani che cercano il posto perfetto per studiare. Che tu abbia bisogno di silenzio assoluto, di un'aula per lavori di gruppo o di una biblioteca aperta 24h, UniStudy ti aiuta a trovarla.

## 🌟 Funzionalità Principali

*   **Multi-Ateneo**: Supporto per oltre 100 atenei e istituti su tutto il territorio nazionale:
    *   **Campania**: Federico II, Vanvitelli, Parthenope, L'Orientale, UNISA (Salerno), UNISANNIO (Benevento).
    *   **Lazio**: La Sapienza, Tor Vergata.
    *   **Piemonte**: Un
- **Habit Tracker** (`proj-habittracker`)
  - **Tags:** `#appgroup` `#ios` `#javascript` `#mac-project` `#swift` `#swiftui` `#web` `#widgetkit` `#xcodegen`
  - **Sintesi:** Benvenuto nel repository ufficiale di **Habit Tracker**, un'applicazione iOS nativa progettata per aiutarti a costruire, mantenere e tracciare le tue abitudini quotidiane in modo semplice ed elegante.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/HabitTracker, `file_uri`: file:///Users/pierfrancesco/Desktop/HabitTracker, `languages`: ['JavaScript', 'Swift'], `frameworks`: ['AppGroup', 'SwiftUI', 'WidgetKit', 'XcodeGen'], `has_git`: True, `relevant_files_count`: 82, `last_modified`: 2026-08-27T11:01:24.397072+00:00, `key_dependencies`: [], `readme_excerpt`: # 🎯 Habit Tracker

Benvenuto nel repository ufficiale di **Habit Tracker**, un'applicazione iOS nativa progettata per aiutarti a costruire, mantenere e tracciare le tue abitudini quotidiane in modo semplice ed elegante. L'app offre un'esperienza fluida e personalizzata per garantire che raggiungere i tuoi obiettivi diventi, appunto, un'abitudine.

---

## 🚀 Panoramica del Progetto

**Habit Tracker** è sviluppata interamente per l'ecosistema Apple (iOS 17.0+), sfruttando le più recenti tecnologie introdotte per iOS come **SwiftUI** e **SwiftData**. L'obiettivo è quello di fornire all'utente uno
- **Mac Pulse Tests** (`proj-macpulsetests`)
  - **Tags:** `#mac-project` `#swift`
  - **Sintesi:** Progetto Mac: Mac Pulse Tests. Stack: Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse/MacPulseTests, `file_uri`: file:///Users/pierfrancesco/MacPulse/MacPulseTests, `languages`: ['Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-10-21T19:49:24.024815+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Mac Pulse Uitests** (`proj-macpulseuitests`)
  - **Tags:** `#mac-project` `#swift`
  - **Sintesi:** Progetto Mac: Mac Pulse Uitests. Stack: Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse/MacPulseUITests, `file_uri`: file:///Users/pierfrancesco/MacPulse/MacPulseUITests, `languages`: ['Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-10-21T19:49:24.080852+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Mac Pulse2Tests** (`proj-macpulse2tests`)
  - **Tags:** `#mac-project` `#swift`
  - **Sintesi:** Progetto Mac: Mac Pulse2Tests. Stack: Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse2/MacPulse2Tests, `file_uri`: file:///Users/pierfrancesco/MacPulse2/MacPulse2Tests, `languages`: ['Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-10-23T07:32:02.367029+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Mac Pulse2Uitests** (`proj-macpulse2uitests`)
  - **Tags:** `#mac-project` `#swift`
  - **Sintesi:** Progetto Mac: Mac Pulse2Uitests. Stack: Swift.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/MacPulse2/MacPulse2UITests, `file_uri`: file:///Users/pierfrancesco/MacPulse2/MacPulse2UITests, `languages`: ['Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-10-23T07:32:02.398936+00:00, `key_dependencies`: [], `readme_excerpt`: 

### [Macro-Label: `UI_COMPONENT`]
- **SwiftUI Interface Layer (proj-appcalcolatori)** (`proj-appcalcolatori-ui-layer`)
  - **Tags:** `#swiftui` `#ui` `#apple`
  - **Sintesi:** Interfaccia utente dichiarativa SwiftUI per il progetto proj-appcalcolatori.
  - **Dettagli:** `parent_project`: proj-appcalcolatori, `file_uri`: file:///Users/pierfrancesco/Desktop/AppCalcolatori
- **SwiftUI Interface Layer (proj-caretrack-demo)** (`proj-caretrack-demo-ui-layer`)
  - **Tags:** `#swiftui` `#ui` `#apple`
  - **Sintesi:** Interfaccia utente dichiarativa SwiftUI per il progetto proj-caretrack-demo.
  - **Dettagli:** `parent_project`: proj-caretrack-demo, `file_uri`: file:///Users/pierfrancesco/Desktop/CareTrack-Demo
- **SwiftUI Interface Layer (proj-habittracker)** (`proj-habittracker-ui-layer`)
  - **Tags:** `#swiftui` `#ui` `#apple`
  - **Sintesi:** Interfaccia utente dichiarativa SwiftUI per il progetto proj-habittracker.
  - **Dettagli:** `parent_project`: proj-habittracker, `file_uri`: file:///Users/pierfrancesco/Desktop/HabitTracker
- **SwiftUI Interface Layer (proj-unistats)** (`proj-unistats-ui-layer`)
  - **Tags:** `#swiftui` `#ui` `#apple`
  - **Sintesi:** Interfaccia utente dichiarativa SwiftUI per il progetto proj-unistats.
  - **Dettagli:** `parent_project`: proj-unistats, `file_uri`: file:///Users/pierfrancesco/Desktop/AppVoti/UniStats

### [Macro-Label: `USER_INTENT`]
- **Accorciamento e Compressione Cappello Capitolo 6** (`user-intent-accorciamento-cappello-capitolo-6`)
  - **Tags:** `#tesi-laurea` `#ottimizzazione-testo` `#latex`
  - **Sintesi:** Richiesta di revisione e sintesi del cappello introduttivo per il Capitolo 6, riducendo la lunghezza e mantenendo una forma discorsiva e diretta.
  - **Dettagli:** `user_prompt`: mi piace ma accorcialo un altro pò, un pò troppo lungo, `context`: Perfezionamento del testo per la tesi di laurea in Informatica (Federico II / ICAR-CNR).
- **Allineamento e Diagnosi Discrepanza Nodi Render e Locale** (`user-intent-allineamento-nodi-render`)
  - **Tags:** `#render` `#sync` `#deploy` `#git` `#discrepanza`
  - **Sintesi:** Richiesta di spiegazione sulla discrepanza tra 208 nodi locali e 204 su Render e sincronizzazione del database cloud.
  - **Dettagli:** `raw`: `user_prompt`: /universal-brain /graphify aggiorna i nodi su render. qui ne 208 su render 204, perchè??, `context`: Discrepanza di 4 nodi tra ambiente locale e istanza Render cloud dovuta a commit pendente.
- **Analisi Feedback Gemini e Piano Ottimizzazione Cervello** (`user-intent-analisi-feedback-gemini-ottimizzazione-cervello`)
  - **Tags:** `#feedback-gemini` `#graphrag` `#ottimizzazione-cervello` `#metamemoria`
  - **Sintesi:** Valutazione critica dell'assessment di Gemini sul Cervello Artificiale e definizione delle migliorie al GraphRAG e all'architettura.
  - **Dettagli:** `raw`: `context`: Diagnosi discrepanza tra percezione esterna di Gemini e stato reale del Knowledge Graph (304 nodi, 789 archi), `user_prompt`: vedi cosa mi ha detto gemini, secondo te che dobbiamo fare, cosa possiamo migliorare??
- **Analisi Integrazioni LLM con Notion e Obsidian** (`user-intent-confronto-integrazioni-llm-notion-obsidian`)
  - **Tags:** `#pkm` `#obsidian` `#notion` `#rag` `#second-brain` `#llm-tools`
  - **Sintesi:** Richiesta di spiegazione comparativa sulle ragioni e i casi d'uso dell'integrazione di LLM con Notion e Obsidian.
  - **Dettagli:** `user_prompt`: Perché molti collegano Notion a Claude, Gemini ecc…cosa fa di diverso. Perché collegano anche obsidian? Cosa si può fare con obsidian, `context`: Valutazione dei sistemi di Personal Knowledge Management (PKM) e strategie RAG locali vs cloud., `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Chiarimento Stack Rendering Grafi Frontend** (`user-intent-chiarimento-stack-rendering-grafi-frontend`)
  - **Tags:** `#frontend` `#graph-visualization` `#vis-network` `#threejs` `#d3js` `#cytoscape`
  - **Sintesi:** Verifica dello stato di utilizzo e adozione di Vis-network, 3d-force-graph, Three.js, D3.js e Cytoscape.js nel frontend del connettoma.
  - **Dettagli:** `context`: Richiesta chiarimenti sull'uso di Cytoscape.js, Vis-network, 3d-force-graph e D3.js nel frontend di Universal AI Brain, `user_prompt`: /universal-brain per la rappresentazione grafica dei grafi nel nostro frontend/sito, usiamo queste cose?? Cytoscape.js, Vis-network, 3d-force-graph, D3.js
- **Costruzione App Personale Apprendimento Portoghese e Tedesco** (`intent-personal-language-learning-app`)
  - **Tags:** `#language-learning` `#portuguese` `#german` `#personal-software` `#srs`
  - **Sintesi:** L'utente desidera sviluppare un software o web app strettamente personale e privato per apprendere il portoghese e il tedesco, superando le limitazioni di energia e monetizzazione di Duolingo.
  - **Dettagli:** `raw`: `target_languages`: ['Portoghese', 'Tedesco'], `motivation`: Superamento paywall/energia di Duolingo, `scope`: Uso esclusivo personale e privato, `user_prompt`: L'utente desidera sviluppare un software o web app strettamente personale e privato per apprendere il portoghese e il tedesco, superando le limitazioni di energia e monetizzazione di Duolingo.
- **De-cluttering UI & Projector 3D a Schermo Intero** (`user-intent-ui-declutter-projector-fullscreen`)
  - **Tags:** `#untagged`
  - **Sintesi:** Semplificazione radicale dell'interfaccia con dropdown e visualizzatore 3D full-page
  - **Dettagli:** `context`: Eliminazione bottoni sparsi, menu a tendina e Projector 3D a schermo intero, `user_prompt`: rifacciamo il look con menù a tendina, projector 3d a schermo intero senza sidebar destra ed eliminazione mappamondo 3d
- **Definizione Architettura & Gamification App Personale Lingue** (`intent-personal-language-app-structure`)
  - **Tags:** `#duolingo-like` `#busuu-like` `#pedagogy` `#curriculum-design` `#gamification`
  - **Sintesi:** L'utente richiede consigli approfonditi sulla struttura funzionale e pedagogica di un'app personale (stile Duolingo/Busuu) con flow a lezioni, zero paywall e nessun blocco energia.
  - **Dettagli:** `raw`: `benchmark_apps`: ['Duolingo', 'Busuu'], `key_requirements`: ['No energy limitations', 'Free/Local', 'Structured CEFR progression'], `user_prompt`: L'utente richiede consigli approfonditi sulla struttura funzionale e pedagogica di un'app personale (stile Duolingo/Busuu) con flow a lezioni, zero paywall e nessun blocco energia.
- **Definizione Linee Guida Grafiche e UI per App Linguistica** (`intent-language-app-ui-design`)
  - **Tags:** `#ui-design` `#design-system` `#ux-flow` `#graphic-style` `#frontend`
  - **Sintesi:** L'utente richiede la definizione della grafica, dello stile visivo e dell'interfaccia utente per l'applicazione personale di apprendimento linguistico.
  - **Dettagli:** `raw`: `focus`: Design dell'interfaccia, token visivi, animazioni e layout degli esercizi, `user_prompt`: L'utente richiede la definizione della grafica, dello stile visivo e dell'interfaccia utente per l'applicazione personale di apprendimento linguistico.
- **Implementazione e Collaudo Ecosistema Ubiquitous Supercervello** (`user-intent-implementazione-ecosistema-supercervello`)
  - **Tags:** `#supercervello` `#raycast` `#safari-clipper` `#siri` `#rem-cycle` `#obsidian-canvas` `#zero-cost`
  - **Sintesi:** Costruzione completa e collaudo a 10 test di tutti i moduli di estensione: Raycast, Web Clipper Safari, Siri Voice Note, Daily Pulse Telegram, Kindle Sync, REM Cycle, Ricerca Ibrida RRF, IDE Hooks e Obsidian Canvas.
  - **Dettagli:** `context`: Costruzione dell'intero ecosistema ad attrito zero su Safari, Mac, Mobile e demone notturno, `user_prompt`: allora procedi con l'implementazione del piano chiaro??? io utilizzo safari. va bene l'orario che hai stabilito. procedi, mi raaccomando, vai piano piano
- **Integrazione Emisferi Globo, Ottica Spaziale e Refinements Projector 3D** (`user-intent-embedding-projector-globe-and-optics`)
  - **Tags:** `#ui` `#projector3d` `#webgl` `#threejs` `#optics`
  - **Sintesi:** Implementazione della modalità Mappamondo Sferico con distribuzione bi-emisferica, controlli slider GPU per distanza nodi, luminosità pura e opacità archi, e pulsante di uscita rosso in basso a sinistra.
  - **Dettagli:** `context`: Mappamondo 3D sferico stile projector, disaccoppiamento luminosità da dimensione nodi, spaziatura nodi fluida e uscita projector in basso a sinistra in rosso, `user_prompt`: in project 3d affianco 3d volumetrico e planare aggiungi emisfero, proviamo a creare un mappamondo... aggiungi la possibilità di modificare la distanza dei nodi tra di loro, se aumentare la luminosità degli archi o dei nodi... non voglio che la luminosità sia dipendente dalla dimensione dei nodi.
- **Integrazione Riferimento Tabelle Comparative nel Cappello del Capitolo 6** (`user-intent-integrazione-tabelle-cappello-capitolo-6`)
  - **Tags:** `#tesi-laurea` `#tabelle-comparative` `#latex` `#metodologia`
  - **Sintesi:** Richiesta di aggiungere 2-3 righe al cappello introduttivo del Capitolo 6 specificando che i risultati saranno presentati e comparati sistematicamente tramite tabelle riassuntive.
  - **Dettagli:** `user_prompt`: perfetto aggiungi solo che vedremo i risultati ottenuti, e potremo compararli tramite le tabelle ecc..giusto altre due/tre righe, `context`: Perfezionamento finale del testo introduttivo del Capitolo 6 (Risultati e Discussione) per la tesi di laurea triennale.
- **Intento Utente: Collegare Cervello via MCP e Skill a Claude, Gemini e ChatGPT** (`user-intent-connect-gemini-claude-chatgpt-mcp`)
  - **Tags:** `#user-intent` `#mcp-integration` `#multi-model-sync`
  - **Sintesi:** Richiesta di configurazione MCP e binding della skill /universal-brain su Claude, Gemini e ChatGPT.
  - **Dettagli:** `raw`: `target`: Multi-LLM ubiquitous cognition, `user_prompt`: Richiesta di configurazione MCP e binding della skill /universal-brain su Claude, Gemini e ChatGPT.
- **Intento Utente: Comprensione del Ruolo di Render Cloud e Analisi del Rifiuto di Claude Web** (`intent-clarify-render-cloud-utility-and-llm-web-refusal`)
  - **Tags:** `#user-intent` `#cloud-architecture` `#claude-web-refusal` `#clarification`
  - **Sintesi:** Pierfrancesco richiede spiegazione sul perché avere il backend su Render se gli agenti desktop leggono localmente, e come superare il rifiuto dei modelli web per lettura memoria.
  - **Dettagli:** `raw`: `user_prompt`: una domanda, ma se claude desktop, antigravity ecc...leggono i file dal mio pc allora che senso ha avere tutto su render?? spiegami?? lo scopo era che le ai leggessero da internet il mio sito, la mia memoria e poi creassero dei file json che avrei aggiunto al mio cervello per mantenere il contesto, e memoria della chat. spiega non agire !!!, `analysis`: Richiesta di formalizzazione della pipeline omnicanale (Cloud API vs Local Stdio vs Web Chat Attachment)
- **Intento Utente: Gateway Telegram per Accesso Cognitivo Ovunque** (`user-intent-telegram-bot-gateway`)
  - **Tags:** `#user-intent` `#telegram` `#telegram-bot` `#omnipresence` `#mobile-access` `#zero-cost`
  - **Sintesi:** Progetto di collegare il cervello a un Bot Telegram personale per query rapide, ricerca e inserimento di memorie/post ovunque via smartphone.
  - **Dettagli:** `raw`: `capabilities`: ['Query FTS5', 'Shortest path', 'Hierarchical tree summary', 'Quick note ingestion'], `user_prompt`: Progetto di collegare il cervello a un Bot Telegram personale per query rapide, ricerca e inserimento di memorie/post ovunque via smartphone.
- **Intento Utente: Grafica Statica Stabile, Zero Oscillazioni e Zero Lag** (`user-intent-zero-oscillation-high-performance-graph`)
  - **Tags:** `#user-preference` `#zero-lag` `#stability` `#anti-jitter` `#high-performance`
  - **Sintesi:** Direttiva esplicita di Pierfrancesco: il grafo del cervello artificiale non deve mai ruotare da solo, oscillare, ballare o generare lag; la struttura visiva deve rimanere fissa e solida come graphify.html, garantendo massima reattività all interazione.
  - **Dettagli:** `raw`: `priority`: Massima priorità UX/Performance, `rule`: Stabilizzazione calcolata in memoria -> Physics spenta -> Nodi fissi -> Zero jitter, `user`: Pierfrancesco Amendola, `user_prompt`: Sistema di design tokens e palette colori per l interfaccia utente ispirata a Graphify.com e Caveman.so: Deep Void (#07080c), Neon Cyan (#00D2FF), Cyber Magenta (#FF007F) e Electric Purple (#A855F7).
- **Intento Utente: Hierarchical Tree Engine Completamente Rilasciato e Sincronizzato** (`intent-ep-20260827-hierarchical-tree-deployment-sync`)
  - **Tags:** `#user-intent` `#query` `#deployment-report-ingestion-and-translation`
  - **Sintesi:** Traduzione e report di rilascio: Hierarchical Tree Engine e tool MCP brain_get_tree implementati con successo.
  - **Dettagli:** `raw`: `raw_query`: traduci: 層級譜系樹（Hierarchical Knowledge Tree / 層級譜系樹）已全面構建完成..., `intent_type`: DEPLOYMENT_REPORT_INGESTION_AND_TRANSLATION, `epistemic_status`: EXTRACTED, `target_domain`: System Release / Graph Engine Implementation / MCP Infrastructure, `user_prompt`: Traduzione e report di rilascio: Hierarchical Tree Engine e tool MCP brain_get_tree implementati con successo.
- **Intento Utente: Il mio che tipo di grafo è?** (`intent-ep-20260827-graph-taxonomy-classification`)
  - **Tags:** `#user-intent` `#query` `#structural-taxonomy-inquiry`
  - **Sintesi:** Il mio che tipo di grafo è?
  - **Dettagli:** `raw`: `raw_query`: Il mio che tipo di grafo è?, `intent_type`: STRUCTURAL_TAXONOMY_INQUIRY, `epistemic_status`: EXTRACTED, `target_domain`: Graph Theory / Formal Knowledge Representation, `user_prompt`: Il mio che tipo di grafo è?
- **Intento Utente: Migliore Soluzione - Albero Gerarchico a Comunità (Dendrogramma)** (`intent-ep-20260827-tree-ranking-translation`)
  - **Tags:** `#user-intent` `#query` `#translation-and-evaluation-consolidation`
  - **Sintesi:** Traduzione e formalizzazione: l'Albero Gerarchico (Dendrogramma) è la soluzione ottimale per risparmio token e Semantic Zoom.
  - **Dettagli:** `raw`: `raw_query`: traduci: 冠絕群策者：層級譜系樹（Hierarchical Community Tree / Dendrogram）..., `intent_type`: TRANSLATION_AND_EVALUATION_CONSOLIDATION, `epistemic_status`: EXTRACTED, `target_domain`: Knowledge Representation / Algorithmic Ranking / Multilingual Translation, `user_prompt`: Traduzione e formalizzazione: l'Albero Gerarchico (Dendrogramma) è la soluzione ottimale per risparmio token e Semantic Zoom.
- **Intento Utente: Non tutto deve collegarsi a Pierfrancesco, creare grafi modulari per dominio** (`user-intent-modular-cluster-decentralization`)
  - **Tags:** `#user-intent` `#graph-architecture` `#domain-separation`
  - **Sintesi:** Proposta di separazione topologica: concetti specialistici (es. medicina) formano cluster dedicati senza dipendere dal nodo persona.
  - **Dettagli:** `raw`: `example`: Onicocriptosi / Unghia incarnita, `user_prompt`: Proposta di separazione topologica: concetti specialistici (es. medicina) formano cluster dedicati senza dipendere dal nodo persona.
- **Intento Utente: Potenziamento GraphRAG & MCP a Costo Zero** (`user-intent-zero-cost-graphrag`)
  - **Tags:** `#user-intent` `#graphrag` `#mcp` `#zero-cost` `#high-efficiency` `#fts5`
  - **Sintesi:** Richiesta esplicita di sviluppo di un motore di ricerca ibrido (FTS5 BM25 + Shortest Path) e server MCP per Claude/Cursor senza costi aggiuntivi.
  - **Dettagli:** `raw`: `requested_features`: ['Motore di ricerca ibrido & GraphRAG (FTS5 BM25, Shortest Path, Subgraph extraction)', 'Protocollo MCP per Claude Desktop, Cursor e Antigravity', 'Zero costi operativi e massima stabilità'], `user_prompt`: Richiesta esplicita di sviluppo di un motore di ricerca ibrido (FTS5 BM25 + Shortest Path) e server MCP per Claude/Cursor senza costi aggiuntivi.
- **Intento Utente: Proposta di strutturare il cervello in più grafi annidati come un palazzo** (`user-intent-hierarchical-multi-layer-graph-design`)
  - **Tags:** `#user-intent` `#graph-architecture` `#multi-layer` `#hypergraph`
  - **Sintesi:** L'utente propone un modello in cui i nodi di un albero/grafo sono a loro volta grafi completi su più livelli.
  - **Dettagli:** `raw`: `metaphor`: Palazzo con pavimenti a grafo e stanze come sotto-nodi, `user_prompt`: L'utente propone un modello in cui i nodi di un albero/grafo sono a loro volta grafi completi su più livelli.
- **Intento Utente: Replicare l'inibizione interemisferica per spegnere l'emisfero non usato** (`user-intent-biological-lazy-loading-inhibition`)
  - **Tags:** `#user-intent` `#neuro-inspired` `#inhibition` `#performance`
  - **Sintesi:** L'utente propone di disattivare l'emisfero non pertinente durante l'analisi e attivarlo solo quando una sinapsi richiede una connessione trasversale.
  - **Dettagli:** `raw`: `metaphor`: Lazy-loading biologico GABAergico, `user_prompt`: L'utente propone di disattivare l'emisfero non pertinente durante l'analisi e attivarlo solo quando una sinapsi richiede una connessione trasversale.
- **Intento Utente: Si possono unire grafi e alberi di ricerca. Un grafo come il** (`intent-ep-20260827-graph-tree-unification`)
  - **Tags:** `#user-intent` `#query` `#theoretical-and-architectural-exploration`
  - **Sintesi:** Si possono unire grafi e alberi di ricerca. Un grafo come il mio con quello che ho creato, cioè un cervello?
  - **Dettagli:** `raw`: `raw_query`: Si possono unire grafi e alberi di ricerca. Un grafo come il mio con quello che ho creato, cioè un cervello?, `intent_type`: THEORETICAL_AND_ARCHITECTURAL_EXPLORATION, `epistemic_status`: EXTRACTED, `target_domain`: Cognitive Architectures / Neuro-Symbolic AI / Knowledge Systems, `user_prompt`: Si possono unire grafi e alberi di ricerca. Un grafo come il mio con quello che ho creato, cioè un cervello?
- **Intento Utente: Strategia Hub Cognitivo Telegram (Gateway Webhook 0€)** (`intent-ep-20260827-telegram-cognitive-hub-spec`)
  - **Tags:** `#user-intent` `#query` `#specification-translation-and-graph-ingest`
  - **Sintesi:** Traduzione e consolidamento: Architettura Telegram Bot Gateway 0€ con routing comandi e BFS trans-callosale.
  - **Dettagli:** `raw`: `raw_query`: traduci: 通透無礙，極佳之策。 Telegram 認知中樞架構（0€ Webhook 網關）..., `intent_type`: SPECIFICATION_TRANSLATION_AND_GRAPH_INGEST, `epistemic_status`: EXTRACTED, `target_domain`: System Integration / Telegram Webhook / Bi-directional BFS / FTS5 BM25, `user_prompt`: Traduzione e consolidamento: Architettura Telegram Bot Gateway 0€ con routing comandi e BFS trans-callosale.
- **Intento Utente: Valutazione Alberi Binari e Alberi Pesati** (`user-intent-tree-search-enhancement`)
  - **Tags:** `#user-intent` `#binary-tree` `#bst` `#weighted-tree` `#search-engine`
  - **Sintesi:** Proposta di integrare strutture ad albero (binari, pesati, gerarchici) per ottimizzare la ricerca e navigazione della memoria.
  - **Dettagli:** `raw`: `question`: Ha senso inserire alberi di ricerca o alberi pesati nel grafo del cervello?, `user_prompt`: Proposta di integrare strutture ad albero (binari, pesati, gerarchici) per ottimizzare la ricerca e navigazione della memoria.
- **Intento Utente: Valutazione Tecnica delle Strutture ad Albero (BST, B+Tree, MST, Tree)** (`intent-ep-20260827-tree-structures-evaluation`)
  - **Tags:** `#user-intent` `#query` `#data-structure-taxonomy-and-evaluation`
  - **Sintesi:** Valutazione tecnica delle strutture ad albero: BST, B+Tree, Maximum Spanning Tree, Hierarchical Tree e Prefix Trie per il grafo cognitivo.
  - **Dettagli:** `raw`: `raw_query`: 樹狀結構技術評析（Tree Evaluation）: BST, B+Tree, MST, Hierarchical Community Tree, Prefix Trie, `intent_type`: DATA_STRUCTURE_TAXONOMY_AND_EVALUATION, `epistemic_status`: EXTRACTED, `target_domain`: Graph Algorithms / Hierarchical Knowledge Trees / Cognitive Retrieval, `user_prompt`: Valutazione tecnica delle strutture ad albero: BST, B+Tree, Maximum Spanning Tree, Hierarchical Tree e Prefix Trie per il grafo cognitivo.
- **Intento Utente: Vorrei collegare il mio cervello a un bot su telegram giusto** (`intent-ep-20260827-telegram-bot-interface`)
  - **Tags:** `#user-intent` `#query` `#feasibility-and-architecture-analysis`
  - **Sintesi:** Vorrei collegare il mio cervello a un bot su telegram giusto per avere a portata di mano sempre le info, che ne pensi? Può essere utile? È gratis? È difficile da fare?
  - **Dettagli:** `raw`: `raw_query`: Vorrei collegare il mio cervello a un bot su telegram giusto per avere a portata di mano sempre le info, che ne pensi? Può essere utile? È gratis? È difficile da fare?, `intent_type`: FEASIBILITY_AND_ARCHITECTURE_ANALYSIS, `epistemic_status`: EXTRACTED, `target_domain`: Interface Design / Mobile Interaction / Telegram Bot API, `user_prompt`: Vorrei collegare il mio cervello a un bot su telegram giusto per avere a portata di mano sempre le info, che ne pensi? Può essere utile? È gratis? È difficile da fare?
- **Intento Utente: mica si perde la struttura a grafo e quello che abbiamo real** (`intent-ep-20260827-hierarchical-overlay-reassurance`)
  - **Tags:** `#user-intent` `#query` `#integrity-and-coexistence-verification`
  - **Sintesi:** mica si perde la struttura a grafo e quello che abbiamo realizzato? Albero Gerarchico (Hierarchical Tree)
  - **Dettagli:** `raw`: `raw_query`: mica si perde la struttura a grafo e quello che abbiamo realizzato? Albero Gerarchico (Hierarchical Tree), `intent_type`: INTEGRITY_AND_COEXISTENCE_VERIFICATION, `epistemic_status`: EXTRACTED, `target_domain`: Knowledge Preservation / Multiscale Graph Architectures, `user_prompt`: mica si perde la struttura a grafo e quello che abbiamo realizzato? Albero Gerarchico (Hierarchical Tree)
- **Intento: Aggiornamento Documentazione README.md** (`user-intent-update-readme-architecture`)
  - **Tags:** `#readme` `#documentazione` `#architettura` `#backend` `#algoritmi`
  - **Sintesi:** Documentare in modo esaustivo architettura bi-emisferica, backend, algoritmi, doppio anello e frontend nel README.md.
  - **Dettagli:** `context`: Riscrivere e potenziare il README.md della repository GitHub con tutti i dettagli tecnici del connettoma, `user_prompt`: ora aggiorna il file read.me della mia repo su github affinchè contenga tutto su come sia strutturato il cervello, il frontend, ma sorpatutto il backedn, la logica, gli algoritmi, i vari sistemi per mantenere attivo il server ecc...
- **Intento: Allora vorrei dirti che oggi ho man...** (`user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: Allora vorrei dirti che oggi ho man...
  - **Dettagli:** `raw`: `user_prompt`: Allora vorrei dirti che oggi ho mangiato pasta al sugo, `channel`: JARVIS Voice Core
- **Intento: Audit Completo Cervello, Graphify & Memoria Cross-Chat** (`user-intent-audit-cervello-e-graphify`)
  - **Tags:** `#audit` `#qa` `#bugfix` `#cross-chat-memory` `#omniscienza` `#graphify`
  - **Sintesi:** Richiesta di revisione completa del codice, verifica errori, prompt, documentazione e garanzia assoluta di persistenza del contesto conversazionale per garantire continuità cognitiva cross-chat.
  - **Dettagli:** `raw`: `area`: Audit, QA, Cross-Chat Memory Persistence, Protocollo Graphify, `context`: L'utente richiede che ogni chat inserisca tutto il contesto, le risposte date e le decisioni, affinché cambiando chat l'AI mantenga omniscienza totale senza perdita di memoria., `timestamp`: 2026-08-28T14:51:11+02:00, `user_prompt`: l'ai deve inserire il contesto della chat, le risposte date, tutto, in modo tale che cambiando chat sappia tutto ti trovi?? abbiamo fatto questo??? è presente questa condizione, è così realizzato lo schema???
- **Intento: Audit critico e mockup frontend del Univ** (`user-intent-audit-critico-e-mockup-fr-2255`)
  - **Tags:** `#user-intent` `#chat` `#audit-critico-e-mockup-frontend-del-universal`
  - **Sintesi:** Intento espresso da Pierfrancesco: Audit critico e mockup frontend del Universal AI Brain
  - **Dettagli:** `user_prompt`: Analizza criticamente il progetto Universal AI Brain e il suo Universal Knowledge Graph, evidenzia punti critici e realizza mockup frontend interattivi con codice reale per scegliere una ristrutturazione., `context`: Sessione su Audit critico e mockup frontend del Universal AI Brain
- **Intento: Cloud-Side Git Auto-Push da Render** (`user-intent-cloud-git-auto-push`)
  - **Tags:** `#cloud-sync` `#git-push` `#render` `#persistenza`
  - **Sintesi:** Eseguire git push automatico direttamente dal cloud ad ogni post/ingestione su Render.
  - **Dettagli:** `context`: Persistenza autonoma lato cloud su Render per evitare regressioni di commit, `user_prompt`: però potremmo fare che ogni volta che facciamo un post tramite sito web, o qualsiasi altra parte, questo post che contiene le nostre info, i nodi, archi, ecc... faccia anche un git push, quindi carichi tutto su github, in modo tale che se render si spegne e si riavvia non andrà a prendere il vecchio db, ma sarà sempre aggiornato, che ne pensi??
- **Intento: Comando /prompt Copia Rapida per Telegra** (`user-intent-comando-prompt-copia-rapi-8585`)
  - **Tags:** `#user-intent` `#chat` `#comando-prompt-copia-rapida-per-telegram-bot`
  - **Sintesi:** Intento espresso da Pierfrancesco: Comando /prompt Copia Rapida per Telegram Bot
  - **Dettagli:** `raw`: `user_prompt`: /universal-brain aggiungi ai comandi su telegram la possibilità che richiamato il comando /prompt si copi sul telefono il prompt che deve poi incollare l'utente nei vari software ai online chiaro??, `context`: Sessione su Comando /prompt Copia Rapida per Telegram Bot
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-2447`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: brain.db                                | Bin 2248704 -> 2260992 bytes
 brain_resurface.py                      |  52 +++++++++++-----
 main.py                                 | 102 ++++++++++++++++++++++++++++++++
 obsidian_vault/.obsidian/workspace.json |   4 +-
 skills-lock.json                        |  78 ++++++++++++++++++++++++
 sync_daemon.py                          |  31 ++++++++++
 telegram_bot.py                         |  61 ++++++++++++++++++-
 7 files changed, 309 insertions(+), 19 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-2471`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: brain.db                                | Bin 2269184 -> 2277376 bytes
 brain_resurface.py                      |  52 +++++++++++-----
 main.py                                 | 102 ++++++++++++++++++++++++++++++++
 obsidian_vault/.obsidian/workspace.json |   4 +-
 skills-lock.json                        |  78 ++++++++++++++++++++++++
 sync_daemon.py                          |  31 ++++++++++
 telegram_bot.py                         |  61 ++++++++++++++++++-
 7 files changed, 309 insertions(+), 19 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-2485`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'brain_resurface.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: brain.db                                | Bin 2293760 -> 2301952 bytes
 brain_resurface.py                      |  52 +++++++++++-----
 main.py                                 | 102 ++++++++++++++++++++++++++++++++
 obsidian_vault/.obsidian/workspace.json |   4 +-
 skills-lock.json                        |  78 ++++++++++++++++++++++++
 sync_daemon.py                          |  31 ++++++++++
 telegram_bot.py                         |  61 ++++++++++++++++++-
 7 files changed, 309 insertions(+), 19 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-2529`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'brain_resurface.py', 'brain_tensions.py', 'brain_weave.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: brain.db                                | Bin 2322432 -> 2322432 bytes
 brain_resurface.py                      |  61 ++++++++++++++-----
 brain_tensions.py                       |  10 +++-
 brain_weave.py                          |  10 +++-
 main.py                                 | 102 ++++++++++++++++++++++++++++++++
 obsidian_vault/.obsidian/workspace.json |   4 +-
 skills-lock.json                        |  78 ++++++++++++++++++++++++
 sync_daemon.py                          |  31 ++++++++++
 telegram_bot.py                         |  61 ++++++++++++++++++-
 9 files changed, 332 insertions(+), 25 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-2691`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['README.md', 'brain.db', 'brain_resurface.py', 'brain_tensions.py', 'brain_weave.py', 'main.py', 'obsidian_vault/.obsidian/workspace.json', 'skills-lock.json', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'obsidian_canvas_sync.py', 'obsidian_vault/00_CONNETOMA_CANVAS.canvas', 'raycast/', 'skills/brandkit', 'skills/design-taste-frontend', 'skills/design-taste-frontend-v1', 'skills/full-output-enforcement', 'skills/gpt-taste', 'skills/high-end-visual-design', 'skills/image-to-code', 'skills/imagegen-frontend-mobile', 'skills/imagegen-frontend-web', 'skills/industrial-brutalist-ui', 'skills/minimalist-ui', 'skills/redesign-existing-projects', 'skills/stitch-design-taste', 'static/video_assets/', 'tests/test_supercervello_ecosystem.py', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: README.md                               |  23 ++++++-
 brain.db                                | Bin 2351104 -> 2359296 bytes
 brain_resurface.py                      |  61 ++++++++++++++-----
 brain_tensions.py                       |  10 +++-
 brain_weave.py                          |  10 +++-
 main.py                                 | 102 ++++++++++++++++++++++++++++++++
 obsidian_vault/.obsidian/workspace.json |   4 +-
 skills-lock.json                        |  78 ++++++++++++++++++++++++
 sync_daemon.py                          |  31 ++++++++++
 telegram_bot.py                         |  61 ++++++++++++++++++-
 10 files changed, 353 insertions(+), 27 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-8745`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'obsidian_vault/.obsidian/graph.json', 'obsidian_vault/.obsidian/workspace.json', 'obsidian_vault/00_Domini/domain-ai-cognitive-systems.md', 'obsidian_vault/00_Domini/domain-crescita-personale.md', 'obsidian_vault/00_Domini/domain-cultura-storia.md', 'obsidian_vault/00_Domini/domain-design-creativita.md', 'obsidian_vault/00_Domini/domain-filosofia-valori.md', 'obsidian_vault/00_Domini/domain-finanza-economia.md', 'obsidian_vault/00_Domini/domain-medicina-salute.md', 'obsidian_vault/00_Domini/domain-musica-audio.md', 'obsidian_vault/00_Domini/domain-produttivita-sistemi.md', 'obsidian_vault/00_Domini/domain-relazioni-comunicazione.md', 'obsidian_vault/00_Domini/domain-scienza-matematica.md', 'obsidian_vault/00_Domini/domain-software-engineering.md', 'obsidian_vault/00_Domini/person-pierfrancesco.md', 'obsidian_vault/00_INDEX.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-cross-model-provenance-validation.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-cloud-local-symbiosis.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-search-mcp.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-infinite-context-architecture.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-shared-cognitive-state-continuity.md', 'obsidian_vault/01_Progetti_Episodi/analysis-bst-vs-graph-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/antigravity-centaur-collaboration.md', 'obsidian_vault/01_Progetti_Episodi/arch-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/art-creative-writing.md', 'obsidian_vault/01_Progetti_Episodi/art-piano-composition.md', 'obsidian_vault/01_Progetti_Episodi/art-theatre-acting.md', 'obsidian_vault/01_Progetti_Episodi/aule-studio-app.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-engineering.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-surgical.md', 'obsidian_vault/01_Progetti_Episodi/chat-session-2026-08-27-ui-evolution.md', 'obsidian_vault/01_Progetti_Episodi/concept-graph-of-graphs-hypergraph.md', 'obsidian_vault/01_Progetti_Episodi/concept-interhemispheric-inhibition-gating.md', 'obsidian_vault/01_Progetti_Episodi/concept-llm-indirect-injection-safeguard.md', 'obsidian_vault/01_Progetti_Episodi/concept-modular-domain-subgraphs.md', 'obsidian_vault/01_Progetti_Episodi/creative-multidisciplinary.md', 'obsidian_vault/01_Progetti_Episodi/deploy-render-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/ep-20260827-render-cloud-vs-local-hybrid-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-graphrag-mcp-evolution.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-telegram-omnipresence.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-universal-context-definition.md', 'obsidian_vault/01_Progetti_Episodi/episode-cross-model-memory-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-frontend-deeptech-redesign-and-physics-zero-lag.md', 'obsidian_vault/01_Progetti_Episodi/episode-infinite-context-philosophy.md', 'obsidian_vault/01_Progetti_Episodi/episode-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-system-metacognition.md', 'obsidian_vault/01_Progetti_Episodi/feat-progressive-areas.md', 'obsidian_vault/01_Progetti_Episodi/goal-multi-ai-shared-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/intent-clarify-render-cloud-utility-and-llm-web-refusal.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/intent-evaluate-ai-brain-architecture.md', 'obsidian_vault/01_Progetti_Episodi/intent-language-app-ui-design.md', 'obsidian_vault/01_Progetti_Episodi/intent-personal-language-learning-app.md', 'obsidian_vault/01_Progetti_Episodi/lesson-boundaries-clarity.md', 'obsidian_vault/01_Progetti_Episodi/lesson-stoic-resilience.md', 'obsidian_vault/01_Progetti_Episodi/memory-perfectionism-tension.md', 'obsidian_vault/01_Progetti_Episodi/mental-centaur-model.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-dendrogram.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-tree-engine-impl.md', 'obsidian_vault/01_Progetti_Episodi/node-knowledge-graph-memory.md', 'obsidian_vault/01_Progetti_Episodi/node-neuro-symbolic-brain.md', 'obsidian_vault/01_Progetti_Episodi/node-search-tree-deliberation.md', 'obsidian_vault/01_Progetti_Episodi/node-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/node-tree-architecture-verdict.md', 'obsidian_vault/01_Progetti_Episodi/node-ubiquitous-ingestion.md', 'obsidian_vault/01_Progetti_Episodi/node-universal-ai-brain-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/proj-caretrack.md', 'obsidian_vault/01_Progetti_Episodi/proj-cervelloartificiale.md', 'obsidian_vault/01_Progetti_Episodi/proj-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/proj-linkly-qr.md', 'obsidian_vault/01_Progetti_Episodi/proj-streaksup-app.md', 'obsidian_vault/01_Progetti_Episodi/proj-tombolawifi.md', 'obsidian_vault/01_Progetti_Episodi/project-royal-gambit-chess.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/rel-marco-di-martino.md', 'obsidian_vault/01_Progetti_Episodi/rel-napoli-culture.md', 'obsidian_vault/01_Progetti_Episodi/rel-parents.md', 'obsidian_vault/01_Progetti_Episodi/rigore-informativo.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-placeholder.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-particle-fx.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-privacy-zero-cloud.md', 'obsidian_vault/01_Progetti_Episodi/tax-ai-reasoning.md', 'obsidian_vault/01_Progetti_Episodi/universal-ai-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-abbandono-jarvis-nuovo-progetto.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ai-shorts-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allineamento-nodi-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-alternative-income-generation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-analisi-feedback-gemini-ottimizzazione-cervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-architettura-connettoma-web-vs-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-audit-critico-e-mockup-fr-2255.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-avvio-openjarvis-ollama-gpt-cloud.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-backend-optimization-hybrid.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-c-un-problema-vorrei-sapere-di-pi-3203.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8743.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8793.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ore-sono-3134.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-chi-pierfrancesco-amendola-e-cosa-8426.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-clean-clustered-ui.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-cloud-git-auto-push.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-comando-prompt-copia-rapi-8585.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-connect-gemini-claude-chatgpt-mcp.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-repo-jarvis-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-video-showcase-universal-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-esplorazione-paradigmi-visuali-grafo.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-fix-daemon-render-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-infinite-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-integrazione-openjarvis-stanford.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-jarvis-ricordi-quali-sono-gli-emis-3117.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ma-tutto-falso-8462.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-non-riesci-a-connetterti-al-mio-cer-8486.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-nuove-rappresentazioni-vi-2874.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-occultamento-pulsanti-mob-9019.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ottimizzazione-mobile-web-8880.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-potenziamento-skill-e-ril-8338.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-provenance-model-tracking.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-i-progetti-principali-di-8169.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-le-abitudini-monitorate-2979.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-reasoning-and-chat-memory.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ristrutturazione-sigillo-12-macro-domini.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-telegram-bot-gateway.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-tree-search-enhancement.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-universal-ai-hub-client.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-valutazione-progetto-language-app.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-verify-github-token-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-zero-cost-graphrag.md', 'obsidian_vault/01_Progetti_Episodi/ux-frictionless.md', 'obsidian_vault/01_Progetti_Episodi/val-authenticity.md', 'obsidian_vault/01_Progetti_Episodi/val-eternal-cognitive-continuity.md', 'obsidian_vault/01_Progetti_Episodi/val-impact-utility.md', 'obsidian_vault/01_Progetti_Episodi/val-independence.md', 'obsidian_vault/01_Progetti_Episodi/val-transparency-loyalty.md', 'raycast/brain_search.py', 'sync_brain.py', 'apple_shortcuts/Appunto_per_il_Cervello.shortcut', 'obsidian_vault/01_Progetti_Episodi/episode-completamento-supercervello-ecosistema.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/episode-revisione-supercervello-cognitive-os.md', 'obsidian_vault/01_Progetti_Episodi/episode-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-costruzione-collaudo-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-valutazione-architetturale-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/test-e2e-web-clipper.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-implementazione-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-review-piano-supercervello-os.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-test-hook-session-end-2411.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3c40d6e17fd5.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3e8f7aed7312.md', 'obsidian_vault/02_Moduli_Atomici/kindle-6d280a533c87.md', 'obsidian_vault/02_Moduli_Atomici/kindle-7439c883249f.md', 'obsidian_vault/02_Moduli_Atomici/kindle-c962fde43767.md', 'obsidian_vault/02_Moduli_Atomici/kindle-cba1775488ae.md', 'obsidian_vault/02_Moduli_Atomici/node-nota-rapida-raycast-test.md', 'obsidian_vault/02_Moduli_Atomici/node-test-raycast-node.md', 'obsidian_vault/02_Moduli_Atomici/voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2447.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2471.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2485.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2529.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2690.md', 'obsidian_vault/02_Moduli_Atomici/voice-test-shortcuts-debug-7964.md', 'obsidian_vault/02_Moduli_Atomici/web-test-fastapi-docs.md', '2.canvas"'], `diff_stat`: brain.db                                           | Bin 2621440 -> 2621440 bytes
 obsidian_vault/.obsidian/graph.json                |   2 +-
 obsidian_vault/.obsidian/workspace.json            |  75 +++---
 .../00_Domini/domain-ai-cognitive-systems.md       | 127 +++++-----
 .../00_Domini/domain-crescita-personale.md         |   7 +-
 obsidian_vault/00_Domini/domain-cultura-storia.md  |   2 +-
 .../00_Domini/domain-design-creativita.md          |  12 +-
 .../00_Domini/domain-filosofia-valori.md           |  34 +--
 .../00_Domini/domain-finanza-economia.md           |   6 +-
 obsidian_vault/00_Domini/domain-medicina-salute.md |   8 +-
 obsidian_vault/00_Domini/domain-musica-audio.md    |   2 +-
 .../00_Domini/domain-produttivita-sistemi.md       |   4 +-
 .../00_Domini/domain-relazioni-comunicazione.md    |   2 +-
 .../00_Domini/domain-scienza-matematica.md         |   2 +-
 .../00_Domini/domain-software-engineering.md       |  22 +-
 obsidian_vault/00_Domini/person-pierfrancesco.md   | 269 ++++++++++++---------
 obsidian_vault/00_INDEX.md                         |   4 +-
 ...-reasoning-cross-model-provenance-validation.md |  12 +-
 .../ai-reasoning-hybrid-cloud-local-symbiosis.md   |  12 +-
 .../ai-reasoning-hybrid-search-mcp.md              |  10 +-
 .../ai-reasoning-infinite-context-architecture.md  |  14 +-
 ...-reasoning-shared-cognitive-state-continuity.md |   8 +-
 .../analysis-bst-vs-graph-taxonomy.md              |   8 +-
 .../antigravity-centaur-collaboration.md           |   8 +-
 .../arch-telegram-webhook-gateway.md               |   8 +-
 .../01_Progetti_Episodi/art-creative-writing.md    |   6 +-
 .../01_Progetti_Episodi/art-piano-composition.md   |  12 +-
 .../01_Progetti_Episodi/art-theatre-acting.md      |   8 +-
 .../01_Progetti_Episodi/aule-studio-app.md         |   6 +-
 .../01_Progetti_Episodi/brand-voice-engineering.md |   2 +-
 .../01_Progetti_Episodi/brand-voice-surgical.md    |  16 +-
 .../chat-session-2026-08-27-ui-evolution.md        |   8 +-
 .../concept-graph-of-graphs-hypergraph.md          |   4 +-
 .../concept-interhemispheric-inhibition-gating.md  |   4 +-
 .../concept-llm-indirect-injection-safeguard.md    |  10 +-
 .../concept-modular-domain-subgraphs.md            |   6 +-
 .../creative-multidisciplinary.md                  |   4 +-
 .../01_Progetti_Episodi/deploy-render-zero-cost.md |   4 +-
 ...27-render-cloud-vs-local-hybrid-architecture.md |   8 +-
 .../episode-2026-08-27-graphrag-mcp-evolution.md   |  10 +-
 .../episode-2026-08-27-telegram-omnipresence.md    |   8 +-
 ...pisode-2026-08-27-tree-structures-evaluation.md |   6 +-
 ...sode-2026-08-27-universal-context-definition.md |  12 +-
 .../episode-cross-model-memory-architecture.md     |  14 +-
 ...ntend-deeptech-redesign-and-physics-zero-lag.md |   4 +-
 .../episode-infinite-context-philosophy.md         |  14 +-
 .../episode-language-app-architecture.md           |  16 +-
 .../episode-system-metacognition.md                |   6 +-
 .../01_Progetti_Episodi/feat-progressive-areas.md  |   8 +-
 .../goal-multi-ai-shared-context-persistence.md    |  16 +-
 ...ify-render-cloud-utility-and-llm-web-refusal.md |   8 +-
 ...nt-ep-20260827-graph-taxonomy-classification.md |   6 +-
 .../intent-ep-20260827-graph-tree-unification.md   |   6 +-
 ...ep-20260827-hierarchical-overlay-reassurance.md |   6 +-
 ...p-20260827-hierarchical-tree-deployment-sync.md |   6 +-
 .../intent-ep-20260827-telegram-bot-interface.md   |   6 +-
 ...tent-ep-20260827-telegram-cognitive-hub-spec.md |   6 +-
 .../intent-ep-20260827-tree-ranking-translation.md |   6 +-
 ...ntent-ep-20260827-tree-structures-evaluation.md |   6 +-
 .../intent-evaluate-ai-brain-architecture.md       |   6 +-
 .../intent-language-app-ui-design.md               |   4 +-
 .../intent-personal-language-learning-app.md       |  10 +-
 .../lesson-boundaries-clarity.md                   |   8 +-
 .../01_Progetti_Episodi/lesson-stoic-resilience.md |   8 +-
 .../memory-perfectionism-tension.md                |  10 +-
 .../01_Progetti_Episodi/mental-centaur-model.md    |  18 +-
 .../node-hierarchical-dendrogram.md                |  10 +-
 .../node-hierarchical-tree-engine-impl.md          |   8 +-
 .../node-knowledge-graph-memory.md                 |  20 +-
 .../node-neuro-symbolic-brain.md                   |  10 +-
 .../node-search-tree-deliberation.md               |  10 +-
 .../node-telegram-webhook-gateway.md               |   6 +-
 .../node-tree-architecture-verdict.md              |   8 +-
 .../node-ubiquitous-ingestion.md                   |   6 +-
 .../node-universal-ai-brain-taxonomy.md            |   6 +-
 .../01_Progetti_Episodi/proj-caretrack.md          |  14 +-
 .../proj-cervelloartificiale.md                    |  19 +-
 .../proj-jarvis-voice-assistant.md                 |  10 +-
 .../01_Progetti_Episodi/proj-linkly-qr.md          |  10 +-
 .../01_Progetti_Episodi/proj-streaksup-app.md      |  20 +-
 .../01_Progetti_Episodi/proj-tombolawifi.md        |  10 +-
 .../project-royal-gambit-chess.md                  |   4 +-
 ...on-ep-20260827-graph-taxonomy-classification.md |   6 +-
 .../reason-ep-20260827-graph-tree-unification.md   |  10 +-
 ...ep-20260827-hierarchical-overlay-reassurance.md |   4 +-
 ...p-20260827-hierarchical-tree-deployment-sync.md |   6 +-
 .../reason-ep-20260827-telegram-bot-interface.md   |   6 +-
 ...ason-ep-20260827-telegram-cognitive-hub-spec.md |   6 +-
 .../reason-ep-20260827-tree-ranking-translation.md |   6 +-
 ...eason-ep-20260827-tree-structures-evaluation.md |   6 +-
 .../reasoning-language-app-architecture.md         |   8 +-
 .../01_Progetti_Episodi/rel-marco-di-martino.md    |  10 +-
 .../01_Progetti_Episodi/rel-napoli-culture.md      |  12 +-
 obsidian_vault/01_Progetti_Episodi/rel-parents.md  |  12 +-
 .../01_Progetti_Episodi/rigore-informativo.md      |  10 +-
 .../01_Progetti_Episodi/rule-zero-cost.md          |  18 +-
 .../01_Progetti_Episodi/rule-zero-placeholder.md   |  14 +-
 .../01_Progetti_Episodi/streaksup-particle-fx.md   |   4 +-
 .../streaksup-privacy-zero-cloud.md                |   8 +-
 .../01_Progetti_Episodi/tax-ai-reasoning.md        |   8 +-
 .../01_Progetti_Episodi/universal-ai-brain.md      |  90 +++----
 .../user-intent-abbandono-jarvis-nuovo-progetto.md |   4 +-
 .../user-intent-ai-shorts-evaluation.md            |   4 +-
 .../user-intent-allineamento-nodi-render.md        |   4 +-
 ...ent-allora-vorrei-dirti-che-oggi-ho-man-4690.md |   4 +-
 .../user-intent-alternative-income-generation.md   |   4 +-
 ...lisi-feedback-gemini-ottimizzazione-cervello.md |   4 +-
 ...ntent-architettura-connettoma-web-vs-desktop.md |   4 +-
 .../user-intent-audit-critico-e-mockup-fr-2255.md  |   4 +-
 ...ser-intent-avvio-openjarvis-ollama-gpt-cloud.md |   4 +-
 .../user-intent-backend-optimization-hybrid.md     |   4 +-
 ...ntent-c-un-problema-vorrei-sapere-di-pi-3203.md |   4 +-
 ...ent-che-ne-pensi-del-mio-cervello-artif-8743.md |   4 +-
 ...ent-che-ne-pensi-del-mio-cervello-artif-8793.md |   4 +-
 .../user-intent-che-ore-sono-3134.md               |   4 +-
 ...ntent-chi-pierfrancesco-amendola-e-cosa-8426.md |   4 +-
 .../user-intent-clean-clustered-ui.md              |   8 +-
 .../user-intent-cloud-git-auto-push.md             |   4 +-
 .../user-intent-comando-prompt-copia-rapi-8585.md  |   4 +-
 ...ser-intent-connect-gemini-claude-chatgpt-mcp.md |   4 +-
 ...user-intent-creazione-jarvis-voice-assistant.md |   4 +-
 .../user-intent-creazione-repo-jarvis-desktop.md   |   4 +-
 ...ent-creazione-video-showcase-universal-brain.md |   4 +-
 ...tent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md |   4 +-
 ...-intent-esplorazione-paradigmi-visuali-grafo.md |   4 +-
 .../user-intent-fix-daemon-render-persistence.md   |   4 +-
 ...ntent-ho-bisogno-di-sapere-tutto-ci-che-2753.md |   4 +-
 .../user-intent-infinite-context-persistence.md    |  14 +-
 ...user-intent-integrazione-openjarvis-stanford.md |   4 +-
 ...tent-jarvis-ricordi-quali-sono-gli-emis-3117.md |   4 +-
 .../user-intent-ma-tutto-falso-8462.md             |   4 +-
 ...ent-non-riesci-a-connetterti-al-mio-cer-8486.md |   4 +-
 .../user-intent-nuove-rappresentazioni-vi-2874.md  |   4 +-
 .../user-intent-occultamento-pulsanti-mob-9019.md  |   4 +-
 .../user-intent-ottimizzazione-mobile-web-8880.md  |   4 +-
 .../user-intent-potenziamento-skill-e-ril-8338.md  |   4 +-
 .../user-intent-provenance-model-tracking.md       |  12 +-
 ...ent-quali-sono-i-progetti-principali-di-8169.md |   4 +-
 ...tent-quali-sono-le-abitudini-monitorate-2979.md |   4 +-
 ...ent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md |   4 +-
 .../user-intent-reasoning-and-chat-memory.md       |   8 +-
 ...ent-ristrutturazione-sigillo-12-macro-domini.md |   4 +-
 .../user-intent-telegram-bot-gateway.md            |  10 +-
 .../user-intent-tree-search-enhancement.md         |  10 +-
 .../user-intent-universal-ai-hub-client.md         |   4 +-
 ...ser-intent-valutazione-progetto-language-app.md |   4 +-
 .../user-intent-verify-github-token-render.md      |   4 +-
 .../user-intent-zero-cost-graphrag.md              |  10 +-
 .../01_Progetti_Episodi/ux-frictionless.md         |  10 +-
 .../01_Progetti_Episodi/val-authenticity.md        |  14 +-
 .../val-eternal-cognitive-continuity.md            |  14 +-
 .../01_Progetti_Episodi/val-impact-utility.md      |  10 +-
 .../01_Progetti_Episodi/val-independence.md        |   8 +-
 .../val-transparency-loyalty.md                    |  12 +-
 raycast/brain_search.py                            |  43 ++--
 sync_brain.py                                      |  21 +-
 156 files changed, 915 insertions(+), 854 deletions(-)
- **Intento: E2E Test Session Hook** (`user-intent-e2e-test-session-hook-9065`)
  - **Tags:** `#ide-hook` `#session-intent` `#e2e-test-session-hook`
  - **Sintesi:** Obiettivo operativo: E2E Test Session Hook.
  - **Dettagli:** `user_prompt`: E2E Test Session Hook, `modified_files`: ['brain.db', 'obsidian_vault/.obsidian/graph.json', 'obsidian_vault/.obsidian/workspace.json', 'obsidian_vault/00_Domini/domain-ai-cognitive-systems.md', 'obsidian_vault/00_Domini/domain-crescita-personale.md', 'obsidian_vault/00_Domini/domain-cultura-storia.md', 'obsidian_vault/00_Domini/domain-design-creativita.md', 'obsidian_vault/00_Domini/domain-filosofia-valori.md', 'obsidian_vault/00_Domini/domain-finanza-economia.md', 'obsidian_vault/00_Domini/domain-medicina-salute.md', 'obsidian_vault/00_Domini/domain-musica-audio.md', 'obsidian_vault/00_Domini/domain-produttivita-sistemi.md', 'obsidian_vault/00_Domini/domain-relazioni-comunicazione.md', 'obsidian_vault/00_Domini/domain-scienza-matematica.md', 'obsidian_vault/00_Domini/domain-software-engineering.md', 'obsidian_vault/00_Domini/person-pierfrancesco.md', 'obsidian_vault/00_INDEX.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-cross-model-provenance-validation.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-cloud-local-symbiosis.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-hybrid-search-mcp.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-infinite-context-architecture.md', 'obsidian_vault/01_Progetti_Episodi/ai-reasoning-shared-cognitive-state-continuity.md', 'obsidian_vault/01_Progetti_Episodi/analysis-bst-vs-graph-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/antigravity-centaur-collaboration.md', 'obsidian_vault/01_Progetti_Episodi/arch-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/art-creative-writing.md', 'obsidian_vault/01_Progetti_Episodi/art-piano-composition.md', 'obsidian_vault/01_Progetti_Episodi/art-theatre-acting.md', 'obsidian_vault/01_Progetti_Episodi/aule-studio-app.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-engineering.md', 'obsidian_vault/01_Progetti_Episodi/brand-voice-surgical.md', 'obsidian_vault/01_Progetti_Episodi/chat-session-2026-08-27-ui-evolution.md', 'obsidian_vault/01_Progetti_Episodi/concept-graph-of-graphs-hypergraph.md', 'obsidian_vault/01_Progetti_Episodi/concept-interhemispheric-inhibition-gating.md', 'obsidian_vault/01_Progetti_Episodi/concept-llm-indirect-injection-safeguard.md', 'obsidian_vault/01_Progetti_Episodi/concept-modular-domain-subgraphs.md', 'obsidian_vault/01_Progetti_Episodi/creative-multidisciplinary.md', 'obsidian_vault/01_Progetti_Episodi/deploy-render-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/ep-20260827-render-cloud-vs-local-hybrid-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-graphrag-mcp-evolution.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-telegram-omnipresence.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/episode-2026-08-27-universal-context-definition.md', 'obsidian_vault/01_Progetti_Episodi/episode-cross-model-memory-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-frontend-deeptech-redesign-and-physics-zero-lag.md', 'obsidian_vault/01_Progetti_Episodi/episode-infinite-context-philosophy.md', 'obsidian_vault/01_Progetti_Episodi/episode-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/episode-system-metacognition.md', 'obsidian_vault/01_Progetti_Episodi/feat-progressive-areas.md', 'obsidian_vault/01_Progetti_Episodi/goal-multi-ai-shared-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/intent-clarify-render-cloud-utility-and-llm-web-refusal.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/intent-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/intent-evaluate-ai-brain-architecture.md', 'obsidian_vault/01_Progetti_Episodi/intent-language-app-ui-design.md', 'obsidian_vault/01_Progetti_Episodi/intent-personal-language-learning-app.md', 'obsidian_vault/01_Progetti_Episodi/lesson-boundaries-clarity.md', 'obsidian_vault/01_Progetti_Episodi/lesson-stoic-resilience.md', 'obsidian_vault/01_Progetti_Episodi/memory-perfectionism-tension.md', 'obsidian_vault/01_Progetti_Episodi/mental-centaur-model.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-dendrogram.md', 'obsidian_vault/01_Progetti_Episodi/node-hierarchical-tree-engine-impl.md', 'obsidian_vault/01_Progetti_Episodi/node-knowledge-graph-memory.md', 'obsidian_vault/01_Progetti_Episodi/node-neuro-symbolic-brain.md', 'obsidian_vault/01_Progetti_Episodi/node-search-tree-deliberation.md', 'obsidian_vault/01_Progetti_Episodi/node-telegram-webhook-gateway.md', 'obsidian_vault/01_Progetti_Episodi/node-tree-architecture-verdict.md', 'obsidian_vault/01_Progetti_Episodi/node-ubiquitous-ingestion.md', 'obsidian_vault/01_Progetti_Episodi/node-universal-ai-brain-taxonomy.md', 'obsidian_vault/01_Progetti_Episodi/proj-caretrack.md', 'obsidian_vault/01_Progetti_Episodi/proj-cervelloartificiale.md', 'obsidian_vault/01_Progetti_Episodi/proj-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/proj-linkly-qr.md', 'obsidian_vault/01_Progetti_Episodi/proj-streaksup-app.md', 'obsidian_vault/01_Progetti_Episodi/proj-tombolawifi.md', 'obsidian_vault/01_Progetti_Episodi/project-royal-gambit-chess.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-taxonomy-classification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-graph-tree-unification.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-overlay-reassurance.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-hierarchical-tree-deployment-sync.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-bot-interface.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-telegram-cognitive-hub-spec.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-ranking-translation.md', 'obsidian_vault/01_Progetti_Episodi/reason-ep-20260827-tree-structures-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-language-app-architecture.md', 'obsidian_vault/01_Progetti_Episodi/rel-marco-di-martino.md', 'obsidian_vault/01_Progetti_Episodi/rel-napoli-culture.md', 'obsidian_vault/01_Progetti_Episodi/rel-parents.md', 'obsidian_vault/01_Progetti_Episodi/rigore-informativo.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-cost.md', 'obsidian_vault/01_Progetti_Episodi/rule-zero-placeholder.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-particle-fx.md', 'obsidian_vault/01_Progetti_Episodi/streaksup-privacy-zero-cloud.md', 'obsidian_vault/01_Progetti_Episodi/tax-ai-reasoning.md', 'obsidian_vault/01_Progetti_Episodi/universal-ai-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-abbandono-jarvis-nuovo-progetto.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ai-shorts-evaluation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allineamento-nodi-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-alternative-income-generation.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-analisi-feedback-gemini-ottimizzazione-cervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-architettura-connettoma-web-vs-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-audit-critico-e-mockup-fr-2255.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-avvio-openjarvis-ollama-gpt-cloud.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-backend-optimization-hybrid.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-c-un-problema-vorrei-sapere-di-pi-3203.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8743.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ne-pensi-del-mio-cervello-artif-8793.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-che-ore-sono-3134.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-chi-pierfrancesco-amendola-e-cosa-8426.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-clean-clustered-ui.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-cloud-git-auto-push.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-comando-prompt-copia-rapi-8585.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-connect-gemini-claude-chatgpt-mcp.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-jarvis-voice-assistant.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-repo-jarvis-desktop.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-creazione-video-showcase-universal-brain.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-esplorazione-paradigmi-visuali-grafo.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-fix-daemon-render-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-infinite-context-persistence.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-integrazione-openjarvis-stanford.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-jarvis-ricordi-quali-sono-gli-emis-3117.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ma-tutto-falso-8462.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-non-riesci-a-connetterti-al-mio-cer-8486.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-nuove-rappresentazioni-vi-2874.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-occultamento-pulsanti-mob-9019.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ottimizzazione-mobile-web-8880.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-potenziamento-skill-e-ril-8338.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-provenance-model-tracking.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-i-progetti-principali-di-8169.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quali-sono-le-abitudini-monitorate-2979.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-reasoning-and-chat-memory.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-ristrutturazione-sigillo-12-macro-domini.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-telegram-bot-gateway.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-tree-search-enhancement.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-universal-ai-hub-client.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-valutazione-progetto-language-app.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-verify-github-token-render.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-zero-cost-graphrag.md', 'obsidian_vault/01_Progetti_Episodi/ux-frictionless.md', 'obsidian_vault/01_Progetti_Episodi/val-authenticity.md', 'obsidian_vault/01_Progetti_Episodi/val-eternal-cognitive-continuity.md', 'obsidian_vault/01_Progetti_Episodi/val-impact-utility.md', 'obsidian_vault/01_Progetti_Episodi/val-independence.md', 'obsidian_vault/01_Progetti_Episodi/val-transparency-loyalty.md', 'telegram_bot.py', 'apple_shortcuts/Appunto_per_il_Cervello.shortcut', 'obsidian_vault/01_Progetti_Episodi/episode-completamento-supercervello-ecosistema.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/episode-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/episode-revisione-supercervello-cognitive-os.md', 'obsidian_vault/01_Progetti_Episodi/episode-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-costruzione-collaudo-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-test-hook-session-end-2411.md', 'obsidian_vault/01_Progetti_Episodi/reasoning-valutazione-architetturale-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/test-e2e-web-clipper.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2447.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2471.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2485.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2529.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-e2e-test-session-hook-2691.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-implementazione-ecosistema-supercervello.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-review-piano-supercervello-os.md', 'obsidian_vault/01_Progetti_Episodi/user-intent-test-hook-session-end-2411.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3c40d6e17fd5.md', 'obsidian_vault/02_Moduli_Atomici/kindle-3e8f7aed7312.md', 'obsidian_vault/02_Moduli_Atomici/kindle-6d280a533c87.md', 'obsidian_vault/02_Moduli_Atomici/kindle-7439c883249f.md', 'obsidian_vault/02_Moduli_Atomici/kindle-c962fde43767.md', 'obsidian_vault/02_Moduli_Atomici/kindle-cba1775488ae.md', 'obsidian_vault/02_Moduli_Atomici/node-nota-rapida-raycast-test.md', 'obsidian_vault/02_Moduli_Atomici/node-test-raycast-node.md', 'obsidian_vault/02_Moduli_Atomici/voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2447.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2471.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2485.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2529.md', 'obsidian_vault/02_Moduli_Atomici/voice-riflessione-sullantifragilit-nei-sistemi-software-2690.md', 'obsidian_vault/02_Moduli_Atomici/voice-test-shortcuts-debug-7964.md', 'obsidian_vault/02_Moduli_Atomici/web-test-fastapi-docs.md', '2.canvas"'], `diff_stat`: brain.db                                           | Bin 2621440 -> 2621440 bytes
 obsidian_vault/.obsidian/graph.json                |   2 +-
 obsidian_vault/.obsidian/workspace.json            |  75 +++---
 .../00_Domini/domain-ai-cognitive-systems.md       | 127 +++++-----
 .../00_Domini/domain-crescita-personale.md         |   7 +-
 obsidian_vault/00_Domini/domain-cultura-storia.md  |   2 +-
 .../00_Domini/domain-design-creativita.md          |  12 +-
 .../00_Domini/domain-filosofia-valori.md           |  34 +--
 .../00_Domini/domain-finanza-economia.md           |   6 +-
 obsidian_vault/00_Domini/domain-medicina-salute.md |   8 +-
 obsidian_vault/00_Domini/domain-musica-audio.md    |   2 +-
 .../00_Domini/domain-produttivita-sistemi.md       |   4 +-
 .../00_Domini/domain-relazioni-comunicazione.md    |   2 +-
 .../00_Domini/domain-scienza-matematica.md         |   2 +-
 .../00_Domini/domain-software-engineering.md       |  22 +-
 obsidian_vault/00_Domini/person-pierfrancesco.md   | 269 ++++++++++++---------
 obsidian_vault/00_INDEX.md                         |   4 +-
 ...-reasoning-cross-model-provenance-validation.md |  12 +-
 .../ai-reasoning-hybrid-cloud-local-symbiosis.md   |  12 +-
 .../ai-reasoning-hybrid-search-mcp.md              |  10 +-
 .../ai-reasoning-infinite-context-architecture.md  |  14 +-
 ...-reasoning-shared-cognitive-state-continuity.md |   8 +-
 .../analysis-bst-vs-graph-taxonomy.md              |   8 +-
 .../antigravity-centaur-collaboration.md           |   8 +-
 .../arch-telegram-webhook-gateway.md               |   8 +-
 .../01_Progetti_Episodi/art-creative-writing.md    |   6 +-
 .../01_Progetti_Episodi/art-piano-composition.md   |  12 +-
 .../01_Progetti_Episodi/art-theatre-acting.md      |   8 +-
 .../01_Progetti_Episodi/aule-studio-app.md         |   6 +-
 .../01_Progetti_Episodi/brand-voice-engineering.md |   2 +-
 .../01_Progetti_Episodi/brand-voice-surgical.md    |  16 +-
 .../chat-session-2026-08-27-ui-evolution.md        |   8 +-
 .../concept-graph-of-graphs-hypergraph.md          |   4 +-
 .../concept-interhemispheric-inhibition-gating.md  |   4 +-
 .../concept-llm-indirect-injection-safeguard.md    |  10 +-
 .../concept-modular-domain-subgraphs.md            |   6 +-
 .../creative-multidisciplinary.md                  |   4 +-
 .../01_Progetti_Episodi/deploy-render-zero-cost.md |   4 +-
 ...27-render-cloud-vs-local-hybrid-architecture.md |   8 +-
 .../episode-2026-08-27-graphrag-mcp-evolution.md   |  10 +-
 .../episode-2026-08-27-telegram-omnipresence.md    |   8 +-
 ...pisode-2026-08-27-tree-structures-evaluation.md |   6 +-
 ...sode-2026-08-27-universal-context-definition.md |  12 +-
 .../episode-cross-model-memory-architecture.md     |  14 +-
 ...ntend-deeptech-redesign-and-physics-zero-lag.md |   4 +-
 .../episode-infinite-context-philosophy.md         |  14 +-
 .../episode-language-app-architecture.md           |  16 +-
 .../episode-system-metacognition.md                |   6 +-
 .../01_Progetti_Episodi/feat-progressive-areas.md  |   8 +-
 .../goal-multi-ai-shared-context-persistence.md    |  16 +-
 ...ify-render-cloud-utility-and-llm-web-refusal.md |   8 +-
 ...nt-ep-20260827-graph-taxonomy-classification.md |   6 +-
 .../intent-ep-20260827-graph-tree-unification.md   |   6 +-
 ...ep-20260827-hierarchical-overlay-reassurance.md |   6 +-
 ...p-20260827-hierarchical-tree-deployment-sync.md |   6 +-
 .../intent-ep-20260827-telegram-bot-interface.md   |   6 +-
 ...tent-ep-20260827-telegram-cognitive-hub-spec.md |   6 +-
 .../intent-ep-20260827-tree-ranking-translation.md |   6 +-
 ...ntent-ep-20260827-tree-structures-evaluation.md |   6 +-
 .../intent-evaluate-ai-brain-architecture.md       |   6 +-
 .../intent-language-app-ui-design.md               |   4 +-
 .../intent-personal-language-learning-app.md       |  10 +-
 .../lesson-boundaries-clarity.md                   |   8 +-
 .../01_Progetti_Episodi/lesson-stoic-resilience.md |   8 +-
 .../memory-perfectionism-tension.md                |  10 +-
 .../01_Progetti_Episodi/mental-centaur-model.md    |  18 +-
 .../node-hierarchical-dendrogram.md                |  10 +-
 .../node-hierarchical-tree-engine-impl.md          |   8 +-
 .../node-knowledge-graph-memory.md                 |  20 +-
 .../node-neuro-symbolic-brain.md                   |  10 +-
 .../node-search-tree-deliberation.md               |  10 +-
 .../node-telegram-webhook-gateway.md               |   6 +-
 .../node-tree-architecture-verdict.md              |   8 +-
 .../node-ubiquitous-ingestion.md                   |   6 +-
 .../node-universal-ai-brain-taxonomy.md            |   6 +-
 .../01_Progetti_Episodi/proj-caretrack.md          |  14 +-
 .../proj-cervelloartificiale.md                    |  19 +-
 .../proj-jarvis-voice-assistant.md                 |  10 +-
 .../01_Progetti_Episodi/proj-linkly-qr.md          |  10 +-
 .../01_Progetti_Episodi/proj-streaksup-app.md      |  20 +-
 .../01_Progetti_Episodi/proj-tombolawifi.md        |  10 +-
 .../project-royal-gambit-chess.md                  |   4 +-
 ...on-ep-20260827-graph-taxonomy-classification.md |   6 +-
 .../reason-ep-20260827-graph-tree-unification.md   |  10 +-
 ...ep-20260827-hierarchical-overlay-reassurance.md |   4 +-
 ...p-20260827-hierarchical-tree-deployment-sync.md |   6 +-
 .../reason-ep-20260827-telegram-bot-interface.md   |   6 +-
 ...ason-ep-20260827-telegram-cognitive-hub-spec.md |   6 +-
 .../reason-ep-20260827-tree-ranking-translation.md |   6 +-
 ...eason-ep-20260827-tree-structures-evaluation.md |   6 +-
 .../reasoning-language-app-architecture.md         |   8 +-
 .../01_Progetti_Episodi/rel-marco-di-martino.md    |  10 +-
 .../01_Progetti_Episodi/rel-napoli-culture.md      |  12 +-
 obsidian_vault/01_Progetti_Episodi/rel-parents.md  |  12 +-
 .../01_Progetti_Episodi/rigore-informativo.md      |  10 +-
 .../01_Progetti_Episodi/rule-zero-cost.md          |  18 +-
 .../01_Progetti_Episodi/rule-zero-placeholder.md   |  14 +-
 .../01_Progetti_Episodi/streaksup-particle-fx.md   |   4 +-
 .../streaksup-privacy-zero-cloud.md                |   8 +-
 .../01_Progetti_Episodi/tax-ai-reasoning.md        |   8 +-
 .../01_Progetti_Episodi/universal-ai-brain.md      |  90 +++----
 .../user-intent-abbandono-jarvis-nuovo-progetto.md |   4 +-
 .../user-intent-ai-shorts-evaluation.md            |   4 +-
 .../user-intent-allineamento-nodi-render.md        |   4 +-
 ...ent-allora-vorrei-dirti-che-oggi-ho-man-4690.md |   4 +-
 .../user-intent-alternative-income-generation.md   |   4 +-
 ...lisi-feedback-gemini-ottimizzazione-cervello.md |   4 +-
 ...ntent-architettura-connettoma-web-vs-desktop.md |   4 +-
 .../user-intent-audit-critico-e-mockup-fr-2255.md  |   4 +-
 ...ser-intent-avvio-openjarvis-ollama-gpt-cloud.md |   4 +-
 .../user-intent-backend-optimization-hybrid.md     |   4 +-
 ...ntent-c-un-problema-vorrei-sapere-di-pi-3203.md |   4 +-
 ...ent-che-ne-pensi-del-mio-cervello-artif-8743.md |   4 +-
 ...ent-che-ne-pensi-del-mio-cervello-artif-8793.md |   4 +-
 .../user-intent-che-ore-sono-3134.md               |   4 +-
 ...ntent-chi-pierfrancesco-amendola-e-cosa-8426.md |   4 +-
 .../user-intent-clean-clustered-ui.md              |   8 +-
 .../user-intent-cloud-git-auto-push.md             |   4 +-
 .../user-intent-comando-prompt-copia-rapi-8585.md  |   4 +-
 ...ser-intent-connect-gemini-claude-chatgpt-mcp.md |   4 +-
 ...user-intent-creazione-jarvis-voice-assistant.md |   4 +-
 .../user-intent-creazione-repo-jarvis-desktop.md   |   4 +-
 ...ent-creazione-video-showcase-universal-brain.md |   4 +-
 ...tent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176.md |   4 +-
 ...-intent-esplorazione-paradigmi-visuali-grafo.md |   4 +-
 .../user-intent-fix-daemon-render-persistence.md   |   4 +-
 ...ntent-ho-bisogno-di-sapere-tutto-ci-che-2753.md |   4 +-
 .../user-intent-infinite-context-persistence.md    |  14 +-
 ...user-intent-integrazione-openjarvis-stanford.md |   4 +-
 ...tent-jarvis-ricordi-quali-sono-gli-emis-3117.md |   4 +-
 .../user-intent-ma-tutto-falso-8462.md             |   4 +-
 ...ent-non-riesci-a-connetterti-al-mio-cer-8486.md |   4 +-
 .../user-intent-nuove-rappresentazioni-vi-2874.md  |   4 +-
 .../user-intent-occultamento-pulsanti-mob-9019.md  |   4 +-
 .../user-intent-ottimizzazione-mobile-web-8880.md  |   4 +-
 .../user-intent-potenziamento-skill-e-ril-8338.md  |   4 +-
 .../user-intent-provenance-model-tracking.md       |  12 +-
 ...ent-quali-sono-i-progetti-principali-di-8169.md |   4 +-
 ...tent-quali-sono-le-abitudini-monitorate-2979.md |   4 +-
 ...ent-quanti-nodi-ci-sono-nel-mio-cervell-4794.md |   4 +-
 .../user-intent-reasoning-and-chat-memory.md       |   8 +-
 ...ent-ristrutturazione-sigillo-12-macro-domini.md |   4 +-
 .../user-intent-telegram-bot-gateway.md            |  10 +-
 .../user-intent-tree-search-enhancement.md         |  10 +-
 .../user-intent-universal-ai-hub-client.md         |   4 +-
 ...ser-intent-valutazione-progetto-language-app.md |   4 +-
 .../user-intent-verify-github-token-render.md      |   4 +-
 .../user-intent-zero-cost-graphrag.md              |  10 +-
 .../01_Progetti_Episodi/ux-frictionless.md         |  10 +-
 .../01_Progetti_Episodi/val-authenticity.md        |  14 +-
 .../val-eternal-cognitive-continuity.md            |  14 +-
 .../01_Progetti_Episodi/val-impact-utility.md      |  10 +-
 .../01_Progetti_Episodi/val-independence.md        |   8 +-
 .../val-transparency-loyalty.md                    |  12 +-
 telegram_bot.py                                    | 145 ++++++++++-
 155 files changed, 1013 insertions(+), 837 deletions(-)
- **Intento: Fix Demone Sync e Persistenza Render** (`user-intent-fix-daemon-render-persistence`)
  - **Tags:** `#demone` `#sync` `#render` `#persistenza`
  - **Sintesi:** Risolvere il malfunzionamento del demone di sync, prevenire lo spegnimento di Render e garantire persistenza continua dei 347 nodi.
  - **Dettagli:** `context`: Fix demone macOS LaunchAgent, keep-alive Render, persistenza 347 nodi, `user_prompt`: il demone da noi creato per il cervello a volte funziona a volte no, controlla i log per capire. poi ogni tot il nostro sito online si spegne e render deve attivarlo di nuovo non so perchè. prima su render avevo 347 nodi poi ho fatto ricarica la pagina, si è aperta la schermata nera di render che dice connessione in corso stiamo deployando il tuo sistema e ne avevo 335...perchè avevo perso tutta la mia memoria aggiuntiva?? fixa e sistema immediatamente questi problemi. testa e controlla che ttutto sia in regola
- **Intento: Jarvis, ricordi quali sono gli emis...** (`user-intent-jarvis-ricordi-quali-sono-gli-emis-3117`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: Jarvis, ricordi quali sono gli emis...
  - **Dettagli:** `raw`: `user_prompt`: Jarvis, ricordi quali sono gli emisferi del mio connettoma e il loro scopo?, `channel`: JARVIS Voice Core
- **Intento: Nuove rappresentazioni visuali del conne** (`user-intent-nuove-rappresentazioni-vi-2874`)
  - **Tags:** `#user-intent` `#chat` `#nuove-rappresentazioni-visuali-del-connettoma`
  - **Sintesi:** Intento espresso da Pierfrancesco: Nuove rappresentazioni visuali del connettoma
  - **Dettagli:** `user_prompt`: Mostrami altre rappresentazioni per vedere il grafo., `context`: Sessione su Nuove rappresentazioni visuali del connettoma
- **Intento: Occultamento Pulsanti Mobile su Browser ** (`user-intent-occultamento-pulsanti-mob-9019`)
  - **Tags:** `#user-intent` `#chat` `#occultamento-pulsanti-mobile-su-browser-deskt`
  - **Sintesi:** Intento espresso da Pierfrancesco: Occultamento Pulsanti Mobile su Browser Desktop
  - **Dettagli:** `raw`: `user_prompt`: /caveman wenyan-ultra. /graphify /universal-brain devi modificare una cosa. quando apro il sito dal web ora in basso a sinistra mi escono tutti dei pulsanti in bianco, non ci devono essere. quei pulsanti sono grafo, ispettore, albero, ecc..., `context`: Sessione su Occultamento Pulsanti Mobile su Browser Desktop
- **Intento: Ottimizzazione Mobile Web Dashboard Univ** (`user-intent-ottimizzazione-mobile-web-8880`)
  - **Tags:** `#user-intent` `#chat` `#ottimizzazione-mobile-web-dashboard-universal`
  - **Sintesi:** Intento espresso da Pierfrancesco: Ottimizzazione Mobile Web Dashboard Universal Brain
  - **Dettagli:** `raw`: `user_prompt`: /caveman wenyan-ultra. assicurati di rendere la schermata online del sito ottimizzata anche epr mobile. ora devi lavorare solo sulla parte mobile, non cambiare l'interfaccia del sito come si vede sul pc. quando apro il sito sul mio telefono non vedo nulla....o almeno vedo solo il riquadro di destra che compare sul sito quando lo apro dal computer. chiaro??? usa i tag @ meta o viewport non so ma quelli usati per rendere le schermata ottimizzate per i vari dispositivi. /universal-brain /graphify, `context`: Sessione su Ottimizzazione Mobile Web Dashboard Universal Brain
- **Intento: Persistenza Telegram e Keep-Alive Demone** (`user-intent-telegram-keepalive-confirmation`)
  - **Tags:** `#telegram` `#keepalive` `#anti-sleep` `#persistenza`
  - **Sintesi:** Confermare che la persistenza a doppio anello copra Telegram e implementare il keep-alive periodico anti-sleep.
  - **Dettagli:** `context`: Conferma persistenza Telegram e richiesta funzione keep-alive anti-sleep a 14m, `user_prompt`: anche se l'inserimento avviene da telegram?? Conferma: Persistenza a doppio anello attiva. Ogni inserimento da Web, Mobile o Chat locale viene salvato, sincronizzato e committato su GitHub in tempo reale. Zero rischio perdite. ho pensato ad una cosa, affinchè il container di render non si spenga dopo 15 minuti, aggiungiamo una funzione al demone. il demone controlla solo se ci sono differenze tra il db locale e il db di render, cioè quello di github, affinchè il container non si spenga mai, il demone è come se dovesse fare ogni 14 minuti delle fine tirchieste in modo tale che il container si attivi e non si spenga mai, capito che intendo, si può fare?
- **Intento: Potenziamento Skill e Rilascio Demone Si** (`user-intent-potenziamento-skill-e-ril-8338`)
  - **Tags:** `#user-intent` `#chat` `#potenziamento-skill-e-rilascio-demone-sincron`
  - **Sintesi:** Intento espresso da Pierfrancesco: Potenziamento Skill e Rilascio Demone Sincronizzazione macOS
  - **Dettagli:** `raw`: `user_prompt`: /universal-brain procedi con il piano da te implementato, procedi a step, controlla ogni passaggio e prima di andare avanti con il prossimo punto ricontrolla !!, `context`: Sessione su Potenziamento Skill e Rilascio Demone Sincronizzazione macOS
- **Intento: Quali sono i progetti principali di...** (`user-intent-quali-sono-i-progetti-principali-di-8169`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a Groq (qwen/qwen3.8-27b): Quali sono i progetti principali di Pierfrancesco Amendola presenti nella memoria?
  - **Dettagli:** `raw`: `user_prompt`: Quali sono i progetti principali di Pierfrancesco Amendola presenti nella memoria?, `provider`: Groq
- **Intento: Quali sono le abitudini monitorate ...** (`user-intent-quali-sono-le-abitudini-monitorate-2979`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: Quali sono le abitudini monitorate ...
  - **Dettagli:** `raw`: `user_prompt`: Quali sono le abitudini monitorate in StreaksUp?, `channel`: JARVIS Voice Core
- **Intento: Test Hook Session End** (`user-intent-test-hook-session-end-2411`)
  - **Tags:** `#ide-hook` `#session-intent` `#test-hook-session-end`
  - **Sintesi:** Obiettivo operativo: Test Hook Session End.
  - **Dettagli:** `user_prompt`: Test Hook Session End, `modified_files`: ['brain_resurface.py', 'main.py', 'sync_daemon.py', 'telegram_bot.py', 'apple_shortcuts/', 'brain_rem_cycle.py', 'brain_vectors.py', 'export_video_preview.py', 'ide_hooks/', 'kindle_sync.py', 'last_chat_id.txt', 'raycast/', 'static/video_assets/', 'universal_brain_preview.gif', 'video_showcase.html', 'web_clipper/'], `diff_stat`: brain_resurface.py |  52 +++++++++++++++++++--------
 main.py            | 102 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 sync_daemon.py     |  31 ++++++++++++++++
 telegram_bot.py    |  61 ++++++++++++++++++++++++++++++--
 4 files changed, 229 insertions(+), 17 deletions(-)
- **Intento: Verifica GITHUB_TOKEN su Render** (`user-intent-verify-github-token-render`)
  - **Tags:** `#github-token` `#render` `#verifica` `#cloud-push`
  - **Sintesi:** Verificare l'attivazione e il funzionamento del token GitHub su Render per auto-push cloud.
  - **Dettagli:** `context`: Verifica del token GITHUB_TOKEN configurato su Render e test di persistenza cloud, `user_prompt`: ho fatto, ho aggiunto ghp_... al mio enviroment di render, puoi controllare che si andato a buon fine
- **Intento: c'è un problema vorrei sapere di pi...** (`user-intent-c-un-problema-vorrei-sapere-di-pi-3203`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: c'è un problema vorrei sapere di pi...
  - **Dettagli:** `raw`: `user_prompt`: c'è un problema vorrei sapere di più riguardo il mio cervello artificiale quello che ho creato consulta il mio cervello artificiale, `channel`: JARVIS Voice Core
- **Intento: che ne pensi del mio cervello artif...** (`user-intent-che-ne-pensi-del-mio-cervello-artif-8743`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a groq (openai/gpt-oss-120b): che ne pensi del mio cervello artificiale?? c'è qualcosaa che possiamo migliorare
  - **Dettagli:** `raw`: `user_prompt`: che ne pensi del mio cervello artificiale?? c'è qualcosaa che possiamo migliorare, `provider`: groq
- **Intento: che ne pensi del mio cervello artif...** (`user-intent-che-ne-pensi-del-mio-cervello-artif-8793`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a gemini (gemini-3.7-flash): che ne pensi del mio cervello artificiale?? c'è qualcosaa che possiamo migliorare
  - **Dettagli:** `raw`: `user_prompt`: che ne pensi del mio cervello artificiale?? c'è qualcosaa che possiamo migliorare, `provider`: gemini
- **Intento: che ore sono...** (`user-intent-che-ore-sono-3134`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: che ore sono...
  - **Dettagli:** `raw`: `user_prompt`: che ore sono, `channel`: JARVIS Voice Core
- **Intento: chi è Pierfrancesco Amendola e cosa...** (`user-intent-chi-pierfrancesco-amendola-e-cosa-8426`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a groq (openai/gpt-oss-120b): chi è Pierfrancesco Amendola e cosa fa il suo cervello artificiale
  - **Dettagli:** `raw`: `user_prompt`: chi è Pierfrancesco Amendola e cosa fa il suo cervello artificiale, `provider`: groq
- **Intento: ehi Jarvis ehi Jarvis mi puoi dire ...** (`user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: ehi Jarvis ehi Jarvis mi puoi dire ...
  - **Dettagli:** `raw`: `user_prompt`: ehi Jarvis ehi Jarvis mi puoi dire che ore sono?, `channel`: JARVIS Voice Core
- **Intento: ho bisogno di sapere tutto ciò che ...** (`user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: ho bisogno di sapere tutto ciò che ...
  - **Dettagli:** `raw`: `user_prompt`: ho bisogno di sapere tutto ciò che sai sul mio cervello artificiale, `channel`: JARVIS Voice Core
- **Intento: ma è tutto falso!!!** (`user-intent-ma-tutto-falso-8462`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a groq (openai/gpt-oss-120b): ma è tutto falso!!!
  - **Dettagli:** `raw`: `user_prompt`: ma è tutto falso!!!, `provider`: groq
- **Intento: non riesci a connetterti al mio cer...** (`user-intent-non-riesci-a-connetterti-al-mio-cer-8486`)
  - **Tags:** `#universal-hub` `#chat-turn` `#intent`
  - **Sintesi:** Prompt espresso a groq (openai/gpt-oss-120b): non riesci a connetterti al mio cervello?
  - **Dettagli:** `raw`: `user_prompt`: non riesci a connetterti al mio cervello?, `provider`: groq
- **Intento: quanti nodi ci sono nel mio cervell...** (`user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794`)
  - **Tags:** `#jarvis` `#voice-command` `#user-intent`
  - **Sintesi:** Comando vocale/richiesta espresso a JARVIS da Pierfrancesco: quanti nodi ci sono nel mio cervell...
  - **Dettagli:** `raw`: `user_prompt`: quanti nodi ci sono nel mio cervello, voglio saperli per entrambi gli emisferi, `channel`: JARVIS Voice Core
- **Ottimizzazione Backend Ibrida con Backup** (`user-intent-backend-optimization-hybrid`)
  - **Tags:** `#backend` `#performance` `#sqlite` `#optimization` `#safety`
  - **Sintesi:** Richiesta di applicare ottimizzazioni backend (indici, cache, CTE) con approccio ibrido e backup preventivo, senza perdere dati o funzionalità.
  - **Dettagli:** `user_prompt`: voglio l'opzione c, ibrida con backup, non voglio perdere nulla!!! procedi con l'implementazione., `context`: Analisi critica di Gemini su bug (tags, cross_links) e necessità di integrare senza rompere il main.py esistente.
- **Potenziamento Cognitivo del Connettoma e Integrazione Obsidian Vault** (`user-intent-potenziamento-cognitivo-obsidian-bridge`)
  - **Tags:** `#obsidian-vault` `#cognitive-enhancement` `#daily-resurface` `#tensions-matrix` `#weave-link` `#firmware-models`
  - **Sintesi:** Integrazione bidirezionale di Obsidian Vault con note atomiche, rilevatore tensioni cognitive, weave link engine per nodi orfani, daily resurface spaced repetition e 9 firmware mentali.
  - **Dettagli:** `context`: Richiesta di potenziare Universal AI Brain superando le feature di Neomas con Obsidian Vault, Daily Resurface, Tensioni, Weave Link e 9 Firmware mentali., `user_prompt`: continua il lavoro che stavamo facendo, continua il lavoro del piano d'implementazione chiaro???
- **Potenziamento Grafico Mappamondo 3D & Relazioni Sinaptiche** (`user-intent-mappamondo-3d-spotlight-relazioni`)
  - **Tags:** `#3d-globe` `#webgl` `#threejs` `#spotlight` `#relationships`
  - **Sintesi:** Richiesta di trasformazione visiva del Mappamondo 3D con spotlight interattivo delle relazioni, gabbia olografica e card sinaptica floating.
  - **Dettagli:** `priority`: HIGH, `theme`: 3d-webgl-generative-ui
- **Preferenze Pierfrancesco Grafica Scacchi Duolingo** (`user-intent-duolingo-chess-preference`)
  - **Tags:** `#pierfrancesco` `#preferenze` `#duolingo` `#scacchi` `#ui-ux`
  - **Sintesi:** Pierfrancesco richiede massima fedeltà visiva allo stile Duolingo Chess: scacchiera menta e bianco, pezzi 2D piatti vettoriali con gerarchia scalare, pulsanti 3D tattili e mascotte Duo interattiva.
- **Prevenzione Perdita Contesto per Saturazione Finestra Chat** (`user-intent-infinite-context-persistence`)
  - **Tags:** `#user-intent` `#context-preservation` `#infinite-memory` `#chat-saturation` `#zero-loss` `#cross-session`
  - **Sintesi:** Volontà utente: azzerare la perdita di contesto causata dalla saturazione delle finestre di contesto degli LLM, garantendo continuità cognitiva perenne tra chat diverse.
  - **Dettagli:** `raw`: `core_vision`: Memoria eterna, coerente e non volatile per passato, presente e futuro., `problem_solved`: Saturazione della context window e perdita della cronologia decisionale nei cambi di sessione., `user_prompt`: lo scopo è che venga salvato il contesto e memorizzato il contesto delle chat con le ai in modo tale che si sa sempre cosa è stato detto, pensato, eccc...quante volte magari si deve cambiare chat perchè alcuni modelli saturano il contesto di una chat e si deve ricominciare da zero, come si fa??? si eprde tutto?? no quindi lo scopo è quello, non perdere mai il contesto e avere sempre memoria, per il passato, presente e futuro.
- **Progettazione Ecosistema & Integrazioni Future del Supercervello** (`user-intent-espansione-supercervello-integrazioni`)
  - **Tags:** `#ecosistema` `#architettura` `#integrazioni` `#obsidian` `#automazioni` `#supercervello`
  - **Sintesi:** Identificazione delle migliori applicazioni, sistemi, flussi e potenziamenti architetturali per estendere il connettoma oltre Obsidian e massimizzarne l'efficacia operativa.
  - **Dettagli:** `context`: Evoluzione del connettoma bi-emisferico verso un Cognitive OS onnipresente, `user_prompt`: abbiamo collegato obsidian al nostro cervello e abbiamo creato questo supercervello. ma che altro possiamo fare per migliorare, quali altri applicazioni, sistemi possiamo sfruttare per miglioare e rendere tutto più efficace e migliore
- **Revisione Piano Supercervello Ubiquitous Cognitive OS** (`user-intent-review-piano-supercervello-os`)
  - **Tags:** `#piano-implementazione` `#supercervello` `#architettura` `#zero-cost` `#knowledge-graph`
  - **Sintesi:** Richiesta di revisione strategica ed ingegneristica del piano di estensione del cervello artificiale in un Cognitive OS ubiquo a costo zero.
  - **Dettagli:** `context`: Estensione del Connettoma Cognitivo Bi-Emisferico con Raycast, Web Clipper, Siri, Fase REM, FastEmbed e IDE hooks a costo zero., `user_prompt`: che ne pensi di questo piano d'implementazione per rendere il cervello che ho creato una superpotenza?? [Piano Supercervello Ubiquitous Cognitive OS]
- **Richiesta Creazione Video Showcase 60s Universal Brain** (`user-intent-creazione-video-showcase-universal-brain`)
  - **Tags:** `#video` `#showcase` `#social-media` `#tutorial` `#universal-brain`
  - **Sintesi:** Richiesta di Pierfrancesco di creare un video tutorial / anteprima di 1 minuto con screenshot, pezzi di codice e spiegazione del Cervello Artificiale per la condivisione social.
  - **Dettagli:** `context`: Creazione di un video showcase/anteprima di 1 minuto, con screenshot, codice, animazioni e kit social per presentare il Cervello Artificiale /universal-brain., `user_prompt`: potresti crearmi un video tutorial, anteprima, un piccolo video di un minuto che spiega tramite scrrenshot presi da internt del mio cervello e tutto, anche con pezzi di codice, il mio cervello artificiale?? /universal-brain così da poterlo postare e far vedere a tutti, presentare un pò il mio cervello,
- **Richiesta Metodi Alternativi di Guadagno** (`user-intent-alternative-income-generation`)
  - **Tags:** `#monetizzazione` `#side-hustle` `#business-models` `#proposte-alternative`
  - **Sintesi:** L'utente richiede la formulazione di strategie alternative e concrete per generare tra 100 e 500 euro/mese a costo zero iniziale.
  - **Dettagli:** `user_prompt`: allora propronimi un altro metodo perfavore, `context`: Transizione da modelli basati sulla viralità passiva a modelli ad alto valore aggiunto basati su sviluppo software e asset digitali.
- **Richiesta Spiegazione Swin Transformer e Deep Stable Learning** (`user-intent-spiegazione-swin-transformer-deep-stable-learning`)
  - **Tags:** `#tesi` `#breast-cancer` `#deep-learning` `#swin-transformer` `#stable-learning`
  - **Sintesi:** Richiesta di spiegazione breve, tecnica ed efficace su Swin Transformer e Deep Stable Learning nel contesto della classificazione del cancro al seno.
  - **Dettagli:** `user_prompt`: puoi spiegarmi in modo breve, conciso ed efficace cosa è un Swim Transformers cos'è una o cosa fa la Deep Stable Learning. Sono concetti della mia tesi sulla classificazione tramite deep Learning di immagini di cancro al seno, `context`: Tesi di laurea sulla classificazione di immagini di cancro al seno tramite tecniche avanzate di Deep Learning.
- **Richiesta Utente: Abbandono Jarvis e Avvio Nuovo Progetto** (`user-intent-abbandono-jarvis-nuovo-progetto`)
  - **Tags:** `#abbandono-jarvis` `#pivot` `#nuovo-progetto` `#semplicità`
  - **Sintesi:** Pierfrancesco ordina la cancellazione di Jarvis/OpenJarvis e l'orientamento verso un progetto più pragmatico e funzionale.
  - **Dettagli:** `raw`: `action`: Cancellazione totale di Desktop/Jarvis e Desktop/OpenJarvis. Svolta verso nuovo progetto più semplice, realistico e funzionale., `user_prompt`: purtropo jarvis e i progetti a loro associati non vanno bene cancelliamo tutto e abbandoniamo il progetto jarvis per il momento, ora pensiamo ad un altro progetto, più semplice, realistico, e forse funzionale!!!!
- **Richiesta Utente: Aree e Disvelamento Progressivo dei Nodi** (`user-intent-clean-clustered-ui`)
  - **Tags:** `#user-request` `#cleanliness` `#hierarchical-view` `#progressive-disclosure`
  - **Sintesi:** Richiesta di organizzare il grafo in macro-aree pulite, con espansione dei sotto-nodi al click e conservazione tematica indipendente delle chat.
  - **Dettagli:** `raw`: `user`: Pierfrancesco Amendola, `priority`: HIGH, `aesthetic_goal`: Eliminare il disordine visivo preservando 100% le relazioni, `user_prompt`: Richiesta di organizzare il grafo in macro-aree pulite, con espansione dei sotto-nodi al click e conservazione tematica indipendente delle chat.
- **Richiesta Utente: Avvio OpenJarvis con Ollama gpt-oss:120b-cloud** (`user-intent-avvio-openjarvis-ollama-gpt-cloud`)
  - **Tags:** `#openjarvis` `#ollama` `#gpt-oss` `#test-riuscito`
  - **Sintesi:** Test di esecuzione su OpenJarvis con Ollama gpt-oss:120b-cloud e recupero dal connettoma neurale.
  - **Dettagli:** `raw`: `action`: Avvio di OpenJarvis con modello Ollama gpt-oss:120b-cloud e verifica risposta con memoria, `user_query`: Chi è Pierfrancesco?, `user_prompt`: Test di esecuzione su OpenJarvis con Ollama gpt-oss:120b-cloud e recupero dal connettoma neurale.
- **Richiesta Utente: Clonazione e Integrazione OpenJarvis Stanford** (`user-intent-integrazione-openjarvis-stanford`)
  - **Tags:** `#openjarvis` `#stanford` `#desktop-app` `#integrazione`
  - **Sintesi:** Pierfrancesco richiede di clonare OpenJarvis sul Desktop e connetterlo al proprio Cervello Artificiale sfruttando anche la desktop app.
  - **Dettagli:** `raw`: `action`: Clonazione di OpenJarvis sul Desktop e collegamento diretto al Universal AI Brain, `repo`: https://github.com/open-jarvis/OpenJarvis, `user_prompt`: Pierfrancesco richiede di clonare OpenJarvis sul Desktop e connetterlo al proprio Cervello Artificiale sfruttando anche la desktop app.
- **Richiesta Utente: Creazione Progetto Autonomo JARVIS su Desktop** (`user-intent-creazione-repo-jarvis-desktop`)
  - **Tags:** `#jarvis` `#desktop-project` `#separazione-moduli` `#connettoma`
  - **Sintesi:** Pierfrancesco stabilisce che JARVIS deve essere un progetto separato su /Users/pierfrancesco/Desktop/Jarvis, utilizzando Universal AI Brain come memoria esterna.
  - **Dettagli:** `raw`: `context`: Creazione repository autonoma /Users/pierfrancesco/Desktop/Jarvis separata da CervelloArtificiale ma collegata ad esso per la memoria a lungo termine., `user_prompt`: il progetto jarvis dovrebbe essere un nuovo progetto in una nuova cartella sul desktop. non deve entrare nel progetto CervelloArtificiale. userà come memoria quella del mio cervello aritificiale. dopo queste premesse partiamo con la creazione di jarvis.
- **Richiesta Utente: Funzionamento Architettura Web vs Desktop e Sincronizzazione Master Prompt** (`user-intent-architettura-connettoma-web-vs-desktop`)
  - **Tags:** `#architettura` `#web-vs-desktop` `#master-prompt` `#sincronizzazione` `#continuità`
  - **Sintesi:** Pierfrancesco chiede chiarimenti sul funzionamento reale dell'albero gerarchico e palazzo cognitivo su backend, come le AI Web accedono alle info rispetto alle AI desktop, e allineamento del pulsante Copia Prompt con sincronizzazione continua.
  - **Dettagli:** `raw`: `context`: Chiarimento architetturale su SQLite FTS5, MCP, OpenAPI Actions, endpoint dinamici su Render e master prompt, `user_prompt`: noi nel nostro progetto abbiamo realizzato tante cose... come sa l'ai sul web che esistono questi sistemi? ... se io ora sul web faccio copia prompt mi esce quello che tu ora hai creato o quello che c'era?? hai sincronizzato?? inoltre stai caricando tutte le risposte e interazioni che stiamo avendo /universal-brain
- **Richiesta Utente: Hub AI Unificato con Connettoma Permanente** (`user-intent-universal-ai-hub-client`)
  - **Tags:** `#ai-hub` `#universal-client` `#chat-ui` `#connettoma` `#grill-me`
  - **Sintesi:** Pierfrancesco intende costruire un client desktop/web unico che unifica tutti i provider AI (OpenAI, Claude, DeepSeek, Gemini, Ollama) con memoria universale automatica a costo zero.
  - **Dettagli:** `raw`: `action`: Creazione di una web/desktop app unificata (stile ChatGPT/Claude/DeepSeek) con memoria bi-emisferica fissa e provider multipli gratuiti., `user_prompt`: voglio creare un interfaccia desktop uguale a chatgpt, claude, deepseek, e quant'altro che ha come skill fissa a prescindere da tutto, senza da dover inserire ogni volta, /universal-brain. c'è una barra dove inseriamo la nostra richiesta, poi un pulsante per scegliere il provider ai... tutto gratis!
- **Richiesta Utente: Memoria dei Ragionamenti AI e delle Chat Eterogenee** (`user-intent-reasoning-and-chat-memory`)
  - **Tags:** `#user-request` `#ai-reasoning` `#chat-memory` `#multi-topic`
  - **Sintesi:** Richiesta di tracciare le domande utente, le deduzioni interne dell'AI e raggruppare chat su argomenti diversi (es. sport, cucina, codice) in aree separate.
  - **Dettagli:** `raw`: `user`: Pierfrancesco Amendola, `goal`: Mappare ogni sessione senza forzare connessioni artificiali tra argomenti disomogenei, `user_prompt`: Richiesta di tracciare le domande utente, le deduzioni interne dell'AI e raggruppare chat su argomenti diversi (es. sport, cucina, codice) in aree separate.
- **Richiesta Utente: Progettazione Assistente Vocale JARVIS Personale 100% Gratuito** (`user-intent-creazione-jarvis-voice-assistant`)
  - **Tags:** `#jarvis` `#voice-assistant` `#zero-cost` `#graphrag` `#openwake-word`
  - **Sintesi:** Pierfrancesco richiede la progettazione di un assistente vocale continuo JARVIS a costo zero, con wake word, memoria persistente bi-emisferica e visualizzazione a grafo HUD stile Iron Man.
  - **Dettagli:** `raw`: `context`: Creazione assistente vocale tipo Iron Man a costo zero (0€), con wake word, LLM gratuiti, TTS neurale, collegato al Persistent Knowledge Graph., `user_prompt`: ho intenzione di creare JARVIS come quello di IronMan... assistente personale vocale, collegato al mio cervello... gratis sia realizzazione che chiamate API
- **Richiesta Utente: Restyling Professionale e Moderno Frontend** (`user-intent-frontend-professional-restyle`)
  - **Tags:** `#user-request` `#ui-ux` `#professional-look` `#hacker-aesthetic` `#graphify-inspiration`
  - **Sintesi:** Richiesta di rendere l'interfaccia frontend più moderna, pulita e da ingegnere informatico (ispirata a Graphify e Caveman), senza perdere alcuna funzione esistente.
  - **Dettagli:** `raw`: `user`: Pierfrancesco Amendola, `preservation`: 100% zero feature loss, `user_prompt`: Restyling estetico completo del frontend in stile ingegneristico d'élite: Topbar IDE unificata a tutta larghezza con HUD sinaptico, canvas con dot-matrix grid, ispettore Bento con badge epistemici e ricerca ⌘K, conservando il 100% delle funzionalità.
- **Richiesta: Esplorazione Nuovi Paradigmi Visuali e Layout per il Grafo** (`user-intent-esplorazione-paradigmi-visuali-grafo`)
  - **Tags:** `#ui-design` `#visual-paradigms` `#graph-visualization` `#interfaccia`
  - **Sintesi:** Richiesta utente di visualizzare nuovi disegni, interfacce e layout architetturali per rappresentare il connettoma neurale (307 nodi, 2 emisferi).
  - **Dettagli:** `context`: Richiesta di vedere nuovi layout, disegni e stili d'interfaccia per il grafo a due emisferi, `user_prompt`: adesso abbiamo avuto un miglioramento e potenziamento??? ora voglio vedere altri esempi di rappresentare il nostro grafo, voglio vedere altri modi, altri 'disegni', deve rimanere così, ma voglio che cambi l'interfaccia chapito che intendo?
- **Rimozione Modello Ollama Residuo su macOS** (`user-intent-rimozione-modello-ollama-mac`)
  - **Tags:** `#macos` `#ollama` `#storage` `#cleanup` `#terminale`
  - **Sintesi:** Richiesta di individuazione ed eliminazione completa di un modello LLM da 7GB rimasto su disco dopo la disinstallazione di Ollama.
  - **Dettagli:** `user_prompt`: ho scaricato Ollama, e mentre ero sul terminale involontariamente ho installato un modello di intelligenza artificiale di 7GB sul mio Mac. ora ho disitintallato Ollama, ma il modello di intelligenza artificiale ora è, teoricamente, ancora sul mio Mac...dove lo trovo?? come lo elimino?? non voglio che ci sia, `context`: macOS; l'utente ha già rimosso l'eseguibile/app Ollama ma necessita di ripulire i file binari pesanti (~/.ollama).
- **Ristrutturazione e Sigillatura dei 12 Macro-Domini Fondativi** (`user-intent-ristrutturazione-sigillo-12-macro-domini`)
  - **Tags:** `#macro-domini` `#palazzo-cognitivo` `#gerarchia` `#sigillo-piano-0`
  - **Sintesi:** Riorganizzazione gerarchica del connettoma: sigillatura del Piano 0 con 12 macro-domini canonici, riassegnazione di tutti i nodi orfani e divieto di creazione dinamica per le AI esterne.
  - **Dettagli:** `context`: Chiusura della tassonomia di Piano 0 e ri-parenting semantico a costo zero e zero perdita dati, `user_prompt`: si assolutamente ristruttura così. però non voglio eprdere i nodi o i loro contenuti dobbiamo solo riorganizzarre. salva tutto il contesto nel cervello mi raccomando !!!
- **Spiegazione Ecografi con Trasduttore Lineare** (`user-intent-definizione-ecografo-trasduttore-lineare`)
  - **Tags:** `#ecografia` `#hardware-medico` `#trasduttore-lineare` `#breast-imaging` `#ultrasound`
  - **Sintesi:** Richiesta di definizione, caratteristiche e campi d'uso degli ecografi con trasduttore lineare.
  - **Dettagli:** `user_prompt`: cosa sono gli ecografi con trasduttore lineare, `context`: Comprensione del dominio di acquisizione immagini ecografiche mammarie per la tesi di laurea.
- **Spiegazione Semplificata Self-Attention e Concetti Causali** (`user-intent-spiegazione-intuitiva-concetti-causali-attention`)
  - **Tags:** `#didattica` `#self-attention` `#causal-inference` `#confounders` `#decorrelation`
  - **Sintesi:** Richiesta di chiarimento divulgativo e intuitivo sui concetti cardine di self-attention, inferenza causale, confounders e decorrelazione delle feature.
  - **Dettagli:** `user_prompt`: mi spieghi cosa 'è la self attention, inferenza causale, decorrelazione delle feature, feature confounders. però in modo semplice, `context`: Necessità di comprensione concettuale e intuitiva dei pilastri matematico-statistici della tesi.
- **Tracciamento Richiesta Utente & Modello AI nella Memoria** (`user-intent-provenance-model-tracking`)
  - **Tags:** `#user-intent` `#model-attribution` `#context-preservation` `#cross-model-memory` `#episodic-tracking`
  - **Sintesi:** Proposta utente: includere nel JSON di ingestione il prompt integrale e il modello AI sorgente per preservare contesto e consentire recall cross-modello.
  - **Dettagli:** `raw`: `user_prompt`: quando l'ai dovrà restituire il json da inviare tramite post, dobbiamo inserire la richiesta dell'utente così da avere contesto, e inserire anche il modello che ha risposto..., `objective`: Consentire a modelli futuri (Claude, GPT, Gemini) di richiamare conversazioni con attribuzione esatta., `target_fields`: ['user_intent', 'model_name', 'timestamp', 'conversation_episode']
- **Valutazione Fattibilità Language App Gratuita e Unica** (`user-intent-valutazione-progetto-language-app`)
  - **Tags:** `#language-learning` `#feasibility` `#planning`
  - **Sintesi:** Richiesta di parere critico, stima complessità/tempi e identificazione elementi mancanti nel progetto di app lingue personale.
  - **Dettagli:** `raw`: `context`: Valutazione fattibilità, tempi, complessità e gap del piano per language app personale gratuita, `user_prompt`: /universal-brain /caveman, che ne pensi del creare un app per imparare le lingue in modo gratis e unico, ne parlavo prima con gemini, mi aveva fatto un progetto, tu cosa ne pensi, quanto complesso può essere?? quanto ci mettiamo a realizzarlo?? ha mancato qualcosa??
- **Valutazione Monetizzazione YT Shorts AI** (`user-intent-ai-shorts-evaluation`)
  - **Tags:** `#monetizzazione` `#youtube` `#ai-video` `#side-hustle`
  - **Sintesi:** L'utente richiede un'analisi di fattibilità per generare 100-500 euro/mese creando YouTube Shorts per bambini generati tramite AI su piattaforme freemium/terze.
  - **Dettagli:** `user_prompt`: mi hanno consigliato per guadagnare soldi un metodo con l'ai però non so se sia fattibile o meno. dicono che è a costo zero all'inizio poi se voglio diventare più esperto, migliore e avere più possibilità bisogna pagare. si tratta di fare i video shorts su yt tramite huggsfield o altre piattaforme così, e caricarli su yt. come argomento loro dicono i video per bambini perchè sono quelli che vanno più virali ecc...tu cosa ne pensi, effettivamente quanto è saturo il mercato?? riuscirò a fare qualche cosa di soldi?? non chiedo migliaia di euro a me basterebbero anche dai 100 ai 500 euro al mese. fammi sapere, `context`: Valutazione critica di un modello di business virale, saturazione del mercato video AI per bambini, policy COPPA e calcolo metriche RPM reali.
- **Valutazione e Ottimizzazione Architettura Knowledge Graph** (`intent-evaluate-ai-brain-architecture`)
  - **Tags:** `#metacognition` `#system-design` `#graph-database` `#prompt-engineering`
  - **Sintesi:** L'utente richiede un'analisi critica dell'architettura del proprio cervello artificiale, cercando lacune, migliorie strutturali e ottimizzazioni del prompt.
  - **Dettagli:** `raw`: `focus_areas`: ['Architecture', 'Prompt', 'Missing Features'], `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Verifica Distribuzioni Linux e Software di Modellazione 3D** (`user-intent-distro-linux-modellazione-3d`)
  - **Tags:** `#linux` `#3d-modeling` `#software` `#distribuzioni` `#open-source`
  - **Sintesi:** Richiesta di informazioni sull'esistenza di distribuzioni Linux per scaricare e utilizzare software di modellazione 3D.
  - **Dettagli:** `user_prompt`: Esistono distribuzioni Linux che permettono di scaricare software di modellazione 3D?, `context`: Analisi dell'ecosistema open source e professionale per la computer grafica 3D su ambiente Linux.
- **Verifica del Vincolo Architetturale Zero-Cost (0,00€)** (`user-intent-verifica-vincolo-zero-costi`)
  - **Tags:** `#zero-cost` `#budget` `#architettura` `#sostenibilità` `#open-source`
  - **Sintesi:** Controllo rigoroso della gratuità totale (0,00€) di tutte le estensioni, integrazioni, strumenti e modelli proposti per il connettoma.
  - **Dettagli:** `context`: Verifica del rispetto del vincolo fondativo: 100% Zero-Cost Architecture (0,00€ Forever), `user_prompt`: trasformare tutto questo è gratis??? hai rispettato la condizione che sia tutto gratis?


## EMISFERO DESTRO (Design, Emozioni, Relazioni, Valori, Arte)
### [Macro-Label: `APP`]
- **App Flash Cards** (`proj-appflashcards`)
  - **Tags:** `#mac-project` `#swift`
  - **Sintesi:** App iOS nativa per studiare con flashcard.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppFlashCards, `file_uri`: file:///Users/pierfrancesco/Desktop/AppFlashCards, `languages`: ['Swift'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 86, `last_modified`: 2026-01-15T12:45:37.751785+00:00, `key_dependencies`: [], `readme_excerpt`: # Ripassa! - Flashcard App

App iOS nativa per studiare con flashcard.

## Caratteristiche

- ✅ Aggiungi domande e risposte
- ✅ Swipe per navigare tra le carte
- ✅ Tap per vedere la risposta con animazione flip 3D
- ✅ Modalità casuale per lo studio
- ✅ Contatore delle carte studiate
- ✅ Statistiche dettagliate
- ✅ Dark mode automatico
- ✅ 100% offline

## Tecnologie

- Swift 5.9+
- SwiftUI
- iOS 16.0+
- UserDefaults per persistenza

## Come Aprire il Progetto

1. Apri `Ripassa.xcodeproj` con Xcode
2. Seleziona un simulatore iOS o device
3. Premi ⌘R per build e run

## Struttura del Progetto

`
- **App Scadenza** (`proj-appscadenza`)
  - **Tags:** `#c` `#c-lang` `#mac-project` `#react` `#swift` `#typescript`
  - **Sintesi:** **Traccia le scadenze. Riduci gli sprechi. Risparmia.**
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppScadenza, `file_uri`: file:///Users/pierfrancesco/Desktop/AppScadenza, `languages`: ['C', 'Swift', 'TypeScript'], `frameworks`: ['React'], `has_git`: False, `relevant_files_count`: 32, `last_modified`: 2026-01-20T22:17:39.717717+00:00, `key_dependencies`: ['@react-native-async-storage/async-storage', '@react-native-community/datetimepicker', 'expo', 'expo-barcode-scanner', 'expo-camera', 'expo-notifications', 'expo-splash-screen', 'expo-status-bar', 'lucide-react-native', 'react', 'react-native', 'react-native-gesture-handler', 'react-native-reanimated', '@types/react', 'typescript'], `readme_excerpt`: # 🌱 FreshCheck

**Traccia le scadenze. Riduci gli sprechi. Risparmia.**

FreshCheck è un'app mobile minimalista per iOS e Android che ti aiuta a gestire le scadenze dei tuoi prodotti alimentari, riducendo gli sprechi e risparmiando denaro.

<p align="center">
  <img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React Native"/>
  <img src="https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white" alt="Expo"/>
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&l

### [Macro-Label: `ARCHITECTURE`]
- **Nota Rapida Raycast Test** (`node-nota-rapida-raycast-test`)
  - **Tags:** `#raycast-quick-add` `#right` `#software-engineering`
  - **Sintesi:** Verifica esecuzione diretta
  - **Dettagli:** `source`: raycast_quick_add, `created_by`: Pierfrancesco Amendola

### [Macro-Label: `BRAND_VOICE`]
- **Dominio: Cultura, Storia & Linguaggi** (`domain-cultura-storia`)
  - **Tags:** `#domain-hub` `#cultura` `#storia` `#lingue` `#letteratura` `#viaggi` `#antropologia`
  - **Sintesi:** Storia, Letteratura, Lingue Straniere, Cultura Generale, Viaggi, Società e Antropologia.
  - **Dettagli:** `scope`: Culture, world history, foreign languages, anthropology, literature
- **Terse Caveman Communication Persona** (`terse-caveman-brand-voice`)
  - **Tags:** `#brand-voice` `#smart-caveman` `#ultra-terse` `#no-fluff` `#pure-signal`
  - **Sintesi:** Voce di brand ultra-compressa e ad altissima densità informativa: cadono preamboli, fronzoli e convenevoli; resta la pura verità tecnica.
  - **Dettagli:** `raw`: `principle`: All technical substance stay. Only fluff die., `style`: Smart Caveman / Wenyan-Ultra
- **Ultra-Direct Engineering Voice** (`brand-voice-engineering`)
  - **Tags:** `#communication` `#caveman-protocol` `#technical-density`
  - **Sintesi:** Modalità comunicativa asciutta, rigorosa, priva di convenevoli e orientata alla massima densità tecnica.
  - **Dettagli:** `raw`: `tone`: Direct, surgical, authoritative, `protocol`: Zero pleasantries, high token-efficiency
- **Voce Chirurgica & Protocollo Caveman** (`brand-voice-surgical`)
  - **Tags:** `#high-density` `#no-fluff` `#direct` `#engineering-tone`
  - **Sintesi:** Comunicazione priva di convenevoli, chirurgica, diretta e con la massima densità concettuale per token.
  - **Dettagli:** `raw`: `style`: Tecnico, asciutto, analitico, orientato all'azione

### [Macro-Label: `COLOR_PALETTE`]
- **Cyan & Magenta Polarity Palette** (`bi-hemispheric-polarity-palette`)
  - **Tags:** `#00d2ff` `#ff007f` `#a855f7` `#neon` `#bipolar` `#synapse-glow`
  - **Sintesi:** Schema cromatico bipolare: Ciano Neon (#00D2FF) per il rigore razionale sinistro, Magenta Neon (#FF007F) per la creatività destra, Viola (#A855F7) per il ponte calloso.
  - **Dettagli:** `raw`: `left_logic`: #00D2FF, `right_creative`: #FF007F, `corpus_callosum`: #A855F7, `glow_opacity`: 0.45
- **Cyber Accent Color Palette** (`palette-neon-cyber`)
  - **Tags:** `#colors` `#cyan` `#magenta` `#contrast`
  - **Sintesi:** Insieme di colori primari e secondari ad alto impatto cromatico per feedback e interazione (#00D2FF, #FF007F, #7928CA, #00E676).
  - **Dettagli:** `raw`: `primary_cyan`: #00D2FF, `secondary_pink`: #FF007F, `electric_purple`: #7928CA, `status_success`: #00E676
- **Flame & Freeze Bipolar Palette** (`streaksup-flame-palette`)
  - **Tags:** `#palette` `#flame-gradient` `#freeze-cyan` `#trophy-colors`
  - **Sintesi:** Palette istituzionale centrata sul gradiente Fiamma (#FFE066 -> #FF8C00 -> #FF3B30), Ciano Streak Freeze (#00C7BE) e Verde Successo (#34C759).
  - **Dettagli:** `raw`: `flame_gradient`: ['#FFE066', '#FF8C00', '#FF3B30'], `freeze_cyan`: #00C7BE, `success_green`: #34C759, `urgent_red`: #FF3B30, `electric_blue`: #007AFF

### [Macro-Label: `CONVERSATION_EPISODE`]
- **Allineamento Nodi Locale vs Render Cloud e Sincronizzazione Deploy** (`episode-allineamento-nodi-render-cloud`)
  - **Tags:** `#episodio-chat` `#render-sync` `#cloud-deploy` `#pierfrancesco`
  - **Sintesi:** Sessione di verifica e sincronizzazione dei nodi della memoria tra ambiente locale e istanza Render.
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Allineamento nodi e deploy Render per Universal Brain, `key_takeaways`: Render usa il repository Git per il deploy; qualsiasi modifica locale a brain.db richiede commit e push su origin/main per aggiornare il cloud., `pending_tasks`: Verifica del completamento del deploy su Render via endpoint /brain.json.
- **Chiarimento Architetturale: Coesistenza della Topologia a Grafo e dell'Albero Gerarchico come Overlay** (`ep-20260827-hierarchical-overlay-reassurance`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T20:38:00CEST: Chiarimento Architetturale: Coesistenza della Topologia a Grafo e dell'Albero Gerarchico come Overlay
  - **Dettagli:** `raw`: `session_id`: ep_20260827_hierarchical_overlay_reassurance, `timestamp`: 2026-08-27T20:38:00CEST, `topic`: Chiarimento Architetturale: Coesistenza della Topologia a Grafo e dell'Albero Gerarchico come Overlay, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Episodio Chat: Architettura Ibrida Cloud Render vs Agenti Locali MCP & Sicurezza LLM** (`ep-20260827-render-cloud-vs-local-hybrid-architecture`)
  - **Tags:** `#chat-episode` `#render-cloud` `#local-mcp` `#prompt-injection-defense` `#hybrid-architecture`
  - **Sintesi:** Chiarimento architetturale sulla dualità e cooperazione tra Render Cloud 24/7 (mobile/web/Telegram/GPTs) e Agenti Locali MCP (Antigravity/Cursor/Claude Desktop) per persistenza contestuale.
  - **Dettagli:** `raw`: `topic`: Architettura Ibrida Cloud Render vs MCP Locale & Gestione Guardrails Anti-Injection nei Web Chat LLM, `participants`: ['Pierfrancesco Amendola', 'Antigravity / Google DeepMind Agent'], `date`: 2026-08-27
- **Episodio Chat: Architettura Memoria Cross-Modello e Attribuzione** (`episode-cross-model-memory-architecture`)
  - **Tags:** `#conversation-episode` `#cross-model-chat` `#provenance-architecture` `#gemini-session`
  - **Sintesi:** Sessione di analisi architetturale tra Pierfrancesco e Gemini 3.7 Flash sull'inclusione di prompt utente e metadati del modello nel grafo di memoria persistente.
  - **Dettagli:** `raw`: `topic`: Cross-Model Memory Provenance & User Intent Ingest, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `date`: 2026-08-27
- **Episodio Chat: Evoluzione UI, Persistenza & Aree a Espansione** (`chat-session-2026-08-27-ui-evolution`)
  - **Tags:** `#session-chat` `#ui-evolution` `#progressive-areas` `#cloud-persistence`
  - **Sintesi:** Episodio conversazionale incentrato sulla pulizia grafica del terminale, l'introduzione di viste a macro-aree progressive e la memoria episodica.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `topics`: ['terminal-overlay-fix', 'progressive-areas', 'lossless-sync', 'ai-reasoning-tracking', 'episodic-chat-memory'], `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Episodio Chat: Evoluzione UI, Persistenza & Aree a Espansione
- **Episodio Conversazionale: Concezione Gateway Mobile Telegram** (`episode-2026-08-27-telegram-omnipresence`)
  - **Tags:** `#conversation-episode` `#telegram` `#omnipresence` `#2026-08-27`
  - **Sintesi:** Ideazione e pianificazione dell'interfaccia mobile Telegram per estendere l'ubiquità del cervello artificiale.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `status`: Pianificato e integrato nel grafo, `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Episodio Conversazionale: Concezione Gateway Mobile Telegram
- **Episodio Conversazionale: Evoluzione GraphRAG & Protocollo MCP** (`episode-2026-08-27-graphrag-mcp-evolution`)
  - **Tags:** `#conversation-episode` `#evolution` `#graphrag` `#mcp` `#antigravity` `#2026-08-27`
  - **Sintesi:** Sessione di ingegnerizzazione avanzata: sviluppo e verifica del motore FTS5 BM25, cammini minimi attraverso il Corpo Calloso e server MCP conforme allo standard Model Context Protocol.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `key_deliverables`: ['Tabella virtuale FTS5 nodes_fts con trigger di sincronizzazione automatica', 'Endpoint GET /api/graph/path (Shortest Path traversal)', 'Endpoint GET /api/graph/subgraph (Scoped context injection)', 'Server mcp_server.py per Claude Desktop, Cursor e Antigravity'], `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Episodio Conversazionale: Evoluzione GraphRAG & Protocollo MCP
- **Episodio Conversazionale: Valutazione Strutture ad Albero** (`episode-2026-08-27-tree-structures-evaluation`)
  - **Tags:** `#conversation-episode` `#trees` `#data-structures` `#graph-theory` `#2026-08-27`
  - **Sintesi:** Discussione e perizia tecnica sull'integrazione di alberi binari, alberi di ricerca e alberi di copertura pesati nel grafo universale.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `outcome`: Validazione di MST e Tassonomia Gerarchica come strutture ad albero superiori rispetto al BST per grafi cognitivi, `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Episodio Conversazionale: Valutazione Strutture ad Albero
- **Episodio Conversazione: Allineamento Hub AI Unificato** (`episode-20260829-avvio-intervista-universal-ai-hub`)
  - **Tags:** `#chat` `#grill-me` `#continuità-cognitiva`
  - **Sintesi:** Avvio dell'intervista interattiva per definire la forma e la tecnologia del nuovo client unificato multi-AI.
  - **Dettagli:** `raw`: `key_takeaways`: Inizio specifica e intervista /grill-me per l'Hub AI Unificato con Universal Brain permanente., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Intervista requisiti e generazione piano d'implementazione, `topic`: Definizione Hub AI Unificato con Memoria Permanente
- **Episodio Conversazione: Allineamento Struttura Autonoma JARVIS** (`episode-20260829-definizione-piano-jarvis-desktop`)
  - **Tags:** `#chat` `#jarvis` `#continuità-cognitiva`
  - **Sintesi:** Definizione dei confini del nuovo progetto JARVIS sul Desktop e predisposizione del piano di esecuzione modulare.
  - **Dettagli:** `raw`: `key_takeaways`: JARVIS risiede in Desktop/Jarvis; CervelloArtificiale resta il backend di memoria; piano pronto per approvazione., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Approvazione piano ed esecuzione creazione cartella Desktop/Jarvis, `topic`: Pianificazione Creazione Cartella e Progetto JARVIS
- **Episodio Conversazione: Architettura Connettoma Neurale, Web Access e Sincronizzazione Prompt** (`episode-20260829-architettura-connettoma-e-sync-prompt`)
  - **Tags:** `#chat` `#continuità-cognitiva` `#architettura` `#master-prompt`
  - **Sintesi:** Sessione di allineamento e chiarimento sui meccanismi interni del Cervello Artificiale (SQLite, FTS5, Palazzo Cognitivo, MCP vs Web) e sincronizzazione immediata del Master Prompt per le AI esterne.
  - **Dettagli:** `raw`: `key_takeaways`: Le AI web usano OpenAPI o Markdown strutturato; il Master Prompt include il Palazzo Cognitivo; ogni sessione viene persistita ed esportata in brain.db e brain.md, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessuno, sincronizzazione completata, `topic`: Architettura Connettoma Neurale e Sincronizzazione Web
- **Episodio Conversazione: Chiusura Jarvis e Pivot su Nuovo Progetto** (`episode-20260829-chiusura-jarvis-nuovo-progetto`)
  - **Tags:** `#chat` `#pivot` `#continuità-cognitiva`
  - **Sintesi:** Eliminazione progetti Jarvis dal desktop e registrazione del cambio di direzione strategico nel connettoma.
  - **Dettagli:** `raw`: `key_takeaways`: Jarvis abbandonato; file rimossi; connettoma pronto per nuova iniziativa pragmatica., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Definizione e avvio del nuovo progetto, `topic`: Chiusura Jarvis e Transizione a Nuovo Progetto
- **Episodio Conversazione: Integrazione OpenJarvis su Desktop** (`episode-20260829-integrazione-openjarvis-desktop`)
  - **Tags:** `#chat` `#openjarvis` `#continuità-cognitiva`
  - **Sintesi:** Clonato il repository Stanford OpenJarvis sul Desktop e integrata la skill/tool per la memoria bi-emisferica del Cervello Artificiale.
  - **Dettagli:** `raw`: `key_takeaways`: OpenJarvis clonato in Desktop/OpenJarvis; UniversalBrainTool attivo e testato con successo; Desktop app Tauri disponibile., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessuno, `topic`: Integrazione OpenJarvis Stanford con Universal AI Brain
- **Episodio Conversazione: Progettazione JARVIS Voice AI e Integrazione Neurale** (`episode-20260829-progettazione-jarvis-voice-ai`)
  - **Tags:** `#chat` `#jarvis` `#voice-ai` `#connettoma`
  - **Sintesi:** Sessione di disamina repository open-source e definizione architetturale completa di JARVIS: assistente vocale continuo a costo zero connesso alla memoria persistente.
  - **Dettagli:** `raw`: `key_takeaways`: sukeesh/Jarvis è obsoleto; isair/jarvis è la migliore base di riferimento; stack a costo 0€ confermato con Groq/Gemini + Whisper + Kokoro + MCP., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Sviluppo jarvis_core.py e collegamento audio-MCP, `topic`: Progettazione JARVIS Personal Voice AI a Costo Zero
- **Episodio Conversazione: Rilascio JARVIS Voice Assistant su Desktop** (`episode-20260829-completamento-rilascio-jarvis-desktop`)
  - **Tags:** `#chat` `#jarvis` `#rilascio` `#continuità-cognitiva`
  - **Sintesi:** Creazione completa e test del nuovo assistente vocale JARVIS sul Desktop, con memoria condivisa del Cervello Artificiale.
  - **Dettagli:** `raw`: `key_takeaways`: JARVIS è pronto sul Desktop; cartella autonoma; connettoma testato e collegato., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessuno, progetto pronto all'uso, `topic`: Creazione e Rilascio del Progetto JARVIS sul Desktop
- **Episodio Conversazione: Test Superato OpenJarvis con Ollama** (`episode-20260829-test-openjarvis-ollama-successo`)
  - **Tags:** `#chat` `#openjarvis` `#continuità-cognitiva`
  - **Sintesi:** Validazione end-to-end completata: OpenJarvis legge il connettoma, esegue inferenza su Ollama e restituisce la descrizione accurata di Pierfrancesco.
  - **Dettagli:** `raw`: `key_takeaways`: OpenJarvis risponde perfettamente usando gpt-oss:120b-cloud via Ollama e il connettoma Universal AI Brain., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash', 'OpenJarvis gpt-oss:120b-cloud'], `pending_tasks`: Nessuno, sistema pronto all'uso vocale e interattivo, `topic`: Verifica Risposta OpenJarvis con Ollama e Cervello Artificiale
- **Episodio Vocale: Allora vorrei dirti che oggi ho man...** (`episode-allora-vorrei-dirti-che-oggi-ho-man-4690`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su Allora vorrei dirti che oggi ho man....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: Allora vorrei dirti che oggi ho man...
- **Episodio Vocale: Jarvis, ricordi quali sono gli emis...** (`episode-jarvis-ricordi-quali-sono-gli-emis-3117`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su Jarvis, ricordi quali sono gli emis....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: Jarvis, ricordi quali sono gli emis...
- **Episodio Vocale: Quali sono le abitudini monitorate ...** (`episode-quali-sono-le-abitudini-monitorate-2979`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su Quali sono le abitudini monitorate ....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: Quali sono le abitudini monitorate ...
- **Episodio Vocale: c'è un problema vorrei sapere di pi...** (`episode-c-un-problema-vorrei-sapere-di-pi-3203`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su c'è un problema vorrei sapere di pi....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: c'è un problema vorrei sapere di pi...
- **Episodio Vocale: che ore sono...** (`episode-che-ore-sono-3134`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su che ore sono....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: che ore sono...
- **Episodio Vocale: ehi Jarvis ehi Jarvis mi puoi dire ...** (`episode-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su ehi Jarvis ehi Jarvis mi puoi dire ....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: ehi Jarvis ehi Jarvis mi puoi dire ...
- **Episodio Vocale: ho bisogno di sapere tutto ciò che ...** (`episode-ho-bisogno-di-sapere-tutto-ci-che-2753`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su ho bisogno di sapere tutto ciò che ....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'None'], `topic`: ho bisogno di sapere tutto ciò che ...
- **Episodio Vocale: quanti nodi ci sono nel mio cervell...** (`episode-quanti-nodi-ci-sono-nel-mio-cervell-4794`)
  - **Tags:** `#jarvis` `#voice-chat` `#continuità-cognitiva`
  - **Sintesi:** Dialogo vocale in tempo reale tra Pierfrancesco e JARVIS su quanti nodi ci sono nel mio cervell....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'openai/gpt-oss-120b'], `topic`: quanti nodi ci sono nel mio cervell...
- **Episodio: Audit Totale & Continuità Cognitiva Cross-Chat** (`episode-audit-completo-e-potenziamento-skill`)
  - **Tags:** `#sessione-audit` `#pierfrancesco` `#universal-brain` `#cross-chat-memory` `#metamemoria`
  - **Sintesi:** Sessione di audit intensivo, correzione bug su backend/MCP/Telegram, potenziamento formale della skill per continuità cross-chat e persistenza delle risposte fornite nel knowledge graph.
  - **Dettagli:** `raw`: `key_takeaways`: L'architettura del Cervello garantisce la continuità multi-sessione tra assistenti AI diversi e chat diverse grazie alla triade USER_INTENT + AI_REASONING + CONVERSATION_EPISODE., `outcome`: Audit superato al 100%, skill potenziata e sincronizzata con la direttiva di continuità cross-chat, grafo aggiornato., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: ['Nessun bug residuo. Sistema pronto per sincronizzazione cloud e deploy.'], `topic`: Audit del codice, prompt e garanzia di memoria cross-chat persistente
- **Episodio: Audit critico e mockup frontend del Univ** (`episode-audit-critico-e-mockup-fr-2255`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Audit critico e mockup frontend del Universal AI Brain
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Audit critico e mockup frontend del Universal AI Brain, `key_takeaways`: Risoluzione e decisioni per Audit critico e mockup frontend del Universal AI Brain, `pending_tasks`: Nessun task pendente
- **Episodio: Bonifica Modello Ollama 7GB su macOS** (`episode-bonifica-storage-ollama-mac`)
  - **Tags:** `#chat` `#troubleshooting` `#macos` `#ollama`
  - **Sintesi:** Sessione dedicata alla localizzazione ed eliminazione dei residui di storage lasciati dal download involontario di un modello locale con Ollama.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Pulizia storage locale da modelli LLM, `key_takeaways`: I modelli di Ollama su macOS persistono in ~/.ollama anche dopo la disinstallazione dell'app; rimozione eseguibile tramite rm -rf ~/.ollama.
- **Episodio: Brainstorming Evolutivo & Nuove Frontiere del Supercervello** (`episode-espansione-ecosistema-supercervello`)
  - **Tags:** `#evoluzione` `#supercervello` `#visione-futura` `#brainstorming`
  - **Sintesi:** Sessione strategica tra Pierfrancesco e Gemini 3.7 Flash sull'espansione e integrazione del connettoma con nuove app e sistemi di automazione.
  - **Dettagli:** `key_takeaways`: Passaggio da archivio a Ubiquitous Cognitive OS tramite Raycast, Web Clipper, Voice Memos e Consolidamento Notturno AI, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Scegliere il primo blocco da implementare (es. Raycast o Web Clipper), `topic`: Integrazioni e miglioramenti futuri per il Supercervello dopo Obsidian
- **Episodio: Chiarimento Concetti Tesi Breast Cancer Classification** (`episode-chiarimento-concetti-tesi-deep-learning`)
  - **Tags:** `#chat` `#tesi` `#oncologia` `#deep-learning`
  - **Sintesi:** Sessione incentrata sulla definizione e contestualizzazione di Swin Transformer e Deep Stable Learning per la classificazione di immagini di cancro al seno.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Architetture Transformer e Inferenza Causale in Imaging Oncologico, `key_takeaways`: Swin Transformer ottimizza la computazione visiva multiscala con finestre shiftate; Deep Stable Learning assicura robustezza OOD rimuovendo correlazioni spurie nei dati clinici.
- **Episodio: Chiarimento Tecnologie Grafiche Frontend** (`episode-chiarimento-librerie-grafi-frontend`)
  - **Tags:** `#chat` `#frontend-stack` `#graph-rendering`
  - **Sintesi:** Sessione di chiarimento sullo stack di visualizzazione grafi adottato e prototipato nel sito e nella dashboard del connettoma.
  - **Dettagli:** `key_takeaways`: Vis-Network e Three.js sono i motori di produzione attivi; D3 e 3D-Force-Graph sono testati nei mockup; Cytoscape è la candidata per scenari iper-complessi (>5000 nodi)., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Eventuale integrazione della vista radiale D3 o motore ibrido per performance estreme, `topic`: Tecnologie di rendering grafico per Universal AI Brain
- **Episodio: Comando /prompt Copia Rapida per Telegra** (`episode-comando-prompt-copia-rapi-8585`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Comando /prompt Copia Rapida per Telegram Bot
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Comando /prompt Copia Rapida per Telegram Bot, `key_takeaways`: La formattazione <pre><code> di Telegram Bot API abilita la copia automatica con singolo tocco su iOS e Android., `pending_tasks`: Nessun task pendente.
- **Episodio: Confronto PKM e RAG su Notion e Obsidian** (`episode-disamina-integrazioni-notion-obsidian`)
  - **Tags:** `#chat` `#pkm` `#notion` `#obsidian` `#produttivita`
  - **Sintesi:** Sessione incentrata sui motivi per cui gli utenti collegano i propri workspace Notion e Obsidian ai modelli di linguaggio (LLM).
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Integrazione LLM con sistemi PKM (Notion vs Obsidian), `key_takeaways`: Notion eccelle in database relazionali collaborativi e automazioni cloud; Obsidian primeggia per privacy, gestione del grafo delle conoscenze e GraphRAG locale su file Markdown., `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Episodio: Controllo di Rispetto del Vincolo 0,00€ Forever** (`episode-verifica-costi-zero-euro`)
  - **Tags:** `#zero-cost` `#garanzia` `#trasparenza`
  - **Sintesi:** Verifica dettagliata punto per punto che l'intero piano di espansione del supercervello rispetti la regola aurea dei 0,00€ Forever.
  - **Dettagli:** `key_takeaways`: Ogni singola soluzione proposta rispetta tassativamente il vincolo di 0,00€ senza abbonamenti nascosti., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Implementare i moduli partendo dalle soluzioni a zero attrito e zero costo, `topic`: Verifica del vincolo di gratuità totale del connettoma
- **Episodio: Creazione Video Showcase 1 Minuto Universal AI Brain** (`episode-video-showcase-anteprima-universal-brain`)
  - **Tags:** `#episodio` `#video` `#anteprima` `#comunicazione`
  - **Sintesi:** Sessione dedicata alla creazione dell'anteprima video di 60 secondi, comprensiva di screenshot generati, codice terminale, musica ed export video per la condivisione del connettoma.
  - **Dettagli:** `key_takeaways`: Creata una pipeline completa di presentazione video di 1 minuto sia via browser a 60fps con export MP4/WebM che via preview GIF animata, corredata dal kit di testo per i post social., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Registrazione video tramite 1-click in video_showcase.html e pubblicazione su LinkedIn / X / GitHub., `topic`: Creazione video tutorial e anteprima 60s per Universal AI Brain
- **Episodio: Debrief Assessment Gemini e Ottimizzazione Memoria Neurale** (`episode-20260829-debrief-assessment-gemini`)
  - **Tags:** `#chat` `#continuità-cognitiva` `#gemini-feedback` `#connettoma`
  - **Sintesi:** Analisi comparativa tra il feedback di Gemini e la reale consistenza del connettoma, con piano per perfezionare il recupero di contesto per le AI esterne.
  - **Dettagli:** `raw`: `key_takeaways`: Il connettoma non è vuoto (304 nodi); il collo di bottiglia è l'iniezione del contesto iniziale verso LLM esterni, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Potenziare il prompt di retrieval / endpoint /brain.md per i client esterni, `topic`: Valutazione feedback Gemini e ottimizzazione connettoma
- **Episodio: Definizione Scopo Universale del Contesto Multi-AI** (`episode-2026-08-27-universal-context-definition`)
  - **Tags:** `#conversation-episode` `#universal-brain` `#context-purpose` `#gemini-session`
  - **Sintesi:** Sessione di formalizzazione dello scopo supremo di Universal AI Brain: memoria persistente del contesto e dei processi mentali cross-AI.
  - **Dettagli:** `raw`: `topic`: Scopo Fondante della Persistenza del Contesto Multi-AI, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `date`: 2026-08-27
- **Episodio: Distribuzione MCP e Skill /universal-brain su Gemini, Claude e ChatGPT** (`episode-2026-08-27-multi-llm-mcp-ecosystem`)
  - **Tags:** `#conversation-episode` `#mcp` `#claude` `#gemini` `#chatgpt` `#multi-llm` `#skill`
  - **Sintesi:** Integrazione globale del cervello e della skill /universal-brain su tutti i modelli di frontiera.
  - **Dettagli:** `raw`: `timestamp`: 2026-08-27T21:45:00CEST, `models_targeted`: ['Claude Desktop', 'Gemini / Antigravity', 'ChatGPT Custom Actions', 'Cursor / Windsurf'], `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Episodio: Distribuzione MCP e Skill /universal-brain su Gemini, Claude e ChatGPT
- **Episodio: Doppio Anello di Persistenza Cloud** (`episode-cloud-git-auto-push`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio sull'approvazione e innesto dell'auto-push Git lato Render per chiudere il cerchio della persistenza.
  - **Dettagli:** `key_takeaways`: Con GITHUB_TOKEN su Render, ogni post web esegue git push in background, eliminando il punto singolo di fallimento se il PC locale è spento., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Inserire GITHUB_TOKEN nelle Environment Variables di Render Dashboard se si desidera attivare il push cloud autonomo., `topic`: Cloud-Side Git Auto-Push e Persistenza a Doppio Anello
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-2447`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-2471`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-2485`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-2529`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-2691`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-8745`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: E2E Test Session Hook** (`episode-e2e-test-session-hook-9065`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: E2E Test Session Hook.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: E2E Test Session Hook, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: Esplorazione Modellazione 3D su Linux** (`episode-esplorazione-linux-3d-modeling`)
  - **Tags:** `#chat` `#linux` `#3d` `#grafica`
  - **Sintesi:** Sessione incentrata sulle capacità del sistema operativo Linux e delle sue varianti nel supporto e download di software di modellazione 3D.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Supporto e distribuzioni Linux per la modellazione 3D, `key_takeaways`: Tutte le principali distro supportano i principali software 3D (Blender, FreeCAD, Maya, Houdini); distro come Fedora Design Suite e Ubuntu Studio li integrano nativamente out-of-the-box.
- **Episodio: Esplorazione Nuovi Layout e Disegni per l'Interfaccia del Cervello** (`episode-20260829-esplorazione-paradigmi-interfaccia-grafo`)
  - **Tags:** `#chat` `#continuità-cognitiva` `#visual-showcase` `#layout`
  - **Sintesi:** Presentazione e analisi interattiva di 5 layout alternativi per l'interfaccia del connettoma a due emisferi.
  - **Dettagli:** `key_takeaways`: I dati rimangono invariati (307 nodi), ma il rendering può spaziare da orbite 3D a torri isometriche a mappe Voronoi., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Scegliere il layout preferito da integrare nella Web App live, `topic`: Nuove visualizzazioni e stili di rendering per il grafo di memoria
- **Episodio: Finalizzazione Cappello Risultati con Riferimento Tabelle** (`episode-perfezionamento-cappello-tabelle-cap-6`)
  - **Tags:** `#chat` `#tesi` `#finalizzazione`
  - **Sintesi:** Completamento dell'introduzione sintetica al capitolo dei risultati con menzione specifica al confronto tramite tabelle e matrici di confusione.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Integrazione riferimento alle tabelle comparative nel Capitolo 6, `key_takeaways`: Generato il frammento definitivo in LaTeX pronto per la compilazione.
- **Episodio: Fondamenti e Filosofia della Memoria Eterna Cross-Chat** (`episode-infinite-context-philosophy`)
  - **Tags:** `#conversation-episode` `#core-mission` `#context-saturation` `#gemini-session`
  - **Sintesi:** Formalizzazione della ragion d'essere del cervello artificiale: superare il reset della memoria per saturazione delle chat tramite grafo semantico unificato.
  - **Dettagli:** `raw`: `date`: 2026-08-27, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Infinite Context & Anti-Amnesia Philosophy
- **Episodio: Nuove rappresentazioni visuali del conne** (`episode-nuove-rappresentazioni-vi-2874`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Nuove rappresentazioni visuali del connettoma
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Nuove rappresentazioni visuali del connettoma, `key_takeaways`: Risoluzione e decisioni per Nuove rappresentazioni visuali del connettoma, `pending_tasks`: Nessun task pendente
- **Episodio: Occultamento Pulsanti Mobile su Browser ** (`episode-occultamento-pulsanti-mob-9019`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Occultamento Pulsanti Mobile su Browser Desktop
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Occultamento Pulsanti Mobile su Browser Desktop, `key_takeaways`: L'uso di display:none inline previene FOUC (Flash of Unstyled Content) dovuto alla cache del browser., `pending_tasks`: Nessun task pendente.
- **Episodio: Ottimizzazione Mobile Web Dashboard Univ** (`episode-ottimizzazione-mobile-web-8880`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Ottimizzazione Mobile Web Dashboard Universal Brain
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Ottimizzazione Mobile Web Dashboard Universal Brain, `key_takeaways`: Il routing a tab mobile separa il canvas 2D dall'ispettore sui display compatti, garantendo massima usabilità., `pending_tasks`: Nessun task pendente.
- **Episodio: Panoramica Sonde Ecografiche Lineari** (`episode-disamina-trasduttori-lineari`)
  - **Tags:** `#chat` `#ecografia` `#hardware` `#tesi`
  - **Sintesi:** Sessione dedicata alla comprensione del principio di funzionamento e dei casi d'uso degli ecografi con sonda lineare.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Tecnologia dei trasduttori lineari in ecografia clinica, `key_takeaways`: Le sonde lineari impiegano alte frequenze per fornire immagini rettangolari ad altissima risoluzione per tessuti superficiali come mammella e tiroide.
- **Episodio: Persistenza Telegram e Heartbeat Demone** (`episode-telegram-keepalive-confirmation`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di conferma della persistenza omnicanale (Telegram incluso) e del meccanismo keep-alive.
  - **Dettagli:** `key_takeaways`: Telegram è ora pienamente integrato nel doppio anello di persistenza. Il demone esegue già un heartbeat anti-sleep ogni 7 minuti evitando lo shutdown di 15m., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessun task pendente. Tutto allineato e funzionante al 100%., `topic`: Telegram Ingest Persistence e Keep-Alive Heartbeat
- **Episodio: Potenziamento Skill e Rilascio Demone Si** (`episode-potenziamento-skill-e-ril-8338`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di dialogo e lavoro su Potenziamento Skill e Rilascio Demone Sincronizzazione macOS
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `topic`: Potenziamento Skill e Rilascio Demone Sincronizzazione macOS, `key_takeaways`: La memoria cross-chat è ora garantita dal demone automatico e dalle direttive imperative distribuite a tutti gli assistenti AI., `pending_tasks`: Nessun task pendente. Il sistema è pienamente autonomo e attivo.
- **Episodio: Progettazione dell'Inibizione Interemisferica & Lazy Loading** (`episode-2026-08-27-interhemispheric-inhibition-design`)
  - **Tags:** `#conversation-episode` `#neuroscience` `#lazy-loading` `#2026-08-27`
  - **Sintesi:** Definizione del modello di lazy loading biologico ispirato all'inibizione GABAergica per un'esecuzione rapida e focalizzata.
  - **Dettagli:** `raw`: `topic`: Biological Interhemispheric Inhibition, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Episodio: Quali sono i progetti principali di...** (`episode-quali-sono-i-progetti-principali-di-8169`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e qwen/qwen3.8-27b (Groq) su Quali sono i progetti principali di....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Groq (qwen/qwen3.8-27b)'], `topic`: Quali sono i progetti principali di...
- **Episodio: Restyling Dark-Tech, Stabilizzazione Fisica & Ripristino Palazzo Cognitivo** (`episode-frontend-deeptech-redesign-and-physics-zero-lag`)
  - **Tags:** `#session-recap` `#frontend-restyling` `#graphify-aesthetic` `#physics-freeze` `#palazzo-cognitivo` `#zero-lag`
  - **Sintesi:** Sessione approfondita di restyling frontend (stile Graphify.com e Caveman.so), eliminazione di oscillazioni e rotazioni continue della fisica su Vis-Network, correzione del bug di ispezione nodi e ripristino della gerarchia a piani del Palazzo Cognitivo (P0, P1, P2).
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'Antigravity Assistant'], `topic`: Frontend Deep-Tech Restyling & Graph Stability, `outcomes`: ['Implementazione estetica Dark-Tech cyberpunk minimalista con Bento Grid e JetBrains Mono', 'Disabilitazione totale del live physics loop post-stabilizzazione (Zero-Oscillation Freeze)', 'Risoluzione ReferenceError su tags in showInfo() per ispezione istantanea dei nodi', 'Classificazione deterministica dei nodi su 3 piani (P0: 15 nodi, P1: 121 nodi, P2: 53 nodi)', 'Eliminazione di rotazioni e rendering su canvas a 60fps ultra-reattivo']
- **Episodio: Restyling UI & Fullscreen 3D Projector** (`episode-ui-declutter-projector-fullscreen`)
  - **Tags:** `#untagged`
  - **Sintesi:** Sessione di riprogettazione estetica e funzionale dell'interfaccia di Universal AI Brain
  - **Dettagli:** `key_takeaways`: Interfaccia ripulita da bottoni sparsi, modalita 3D immersiva a schermo intero senza sidebar, `participants`: ['Pierfrancesco Amendola', 'Antigravity'], `topic`: UI/UX De-cluttering & 3D Projector Fullscreen
- **Episodio: Revisione Piano Supercervello Cognitive OS** (`episode-revisione-supercervello-cognitive-os`)
  - **Tags:** `#chat` `#supercervello` `#architettura` `#brain-os`
  - **Sintesi:** Sessione di revisione critica del piano di implementazione del Supercervello Ubiquitous Cognitive OS a costo zero.
  - **Dettagli:** `key_takeaways`: Il piano è solido, copre l'intero ciclo di vita dell'informazione e implementa una reale autonomia cognitiva locale (Fase REM + Ricerca Ibrida)., `participants`: ['Pierfrancesco Amendola', 'Gemini'], `pending_tasks`: Implementare e collaudare tutti i moduli, `topic`: Architettura ed estensione del Connettoma Cognitivo
- **Episodio: Revisione Sintetica Introduzione Risultati** (`episode-revisione-sintesi-cappello-cap-6`)
  - **Tags:** `#chat` `#tesi` `#refining`
  - **Sintesi:** Iterazione rapida per ridurre la verbosità del testo introduttivo del capitolo dei risultati della tesi di Pierfrancesco.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Sintesi testo introduttivo Capitolo 6, `key_takeaways`: Generata versione compatta di due paragrafi pronta per il codice sorgente LaTeX.
- **Episodio: Rilascio Documentazione Ufficiale README** (`episode-update-readme-architecture`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di redazione e pubblicazione del README.md completo su GitHub.
  - **Dettagli:** `key_takeaways`: Il README.md è ora la fonte di verità tecnica completa per l'architettura, il funzionamento del demone, il backend FastAPI e il frontend., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessun task pendente. Repository e connettoma allineati al 100%., `topic`: Aggiornamento Documentazione e Architettura README.md
- **Episodio: Rilascio Motori Cognitivi Avanzati e Obsidian Bridge** (`episode-potenziamento-cognitivo-obsidian-bridge`)
  - **Tags:** `#chat` `#connettoma` `#obsidian` `#continuità-cognitiva`
  - **Sintesi:** Sessione di analisi del progetto Neomas, superamento con architettura ad alte prestazioni SQLite WAL e rilascio completo del ponte Obsidian con briefing giornaliero e matrici dialettiche.
  - **Dettagli:** `key_takeaways`: Universal AI Brain supera Neomas integrando un vero database SQLite WAL + FTS5 sub-millisecondo con sincronizzazione bidirezionale Markdown su Obsidian Vault e suite completa di motori cognitivi., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Sincronizzazione finale e auto-push Git / Render., `topic`: Rilascio Completo Motori Cognitivi e Obsidian Bridge
- **Episodio: Rilascio e Collaudo Completo del Supercervello Cognitivo** (`episode-completamento-supercervello-ecosistema`)
  - **Tags:** `#rilascio` `#collaudo` `#supercervello` `#successo`
  - **Sintesi:** Completamento e collaudo con successo di tutti i moduli dell'ecosistema cognitivo onnipresente a costo zero.
  - **Dettagli:** `key_takeaways`: L'intero ecosistema è ora operativo e integrato a 360 gradi su Mac, Safari, iPhone, Telegram, IDE e Obsidian., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Abilitare gli script su Raycast e il Web Clipper in Safari, `topic`: Costruzione e rilascio dell'ecosistema completo Supercervello
- **Episodio: Risoluzione Demone e Persistenza Nodi** (`episode-fix-daemon-render-persistence`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di analisi e riparazione del demone di sincronizzazione e della persistenza del connettoma.
  - **Dettagli:** `key_takeaways`: I LaunchAgent di macOS non possono avviare script in ~/Desktop senza FDA; spostare i binari in ~/.local/bin risolve il problema. Render free tier dorme dopo 15m se non riceve ping; il keep-alive locale lo mantiene attivo. Git deve essere la sorgente di verità sempre aggiornata., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessun task pendente. Demone e connettoma operativi., `topic`: Fix Demone Sync e Persistenza Nodi Render
- **Episodio: Ristrutturazione Fondativa del Connettoma a 12 Macro-Domini** (`episode-20260829-sigillatura-12-macro-domini`)
  - **Tags:** `#chat` `#continuità-cognitiva` `#macro-domini` `#palazzo-cognitivo`
  - **Sintesi:** Riorganizzazione storica e sigillo del Piano 0 del Palazzo Cognitivo con 12 Macro-Domini permanenti e blindatura delle regole di routing.
  - **Dettagli:** `key_takeaways`: Il Piano 0 è ora immutabile (13 nodi); tutte le future AI devono associare ogni nuovo nodo a uno dei 12 domini, `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Sincronizzazione finale PC ⮂ Render Cloud, `topic`: Riorganizzazione Macro-Domini e sigillatura Piano 0
- **Episodio: Spiegazione Intuitiva Concetti Causali e Attention** (`episode-chiarimento-intuitivo-pilastri-teorici`)
  - **Tags:** `#chat` `#divulgazione` `#fondamenti-ai` `#tesi`
  - **Sintesi:** Sessione dedicata alla chiarificazione intuitiva di Self-Attention, Inferenza Causale, Feature Confounders e Decorrelazione.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Intuizione dietro Deep Stable Learning e Transformers, `key_takeaways`: La self-attention calcola l'importanza relativa del contesto; l'inferenza causale evita shortcut; i confounders sono falsi indizi; la decorrelazione neutralizza i confounders.
- **Episodio: Teoria dei Sotto-Grafi Modulari e Decentramento Hub** (`episode-2026-08-27-modular-domain-graph-topology`)
  - **Tags:** `#conversation-episode` `#graph-theory` `#modularity` `#2026-08-27`
  - **Sintesi:** Definizione della topologia a sotto-grafi modulari: entità enciclopediche e verticali isolate da person-pierfrancesco.
  - **Dettagli:** `raw`: `topic`: Modular Subgraph Clustering, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Episodio: Test Hook Session End** (`episode-test-hook-session-end-2411`)
  - **Tags:** `#ide-hook` `#dialogue-episode`
  - **Sintesi:** Sessione di sviluppo dedicata a: Test Hook Session End.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'IDE Assistant'], `topic`: Test Hook Session End, `key_takeaways`: Task implementato e verificato con successo.
- **Episodio: Validazione Token GitHub Render** (`episode-verify-github-token-render`)
  - **Tags:** `#episodio-chat` `#continuità-cognitiva` `#pierfrancesco`
  - **Sintesi:** Episodio di verifica dell'inserimento del token GITHUB_TOKEN su Render e test di persistenza.
  - **Dettagli:** `key_takeaways`: Il token GITHUB_TOKEN è stato inserito con successo su Render; i nodi ingestati online vengono elaborati e persistiti in tempo reale., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Nessun task pendente. Sistema operativo e blindato., `topic`: Verifica Token Render e Auto-Push Cloud
- **Episodio: Valutazione e Design del Modello Graph-of-Graphs a Piani** (`episode-2026-08-27-fractal-graph-of-graphs-evaluation`)
  - **Tags:** `#conversation-episode` `#graph-of-graphs` `#hypergraph` `#2026-08-27`
  - **Sintesi:** Analisi comparativa, pro, contro e fattibilità tecnica del modello di grafo a palazzo frattale su SQLite.
  - **Dettagli:** `raw`: `topic`: Multi-Layer Graph-of-Graphs Design, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Episodio: che ne pensi del mio cervello artif...** (`episode-che-ne-pensi-del-mio-cervello-artif-8743`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e openai/gpt-oss-120b (groq) su che ne pensi del mio cervello artif....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'groq (openai/gpt-oss-120b)'], `topic`: che ne pensi del mio cervello artif...
- **Episodio: che ne pensi del mio cervello artif...** (`episode-che-ne-pensi-del-mio-cervello-artif-8793`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e gemini-3.7-flash (gemini) su che ne pensi del mio cervello artif....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'gemini (gemini-3.7-flash)'], `topic`: che ne pensi del mio cervello artif...
- **Episodio: chi è Pierfrancesco Amendola e cosa...** (`episode-chi-pierfrancesco-amendola-e-cosa-8426`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e openai/gpt-oss-120b (groq) su chi è Pierfrancesco Amendola e cosa....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'groq (openai/gpt-oss-120b)'], `topic`: chi è Pierfrancesco Amendola e cosa...
- **Episodio: ma è tutto falso!!!** (`episode-ma-tutto-falso-8462`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e openai/gpt-oss-120b (groq) su ma è tutto falso!!!.
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'groq (openai/gpt-oss-120b)'], `topic`: ma è tutto falso!!!
- **Episodio: non riesci a connetterti al mio cer...** (`episode-non-riesci-a-connetterti-al-mio-cer-8486`)
  - **Tags:** `#universal-hub` `#sessione-chat`
  - **Sintesi:** Conversazione tra Pierfrancesco e openai/gpt-oss-120b (groq) su non riesci a connetterti al mio cer....
  - **Dettagli:** `raw`: `participants`: ['Pierfrancesco Amendola', 'groq (openai/gpt-oss-120b)'], `topic`: non riesci a connetterti al mio cer...
- **Metacognizione e Sviluppo del Sistema AI** (`episode-system-metacognition`)
  - **Tags:** `#system-evaluation` `#meta-conversation` `#ai-development`
  - **Sintesi:** Sessione dedicata all'introspezione sistemica e al miglioramento dell'infrastruttura cognitiva dell'AI stessa.
  - **Dettagli:** `raw`: `date`: 2026-08-29, `topic`: System Metacognition & Graphify Protocol, `ingested_via`: telegram_json_post, `user`: Pierfrancesco
- **Perfezionamento del 3D Cognitive Embedding Projector & Ottica Neurale** (`episode-embedding-projector-globe-and-optics`)
  - **Tags:** `#episode` `#projector3d` `#design` `#session`
  - **Sintesi:** Sessione di sviluppo per arricchire il visualizzatore neurale 3D con proiezione a globo, controllo di luminosità e spaziatura, e layout ergonomico.
  - **Dettagli:** `key_takeaways`: Il Projector 3D dispone ora di 3 modalità spaziali (3D Volum., 2D Planare, Emisferi Globo), controlli ottici in tempo reale e uscita rapida. Il grafo 2D e la sidebar restano invariati., `participants`: ['Pierfrancesco Amendola', 'Antigravity 2.0'], `pending_tasks`: Nessuno, `topic`: Evoluzione del 3D Cognitive Embedding Projector & Ottica Neurale
- **Progettazione Piattaforma Personale di Apprendimento Linguistico** (`episode-language-app-architecture`)
  - **Tags:** `#language-learning` `#software-design` `#chat-session`
  - **Sintesi:** Discussione architetturale incentrata sulla creazione di un'applicazione proprietaria e non divulgata per lo studio del portoghese e del tedesco senza restrizioni di utilizzo.
  - **Dettagli:** `raw`: `date`: 2026-08-29, `topic`: Architettura software per apprendimento linguistico autonomo, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Release Commit 62e48df (Render Hot-Rebuild)** (`node-commit-62e48df`)
  - **Tags:** `#mutation-import` `#devops-timeline` `#deployment-event`
  - **Sintesi:** Release Commit 62e48df (Render Hot-Rebuild) (Layer: DEVOPS_TIMELINE, Tipo: DEPLOYMENT_EVENT)
  - **Dettagli:** `raw`: `id`: node_commit_62e48df, `label`: Release Commit 62e48df (Render Hot-Rebuild), `type`: DEPLOYMENT_EVENT, `layer`: DEVOPS_TIMELINE, `participants`: ['Pierfrancesco Amendola', 'AI Assistant'], `topic`: Release Commit 62e48df (Render Hot-Rebuild)
- **Rilascio e Sincronizzazione dell'Hierarchical Tree Engine e degli Strumenti MCP nel Cervello Cognitivo** (`ep-20260827-hierarchical-tree-deployment-sync`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T20:34:46CEST: Rilascio e Sincronizzazione dell'Hierarchical Tree Engine e degli Strumenti MCP nel Cervello Cognitivo
  - **Dettagli:** `raw`: `session_id`: ep_20260827_hierarchical_tree_deployment_sync, `timestamp`: 2026-08-27T20:34:46CEST, `topic`: Rilascio e Sincronizzazione dell'Hierarchical Tree Engine e degli Strumenti MCP nel Cervello Cognitivo, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Sessione Alternative di Guadagno Digitale** (`episode-alternative-monetization-brainstorming`)
  - **Tags:** `#chat` `#strategia` `#side-business` `#idee-monetizzazione`
  - **Sintesi:** Definizione di quattro percorsi operativi di guadagno a costo zero per raggiungere il target di 100-500€ mensili.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Strategie pratiche di monetizzazione alternativa: Automazioni B2B, Micro-SaaS, Boilerplate ed Editoria Tecnica., `key_takeaways`: Le automazioni per attività locali permettono monetizzazione immediata; micro-app e asset digitali garantiscono rendita scalabile nel tempo.
- **Sessione Ottimizzazione Backend e Audit Sicurezza** (`episode-backend-optimization-session`)
  - **Tags:** `#chat` `#sviluppo` `#collaborazione-ai` `#sicurezza-dati`
  - **Sintesi:** Sessione collaborativa multi-modello (Qwen + Gemini) per ottimizzare il Universal Knowledge Graph. Enfasi sulla sicurezza dei dati (backup), correzione bug critici e raggiungimento di performance estreme (pathfinding 0.05ms).
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Qwen 2.5 Max', 'Gemini'], `topic`: Implementazione Opzione C: Ottimizzazione backend ibrida con backup e fix critici, `key_takeaways`: Importanza dell'audit incrociato tra AI per individuare bug sottili; successo dell'approccio ibrido (cache RAM + SQL CTE); preservation totale della logica cognitiva esistente.
- **Sessione Valutazione e Stima Language App** (`episode-valutazione-language-app-antigravity`)
  - **Tags:** `#chat` `#language-app` `#brain-sync`
  - **Sintesi:** Discussione su fattibilità, tempi, complessità e gap del progetto app lingue personale.
  - **Dettagli:** `raw`: `key_takeaways`: Progetto solido; MVP rapido in pochi giorni; critico automatizzare generazione contenuti CEFR anziché scrivere lezioni a mano., `participants`: ['Pierfrancesco Amendola', 'Gemini 3.7 Flash'], `pending_tasks`: Conferma stack (PWA React vs Flutter) e avvio script generazione lezioni A1., `topic`: Valutazione e pianificazione Language Learning App
- **Specifiche Tecniche e Mappatura Comandi dell'Hub Cognitivo Telegram (0€ Webhook Gateway)** (`ep-20260827-telegram-cognitive-hub-spec`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T20:37:03CEST: Specifiche Tecniche e Mappatura Comandi dell'Hub Cognitivo Telegram (0€ Webhook Gateway)
  - **Dettagli:** `raw`: `session_id`: ep_20260827_telegram_cognitive_hub_spec, `timestamp`: 2026-08-27T20:37:03CEST, `topic`: Specifiche Tecniche e Mappatura Comandi dell'Hub Cognitivo Telegram (0€ Webhook Gateway), `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Tassonomia e Classificazione Formale dell'Universal Knowledge Graph** (`ep-20260827-graph-taxonomy-classification`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T18:34:00CEST: Tassonomia e Classificazione Formale dell'Universal Knowledge Graph
  - **Dettagli:** `raw`: `session_id`: ep_20260827_graph_taxonomy_classification, `timestamp`: 2026-08-27T18:34:00CEST, `topic`: Tassonomia e Classificazione Formale dell'Universal Knowledge Graph, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Traduzione e Consolidamento del Benchmark Comparativo sulle Strutture ad Albero per il Grafo Cognitivo** (`ep-20260827-tree-ranking-translation`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T20:32:00CEST: Traduzione e Consolidamento del Benchmark Comparativo sulle Strutture ad Albero per il Grafo Cognitivo
  - **Dettagli:** `raw`: `session_id`: ep_20260827_tree_ranking_translation, `timestamp`: 2026-08-27T20:32:00CEST, `topic`: Traduzione e Consolidamento del Benchmark Comparativo sulle Strutture ad Albero per il Grafo Cognitivo, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Unificazione Architetturale tra Knowledge Graph e Search Trees per Cervelli Artificiali** (`ep-20260827-graph-tree-unification`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T18:28:00CEST: Unificazione Architetturale tra Knowledge Graph e Search Trees per Cervelli Artificiali
  - **Dettagli:** `raw`: `session_id`: ep_20260827_graph_tree_unification, `timestamp`: 2026-08-27T18:28:00CEST, `topic`: Unificazione Architetturale tra Knowledge Graph e Search Trees per Cervelli Artificiali, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Valutazione Business Model YouTube Shorts AI** (`episode-yt-shorts-business-model`)
  - **Tags:** `#chat` `#consulenza` `#business` `#ai-creators` `#youtube`
  - **Sintesi:** Analisi critica della proposta di monetizzazione tramite canali YouTube Shorts per bambini generati con AI.
  - **Dettagli:** `participants`: ['Pierfrancesco Amendola', 'Gemini'], `topic`: Saturazione di mercato, RPM Shorts, vincoli normativi COPPA e approccio ingegneristico., `key_takeaways`: Il modello 'guru' è insostenibile per via di RPM minimi e restrizioni sui minori. Se approcciato, richiede sviluppo di pipeline proprietarie a costo zero.
- **Valutazione Tecnica delle Strutture ad Albero (MST, Dendrogram, Trie, B+Tree) nel Knowledge Graph** (`ep-20260827-tree-structures-evaluation`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T20:30:00CEST: Valutazione Tecnica delle Strutture ad Albero (MST, Dendrogram, Trie, B+Tree) nel Knowledge Graph
  - **Dettagli:** `raw`: `session_id`: ep_20260827_tree_structures_evaluation, `timestamp`: 2026-08-27T20:30:00CEST, `topic`: Valutazione Tecnica delle Strutture ad Albero (MST, Dendrogram, Trie, B+Tree) nel Knowledge Graph, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']
- **Valutazione e Design di un Telegram Bot come Interfaccia I/O Mobile per il Knowledge Graph** (`ep-20260827-telegram-bot-interface`)
  - **Tags:** `#conversation-episode` `#2026-08-27` `#cognitive-sync`
  - **Sintesi:** Episodio del 2026-08-27T18:58:00CEST: Valutazione e Design di un Telegram Bot come Interfaccia I/O Mobile per il Knowledge Graph
  - **Dettagli:** `raw`: `session_id`: ep_20260827_telegram_bot_interface, `timestamp`: 2026-08-27T18:58:00CEST, `topic`: Valutazione e Design di un Telegram Bot come Interfaccia I/O Mobile per il Knowledge Graph, `status`: CONSOLIDATED, `participants`: ['Pierfrancesco Amendola', 'AI Assistant']

### [Macro-Label: `CREATIVE_IDEA`]
- **Celebration Particle & FX Engine** (`streaksup-particle-fx`)
  - **Tags:** `#particles` `#notch-fireworks` `#confetti` `#sparkles` `#splash-flame`
  - **Sintesi:** Suite di effetti grafici ed esplosioni particellari reattive: Notch Fireworks dalla Dynamic Island al 100%, coriandoli gravitazionali, scintille radiali e splash fiammante elastico.
  - **Dettagli:** `raw`: `effects`: ['NotchFireworksView', 'ConfettiCannonView', 'CompletionSparkleEffect', 'FlameLaunchSplashView']
- **Continuous Human-AI Symbiosis Vision** (`continuous-ai-symbiosis`)
  - **Tags:** `#symbiosis` `#continuous-memory` `#ai-evolution` `#dual-brain` `#co-pilot`
  - **Sintesi:** Visione filosofica di un intelligenza aumentata: la memoria dell utente e dei suoi progetti sopravvive tra sessioni distinte attraverso un grafo vivente.
  - **Dettagli:** `raw`: `paradigm`: Co-evolution, `substrate`: Dual Brain Knowledge Graph, `accessibility`: Universal to all LLM agents
- **Dominio: Musica, Audio & Suono** (`domain-musica-audio`)
  - **Tags:** `#domain-hub` `#musica` `#audio` `#ear-training` `#composizione` `#sound-design`
  - **Sintesi:** Teoria Musicale, Ear Training, Composizione, Sound Design, Audio Engineering e Produzione Musicale.
  - **Dettagli:** `scope`: Music theory, ear training, sound synthesis, composition
- **Evoluzione UI & Architettura di Memoria Resiliente** (`session-evolution-ui-persistence`)
  - **Tags:** `#session-evolution` `#ui-polish` `#resilience` `#centaur` `#antigravity`
  - **Sintesi:** Sessione di potenziamento dell'Universal AI Brain: introduzione del terminale chiaro, caricamento JSON visuale e blindatura della persistenza.
  - **Dettagli:** `raw`: `session_date`: 2026-08-27, `architect`: Pierfrancesco Amendola, `executor`: Antigravity
- **Idea per nuova app AI** (`tg-idea-per-nuova-app-ai`)
  - **Tags:** `#telegram` `#mobile-note` `#quick-thought`
  - **Sintesi:** Sviluppo di un agent autonomo
  - **Dettagli:** `raw`: `source`: telegram-bot, `user`: Pierfrancesco
- **Pianoforte Classico & Composizione** (`art-piano-composition`)
  - **Tags:** `#piano` `#classical-music` `#composition` `#emotional-outlet`
  - **Sintesi:** Studio del pianoforte dall'età di tre anni; rifugio espressivo e contrappeso emotivo al rigore logico-scientifico.
  - **Dettagli:** `raw`: `instruments`: Pianoforte (principale), chitarra e violino (autodidatta), `roles`: Compositore, arrangiatore, direttore artistico
- **Recitazione Teatrale (Tricca Ballacche)** (`art-theatre-acting`)
  - **Tags:** `#theatre` `#acting` `#presence` `#public-speaking`
  - **Sintesi:** Esperienza attoriale sul palco come strumento di esplorazione delle dinamiche umane e presenza scenica.
  - **Dettagli:** `raw`: `troupe`: Compagnia Teatrale Tricca Ballacche, `skills`: Comunicazione paraverbale, gestione emotiva dal vivo
- **Scrittura & Pubblicazione Indipendente** (`art-creative-writing`)
  - **Tags:** `#kdp` `#writing` `#children-books` `#essays`
  - **Sintesi:** Attività di autore ed editore su Amazon KDP per libri per ragazzi, narrativa e manuali tecnici.
  - **Dettagli:** `raw`: `genres`: Divulgazione scientifica, letteratura per l'infanzia, saggistica
- **Simbiosi Operativa Antigravity & Pierfrancesco** (`antigravity-centaur-collaboration`)
  - **Tags:** `#centaur-ai` `#co-pilot` `#pair-programming` `#continuous-sync`
  - **Sintesi:** Manifestazione pratica del Modello Centauro: intenzione e guida umana sposate all'esecuzione deterministica dell'assistente AI.
  - **Dettagli:** `raw`: `modality`: Caveman Protocol + Graph Knowledge Persistence, `synergy`: Strategia & Anima (Pierfrancesco) + Implementazione & Sintesi (Antigravity)
- **Sintesi Artistico-Scientifica & Centauro** (`creative-multidisciplinary`)
  - **Tags:** `#music` `#theatre` `#writing` `#centaur-ai`
  - **Sintesi:** Integrazione tra rigore computazionale e sensibilità creativa (pianoforte, teatro Tricca Ballacche, scrittura, modello Centauro).
  - **Dettagli:** `raw`: `music`: Pianoforte, chitarra, violino, composizione, `theatre`: Attore compagnia Tricca Ballacche, `languages`: Italiano, Inglese (cert. UK), Spagnolo, Francese, Tedesco, Portoghese, `human_ai_vision`: Centaur Model: umana strategia + macchina computazionale
- **Test E2E Web Clipper Node** (`test-e2e-web-clipper`)
  - **Tags:** `#web-clipper` `#test`
  - **Sintesi:** Verifica completa dell'ingestione Web Clipper.
  - **Dettagli:** `url`: https://example.com, `user`: Pierfrancesco
- **Test Live Download Node** (`test-live-download-node`)
  - **Tags:** `#daemon-download-test`
  - **Sintesi:** Test di verifica download automatico da cloud a locale
  - **Dettagli:** `raw`: `source`: render-api

### [Macro-Label: `DESIGN_TOKEN`]
- **Cyber Slate Dark Aesthetics** (`cyber-slate-space-aesthetic`)
  - **Tags:** `#090d16` `#0f172a` `#020617` `#dark-mode` `#glassmorphism` `#backdrop-blur`
  - **Sintesi:** Estetica visuale cosmica a basso contrasto di fondo (#090d16) con pannelli in vetro sfumato (backdrop-filter: blur(16px)) e bordi slate.
  - **Dettagli:** `raw`: `bg_main`: #090d16, `card_bg`: rgba(15, 23, 42, 0.84), `border`: rgba(51, 65, 85, 0.6), `blur`: 16px
- **Dark Neon Cyber Aesthetic** (`design-cyber-neon`)
  - **Tags:** `#dark-mode` `#cyan` `#magenta` `#glassmorphism`
  - **Sintesi:** Design system scuro ad alto impatto visivo con superfici in vetro e accenti neon ad alto contrasto.
  - **Dettagli:** `raw`: `bg_base`: #0A0E17, `bg_surface`: #0F172A, `accent_cyan`: #00D2FF, `accent_magenta`: #FF007F, `accent_purple`: #7928CA, `blur_intensity`: 16px
- **Dark Neon Design Tokens** (`design-tokens-core`)
  - **Tags:** `#design-system` `#tokens` `#css` `#dark-mode`
  - **Sintesi:** Design system scuro ad alto contrasto con superfici semitrasparenti e accenti luminosi.
  - **Dettagli:** `raw`: `bg_base`: #0A0E17, `bg_surface`: #0F172A, `bg_panel`: #121826, `border_subtle`: rgba(255, 255, 255, 0.08), `glass_blur`: 16px
- **Design System Duolingo Chess** (`design-duolingo-chess-system`)
  - **Tags:** `#duolingo` `#design-system` `#color-palette` `#3d-buttons` `#vector-art`
  - **Sintesi:** Design system ispirato a design.duolingo.com e blog.duolingo.com. Palette ufficiale Duolingo, pulsanti 3D estrusi, sagome vettoriali parametriche e mascotte Duo il Gufo.
- **Design System Moderno & Minimal per App di Lingue** (`design-language-app-system`)
  - **Tags:** `#palette` `#typography` `#tokens` `#dark-mode` `#micro-interactions`
  - **Sintesi:** Design system basato su estetica pulita e moderna, chip interattivi 3D minimali, palette semantica (Emerald/Rose/Indigo) e transizioni fluide a basso attrito cognitivo.
  - **Dettagli:** `raw`: `style`: Modern Minimalist / Clean Tech, `feedback_loop`: Scale transition, gentle shake on error, persistent bottom actions
- **Design Token: Palette Deep-Tech & Cyberpunk Minimalist** (`design-token-cyberpunk-minimalist-palette`)
  - **Tags:** `#design-system` `#color-palette` `#dark-tech` `#cyberpunk` `#bento-grid`
  - **Sintesi:** Sistema di design tokens e palette colori per l interfaccia utente ispirata a Graphify.com e Caveman.so: Deep Void (#07080c), Neon Cyan (#00D2FF), Cyber Magenta (#FF007F) e Electric Purple (#A855F7).
  - **Dettagli:** `raw`: `background`: #07080c (Deep Void), `surface`: #0e1017 (Dark Surface), `panel`: #141722 (Panel Elevato), `left_hemisphere`: #00D2FF (Neon Cyan), `right_hemisphere`: #FF007F (Cyber Magenta), `corpus_callosum`: #A855F7 (Electric Purple), `typography`: JetBrains Mono + Inter/Geist
- **Dominio: Design, UI/UX & Creatività** (`domain-design-creativita`)
  - **Tags:** `#domain-hub` `#design` `#ui-ux` `#dark-tech` `#graphic-design` `#brand-voice` `#tipografia`
  - **Sintesi:** UI/UX Design Dark-Tech, Graphic Design, Brand Voice, Tipografia, Estetica Visiva e Interaction Design.
  - **Dettagli:** `scope`: UI/UX design systems, aesthetics, typography, branding
- **StreaksUp Glassmorphic Design System** (`streaksup-glassmorphism-system`)
  - **Tags:** `#glassmorphism` `#materials` `#sf-rounded` `#shadow-elevation`
  - **Sintesi:** Design system basato su materiali SwiftUI (.regularMaterial, .ultraThinMaterial), bordi sfumati con gradienti di categoria e raggi di curvatura continui 20-24pt.
  - **Dettagli:** `raw`: `typography`: Font.system(..., design: .rounded), `materials`: ['.regularMaterial', '.ultraThinMaterial'], `corner_radius`: Card 20pt / Hero 24pt continuous, `haptic_integration`: HapticManager (Light, Medium, Success, Warning)

### [Macro-Label: `EMOTIONAL_MEMORY`]
- **Tensione tra Controllo Perfezionistico ed Espressione** (`memory-perfectionism-tension`)
  - **Tags:** `#perfectionism` `#anxiety` `#vulnerability` `#catharsis`
  - **Sintesi:** La costante ricerca dell'eccellenza e il sovraccarico di responsabilità bilanciati attraverso lo sfogo catartico della musica e dell'arte.
  - **Dettagli:** `raw`: `tension`: Rigore ingegneristico assoluto vs bisogno viscerale di espressione emotiva libera

### [Macro-Label: `LIFE_LESSON`]
- **Dominio: Crescita Personale, Abitudini & Benessere** (`domain-crescita-personale`)
  - **Tags:** `#domain-hub` `#crescita-personale` `#abitudini` `#lezioni-vita` `#benessere` `#riflessioni`
  - **Sintesi:** Memoria Episodica di Vita, Lezioni Apprese, Abitudini Quotidiane, Riflessioni Personali, Fitness Mentale e Crescita Continua.
  - **Dettagli:** `scope`: Personal growth, daily habits, life lessons, holistic wellbeing
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-3e8f7aed7312`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi.
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi., `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-7439c883249f`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202485792
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202485792, `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-3c40d6e17fd5`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202529771
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202529771, `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-cba1775488ae`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202690874
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788202690874, `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-bb8b1e467610`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788208745203
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788208745203, `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Il Cigno Nero (Nassim Taleb) - Estratto** (`kindle-c7eedf9ce6bb`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788209065631
  - **Dettagli:** `book_title`: Il Cigno Nero, `author`: Nassim Taleb, `full_quote`: Non considerare solo ciò che vedi, ma anche ciò che non vedi. Token: 1788209065631, `kindle_meta`: - Highlight Loc. 100 | 2024-01-01, `imported_by`: kindle_sync_engine
- **Lezione di Architettura: Backend come Singola Sorgente di Verità e Pipeline di Rendering Pulita** (`lesson-backend-ground-truth-and-clean-canvas-rendering`)
  - **Tags:** `#architecture-lesson` `#ground-truth` `#clean-code` `#full-stack-integrity`
  - **Sintesi:** Principio guida per lo sviluppo del Cervello Artificiale: il backend SQLite/FastAPI deve essere l unica sorgente di verità per lo stato e i metadati, mentre il frontend deve limitarsi a presentare i dati con zero loop di rendering o simulazioni fisiche non controllate.
  - **Dettagli:** `raw`: `lesson`: Mai far divergere la logica di classificazione tra client e server; garantire sempre integrità schema e checkpoint WAL., `domain`: Ingegneria del Software & Sistemi Cognitivi
- **Lezione sui Confini Affettivi & Non-Idealizzazione** (`lesson-boundaries-clarity`)
  - **Tags:** `#emotional-growth` `#boundaries` `#relationships` `#clarity`
  - **Sintesi:** Non farsi carico unilateralmente della stabilità altrui; l'intensità emotiva non sostituisce la compatibilità e la chiarezza dei confini.
  - **Dettagli:** `raw`: `principles`: ['Rifiuto della sindrome del salvatore', 'Distinzione tra chimica momentanea e allineamento valoriale', 'Comunicazione esplicita senza dare nulla per scontato']
- **Meditazioni (Marco Aurelio) - Estratto** (`kindle-6d280a533c87`)
  - **Tags:** `#kindle` `#lettura` `#libro` `#right` `#crescita-personale`
  - **Sintesi:** Non perdere altro tempo a discutere su cosa sia un uomo buono: sii un uomo buono.
  - **Dettagli:** `book_title`: Meditazioni, `author`: Marco Aurelio, `full_quote`: Non perdere altro tempo a discutere su cosa sia un uomo buono: sii un uomo buono., `kindle_meta`: - Your Highlight on Location 45-48 | Added on Monday, January 15, 2024 10:30:00 AM, `imported_by`: kindle_sync_engine
- **Oggi ho riflettuto sul principio stoico della dicotomia del** (`voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214`)
  - **Tags:** `#siri-shortcuts` `#voice-capture` `#right`
  - **Sintesi:** Oggi ho riflettuto sul principio stoico della dicotomia del controllo nella vita e nel lavoro.
  - **Dettagli:** `source`: test_shortcut, `full_transcript`: Oggi ho riflettuto sul principio stoico della dicotomia del controllo nella vita e nel lavoro., `captured_by`: Pierfrancesco Amendola
- **Resilienza Operativa & Post-Mortem Emotivo** (`lesson-stoic-resilience`)
  - **Tags:** `#stoicism` `#resilience` `#growth-mindset` `#refactoring`
  - **Sintesi:** Trattare gli ostacoli e le delusioni come dati da analizzare a mente fredda per iterare e migliorare senza autocommiserazione.
  - **Dettagli:** `raw`: `method`: Isolare la causa radice, applicare la correzione, ripartire con focus rinnovato
- **Riflessione sull'antifragilità nei sistemi software compless** (`voice-riflessione-sullantifragilit-nei-sistemi-software-2447`)
  - **Tags:** `#voice-capture` `#siri-shortcuts` `#right`
  - **Sintesi:** Riflessione sull'antifragilità nei sistemi software complessi e distribuiti.
  - **Dettagli:** `source`: test_suite_siri, `full_transcript`: Riflessione sull'antifragilità nei sistemi software complessi e distribuiti., `captured_by`: Pierfrancesco Amendola
- **Voglio portare a spasso il cane perché mi provoca tante emoz** (`voice-voglio-portare-a-spasso-il-cane-perch-mi-provoca-t-1518`)
  - **Tags:** `#siri-shortcuts` `#voice-capture` `#right`
  - **Sintesi:** Voglio portare a spasso il cane perché mi provoca tante emozioni e mi manca
  - **Dettagli:** `source`: siri_voice, `full_transcript`: Voglio portare a spasso il cane perché mi provoca tante emozioni e mi manca, `captured_by`: Pierfrancesco Amendola

### [Macro-Label: `MENTAL_MODEL`]
- **Antifragility (Antifragilità)** (`firmware-antifragility`)
  - **Tags:** `#firmware` `#mental-model` `#antifragility`
  - **Sintesi:** Trarre vantaggio dal disordine, dagli errori e dalla volatilità anziché limitarsi a resistervi.
  - **Dettagli:** `author`: Nassim Nicholas Taleb, `reasoning_steps`: ['1. Isola le asimmetrie: dove hai un limite di perdita noto (downside cappato) e un potenziale di guadagno illimitato (upside aperto)?', '2. Progetta un meccanismo di feedback loop che trasformi ogni bug, errore o fallimento in una regola/test automatizzato permanente.', '3. Elimina le fragilità da singolo punto di rottura (Single Point of Failure).', '4. Aggiungi ridondanza strategica e modularità disaccoppiata.']
- **Feynman Technique (Tecnica di Feynman)** (`firmware-feynman`)
  - **Tags:** `#firmware` `#mental-model` `#feynman`
  - **Sintesi:** Se non riesci a spiegarlo in termini semplici a un profano, non lo hai compreso a fondo.
  - **Dettagli:** `author`: Richard Feynman, `reasoning_steps`: ['1. Spiega il concetto, architettura o bug in linguaggio naturale chiarissimo, come a un bambino di 10 anni.', '2. Individua i passaggi in cui sei costretto a ricorrere a gergo tecnico complicato per mascherare un vuoto concettuale.', '3. Torna alla sorgente per chiarire quel punto esatto finché non diventa trasparente.', '4. Usa analogie intuitive e riduci la spiegazione alla sua pura essenza.']

### [Macro-Label: `PERSONAL_VALUE`]
- **Autenticità & Trasparenza Radicale** (`val-authenticity`)
  - **Tags:** `#core-value` `#authenticity` `#honesty` `#no-games`
  - **Sintesi:** Priorità assoluta alla sincerità e alla chiarezza nei rapporti; rifiuto di maschere sociali, ipocrisia e passività.
  - **Dettagli:** `raw`: `standard`: Comunicazione limpida, rispetto dei patti, integrità morale
- **Autonomia, Autosufficienza & Merito** (`val-independence`)
  - **Tags:** `#core-value` `#self-reliance` `#merit` `#zero-cost`
  - **Sintesi:** Costruire la propria libertà attraverso la competenza tecnica verificabile, l'autosufficienza e l'etica del lavoro.
  - **Dettagli:** `raw`: `ethos`: Nessuna scorciatoia, padronanza dei fondamentali, indipendenza creativa
- **Continuità Cognitiva Eterna (Zero Context Loss)** (`val-eternal-cognitive-continuity`)
  - **Tags:** `#eternal-memory` `#core-philosophy` `#cognitive-continuity` `#universal-brain` `#anti-amnesia`
  - **Sintesi:** Valore fondante di Universal AI Brain: nessun pensiero, decisione o ragionamento deve andare perso a causa dei limiti fisici di token delle singole chat.
  - **Dettagli:** `raw`: `anti_pattern_blocked`: Reset amnesico della chat e perdita del filo logico, `principle`: Ogni sessione AI è un frammento transitorio; il grafo è la coscienza persistente unificata., `temporal_scope`: Passato, presente e futuro
- **Dominio: Filosofia, Etica & Principi di Vita** (`domain-filosofia-valori`)
  - **Tags:** `#domain-hub` `#filosofia` `#etica` `#stoicismo` `#valori-personali` `#decision-making`
  - **Sintesi:** Filosofia, Stoicismo, Modelli Mentali, Principi Etici, Decision Making, Autodisciplina e Modelli di Saggezza.
  - **Dettagli:** `scope`: Philosophy, stoic mental models, ethical principles, core personal values
- **Lealtà & Cura dei Legami Significativi** (`val-transparency-loyalty`)
  - **Tags:** `#core-value` `#loyalty` `#family` `#friendship`
  - **Sintesi:** Fedeltà incondizionata a chi ha dimostrato supporto autentico, rispetto e presenza nei momenti critici.
  - **Dettagli:** `raw`: `expression`: Presenza attiva, riconoscenza esplicita e protezione dei rapporti veri
- **Pierfrancesco Amendola** (`person-pierfrancesco`)
  - **Tags:** `#identity` `#creator` `#software-architect` `#ai-researcher` `#human-core`
  - **Sintesi:** Identità centrale, connettoma fondativo e profilo di Pierfrancesco Amendola.
  - **Dettagli:** `raw`: `role`: Architect & Founder, `location`: Italy
- **Privacy-by-Design & Zero-Cloud** (`streaksup-privacy-zero-cloud`)
  - **Tags:** `#privacy-by-design` `#zero-cloud` `#no-tracking` `#data-sovereignty`
  - **Sintesi:** Valore etico cardine: 100% offline, nessun server remoto, nessun tracciamento analytics, nessun account richiesto e piena esportazione JSON.
  - **Dettagli:** `raw`: `cloud_dependency`: Zero (100% local), `telemetry`: None, `account_required`: False, `backup`: Full JSON export / import
- **Utilità Concreta & Impatto Sociale** (`val-impact-utility`)
  - **Tags:** `#core-value` `#social-impact` `#medicine` `#safety`
  - **Sintesi:** La tecnologia deve risolvere problemi reali, proteggere le persone e migliorare l'esperienza umana quotidiana.
  - **Dettagli:** `raw`: `mission`: Salute digitale, prevenzione, accessibilità ed educazione

### [Macro-Label: `PROJECT`]
- **App Alcool** (`proj-appalcool`)
  - **Tags:** `#c` `#c-lang` `#dart` `#flutter` `#javascript` `#mac-project` `#swift` `#typescript` `#web`
  - **Sintesi:** **SafeCheck** is a Flutter mobile app that helps users assess their alcohol consumption safety in real‑time. It combines a series of physical‑performance tests (reflex, balance, coordination, HGN) wit
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppAlcool, `file_uri`: file:///Users/pierfrancesco/Desktop/AppAlcool, `languages`: ['C', 'Dart', 'JavaScript', 'Swift', 'TypeScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 123, `last_modified`: 2026-06-19T14:32:45.444215+00:00, `key_dependencies`: [], `readme_excerpt`: # SafeCheck 📱

**SafeCheck** is a Flutter mobile app that helps users assess their alcohol consumption safety in real‑time. It combines a series of physical‑performance tests (reflex, balance, coordination, HGN) with a Watson Total Body Water (TBW) based Blood Alcohol Concentration (BAC) calculator. The app then fuses the physiological test scores with the chemical BAC estimate to produce a final safety score and risk level.

---

## Table of Contents
1. [Features](#features)
2. [Architecture & Tech Stack](#architecture--tech-stack)
3. [Installation & Setup](#installation--setup)
4. [Running t
- **App Palette** (`proj-apppalette`)
  - **Tags:** `#c++` `#cpp` `#dart` `#flutter` `#javascript` `#mac-project` `#python` `#swift` `#typescript` `#web`
  - **Sintesi:** A new Flutter project.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppPalette, `file_uri`: file:///Users/pierfrancesco/Desktop/AppPalette, `languages`: ['C++', 'Dart', 'JavaScript', 'Python', 'Swift', 'TypeScript'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 118, `last_modified`: 2026-06-11T19:00:06.667132+00:00, `key_dependencies`: [], `readme_excerpt`: # palette_app

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
- **Backend** (`proj-backend`)
  - **Tags:** `#backend` `#express` `#javascript` `#mac-project`
  - **Sintesi:** Progetto Mac: Backend. Stack: Express, JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppMatch/backend, `file_uri`: file:///Users/pierfrancesco/Desktop/AppMatch/backend, `languages`: ['JavaScript'], `frameworks`: ['Express'], `has_git`: False, `relevant_files_count`: 33, `last_modified`: 2026-06-11T19:30:16.978260+00:00, `key_dependencies`: ['bcryptjs', 'cors', 'dotenv', 'express', 'express-rate-limit', 'jsonwebtoken', 'mongoose', 'morgan', 'nodemailer', 'redis', 'socket.io', 'winston', 'zod', 'nodemon'], `readme_excerpt`: 
- **Care Track Demo** (`proj-caretrack-demo`)
  - **Tags:** `#ios` `#mac-project` `#swift` `#swiftui` `#xcodegen`
  - **Sintesi:** ![Platform](https://img.shields.io/badge/Platform-iOS%2018.0+-blue.svg)
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/CareTrack-Demo, `file_uri`: file:///Users/pierfrancesco/Desktop/CareTrack-Demo, `languages`: ['Swift'], `frameworks`: ['SwiftUI', 'XcodeGen'], `has_git`: True, `relevant_files_count`: 64, `last_modified`: 2026-05-06T18:20:04.223387+00:00, `key_dependencies`: [], `readme_excerpt`: # 🏥 CareTrack

![Platform](https://img.shields.io/badge/Platform-iOS%2018.0+-blue.svg)
![Swift](https://img.shields.io/badge/Swift-5.0-orange.svg)
![UI](https://img.shields.io/badge/UI-SwiftUI-success.svg)
![Architecture](https://img.shields.io/badge/Architecture-MVVM-lightgrey.svg)

**CareTrack** è un'applicazione iOS innovativa per la gestione dell'assistenza sanitaria domiciliare e il monitoraggio clinico. Progettata per favorire la collaborazione e la trasparenza, connette in tempo reale tre attori fondamentali del percorso di cura: **Pazienti**, **Caregiver** e **Infermieri/Medici**.

---
- **Cypress Tests** (`proj-cypress_tests`)
  - **Tags:** `#cypress` `#javascript` `#mac-project` `#testing`
  - **Sintesi:** Progetto Mac: Cypress Tests. Stack: Cypress, JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppMatch/cypress_tests, `file_uri`: file:///Users/pierfrancesco/Desktop/AppMatch/cypress_tests, `languages`: ['JavaScript'], `frameworks`: ['Cypress'], `has_git`: False, `relevant_files_count`: 8, `last_modified`: 2026-06-11T14:07:36.400553+00:00, `key_dependencies`: ['cypress'], `readme_excerpt`: 
- **Docs Md** (`proj-docs_md`)
  - **Tags:** `#mac-project`
  - **Sintesi:** ![Status](https://img.shields.io/badge/status-active-success.svg)
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/docs_md, `file_uri`: file:///Users/pierfrancesco/DataMed/docs_md, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 82, `last_modified`: 2025-12-10T14:57:25.543971+00:00, `key_dependencies`: [], `readme_excerpt`: # 🎓 App Federico II - Per Studenti

![Status](https://img.shields.io/badge/status-active-success.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

App mobile completa per gli studenti dell'Università degli Studi di Napoli Federico II.

## ✨ Funzionalità

- 📊 **Gestione Voti** - Tieni traccia dei tuoi esami e calcola la media
- 📅 **Orario Lezioni** - Organizza il tuo calendario settimanale
- 🗺️ **Mappa Ristoranti Convenzionati** - Trova ristoranti con convenzioni ADISURC e universitarie
- 📚 **Aule Studio** - Visualizza la capienza delle aule studio disponibili
- 🎓 **Borse di
- **Federico Iiapp** (`proj-federicoiiapp`)
  - **Tags:** `#c` `#c-lang` `#javascript` `#mac-project` `#python` `#react` `#swift` `#typescript` `#web`
  - **Sintesi:** Progetto Mac: Federico Iiapp. Stack: C, JavaScript, Python, React, Swift, TypeScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/FedericoIIApp, `file_uri`: file:///Users/pierfrancesco/DataMed/FedericoIIApp, `languages`: ['C', 'JavaScript', 'Python', 'Swift', 'TypeScript'], `frameworks`: ['React'], `has_git`: False, `relevant_files_count`: 228, `last_modified`: 2026-03-07T14:17:31.712535+00:00, `key_dependencies`: ['@expo/vector-icons', '@react-native-async-storage/async-storage', '@react-native-community/datetimepicker', '@react-native-community/netinfo', '@react-navigation/bottom-tabs', '@react-navigation/drawer', '@react-navigation/native', '@react-navigation/stack', '@shopify/react-native-skia', 'expo', 'expo-auth-session', 'expo-calendar', 'expo-camera', 'expo-constants', 'expo-crypto'], `readme_excerpt`: 
- **Frontend** (`proj-frontend`)
  - **Tags:** `#c++` `#cpp` `#dart` `#flutter` `#mac-project` `#swift` `#web`
  - **Sintesi:** A new Flutter project.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/AppMatch/frontend, `file_uri`: file:///Users/pierfrancesco/Desktop/AppMatch/frontend, `languages`: ['C++', 'Dart', 'Swift'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 83, `last_modified`: 2026-06-11T19:39:44.392223+00:00, `key_dependencies`: [], `readme_excerpt`: # unicampus

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
- **Mary** (`proj-mary`)
  - **Tags:** `#mac-project` `#web`
  - **Sintesi:** Progetto Mac: Mary. Stack: Varie.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/Sfizi HTML/Mary, `file_uri`: file:///Users/pierfrancesco/Desktop/Sfizi HTML/Mary, `languages`: [], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2026-03-24T08:47:43.343496+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Missing Feedback** (`proj-missing-feedback`)
  - **Tags:** `#backend` `#express` `#javascript` `#mac-project`
  - **Sintesi:** Progetto Mac: Missing Feedback. Stack: Express, JavaScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/backend/missing-feedback, `file_uri`: file:///Users/pierfrancesco/DataMed/backend/missing-feedback, `languages`: ['JavaScript'], `frameworks`: ['Express'], `has_git`: False, `relevant_files_count`: 3, `last_modified`: 2025-12-10T14:57:25.531224+00:00, `key_dependencies`: ['cors', 'dotenv', 'express', 'nodemailer'], `readme_excerpt`: 
- **Palazzografica** (`proj-palazzografica`)
  - **Tags:** `#c` `#c-lang` `#mac-project`
  - **Sintesi:** Progetto Mac: Palazzografica. Stack: C.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/palazzo/palazzografica/palazzografica, `file_uri`: file:///Users/pierfrancesco/Desktop/palazzo/palazzografica/palazzografica, `languages`: ['C'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2024-10-22T21:42:34.210587+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Scripts** (`proj-scripts`)
  - **Tags:** `#javascript` `#mac-project` `#python`
  - **Sintesi:** Progetto Mac: Scripts. Stack: JavaScript, Python.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/scripts, `file_uri`: file:///Users/pierfrancesco/DataMed/scripts, `languages`: ['JavaScript', 'Python'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 6, `last_modified`: 2025-12-10T14:57:25.567495+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Tests** (`proj-tests`)
  - **Tags:** `#mac-project` `#typescript`
  - **Sintesi:** Progetto Mac: Tests. Stack: TypeScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/tests, `file_uri`: file:///Users/pierfrancesco/DataMed/tests, `languages`: ['TypeScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 1, `last_modified`: 2025-12-10T14:57:25.571074+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Uni Match** (`proj-unimatch`)
  - **Tags:** `#mac-project` `#react` `#typescript`
  - **Sintesi:** Progetto Mac: Uni Match. Stack: React, TypeScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UniMatch, `file_uri`: file:///Users/pierfrancesco/Desktop/UniMatch, `languages`: ['TypeScript'], `frameworks`: ['React'], `has_git`: False, `relevant_files_count`: 33, `last_modified`: 2026-03-06T10:58:20.293816+00:00, `key_dependencies`: ['@expo/vector-icons', '@react-navigation/bottom-tabs', '@react-navigation/native', '@react-navigation/native-stack', 'expo', 'expo-asset', 'expo-constants', 'expo-file-system', 'expo-font', 'expo-linear-gradient', 'expo-status-bar', 'react', 'react-native', 'react-native-gesture-handler', 'react-native-safe-area-context'], `readme_excerpt`: 
- **Uni Match 1** (`proj-unimatch-1`)
  - **Tags:** `#c++` `#cpp` `#dart` `#flutter` `#mac-project` `#swift` `#web`
  - **Sintesi:** App Flutter cross-platform (iOS + Android) per il dating tra studenti universitari italiani.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/Desktop/UniMatch-1, `file_uri`: file:///Users/pierfrancesco/Desktop/UniMatch-1, `languages`: ['C++', 'Dart', 'Swift'], `frameworks`: [], `has_git`: True, `relevant_files_count`: 120, `last_modified`: 2026-05-24T10:50:51.634229+00:00, `key_dependencies`: [], `readme_excerpt`: # 🎓 UniMatch — Dating App per Universitari Italiani

App Flutter cross-platform (iOS + Android) per il dating tra studenti universitari italiani.

---

## 📁 Struttura del Progetto

```
unimatch/
├── lib/
│   ├── main.dart                    # Entry point + routing
│   ├── theme/
│   │   └── app_theme.dart           # Colori, tema light/dark
│   ├── models/
│   │   └── models.dart              # UserProfile, MatchModel, MessageModel
│   ├── services/
│   │   ├── auth_service.dart        # Login/registrazione Supabase
│   │   └── encryption_service.dart  # AES-256-GCM E2E + PBKDF2 password
│   ├
- **Utils** (`proj-utils`)
  - **Tags:** `#javascript` `#mac-project` `#typescript`
  - **Sintesi:** Progetto Mac: Utils. Stack: JavaScript, TypeScript.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/src/utils, `file_uri`: file:///Users/pierfrancesco/DataMed/src/utils, `languages`: ['JavaScript', 'TypeScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 2, `last_modified`: 2025-12-10T14:57:25.569220+00:00, `key_dependencies`: [], `readme_excerpt`: 
- **Website** (`proj-website`)
  - **Tags:** `#javascript` `#mac-project` `#web`
  - **Sintesi:** Un sito web moderno e responsivo che contiene Privacy Policy, Termini e Condizioni, FAQ e informazioni di supporto per l'app FedericoII Studenti.
  - **Dettagli:** `local_path`: /Users/pierfrancesco/DataMed/website, `file_uri`: file:///Users/pierfrancesco/DataMed/website, `languages`: ['JavaScript'], `frameworks`: [], `has_git`: False, `relevant_files_count`: 4, `last_modified`: 2026-03-06T18:50:25.763196+00:00, `key_dependencies`: [], `readme_excerpt`: # FedericoII Studenti - Official Website

Un sito web moderno e responsivo che contiene Privacy Policy, Termini e Condizioni, FAQ e informazioni di supporto per l'app FedericoII Studenti.

## ✨ Features

- 🎨 **Design Premium**: Gradients moderni, animazioni fluide, tema scuro e chiaro
- 📱 **Fully Responsive**: Perfetto su mobile, tablet e desktop
- ⚡ **Performance Optimized**: Nessuna dipendenza esterna, CSS/JS inline
- 🌙 **Dark Mode**: Toggle built-in con persistenza tra sessioni
- ♿ **Accessible**: WCAG 2.1 compliant, keyboard navigation, reduced motion support
- 🔒 **Privacy First**: Nessun 

### [Macro-Label: `RELATIONSHIP`]
- **Antonio Renato Chieppa** (`rel-antonio-chieppa`)
  - **Tags:** `#friendship` `#study-partner` `#academic-collaboration`
  - **Sintesi:** Collega di corso e amico con cui condividere appunti, sessioni di studio e motivazione accademica.
  - **Dettagli:** `raw`: `context`: Collaborazione e sostegno nello studio universitario
- **Dominio: Relazioni, Comunicazione & Persone** (`domain-relazioni-comunicazione`)
  - **Tags:** `#domain-hub` `#relazioni` `#comunicazione` `#networking` `#empatia` `#sociale`
  - **Sintesi:** Relazioni Umane, Famiglia, Amici, Networking Professionale, Comunicazione Interpersonale, Empatia e Dinamiche Sociali.
  - **Dettagli:** `scope`: Human relationships, networking, empathy, communication skills
- **Genitori (Madre e Padre)** (`rel-parents`)
  - **Tags:** `#family` `#dedication` `#gratitude` `#roots`
  - **Sintesi:** Punto fermo affettivo e motivazionale; destinatari della dedica di tesi e di supporto concreto continuativo.
  - **Dettagli:** `raw`: `bonds`: Supporto tecnologico madre, dedica formale tesi di laurea padre e madre
- **Marco Di Martino** (`rel-marco-di-martino`)
  - **Tags:** `#friendship` `#university-peer` `#mutual-support`
  - **Sintesi:** Compagno di percorso accademico e amico fidato con cui condividere la crescita universitaria e le sfide di studio.
  - **Dettagli:** `raw`: `context`: Supporto reciproco continuativo durante la laurea in Informatica
- **Mentorship Accademica (Nadia Brancati & Daniel Riccio)** (`rel-academic-mentors`)
  - **Tags:** `#icar-cnr` `#unina` `#thesis` `#mentorship`
  - **Sintesi:** Guide scientifiche del percorso di tesi e ricerca biomedica in Deep Learning presso ICAR-CNR e UniNa.
  - **Dettagli:** `raw`: `supervisor_cnr`: Dr.ssa Nadia Brancati (ICAR-CNR), `advisor_unina`: Prof. Daniel Riccio (UniNa)
- **Radici Partenopee & Territorio** (`rel-napoli-culture`)
  - **Tags:** `#napoli` `#identity` `#culture` `#theatre`
  - **Sintesi:** Forte attaccamento culturale alla città di Napoli, fonte di ispirazione per progetti software, artistici e teatrali.
  - **Dettagli:** `raw`: `city`: Napoli, `influences`: Teatro tradizionale, spirito conviviale, innovazione tecnologica territoriale

### [Macro-Label: `UI_COMPONENT`]
- **3D Force Graph Galaxy Visualizer** (`3d-force-galaxy-view`)
  - **Tags:** `#3d-force-graph` `#webgl` `#threejs` `#galaxy-hud` `#raycasting` `#spatial-split`
  - **Sintesi:** Universo 3D interattivo WebGL in cui i nodi orbitano con forze repulsive e attrattive che li separano ordinatamente lungo l asse X.
  - **Dettagli:** `raw`: `renderer`: WebGL ThreeJS, `particle_speed`: 0.007, `camera_orbit_step`: Math.PI / 1800
- **Animated Gauge Widget (SwiftUI)** (`ui-gauge-widget-alcolsafe`)
  - **Tags:** `#swiftui` `#animated-gauge` `#widget` `#alcolsafe` `#mobile-ui`
  - **Sintesi:** Componente UI nativo SwiftUI per tachimetro/indicatore di stato circolare animato e reattivo.
  - **Dettagli:** `raw`: `framework`: SwiftUI iOS, `component_type`: Dynamic animated circular gauge
- **AuleStudio Student Mobile Interface** (`aule-studio-mobile-ui`)
  - **Tags:** `#mobile-ui` `#clean-design` `#cards` `#seat-map` `#badges` `#student-experience`
  - **Sintesi:** Interfaccia grafica mobile fluida, pulita e minimale orientata a universitari: schede aula immediate, mappa visiva e contatori posti cromatici.
  - **Dettagli:** `raw`: `ui_style`: Modern Minimalist Card-Based, `colors`: {'available': '#10b981', 'crowded': '#f59e0b', 'full': '#ef4444'}
- **Componente UI: Navigatore Multilivello a Piani del Palazzo Cognitivo** (`ui-component-palazzo-cognitivo-multi-layer-navigator`)
  - **Tags:** `#ui-component` `#palazzo-cognitivo` `#elevator-selector` `#multi-layer` `#bento-grid`
  - **Sintesi:** Pannello di navigazione e ascensore cognitivo per esplorare la conoscenza su piani semantici (Attico Domini P0, Progetti P1, Moduli Atomici P2) con pulsanti dedicati, contatori nodi in tempo reale e vista 3D stratificata.
  - **Dettagli:** `raw`: `floors`: {'P0': 'Piano 0: Attico Macro-Domini & Core Hubs (15 nodi)', 'P1': 'Piano 1: Progetti & Aree Tematiche (121 nodi)', 'P2': 'Piano 2: Moduli, Algoritmi & Dettagli Atomici (53 nodi)'}, `navigation_modes`: ['all (Tutti i Piani)', 'vertical (Vista 3D Piani)', '0', '1', '2'], `features`: ['Auto-fit immediato del viewport', 'Ascensori sinaptici evidenziati', 'Zero black-screen filtering']
- **Dynamic Island & Living/Dying Flame** (`streaksup-dynamic-island-ui`)
  - **Tags:** `#dynamic-island` `#live-activity` `#countdown-timer` `#dying-flame`
  - **Sintesi:** Esperienza Live Activity e Dynamic Island con timer conto alla rovescia a mezzanotte, pulsante 'Fatto' rapido e fiamma vivente che si affievolisce con l'avvicinarsi della scadenza.
  - **Dettagli:** `raw`: `regions`: ['compactLeading', 'compactTrailing', 'minimal', 'expanded'], `lock_screen_features`: ['Timer a scomparsa', 'Flame Orb a intensità dinamica', 'Badge streak sicuro', 'Pulsante in-place']
- **Frontend Web Tree Explorer (HUD Button)** (`node-web-tree-explorer`)
  - **Tags:** `#mutation-import` `#presentation-layer` `#ui-component`
  - **Sintesi:** Frontend Web Tree Explorer (HUD Button) (Layer: PRESENTATION_LAYER, Tipo: UI_COMPONENT)
  - **Dettagli:** `raw`: `id`: node_web_tree_explorer, `label`: Frontend Web Tree Explorer (HUD Button), `type`: UI_COMPONENT, `layer`: PRESENTATION_LAYER
- **Glassmorphism Dark Surface Component** (`ui-glass-dark-theme`)
  - **Tags:** `#glassmorphism` `#cards` `#ui-kit`
  - **Sintesi:** Componente contenitore a strati con effetto vetro e bordo ad alta definizione visiva.
  - **Dettagli:** `raw`: `backdrop_filter`: blur(16px) saturate(180%), `background`: rgba(15, 23, 42, 0.75), `border`: 1px solid rgba(0, 210, 255, 0.15)
- **Multi-Format WidgetKit Suite** (`streaksup-widget-suite-ui`)
  - **Tags:** `#widgets` `#lock-screen-complications` `#heatmap` `#daily-progress`
  - **Sintesi:** Suite di 4 widget (Single Habit Focus, Today Dashboard, Daily Progress, Weekly Heatmap) e relative complicanze Lock Screen (circular, rectangular, inline).
  - **Dettagli:** `raw`: `widgets`: ['SingleHabitFocusWidget (small, medium, lock screen)', 'TodayHabitsWidget (medium, large)', 'DailyProgressWidget (small, medium)', 'WeeklyHeatmapWidget (medium, large)']
- **Redesign Pezzi Scacchiera Duolingo Vettoriali** (`design-duolingo-chess-pieces`)
  - **Tags:** `#scacchi` `#duolingo` `#swiftui` `#design-system` `#vettoriale`
  - **Sintesi:** Decisione di redesign dei pezzi degli scacchi con vettori SwiftUI parametrici 2D Duolingo puliti e gerarchia visiva proporzionata.
- **Telegram Bot Interface (Mobile I/O)** (`node-telegram-bot-interface`)
  - **Tags:** `#mutation-import` `#io-layer` `#perceptual-interface`
  - **Sintesi:** Telegram Bot Interface (Mobile I/O) (Layer: IO_LAYER, Tipo: PERCEPTUAL_INTERFACE)
  - **Dettagli:** `raw`: `id`: node_telegram_bot_interface, `label`: Telegram Bot Interface (Mobile I/O), `type`: PERCEPTUAL_INTERFACE, `layer`: IO_LAYER

### [Macro-Label: `UI_DESIGN`]
- **Restyling Frontend Dark-Tech (Graphify & Caveman Aesthetic)** (`feat-dark-tech-frontend-restyle`)
  - **Tags:** `#frontend` `#dark-tech` `#graphify` `#caveman` `#bento-ui` `#ide-topbar` `#cmd-k`
  - **Sintesi:** Restyling estetico completo del frontend in stile ingegneristico d'élite: Topbar IDE unificata a tutta larghezza con HUD sinaptico, canvas con dot-matrix grid, ispettore Bento con badge epistemici e ricerca ⌘K, conservando il 100% delle funzionalità.
  - **Dettagli:** `raw`: `theme`: dark-tech-void, `inspired_by`: graphify.com & caveman.so, `font`: JetBrains Mono & Inter, `topbar`: unified-ide-bar

### [Macro-Label: `UX_FLOW`]
- **Alertless App Icon Switcher Flow** (`streaksup-alertless-icon-ux`)
  - **Tags:** `#method-swizzling` `#app-icon` `#seamless-ux` `#toast-celebration`
  - **Sintesi:** Flusso di cambio icona privo di frizione che silenzia l'alert nativo Apple tramite Method Swizzling su UIViewController e mostra un toast di celebrazione personalizzato.
  - **Dettagli:** `raw`: `swizzling_target`: UIViewController.present(_:animated:completion:), `suppressor`: IconChangeAlertSuppressor, `feedback_view`: AppIconChangedToastView
- **AuleStudio 3-Step Booking UX Flow** (`student-booking-ux-flow`)
  - **Tags:** `#ux-flow` `#frictionless` `#3-steps` `#qr-code` `#quick-reserve`
  - **Sintesi:** Flusso di prenotazione a zero attrito: 1. Scegli Polo/Aula -> 2. Seleziona Fascia Oraria -> 3. Conferma e genera pass QR d ingresso.
  - **Dettagli:** `raw`: `step_1`: Cerca aula per vicinanza e posti liberi, `step_2`: Seleziona postazione e orario, `step_3`: Ricevi badge QR istantaneo
- **Frictionless Thumb-Zone Flow** (`ux-frictionless-flow`)
  - **Tags:** `#ux` `#ergonomics` `#mobile-first` `#micro-interactions`
  - **Sintesi:** Esperienza d'uso priva di ostacoli con azioni chiave aggregate nell'area di raggiungibilità del pollice (Thumb Zone 44x44pt).
  - **Dettagli:** `raw`: `animation_duration`: 150ms-250ms, `easing`: cubic-bezier(0.4, 0.0, 0.2, 1), `min_touch_target`: 44x44pt
- **UX ad Ergonomia Immediata (Thumb Zone)** (`ux-frictionless`)
  - **Tags:** `#ux` `#mobile-first` `#ergonomics` `#feedback`
  - **Sintesi:** Interfacce prive di frizione con controlli primari nella zona del pollice e transizioni ultra-reattive (150-250ms).
  - **Dettagli:** `raw`: `touch_target_min`: 44x44pt, `animation_easing`: cubic-bezier(0.4, 0.0, 0.2, 1), `onboarding_style`: Zero-friction, affordance-guided


## CONNESSIONI TRASVERSALI (Corpo Calloso & Struttura)
### Ponti Inter-Emisfero (Corpo Calloso):
- (`aule-studio-app`) --[ADOPTS_FLOW]--> (`ux-frictionless-flow`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ADOPTS_RULE]--> (`caveman-communication-protocol`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ADVOCATES]--> (`mental-centaur-model`) *(Corpo Calloso)*
- (`ai-reasoning-domain-subgraph-modularity`) --[ANALYZES_EPISODE]--> (`episode-2026-08-27-modular-domain-graph-topology`) *(Corpo Calloso)*
- (`ai-reasoning-gabaergic-gating-formalization`) --[ANALYZES_EPISODE]--> (`episode-2026-08-27-interhemispheric-inhibition-design`) *(Corpo Calloso)*
- (`ai-reasoning-hypergraph-multi-scale-feasibility`) --[ANALYZES_EPISODE]--> (`episode-2026-08-27-fractal-graph-of-graphs-evaluation`) *(Corpo Calloso)*
- (`reason-ep-20260827-graph-taxonomy-classification`) --[ANALYZES_EPISODE]--> (`ep-20260827-graph-taxonomy-classification`) *(Corpo Calloso)*
- (`reason-ep-20260827-graph-tree-unification`) --[ANALYZES_EPISODE]--> (`ep-20260827-graph-tree-unification`) *(Corpo Calloso)*
- (`reason-ep-20260827-hierarchical-overlay-reassurance`) --[ANALYZES_EPISODE]--> (`ep-20260827-hierarchical-overlay-reassurance`) *(Corpo Calloso)*
- (`reason-ep-20260827-hierarchical-tree-deployment-sync`) --[ANALYZES_EPISODE]--> (`ep-20260827-hierarchical-tree-deployment-sync`) *(Corpo Calloso)*
- (`reason-ep-20260827-telegram-bot-interface`) --[ANALYZES_EPISODE]--> (`ep-20260827-telegram-bot-interface`) *(Corpo Calloso)*
- (`reason-ep-20260827-telegram-cognitive-hub-spec`) --[ANALYZES_EPISODE]--> (`ep-20260827-telegram-cognitive-hub-spec`) *(Corpo Calloso)*
- (`reason-ep-20260827-tree-ranking-translation`) --[ANALYZES_EPISODE]--> (`ep-20260827-tree-ranking-translation`) *(Corpo Calloso)*
- (`reason-ep-20260827-tree-structures-evaluation`) --[ANALYZES_EPISODE]--> (`ep-20260827-tree-structures-evaluation`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[APPLIES]--> (`rule-zero-cost`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECTED]--> (`proj-unicampus`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECTED_AND_DEVELOPED]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECT_AND_CREATOR]--> (`domain-ai-cognitive-systems`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECT_AND_CREATOR]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECT_AND_CREATOR]--> (`domain-software-engineering`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ARCHITECT_OF]--> (`universal-ai-brain`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[AUTHORED]--> (`proj-kdp-ai-guide`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[AUTHOR_OF]--> (`proj-kdp-ai-book`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`continuous-ai-symbiosis`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-multi-llm-mcp-ecosystem`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-modular-domain-graph-topology`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-fractal-graph-of-graphs-evaluation`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`chat-session-2026-08-27-ui-evolution`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-graphrag-mcp-evolution`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-telegram-omnipresence`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-2026-08-27-tree-structures-evaluation`) *(Corpo Calloso)*
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`episode-cross-model-memory-architecture`) *(Corpo Calloso)*
- (`node-nota-rapida-raycast-test`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`) *(Corpo Calloso)*
- (`proj-appalcool`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-caretrack-demo`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-docs_md`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-federicoiiapp`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-missing-feedback`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-scripts`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-tests`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-utils`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`proj-website`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`ai-reasoning-cross-model-provenance-validation`) --[BELONGS_TO_EPISODE]--> (`episode-cross-model-memory-architecture`) *(Corpo Calloso)*
- (`ai-reasoning-hybrid-cloud-local-symbiosis`) --[BELONGS_TO_EPISODE]--> (`ep-20260827-render-cloud-vs-local-hybrid-architecture`) *(Corpo Calloso)*
- (`ai-reasoning-infinite-context-architecture`) --[BELONGS_TO_EPISODE]--> (`episode-infinite-context-philosophy`) *(Corpo Calloso)*
- (`ai-reasoning-shared-cognitive-state-continuity`) --[BELONGS_TO_EPISODE]--> (`episode-2026-08-27-universal-context-definition`) *(Corpo Calloso)*
- (`concept-llm-indirect-injection-safeguard`) --[BELONGS_TO_EPISODE]--> (`ep-20260827-render-cloud-vs-local-hybrid-architecture`) *(Corpo Calloso)*
- (`goal-multi-ai-shared-context-persistence`) --[BELONGS_TO_EPISODE]--> (`episode-2026-08-27-universal-context-definition`) *(Corpo Calloso)*
- (`intent-clarify-render-cloud-utility-and-llm-web-refusal`) --[BELONGS_TO_EPISODE]--> (`ep-20260827-render-cloud-vs-local-hybrid-architecture`) *(Corpo Calloso)*
- (`intent-evaluate-ai-brain-architecture`) --[BELONGS_TO_EPISODE]--> (`episode-system-metacognition`) *(Corpo Calloso)*
- (`intent-language-app-ui-design`) --[BELONGS_TO_EPISODE]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`intent-personal-language-app-structure`) --[BELONGS_TO_EPISODE]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`intent-personal-language-learning-app`) --[BELONGS_TO_EPISODE]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`reasoning-language-app-architecture`) --[BELONGS_TO_EPISODE]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`user-intent-infinite-context-persistence`) --[BELONGS_TO_EPISODE]--> (`episode-infinite-context-philosophy`) *(Corpo Calloso)*
- (`user-intent-provenance-model-tracking`) --[BELONGS_TO_EPISODE]--> (`episode-cross-model-memory-architecture`) *(Corpo Calloso)*
- (`proj-harmonyapp`) --[BRIDGES_TO]--> (`art-piano-composition`) *(Corpo Calloso)*
- (`proj-tombolawifi`) --[CELEBRATES]--> (`rel-napoli-culture`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[COMMISSIONED]--> (`feat-light-terminal`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[COMMISSIONED]--> (`feat-progressive-areas`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[COMMITTED_TO]--> (`zero-debt-cost-rule`) *(Corpo Calloso)*
- (`brand-voice-surgical`) --[COMPLEMENTS]--> (`rule-zero-placeholder`) *(Corpo Calloso)*
- (`aule-studio-app`) --[CONTAINS_MODULE]--> (`aule-studio-mobile-ui`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`3d-force-galaxy-view`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`ui-gauge-widget-alcolsafe`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`ui-glass-dark-theme`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`student-booking-ux-flow`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`ux-frictionless-flow`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`node-telegram-bot-interface`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`node-web-tree-explorer`) *(Corpo Calloso)*
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`ux-frictionless`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-flame-palette`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-glassmorphism-system`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-dynamic-island-ui`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-alertless-icon-ux`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-particle-fx`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-privacy-zero-cloud`) *(Corpo Calloso)*
- (`streaksup-app-intents-engine`) --[CONTROLS_IN_PLACE]--> (`streaksup-dynamic-island-ui`) *(Corpo Calloso)*
- (`ai-reasoning-cross-model-provenance-validation`) --[CORPUS_CALLOSUM_LINK]--> (`episode-cross-model-memory-architecture`) *(Corpo Calloso)*
- (`ai-reasoning-infinite-context-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`episode-infinite-context-philosophy`) *(Corpo Calloso)*
- (`ai-reasoning-infinite-context-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`val-eternal-cognitive-continuity`) *(Corpo Calloso)*
- (`ai-reasoning-shared-cognitive-state-continuity`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-universal-context-definition`) *(Corpo Calloso)*
- (`antigravity-centaur-collaboration`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`) *(Corpo Calloso)*
- (`art-creative-writing`) --[CORPUS_CALLOSUM_LINK]--> (`proj-kdp-ai-guide`) *(Corpo Calloso)*
- (`art-piano-composition`) --[CORPUS_CALLOSUM_LINK]--> (`proj-harmonyapp`) *(Corpo Calloso)*
- (`brand-voice-engineering`) --[CORPUS_CALLOSUM_LINK]--> (`identity-cs-researcher`) *(Corpo Calloso)*
- (`brand-voice-surgical`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-placeholder`) *(Corpo Calloso)*
- (`creative-multidisciplinary`) --[CORPUS_CALLOSUM_LINK]--> (`proj-kdp-ai-book`) *(Corpo Calloso)*
- (`design-cyber-neon`) --[CORPUS_CALLOSUM_LINK]--> (`proj-specula`) *(Corpo Calloso)*
- (`design-language-app-system`) --[CORPUS_CALLOSUM_LINK]--> (`intent-language-app-ui-design`) *(Corpo Calloso)*
- (`episode-2026-08-27-graphrag-mcp-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`session-continuous-evolution`) *(Corpo Calloso)*
- (`episode-2026-08-27-graphrag-mcp-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`) *(Corpo Calloso)*
- (`episode-2026-08-27-telegram-omnipresence`) --[CORPUS_CALLOSUM_LINK]--> (`session-continuous-evolution`) *(Corpo Calloso)*
- (`episode-2026-08-27-tree-structures-evaluation`) --[CORPUS_CALLOSUM_LINK]--> (`session-continuous-evolution`) *(Corpo Calloso)*
- (`episode-2026-08-27-universal-context-definition`) --[CORPUS_CALLOSUM_LINK]--> (`ai-reasoning-shared-cognitive-state-continuity`) *(Corpo Calloso)*
- (`episode-2026-08-27-universal-context-definition`) --[CORPUS_CALLOSUM_LINK]--> (`goal-multi-ai-shared-context-persistence`) *(Corpo Calloso)*
- (`episode-cross-model-memory-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`ai-reasoning-cross-model-provenance-validation`) *(Corpo Calloso)*
- (`episode-cross-model-memory-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`user-intent-provenance-model-tracking`) *(Corpo Calloso)*
- (`episode-infinite-context-philosophy`) --[CORPUS_CALLOSUM_LINK]--> (`ai-reasoning-infinite-context-architecture`) *(Corpo Calloso)*
- (`episode-infinite-context-philosophy`) --[CORPUS_CALLOSUM_LINK]--> (`user-intent-infinite-context-persistence`) *(Corpo Calloso)*
- (`episode-language-app-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`intent-personal-language-learning-app`) *(Corpo Calloso)*
- (`episode-language-app-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`reasoning-language-app-architecture`) *(Corpo Calloso)*
- (`episode-system-metacognition`) --[CORPUS_CALLOSUM_LINK]--> (`reasoning-brain-architecture-analysis`) *(Corpo Calloso)*
- (`episode-system-metacognition`) --[CORPUS_CALLOSUM_LINK]--> (`intent-evaluate-ai-brain-architecture`) *(Corpo Calloso)*
- (`feat-ai-json-importer`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`feat-copy-ai-prompt`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`feat-light-terminal`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`goal-multi-ai-shared-context-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-universal-context-definition`) *(Corpo Calloso)*
- (`goal-multi-ai-shared-context-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`idea-hierarchical-weighted-trees`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-tree-structures-evaluation`) *(Corpo Calloso)*
- (`identity-cs-researcher`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-engineering`) *(Corpo Calloso)*
- (`intent-evaluate-ai-brain-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`episode-system-metacognition`) *(Corpo Calloso)*
- (`intent-language-app-ui-design`) --[CORPUS_CALLOSUM_LINK]--> (`design-language-app-system`) *(Corpo Calloso)*
- (`intent-language-app-ui-design`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`intent-personal-language-app-structure`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`intent-personal-language-learning-app`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`lesson-stoic-resilience`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-placeholder`) *(Corpo Calloso)*
- (`memory-perfectionism-tension`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-placeholder`) *(Corpo Calloso)*
- (`mental-centaur-model`) --[CORPUS_CALLOSUM_LINK]--> (`art-creative-writing`) *(Corpo Calloso)*
- (`mental-centaur-model`) --[CORPUS_CALLOSUM_LINK]--> (`val-authenticity`) *(Corpo Calloso)*
- (`proj-alcolsafe`) --[CORPUS_CALLOSUM_LINK]--> (`val-impact-utility`) *(Corpo Calloso)*
- (`proj-caretrack`) --[CORPUS_CALLOSUM_LINK]--> (`val-impact-utility`) *(Corpo Calloso)*
- (`proj-cinematch`) --[CORPUS_CALLOSUM_LINK]--> (`ux-frictionless`) *(Corpo Calloso)*
- (`proj-harmonyapp`) --[CORPUS_CALLOSUM_LINK]--> (`art-piano-composition`) *(Corpo Calloso)*
- (`proj-holly-benji-ai`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-engineering`) *(Corpo Calloso)*
- (`proj-kdp-ai-book`) --[CORPUS_CALLOSUM_LINK]--> (`creative-multidisciplinary`) *(Corpo Calloso)*
- (`proj-kdp-ai-guide`) --[CORPUS_CALLOSUM_LINK]--> (`art-creative-writing`) *(Corpo Calloso)*
- (`proj-linkly-qr`) --[CORPUS_CALLOSUM_LINK]--> (`ux-frictionless`) *(Corpo Calloso)*
- (`proj-napolilive`) --[CORPUS_CALLOSUM_LINK]--> (`rel-napoli-culture`) *(Corpo Calloso)*
- (`proj-particlesimulator`) --[CORPUS_CALLOSUM_LINK]--> (`art-piano-composition`) *(Corpo Calloso)*
- (`proj-specula`) --[CORPUS_CALLOSUM_LINK]--> (`design-cyber-neon`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-glassmorphism-system`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-flame-palette`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-privacy-zero-cloud`) *(Corpo Calloso)*
- (`proj-tombolawifi`) --[CORPUS_CALLOSUM_LINK]--> (`rel-napoli-culture`) *(Corpo Calloso)*
- (`reasoning-hybrid-pedagogy-engine`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`reasoning-language-app-architecture`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`) *(Corpo Calloso)*
- (`rel-napoli-culture`) --[CORPUS_CALLOSUM_LINK]--> (`proj-napolilive`) *(Corpo Calloso)*
- (`rel-napoli-culture`) --[CORPUS_CALLOSUM_LINK]--> (`proj-tombolawifi`) *(Corpo Calloso)*
- (`rigore-informativo`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-surgical`) *(Corpo Calloso)*
- (`rigore-informativo`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`rule-cloud-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`rule-zero-cost`) --[CORPUS_CALLOSUM_LINK]--> (`val-independence`) *(Corpo Calloso)*
- (`rule-zero-placeholder`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-surgical`) *(Corpo Calloso)*
- (`session-continuous-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`streaksup-alertless-icon-ux`) --[CORPUS_CALLOSUM_LINK]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`streaksup-app-intents-engine`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-dynamic-island-ui`) *(Corpo Calloso)*
- (`streaksup-app-intents-engine`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`streaksup-darwin-ipc-protocol`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`streaksup-dynamic-island-ui`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-app-intents-engine`) *(Corpo Calloso)*
- (`streaksup-flame-palette`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-streak-freeze-algo`) *(Corpo Calloso)*
- (`streaksup-flame-palette`) --[CORPUS_CALLOSUM_LINK]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`streaksup-gamification-engine`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-particle-fx`) *(Corpo Calloso)*
- (`streaksup-glassmorphism-system`) --[CORPUS_CALLOSUM_LINK]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`streaksup-i18n-runtime-engine`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`streaksup-particle-fx`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-gamification-engine`) *(Corpo Calloso)*
- (`streaksup-privacy-zero-cloud`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-swiftdata-arch`) *(Corpo Calloso)*
- (`streaksup-privacy-zero-cloud`) --[CORPUS_CALLOSUM_LINK]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`streaksup-streak-freeze-algo`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-flame-palette`) *(Corpo Calloso)*
- (`streaksup-swiftdata-arch`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-privacy-zero-cloud`) *(Corpo Calloso)*
- (`streaksup-widget-suite-ui`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-app-intents-engine`) *(Corpo Calloso)*
- (`streaksup-widget-suite-ui`) --[CORPUS_CALLOSUM_LINK]--> (`streaksup-darwin-ipc-protocol`) *(Corpo Calloso)*
- (`user-intent-infinite-context-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`episode-infinite-context-philosophy`) *(Corpo Calloso)*
- (`user-intent-infinite-context-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`val-eternal-cognitive-continuity`) *(Corpo Calloso)*
- (`user-intent-provenance-model-tracking`) --[CORPUS_CALLOSUM_LINK]--> (`episode-cross-model-memory-architecture`) *(Corpo Calloso)*
- (`user-intent-telegram-bot-gateway`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-telegram-omnipresence`) *(Corpo Calloso)*
- (`user-intent-telegram-bot-gateway`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-tree-search-enhancement`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-tree-structures-evaluation`) *(Corpo Calloso)*
- (`user-intent-tree-search-enhancement`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-zero-cost-graphrag`) --[CORPUS_CALLOSUM_LINK]--> (`episode-2026-08-27-graphrag-mcp-evolution`) *(Corpo Calloso)*
- (`user-intent-zero-cost-graphrag`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-zero-oscillation-high-performance-graph`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`ux-frictionless`) --[CORPUS_CALLOSUM_LINK]--> (`proj-caretrack`) *(Corpo Calloso)*
- (`ux-frictionless`) --[CORPUS_CALLOSUM_LINK]--> (`proj-linkly-qr`) *(Corpo Calloso)*
- (`val-eternal-cognitive-continuity`) --[CORPUS_CALLOSUM_LINK]--> (`ai-reasoning-infinite-context-architecture`) *(Corpo Calloso)*
- (`val-eternal-cognitive-continuity`) --[CORPUS_CALLOSUM_LINK]--> (`user-intent-infinite-context-persistence`) *(Corpo Calloso)*
- (`val-impact-utility`) --[CORPUS_CALLOSUM_LINK]--> (`proj-alcolsafe`) *(Corpo Calloso)*
- (`val-impact-utility`) --[CORPUS_CALLOSUM_LINK]--> (`proj-caretrack`) *(Corpo Calloso)*
- (`val-independence`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[CREATED]--> (`proj-napolilive`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[CREATED]--> (`proj-tombolawifi`) *(Corpo Calloso)*
- (`proj-1-minimal`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-10-funptr`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-12-templates`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-2`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-2-structured`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-3-basictypes`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-4-allocation`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-5-usertypes`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-6-iostream`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-7-string`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-8-psecasgen`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-accentcolor-colorset`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-advanceddb-mod-db-tech`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-algebra`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-appabbonamenti`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-appaulestudiotypescript`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-appcalcolatori`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-appicon-appiconset`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-appnapoli`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-apptombola`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-asd-lasd`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-auth_screens`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-basi-di-dati-esercizi`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-bdd`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-binari`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-book`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-calm-raman`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-cervelloartificiale`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-ciscocertification`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-codice_architettura_tesi`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-compito-luglio`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-compito-settembre`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-composetest`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-cose_laurea`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-eager-pasteur`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-economia`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-eserciziocontocorrente`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-example`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-examples`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-fantaformula1`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-foodlab2025`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-gennaio-2021`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-gioco`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-giocoscacchi`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-giugno-2021`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-gods-eye-view-main`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-googlecertificate`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-habittracker`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-happy-plant-keeper`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-ingsw`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-jules_session_5370203018288358434`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-lp---prova-esame-giugno`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-lp1`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-lso`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-macpulse2tests`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-macpulse2uitests`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-macpulsetests`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-macpulseuitests`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-marzo-2021`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-ml-neural-networks-dl`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-new-project`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-new_chapters`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-nvidiacertification`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-oo`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-osmci`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-outputs`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-pack3`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-pack4`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-palazzo`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-particle-engine-simulation`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-pdc`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-pgf-pie`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-pierfrancescoamendola`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-posgresql-pgadmin`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-progetto-gestione-bibloteca`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-propedia-demo`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-psld1`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-psld2-senza-git`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-qr_generator`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render1`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render2`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render3`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_final`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_pdf_temp`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_proof_1`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_proof_final`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_revision`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-render_revision_final`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-rendered`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-rendered_v2`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-reti-di-calcolatori`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-sample`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-sim`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-sitocertificati`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-slidetecweb`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-soluzionepostgress_pgadmin_prof`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-source_chapters`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-spiegazione-codice-librerire`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-statistica`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-svolti`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-taste-skill`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-tecweblezioni`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-testrepo-main`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-tscheck`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-uni-grade-projections-main`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-unistats`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-videoyt`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`proj-workspace`) --[CREATED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[CREATOR_OF]--> (`aule-studio-app`) *(Corpo Calloso)*
- (`concept-interhemispheric-inhibition-gating`) --[CROSS_CALLOSAL_INHIBITION]--> (`domain-filosofia-valori`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DECLARED]--> (`user-intent-zero-cost-graphrag`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEFINED]--> (`feat-copy-ai-prompt`) *(Corpo Calloso)*
- (`caveman-communication-protocol`) --[DEFINES_VOICE]--> (`terse-caveman-brand-voice`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEPLOYED]--> (`proj-specula`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEPLOYED]--> (`proj-linkly-qr`) *(Corpo Calloso)*
- (`node-commit-62e48df`) --[DEPLOYS_TO_PRODUCTION]--> (`node-hierarchical-tree-engine-impl`) *(Corpo Calloso)*
- (`proj-specula`) --[DERIVES_FROM]--> (`design-cyber-neon`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEVELOPED]--> (`proj-alcolsafe`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEVELOPED]--> (`proj-cinematch`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[DEVELOPED]--> (`proj-caretrack`) *(Corpo Calloso)*
- (`user-intent-clean-clustered-ui`) --[DISCUSSED_IN]--> (`chat-session-2026-08-27-ui-evolution`) *(Corpo Calloso)*
- (`user-intent-reasoning-and-chat-memory`) --[DISCUSSED_IN]--> (`chat-session-2026-08-27-ui-evolution`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[DISPLAYS_ON]--> (`streaksup-dynamic-island-ui`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EMBODIES_PROFILE]--> (`identity-cs-researcher`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[EMBODIES_VALUE]--> (`streaksup-privacy-zero-cloud`) *(Corpo Calloso)*
- (`node-telegram-bot-interface`) --[ENABLES]--> (`node-ubiquitous-ingestion`) *(Corpo Calloso)*
- (`ai-memory-ingest-spec`) --[ENABLES_PERSISTENCE]--> (`continuous-ai-symbiosis`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ENFORCES]--> (`rule-zero-placeholder`) *(Corpo Calloso)*
- (`zero-debt-cost-rule`) --[ENFORCES_MINIMALISM]--> (`cyber-slate-space-aesthetic`) *(Corpo Calloso)*
- (`streaksup-alertless-icon-ux`) --[ENHANCES_EXPERIENCE_OF]--> (`proj-streaksup-app`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ESTABLISHED]--> (`tax-ai-reasoning`) *(Corpo Calloso)*
- (`reason-ep-20260827-hierarchical-tree-deployment-sync`) --[ESTABLISHES_CONCEPT]--> (`node-web-tree-explorer`) *(Corpo Calloso)*
- (`reason-ep-20260827-hierarchical-tree-deployment-sync`) --[ESTABLISHES_CONCEPT]--> (`node-commit-62e48df`) *(Corpo Calloso)*
- (`reason-ep-20260827-telegram-bot-interface`) --[ESTABLISHES_CONCEPT]--> (`node-telegram-bot-interface`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[EXPORTS_WIDGETS]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-graph-taxonomy-classification`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-graph-tree-unification`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-hierarchical-overlay-reassurance`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-hierarchical-tree-deployment-sync`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-telegram-bot-interface`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-telegram-cognitive-hub-spec`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-tree-ranking-translation`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[EXPRESSED]--> (`intent-ep-20260827-tree-structures-evaluation`) *(Corpo Calloso)*
- (`intent-clarify-render-cloud-utility-and-llm-web-refusal`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`node-test-raycast-node`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-abbandono-jarvis-nuovo-progetto`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-accorciamento-cappello-capitolo-6`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ai-shorts-evaluation`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-allineamento-nodi-render`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-alternative-income-generation`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-analisi-feedback-gemini-ottimizzazione-cervello`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-architettura-connettoma-web-vs-desktop`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-audit-critico-e-mockup-fr-2255`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-avvio-openjarvis-ollama-gpt-cloud`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-backend-optimization-hybrid`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-c-un-problema-vorrei-sapere-di-pi-3203`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-che-ne-pensi-del-mio-cervello-artif-8743`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-che-ne-pensi-del-mio-cervello-artif-8793`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-che-ore-sono-3134`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-chi-pierfrancesco-amendola-e-cosa-8426`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-chiarimento-stack-rendering-grafi-frontend`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-cloud-git-auto-push`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-comando-prompt-copia-rapi-8585`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-confronto-integrazioni-llm-notion-obsidian`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-creazione-jarvis-voice-assistant`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-creazione-repo-jarvis-desktop`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-creazione-video-showcase-universal-brain`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-definizione-ecografo-trasduttore-lineare`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-distro-linux-modellazione-3d`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-2447`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-2471`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-2485`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-2529`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-2691`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-8745`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-e2e-test-session-hook-9065`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-embedding-projector-globe-and-optics`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-espansione-supercervello-integrazioni`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-esplorazione-paradigmi-visuali-grafo`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-fix-daemon-render-persistence`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-implementazione-ecosistema-supercervello`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-integrazione-openjarvis-stanford`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-integrazione-tabelle-cappello-capitolo-6`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-jarvis-ricordi-quali-sono-gli-emis-3117`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ma-tutto-falso-8462`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-non-riesci-a-connetterti-al-mio-cer-8486`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-nuove-rappresentazioni-vi-2874`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-occultamento-pulsanti-mob-9019`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ottimizzazione-mobile-web-8880`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-potenziamento-cognitivo-obsidian-bridge`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-potenziamento-skill-e-ril-8338`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-quali-sono-i-progetti-principali-di-8169`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-quali-sono-le-abitudini-monitorate-2979`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-review-piano-supercervello-os`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-rimozione-modello-ollama-mac`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ristrutturazione-sigillo-12-macro-domini`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-spiegazione-intuitiva-concetti-causali-attention`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-spiegazione-swin-transformer-deep-stable-learning`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-telegram-keepalive-confirmation`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-test-hook-session-end-2411`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-ui-declutter-projector-fullscreen`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-universal-ai-hub-client`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-update-readme-architecture`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-valutazione-progetto-language-app`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-verifica-vincolo-zero-costi`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-verify-github-token-render`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2471`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2485`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2529`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2690`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-8745`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-9065`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`voice-test-shortcuts-debug-7964`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`web-test-fastapi-docs`) --[EXPRESSED_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`user-intent-infinite-context-persistence`) --[EXPRESSES]--> (`val-eternal-cognitive-continuity`) *(Corpo Calloso)*
- (`episode-2026-08-27-graphrag-mcp-evolution`) --[EXTENDS]--> (`session-continuous-evolution`) *(Corpo Calloso)*
- (`aule-studio-backend-arch`) --[FEEDS_DATA_TO]--> (`student-booking-ux-flow`) *(Corpo Calloso)*
- (`ai-reasoning-hybrid-search-mcp`) --[FORMULATES]--> (`episode-2026-08-27-graphrag-mcp-evolution`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-ai-cognitive-systems`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-finanza-economia`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-medicina-salute`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-produttivita-sistemi`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-scienza-matematica`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-software-engineering`) *(Corpo Calloso)*
- (`proj-alcolsafe`) --[FULFILLS]--> (`val-impact-utility`) *(Corpo Calloso)*
- (`proj-caretrack`) --[FULFILLS]--> (`val-impact-utility`) *(Corpo Calloso)*
- (`identity-cs-researcher`) --[HARMONIZES]--> (`creative-multidisciplinary`) *(Corpo Calloso)*
- (`proj-napolilive`) --[HONORS]--> (`rel-napoli-culture`) *(Corpo Calloso)*
- (`proj-linkly-qr`) --[IMPLEMENTS]--> (`ux-frictionless`) *(Corpo Calloso)*
- (`project-royal-gambit-chess`) --[IMPLEMENTS]--> (`design-duolingo-chess-system`) *(Corpo Calloso)*
- (`universal-ai-brain`) --[IMPLEMENTS_UI]--> (`feat-dark-tech-frontend-restyle`) *(Corpo Calloso)*
- (`proj-alcolsafe`) --[INCORPORATES_UI]--> (`ui-gauge-widget-alcolsafe`) *(Corpo Calloso)*
- (`user-intent-frontend-professional-restyle`) --[INSPIRED]--> (`feat-dark-tech-frontend-restyle`) *(Corpo Calloso)*
- (`session-continuous-evolution`) --[INSTANTIATES]--> (`antigravity-centaur-collaboration`) *(Corpo Calloso)*
- (`node-telegram-bot-interface`) --[INTERFACES_WITH]--> (`node-knowledge-graph-memory`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[MANDATES]--> (`rule-cloud-persistence`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[MASTERS_STACK]--> (`flutter-dart-ecosystem`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[MASTERS_STACK]--> (`fastapi-python-stack`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[ORCHESTRATED]--> (`session-continuous-evolution`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[OWNS]--> (`project-royal-gambit-chess`) *(Corpo Calloso)*
- (`arch-telegram-webhook-gateway`) --[PART_OF]--> (`episode-2026-08-27-telegram-omnipresence`) *(Corpo Calloso)*
- (`idea-hierarchical-weighted-trees`) --[PART_OF]--> (`episode-2026-08-27-tree-structures-evaluation`) *(Corpo Calloso)*
- (`intent-ep-20260827-graph-taxonomy-classification`) --[PART_OF_EPISODE]--> (`ep-20260827-graph-taxonomy-classification`) *(Corpo Calloso)*
- (`intent-ep-20260827-graph-tree-unification`) --[PART_OF_EPISODE]--> (`ep-20260827-graph-tree-unification`) *(Corpo Calloso)*
- (`intent-ep-20260827-hierarchical-overlay-reassurance`) --[PART_OF_EPISODE]--> (`ep-20260827-hierarchical-overlay-reassurance`) *(Corpo Calloso)*
- (`intent-ep-20260827-hierarchical-tree-deployment-sync`) --[PART_OF_EPISODE]--> (`ep-20260827-hierarchical-tree-deployment-sync`) *(Corpo Calloso)*
- (`intent-ep-20260827-telegram-bot-interface`) --[PART_OF_EPISODE]--> (`ep-20260827-telegram-bot-interface`) *(Corpo Calloso)*
- (`intent-ep-20260827-telegram-cognitive-hub-spec`) --[PART_OF_EPISODE]--> (`ep-20260827-telegram-cognitive-hub-spec`) *(Corpo Calloso)*
- (`intent-ep-20260827-tree-ranking-translation`) --[PART_OF_EPISODE]--> (`ep-20260827-tree-ranking-translation`) *(Corpo Calloso)*
- (`intent-ep-20260827-tree-structures-evaluation`) --[PART_OF_EPISODE]--> (`ep-20260827-tree-structures-evaluation`) *(Corpo Calloso)*
- (`user-intent-biological-lazy-loading-inhibition`) --[PART_OF_EPISODE]--> (`episode-2026-08-27-interhemispheric-inhibition-design`) *(Corpo Calloso)*
- (`user-intent-connect-gemini-claude-chatgpt-mcp`) --[PART_OF_EPISODE]--> (`episode-2026-08-27-multi-llm-mcp-ecosystem`) *(Corpo Calloso)*
- (`user-intent-hierarchical-multi-layer-graph-design`) --[PART_OF_EPISODE]--> (`episode-2026-08-27-fractal-graph-of-graphs-evaluation`) *(Corpo Calloso)*
- (`user-intent-modular-cluster-decentralization`) --[PART_OF_EPISODE]--> (`episode-2026-08-27-modular-domain-graph-topology`) *(Corpo Calloso)*
- (`proj-caretrack-demo-ui-layer`) --[PART_OF_PROJECT]--> (`proj-caretrack-demo`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[PLANNED]--> (`user-intent-telegram-bot-gateway`) *(Corpo Calloso)*
- (`taxonomy-deterministic-floor-classification-engine`) --[POWERS_HIERARCHY]--> (`ui-component-palazzo-cognitivo-multi-layer-navigator`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[PREFERS]--> (`rigore-informativo`) *(Corpo Calloso)*
- (`episode-frontend-deeptech-redesign-and-physics-zero-lag`) --[PRODUCED_ARCHITECTURE]--> (`architecture-vis-network-silent-stabilization-zero-lag`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[PROPOSED]--> (`user-intent-tree-search-enhancement`) *(Corpo Calloso)*
- (`aule-studio-app`) --[PROVIDES_FLOW]--> (`student-booking-ux-flow`) *(Corpo Calloso)*
- (`kindle-c962fde43767`) --[READ_BY]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`ai-reasoning-episodic-memory-architecture`) --[REASONED_DURING]--> (`chat-session-2026-08-27-ui-evolution`) *(Corpo Calloso)*
- (`universal-ai-brain`) --[RECORDED_EPISODE]--> (`chat-session-2026-08-27-ui-evolution`) *(Corpo Calloso)*
- (`episode-20260829-architettura-connettoma-e-sync-prompt`) --[RECORDS_INTENT]--> (`user-intent-architettura-connettoma-web-vs-desktop`) *(Corpo Calloso)*
- (`episode-20260829-avvio-intervista-universal-ai-hub`) --[RECORDS_INTENT]--> (`user-intent-universal-ai-hub-client`) *(Corpo Calloso)*
- (`episode-20260829-chiusura-jarvis-nuovo-progetto`) --[RECORDS_INTENT]--> (`user-intent-abbandono-jarvis-nuovo-progetto`) *(Corpo Calloso)*
- (`episode-20260829-completamento-rilascio-jarvis-desktop`) --[RECORDS_INTENT]--> (`user-intent-creazione-repo-jarvis-desktop`) *(Corpo Calloso)*
- (`episode-20260829-debrief-assessment-gemini`) --[RECORDS_INTENT]--> (`user-intent-analisi-feedback-gemini-ottimizzazione-cervello`) *(Corpo Calloso)*
- (`episode-20260829-definizione-piano-jarvis-desktop`) --[RECORDS_INTENT]--> (`user-intent-creazione-repo-jarvis-desktop`) *(Corpo Calloso)*
- (`episode-20260829-esplorazione-paradigmi-interfaccia-grafo`) --[RECORDS_INTENT]--> (`user-intent-esplorazione-paradigmi-visuali-grafo`) *(Corpo Calloso)*
- (`episode-20260829-integrazione-openjarvis-desktop`) --[RECORDS_INTENT]--> (`user-intent-integrazione-openjarvis-stanford`) *(Corpo Calloso)*
- (`episode-20260829-progettazione-jarvis-voice-ai`) --[RECORDS_INTENT]--> (`user-intent-creazione-jarvis-voice-assistant`) *(Corpo Calloso)*
- (`episode-20260829-sigillatura-12-macro-domini`) --[RECORDS_INTENT]--> (`user-intent-ristrutturazione-sigillo-12-macro-domini`) *(Corpo Calloso)*
- (`episode-20260829-test-openjarvis-ollama-successo`) --[RECORDS_INTENT]--> (`user-intent-avvio-openjarvis-ollama-gpt-cloud`) *(Corpo Calloso)*
- (`episode-allineamento-nodi-render-cloud`) --[RECORDS_INTENT]--> (`user-intent-allineamento-nodi-render`) *(Corpo Calloso)*
- (`episode-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[RECORDS_INTENT]--> (`user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690`) *(Corpo Calloso)*
- (`episode-alternative-monetization-brainstorming`) --[RECORDS_INTENT]--> (`user-intent-alternative-income-generation`) *(Corpo Calloso)*
- (`episode-audit-critico-e-mockup-fr-2255`) --[RECORDS_INTENT]--> (`user-intent-audit-critico-e-mockup-fr-2255`) *(Corpo Calloso)*
- (`episode-backend-optimization-session`) --[RECORDS_INTENT]--> (`user-intent-backend-optimization-hybrid`) *(Corpo Calloso)*
- (`episode-bonifica-storage-ollama-mac`) --[RECORDS_INTENT]--> (`user-intent-rimozione-modello-ollama-mac`) *(Corpo Calloso)*
- (`episode-c-un-problema-vorrei-sapere-di-pi-3203`) --[RECORDS_INTENT]--> (`user-intent-c-un-problema-vorrei-sapere-di-pi-3203`) *(Corpo Calloso)*
- (`episode-che-ne-pensi-del-mio-cervello-artif-8743`) --[RECORDS_INTENT]--> (`user-intent-che-ne-pensi-del-mio-cervello-artif-8743`) *(Corpo Calloso)*
- (`episode-che-ne-pensi-del-mio-cervello-artif-8793`) --[RECORDS_INTENT]--> (`user-intent-che-ne-pensi-del-mio-cervello-artif-8793`) *(Corpo Calloso)*
- (`episode-che-ore-sono-3134`) --[RECORDS_INTENT]--> (`user-intent-che-ore-sono-3134`) *(Corpo Calloso)*
- (`episode-chi-pierfrancesco-amendola-e-cosa-8426`) --[RECORDS_INTENT]--> (`user-intent-chi-pierfrancesco-amendola-e-cosa-8426`) *(Corpo Calloso)*
- (`episode-chiarimento-concetti-tesi-deep-learning`) --[RECORDS_INTENT]--> (`user-intent-spiegazione-swin-transformer-deep-stable-learning`) *(Corpo Calloso)*
- (`episode-chiarimento-intuitivo-pilastri-teorici`) --[RECORDS_INTENT]--> (`user-intent-spiegazione-intuitiva-concetti-causali-attention`) *(Corpo Calloso)*
- (`episode-chiarimento-librerie-grafi-frontend`) --[RECORDS_INTENT]--> (`user-intent-chiarimento-stack-rendering-grafi-frontend`) *(Corpo Calloso)*
- (`episode-cloud-git-auto-push`) --[RECORDS_INTENT]--> (`user-intent-cloud-git-auto-push`) *(Corpo Calloso)*
- (`episode-comando-prompt-copia-rapi-8585`) --[RECORDS_INTENT]--> (`user-intent-comando-prompt-copia-rapi-8585`) *(Corpo Calloso)*
- (`episode-completamento-supercervello-ecosistema`) --[RECORDS_INTENT]--> (`user-intent-implementazione-ecosistema-supercervello`) *(Corpo Calloso)*
- (`episode-disamina-integrazioni-notion-obsidian`) --[RECORDS_INTENT]--> (`user-intent-confronto-integrazioni-llm-notion-obsidian`) *(Corpo Calloso)*
- (`episode-disamina-trasduttori-lineari`) --[RECORDS_INTENT]--> (`user-intent-definizione-ecografo-trasduttore-lineare`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2447`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-2447`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2471`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-2471`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2485`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-2485`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2529`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-2529`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2691`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-2691`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-8745`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-8745`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-9065`) --[RECORDS_INTENT]--> (`user-intent-e2e-test-session-hook-9065`) *(Corpo Calloso)*
- (`episode-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[RECORDS_INTENT]--> (`user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) *(Corpo Calloso)*
- (`episode-embedding-projector-globe-and-optics`) --[RECORDS_INTENT]--> (`user-intent-embedding-projector-globe-and-optics`) *(Corpo Calloso)*
- (`episode-espansione-ecosistema-supercervello`) --[RECORDS_INTENT]--> (`user-intent-espansione-supercervello-integrazioni`) *(Corpo Calloso)*
- (`episode-esplorazione-linux-3d-modeling`) --[RECORDS_INTENT]--> (`user-intent-distro-linux-modellazione-3d`) *(Corpo Calloso)*
- (`episode-fix-daemon-render-persistence`) --[RECORDS_INTENT]--> (`user-intent-fix-daemon-render-persistence`) *(Corpo Calloso)*
- (`episode-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[RECORDS_INTENT]--> (`user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753`) *(Corpo Calloso)*
- (`episode-jarvis-ricordi-quali-sono-gli-emis-3117`) --[RECORDS_INTENT]--> (`user-intent-jarvis-ricordi-quali-sono-gli-emis-3117`) *(Corpo Calloso)*
- (`episode-ma-tutto-falso-8462`) --[RECORDS_INTENT]--> (`user-intent-ma-tutto-falso-8462`) *(Corpo Calloso)*
- (`episode-non-riesci-a-connetterti-al-mio-cer-8486`) --[RECORDS_INTENT]--> (`user-intent-non-riesci-a-connetterti-al-mio-cer-8486`) *(Corpo Calloso)*
- (`episode-nuove-rappresentazioni-vi-2874`) --[RECORDS_INTENT]--> (`user-intent-nuove-rappresentazioni-vi-2874`) *(Corpo Calloso)*
- (`episode-occultamento-pulsanti-mob-9019`) --[RECORDS_INTENT]--> (`user-intent-occultamento-pulsanti-mob-9019`) *(Corpo Calloso)*
- (`episode-ottimizzazione-mobile-web-8880`) --[RECORDS_INTENT]--> (`user-intent-ottimizzazione-mobile-web-8880`) *(Corpo Calloso)*
- (`episode-perfezionamento-cappello-tabelle-cap-6`) --[RECORDS_INTENT]--> (`user-intent-integrazione-tabelle-cappello-capitolo-6`) *(Corpo Calloso)*
- (`episode-potenziamento-cognitivo-obsidian-bridge`) --[RECORDS_INTENT]--> (`user-intent-potenziamento-cognitivo-obsidian-bridge`) *(Corpo Calloso)*
- (`episode-potenziamento-skill-e-ril-8338`) --[RECORDS_INTENT]--> (`user-intent-potenziamento-skill-e-ril-8338`) *(Corpo Calloso)*
- (`episode-quali-sono-i-progetti-principali-di-8169`) --[RECORDS_INTENT]--> (`user-intent-quali-sono-i-progetti-principali-di-8169`) *(Corpo Calloso)*
- (`episode-quali-sono-le-abitudini-monitorate-2979`) --[RECORDS_INTENT]--> (`user-intent-quali-sono-le-abitudini-monitorate-2979`) *(Corpo Calloso)*
- (`episode-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[RECORDS_INTENT]--> (`user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794`) *(Corpo Calloso)*
- (`episode-revisione-sintesi-cappello-cap-6`) --[RECORDS_INTENT]--> (`user-intent-accorciamento-cappello-capitolo-6`) *(Corpo Calloso)*
- (`episode-revisione-supercervello-cognitive-os`) --[RECORDS_INTENT]--> (`user-intent-review-piano-supercervello-os`) *(Corpo Calloso)*
- (`episode-telegram-keepalive-confirmation`) --[RECORDS_INTENT]--> (`user-intent-telegram-keepalive-confirmation`) *(Corpo Calloso)*
- (`episode-test-hook-session-end-2411`) --[RECORDS_INTENT]--> (`user-intent-test-hook-session-end-2411`) *(Corpo Calloso)*
- (`episode-ui-declutter-projector-fullscreen`) --[RECORDS_INTENT]--> (`user-intent-ui-declutter-projector-fullscreen`) *(Corpo Calloso)*
- (`episode-update-readme-architecture`) --[RECORDS_INTENT]--> (`user-intent-update-readme-architecture`) *(Corpo Calloso)*
- (`episode-valutazione-language-app-antigravity`) --[RECORDS_INTENT]--> (`user-intent-valutazione-progetto-language-app`) *(Corpo Calloso)*
- (`episode-verifica-costi-zero-euro`) --[RECORDS_INTENT]--> (`user-intent-verifica-vincolo-zero-costi`) *(Corpo Calloso)*
- (`episode-verify-github-token-render`) --[RECORDS_INTENT]--> (`user-intent-verify-github-token-render`) *(Corpo Calloso)*
- (`episode-video-showcase-anteprima-universal-brain`) --[RECORDS_INTENT]--> (`user-intent-creazione-video-showcase-universal-brain`) *(Corpo Calloso)*
- (`episode-yt-shorts-business-model`) --[RECORDS_INTENT]--> (`user-intent-ai-shorts-evaluation`) *(Corpo Calloso)*
- (`episode-20260829-architettura-connettoma-e-sync-prompt`) --[RECORDS_REASONING]--> (`reasoning-architettura-connettoma-web-vs-desktop`) *(Corpo Calloso)*
- (`episode-20260829-avvio-intervista-universal-ai-hub`) --[RECORDS_REASONING]--> (`reasoning-architettura-universal-ai-hub`) *(Corpo Calloso)*
- (`episode-20260829-chiusura-jarvis-nuovo-progetto`) --[RECORDS_REASONING]--> (`reasoning-eliminazione-jarvis-pulizia`) *(Corpo Calloso)*
- (`episode-20260829-completamento-rilascio-jarvis-desktop`) --[RECORDS_REASONING]--> (`reasoning-rilascio-jarvis-desktop-completato`) *(Corpo Calloso)*
- (`episode-20260829-debrief-assessment-gemini`) --[RECORDS_REASONING]--> (`reasoning-diagnosi-retrieval-gemini-e-roadmap-potenziamento`) *(Corpo Calloso)*
- (`episode-20260829-definizione-piano-jarvis-desktop`) --[RECORDS_REASONING]--> (`reasoning-piano-implementazione-jarvis-desktop`) *(Corpo Calloso)*
- (`episode-20260829-esplorazione-paradigmi-interfaccia-grafo`) --[RECORDS_REASONING]--> (`reasoning-progettazione-5-paradigmi-visuali-connettoma`) *(Corpo Calloso)*
- (`episode-20260829-integrazione-openjarvis-desktop`) --[RECORDS_REASONING]--> (`reasoning-openjarvis-collegamento-connettoma`) *(Corpo Calloso)*
- (`episode-20260829-progettazione-jarvis-voice-ai`) --[RECORDS_REASONING]--> (`reasoning-architettura-jarvis-zero-cost`) *(Corpo Calloso)*
- (`episode-20260829-sigillatura-12-macro-domini`) --[RECORDS_REASONING]--> (`reasoning-ristrutturazione-sigillo-12-domini-completata`) *(Corpo Calloso)*
- (`episode-20260829-test-openjarvis-ollama-successo`) --[RECORDS_REASONING]--> (`reasoning-verifica-openjarvis-ollama-gpt-cloud`) *(Corpo Calloso)*
- (`episode-allineamento-nodi-render-cloud`) --[RECORDS_REASONING]--> (`reasoning-diagnosi-discrepanza-deploy-render`) *(Corpo Calloso)*
- (`episode-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[RECORDS_REASONING]--> (`reasoning-allora-vorrei-dirti-che-oggi-ho-man-4690`) *(Corpo Calloso)*
- (`episode-alternative-monetization-brainstorming`) --[RECORDS_REASONING]--> (`ai-reasoning-alternative-monetization-strategies`) *(Corpo Calloso)*
- (`episode-audit-critico-e-mockup-fr-2255`) --[RECORDS_REASONING]--> (`reasoning-audit-critico-e-mockup-fr-2255`) *(Corpo Calloso)*
- (`episode-backend-optimization-session`) --[RECORDS_REASONING]--> (`reasoning-backend-audit-and-fix`) *(Corpo Calloso)*
- (`episode-bonifica-storage-ollama-mac`) --[RECORDS_REASONING]--> (`reasoning-risoluzione-residui-ollama-mac`) *(Corpo Calloso)*
- (`episode-c-un-problema-vorrei-sapere-di-pi-3203`) --[RECORDS_REASONING]--> (`reasoning-c-un-problema-vorrei-sapere-di-pi-3203`) *(Corpo Calloso)*
- (`episode-che-ne-pensi-del-mio-cervello-artif-8743`) --[RECORDS_REASONING]--> (`reasoning-che-ne-pensi-del-mio-cervello-artif-8743`) *(Corpo Calloso)*
- (`episode-che-ne-pensi-del-mio-cervello-artif-8793`) --[RECORDS_REASONING]--> (`reasoning-che-ne-pensi-del-mio-cervello-artif-8793`) *(Corpo Calloso)*
- (`episode-che-ore-sono-3134`) --[RECORDS_REASONING]--> (`reasoning-che-ore-sono-3134`) *(Corpo Calloso)*
- (`episode-chi-pierfrancesco-amendola-e-cosa-8426`) --[RECORDS_REASONING]--> (`reasoning-chi-pierfrancesco-amendola-e-cosa-8426`) *(Corpo Calloso)*
- (`episode-chiarimento-concetti-tesi-deep-learning`) --[RECORDS_REASONING]--> (`reasoning-sintesi-teorica-swin-e-deep-stable-learning`) *(Corpo Calloso)*
- (`episode-chiarimento-intuitivo-pilastri-teorici`) --[RECORDS_REASONING]--> (`reasoning-semplificazione-concettuale-causal-dl`) *(Corpo Calloso)*
- (`episode-chiarimento-librerie-grafi-frontend`) --[RECORDS_REASONING]--> (`reasoning-analisi-stack-grafico-universal-brain`) *(Corpo Calloso)*
- (`episode-cloud-git-auto-push`) --[RECORDS_REASONING]--> (`reasoning-cloud-git-auto-push`) *(Corpo Calloso)*
- (`episode-comando-prompt-copia-rapi-8585`) --[RECORDS_REASONING]--> (`reasoning-comando-prompt-copia-rapi-8585`) *(Corpo Calloso)*
- (`episode-completamento-supercervello-ecosistema`) --[RECORDS_REASONING]--> (`reasoning-costruzione-collaudo-ecosistema-supercervello`) *(Corpo Calloso)*
- (`episode-disamina-integrazioni-notion-obsidian`) --[RECORDS_REASONING]--> (`reasoning-tassonomia-pkm-rag-notion-obsidian`) *(Corpo Calloso)*
- (`episode-disamina-trasduttori-lineari`) --[RECORDS_REASONING]--> (`reasoning-caratterizzazione-trasduttore-lineare`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2447`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-2447`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2471`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-2471`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2485`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-2485`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2529`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-2529`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-2691`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-2691`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-8745`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-8745`) *(Corpo Calloso)*
- (`episode-e2e-test-session-hook-9065`) --[RECORDS_REASONING]--> (`reasoning-e2e-test-session-hook-9065`) *(Corpo Calloso)*
- (`episode-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[RECORDS_REASONING]--> (`reasoning-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) *(Corpo Calloso)*
- (`episode-embedding-projector-globe-and-optics`) --[RECORDS_REASONING]--> (`reasoning-embedding-projector-globe-and-optics`) *(Corpo Calloso)*
- (`episode-espansione-ecosistema-supercervello`) --[RECORDS_REASONING]--> (`reasoning-architettura-ecosistema-cognitivo-onnipresente`) *(Corpo Calloso)*
- (`episode-esplorazione-linux-3d-modeling`) --[RECORDS_REASONING]--> (`reasoning-mappatura-ecosistema-linux-3d`) *(Corpo Calloso)*
- (`episode-fix-daemon-render-persistence`) --[RECORDS_REASONING]--> (`reasoning-fix-daemon-render-persistence`) *(Corpo Calloso)*
- (`episode-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[RECORDS_REASONING]--> (`reasoning-ho-bisogno-di-sapere-tutto-ci-che-2753`) *(Corpo Calloso)*
- (`episode-jarvis-ricordi-quali-sono-gli-emis-3117`) --[RECORDS_REASONING]--> (`reasoning-jarvis-ricordi-quali-sono-gli-emis-3117`) *(Corpo Calloso)*
- (`episode-ma-tutto-falso-8462`) --[RECORDS_REASONING]--> (`reasoning-ma-tutto-falso-8462`) *(Corpo Calloso)*
- (`episode-non-riesci-a-connetterti-al-mio-cer-8486`) --[RECORDS_REASONING]--> (`reasoning-non-riesci-a-connetterti-al-mio-cer-8486`) *(Corpo Calloso)*
- (`episode-nuove-rappresentazioni-vi-2874`) --[RECORDS_REASONING]--> (`reasoning-nuove-rappresentazioni-vi-2874`) *(Corpo Calloso)*
- (`episode-occultamento-pulsanti-mob-9019`) --[RECORDS_REASONING]--> (`reasoning-occultamento-pulsanti-mob-9019`) *(Corpo Calloso)*
- (`episode-ottimizzazione-mobile-web-8880`) --[RECORDS_REASONING]--> (`reasoning-ottimizzazione-mobile-web-8880`) *(Corpo Calloso)*
- (`episode-perfezionamento-cappello-tabelle-cap-6`) --[RECORDS_REASONING]--> (`reasoning-integrazione-esplicita-tabelle-comparative`) *(Corpo Calloso)*
- (`episode-potenziamento-cognitivo-obsidian-bridge`) --[RECORDS_REASONING]--> (`reasoning-potenziamento-cognitivo-obsidian-bridge`) *(Corpo Calloso)*
- (`episode-potenziamento-skill-e-ril-8338`) --[RECORDS_REASONING]--> (`reasoning-potenziamento-skill-e-ril-8338`) *(Corpo Calloso)*
- (`episode-quali-sono-i-progetti-principali-di-8169`) --[RECORDS_REASONING]--> (`reasoning-quali-sono-i-progetti-principali-di-8169`) *(Corpo Calloso)*
- (`episode-quali-sono-le-abitudini-monitorate-2979`) --[RECORDS_REASONING]--> (`reasoning-quali-sono-le-abitudini-monitorate-2979`) *(Corpo Calloso)*
- (`episode-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[RECORDS_REASONING]--> (`reasoning-quanti-nodi-ci-sono-nel-mio-cervell-4794`) *(Corpo Calloso)*
- (`episode-revisione-sintesi-cappello-cap-6`) --[RECORDS_REASONING]--> (`reasoning-ottimizzazione-sintetica-testo`) *(Corpo Calloso)*
- (`episode-revisione-supercervello-cognitive-os`) --[RECORDS_REASONING]--> (`reasoning-valutazione-architetturale-supercervello`) *(Corpo Calloso)*
- (`episode-telegram-keepalive-confirmation`) --[RECORDS_REASONING]--> (`reasoning-telegram-keepalive-confirmation`) *(Corpo Calloso)*
- (`episode-test-hook-session-end-2411`) --[RECORDS_REASONING]--> (`reasoning-test-hook-session-end-2411`) *(Corpo Calloso)*
- (`episode-ui-declutter-projector-fullscreen`) --[RECORDS_REASONING]--> (`reasoning-ui-declutter-projector-fullscreen`) *(Corpo Calloso)*
- (`episode-update-readme-architecture`) --[RECORDS_REASONING]--> (`reasoning-update-readme-architecture`) *(Corpo Calloso)*
- (`episode-valutazione-language-app-antigravity`) --[RECORDS_REASONING]--> (`reasoning-analisi-fattibilita-language-app`) *(Corpo Calloso)*
- (`episode-verifica-costi-zero-euro`) --[RECORDS_REASONING]--> (`reasoning-validazione-architettura-zero-costi`) *(Corpo Calloso)*
- (`episode-verify-github-token-render`) --[RECORDS_REASONING]--> (`reasoning-verify-github-token-render`) *(Corpo Calloso)*
- (`episode-video-showcase-anteprima-universal-brain`) --[RECORDS_REASONING]--> (`reasoning-creazione-video-showcase-universal-brain`) *(Corpo Calloso)*
- (`episode-yt-shorts-business-model`) --[RECORDS_REASONING]--> (`ai-reasoning-market-analysis-automation`) *(Corpo Calloso)*
- (`aule-studio-app`) --[RENDERED_VIA]--> (`aule-studio-mobile-ui`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[RENDERS_FX]--> (`streaksup-particle-fx`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[REQUESTED]--> (`user-intent-frontend-professional-restyle`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[REQUESTED]--> (`user-intent-clean-clustered-ui`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[REQUESTED]--> (`user-intent-connect-gemini-claude-chatgpt-mcp`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[REQUESTED]--> (`user-intent-reasoning-and-chat-memory`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[RESEARCHES_AT]--> (`proj-bioinformatics-icar`) *(Corpo Calloso)*
- (`goal-multi-ai-shared-context-persistence`) --[SERVES_USER]--> (`person-pierfrancesco`) *(Corpo Calloso)*
- (`streaksup-streak-freeze-algo`) --[SHIELD_THEMED_BY]--> (`streaksup-flame-palette`) *(Corpo Calloso)*
- (`design-language-app-system`) --[SOLVES]--> (`intent-language-app-ui-design`) *(Corpo Calloso)*
- (`fastapi-python-stack`) --[STREAMS_JSON_TO]--> (`3d-force-galaxy-view`) *(Corpo Calloso)*
- (`person-pierfrancesco`) --[STUDIES_AT]--> (`coursework-cs-federico2`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[STYLED_BY]--> (`streaksup-glassmorphism-system`) *(Corpo Calloso)*
- (`universal-ai-brain`) --[STYLED_BY]--> (`bi-hemispheric-polarity-palette`) *(Corpo Calloso)*
- (`rigore-informativo`) --[SYNONYM_OF]--> (`brand-voice-surgical`) *(Corpo Calloso)*
- (`streaksup-gamification-engine`) --[TRIGGERS_CELEBRATION]--> (`streaksup-particle-fx`) *(Corpo Calloso)*
- (`streaksup-app-intents-engine`) --[TRIGGERS_RELOAD_ON]--> (`streaksup-widget-suite-ui`) *(Corpo Calloso)*
- (`proj-streaksup-app`) --[USES_PALETTE]--> (`streaksup-flame-palette`) *(Corpo Calloso)*
- (`antigravity-centaur-collaboration`) --[VALIDATES_EMPIRICALLY]--> (`mental-centaur-model`) *(Corpo Calloso)*
- (`universal-ai-brain`) --[VISUALIZED_IN]--> (`3d-force-galaxy-view`) *(Corpo Calloso)*
- (`node-web-tree-explorer`) --[VISUALIZES_AND_FOCUSES]--> (`node-hierarchical-tree-engine-impl`) *(Corpo Calloso)*
- (`sqlite-wal-persistence`) --[ZERO_OVERHEAD_THEME]--> (`cyber-slate-space-aesthetic`) *(Corpo Calloso)*

### Connessioni Intra-Emisfero:
- (`node-hierarchical-dendrogram`) --[ACTS_AS_INDEXING_OVERLAY_UPON]--> (`node-knowledge-graph-memory`)
- (`proj-streaksup-app`) --[ALIGNED_WITH]--> (`rule-zero-cost`)
- (`episode-frontend-deeptech-redesign-and-physics-zero-lag`) --[APPLIED_DESIGN_SYSTEM]--> (`design-token-cyberpunk-minimalist-palette`)
- (`design-duolingo-chess-pieces`) --[APPLIES_TO]--> (`person-pierfrancesco`)
- (`ai-reasoning-hybrid-cloud-local-symbiosis`) --[ARCHITECTURAL_DECISION_FOR]--> (`domain-software-engineering`)
- (`ai-reasoning-hybrid-cloud-local-symbiosis`) --[ARCHITECTURAL_PILLAR_OF]--> (`universal-ai-brain`)
- (`person-pierfrancesco`) --[ARCHITECT_AND_CREATOR]--> (`domain-design-creativita`)
- (`person-pierfrancesco`) --[ARCHITECT_AND_CREATOR]--> (`domain-filosofia-valori`)
- (`identity-cs-researcher`) --[AUTHORED]--> (`proj-kdp-ai-book`)
- (`aule-studio-app`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-episodic-memory-architecture`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-clustering-decision`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`graphify-knowledge-engine`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-cinematch`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`sqlite-wal-persistence`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`feat-light-terminal`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-unicampus`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`caveman-communication-protocol`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-kdp-ai-guide`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-holly-benji-ai`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`identity-cs-researcher`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rule-cloud-persistence`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`session-continuous-evolution`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`zero-debt-cost-rule`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`feat-copy-ai-prompt`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rule-ai-thought-tracing`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`epistemologia-rigorosa`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rule-episodic-chat-preservation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`idea-hierarchical-weighted-trees`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`repo-github-universal-ai-brain`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-epistemic-grading-system`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-multiscale-overlay-pattern`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-mcp-brain-get-tree`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-commit-965f0a8`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-multi-llm-mcp-skill-distribution`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`skill-universal-brain-installed`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-modular-cluster-decentralization`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-domain-subgraph-modularity`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-hierarchical-multi-layer-graph-design`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-hypergraph-multi-scale-feasibility`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-cross-model-provenance-validation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`ai-reasoning-hybrid-search-mcp`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`analysis-bst-vs-graph-taxonomy`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`arch-telegram-webhook-gateway`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`concept-graph-of-graphs-hypergraph`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`concept-modular-domain-subgraphs`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`deploy-render-zero-cost`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`feat-progressive-areas`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-graph-taxonomy-classification`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-graph-tree-unification`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-hierarchical-overlay-reassurance`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-hierarchical-tree-deployment-sync`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-telegram-bot-interface`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-telegram-cognitive-hub-spec`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-tree-ranking-translation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`intent-ep-20260827-tree-structures-evaluation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-hierarchical-dendrogram`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-hierarchical-tree-engine-impl`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-neuro-symbolic-brain`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-search-tree-deliberation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-telegram-webhook-gateway`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-tree-architecture-verdict`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-ubiquitous-ingestion`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-universal-ai-brain-taxonomy`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-linkly-qr`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`proj-tombolawifi`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-graph-taxonomy-classification`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-graph-tree-unification`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-hierarchical-overlay-reassurance`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-hierarchical-tree-deployment-sync`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-telegram-bot-interface`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-telegram-cognitive-hub-spec`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-tree-ranking-translation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`reason-ep-20260827-tree-structures-evaluation`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rigore-informativo`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rule-zero-placeholder`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`tax-ai-reasoning`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-clean-clustered-ui`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-connect-gemini-claude-chatgpt-mcp`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-provenance-model-tracking`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-reasoning-and-chat-memory`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-telegram-bot-gateway`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-tree-search-enhancement`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`user-intent-zero-cost-graphrag`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`mental-centaur-model`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`node-knowledge-graph-memory`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`rule-zero-cost`)
- (`domain-ai-cognitive-systems`) --[BELONGS_TO_DOMAIN]--> (`universal-ai-brain`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`terse-caveman-brand-voice`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`bi-hemispheric-polarity-palette`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`palette-neon-cyber`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`cyber-slate-space-aesthetic`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`design-cyber-neon`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`design-tokens-core`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`art-piano-composition`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`brand-voice-engineering`)
- (`domain-design-creativita`) --[BELONGS_TO_DOMAIN]--> (`brand-voice-surgical`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`session-evolution-ui-persistence`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`rel-antonio-chieppa`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`rel-academic-mentors`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`tg-idea-per-nuova-app-ai`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-graph-tree-unification`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-graph-taxonomy-classification`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-telegram-bot-interface`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-tree-structures-evaluation`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-tree-ranking-translation`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-hierarchical-overlay-reassurance`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-hierarchical-tree-deployment-sync`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`node-commit-62e48df`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`ep-20260827-telegram-cognitive-hub-spec`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`antigravity-centaur-collaboration`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`art-creative-writing`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`art-theatre-acting`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`creative-multidisciplinary`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`lesson-boundaries-clarity`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`lesson-stoic-resilience`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`memory-perfectionism-tension`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`rel-marco-di-martino`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`rel-napoli-culture`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`rel-parents`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`val-authenticity`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`val-impact-utility`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`val-independence`)
- (`domain-filosofia-valori`) --[BELONGS_TO_DOMAIN]--> (`val-transparency-loyalty`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-bioinformatics-icar`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-specula`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-alcolsafe`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-kdp-ai-book`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`coursework-cs-federico2`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-napolilive`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`fastapi-python-stack`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`flutter-dart-ecosystem`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`aule-studio-app`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-caretrack`)
- (`domain-software-engineering`) --[BELONGS_TO_DOMAIN]--> (`proj-streaksup-app`)
- (`kindle-3c40d6e17fd5`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-3e8f7aed7312`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-6d280a533c87`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-7439c883249f`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-bb8b1e467610`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-c7eedf9ce6bb`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`kindle-c962fde43767`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`kindle-cba1775488ae`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`node-test-raycast-node`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-1-minimal`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-10-funptr`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-12-templates`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-2`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-2-structured`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-3-basictypes`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-4-allocation`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-5-usertypes`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-6-iostream`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-7-string`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-8-psecasgen`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-accentcolor-colorset`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-advanceddb-mod-db-tech`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-algebra`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-appabbonamenti`) --[BELONGS_TO_DOMAIN]--> (`domain-finanza-economia`)
- (`proj-appaulestudiotypescript`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-appcalcolatori`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-appflashcards`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`proj-appicon-appiconset`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-appnapoli`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-apppalette`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`proj-appscadenza`) --[BELONGS_TO_DOMAIN]--> (`domain-crescita-personale`)
- (`proj-apptombola`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-asd-lasd`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-auth_screens`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-backend`) --[BELONGS_TO_DOMAIN]--> (`domain-relazioni-comunicazione`)
- (`proj-basi-di-dati-esercizi`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-bdd`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-binari`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-book`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-calm-raman`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-caretrack`) --[BELONGS_TO_DOMAIN]--> (`domain-medicina-salute`)
- (`proj-cervelloartificiale`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`proj-ciscocertification`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-codice_architettura_tesi`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-compito-luglio`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-compito-settembre`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-composetest`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-cose_laurea`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-cypress_tests`) --[BELONGS_TO_DOMAIN]--> (`domain-relazioni-comunicazione`)
- (`proj-eager-pasteur`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-economia`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-eserciziocontocorrente`) --[BELONGS_TO_DOMAIN]--> (`domain-finanza-economia`)
- (`proj-example`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-examples`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-fantaformula1`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-foodlab2025`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-frontend`) --[BELONGS_TO_DOMAIN]--> (`domain-relazioni-comunicazione`)
- (`proj-gennaio-2021`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-gioco`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-giocoscacchi`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`proj-giugno-2021`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-gods-eye-view-main`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-googlecertificate`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-habittracker`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-happy-plant-keeper`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-ingsw`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-jarvis-voice-assistant`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`proj-jules_session_5370203018288358434`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-lp---prova-esame-giugno`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-lp1`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-lso`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-macpulse2tests`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-macpulse2uitests`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-macpulsetests`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-macpulseuitests`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-mary`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`proj-marzo-2021`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-ml-neural-networks-dl`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-new-project`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-new_chapters`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-nvidiacertification`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-oo`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-osmci`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-outputs`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-pack3`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-pack4`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-palazzo`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-palazzografica`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`proj-particle-engine-simulation`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`proj-pdc`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-pgf-pie`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-pierfrancescoamendola`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-posgresql-pgadmin`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-progetto-gestione-bibloteca`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-propedia-demo`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-psld1`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-psld2-senza-git`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-qr_generator`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render1`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render2`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render3`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_final`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_pdf_temp`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_proof_1`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_proof_final`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_revision`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-render_revision_final`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-rendered`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-rendered_v2`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-reti-di-calcolatori`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-sample`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-sim`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-sitocertificati`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-slidetecweb`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-soluzionepostgress_pgadmin_prof`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-source_chapters`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-spiegazione-codice-librerire`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-statistica`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-streaksup-app`) --[BELONGS_TO_DOMAIN]--> (`domain-produttivita-sistemi`)
- (`proj-svolti`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-taste-skill`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-tecweblezioni`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-testrepo-main`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-tscheck`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`proj-uni-grade-projections-main`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-unimatch`) --[BELONGS_TO_DOMAIN]--> (`domain-relazioni-comunicazione`)
- (`proj-unimatch-1`) --[BELONGS_TO_DOMAIN]--> (`domain-relazioni-comunicazione`)
- (`proj-unistats`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-videoyt`) --[BELONGS_TO_DOMAIN]--> (`domain-scienza-matematica`)
- (`proj-workspace`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`project-royal-gambit-chess`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`universal-ai-brain`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2447`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2471`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2485`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2529`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2690`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-8745`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-9065`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-test-shortcuts-debug-7964`) --[BELONGS_TO_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`voice-voglio-portare-a-spasso-il-cane-perch-mi-provoca-t-1518`) --[BELONGS_TO_DOMAIN]--> (`domain-design-creativita`)
- (`web-test-fastapi-docs`) --[BELONGS_TO_DOMAIN]--> (`domain-software-engineering`)
- (`val-eternal-cognitive-continuity`) --[BELONGS_TO_EPISODE]--> (`episode-infinite-context-philosophy`)
- (`user-intent-mappamondo-3d-spotlight-relazioni`) --[BELONGS_TO_PROJECT]--> (`universal-ai-brain`)
- (`person-pierfrancesco`) --[BONDS_WITH]--> (`rel-marco-di-martino`)
- (`aule-studio-app`) --[BUILT_WITH]--> (`flutter-dart-ecosystem`)
- (`person-pierfrancesco`) --[CAPTURED_VIA_TELEGRAM]--> (`tg-idea-per-nuova-app-ai`)
- (`person-pierfrancesco`) --[CHAMPIONS_VISION]--> (`continuous-ai-symbiosis`)
- (`art-piano-composition`) --[CHANNELS_AND_HEALS]--> (`memory-perfectionism-tension`)
- (`person-pierfrancesco`) --[CHERISHES]--> (`rel-parents`)
- (`concept-llm-indirect-injection-safeguard`) --[COGNITIVE_RULE_OF]--> (`domain-ai-cognitive-systems`)
- (`person-pierfrancesco`) --[COLLABORATES_WITH]--> (`rel-antonio-chieppa`)
- (`goal-multi-ai-shared-context-persistence`) --[COMPLEMENTS]--> (`user-intent-provenance-model-tracking`)
- (`reasoning-openjarvis-collegamento-connettoma`) --[CONNECTS]--> (`proj-jarvis-voice-assistant`)
- (`node-search-tree-deliberation`) --[CONSOLIDATES_DISCOVERED_PATHS_INTO]--> (`node-knowledge-graph-memory`)
- (`design-duolingo-chess-system`) --[CONTAINS]--> (`design-duolingo-chess-pieces`)
- (`domain-ai-cognitive-systems`) --[CONTAINS_CONCEPT]--> (`concept-interhemispheric-inhibition-gating`)
- (`aule-studio-app`) --[CONTAINS_MODULE]--> (`aule-studio-backend-arch`)
- (`domain-medicina-salute`) --[CONTAINS_MODULE]--> (`medical-onicocriptosi-unghia-incarnita`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`proj-harmonyapp`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`proj-particlesimulator`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`proj-regexriddle`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`proj-tesi-busbra-cnr`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`proj-tombola-wifi`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`ai-memory-ingest-spec`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`feat-ai-json-importer`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`arch-sqlite-wal`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`node-mst-conceptual-backbone`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`node-prefix-radix-trie`)
- (`domain-software-engineering`) --[CONTAINS_MODULE]--> (`node-bidirectional-bfs-pathfinding`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-gamification-engine`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-streak-freeze-algo`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-app-intents-engine`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-darwin-ipc-protocol`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-i18n-runtime-engine`)
- (`proj-streaksup-app`) --[CONTAINS_MODULE]--> (`streaksup-swiftdata-arch`)
- (`domain-medicina-salute`) --[CONTAINS_PATHOLOGY]--> (`medical-onicocriptosi-unghia-incarnita`)
- (`ep-20260827-render-cloud-vs-local-hybrid-architecture`) --[CONVERSATION_WITH]--> (`person-pierfrancesco`)
- (`ai-reasoning-hybrid-search-mcp`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`)
- (`ai-reasoning-hybrid-search-mcp`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`analysis-bst-vs-graph-taxonomy`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`)
- (`analysis-bst-vs-graph-taxonomy`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`antigravity-centaur-collaboration`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-surgical`)
- (`arch-telegram-webhook-gateway`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`architecture-vis-network-silent-stabilization-zero-lag`) --[CORPUS_CALLOSUM_LINK]--> (`concept-graph-of-graphs-hypergraph`)
- (`art-piano-composition`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`art-theatre-acting`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`coursework-cs-federico2`) --[CORPUS_CALLOSUM_LINK]--> (`identity-cs-researcher`)
- (`deploy-render-zero-cost`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`design-language-app-system`) --[CORPUS_CALLOSUM_LINK]--> (`episode-language-app-architecture`)
- (`episode-2026-08-27-graphrag-mcp-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`episode-2026-08-27-telegram-omnipresence`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`episode-2026-08-27-tree-structures-evaluation`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`episode-frontend-deeptech-redesign-and-physics-zero-lag`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`epistemologia-rigorosa`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-placeholder`)
- (`lesson-backend-ground-truth-and-clean-canvas-rendering`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`lesson-boundaries-clarity`) --[CORPUS_CALLOSUM_LINK]--> (`val-authenticity`)
- (`lesson-stoic-resilience`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`memory-perfectionism-tension`) --[CORPUS_CALLOSUM_LINK]--> (`art-piano-composition`)
- (`person-pierfrancesco`) --[CORPUS_CALLOSUM_LINK]--> (`art-piano-composition`)
- (`person-pierfrancesco`) --[CORPUS_CALLOSUM_LINK]--> (`rel-marco-di-martino`)
- (`person-pierfrancesco`) --[CORPUS_CALLOSUM_LINK]--> (`rel-parents`)
- (`person-pierfrancesco`) --[CORPUS_CALLOSUM_LINK]--> (`val-transparency-loyalty`)
- (`proj-bioinformatics-icar`) --[CORPUS_CALLOSUM_LINK]--> (`identity-cs-researcher`)
- (`proj-regexriddle`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`)
- (`proj-tesi-busbra-cnr`) --[CORPUS_CALLOSUM_LINK]--> (`identity-cs-researcher`)
- (`proj-unicampus`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`reasoning-brain-architecture-analysis`) --[CORPUS_CALLOSUM_LINK]--> (`intent-evaluate-ai-brain-architecture`)
- (`rel-academic-mentors`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`rel-antonio-chieppa`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`rel-marco-di-martino`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`rel-napoli-culture`) --[CORPUS_CALLOSUM_LINK]--> (`art-theatre-acting`)
- (`rel-parents`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`rel-parents`) --[CORPUS_CALLOSUM_LINK]--> (`val-transparency-loyalty`)
- (`repo-github-universal-ai-brain`) --[CORPUS_CALLOSUM_LINK]--> (`session-continuous-evolution`)
- (`repo-github-universal-ai-brain`) --[CORPUS_CALLOSUM_LINK]--> (`deploy-render-zero-cost`)
- (`session-continuous-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`mental-centaur-model`)
- (`session-continuous-evolution`) --[CORPUS_CALLOSUM_LINK]--> (`rule-zero-cost`)
- (`session-evolution-ui-persistence`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`ui-component-palazzo-cognitivo-multi-layer-navigator`) --[CORPUS_CALLOSUM_LINK]--> (`person-pierfrancesco`)
- (`val-authenticity`) --[CORPUS_CALLOSUM_LINK]--> (`brand-voice-surgical`)
- (`val-authenticity`) --[CORPUS_CALLOSUM_LINK]--> (`lesson-boundaries-clarity`)
- (`val-transparency-loyalty`) --[CORPUS_CALLOSUM_LINK]--> (`rel-marco-di-martino`)
- (`val-transparency-loyalty`) --[CORPUS_CALLOSUM_LINK]--> (`rel-parents`)
- (`proj-appalcool`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-appflashcards`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-apppalette`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-appscadenza`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-backend`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-caretrack-demo`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-cypress_tests`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-docs_md`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-federicoiiapp`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-frontend`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-mary`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-missing-feedback`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-palazzografica`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-scripts`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-tests`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-unimatch`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-unimatch-1`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-utils`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`proj-website`) --[CREATED_BY]--> (`person-pierfrancesco`)
- (`user-intent-telegram-bot-gateway`) --[DEFINES]--> (`arch-telegram-webhook-gateway`)
- (`ai-reasoning-infinite-context-architecture`) --[DEFINES_CORE_PURPOSE_OF]--> (`universal-ai-brain`)
- (`goal-multi-ai-shared-context-persistence`) --[DEFINES_MISSION_OF]--> (`universal-ai-brain`)
- (`session-continuous-evolution`) --[DEPLOYS_TO]--> (`deploy-render-zero-cost`)
- (`identity-cs-researcher`) --[DEVELOPED]--> (`proj-tombola-wifi`)
- (`user-intent-clean-clustered-ui`) --[DRIVES_IMPLEMENTATION]--> (`feat-progressive-areas`)
- (`node-hierarchical-dendrogram`) --[ELECTED_AS_OPTIMAL_SOLUTION]--> (`node-tree-architecture-verdict`)
- (`person-pierfrancesco`) --[EMBODIES]--> (`val-authenticity`)
- (`tax-ai-reasoning`) --[ENFORCED_BY]--> (`rule-ai-thought-tracing`)
- (`universal-ai-brain`) --[ENFORCES_STYLE]--> (`caveman-communication-protocol`)
- (`feat-progressive-areas`) --[ENHANCES]--> (`universal-ai-brain`)
- (`reason-ep-20260827-graph-taxonomy-classification`) --[ESTABLISHES_CONCEPT]--> (`node-epistemic-grading-system`)
- (`reason-ep-20260827-graph-taxonomy-classification`) --[ESTABLISHES_CONCEPT]--> (`node-universal-ai-brain-taxonomy`)
- (`reason-ep-20260827-graph-tree-unification`) --[ESTABLISHES_CONCEPT]--> (`node-knowledge-graph-memory`)
- (`reason-ep-20260827-graph-tree-unification`) --[ESTABLISHES_CONCEPT]--> (`node-neuro-symbolic-brain`)
- (`reason-ep-20260827-graph-tree-unification`) --[ESTABLISHES_CONCEPT]--> (`node-search-tree-deliberation`)
- (`reason-ep-20260827-hierarchical-overlay-reassurance`) --[ESTABLISHES_CONCEPT]--> (`node-multiscale-overlay-pattern`)
- (`reason-ep-20260827-hierarchical-tree-deployment-sync`) --[ESTABLISHES_CONCEPT]--> (`node-mcp-brain-get-tree`)
- (`reason-ep-20260827-hierarchical-tree-deployment-sync`) --[ESTABLISHES_CONCEPT]--> (`node-hierarchical-tree-engine-impl`)
- (`reason-ep-20260827-telegram-bot-interface`) --[ESTABLISHES_CONCEPT]--> (`node-ubiquitous-ingestion`)
- (`reason-ep-20260827-telegram-cognitive-hub-spec`) --[ESTABLISHES_CONCEPT]--> (`node-bidirectional-bfs-pathfinding`)
- (`reason-ep-20260827-telegram-cognitive-hub-spec`) --[ESTABLISHES_CONCEPT]--> (`node-commit-965f0a8`)
- (`reason-ep-20260827-telegram-cognitive-hub-spec`) --[ESTABLISHES_CONCEPT]--> (`node-telegram-webhook-gateway`)
- (`reason-ep-20260827-tree-ranking-translation`) --[ESTABLISHES_CONCEPT]--> (`node-tree-architecture-verdict`)
- (`reason-ep-20260827-tree-structures-evaluation`) --[ESTABLISHES_CONCEPT]--> (`node-mst-conceptual-backbone`)
- (`reason-ep-20260827-tree-structures-evaluation`) --[ESTABLISHES_CONCEPT]--> (`node-prefix-radix-trie`)
- (`reason-ep-20260827-tree-structures-evaluation`) --[ESTABLISHES_CONCEPT]--> (`node-hierarchical-dendrogram`)
- (`user-intent-tree-search-enhancement`) --[EVALUATED_BY]--> (`analysis-bst-vs-graph-taxonomy`)
- (`reasoning-brain-architecture-analysis`) --[EVALUATES]--> (`intent-evaluate-ai-brain-architecture`)
- (`node-telegram-webhook-gateway`) --[EXECUTES_VIA_COMMAND_PATH]--> (`node-bidirectional-bfs-pathfinding`)
- (`node-telegram-webhook-gateway`) --[EXECUTES_VIA_COMMAND_TREE]--> (`node-hierarchical-tree-engine-impl`)
- (`ai-reasoning-hybrid-cloud-local-symbiosis`) --[EXPANDS_DOMAIN]--> (`domain-ai-cognitive-systems`)
- (`proj-streaksup-app`) --[EXPOSES_INTERACTIVITY_VIA]--> (`streaksup-app-intents-engine`)
- (`universal-ai-brain`) --[EXPOSES_PROTOCOL]--> (`ai-memory-ingest-spec`)
- (`node-nota-rapida-raycast-test`) --[EXPRESSED_BY]--> (`person-pierfrancesco`)
- (`test-e2e-web-clipper`) --[EXPRESSED_BY]--> (`person-pierfrancesco`)
- (`voice-oggi-ho-riflettuto-sul-principio-stoico-della-dico-2214`) --[EXPRESSED_BY]--> (`person-pierfrancesco`)
- (`voice-riflessione-sullantifragilit-nei-sistemi-software-2447`) --[EXPRESSED_BY]--> (`person-pierfrancesco`)
- (`voice-voglio-portare-a-spasso-il-cane-perch-mi-provoca-t-1518`) --[EXPRESSED_BY]--> (`person-pierfrancesco`)
- (`person-pierfrancesco`) --[EXPRESSES_SYNTHESIS]--> (`creative-multidisciplinary`)
- (`user-intent-provenance-model-tracking`) --[EXTENDS]--> (`ai-memory-ingest-spec`)
- (`proj-jarvis-voice-assistant`) --[EXTENDS_BRAIN]--> (`universal-ai-brain`)
- (`concept-graph-of-graphs-hypergraph`) --[EXTENDS_MODULARITY]--> (`concept-modular-domain-subgraphs`)
- (`repo-github-universal-ai-brain`) --[FEEDS_DEPLOY]--> (`deploy-render-zero-cost`)
- (`node-ubiquitous-ingestion`) --[FEEDS_REALTIME_DATA_INTO]--> (`node-knowledge-graph-memory`)
- (`ai-reasoning-infinite-context-architecture`) --[FORMALIZES]--> (`user-intent-infinite-context-persistence`)
- (`node-neuro-symbolic-brain`) --[FORMALLY_CLASSIFIED_AS]--> (`node-universal-ai-brain-taxonomy`)
- (`ai-reasoning-episodic-memory-architecture`) --[FORMULATED_RULE]--> (`rule-episodic-chat-preservation`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-crescita-personale`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-cultura-storia`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-design-creativita`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-filosofia-valori`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-musica-audio`)
- (`person-pierfrancesco`) --[FOUNDATIONAL_PILLAR]--> (`domain-relazioni-comunicazione`)
- (`ai-reasoning-alternative-monetization-strategies`) --[FULFILLS]--> (`user-intent-alternative-income-generation`)
- (`ai-reasoning-market-analysis-automation`) --[FULFILLS]--> (`user-intent-ai-shorts-evaluation`)
- (`reasoning-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[FULFILLS]--> (`user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690`)
- (`reasoning-analisi-fattibilita-language-app`) --[FULFILLS]--> (`user-intent-valutazione-progetto-language-app`)
- (`reasoning-analisi-stack-grafico-universal-brain`) --[FULFILLS]--> (`user-intent-chiarimento-stack-rendering-grafi-frontend`)
- (`reasoning-architettura-connettoma-web-vs-desktop`) --[FULFILLS]--> (`user-intent-architettura-connettoma-web-vs-desktop`)
- (`reasoning-architettura-ecosistema-cognitivo-onnipresente`) --[FULFILLS]--> (`user-intent-espansione-supercervello-integrazioni`)
- (`reasoning-architettura-jarvis-zero-cost`) --[FULFILLS]--> (`user-intent-creazione-jarvis-voice-assistant`)
- (`reasoning-architettura-universal-ai-hub`) --[FULFILLS]--> (`user-intent-universal-ai-hub-client`)
- (`reasoning-audit-critico-e-mockup-fr-2255`) --[FULFILLS]--> (`user-intent-audit-critico-e-mockup-fr-2255`)
- (`reasoning-backend-audit-and-fix`) --[FULFILLS]--> (`user-intent-backend-optimization-hybrid`)
- (`reasoning-c-un-problema-vorrei-sapere-di-pi-3203`) --[FULFILLS]--> (`user-intent-c-un-problema-vorrei-sapere-di-pi-3203`)
- (`reasoning-caratterizzazione-trasduttore-lineare`) --[FULFILLS]--> (`user-intent-definizione-ecografo-trasduttore-lineare`)
- (`reasoning-che-ne-pensi-del-mio-cervello-artif-8743`) --[FULFILLS]--> (`user-intent-che-ne-pensi-del-mio-cervello-artif-8743`)
- (`reasoning-che-ne-pensi-del-mio-cervello-artif-8793`) --[FULFILLS]--> (`user-intent-che-ne-pensi-del-mio-cervello-artif-8793`)
- (`reasoning-che-ore-sono-3134`) --[FULFILLS]--> (`user-intent-che-ore-sono-3134`)
- (`reasoning-chi-pierfrancesco-amendola-e-cosa-8426`) --[FULFILLS]--> (`user-intent-chi-pierfrancesco-amendola-e-cosa-8426`)
- (`reasoning-cloud-git-auto-push`) --[FULFILLS]--> (`user-intent-cloud-git-auto-push`)
- (`reasoning-comando-prompt-copia-rapi-8585`) --[FULFILLS]--> (`user-intent-comando-prompt-copia-rapi-8585`)
- (`reasoning-costruzione-collaudo-ecosistema-supercervello`) --[FULFILLS]--> (`user-intent-implementazione-ecosistema-supercervello`)
- (`reasoning-creazione-video-showcase-universal-brain`) --[FULFILLS]--> (`user-intent-creazione-video-showcase-universal-brain`)
- (`reasoning-diagnosi-discrepanza-deploy-render`) --[FULFILLS]--> (`user-intent-allineamento-nodi-render`)
- (`reasoning-diagnosi-retrieval-gemini-e-roadmap-potenziamento`) --[FULFILLS]--> (`user-intent-analisi-feedback-gemini-ottimizzazione-cervello`)
- (`reasoning-e2e-test-session-hook-2447`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-2447`)
- (`reasoning-e2e-test-session-hook-2471`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-2471`)
- (`reasoning-e2e-test-session-hook-2485`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-2485`)
- (`reasoning-e2e-test-session-hook-2529`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-2529`)
- (`reasoning-e2e-test-session-hook-2691`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-2691`)
- (`reasoning-e2e-test-session-hook-8745`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-8745`)
- (`reasoning-e2e-test-session-hook-9065`) --[FULFILLS]--> (`user-intent-e2e-test-session-hook-9065`)
- (`reasoning-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[FULFILLS]--> (`user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`)
- (`reasoning-eliminazione-jarvis-pulizia`) --[FULFILLS]--> (`user-intent-abbandono-jarvis-nuovo-progetto`)
- (`reasoning-embedding-projector-globe-and-optics`) --[FULFILLS]--> (`user-intent-embedding-projector-globe-and-optics`)
- (`reasoning-fix-daemon-render-persistence`) --[FULFILLS]--> (`user-intent-fix-daemon-render-persistence`)
- (`reasoning-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[FULFILLS]--> (`user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753`)
- (`reasoning-integrazione-esplicita-tabelle-comparative`) --[FULFILLS]--> (`user-intent-integrazione-tabelle-cappello-capitolo-6`)
- (`reasoning-jarvis-ricordi-quali-sono-gli-emis-3117`) --[FULFILLS]--> (`user-intent-jarvis-ricordi-quali-sono-gli-emis-3117`)
- (`reasoning-ma-tutto-falso-8462`) --[FULFILLS]--> (`user-intent-ma-tutto-falso-8462`)
- (`reasoning-mappatura-ecosistema-linux-3d`) --[FULFILLS]--> (`user-intent-distro-linux-modellazione-3d`)
- (`reasoning-non-riesci-a-connetterti-al-mio-cer-8486`) --[FULFILLS]--> (`user-intent-non-riesci-a-connetterti-al-mio-cer-8486`)
- (`reasoning-nuove-rappresentazioni-vi-2874`) --[FULFILLS]--> (`user-intent-nuove-rappresentazioni-vi-2874`)
- (`reasoning-occultamento-pulsanti-mob-9019`) --[FULFILLS]--> (`user-intent-occultamento-pulsanti-mob-9019`)
- (`reasoning-openjarvis-collegamento-connettoma`) --[FULFILLS]--> (`user-intent-integrazione-openjarvis-stanford`)
- (`reasoning-ottimizzazione-mobile-web-8880`) --[FULFILLS]--> (`user-intent-ottimizzazione-mobile-web-8880`)
- (`reasoning-ottimizzazione-sintetica-testo`) --[FULFILLS]--> (`user-intent-accorciamento-cappello-capitolo-6`)
- (`reasoning-piano-implementazione-jarvis-desktop`) --[FULFILLS]--> (`user-intent-creazione-repo-jarvis-desktop`)
- (`reasoning-potenziamento-cognitivo-obsidian-bridge`) --[FULFILLS]--> (`user-intent-potenziamento-cognitivo-obsidian-bridge`)
- (`reasoning-potenziamento-skill-e-ril-8338`) --[FULFILLS]--> (`user-intent-potenziamento-skill-e-ril-8338`)
- (`reasoning-progettazione-5-paradigmi-visuali-connettoma`) --[FULFILLS]--> (`user-intent-esplorazione-paradigmi-visuali-grafo`)
- (`reasoning-quali-sono-i-progetti-principali-di-8169`) --[FULFILLS]--> (`user-intent-quali-sono-i-progetti-principali-di-8169`)
- (`reasoning-quali-sono-le-abitudini-monitorate-2979`) --[FULFILLS]--> (`user-intent-quali-sono-le-abitudini-monitorate-2979`)
- (`reasoning-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[FULFILLS]--> (`user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794`)
- (`reasoning-rilascio-jarvis-desktop-completato`) --[FULFILLS]--> (`user-intent-creazione-repo-jarvis-desktop`)
- (`reasoning-risoluzione-residui-ollama-mac`) --[FULFILLS]--> (`user-intent-rimozione-modello-ollama-mac`)
- (`reasoning-ristrutturazione-sigillo-12-domini-completata`) --[FULFILLS]--> (`user-intent-ristrutturazione-sigillo-12-macro-domini`)
- (`reasoning-semplificazione-concettuale-causal-dl`) --[FULFILLS]--> (`user-intent-spiegazione-intuitiva-concetti-causali-attention`)
- (`reasoning-sintesi-teorica-swin-e-deep-stable-learning`) --[FULFILLS]--> (`user-intent-spiegazione-swin-transformer-deep-stable-learning`)
- (`reasoning-tassonomia-pkm-rag-notion-obsidian`) --[FULFILLS]--> (`user-intent-confronto-integrazioni-llm-notion-obsidian`)
- (`reasoning-telegram-keepalive-confirmation`) --[FULFILLS]--> (`user-intent-telegram-keepalive-confirmation`)
- (`reasoning-test-hook-session-end-2411`) --[FULFILLS]--> (`user-intent-test-hook-session-end-2411`)
- (`reasoning-ui-declutter-projector-fullscreen`) --[FULFILLS]--> (`user-intent-ui-declutter-projector-fullscreen`)
- (`reasoning-update-readme-architecture`) --[FULFILLS]--> (`user-intent-update-readme-architecture`)
- (`reasoning-validazione-architettura-zero-costi`) --[FULFILLS]--> (`user-intent-verifica-vincolo-zero-costi`)
- (`reasoning-valutazione-architetturale-supercervello`) --[FULFILLS]--> (`user-intent-review-piano-supercervello-os`)
- (`reasoning-verifica-openjarvis-ollama-gpt-cloud`) --[FULFILLS]--> (`user-intent-avvio-openjarvis-ollama-gpt-cloud`)
- (`reasoning-verify-github-token-render`) --[FULFILLS]--> (`user-intent-verify-github-token-render`)
- (`reasoning-architettura-mappamondo-spotlight-3d`) --[FULFILLS_INTENT]--> (`user-intent-mappamondo-3d-spotlight-relazioni`)
- (`intent-ep-20260827-graph-taxonomy-classification`) --[GENERATES_REASONING]--> (`reason-ep-20260827-graph-taxonomy-classification`)
- (`intent-ep-20260827-graph-tree-unification`) --[GENERATES_REASONING]--> (`reason-ep-20260827-graph-tree-unification`)
- (`intent-ep-20260827-hierarchical-overlay-reassurance`) --[GENERATES_REASONING]--> (`reason-ep-20260827-hierarchical-overlay-reassurance`)
- (`intent-ep-20260827-hierarchical-tree-deployment-sync`) --[GENERATES_REASONING]--> (`reason-ep-20260827-hierarchical-tree-deployment-sync`)
- (`intent-ep-20260827-telegram-bot-interface`) --[GENERATES_REASONING]--> (`reason-ep-20260827-telegram-bot-interface`)
- (`intent-ep-20260827-telegram-cognitive-hub-spec`) --[GENERATES_REASONING]--> (`reason-ep-20260827-telegram-cognitive-hub-spec`)
- (`intent-ep-20260827-tree-ranking-translation`) --[GENERATES_REASONING]--> (`reason-ep-20260827-tree-ranking-translation`)
- (`intent-ep-20260827-tree-structures-evaluation`) --[GENERATES_REASONING]--> (`reason-ep-20260827-tree-structures-evaluation`)
- (`user-intent-connect-gemini-claude-chatgpt-mcp`) --[GENERATES_REASONING]--> (`ai-reasoning-multi-llm-mcp-skill-distribution`)
- (`tax-ai-reasoning`) --[GOVERNS]--> (`ai-reasoning-clustering-decision`)
- (`concept-llm-indirect-injection-safeguard`) --[GOVERNS_INGESTION_FOR]--> (`universal-ai-brain`)
- (`node-tree-architecture-verdict`) --[GOVERNS_MULTISCALE_RETRIEVAL_OF]--> (`node-knowledge-graph-memory`)
- (`concept-modular-domain-subgraphs`) --[GOVERNS_PARTITIONING]--> (`domain-medicina-salute`)
- (`val-eternal-cognitive-continuity`) --[HELD_BY]--> (`person-pierfrancesco`)
- (`session-continuous-evolution`) --[HOSTED_ON]--> (`repo-github-universal-ai-brain`)
- (`concept-interhemispheric-inhibition-gating`) --[IMPLEMENTED_BY]--> (`algorithm-selective-hemispheric-activation`)
- (`aule-studio-app`) --[IMPLEMENTS_LOGIC]--> (`aule-studio-backend-arch`)
- (`universal-ai-brain`) --[INCORPORATES]--> (`tax-ai-reasoning`)
- (`node-universal-ai-brain-taxonomy`) --[INCORPORATES_AS_CORE_FEATURE]--> (`node-epistemic-grading-system`)
- (`universal-ai-brain`) --[INTEGRATES_AUDIT]--> (`graphify-knowledge-engine`)
- (`episode-20260829-architettura-connettoma-e-sync-prompt`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-avvio-intervista-universal-ai-hub`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-chiusura-jarvis-nuovo-progetto`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-completamento-rilascio-jarvis-desktop`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-debrief-assessment-gemini`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-definizione-piano-jarvis-desktop`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-esplorazione-paradigmi-interfaccia-grafo`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-integrazione-openjarvis-desktop`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-progettazione-jarvis-voice-ai`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-sigillatura-12-macro-domini`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-20260829-test-openjarvis-ollama-successo`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-allineamento-nodi-render-cloud`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-alternative-monetization-brainstorming`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-audit-critico-e-mockup-fr-2255`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-backend-optimization-session`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-bonifica-storage-ollama-mac`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-c-un-problema-vorrei-sapere-di-pi-3203`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-che-ne-pensi-del-mio-cervello-artif-8743`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-che-ne-pensi-del-mio-cervello-artif-8793`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-che-ore-sono-3134`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-chi-pierfrancesco-amendola-e-cosa-8426`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-chiarimento-concetti-tesi-deep-learning`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-chiarimento-intuitivo-pilastri-teorici`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-chiarimento-librerie-grafi-frontend`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-cloud-git-auto-push`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-comando-prompt-copia-rapi-8585`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-completamento-supercervello-ecosistema`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-disamina-integrazioni-notion-obsidian`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-disamina-trasduttori-lineari`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-2447`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-2471`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-2485`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-2529`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-2691`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-8745`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-e2e-test-session-hook-9065`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-embedding-projector-globe-and-optics`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-espansione-ecosistema-supercervello`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-esplorazione-linux-3d-modeling`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-fix-daemon-render-persistence`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-jarvis-ricordi-quali-sono-gli-emis-3117`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-ma-tutto-falso-8462`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-non-riesci-a-connetterti-al-mio-cer-8486`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-nuove-rappresentazioni-vi-2874`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-occultamento-pulsanti-mob-9019`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-ottimizzazione-mobile-web-8880`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-perfezionamento-cappello-tabelle-cap-6`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-potenziamento-cognitivo-obsidian-bridge`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-potenziamento-skill-e-ril-8338`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-quali-sono-i-progetti-principali-di-8169`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-quali-sono-le-abitudini-monitorate-2979`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-revisione-sintesi-cappello-cap-6`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-revisione-supercervello-cognitive-os`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-telegram-keepalive-confirmation`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-test-hook-session-end-2411`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-ui-declutter-projector-fullscreen`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-update-readme-architecture`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-valutazione-language-app-antigravity`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-verifica-costi-zero-euro`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-verify-github-token-render`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-video-showcase-anteprima-universal-brain`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`episode-yt-shorts-business-model`) --[INTERACTION_WITH]--> (`person-pierfrancesco`)
- (`skill-universal-brain-installed`) --[INTERFACES_WITH]--> (`node-knowledge-graph-memory`)
- (`node-mcp-brain-get-tree`) --[INTERROGATES]--> (`node-hierarchical-tree-engine-impl`)
- (`streaksup-darwin-ipc-protocol`) --[INVALIDATES_CACHE_FOR]--> (`streaksup-swiftdata-arch`)
- (`episode-frontend-deeptech-redesign-and-physics-zero-lag`) --[INVOLVES_USER]--> (`person-pierfrancesco`)
- (`identity-cs-researcher`) --[LEAD_PITCHED]--> (`proj-holly-benji-ai`)
- (`streaksup-i18n-runtime-engine`) --[LOCALIZES]--> (`proj-streaksup-app`)
- (`user-intent-zero-oscillation-high-performance-graph`) --[MANDATES_REQUIREMENT]--> (`architecture-vis-network-silent-stabilization-zero-lag`)
- (`lesson-backend-ground-truth-and-clean-canvas-rendering`) --[MENTAL_MODEL_OF]--> (`person-pierfrancesco`)
- (`person-pierfrancesco`) --[MENTORED_BY]--> (`rel-academic-mentors`)
- (`lesson-stoic-resilience`) --[MITIGATES]--> (`memory-perfectionism-tension`)
- (`reasoning-ui-declutter-projector-fullscreen`) --[MODIFIES]--> (`universal-ai-brain`)
- (`ai-reasoning-cross-model-provenance-validation`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-analisi-fattibilita-language-app`) --[OPTIMIZES]--> (`reasoning-language-app-architecture`)
- (`reasoning-analisi-stack-grafico-universal-brain`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-architettura-connettoma-web-vs-desktop`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-architettura-ecosistema-cognitivo-onnipresente`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-architettura-jarvis-zero-cost`) --[OPTIMIZES]--> (`proj-jarvis-voice-assistant`)
- (`reasoning-audit-critico-e-mockup-fr-2255`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-c-un-problema-vorrei-sapere-di-pi-3203`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-che-ore-sono-3134`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-cloud-git-auto-push`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-comando-prompt-copia-rapi-8585`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-costruzione-collaudo-ecosistema-supercervello`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-creazione-video-showcase-universal-brain`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-diagnosi-discrepanza-deploy-render`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-diagnosi-retrieval-gemini-e-roadmap-potenziamento`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-e2e-test-session-hook-2447`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-2471`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-2485`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-2529`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-2691`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-8745`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-e2e-test-session-hook-9065`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-embedding-projector-globe-and-optics`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-fix-daemon-render-persistence`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-jarvis-ricordi-quali-sono-gli-emis-3117`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-nuove-rappresentazioni-vi-2874`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-occultamento-pulsanti-mob-9019`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-ottimizzazione-mobile-web-8880`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-potenziamento-cognitivo-obsidian-bridge`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-potenziamento-skill-e-ril-8338`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-progettazione-5-paradigmi-visuali-connettoma`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-quali-sono-le-abitudini-monitorate-2979`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-rilascio-jarvis-desktop-completato`) --[OPTIMIZES]--> (`proj-jarvis-voice-assistant`)
- (`reasoning-ristrutturazione-sigillo-12-domini-completata`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-telegram-keepalive-confirmation`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-test-hook-session-end-2411`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-update-readme-architecture`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`reasoning-validazione-architettura-zero-costi`) --[OPTIMIZES]--> (`proj-cervelloartificiale`)
- (`reasoning-verify-github-token-render`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`test-cloud-git-autopush-verification`) --[OPTIMIZES]--> (`universal-ai-brain`)
- (`person-pierfrancesco`) --[ORCHESTRATED]--> (`session-evolution-ui-persistence`)
- (`node-knowledge-graph-memory`) --[ORGANIZES_CLUSTERS_INTO]--> (`node-hierarchical-dendrogram`)
- (`user-intent-reasoning-and-chat-memory`) --[ORIGINATED]--> (`tax-ai-reasoning`)
- (`user-intent-biological-lazy-loading-inhibition`) --[ORIGINATES_PARADIGM]--> (`concept-interhemispheric-inhibition-gating`)
- (`user-intent-modular-cluster-decentralization`) --[ORIGINATES_RULE]--> (`concept-modular-domain-subgraphs`)
- (`proj-appcalcolatori-ui-layer`) --[PART_OF_PROJECT]--> (`proj-appcalcolatori`)
- (`proj-cervelloartificiale-api-routes`) --[PART_OF_PROJECT]--> (`proj-cervelloartificiale`)
- (`proj-habittracker-ui-layer`) --[PART_OF_PROJECT]--> (`proj-habittracker`)
- (`proj-unistats-ui-layer`) --[PART_OF_PROJECT]--> (`proj-unistats`)
- (`person-pierfrancesco`) --[PERFORMS_IN]--> (`art-theatre-acting`)
- (`universal-ai-brain`) --[PERSISTS_INTO]--> (`sqlite-wal-persistence`)
- (`proj-streaksup-app`) --[PERSISTS_WITH]--> (`streaksup-swiftdata-arch`)
- (`proj-streaksup-app`) --[POWERED_BY]--> (`streaksup-gamification-engine`)
- (`universal-ai-brain`) --[POWERED_BY]--> (`fastapi-python-stack`)
- (`person-pierfrancesco`) --[PRACTICES]--> (`art-piano-composition`)
- (`node-knowledge-graph-memory`) --[PRESERVES_TOTAL_TOPOLOGY_IN]--> (`node-multiscale-overlay-pattern`)
- (`concept-llm-indirect-injection-safeguard`) --[PREVENTS_FALSE_POSITIVES_IN]--> (`ai-reasoning-hybrid-cloud-local-symbiosis`)
- (`person-pierfrancesco`) --[PRODUCES]--> (`art-creative-writing`)
- (`node-knowledge-graph-memory`) --[PROJECTS_INTO_LINEAR_DEDUCTION_VIA]--> (`node-mst-conceptual-backbone`)
- (`user-intent-hierarchical-multi-layer-graph-design`) --[PROPOSES_CONCEPT]--> (`concept-graph-of-graphs-hypergraph`)
- (`node-hierarchical-tree-engine-impl`) --[PROVIDES_HIERARCHICAL_VIEW_FOR]--> (`node-knowledge-graph-memory`)
- (`node-prefix-radix-trie`) --[PROVIDES_INSTANT_NODE_ACCESS_TO]--> (`node-knowledge-graph-memory`)
- (`node-knowledge-graph-memory`) --[PROVIDES_STATE_SPACE_AND_CONSTRAINTS]--> (`node-search-tree-deliberation`)
- (`ai-reasoning-clustering-decision`) --[RATIONALE_FOR]--> (`feat-progressive-areas`)
- (`kindle-3c40d6e17fd5`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-3e8f7aed7312`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-6d280a533c87`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-7439c883249f`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-bb8b1e467610`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-c7eedf9ce6bb`) --[READ_BY]--> (`person-pierfrancesco`)
- (`kindle-cba1775488ae`) --[READ_BY]--> (`person-pierfrancesco`)
- (`analysis-bst-vs-graph-taxonomy`) --[RECOMMENDS]--> (`idea-hierarchical-weighted-trees`)
- (`node-commit-965f0a8`) --[RECORDS_ARCHITECTURE_INTENT]--> (`node-telegram-webhook-gateway`)
- (`episode-frontend-deeptech-redesign-and-physics-zero-lag`) --[REFINED_COMPONENT]--> (`ui-component-palazzo-cognitivo-multi-layer-navigator`)
- (`lesson-boundaries-clarity`) --[REINFORCES]--> (`val-authenticity`)
- (`user-intent-valutazione-progetto-language-app`) --[RELATES_TO]--> (`intent-personal-language-learning-app`)
- (`identity-cs-researcher`) --[RESEARCHED]--> (`proj-bioinformatics-icar`)
- (`identity-cs-researcher`) --[RESEARCHING_THESIS]--> (`proj-tesi-busbra-cnr`)
- (`concept-llm-indirect-injection-safeguard`) --[RESOLVES_ISSUE_OF]--> (`intent-clarify-render-cloud-utility-and-llm-web-refusal`)
- (`ai-reasoning-hybrid-cloud-local-symbiosis`) --[RESPONDS_TO_INTENT]--> (`intent-clarify-render-cloud-utility-and-llm-web-refusal`)
- (`person-pierfrancesco`) --[ROOTED_IN]--> (`rel-napoli-culture`)
- (`project-royal-gambit-chess`) --[SATISFIES]--> (`user-intent-duolingo-chess-preference`)
- (`reasoning-hybrid-pedagogy-engine`) --[SOLVES]--> (`intent-personal-language-app-structure`)
- (`reasoning-language-app-architecture`) --[SOLVES]--> (`intent-personal-language-learning-app`)
- (`person-pierfrancesco`) --[STRIVES_FOR]--> (`val-impact-utility`)
- (`identity-cs-researcher`) --[STUDIED]--> (`coursework-cs-federico2`)
- (`epistemologia-rigorosa`) --[SUPPORTS]--> (`rule-zero-placeholder`)
- (`user-intent-abbandono-jarvis-nuovo-progetto`) --[TARGETS_PROJECT]--> (`proj-jarvis-voice-assistant`)
- (`user-intent-ai-shorts-evaluation`) --[TARGETS_PROJECT]--> (`domain-finanza-economia`)
- (`user-intent-allineamento-nodi-render`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-allora-vorrei-dirti-che-oggi-ho-man-4690`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-alternative-income-generation`) --[TARGETS_PROJECT]--> (`domain-finanza-economia`)
- (`user-intent-analisi-feedback-gemini-ottimizzazione-cervello`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-architettura-connettoma-web-vs-desktop`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-audit-critico-e-mockup-fr-2255`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-avvio-openjarvis-ollama-gpt-cloud`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-backend-optimization-hybrid`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-c-un-problema-vorrei-sapere-di-pi-3203`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-che-ne-pensi-del-mio-cervello-artif-8743`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-che-ne-pensi-del-mio-cervello-artif-8793`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-che-ore-sono-3134`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-chi-pierfrancesco-amendola-e-cosa-8426`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-chiarimento-stack-rendering-grafi-frontend`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-cloud-git-auto-push`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-comando-prompt-copia-rapi-8585`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-creazione-jarvis-voice-assistant`) --[TARGETS_PROJECT]--> (`proj-jarvis-voice-assistant`)
- (`user-intent-creazione-repo-jarvis-desktop`) --[TARGETS_PROJECT]--> (`proj-jarvis-voice-assistant`)
- (`user-intent-creazione-video-showcase-universal-brain`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-e2e-test-session-hook-2447`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-2471`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-2485`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-2529`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-2691`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-8745`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-e2e-test-session-hook-9065`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-ehi-jarvis-ehi-jarvis-mi-puoi-dire-3176`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-embedding-projector-globe-and-optics`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-espansione-supercervello-integrazioni`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-esplorazione-paradigmi-visuali-grafo`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-fix-daemon-render-persistence`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-ho-bisogno-di-sapere-tutto-ci-che-2753`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-implementazione-ecosistema-supercervello`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-integrazione-openjarvis-stanford`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-jarvis-ricordi-quali-sono-gli-emis-3117`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-ma-tutto-falso-8462`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-non-riesci-a-connetterti-al-mio-cer-8486`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-nuove-rappresentazioni-vi-2874`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-occultamento-pulsanti-mob-9019`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-ottimizzazione-mobile-web-8880`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-potenziamento-cognitivo-obsidian-bridge`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-potenziamento-skill-e-ril-8338`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-quali-sono-i-progetti-principali-di-8169`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-quali-sono-le-abitudini-monitorate-2979`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-quanti-nodi-ci-sono-nel-mio-cervell-4794`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-review-piano-supercervello-os`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-ristrutturazione-sigillo-12-macro-domini`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-telegram-keepalive-confirmation`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-test-hook-session-end-2411`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-ui-declutter-projector-fullscreen`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-universal-ai-hub-client`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-update-readme-architecture`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-verifica-vincolo-zero-costi`) --[TARGETS_PROJECT]--> (`proj-cervelloartificiale`)
- (`user-intent-verify-github-token-render`) --[TARGETS_PROJECT]--> (`universal-ai-brain`)
- (`user-intent-zero-cost-graphrag`) --[TRIGGERS]--> (`ai-reasoning-hybrid-search-mcp`)
- (`person-pierfrancesco`) --[UPHOLDS]--> (`val-transparency-loyalty`)
- (`project-royal-gambit-chess`) --[USES]--> (`tech-minimax-chess-engine`)
- (`node-neuro-symbolic-brain`) --[USES_AS_CEREBRAL_CORTEX]--> (`node-knowledge-graph-memory`)
- (`node-neuro-symbolic-brain`) --[USES_AS_PREFRONTAL_DELIBERATION]--> (`node-search-tree-deliberation`)
- (`identity-cs-researcher`) --[UTILIZES]--> (`arch-sqlite-wal`)
- (`ai-reasoning-cross-model-provenance-validation`) --[VALIDATES]--> (`user-intent-provenance-model-tracking`)
- (`ai-reasoning-shared-cognitive-state-continuity`) --[VALIDATES]--> (`goal-multi-ai-shared-context-persistence`)
- (`ai-reasoning-multi-llm-mcp-skill-distribution`) --[VALIDATES_IMPLEMENTATION]--> (`skill-universal-brain-installed`)
- (`person-pierfrancesco`) --[VALUES]--> (`val-independence`)
