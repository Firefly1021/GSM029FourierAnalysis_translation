"""Build reviewed metadata for the accepted Chapter 2 continuation."""

from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

from build_chapter_metadata import ROOT, collect_displays, read_jsonl, write_jsonl


def main() -> int:
    tail = ROOT / "tex" / "chapters" / "chapter-02-tail.tex"
    source = read_jsonl(ROOT / "structured" / "source" / "chapter-02-tail.jsonl")
    children: defaultdict[int, list[dict]] = defaultdict(list)
    for record in source:
        children[int(record["pdf_page"])].append(record)

    formulas = collect_displays("02", [tail], starting_numbered_index=12)
    by_page: defaultdict[int, list[str]] = defaultdict(list)
    for formula in formulas:
        by_page[int(formula["source_pdf_page"])].append(formula["id"])

    pages = []
    for page in range(52, 60):
        pages.append({
            "source_block_id": f"chapter-02-page-{page:03d}",
            "source_child_block_ids": [item["id"] for item in children[page]],
            "original_pdf_page": page,
            "printed_page": page - 12,
            "environment_type": "page-container",
            "formula_ids": by_page[page],
            "references": [],
            "cross_reference_registry": "qa/translation/chapter-02-cross-reference-registry.tsv",
            "translation_anchor": f"chapter-02-page-{page:03d}",
            "translation_status": "translated",
            "formula_review_status": "reviewed",
            "translation_text_file": "translation/reviewed/chapter-02-tail.tex",
            "review_status": "reviewed",
        })

    write_jsonl(ROOT / "structured" / "reviewed" / "chapter-02-tail.jsonl", pages)
    write_jsonl(ROOT / "translation" / "draft" / "chapter-02-tail.jsonl", pages)
    write_jsonl(ROOT / "translation" / "reviewed" / "chapter-02-tail.jsonl", pages)
    write_jsonl(ROOT / "formulae" / "chapter-02-tail-reviewed-formulas.jsonl", formulas)
    shutil.copy2(tail, ROOT / "translation" / "draft" / "chapter-02-tail.tex")
    shutil.copy2(tail, ROOT / "translation" / "reviewed" / "chapter-02-tail.tex")
    driver = ROOT / "tex" / "chapters" / "chapter-02.tex"
    shutil.copy2(driver, ROOT / "translation" / "draft" / "chapter-02.tex")
    shutil.copy2(driver, ROOT / "translation" / "reviewed" / "chapter-02.tex")

    accepted = read_jsonl(ROOT / "translation" / "reviewed" / "sample-pages-037-051.jsonl")
    write_jsonl(ROOT / "translation" / "reviewed" / "chapter-02.jsonl", accepted + pages)
    write_jsonl(ROOT / "structured" / "reviewed" / "chapter-02.jsonl", accepted + pages)
    print(f"tail_pages={len(pages)} displays={len(formulas)} numbered={sum(f['display_type'] == 'numbered-equation' for f in formulas)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
