"""Check exact registered personal-name forms in one translated chapter."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_PAGE = re.compile(r"PDF\s+(\d+)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id")
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    args = parser.parse_args()

    files = [
        ROOT / "tex" / "chapters" / f"{args.chapter_id}.tex",
        *sorted((ROOT / "tex" / "chapters" / args.chapter_id).glob("*.tex")),
    ]
    translated = "\n".join(path.read_text(encoding="utf-8") for path in files if path.is_file())
    expected: list[dict[str, str]] = []
    with (ROOT / "glossary" / "proper-names.tsv").open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            match = PDF_PAGE.search(row["First Occurrence"])
            if match and args.start_page <= int(match.group(1)) <= args.end_page:
                expected.append(row)
    missing = [row for row in expected if row["Canonical Form"] not in translated]
    duplicate_entries: list[str] = []
    seen: set[str] = set()
    for row in expected:
        source = row["Source Form"]
        if source in seen:
            duplicate_entries.append(source)
        seen.add(source)

    report_path = ROOT / "qa" / "translation" / f"{args.chapter_id}-name-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = [
        f"# {args.chapter_id} personal-name report",
        "",
        f"- Registered names first occurring in source range: {len(expected)}",
        f"- Exact canonical forms found: {len(expected) - len(missing)}",
        f"- Missing exact forms: {len(missing)}",
        f"- Duplicate in-range registry entries: {len(duplicate_entries)}",
        "",
        "## Missing forms",
        "",
        *([f"- `{row['Canonical Form']}` ({row['First Occurrence']})" for row in missing] or ["- None."]),
        "",
        "## Duplicate registry entries",
        "",
        *([f"- `{name}`" for name in duplicate_entries] or ["- None."]),
        "",
        "## Result",
        "",
        "Pass: every in-range registered name is present byte-for-byte in the translated chapter."
        if not missing and not duplicate_entries
        else "Fail: review the findings above.",
        "",
    ]
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(f"registered={len(expected)} missing={len(missing)} duplicate_entries={len(duplicate_entries)}")
    return 0 if not missing and not duplicate_entries else 1


if __name__ == "__main__":
    raise SystemExit(main())
