---
id: streaksup-darwin-ipc-protocol
label: Cross-Process Darwin IPC Protocol
hemisphere: LEFT
primary_label: BUSINESS_LOGIC
category: BUSINESS_LOGIC
layer_level: 2
parent_graph_id: proj-streaksup-app
tags: [darwin-notifications, ipc, cross-process, cfnotificationcenter]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Cross-Process Darwin IPC Protocol

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `BUSINESS_LOGIC` | **Piano:** 2 | **Padre:** [[proj-streaksup-app]]

## 📝 Sintesi
Protocollo di sincronizzazione inter-processo basato su CFNotificationCenter per invalidare la cache ModelContext dell'app ad ogni mutazione da widget.

## 📋 Dettagli Strutturati
- **raw:** `notification_name`: com.pierfrancescoamendola.streaksup.habitDataChanged, `center`: CFNotificationCenterGetDarwinNotifyCenter(), `action`: modelContext.rollback() + fetchHabits()

## 🔗 Connessioni Uscenti
- [[streaksup-widget-suite-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[streaksup-swiftdata-arch]] (`INVALIDATES_CACHE_FOR`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[streaksup-widget-suite-ui]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[proj-streaksup-app]] (`CONTAINS_MODULE`) — _Restored from history_
