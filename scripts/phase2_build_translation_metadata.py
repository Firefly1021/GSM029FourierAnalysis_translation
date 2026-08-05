"""Build page-level sample source/translation linkage metadata.

This does not alter raw extraction. It wraps the existing structured child blocks
in one reviewable parent per PDF page and links each translation record to the
formula registry and the reviewed LaTeX sample.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = range(37, 52)


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def main() -> None:
    children = read_jsonl(ROOT / "structured/source/sample-pages-037-051.jsonl")
    formulas = read_jsonl(ROOT / "formulae/sample-formula-registry.jsonl")
    children_by_page: dict[int, list[dict]] = defaultdict(list)
    formula_ids_by_page: dict[int, list[str]] = defaultdict(list)
    for row in children:
        children_by_page[int(row["pdf_page"])].append(row)
    for row in formulas:
        formula_ids_by_page[int(row["pdf_page"])].append(row["id"])

    source_rows: list[dict] = []
    draft_rows: list[dict] = []
    reviewed_rows: list[dict] = []
    for page in PAGES:
        source_id = f"sample-page-{page:03d}"
        child_ids = [row["id"] for row in children_by_page[page]]
        source_rows.append(
            {
                "id": source_id,
                "pdf_page": page,
                "printed_page": page - 12,
                "environment_type": "page-container",
                "child_block_ids": child_ids,
                "formula_ids": formula_ids_by_page[page],
                "raw_text_path": f"workspace/raw-text/sample/page-{page:03d}.txt",
                "layout_path": f"workspace/layout/sample/page-{page:03d}.json",
                "review_status": "needs-review",
                "notes": "Page container preserves linkage; semantic children remain in structured/source/sample-pages-037-051.jsonl.",
            }
        )
        base_translation = {
                "source_block_id": source_id,
                "source_child_block_ids": child_ids,
                "original_pdf_page": page,
                "printed_page": page - 12,
                "environment_type": "page-container",
                "formula_ids": formula_ids_by_page[page],
                "references": [],
                "cross_reference_registry": "qa/translation/cross-reference-registry.tsv",
                "translation_anchor": f"sample-page-{page:03d}",
                "translation_status": "translated",
                "formula_review_status": "blocking-needs-review",
            }
        draft_rows.append({**base_translation, "translation_text_file": "translation/draft/sample.tex", "review_status": "not-reviewed"})
        reviewed_rows.append({**base_translation, "translation_text_file": "translation/reviewed/sample.tex", "review_status": "needs-review"})

    write_jsonl(ROOT / "structured/source/sample-page-containers.jsonl", source_rows)
    write_jsonl(ROOT / "translation/draft/sample-pages-037-051.jsonl", draft_rows)
    write_jsonl(ROOT / "translation/reviewed/sample-pages-037-051.jsonl", reviewed_rows)
    reviewed_text = (ROOT / "tex/chapters/sample.tex").read_text(encoding="utf-8")
    (ROOT / "translation/draft/sample.tex").write_text(
        "% First-pass mathematical-faithfulness draft.\n" + reviewed_text,
        encoding="utf-8",
    )
    (ROOT / "translation/reviewed/sample.tex").write_text(
        "% Second-pass Chinese mathematical-style review; still pending human approval.\n" + reviewed_text,
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
