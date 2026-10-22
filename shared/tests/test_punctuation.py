"""Chinese-prose ASCII punctuation QA tests."""

import unittest

from mathbook.qa import find_chinese_prose_punctuation, normalize_chinese_prose_punctuation


class PunctuationTests(unittest.TestCase):
    def test_prose_is_normalized(self) -> None:
        source = "中文，正文。下一句（说明）：完成！\n"
        self.assertEqual(normalize_chinese_prose_punctuation(source), "中文,正文.下一句(说明):完成!\n")

    def test_math_and_reference_keys_are_protected(self) -> None:
        source = "正文，见 \\eqref{eq:保持，键}。数学 $\\text{保留，公式。}$。"
        normalized = normalize_chinese_prose_punctuation(source)
        self.assertIn("\\eqref{eq:保持，键}", normalized)
        self.assertIn("$\\text{保留，公式。}$", normalized)
        self.assertEqual(find_chinese_prose_punctuation(normalized), [])


if __name__ == "__main__":
    unittest.main()
