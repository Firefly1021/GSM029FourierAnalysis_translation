"""Read-only source diagnosis; derived data stays within this book."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'shared/src'))
from mathbook.project import ProjectPaths, sha256_file
from mathbook.workflow import _write_json, verify_book_context
from pypdf import PdfReader
from pypdf.generic import ContentStream
import pdfplumber

BOOK_ID = 'an-introduction-to-partial-differential-equations'
project = ProjectPaths(ROOT)
book, _ = verify_book_context(project, BOOK_ID, writable=True)
source = book.require_source_pdf()
before = sha256_file(source)
reader = PdfReader(source)
rows = []
headings = []
with pdfplumber.open(source) as pdf:
    for index, page in enumerate(pdf.pages):
        text = reader.pages[index].extract_text() or ''
        images = page.images
        # Some scans are tiled into many image objects; the largest tile alone
        # must not cause an OCR scan to be misclassified as native/mixed.
        boxes = [(max(0, im['x0']), max(0, im['top']), min(page.width, im['x1']),
                  min(page.height, im['bottom'])) for im in images]
        xs = sorted({x for box in boxes for x in (box[0], box[2])})
        area = 0
        for xa, xb in zip(xs, xs[1:]):
            intervals = sorted((y0, y1) for x0, y0, x1, y1 in boxes if x0 < xb and x1 > xa)
            length, end = 0, 0
            for y0, y1 in intervals:
                length += max(0, y1 - max(y0, end))
                end = max(end, y1)
            area += (xb - xa) * length
        coverage = area / (page.width * page.height)
        render_modes = sorted({int(operands[0]) for operands, op in
                               ContentStream(reader.pages[index].get_contents(), reader).operations
                               if op == b'Tr' and operands})
        scan = coverage > .9
        resolutions = [round(min(im.get('srcsize', (0, 0))[0] / (im['width'] / 72),
                                 im.get('srcsize', (0, 0))[1] / (im['height'] / 72)), 1)
                       for im in images if im['width'] and im['height']]
        first = [s.strip() for s in text.splitlines()[:3]]
        observed = next((int(m.group(1)) for s in first if
                         (m := re.match(r'^(\d{1,3})\s+\d+\.', s))), None)
        if observed is None:
            observed = next((int(m.group(1)) for s in first if
                             (m := re.search(r'Questions\s+(\d{1,3})\s*$', s))), None)
        row = {'pdf_page': index + 1, 'width_pt': page.width, 'height_pt': page.height,
               'rotation': int(reader.pages[index].get('/Rotate', 0)),
               'image_count': len(images), 'image_union_coverage': round(coverage, 5),
               'scan_resolution_dpi': resolutions, 'text_characters': len(text),
               'text_rendering_modes': render_modes,
               'kind': 'scanned-with-hidden-ocr' if scan and text.strip() else
                       'scanned' if scan else 'mixed' if images else 'native' if text.strip() else 'unknown',
               'text_layer_reliability': 'not-authoritative' if scan else 'requires-validation',
               'printed_page_observed_ocr': observed,
               'printed_page_candidate': str(index - 9) if index >= 10 else None,
               'mapping_status': 'candidate-offset-not-individually-verified' if index >= 10 else 'frontmatter-needs-review'}
        rows.append(row)
        if index >= 10:
            for line in text.splitlines():
                if re.match(r'^\d{1,2}(?:\.\d{1,2}){1,2}\s+[A-Za-z]', line.strip()):
                    headings.append({'pdf_page': index+1, 'ocr_heading': line.strip(),
                                     'status': 'candidate-not-verified-against-image'})
        page.close()
        if (index+1) % 100 == 0:
            print('Diagnosed', index+1, 'pages', flush=True)
assert before == sha256_file(source)
summary = {'book_id': BOOK_ID, 'source_sha256': before, 'page_count': len(rows),
           'classification_counts': dict(Counter(row['kind'] for row in rows)),
           'source_type': 'scan with OCR text layer; image is authoritative',
           'native_extraction_strategy_rejected': True,
           'scope': 'All-page image/text-layer diagnosis; no claim of full-book mathematical OCR verification.',
           'printed_mapping': 'PDF page minus 10 is a body-page candidate; only sample mappings are visually verified.'}
_write_json(book.qa / 'page-diagnosis.json', {'summary': summary, 'pages': rows})
_write_json(book.root / 'structured/source/page-map.json', {'pages': rows})
_write_json(book.root / 'structured/source/heading-candidates.json', {'headings': headings})
print(json.dumps(summary, indent=2))
