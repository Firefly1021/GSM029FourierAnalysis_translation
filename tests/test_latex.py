"""LaTeX adapter conflict and output-interface tests."""

import unittest

from mathbook.build import TRANSLATED_ENVIRONMENT_REFERENCE
from mathbook.latex import adapter_environment_conflicts, emit_environment
from mathbook.project import ROOT


class LatexTests(unittest.TestCase):
    def test_adapter_only_overrides_authorized_user_environments(self) -> None:
        conflicts = adapter_environment_conflicts(
            ROOT / "template/style/Mystyle.sty",
            ROOT / "template/adapter/translation-adapter.sty",
        )
        self.assertEqual(
            conflicts,
            {"Theorem", "Definition", "Lemma", "Proposition", "Corollary", "Proof", "Example", "Exercise"},
        )

    def test_adapter_statement_environments_are_referenceable(self) -> None:
        adapter = (ROOT / "template/adapter/translation-adapter.sty").read_text(encoding="utf-8")
        for environment in ("Theorem", "Definition", "Lemma", "Proposition", "Corollary", "Example", "Remark", "Exercise"):
            self.assertIn(f"DocumentEnvironment{{{environment}}}", adapter)
        self.assertGreaterEqual(adapter.count("\\refstepcounter{statement}"), 8)
        self.assertIn("boxrule=0pt", adapter)
        self.assertIn("breakable", adapter)

    def test_output_uses_existing_environment(self) -> None:
        output = emit_environment("Theorem", "template-test-body", "template-test-title")
        self.assertIn("\\begin{Theorem}{template-test-title}", output)
        self.assertIn("\\end{Theorem}", output)

    def test_environment_display_names_remain_english(self) -> None:
        adapter = (ROOT / "template/adapter/translation-adapter.sty").read_text(encoding="utf-8")
        for heading in ("Theorem", "Definition", "Lemma", "Proposition", "Corollary", "Example", "Remark", "Exercise"):
            self.assertIn(f"{heading}~\\thestatement", adapter)
        self.assertIn("\\textbf{Proof:}", adapter)
        for translated in ("定理", "定义", "引理", "命题", "推论", "例~", "注~", "习题", "证明:"):
            self.assertNotIn(translated, adapter)

    def test_translated_environment_reference_prefix_is_rejected(self) -> None:
        self.assertIsNotNone(TRANSLATED_ENVIRONMENT_REFERENCE.search("见定理\\ref{thm:sample}."))
        self.assertIsNone(TRANSLATED_ENVIRONMENT_REFERENCE.search("见 Theorem~\\ref{thm:sample}."))


if __name__ == "__main__":
    unittest.main()
