"""Shared and per-book project-path tests."""

import unittest

from mathbook.project import ProjectError, ProjectPaths, load_config, source_pdf_files, validate_book_id, validate_project_structure
from mathbook.workflow import book_status, list_books


class ProjectTests(unittest.TestCase):
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
        self.assertEqual([item["book_id"] for item in list_books(ProjectPaths())], ["fourier-analysis"])


if __name__ == "__main__":
    unittest.main()
