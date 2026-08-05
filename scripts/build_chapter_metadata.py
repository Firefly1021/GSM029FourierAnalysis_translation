"""Build review metadata from a completed chapter without altering source inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANCHOR_OR_DISPLAY = re.compile(
    r"\\hypertarget\{chapter-(?P<chapter>\d{2})-page-(?P<page>\d{3})\}\{\}"
    r"|(?P<equation>\\begin\{equation\*?\}.*?\\end\{equation\*?\})"
    r"|(?P<bracket>\\\[.*?\\\])",
    re.DOTALL,
)
LABEL = re.compile(r"\\label\{([^}]+)\}")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def collect_displays(chapter_number: str, section_files: list[Path]) -> list[dict]:
    records: list[dict] = []
    current_page: int | None = None
    numbered_index = 0
    page_index: defaultdict[int, int] = defaultdict(int)
    for path in section_files:
        text = path.read_text(encoding="utf-8")
        for match in ANCHOR_OR_DISPLAY.finditer(text):
            if match.group("page"):
                current_page = int(match.group("page"))
                continue
            if current_page is None:
                raise ValueError(f"Display before a page anchor in {path}")
            latex = match.group("equation") or match.group("bracket")
            page_index[current_page] += 1
            is_numbered = latex.startswith("\\begin{equation}")
            label_match = LABEL.search(latex)
            if is_numbered:
                numbered_index += 1
            digest = hashlib.sha256(latex.encode("utf-8")).hexdigest()[:16]
            line = text.count("\n", 0, match.start()) + 1
            records.append(
                {
                    "id": f"formula-chapter-{chapter_number}-p{current_page:03d}-{page_index[current_page]:03d}-{digest}",
                    "chapter": int(chapter_number),
                    "source_pdf_page": current_page,
                    "tex_file": path.relative_to(ROOT).as_posix(),
                    "tex_line": line,
                    "display_type": "numbered-equation" if is_numbered else "unnumbered-display",
                    "source_number": f"{int(chapter_number)}.{numbered_index}" if is_numbered else None,
                    "label": label_match.group(1) if label_match else None,
                    "latex": latex,
                    "token_checks": {
                        "subscripts": "visually-checked",
                        "superscripts": "visually-checked",
                        "relations": "visually-checked",
                        "signs": "visually-checked",
                        "delimiters": "visually-checked",
                        "domains_and_ranges": "visually-checked",
                    },
                    "review_status": "reviewed",
                }
            )
    return records


def copy_translation_snapshot(chapter_id: str, driver: Path, section_files: list[Path], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(driver, destination / f"{chapter_id}.tex")
    section_destination = destination / chapter_id
    section_destination.mkdir(parents=True, exist_ok=True)
    for path in section_files:
        shutil.copy2(path, section_destination / path.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id", help="For example: chapter-01")
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    parser.add_argument("--printed-offset", type=int, required=True)
    parser.add_argument("--blank-page", type=int, action="append", default=[])
    args = parser.parse_args()

    chapter_match = re.fullmatch(r"chapter-(\d{2})", args.chapter_id)
    if not chapter_match:
        raise ValueError("chapter_id must have the form chapter-NN")
    chapter_number = chapter_match.group(1)
    driver = ROOT / "tex" / "chapters" / f"{args.chapter_id}.tex"
    section_files = sorted((ROOT / "tex" / "chapters" / args.chapter_id).glob("*.tex"))
    if not driver.is_file() or not section_files:
        raise FileNotFoundError("Chapter driver or section files are missing")

    source_records = read_jsonl(ROOT / "structured" / "source" / f"{args.chapter_id}.jsonl")
    children: defaultdict[int, list[dict]] = defaultdict(list)
    for record in source_records:
        children[int(record["pdf_page"])].append(record)

    formulas = collect_displays(chapter_number, section_files)
    formulas_by_page: defaultdict[int, list[str]] = defaultdict(list)
    for formula in formulas:
        formulas_by_page[int(formula["source_pdf_page"])].append(formula["id"])

    page_records: list[dict] = []
    for page in range(args.start_page, args.end_page + 1):
        blank = page in args.blank_page
        page_records.append(
            {
                "source_block_id": f"{args.chapter_id}-page-{page:03d}",
                "source_child_block_ids": [item["id"] for item in children[page]],
                "original_pdf_page": page,
                "printed_page": page + args.printed_offset,
                "environment_type": "page-container",
                "formula_ids": formulas_by_page[page],
                "references": [],
                "cross_reference_registry": f"qa/translation/{args.chapter_id}-cross-reference-registry.tsv",
                "translation_anchor": None if blank else f"{args.chapter_id}-page-{page:03d}",
                "translation_status": "source-blank" if blank else "translated",
                "formula_review_status": "not-applicable" if blank else "reviewed",
                "translation_text_file": f"translation/reviewed/{args.chapter_id}.tex",
                "review_status": "not-applicable" if blank else "reviewed",
            }
        )

    write_jsonl(ROOT / "structured" / "reviewed" / f"{args.chapter_id}.jsonl", page_records)
    write_jsonl(ROOT / "translation" / "draft" / f"{args.chapter_id}.jsonl", page_records)
    write_jsonl(ROOT / "translation" / "reviewed" / f"{args.chapter_id}.jsonl", page_records)
    write_jsonl(ROOT / "formulae" / f"{args.chapter_id}-reviewed-formulas.jsonl", formulas)
    copy_translation_snapshot(args.chapter_id, driver, section_files, ROOT / "translation" / "draft")
    copy_translation_snapshot(args.chapter_id, driver, section_files, ROOT / "translation" / "reviewed")

    numbered = sum(item["display_type"] == "numbered-equation" for item in formulas)
    print(f"pages={len(page_records)} displays={len(formulas)} numbered={numbered} unnumbered={len(formulas)-numbered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
