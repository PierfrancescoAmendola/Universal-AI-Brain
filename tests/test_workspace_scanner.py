#!/usr/bin/env python3
"""
Unit tests for mac_workspace_scanner.py
"""

import os
import shutil
import tempfile
import unittest

from mac_workspace_scanner import find_project_roots, is_system_or_ignored


class TestWorkspaceScanner(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
        # 1. Progetto iOS mock
        self.ios_proj = os.path.join(self.test_dir, "MockIOSApp")
        os.makedirs(os.path.join(self.ios_proj, "Sources"), exist_ok=True)
        os.makedirs(os.path.join(self.ios_proj, "DerivedData"), exist_ok=True) # Ignored
        with open(os.path.join(self.ios_proj, "project.yml"), "w") as f:
            f.write("name: MockIOSApp\n")
        with open(os.path.join(self.ios_proj, "Sources", "App.swift"), "w") as f:
            f.write("import SwiftUI\n")
            
        # 2. Progetto Web mock con node_modules
        self.web_proj = os.path.join(self.test_dir, "MockWebPortal")
        os.makedirs(os.path.join(self.web_proj, "src"), exist_ok=True)
        os.makedirs(os.path.join(self.web_proj, "node_modules", "react"), exist_ok=True) # Ignored
        with open(os.path.join(self.web_proj, "package.json"), "w") as f:
            f.write('{"name": "mock-web"}\n')
        with open(os.path.join(self.web_proj, "src", "index.tsx"), "w") as f:
            f.write("export const App = () => <div>Hello</div>;\n")

        # 3. Progetto Python AI mock
        self.py_proj = os.path.join(self.test_dir, "MockPythonAI")
        os.makedirs(os.path.join(self.py_proj, ".venv"), exist_ok=True) # Ignored
        with open(os.path.join(self.py_proj, "pyproject.toml"), "w") as f:
            f.write('[project]\nname = "mock-ai"\n')
        with open(os.path.join(self.py_proj, "main.py"), "w") as f:
            f.write("print('AI Agent')\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_ignore_rules(self):
        """Verifica che le directory spazzatura e di cache vengano ignorate."""
        self.assertTrue(is_system_or_ignored("node_modules"))
        self.assertTrue(is_system_or_ignored(".git"))
        self.assertTrue(is_system_or_ignored("DerivedData"))
        self.assertTrue(is_system_or_ignored(".venv"))
        self.assertTrue(is_system_or_ignored(".DS_Store"))
        self.assertFalse(is_system_or_ignored("Sources"))
        self.assertFalse(is_system_or_ignored("AppAlcool"))

    def test_find_project_roots(self):
        """Verifica che lo scanner trovi tutti e 3 i progetti mock senza scendere nei node_modules/DerivedData."""
        projects = find_project_roots(search_paths=[self.test_dir])
        self.assertEqual(len(projects), 3)
        names = {p["name"] for p in projects}
        self.assertIn("MockIOSApp", names)
        self.assertIn("MockWebPortal", names)
        self.assertIn("MockPythonAI", names)
        
        # Verifica metadati
        ios_info = next(p for p in projects if p["name"] == "MockIOSApp")
        self.assertIn(".swift", ios_info["extensions"])
        self.assertEqual(ios_info["file_uri"], f"file://{self.ios_proj}")


if __name__ == "__main__":
    unittest.main()
