# Sample extraction report

- Natural range: PDF pages 171-173, complete Section 6.3.
- Extraction source: native PDF text layer plus rendered-page verification.
- Raw extraction: `workspace/raw-text/sample-pages-171-173.txt`.
- Source records: `structured/source/sample-pages-171-173.jsonl`.
- Reviewed records: `structured/reviewed/sample-pages-171-173.jsonl`.
- Reviewed text blocks: 10.
- OCR used: no.
- Page boundaries recorded: yes.
- Layout and formula verification against rendered pages: passed.

Text-layer spacing artifacts were not silently treated as source typography. Every sample formula and structural boundary was checked against rendered PDF pages 171-173.
