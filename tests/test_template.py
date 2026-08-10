"""Read-only template analysis, dependency, hash, and compilation tests."""

import unittest
from unittest import mock

from mathbook.project import ROOT, iter_files, sha256_file
from mathbook.template import (
    TEMPLATE_ROOT,
    analyze_template,
    build_manifest,
    compile_reference,
    dependency_report,
    strip_comments,
    validate_template_inputs,
)


class TemplateTests(unittest.TestCase):
    def test_inputs_are_complete(self) -> None:
        self.assertEqual(validate_template_inputs(), [])

    def test_manifest_hashes_match_files(self) -> None:
        manifest = build_manifest()
        for entry in manifest["files"]:
            self.assertEqual(entry["sha256"], sha256_file(ROOT / entry["path"]))

    def test_commands_and_reference_usage_are_recognized(self) -> None:
        analysis = analyze_template()
        command_names = {item["name"] for item in analysis["custom_commands"]}
        environment_names = {item["name"] for item in analysis["custom_environments"]}
        self.assertIn("\\ttt", command_names)
        self.assertIn("Theorem", environment_names)
        self.assertEqual(analysis["document_class"], "ctexart")
        self.assertGreater(analysis["reference_usage"]["display_math_double_dollar"], 0)

    def test_commented_inputs_are_not_dependencies(self) -> None:
        text = strip_comments("% \\input{missing.tex}\n\\input{active.tex}")
        self.assertNotIn("missing.tex", text)
        self.assertIn("active.tex", text)

    def test_missing_dependency_is_diagnosed(self) -> None:
        analysis = analyze_template()
        with mock.patch("mathbook.template._kpsewhich", return_value=None):
            report = dependency_report(analysis)
        self.assertGreater(len(report["missing"]), 0)

    def test_reference_compiles_without_changing_inputs(self) -> None:
        before = {path: sha256_file(path) for path in iter_files(TEMPLATE_ROOT)}
        report = compile_reference()
        after = {path: sha256_file(path) for path in iter_files(TEMPLATE_ROOT)}
        self.assertTrue(report["success"])
        self.assertTrue(report["template_integrity_verified"])
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
