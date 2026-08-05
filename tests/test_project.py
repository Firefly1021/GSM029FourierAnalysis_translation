"""Project structure, configuration, and PDF phase-guard tests."""

import contextlib
import io
import unittest

from mathbook.cli import main
from mathbook.project import load_config, validate_project_structure


class ProjectTests(unittest.TestCase):
    def test_required_structure_exists(self) -> None:
        self.assertEqual(validate_project_structure(), [])

    def test_configurations_parse(self) -> None:
        project = load_config("project.yaml")
        translation = load_config("translation.yaml")
        self.assertEqual(project["template"]["engine"], "xelatex")
        self.assertTrue(translation["proper_names"]["preserve_exactly"])

    def test_full_book_pdf_commands_remain_guarded(self) -> None:
        for command in ("inspect-pdf", "render", "extract", "structure", "terminology", "check-names", "translate", "qa", "compile"):
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = main([command])
            self.assertEqual(code, 2)
            self.assertEqual(
                stderr.getvalue().strip(),
                f"The '{command}' command is not enabled beyond the validated sample.",
            )


if __name__ == "__main__":
    unittest.main()
