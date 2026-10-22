"""Check or normalize ASCII punctuation in translated Chinese TeX prose."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from mathbook.script_context import selected_book_root

from mathbook.qa import find_chinese_prose_punctuation, normalize_chinese_prose_punctuation


ROOT = selected_book_root()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="tex/chapters/sample.tex")
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--report", default="qa/translation/punctuation-report.md")
    args = parser.parse_args()
    path = ROOT / args.path
    text = path.read_text(encoding="utf-8")
    before = find_chinese_prose_punctuation(text)
    if args.fix and before:
        path.write_text(normalize_chinese_prose_punctuation(text), encoding="utf-8")
    after_text = path.read_text(encoding="utf-8")
    after = find_chinese_prose_punctuation(after_text)
    counts = Counter(item.character for item in before)
    report = [
        "# Chinese-prose punctuation report",
        "",
        f"- File: `{args.path}`",
        "- Scope: translated Chinese prose only; math, comments, code, LaTeX reference commands and their keys are protected.",
        f"- Forbidden occurrences before normalization: {len(before)}",
        f"- Forbidden occurrences after normalization: {len(after)}",
        f"- Automatic normalization requested: {'Yes' if args.fix else 'No'}",
        "",
        "## Replacements",
        "",
    ]
    if counts:
        report.extend(f"- `{character}`: {count}" for character, count in sorted(counts.items()))
    else:
        report.append("- None.")
    report.extend(["", "## Result", "", "Pass." if not after else "Fail: forbidden punctuation remains.", ""])
    report_path = ROOT / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report), encoding="utf-8")
    if after:
        for item in after:
            print(f"{path}:{item.line}:{item.column}: {item.character} -> {item.replacement}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
