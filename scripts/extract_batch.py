"""Preserve raw PDF extraction and conservative structure/formula candidates for one batch."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

import pdfplumber
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "input" / "source" / "GSM029 - Fourier Analysis.pdf"


def stable_formula_id(batch_id: str, page: int, bbox: tuple[float, float, float, float], raw: str) -> str:
    payload = f"{batch_id}|{page}|{bbox!r}|{raw}".encode("utf-8")
    return f"formula-{batch_id}-" + hashlib.sha256(payload).hexdigest()[:16]


def group_lines(words: list[dict]) -> list[dict]:
    buckets: dict[int, list[dict]] = defaultdict(list)
    for word in words:
        buckets[round(float(word["top"]) / 3) * 3].append(word)
    lines = []
    for _, items in sorted(buckets.items()):
        items.sort(key=lambda item: float(item["x0"]))
        lines.append(
            {
                "text": " ".join(item["text"] for item in items),
                "x0": min(float(item["x0"]) for item in items),
                "x1": max(float(item["x1"]) for item in items),
                "top": min(float(item["top"]) for item in items),
                "bottom": max(float(item["bottom"]) for item in items),
                "fonts": sorted({str(item.get("fontname") or "unknown") for item in items}),
                "sizes": sorted({round(float(item.get("size") or 0), 2) for item in items}),
            }
        )
    return lines


def block_type(text: str) -> str:
    value = text.lstrip()
    if re.match(r"^Chapter\s+\d+", value, re.I):
        return "chapter"
    if re.match(r"^(?:§\s*)?\d+\.\s+", value):
        return "section"
    for label, kind in (
        ("Definition", "definition"),
        ("Theorem", "theorem"),
        ("Lemma", "lemma"),
        ("Proposition", "proposition"),
        ("Corollary", "corollary"),
        ("Example", "example"),
        ("Remark", "remark"),
        ("Exercise", "exercise"),
    ):
        if value.startswith(label):
            return kind
    if value.startswith("Proof"):
        return "proof"
    return "ordinary-paragraph"


def looks_formula(line: dict, page_width: float) -> bool:
    text = line["text"].strip()
    if not text or len(text) > 220:
        return False
    has_operator = bool(re.search(r"[=<>≤≥∫Σ∑∏]|\b(?:sup|inf|lim|max|min)\b", text))
    has_math_font = any("Symbol" in font or "Italic" in font for font in line["fonts"])
    centered_or_numbered = line["x0"] > page_width * 0.12 or bool(re.search(r"\(?\d+\.\d+\)?\s*$", text))
    sentence_like = text.endswith((".", ";", ":")) and len(text.split()) > 14
    return has_operator and has_math_font and centered_or_numbered and not sentence_like


def crop_formula(rendered_path: Path, page_width: float, page_height: float, bbox, output: Path) -> None:
    with Image.open(rendered_path) as image:
        sx = image.width / page_width
        sy = image.height / page_height
        x0, top, x1, bottom = bbox
        crop = (
            max(0, int(x0 * sx) - 12),
            max(0, int(top * sy) - 8),
            min(image.width, int(x1 * sx) + 12),
            min(image.height, int(bottom * sy) + 8),
        )
        image.crop(crop).save(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    parser.add_argument("--printed-offset", type=int, default=-12)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9-]+", args.batch_id):
        raise SystemExit("batch_id must contain only lowercase letters, digits, and hyphens")
    if args.start_page < 1 or args.end_page < args.start_page:
        raise SystemExit("invalid page range")

    raw_dir = ROOT / "workspace" / "raw-text" / args.batch_id
    layout_dir = ROOT / "workspace" / "layout" / args.batch_id
    formula_dir = ROOT / "workspace" / "formula-images" / args.batch_id
    rendered_dir = ROOT / "workspace" / "pages" / args.batch_id
    for directory in (raw_dir, layout_dir, formula_dir):
        directory.mkdir(parents=True, exist_ok=True)

    blocks: list[dict] = []
    formulas: list[dict] = []
    structure_review: list[dict] = []
    repairs: list[dict] = []
    with pdfplumber.open(PDF) as pdf:
        if args.end_page > len(pdf.pages):
            raise SystemExit(f"end page {args.end_page} exceeds PDF length {len(pdf.pages)}")
        for page_number in range(args.start_page, args.end_page + 1):
            page = pdf.pages[page_number - 1]
            printed_page = page_number + args.printed_offset
            text = page.extract_text(x_tolerance=2, y_tolerance=3, layout=True) or ""
            (raw_dir / f"page-{page_number:03d}.txt").write_text(text + "\n", encoding="utf-8")
            words = page.extract_words(
                x_tolerance=2,
                y_tolerance=3,
                extra_attrs=["fontname", "size"],
                keep_blank_chars=False,
            )
            lines = group_lines(words)
            layout = {
                "pdf_page": page_number,
                "printed_page": printed_page,
                "width_points": float(page.width),
                "height_points": float(page.height),
                "rotation": page.rotation,
                "words": words,
                "lines": lines,
                "source": "hidden OCR text layer and PDF coordinates",
                "raw_preserved": True,
            }
            (layout_dir / f"page-{page_number:03d}.json").write_text(
                json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

            page_blocks = []
            paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
            for index, paragraph in enumerate(paragraphs, start=1):
                kind = block_type(paragraph)
                confidence = 0.9 if kind != "ordinary-paragraph" else 0.68
                identifier = f"src-{args.batch_id}-p{page_number:03d}-b{index:03d}"
                block = {
                    "id": identifier,
                    "batch_id": args.batch_id,
                    "pdf_page": page_number,
                    "printed_page": printed_page,
                    "block_type": kind,
                    "environment_type": kind,
                    "number": None,
                    "source_text": paragraph,
                    "formula_ids": [],
                    "label": None,
                    "references": sorted(set(re.findall(r"\((\d+\.\d+)\)", paragraph))),
                    "footnote_ids": [],
                    "figure_ids": [],
                    "translation_status": "not-translated",
                    "confidence": confidence,
                    "review_status": "needs-review",
                }
                blocks.append(block)
                page_blocks.append(block)
                if confidence < 0.8:
                    structure_review.append(
                        {
                            "block_id": identifier,
                            "reason": "OCR paragraph segmentation and environment type require visual review.",
                            "confidence": confidence,
                            "review_status": "needs-review",
                        }
                    )

            page_formula_ids = []
            rendered = rendered_dir / f"page-{page_number:03d}.png"
            for line in (item for item in lines if looks_formula(item, float(page.width))):
                bbox = (line["x0"], line["top"], line["x1"], line["bottom"])
                identifier = stable_formula_id(args.batch_id, page_number, bbox, line["text"])
                crop_rel = f"workspace/formula-images/{args.batch_id}/{identifier}.png"
                if rendered.exists():
                    crop_formula(rendered, float(page.width), float(page.height), bbox, ROOT / crop_rel)
                equation_match = re.search(r"\(?((?:\d+)\.(?:\d+))\)?\s*$", line["text"].strip())
                formula = {
                    "id": identifier,
                    "batch_id": args.batch_id,
                    "pdf_page": page_number,
                    "printed_page": printed_page,
                    "bbox": [round(value, 3) for value in bbox],
                    "display": True,
                    "source_text": line["text"],
                    "latex": None,
                    "latex_status": "not-transcribed",
                    "equation_number": equation_match.group(1) if equation_match else None,
                    "label": None,
                    "references": [],
                    "confidence": 0.35,
                    "image_crop_path": crop_rel if rendered.exists() else None,
                    "review_status": "needs-review",
                    "token_checks": {
                        "subscripts": "pending",
                        "superscripts": "pending",
                        "parentheses": "pending",
                        "signs": "pending",
                        "integration_domains": "pending",
                        "summation_ranges": "pending",
                        "relations": "pending",
                    },
                }
                formulas.append(formula)
                page_formula_ids.append(identifier)
            for block in page_blocks:
                block["formula_ids"] = page_formula_ids
            repairs.append(
                {
                    "pdf_page": page_number,
                    "printed_page": printed_page,
                    "repairs": [],
                    "notes": "Raw extraction preserved. No automatic dehyphenation, header/footer removal, cross-page merge, or formula correction was applied.",
                }
            )

    structured_path = ROOT / "structured" / "source" / f"{args.batch_id}.jsonl"
    formula_path = ROOT / "formulae" / f"{args.batch_id}-formula-registry.jsonl"
    structure_review_path = ROOT / "qa" / "structure" / f"{args.batch_id}-review.jsonl"
    formula_review_path = ROOT / "qa" / "formula" / f"{args.batch_id}-review.jsonl"
    repair_path = ROOT / "workspace" / "layout" / f"{args.batch_id}-automatic-repair-log.json"
    for path in (structured_path, formula_path, structure_review_path, formula_review_path, repair_path):
        path.parent.mkdir(parents=True, exist_ok=True)
    structured_path.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in blocks), encoding="utf-8")
    formula_path.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in formulas), encoding="utf-8")
    structure_review_path.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in structure_review), encoding="utf-8")
    formula_review_path.write_text(
        "".join(
            json.dumps(
                {
                    "formula_id": item["id"],
                    "pdf_page": item["pdf_page"],
                    "reason": "Hidden OCR is not accepted as mathematical LaTeX; compare with the rendered source page.",
                    "review_status": "needs-review",
                },
                ensure_ascii=False,
            )
            + "\n"
            for item in formulas
        ),
        encoding="utf-8",
    )
    repair_path.write_text(json.dumps(repairs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "batch_id": args.batch_id,
                "pages": args.end_page - args.start_page + 1,
                "blocks": len(blocks),
                "formula_candidates": len(formulas),
                "structure_review_items": len(structure_review),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
