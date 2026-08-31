#!/usr/bin/env python3
"""
Unit tests for mac_stack_extractor.py
"""

import os
import shutil
import tempfile
import unittest

from mac_stack_extractor import extract_project_semantics, classify_project_domain


class TestStackExtractor(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
        # Progetto FastApi Python
        self.py_dir = os.path.join(self.test_dir, "MyFastAPIProject")
        os.makedirs(self.py_dir, exist_ok=True)
        with open(os.path.join(self.py_dir, "requirements.txt"), "w") as f:
            f.write("fastapi>=0.100.0\nuvicorn>=0.22.0\npydantic\n")
        with open(os.path.join(self.py_dir, "README.md"), "w") as f:
            f.write("# My FastAPI Project\nBackend REST asincrono per gestione dati.\n")
            
        # Progetto iOS SwiftUI
        self.ios_dir = os.path.join(self.test_dir, "AppAlcool")
        os.makedirs(self.ios_dir, exist_ok=True)
        with open(os.path.join(self.ios_dir, "project.yml"), "w") as f:
            f.write("name: AppAlcool\ntargets:\n  AppAlcool:\n    type: application\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_extract_python_project_semantics(self):
        """Verifica estrazione metadati FastAPI da requirements.txt e README.md."""
        proj_info = {
            "name": "MyFastAPIProject",
            "path": self.py_dir,
            "extensions": [".py", ".md", ".txt"],
            "indicators": ["requirements.txt", "README.md"],
            "has_git": True,
            "relevant_files_count": 5
        }
        res = extract_project_semantics(proj_info)
        self.assertEqual(res["id"], "proj-myfastapiproject")
        self.assertIn("Python", res["details"]["languages"])
        self.assertIn("FastAPI", res["details"]["frameworks"])
        self.assertEqual(res["parent_graph_id"], "domain-software-engineering")
        self.assertIn("file://", res["details"]["file_uri"])

    def test_extract_medical_ios_project(self):
        """Verifica classificazione di AppAlcool nel dominio medicina e salute."""
        proj_info = {
            "name": "AppAlcool",
            "path": self.ios_dir,
            "extensions": [".swift", ".yml"],
            "indicators": ["project.yml"],
            "has_git": False,
            "relevant_files_count": 25
        }
        res = extract_project_semantics(proj_info)
        self.assertEqual(res["id"], "proj-appalcool")
        self.assertEqual(res["hemisphere"], "RIGHT")
        self.assertEqual(res["parent_graph_id"], "domain-medicina-salute")
        self.assertIn("SwiftUI", res["details"]["frameworks"])


if __name__ == "__main__":
    unittest.main()
