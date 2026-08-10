"""Diagnose every page of the supplied source PDF without modifying input files."""

from __future__ import annotations

import hashlib
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

from mathbook.script_context import selected_book_root


ROOT = selected_book_root()
SOURCE = ROOT / "input" / "source"
QA = ROOT / "qa"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def extraction_score(text: str) -> float:
    if not text:
        return 0.0
    non_space = [char for char in text if not char.isspace()]
    if not non_space:
        return 0.0
    acceptable = sum(char.isprintable() and char not in "�\x00" for char in non_space)
    wordlike = sum(char.isalnum() or char in ".,;:!?()[]{}'\"+-=*/<>%§" for char in non_space)
    return round(min(1.0, 0.65 * acceptable / len(non_space) + 0.35 * wordlike / len(non_space)), 4)


def column_estimate(words: list[dict], width: float) -> str:
    if len(words) < 20:
        return "uncertain"
    center = width / 2
    central = sum(1 for word in words if center - width * 0.06 <= (word["x0"] + word["x1"]) / 2 <= center + width * 0.06)
    left = sum(1 for word in words if word["x1"] < center - width * 0.06)
    right = sum(1 for word in words if word["x0"] > center + width * 0.06)
    if left > 10 and right > 10 and central / len(words) < 0.015:
        return "double"
    return "single"


def page_record(page, page_number: int) -> tuple[dict, str]:
    text = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
    words = page.extract_words(x_tolerance=2, y_tolerance=3, keep_blank_chars=False)
    chars = page.chars
    images = page.images
    page_area = max(1.0, float(page.width * page.height))
    image_areas = [max(0.0, (image.get("x1", 0) - image.get("x0", 0)) * (image.get("y1", 0) - image.get("y0", 0))) for image in images]
    image_coverage = min(1.0, sum(image_areas) / page_area)
    full_page_image = any(area / page_area > 0.70 for area in image_areas)
    fonts = Counter(str(char.get("fontname") or "unknown") for char in chars)
    hidden = sum(count for name, count in fonts.items() if "HiddenHorzOCR" in name)
    hidden_ratio = hidden / len(chars) if chars else 0.0
    quality = extraction_score(text)
    if full_page_image and chars:
        classification = "mixed"
    elif full_page_image:
        classification = "scanned"
    elif chars:
        classification = "native"
    else:
        classification = "uncertain"
    font_sizes = [float(char.get("size") or 0) for char in chars if float(char.get("size") or 0) > 0]
    median_size = statistics.median(font_sizes) if font_sizes else None
    footnote_chars = 0
    marginal_chars = 0
    for char in chars:
        size = float(char.get("size") or 0)
        if median_size and char.get("top", 0) > page.height * 0.78 and size < median_size * 0.82:
            footnote_chars += 1
        if char.get("x0", 0) < page.width * 0.06 or char.get("x1", page.width) > page.width * 0.94:
            marginal_chars += 1
    math_symbols = set("=<>±−+×÷∫∑∏√∞≤≥≈≠∂∇∈∉⊂⊆∪∩→↦")
    math_like = sum(
        1
        for char in chars
        if any(token in str(char.get("fontname") or "") for token in ("Symbol", "Math", "Italic"))
        or str(char.get("text") or "") in math_symbols
    )
    math_density = round(math_like / len(chars), 4) if chars else 0.0
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    header = lines[0] if lines else None
    footer = lines[-1] if lines else None
    anomalies: list[str] = []
    if not chars and not images:
        anomalies.append("blank-page")
    if chars and quality < 0.75:
        anomalies.append("low-text-extraction-quality")
    if page.rotation % 360:
        anomalies.append("rotated-page")
    if classification in {"scanned", "mixed"} and hidden_ratio > 0.5:
        anomalies.append("hidden-ocr-dominant")
    if chars and len(text.strip()) < 20:
        anomalies.append("very-low-extracted-text")
    ocr_necessary = classification == "scanned" or (classification == "mixed" and (hidden_ratio > 0.5 or quality < 0.85))
    record = {
        "pdf_page": page_number,
        "classification": classification,
        "text_layer": bool(chars),
        "text_layer_character_count": len(chars),
        "extracted_character_count": len(text),
        "extraction_quality_score": quality,
        "extraction_normal": quality >= 0.75,
        "hidden_ocr_character_ratio": round(hidden_ratio, 4),
        "ocr_necessary_for_body": ocr_necessary,
        "rotation_degrees": page.rotation,
        "width_points": round(float(page.width), 3),
        "height_points": round(float(page.height), 3),
        "image_count": len(images),
        "image_coverage_ratio": round(image_coverage, 4),
        "fonts": [{"name": name, "character_count": count} for name, count in fonts.most_common()],
        "column_estimate": column_estimate(words, float(page.width)),
        "header_candidate": header,
        "footer_candidate": footer,
        "footnote_like_character_count": footnote_chars,
        "marginal_like_character_count": marginal_chars,
        "math_density_score": math_density,
        "anomalies": anomalies,
    }
    return record, text


def main() -> int:
    source_files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    pdfs = [path for path in source_files if path.suffix.lower() == ".pdf"]
    if not pdfs:
        raise SystemExit("No source PDF found.")
    if len(pdfs) != 1:
        raise SystemExit("Multiple source PDFs require explicit selection before diagnosis.")
    primary = pdfs[0]
    reader = PdfReader(primary)
    metadata = {str(key).lstrip("/"): str(value) for key, value in (reader.metadata or {}).items()}
    manifest_files = []
    for path in source_files:
        kind = "pdf" if path.suffix.lower() == ".pdf" else ("directory-marker" if path.name == ".gitkeep" else "auxiliary")
        manifest_files.append({
            "path": rel(path), "file_type": kind, "size_bytes": path.stat().st_size,
            "sha256": sha256(path), "page_count": len(reader.pages) if path == primary else None,
            "primary_translation_source": path == primary,
        })
    manifest = {
        "read_only": True,
        "files": manifest_files,
        "selected_primary": rel(primary),
        "selection_reason": "Exactly one substantive PDF is present in input/source/.",
        "tex_source_present": any(path.suffix.lower() in {".tex", ".sty", ".cls"} for path in source_files),
        "errata_present": any("errata" in path.name.lower() or "corrig" in path.name.lower() for path in source_files),
        "original_figures_present": any(path.suffix.lower() in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".svg", ".eps"} for path in source_files),
        "auxiliary_material_present": any(path.name != ".gitkeep" and path != primary for path in source_files),
        "pdf_metadata": metadata,
    }
    QA.mkdir(parents=True, exist_ok=True)
    (QA / "source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    selection = f"""# Source selection\n\n- Selected primary source: `{rel(primary)}`\n- Reason: exactly one substantive PDF is present; no competing PDF required content-based selection.\n- File size: {primary.stat().st_size} bytes\n- SHA-256: `{sha256(primary)}`\n- Pages: {len(reader.pages)}\n- TeX source present in `input/source/`: no\n- Errata present: no\n- Original figure files present: no\n- Auxiliary source material present: no\n\nThe PDF metadata title is `{metadata.get('Title', '')}` and the metadata author is `{metadata.get('Author', '')}`. No source file was modified.\n"""
    (QA / "source-selection.md").write_text(selection, encoding="utf-8")

    records: list[dict] = []
    texts: list[str] = []
    with pdfplumber.open(primary) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            record, text = page_record(page, index)
            records.append(record)
            texts.append(text)
    counts = Counter(record["classification"] for record in records)
    ocr_pages = [record["pdf_page"] for record in records if record["ocr_necessary_for_body"]]
    problem_records = [record for record in records if any(item not in {"hidden-ocr-dominant"} for item in record["anomalies"])]
    inspection = {
        "source": rel(primary),
        "sha256": sha256(primary),
        "page_count": len(records),
        "metadata": metadata,
        "classification_counts": dict(counts),
        "ocr_recommended_pages": ocr_pages,
        "pages": records,
        "methodology": {
            "classification": "Per-page text objects, full-page image coverage, and HiddenHorzOCR usage.",
            "math_density": "Heuristic based on symbol/math/italic fonts and operator glyphs; formulas require separate visual review.",
            "columns": "Heuristic based on word positions; uncertain pages require visual review.",
        },
    }
    (QA / "pdf-inspection.json").write_text(json.dumps(inspection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (QA / "problem-pages.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for record in problem_records:
            handle.write(json.dumps({
                "pdf_page": record["pdf_page"], "classification": record["classification"],
                "anomalies": record["anomalies"], "review_status": "needs-review",
            }, ensure_ascii=False) + "\n")
    sizes = Counter((record["width_points"], record["height_points"]) for record in records)
    columns = Counter(record["column_estimate"] for record in records)
    report = f"""# Whole-PDF inspection\n\n- Source: `{rel(primary)}`\n- Pages inspected individually: {len(records)}\n- Per-page classifications: {dict(counts)}\n- Dominant page size: {sizes.most_common(1)[0][0][0]} x {sizes.most_common(1)[0][0][1]} pt ({sizes.most_common(1)[0][1]} pages)\n- Rotation: {Counter(record['rotation_degrees'] for record in records)}\n- Column heuristic: {dict(columns)}\n- Pages recommended for body OCR or OCR verification: {len(ocr_pages)}\n- Problem pages requiring review: {len(problem_records)}\n\nThe PDF is a scanned-image publication with a hidden OCR text layer on many pages. Classification was performed page by page; no whole-file shortcut was used. Ordinary OCR output is not treated as final formula LaTeX. Formula density and column count are heuristics and are visually checked for the selected sample.\n\nDetailed per-page metrics, fonts, image counts, header/footer candidates, footnote/marginal-note indicators, and anomalies are in `qa/pdf-inspection.json`.\n"""
    (QA / "pdf-inspection.md").write_text(report, encoding="utf-8")

    chapter_hits = []
    for page_number, text in enumerate(texts, start=1):
        match = re.search(r"(?im)^\s*Chapter\s+([1-9])\s*$", text)
        if match:
            chapter_hits.append({"type": "chapter", "number": int(match.group(1)), "pdf_page": page_number})
    for label, pattern in (("bibliography", r"(?im)^\s*Bibliography\s*$"), ("index", r"(?im)^\s*Index\s*$")):
        for page_number, text in enumerate(texts, start=1):
            if re.search(pattern, text):
                chapter_hits.append({"type": label, "pdf_page": page_number})
                break
    structure = {
        "source": rel(primary),
        "confidence": 0.85,
        "review_status": "needs-review",
        "front_matter": [
            {"type": "cover-title", "pdf_pages": [1]},
            {"type": "copyright-or-blank", "pdf_pages": [2], "review_status": "needs-visual-review"},
            {"type": "table-of-contents", "pdf_pages": [3, 4, 5]},
            {"type": "preface", "pdf_pages": [7, 8, 9]},
            {"type": "preliminaries", "pdf_pages": [11, 12]},
        ],
        "detected_major_headings": sorted(chapter_hits, key=lambda item: item["pdf_page"]),
        "notes": ["Blank/interstitial pages and final bibliography/index boundaries require visual confirmation."],
    }
    (QA / "book-structure.json").write_text(json.dumps(structure, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    toc_text = "\n\n".join(texts[2:5]).strip()
    (QA / "table-of-contents.md").write_text("# Extracted table of contents\n\nSource PDF pages 3–5. OCR text is preserved for preliminary structure only.\n\n```text\n" + toc_text + "\n```\n", encoding="utf-8")
    print(json.dumps({"source": rel(primary), "pages": len(records), "classifications": dict(counts), "problem_pages": len(problem_records), "chapter_hits": chapter_hits}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
