---
id: user-intent-provenance-model-tracking
label: Tracciamento Richiesta Utente & Modello AI nella Memoria
hemisphere: LEFT
primary_label: USER_INTENT
category: USER_INTENT
layer_level: 1
parent_graph_id: domain-ai-cognitive-systems
tags: [user-intent, model-attribution, context-preservation, cross-model-memory, episodic-tracking]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Tracciamento Richiesta Utente & Modello AI nella Memoria

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `USER_INTENT` | **Piano:** 1 | **Padre:** [[domain-ai-cognitive-systems]]

## 📝 Sintesi
Proposta utente: includere nel JSON di ingestione il prompt integrale e il modello AI sorgente per preservare contesto e consentire recall cross-modello.

## 📋 Dettagli Strutturati
- **raw:** `user_prompt`: quando l'ai dovrà restituire il json da inviare tramite post, dobbiamo inserire la richiesta dell'utente così da avere contesto, e inserire anche il modello che ha risposto..., `objective`: Consentire a modelli futuri (Claude, GPT, Gemini) di richiamare conversazioni con attribuzione esatta., `target_fields`: ['user_intent', 'model_name', 'timestamp', 'conversation_episode']

## 🔗 Connessioni Uscenti
- [[episode-cross-model-memory-architecture]] (`BELONGS_TO_EPISODE`) — _Restored from history_
- [[episode-cross-model-memory-architecture]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[ai-memory-ingest-spec]] (`EXTENDS`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[episode-cross-model-memory-architecture]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[domain-ai-cognitive-systems]] (`BELONGS_TO_DOMAIN`) — _Restored from history_
- [[goal-multi-ai-shared-context-persistence]] (`COMPLEMENTS`) — _Restored from history_
- [[ai-reasoning-cross-model-provenance-validation]] (`VALIDATES`) — _Restored from history_
