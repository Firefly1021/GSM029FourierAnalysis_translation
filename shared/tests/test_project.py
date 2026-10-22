"""Shared and per-book project-path tests."""

import tempfile
import unittest
from pathlib import Path

from mathbook.project import (
    ProjectError,
    ProjectPaths,
    directory_manifest_hash,
    load_config,
    manifest_file_fingerprint,
    source_pdf_files,
    validate_book_id,
    validate_project_structure,
)
from mathbook.workflow import book_status, list_books


class ProjectTests(unittest.TestCase):
    def test_manifest_fingerprints_are_portable_across_text_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_root = Path(first)
            second_root = Path(second)
            (first_root / "sample.tex").write_bytes(b"alpha\nbeta\n")
            (second_root / "sample.tex").write_bytes(b"alpha\r\nbeta\r\n")
            self.assertEqual(
                manifest_file_fingerprint(first_root / "sample.tex"),
                manifest_file_fingerprint(second_root / "sample.tex"),
            )
            self.assertEqual(directory_manifest_hash(first_root), directory_manifest_hash(second_root))

    def test_required_multi_book_structure_exists(self) -> None:
        self.assertEqual(validate_project_structure(), [])

    def test_configurations_parse(self) -> None:
        default = load_config("default.yaml")
        translation = load_config("translation.yaml")
        self.assertEqual(default["template"]["engine"], "xelatex")
        self.assertTrue(translation["proper_names"]["preserve_exactly"])

    def test_book_id_and_implicit_selection_guards(self) -> None:
        self.assertEqual(validate_book_id("fourier-analysis"), "fourier-analysis")
        for value in ("", "../escape", "Book", "two words", "a/b", "-leading"):
            with self.assertRaises(ProjectError):
                validate_book_id(value)
        with self.assertRaises(ProjectError):
            source_pdf_files()

    def test_completed_first_book_is_registered(self) -> None:
        status = book_status(ProjectPaths(), "fourier-analysis")
        self.assertEqual(status["status"], "completed")
        self.assertEqual(status["source_hash"], "03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf")
        self.assertIn("fourier-analysis", [item["book_id"] for item in list_books(ProjectPaths())])


if __name__ == "__main__":
    unittest.main()
