"""Stable and immutable formula registration tests."""

import unittest

from mathbook.formula import FormulaRegistry


class FormulaTests(unittest.TestCase):
    def test_formula_id_is_stable(self) -> None:
        registry = FormulaRegistry()
        first = registry.register("source-token-stream", ("source-token-stream",), 1, None, 1.0)
        second = registry.register("source-token-stream", ("source-token-stream",), 1, None, 1.0)
        self.assertEqual(first.id, second.id)
        self.assertEqual(first.source_latex, "source-token-stream")

    def test_uncertain_formula_cannot_be_preapproved(self) -> None:
        with self.assertRaises(ValueError):
            FormulaRegistry().register("source-token-stream", (), 1, None, 0.5, "approved")


if __name__ == "__main__":
    unittest.main()

