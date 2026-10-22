"""Preserve raw/layout sample data and create conservative structure/formula candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

import pdfplumber
from PIL import Image

from mathbook.script_context import selected_book_paths


BOOK = selected_book_paths()
ROOT = BOOK.root
PDF = BOOK.require_source_pdf()
def stable_formula_id(page: int, bbox: tuple[float, float, float, float], raw: str) -> str:
    payload = f"{page}|{bbox!r}|{raw}".encode("utf-8")
    return "formula-" + hashlib.sha256(payload).hexdigest()[:16]


def group_lines(words: list[dict]) -> list[dict]:
    buckets: dict[int, list[dict]] = defaultdict(list)
    for word in words:
        buckets[round(float(word["top"]) / 3) * 3].append(word)
    lines = []
    for top, items in sorted(buckets.items()):
        items.sort(key=lambda item: float(item["x0"]))
        lines.append({
            "text": " ".join(item["text"] for item in items),
            "x0": min(float(item["x0"]) for item in items),
            "x1": max(float(item["x1"]) for item in items),
            "top": min(float(item["top"]) for item in items),
            "bottom": max(float(item["bottom"]) for item in items),
            "fonts": sorted({str(item.get("fontname") or "unknown") for item in items}),
            "sizes": sorted({round(float(item.get("size") or 0), 2) for item in items}),
        })
    return lines


def block_type(text: str) -> str:
    value = text.lstrip()
    if re.match(r"^Chapter\s+\d+", value, re.I):
        return "chapter"
    if re.match(r"^\d+\.\s+", value):
        return "section"
    for label, kind in (("Theorem", "theorem"), ("Lemma", "lemma"), ("Proposition", "proposition"), ("Corollary", "corollary")):
        if value.startswith(label):
            return kind
    if value.startswith("Proof"):
        return "proof"
    return "ordinary-paragraph"


def looks_formula(line: dict, page_width: float) -> bool:
    text = line["text"].strip()
    if not text or len(text) > 180:
        return False
    has_operator = bool(re.search(r"[=<>≤≥∫Σ∑]|\b(?:sup|lim|max|min)\b", text))
    has_math_font = any("Symbol" in font or "Italic" in font for font in line["fonts"])
    centered_or_numbered = line["x0"] > page_width * 0.12 or bool(re.match(r"^\(?\d+\.\d+\)?", text))
    sentence_like = text.endswith((".", ";", ":")) and len(text.split()) > 10
    return has_operator and has_math_font and centered_or_numbered and not sentence_like


def crop_formula(rendered_path: Path, page_width: float, page_height: float, bbox, output: Path) -> None:
    with Image.open(rendered_path) as image:
        sx = image.width / page_width
        sy = image.height / page_height
        x0, top, x1, bottom = bbox
        pad_x, pad_y = 8, 5
        crop = (
            max(0, int(x0 * sx) - pad_x), max(0, int(top * sy) - pad_y),
            min(image.width, int(x1 * sx) + pad_x), min(image.height, int(bottom * sy) + pad_y),
        )
        image.crop(crop).save(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    args = parser.parse_args()
    if args.start_page < 1 or args.end_page < args.start_page:
        raise SystemExit("invalid page range")
    raw_dir = ROOT / "workspace" / "raw-text" / "sample"
    layout_dir = ROOT / "workspace" / "layout" / "sample"
    structured_dir = ROOT / "structured" / "source"
    formula_dir = ROOT / "workspace" / "formula-images" / "sample"
    registry_path = ROOT / "formulae" / "sample-formula-registry.jsonl"
    review_dir = ROOT / "qa" / "structure"
    formula_qa = ROOT / "qa" / "formula"
    for directory in (raw_dir, layout_dir, structured_dir, formula_dir, registry_path.parent, review_dir, formula_qa):
        directory.mkdir(parents=True, exist_ok=True)

    all_blocks = []
    all_formulas = []
    review_items = []
    repair_log = []
    with pdfplumber.open(PDF) as pdf:
        if args.end_page > len(pdf.pages):
            raise SystemExit(f"end page {args.end_page} exceeds PDF length {len(pdf.pages)}")
        for page_number in range(args.start_page, args.end_page + 1):
            page = pdf.pages[page_number - 1]
            text = page.extract_text(x_tolerance=2, y_tolerance=3, layout=True) or ""
            raw_dir.joinpath(f"page-{page_number:03d}.txt").write_text(text + "\n", encoding="utf-8")
            words = page.extract_words(x_tolerance=2, y_tolerance=3, extra_attrs=["fontname", "size"], keep_blank_chars=False)
            lines = group_lines(words)
            layout = {
                "pdf_page": page_number, "width_points": float(page.width), "height_points": float(page.height),
                "rotation": page.rotation, "words": words, "lines": lines,
                "source": "hidden OCR text layer and PDF coordinates", "raw_preserved": True,
            }
            layout_dir.joinpath(f"page-{page_number:03d}.json").write_text(json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
            for index, paragraph in enumerate(paragraphs, start=1):
                kind = block_type(paragraph)
                confidence = 0.92 if kind in {"chapter", "section", "theorem", "lemma", "proposition", "corollary", "proof"} else 0.72
                block = {
                    "id": f"src-p{page_number:03d}-b{index:03d}", "pdf_page": page_number,
                    "block_type": kind, "source_text": paragraph, "formula_ids": [],
                    "references": sorted(set(re.findall(r"\((\d+\.\d+)\)", paragraph))),
                    "confidence": confidence, "review_status": "needs-review" if confidence < 0.8 else "not-reviewed",
                }
                all_blocks.append(block)
                if confidence < 0.8:
                    review_items.append({"block_id": block["id"], "reason": "OCR paragraph segmentation requires review.", "confidence": confidence, "review_status": "needs-review"})

            rendered = ROOT / "workspace" / "pages" / "sample" / f"page-{page_number:03d}.png"
            page_formula_ids = []
            for formula_index, line in enumerate((item for item in lines if looks_formula(item, float(page.width))), start=1):
                bbox = (line["x0"], line["top"], line["x1"], line["bottom"])
                identifier = stable_formula_id(page_number, bbox, line["text"])
                crop_rel = f"workspace/formula-images/sample/{identifier}.png"
                if rendered.exists():
                    crop_formula(rendered, float(page.width), float(page.height), bbox, ROOT / crop_rel)
                equation_match = re.match(r"^\(?((?:\d+)\.(?:\d+))\)?", line["text"].strip())
                formula = {
                    "id": identifier, "pdf_page": page_number, "bbox": [round(value, 3) for value in bbox],
                    "display": True, "source_text": line["text"],
                    "latex": line["text"], "latex_status": "ocr-candidate-not-final",
                    "equation_number": equation_match.group(1) if equation_match else None,
                    "label": None, "references": [], "confidence": 0.45,
                    "image_crop_path": crop_rel if rendered.exists() else None,
                    "review_status": "needs-review",
                    "token_checks": {"subscripts": "pending", "superscripts": "pending", "parentheses": "pending", "signs": "pending", "integration_domains": "pending", "summation_ranges": "pending", "relations": "pending"},
                }
                all_formulas.append(formula)
                page_formula_ids.append(identifier)
            for block in all_blocks:
                if block["pdf_page"] == page_number:
                    block["formula_ids"] = page_formula_ids
            repair_log.append({
                "pdf_page": page_number,
                "repairs": [],
                "notes": "Raw extraction preserved. No automatic dehyphenation, header/footer removal, cross-page merge, or formula correction was applied.",
            })

    structured_dir.joinpath("sample-pages-037-051.jsonl").write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in all_blocks), encoding="utf-8")
    registry_path.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in all_formulas), encoding="utf-8")
    review_dir.joinpath("sample-review.jsonl").write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in review_items), encoding="utf-8")
    formula_qa.joinpath("sample-review.jsonl").write_text("".join(json.dumps({"formula_id": item["id"], "reason": "Hidden OCR is not accepted as final mathematical LaTeX.", "review_status": "needs-review"}, ensure_ascii=False) + "\n" for item in all_formulas), encoding="utf-8")
    ROOT.joinpath("workspace", "layout", "sample-automatic-repair-log.json").write_text(json.dumps(repair_log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = f"""# Sample formula report\n\n- Sample PDF pages: {args.start_page}--{args.end_page}\n- Detected display-formula candidates: {len(all_formulas)}\n- Stable IDs: SHA-256-derived from page, coordinates, and unmodified OCR source text.\n- Image crops: `workspace/formula-images/sample/`\n- Final LaTeX confidence: low. Every `latex` value is explicitly marked `ocr-candidate-not-final` and queued for manual token-by-token review.\n\nThe hidden OCR layer does not encode reliable mathematical structure. Compilation of an OCR candidate is not evidence of formula correctness. Inline-formula completeness and every subscript, superscript, delimiter, sign, integration domain, summation range, equality, and inequality remain blocking review items before full-book translation.\n"""
    formula_qa.joinpath("sample-formula-report.md").write_text(report, encoding="utf-8")
    print(json.dumps({"pages": args.end_page - args.start_page + 1, "blocks": len(all_blocks), "formula_candidates": len(all_formulas), "review_blocks": len(review_items)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
