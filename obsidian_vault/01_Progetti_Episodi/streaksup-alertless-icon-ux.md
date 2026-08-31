---
id: streaksup-alertless-icon-ux
label: Alertless App Icon Switcher Flow
hemisphere: RIGHT
primary_label: UX_FLOW
category: UX_FLOW
layer_level: 1
parent_graph_id: proj-streaksup-app
tags: [method-swizzling, app-icon, seamless-ux, toast-celebration]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Alertless App Icon Switcher Flow

> **Emisfero:** 🌸 Destro (Art & Values)  
> **Categoria:** `UX_FLOW` | **Piano:** 1 | **Padre:** [[proj-streaksup-app]]

## 📝 Sintesi
Flusso di cambio icona privo di frizione che silenzia l'alert nativo Apple tramite Method Swizzling su UIViewController e mostra un toast di celebrazione personalizzato.

## 📋 Dettagli Strutturati
- **raw:** `swizzling_target`: UIViewController.present(_:animated:completion:), `suppressor`: IconChangeAlertSuppressor, `feedback_view`: AppIconChangedToastView

## 🔗 Connessioni Uscenti
- [[proj-streaksup-app]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[proj-streaksup-app]] (`ENHANCES_EXPERIENCE_OF`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[proj-streaksup-app]] (`CONTAINS_MODULE`) — _Restored from history_
