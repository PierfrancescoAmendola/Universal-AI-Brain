#!/usr/bin/env python3
"""
Universal AI Brain - Mac Workspace & Project Scanner (100% Read-Only)
====================================================================
Esplora in sola lettura l'intero Mac dell'utente (/Users/pierfrancesco) individuando:
- Repository Git
- Progetti Xcode / iOS (Swift, SwiftUI, SwiftData)
- Progetti Web / Fullstack (TypeScript, React, Node, HTML/CSS)
- Progetti Python / AI / Backend (FastAPI, Flask, Script)
- Progetti C / C++ / Algoritmi (LASD, Tesi, CMake, Makefile)
- Progetti Mobile (Flutter / Dart)
- Cartelle di Studio / Documentazione / Libri / Tesi

Filtra rigorosamente ogni directory di build, cache, file binari o di sistema (.git, node_modules, .venv, DerivedData, .DS_Store).
GARANZIA ASSOLUTA: Nessun file sorgente viene mai modificato, spostato o eliminato.
"""

import os
import sys
import time
from datetime import datetime, timezone
from typing import List, Dict, Any, Set, Optional

# Percorsi di scansione predefiniti sul Mac dell'utente
USER_HOME = os.path.expanduser("~")
DEFAULT_SCAN_ROOTS = [
    os.path.join(USER_HOME, "Desktop"),
    os.path.join(USER_HOME, "Documents"),
    os.path.join(USER_HOME, "Downloads"),
    os.path.join(USER_HOME, "DataMed"),
    os.path.join(USER_HOME, "MacPulse"),
    os.path.join(USER_HOME, "MacPulse2"),
    os.path.join(USER_HOME, "Script_di_Pulizia_Per_MacOs"),
    os.path.join(USER_HOME, "git"),
    os.path.join(USER_HOME, "source"),
    os.path.join(USER_HOME, "changemind"),
    os.path.join(USER_HOME, "Duckerfile"),
]

# Cartelle e percorsi di sistema da ignorare tassativamente
SYSTEM_IGNORE_DIRS = {
    ".git", "node_modules", ".venv", "venv", "env", "__pycache__",
    "deriveddata", "build", "dist", "out", ".next", ".nuxt",
    ".ds_store", ".trash", ".npm", ".cache", ".gradle", "pods",
    "xcuserdata", ".idea", ".vscode", "library", "pictures",
    "music", "movies", "applications", "public", ".gemini",
    ".antigravity", ".cargo", ".rustup", "site-packages",
    "vendor", ".pytest_cache", ".mypy_cache", ".angular",
    "graphify-out", "cache", "tmp", "temp", ".cpcache"
}

# Indicatori univoci di progetti software / workspace
PROJECT_INDICATORS = {
    # iOS / Apple
    "project.yml", "package.swift", "podfile", "cartfile",
    # JavaScript / TypeScript / Web
    "package.json", "tsconfig.json", "vite.config.js", "vite.config.ts", "next.config.js",
    # Python
    "pyproject.toml", "requirements.txt", "setup.py", "pipfile", "environment.yml",
    # C / C++ / Rust / Go / Java
    "cmakelists.txt", "makefile", "cargo.toml", "go.mod", "pom.xml", "build.gradle",
    # Flutter / Mobile
    "pubspec.yaml",
    # Docs / General
    "readme.md", "readme.txt", "readme", "index.html"
}

# Estensioni sorgente considerate codice o documentazione utile
RELEVANT_EXTENSIONS = {
    ".swift", ".py", ".ts", ".js", ".jsx", ".tsx", ".cpp", ".c", ".h", ".hpp",
    ".html", ".css", ".scss", ".dart", ".java", ".go", ".rs", ".sql", ".sh",
    ".md", ".json", ".yaml", ".yml", ".toml", ".pdf", ".docx", ".txt"
}


def is_system_or_ignored(dir_name: str) -> bool:
    """Verifica se una directory appartiene alla blacklist di sistema o cache."""
    return dir_name.lower() in SYSTEM_IGNORE_DIRS or dir_name.startswith(".")


def find_project_roots(search_paths: Optional[List[str]] = None, max_depth: int = 5) -> List[Dict[str, Any]]:
    """
    Scansiona ricorsivamente i percorsi specificati identificando la radice di ogni progetto.
    Ritorna una lista di descrittori di progetto con metadati e file chiave.
    """
    roots_to_scan = search_paths or DEFAULT_SCAN_ROOTS
    valid_scan_roots = [p for p in roots_to_scan if os.path.exists(p) and os.path.isdir(p)]
    
    discovered_projects: List[Dict[str, Any]] = []
    visited_paths: Set[str] = set()

    for root_dir in valid_scan_roots:
        _scan_directory_recursive(root_dir, root_dir, 0, max_depth, discovered_projects, visited_paths)

    return discovered_projects


def _scan_directory_recursive(
    current_dir: str,
    root_origin: str,
    current_depth: int,
    max_depth: int,
    discovered: List[Dict[str, Any]],
    visited: Set[str]
) -> bool:
    """
    Funzione ricorsiva di scansione read-only.
    Ritorna True se current_dir è una radice di progetto identificata.
    """
    real_path = os.path.realpath(current_dir)
    if real_path in visited or current_depth > max_depth:
        return False
    visited.add(real_path)

    base_name = os.path.basename(current_dir)
    if is_system_or_ignored(base_name) and current_depth > 0:
        return False

    try:
        entries = list(os.scandir(current_dir))
    except (PermissionError, FileNotFoundError, OSError):
        return False

    files_list = [e for e in entries if e.is_file(follow_symlinks=False)]
    dirs_list = [e for e in entries if e.is_dir(follow_symlinks=False) and not is_system_or_ignored(e.name)]

    file_names_lower = {f.name.lower(): f.name for f in files_list}
    
    # 1. Verifica se questa directory contiene file indicatori di progetto
    detected_indicators = [
        file_names_lower[ind] for ind in PROJECT_INDICATORS if ind in file_names_lower
    ]
    has_git = any(e.name == ".git" for e in entries if e.is_dir(follow_symlinks=False))

    # Criterio di identificazione radice progetto:
    # A) Contiene .git o file indicatori forti (es. package.json, project.yml, pyproject.toml, CMakeLists.txt)
    # B) Oppure ha file di codice rilevanti e non siamo alla radice generica di scansione (es. non /Users/.../Desktop)
    has_strong_indicator = has_git or any(
        ind.lower() in ("package.json", "project.yml", "pyproject.toml", "cargo.toml", "pubspec.yaml", "cmakelists.txt", "pom.xml", "makefile")
        for ind in detected_indicators
    )
    
    is_project_root = False
    if current_dir != root_origin:
        if has_strong_indicator:
            is_project_root = True
        elif detected_indicators and len(files_list) >= 2:
            is_project_root = True
        elif any(f.name.endswith(tuple(RELEVANT_EXTENSIONS)) for f in files_list) and not dirs_list:
            is_project_root = True

    if is_project_root:
        project_info = inspect_project_metadata(current_dir, files_list, detected_indicators, has_git)
        discovered.append(project_info)
        # Se è una radice di progetto, non scendiamo nei sotto-moduli a meno che non sia una monorepo esplicita
        is_monorepo = any(f.lower() in ("pnpm-workspace.yaml", "lerna.json") for f in detected_indicators)
        if not is_monorepo:
            return True

    # Continua la scansione nelle sotto-cartelle
    for d in dirs_list:
        _scan_directory_recursive(d.path, root_origin, current_depth + 1, max_depth, discovered, visited)

    return is_project_root


def inspect_project_metadata(
    project_dir: str,
    top_files: List[os.DirEntry],
    indicators: List[str],
    has_git: bool
) -> Dict[str, Any]:
    """
    Raccoglie statistiche e metadati di base sul progetto in maniera 100% read-only.
    """
    name = os.path.basename(project_dir)
    total_files = 0
    total_size_bytes = 0
    extensions_found: Set[str] = set()
    latest_mtime = 0.0

    try:
        for root, dirs, files in os.walk(project_dir):
            # Esclude cartelle di build e cache sul posto
            dirs[:] = [d for d in dirs if not is_system_or_ignored(d)]
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in RELEVANT_EXTENSIONS:
                    extensions_found.add(ext)
                    fp = os.path.join(root, f)
                    try:
                        st = os.stat(fp)
                        total_files += 1
                        total_size_bytes += st.st_size
                        latest_mtime = max(latest_mtime, st.st_mtime)
                    except (PermissionError, OSError):
                        pass
    except (PermissionError, OSError):
        pass

    mtime_dt = datetime.fromtimestamp(latest_mtime, tz=timezone.utc).isoformat() if latest_mtime > 0 else datetime.now(timezone.utc).isoformat()

    return {
        "name": name,
        "path": project_dir,
        "file_uri": f"file://{project_dir}",
        "has_git": has_git,
        "indicators": indicators,
        "extensions": sorted(list(extensions_found)),
        "relevant_files_count": total_files,
        "total_size_bytes": total_size_bytes,
        "last_modified": mtime_dt
    }


if __name__ == "__main__":
    print("🔍 Avvio Scansione Workspace Mac (100% Read-Only)...")
    t0 = time.time()
    projects = find_project_roots()
    t1 = time.time()
    print(f"✅ Scansione completata in {t1 - t0:.2f}s! Trovati {len(projects)} progetti/repository sul Mac:")
    for p in projects:
        print(f"  • [{p['name']}] ({p['relevant_files_count']} file) -> {p['path']}")
