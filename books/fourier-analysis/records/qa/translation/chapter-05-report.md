# Chapter 5 translation and regression report

## Scope

- Unit: Chapter 5, *Singular Integrals (II)*.
- Source range: PDF 103--126 / printed 91--114.
- Canonical TeX: `tex/chapters/chapter-05.tex` and `tex/chapters/chapter-05/`.
- Reviewed page metadata: `structured/reviewed/chapter-05.jsonl` and `translation/reviewed/chapter-05.jsonl`.

## Extraction and structure

- Source page containers: 24.
- Conservative raw blocks retained: 266.
- Translation anchors: one for each source page.
- Statement environments: 19, numbered consecutively as 5.1--5.19.
- Display groups: 74; 24 are numbered equations 5.1--5.24.

## Cross-references

- Semantic labels: 59, all unique.
- Determinable LaTeX reference commands: 77.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved forward or bibliographic references: 16; none was guessed.
- Detailed ledger: `qa/translation/chapter-05-cross-reference-registry.tsv`.

No accepted Chapter 1--4 translation file changed in this batch. Chapter 5 begins on a fresh output page.

## Language and names

- Forbidden full-width punctuation in Chapter 5 Chinese prose: 0.
- Registered names first occurring in this source range: 13.
- Exact canonical name forms found: 13.
- Missing or altered registered names: 0.
- New terminology and name entries remain `needs-review`.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch5-regression-20260805-2`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 80 pages, 636256 bytes.
- Undefined references, multiply-defined labels, duplicate destinations, rerun warnings, and overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape.
- Cumulative artifact: `output/book-zh-progress.pdf`.

The Chapter 4/5 boundary and cumulative output pages 68--80 were rendered and visually inspected. No clipping, overflow, broken statement box, blank translated content page, or earlier-chapter layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 5 is complete for the supplied source and may be committed locally. The absent Bibliography and Index do not block Chapter 6.
