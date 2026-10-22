"""Exact personal-name and eponym terminology tests."""

import unittest

from mathbook.terminology import TerminologyRegistry, assert_name_preserved, name_is_preserved, translate_eponym_term


class NameTests(unittest.TestCase):
    def test_accents_are_preserved(self) -> None:
        self.assertTrue(name_is_preserved("Poincaré", "Poincaré"))
        self.assertFalse(name_is_preserved("Poincaré", "Poincare"))

    def test_hyphen_initials_and_abbreviation_are_preserved(self) -> None:
        for name in ("Lax--Milgram", "T.M. Apostol", "Célian Sun"):
            assert_name_preserved(name, name)
        with self.assertRaises(ValueError):
            assert_name_preserved("T.M. Apostol", "T. M. Apostol")

    def test_only_ordinary_eponym_noun_is_translated(self) -> None:
        self.assertEqual(translate_eponym_term("Hilbert space"), "Hilbert 空间")
        self.assertEqual(translate_eponym_term("Poincaré inequality"), "Poincaré 不等式")
        self.assertEqual(translate_eponym_term("Lax--Milgram theorem"), "Lax--Milgram 定理")

    def test_unconfirmed_term_cannot_be_approved(self) -> None:
        with self.assertRaises(ValueError):
            TerminologyRegistry().register("source-term", "target-term", None, "approved")


if __name__ == "__main__":
    unittest.main()
