# Chapter 6 translation and regression report

## Scope

- Unit: Chapter 6, *H1 and BMO*.
- Source range: PDF 127--144 / printed 115--132.
- Canonical TeX: `tex/chapters/chapter-06.tex` and `tex/chapters/chapter-06/`.
- Reviewed page metadata: `structured/reviewed/chapter-06.jsonl` and `translation/reviewed/chapter-06.jsonl`.

## Extraction and structure

- Source page containers: 18.
- Conservative raw blocks retained: 206.
- Translation anchors: one for each source page.
- Statement environments: 21, numbered consecutively as 6.1--6.21.
- Display groups: 79; 9 are numbered equations 6.1--6.9.
- Hidden-text formula candidates routed through review: 45; canonical TeX displays were checked against rendered source pages.

## Cross-references

- Semantic labels: 44, all unique.
- Determinable LaTeX reference commands: 57.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved bibliographic references: 52; none was guessed.
- Detailed ledger: `qa/translation/chapter-06-cross-reference-registry.tsv`.

No accepted Chapter 1--5 translation file changed in this batch. Chapter 6 begins on a fresh output page.

## Language and names

- Forbidden full-width punctuation in Chapter 6 Chinese prose: 0.
- Registered names first occurring in this source range: 33.
- Exact canonical name forms found: 33.
- Missing or altered registered names: 0.
- New terminology and name entries remain `needs-review`.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch6-regression-20260807-2`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 94 pages, 711536 bytes.
- Undefined references, multiply-defined labels, duplicate destinations, rerun warnings, and overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape.
- Cumulative artifact: `output/book-zh-progress.pdf`.

The Chapter 5/6 boundary and cumulative output pages 80--94 were rendered and visually inspected. No clipping, overflow, broken statement box, blank translated content page, or earlier-chapter layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 64 passed, 10 skipped.

## Result

Pass. Chapter 6 is complete for the supplied source and may be committed locally. The absent Bibliography and Index do not block Chapter 7.
