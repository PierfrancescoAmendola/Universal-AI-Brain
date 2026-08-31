#!/usr/bin/env python3
"""
Universal AI Brain - Mac Project Semantic Stack Extractor (100% Read-Only)
==========================================================================
Analizza in sola lettura la struttura di un progetto identificato sul Mac:
- Estrae il titolo, la descrizione e le sezioni chiave dal README
- Riconosce lo stack tecnologico (SwiftUI, FastAPI, React, TypeScript, C++, Python, Flutter, ecc.)
- Assegna l'emisfero biologico (LEFT / RIGHT) e il Macro-Dominio del Palazzo Cognitivo (Piano 0)
- Genera i nodi di Progetto (Piano 1) e i Moduli Architetturali (Piano 2) con URI cliccabili (file:///)
"""

import os
import re
import json
from typing import Dict, Any, List, Optional, Set


def extract_project_semantics(project_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Estrae semantica completa, dipendenze e classificazione per un progetto Mac.
    """
    path = project_info["path"]
    name = project_info["name"]
    extensions = set(project_info.get("extensions", []))
    indicators = [i.lower() for i in project_info.get("indicators", [])]

    # 1. Riconoscimento Linguaggi & Framework
    languages: Set[str] = set()
    frameworks: Set[str] = set()
    tags: Set[str] = {"mac-project"}

    if ".swift" in extensions:
        languages.add("Swift")
        tags.add("swift")
    if ".py" in extensions:
        languages.add("Python")
        tags.add("python")
    if ".ts" in extensions or ".tsx" in extensions:
        languages.add("TypeScript")
        tags.add("typescript")
    if ".js" in extensions or ".jsx" in extensions:
        languages.add("JavaScript")
        tags.add("javascript")
    if ".cpp" in extensions or ".hpp" in extensions:
        languages.add("C++")
        tags.add("cpp")
    if ".c" in extensions or ".h" in extensions and ".cpp" not in extensions:
        languages.add("C")
        tags.add("c-lang")
    if ".dart" in extensions:
        languages.add("Dart")
        tags.add("flutter")
    if ".html" in extensions or ".css" in extensions:
        tags.add("web")

    # 2. Ispezione Config & Manifest (100% Read-Only)
    config_details = inspect_manifest_files(path)
    frameworks.update(config_details.get("frameworks", []))
    tags.update(config_details.get("tags", []))

    # 3. Lettura README (se presente)
    readme_info = read_project_readme(path)

    # 4. Assegnazione Emisfero e Macro-Dominio Fondativo (Piano 0)
    domain_id, hemisphere, primary_label = classify_project_domain(name, path, languages, frameworks, tags)

    # 5. Generazione ID univoco standardizzato
    slug = re.sub(r'[^a-zA-Z0-9_\-]+', '-', name.lower()).strip('-')
    project_id = f"proj-{slug}"

    # 6. Composizione sintesi semantica
    clean_label = format_project_label(name)
    summary = readme_info.get("summary") or f"Progetto Mac: {clean_label}. Stack: {', '.join(sorted(list(languages.union(frameworks)))) or 'Varie'}."

    details = {
        "local_path": path,
        "file_uri": f"file://{path}",
        "languages": sorted(list(languages)),
        "frameworks": sorted(list(frameworks)),
        "has_git": project_info.get("has_git", False),
        "relevant_files_count": project_info.get("relevant_files_count", 0),
        "last_modified": project_info.get("last_modified"),
        "key_dependencies": config_details.get("dependencies", [])[:15],
        "readme_excerpt": readme_info.get("excerpt", "")
    }

    # 7. Rilevamento Moduli Architetturali (Piano 2)
    atomic_modules = detect_atomic_modules(path, project_id, languages, frameworks)

    return {
        "id": project_id,
        "label": clean_label,
        "hemisphere": hemisphere,
        "primary_label": primary_label,
        "category": "PROJECT",
        "layer_level": 1,
        "parent_graph_id": domain_id,
        "summary": summary,
        "tags": sorted(list(tags.union({l.lower() for l in languages}, {f.lower() for f in frameworks}))),
        "details": details,
        "atomic_modules": atomic_modules
    }


def inspect_manifest_files(project_path: str) -> Dict[str, Any]:
    """Ispeziona i file di configurazione noti in sola lettura per scoprire librerie e framework."""
    frameworks: Set[str] = set()
    tags: Set[str] = set()
    dependencies: List[str] = []

    # A. package.json (Node / Web)
    pkg_json_path = os.path.join(project_path, "package.json")
    if os.path.exists(pkg_json_path):
        try:
            with open(pkg_json_path, "r", encoding="utf-8", errors="ignore") as f:
                data = json.load(f)
                all_deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                dependencies.extend(list(all_deps.keys()))
                
                dep_keys_lower = {k.lower() for k in all_deps.keys()}
                if "react" in dep_keys_lower: frameworks.add("React"); tags.add("react")
                if "next" in dep_keys_lower: frameworks.add("Next.js"); tags.add("nextjs")
                if "vue" in dep_keys_lower: frameworks.add("Vue"); tags.add("vue")
                if "express" in dep_keys_lower: frameworks.add("Express"); tags.add("backend")
                if "tailwindcss" in dep_keys_lower: frameworks.add("TailwindCSS"); tags.add("tailwind")
                if "vite" in dep_keys_lower: frameworks.add("Vite")
                if "cypress" in dep_keys_lower: frameworks.add("Cypress"); tags.add("testing")
        except Exception:
            pass

    # B. project.yml / Package.swift (iOS / Xcode)
    proj_yml_path = os.path.join(project_path, "project.yml")
    if os.path.exists(proj_yml_path):
        frameworks.add("XcodeGen")
        frameworks.add("SwiftUI")
        tags.add("ios")
        try:
            with open(proj_yml_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()
                if "swiftdata" in content: frameworks.add("SwiftData"); tags.add("swiftdata")
                if "widgetkit" in content: frameworks.add("WidgetKit"); tags.add("widgetkit")
                if "appgroup" in content or "group." in content: frameworks.add("AppGroup")
        except Exception:
            pass

    # C. pyproject.toml / requirements.txt (Python)
    req_path = os.path.join(project_path, "requirements.txt")
    if os.path.exists(req_path):
        try:
            with open(req_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = [line.strip().lower() for line in f if line.strip() and not line.startswith("#")]
                for l in lines:
                    pkg_name = re.split(r'[=<>~!]', l)[0].strip()
                    if pkg_name: dependencies.append(pkg_name)
                    if "fastapi" in pkg_name: frameworks.add("FastAPI"); tags.add("fastapi")
                    if "uvicorn" in pkg_name: frameworks.add("Uvicorn")
                    if "sqlalchemy" in pkg_name: frameworks.add("SQLAlchemy")
                    if "torch" in pkg_name or "pytorch" in pkg_name: frameworks.add("PyTorch"); tags.add("ai-ml")
                    if "pandas" in pkg_name: frameworks.add("Pandas")
        except Exception:
            pass

    return {
        "frameworks": sorted(list(frameworks)),
        "tags": sorted(list(tags)),
        "dependencies": dependencies
    }


def read_project_readme(project_path: str) -> Dict[str, str]:
    """Legge il README in sola lettura ed estrae sommario e abstract."""
    readme_candidates = ["README.md", "readme.md", "README.txt", "README", "readme.txt"]
    for candidate in readme_candidates:
        fp = os.path.join(project_path, candidate)
        if os.path.exists(fp):
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read(2048).strip()
                    lines = [l.strip() for l in content.split("\n") if l.strip()]
                    summary = ""
                    for line in lines:
                        if line.startswith("#"):
                            continue
                        if len(line) > 20:
                            summary = line[:200]
                            break
                    return {
                        "summary": summary,
                        "excerpt": content[:600]
                    }
            except Exception:
                pass
    return {"summary": "", "excerpt": ""}


def classify_project_domain(
    name: str,
    path: str,
    languages: Set[str],
    frameworks: Set[str],
    tags: Set[str]
) -> tuple[str, str, str]:
    """
    Determina l'emisfero biologico e il macro-dominio fondativo (Piano 0) a cui appartiene il progetto.
    """
    n_low = name.lower()
    p_low = path.lower()

    # 1. Salute / Medicina / Clinical
    if any(k in n_low or k in p_low for k in ("datamed", "alcool", "alcolsafe", "caretrack", "medical", "onicocriptosi", "salute")):
        return ("domain-medicina-salute", "RIGHT", "PROJECT")

    # 2. Relazioni & Social Matching
    if any(k in n_low or k in p_low for k in ("unimatch", "match", "relazioni", "social")):
        return ("domain-relazioni-comunicazione", "RIGHT", "PROJECT")

    # 3. Finanza & Abbonamenti
    if any(k in n_low or k in p_low for k in ("abbonamenti", "contocorrente", "finanza", "spese")):
        return ("domain-finanza-economia", "LEFT", "APP")

    # 4. Design & Palette
    if any(k in n_low or k in p_low for k in ("palette", "design", "grafica", "sfizi")):
        return ("domain-design-creativita", "RIGHT", "PROJECT")

    # 5. Università / Algoritmi / Tesi / Esami
    if any(k in n_low or k in p_low for k in ("uni", "tesi", "lasd", "lp1", "laurea", "calcolatori", "progetto-gestione-bibloteca", "basi di dati")):
        return ("domain-scienza-matematica", "LEFT", "PROJECT")

    # 6. Crescita Personale & Flashcards
    if any(k in n_low or k in p_low for k in ("flashcard", "abitudini", "voti", "scadenza")):
        return ("domain-crescita-personale", "RIGHT", "APP")

    # 7. Sistemi & Produttività / Script Mac
    if any(k in n_low for k in ("macpulse", "script_di_pulizia", "habittracker", "duckerfile", "pulizia", "backup", "aule")):
        return ("domain-produttivita-sistemi", "LEFT", "SCRIPT_TOOL")

    # 8. AI / Cognitive / LLM / Giochi Complessi
    if any(k in n_low for k in ("cervello", "libroai", "jarvis", "particle", "game", "scacchi", "changemind")):
        return ("domain-ai-cognitive-systems", "LEFT", "PROJECT")

    # Default: Ingegneria del Software (Include tutte le App iOS Swift, Web TypeScript, FastAPI)
    return ("domain-software-engineering", "LEFT", "APP" if "Swift" in languages or "SwiftUI" in frameworks else "PROJECT")


def format_project_label(name: str) -> str:
    """Formatta il nome della cartella in un titolo leggibile ed elegante."""
    # Rimuove prefissi o separatori
    clean = name.replace("_", " ").replace("-", " ")
    # Separa CamelCase
    clean = re.sub(r'([a-z])([A-Z])', r'\1 \2', clean)
    return clean.strip().title()


def detect_atomic_modules(project_path: str, project_id: str, languages: Set[str], frameworks: Set[str]) -> List[Dict[str, Any]]:
    """Identifica i sotto-moduli atomici e le architetture chiave per il Piano 2."""
    modules = []
    
    # Esempi di componenti chiave
    if "SwiftData" in frameworks or "SwiftUI" in frameworks:
        modules.append({
            "id": f"{project_id}-ui-layer",
            "label": f"SwiftUI Interface Layer ({project_id})",
            "hemisphere": "LEFT",
            "primary_label": "UI_COMPONENT",
            "layer_level": 2,
            "parent_graph_id": project_id,
            "summary": f"Interfaccia utente dichiarativa SwiftUI per il progetto {project_id}.",
            "tags": ["swiftui", "ui", "apple"]
        })
    if "FastAPI" in frameworks:
        modules.append({
            "id": f"{project_id}-api-routes",
            "label": f"FastAPI REST Endpoints ({project_id})",
            "hemisphere": "LEFT",
            "primary_label": "API_ENDPOINT",
            "layer_level": 2,
            "parent_graph_id": project_id,
            "summary": f"Pipeline API REST asincrona con validazione Pydantic per {project_id}.",
            "tags": ["fastapi", "rest-api", "python"]
        })

    return modules
