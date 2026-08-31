---
id: proj-appcalcolatori
label: App Calcolatori
hemisphere: LEFT
primary_label: PROJECT
category: PROJECT
layer_level: 1
parent_graph_id: domain-scienza-matematica
tags: [ios, mac-project, swift, swiftui, xcodegen]
confidence: EXTRACTED
updated_at: "2026-08-31T15:23:50.646666+00:00"
---

# App Calcolatori

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `PROJECT` | **Piano:** 1 | **Padre:** [[domain-scienza-matematica]]

## 📝 Sintesi
Native iPhone utility suite built with SwiftUI, Swift 6, and iOS 18+.

## 📋 Dettagli Strutturati
- **📂 Percorso Mac:** [file:///Users/pierfrancesco/Desktop/AppCalcolatori](file:///Users/pierfrancesco/Desktop/AppCalcolatori)
- **languages:**
  - Swift
- **frameworks:**
  - SwiftUI
  - XcodeGen
- **has_git:** False
- **relevant_files_count:** 23
- **last_modified:** 2026-07-29T07:41:17.289956+00:00
- **key_dependencies:**
- **readme_excerpt:** # PocketCalc+

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

## 🔗 Connessioni Uscenti
- [[domain-scienza-matematica]] (`BELONGS_TO_DOMAIN`) — _Progetto Mac catalogato nel suo macro-dominio di riferimento_
- [[person-pierfrancesco]] (`CREATED_BY`) — _Progetto ideato e sviluppato da Pierfrancesco Amendola_

## 📥 Connessioni Entranti (Backlinks)
- [[proj-appcalcolatori-ui-layer]] (`PART_OF_PROJECT`) — _Modulo architetturale del progetto_
