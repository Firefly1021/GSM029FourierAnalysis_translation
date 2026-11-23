# Chapter 9 translation and regression report

## Scope

- Unit: Chapter 9, *The T1 Theorem*.
- Source range: PDF 207--228 / printed 195--216.
- Canonical TeX: `tex/chapters/chapter-09.tex` and `tex/chapters/chapter-09/`.
- Reviewed page metadata: `structured/reviewed/chapter-09.jsonl` and `translation/reviewed/chapter-09.jsonl`.

## Extraction and structure

- Source page containers: 22.
- Conservative raw blocks retained: 249.
- Translation anchors: one for each source page.
- Statement environments: 19, numbered consecutively as 9.1--9.19.
- Display groups: 142; 9 are numbered equations 9.1--9.9.
- Hidden-text formula candidates routed through review: 77; canonical TeX displays were checked against rendered source pages.

## Cross-references

- Semantic labels: 38, all unique.
- Determinable LaTeX reference commands: 65.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved source citations: 5; none was guessed because the supplied source has no bibliography.
- Detailed ledger: `qa/translation/chapter-09-cross-reference-registry.tsv`.

No accepted Chapter 1--8 translation file changed in this batch. Chapter 9 begins on a fresh output page.

## Language and names

- Forbidden full-width punctuation in Chapter 9 Chinese prose: 0.
- Registered names first occurring in this source range: 13.
- Exact canonical name forms found: 13.
- Missing or altered registered names: 0.
- New terminology and name entries remain `needs-review`.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch9-regression-20260807-1`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 160 pages, 1029733 bytes.
- Undefined references, multiply-defined labels, duplicate destinations, rerun warnings, and overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape; pre-existing math-in-bookmark warnings remain nonfatal.
- Cumulative artifact: `output/book-zh-progress.pdf`.
- Cumulative artifact SHA-256: `436a4744800ecfa2a79d0e59357cc22b7e51770aa7f60b9bb9c4cd0688c35bfd`.

Cumulative output pages 142--160 were rendered and visually inspected. No clipping, overflow, broken statement box, blank translated content page, or earlier-chapter layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 9 is complete for the supplied source and may be committed locally. The absent Bibliography and Index do not block the supplied front matter.
