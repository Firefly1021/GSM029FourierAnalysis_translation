"""Build reviewed metadata for the translated front matter."""

from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

from build_chapter_metadata import collect_displays, read_jsonl, write_jsonl


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    source_records = read_jsonl(ROOT / "structured" / "source" / "frontmatter.jsonl")
    children: defaultdict[int, list[dict]] = defaultdict(list)
    for record in source_records:
        children[int(record["pdf_page"])].append(record)

    tex_path = ROOT / "tex" / "frontmatter.tex"
    formulas = collect_displays("00", [tex_path])
    formulas_by_page: defaultdict[int, list[str]] = defaultdict(list)
    for formula in formulas:
        formula["id"] = formula["id"].replace("formula-chapter-00", "formula-frontmatter")
        formula["chapter"] = None
        formula["unit"] = "frontmatter"
        formulas_by_page[int(formula["source_pdf_page"])].append(formula["id"])

    shared_toc_anchor = "frontmatter-page-003"
    blank_pages = {2, 6, 10}
    pages: list[dict] = []
    for page in range(1, 13):
        blank = page in blank_pages
        if page in {3, 4, 5}:
            anchor = shared_toc_anchor
        else:
            anchor = f"frontmatter-page-{page:03d}"
        pages.append(
            {
                "source_block_id": f"frontmatter-page-{page:03d}",
                "source_child_block_ids": [item["id"] for item in children[page]],
                "original_pdf_page": page,
                "printed_page": None,
                "environment_type": "page-container",
                "formula_ids": formulas_by_page[page],
                "references": [],
                "cross_reference_registry": "qa/translation/frontmatter-cross-reference-registry.tsv",
                "translation_anchor": anchor,
                "translation_status": "source-blank" if blank else "translated",
                "formula_review_status": "not-applicable" if blank else "reviewed",
                "translation_text_file": "translation/reviewed/frontmatter.tex",
                "review_status": "not-applicable" if blank else "reviewed",
            }
        )

    for directory in ("structured/reviewed", "translation/draft", "translation/reviewed"):
        write_jsonl(ROOT / directory / "frontmatter.jsonl", pages)
    write_jsonl(ROOT / "formulae" / "frontmatter-reviewed-formulas.jsonl", formulas)
    shutil.copy2(tex_path, ROOT / "translation" / "draft" / "frontmatter.tex")
    shutil.copy2(tex_path, ROOT / "translation" / "reviewed" / "frontmatter.tex")
    print(
        json.dumps(
            {
                "pages": len(pages),
                "blank_pages": len(blank_pages),
                "displays": len(formulas),
                "numbered": sum(item["display_type"] == "numbered-equation" for item in formulas),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
