---
id: reason-ep-20260827-telegram-cognitive-hub-spec
label: "Deduzione AI: Specifiche Tecniche e Mappatura Comandi dell'Hub C"
hemisphere: LEFT
primary_label: AI_REASONING
category: AI_REASONING
layer_level: 1
parent_graph_id: universal-ai-brain
tags: [ai-reasoning, epistemic-synthesis]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Deduzione AI: Specifiche Tecniche e Mappatura Comandi dell'Hub C

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `AI_REASONING` | **Piano:** 1 | **Padre:** [[universal-ai-brain]]

## 📝 Sintesi
Definita la pipeline I/O perimetrale: Telegram App -> HTTPS Webhook (/api/telegram/webhook) -> Whitelist Auth -> Intent Router (/search, /path, /tree, Ingest) -> brain.db.

## 📋 Dettagli Strutturati
- **raw:** `epistemic_rubric`: {'extracted': ['Integrazione di POST /api/telegram/webhook direttamente in main.py a costo zero', 'Comandi definiti: /search (FTS5 BM25), /path (BFS bidirezionale corpo calloso), /tree (Albero sintetico)', 'Supporto per parsing testo/audio per ingestione automatica in brain.db', 'Autenticazione di sicurezza tramite User ID Whitelist', 'Stato registrato al Commit 965f0a8: 110 nodi e 253 sinapsi'], 'inferred': ["L'architettura Telegram unifica il livello di percezione (audio/testo) con il livello di navigazione del connettoma (BFS inter-emisferico)", 'Il gateway funge da estensione mobile real-time del server MCP e del database SQLite'], 'ambiguous': []}, `architectural_synthesis`: Definita la pipeline I/O perimetrale: Telegram App -> HTTPS Webhook (/api/telegram/webhook) -> Whitelist Auth -> Intent Router (/search, /path, /tree, Ingest) -> brain.db., `model`: LLM Assistant (Historical Session)

## 🔗 Connessioni Uscenti
- [[ep-20260827-telegram-cognitive-hub-spec]] (`ANALYZES_EPISODE`) — _Restored from history_
- [[node-telegram-webhook-gateway]] (`ESTABLISHES_CONCEPT`) — _Restored from history_
- [[node-bidirectional-bfs-pathfinding]] (`ESTABLISHES_CONCEPT`) — _Restored from history_
- [[node-commit-965f0a8]] (`ESTABLISHES_CONCEPT`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[domain-ai-cognitive-systems]] (`BELONGS_TO_DOMAIN`) — _Restored from history_
- [[intent-ep-20260827-telegram-cognitive-hub-spec]] (`GENERATES_REASONING`) — _Restored from history_
