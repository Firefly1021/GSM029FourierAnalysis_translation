# PDF-to-printed-page mapping report

- PDF pages 9--14 correspond to printed roman pages v--x.
- PDF pages 15--388 correspond to printed pages 1--374 by `printed_page = pdf_page - 14`.
- Missing printed pages in that range: none detected.
- Unpaginated PDF pages: 1--8 and 389--400.
- Complete structured map: `structured/source/page-map.jsonl` and `structured/source/page-map.tsv`.
- Sample map: PDF 37--55 corresponds to printed 23--41, Chapter I, Section 2 tail through Section 3 opening.

All OCR blocks, formula records, QA issues, and translation source markers use both PDF and printed-page metadata when a printed page exists.
