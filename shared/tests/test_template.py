"""Read-only template analysis, dependency, hash, and compilation tests."""

import unittest
import hashlib
import json
from pathlib import Path
from unittest import mock

from mathbook.project import ROOT, iter_files, manifest_file_fingerprint, sha256_file
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
    def test_aljabr_visual_parameters_follow_original_template(self) -> None:
        upstream = TEMPLATE_ROOT / "collections/aljabr-1/upstream"
        adapter = (TEMPLATE_ROOT / "adapter/aljabr-1/feec-aljabr.sty").read_text(encoding="utf-8")
        reference = (upstream / "Template-AJbook.tex").read_text(encoding="utf-8")
        cls = (upstream / "AJbook.cls").read_text(encoding="utf-8")
        setting = r"\renewcommand*\arraystretch{1.5}"
        self.assertIn(setting, reference)
        self.assertIn(setting, adapter)
        for setting in (r"\theoremseparator{\ }", r"\theoremseparator{\enspace}"):
            self.assertIn(setting, cls)
            self.assertIn(setting, adapter)
        for override in (r"\emergencystretch", r"\geometry{", r"\fontsize", r"\setstretch", r"\setcounter{secnumdepth}", r"\setcounter{tocdepth}"):
            self.assertNotIn(override, adapter)
        self.assertNotIn("esint", adapter)

    def test_aljabr_summary_box_reuses_upstream_visual_keys(self) -> None:
        cls = (TEMPLATE_ROOT / "collections/aljabr-1/upstream/AJbook.cls").read_text(encoding="utf-8")
        adapter = (TEMPLATE_ROOT / "adapter/aljabr-1/feec-aljabr.sty").read_text(encoding="utf-8")
        for setting in ("colback = white, colbacktitle = white", "colframe = gray!50, boxrule=0.2mm", "before skip = 0.5cm", "top = 3mm", "bottom = 3mm"):
            self.assertIn(setting, cls)
            self.assertIn(setting, adapter)
        self.assertNotIn("KuangNei", adapter)

    def test_aljabr_backmatter_uses_native_template_layout(self) -> None:
        adapter = (TEMPLATE_ROOT / "adapter/aljabr-1/feec-aljabr.sty").read_text(encoding="utf-8")
        self.assertIn(r"\RequirePackage[xindy,splitindex]{imakeidx}", adapter)
        self.assertIn(r"\makeindex[columns=2,program=truexindy", adapter)
        for primitive in (r"\bibsetup\bibfont", r"\biblabelsep", r"\bibitemsep", r"\bibparsep"):
            self.assertIn(primitive, adapter)

    def test_aljabr_uses_unmodified_upstream_font_setup_without_fallback(self) -> None:
        text = (TEMPLATE_ROOT / "adapter/aljabr-1/feec-fonts.tex").read_text(encoding="utf-8")
        self.assertIn(r"\input{font-setup-open.tex}", text)
        self.assertNotIn(r"\setCJKfamilyfont", text)
        self.assertNotIn("FandolHei", text)

    def test_aljabr_official_noto_font_files_match_pinned_manifest(self) -> None:
        root = TEMPLATE_ROOT / "collections/aljabr-1/fonts/noto-sans-cjk-sc"
        data = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({row["weight"] for row in data["files"]}, {"Regular", "Bold", "Medium", "Black"})
        for row in data["files"]:
            raw = (root / row["file"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
            self.assertEqual(hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(), row["git_blob"])
        self.assertEqual(sha256_file(root / "LICENSE"), data["license_sha256"])

    def test_inputs_are_complete(self) -> None:
        self.assertEqual(validate_template_inputs(), [])

    def test_manifest_hashes_match_files(self) -> None:
        manifest = build_manifest()
        for entry in manifest["files"]:
            size, file_hash = manifest_file_fingerprint(ROOT / entry["path"])
            self.assertEqual(entry["size_bytes"], size)
            self.assertEqual(entry["sha256"], file_hash)

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
        # An optional class collection must never leak into the default build.
        self.assertFalse((Path(report["build_directory"]) / "AJbook.cls").exists())
        self.assertFalse((Path(report["build_directory"]) / "feec-aljabr.sty").exists())


if __name__ == "__main__":
    unittest.main()
