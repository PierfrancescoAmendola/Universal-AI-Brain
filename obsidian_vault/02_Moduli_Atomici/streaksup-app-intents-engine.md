---
id: streaksup-app-intents-engine
label: App Intents & Dynamic Interactive Engine
hemisphere: LEFT
primary_label: API_SPEC
category: API_SPEC
layer_level: 2
parent_graph_id: proj-streaksup-app
tags: [app-intents, interactive-widgets, app-entity, toggle-habit]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# App Intents & Dynamic Interactive Engine

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `API_SPEC` | **Piano:** 2 | **Padre:** [[proj-streaksup-app]]

## 📝 Sintesi
Motore di interattività in-place per Widget e Live Activities tramite ToggleHabitIntent, HabitEntity e HabitEntityQuery.

## 📋 Dettagli Strutturati
- **raw:** `toggle_intent`: ToggleHabitIntent(habitID: String), `entity_query`: HabitEntityQuery, `config_intent`: SingleHabitConfigurationIntent, `sync_targets`: ['WidgetCenter.reloadAllTimelines', 'HabitActivityManager', 'Darwin IPC']

## 🔗 Connessioni Uscenti
- [[streaksup-dynamic-island-ui]] (`CONTROLS_IN_PLACE`) — _Restored from history_
- [[streaksup-dynamic-island-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[streaksup-widget-suite-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[streaksup-widget-suite-ui]] (`TRIGGERS_RELOAD_ON`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[streaksup-dynamic-island-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[streaksup-widget-suite-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[proj-streaksup-app]] (`CONTAINS_MODULE`) — _Restored from history_
- [[proj-streaksup-app]] (`EXPOSES_INTERACTIVITY_VIA`) — _Restored from history_
