"""Audit ASCII punctuation in the Chinese prose of one translated chapter."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from mathbook.qa import find_chinese_prose_punctuation


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id", help="For example: chapter-01")
    parser.add_argument("--tex", action="append", help="Optional TeX file; repeat for a multi-file batch")
    args = parser.parse_args()
    files = (
        [ROOT / path for path in args.tex]
        if args.tex
        else [
            ROOT / "tex" / "chapters" / f"{args.chapter_id}.tex",
            *sorted((ROOT / "tex" / "chapters" / args.chapter_id).glob("*.tex")),
        ]
    )
    violations: list[tuple[Path, object]] = []
    for path in files:
        if path.is_file():
            violations.extend((path, item) for item in find_chinese_prose_punctuation(path.read_text(encoding="utf-8")))
    counts = Counter(item.character for _, item in violations)
    report_path = ROOT / "qa" / "translation" / f"{args.chapter_id}-punctuation-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = [
        f"# {args.chapter_id} Chinese-prose punctuation report",
        "",
        f"- Files checked: {len(files)}",
        "- Scope: Chinese prose only; math, comments, code, LaTeX commands, labels, paths, URLs, and bibliography data are protected.",
        f"- Forbidden full-width punctuation occurrences: {len(violations)}",
        "",
        "## Character counts",
        "",
        *([f"- `{character}`: {count}" for character, count in sorted(counts.items())] or ["- None."]),
        "",
        "## Findings",
        "",
        *(
            [
                f"- `{path.relative_to(ROOT).as_posix()}:{item.line}:{item.column}`: `{item.character}` -> `{item.replacement}`"
                for path, item in violations
            ]
            or ["- None."]
        ),
        "",
        "## Result",
        "",
        "Pass." if not violations else "Fail: forbidden punctuation remains.",
        "",
    ]
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(f"files={len(files)} violations={len(violations)}")
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
