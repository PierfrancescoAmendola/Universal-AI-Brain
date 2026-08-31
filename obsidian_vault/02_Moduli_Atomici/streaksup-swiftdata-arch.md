---
id: streaksup-swiftdata-arch
label: SwiftData Shared Container & Models
hemisphere: LEFT
primary_label: DATA_STRUCTURE
category: DATA_STRUCTURE
layer_level: 2
parent_graph_id: proj-streaksup-app
tags: [swiftdata, sqlite-wal, models, app-group, concurrency]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# SwiftData Shared Container & Models

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `DATA_STRUCTURE` | **Piano:** 2 | **Padre:** [[proj-streaksup-app]]

## 📝 Sintesi
Storage condiviso tra App principale ed estensione Widget tramite ModelContainer su SQLite WAL con modelli Habit, HabitLog e HabitCategory.

## 📋 Dettagli Strutturati
- **raw:** `models`: ['Habit', 'HabitLog', 'HabitCategory'], `helper`: SwiftDataHelper, `concurrency_protection`: ModelContext rollback su notifiche Darwin, `cascade_deletion`: Inverse relationship Habit -> logs

## 🔗 Connessioni Uscenti
- [[streaksup-privacy-zero-cloud]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[streaksup-privacy-zero-cloud]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[proj-streaksup-app]] (`CONTAINS_MODULE`) — _Restored from history_
- [[streaksup-darwin-ipc-protocol]] (`INVALIDATES_CACHE_FOR`) — _Restored from history_
- [[proj-streaksup-app]] (`PERSISTS_WITH`) — _Restored from history_
