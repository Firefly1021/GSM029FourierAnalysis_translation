# Chapter 8 translation and regression report

## Scope

- Unit: Chapter 8, *Littlewood--Paley Theory and Multipliers*.
- Source range: PDF 169--206 / printed 157--194.
- Canonical TeX: `tex/chapters/chapter-08.tex` and `tex/chapters/chapter-08/`.
- Reviewed page metadata: `structured/reviewed/chapter-08.jsonl` and `translation/reviewed/chapter-08.jsonl`.

## Extraction and structure

- Source page containers: 38.
- Conservative raw blocks retained: 440.
- Translation anchors: one for each source page.
- Statement environments: 38, numbered consecutively as 8.1--8.38.
- Display groups: 199; 29 are numbered equations 8.1--8.29.
- Hidden-text formula candidates routed through review: 133; canonical TeX displays were checked against rendered source pages.

## Cross-references

- Semantic labels: 84, all unique.
- Determinable LaTeX reference commands: 175.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved source citations: 2; neither was guessed because the supplied source has no bibliography.
- Detailed ledger: `qa/translation/chapter-08-cross-reference-registry.tsv`.

No accepted Chapter 1--7 translation file changed in this batch. Chapter 8 begins on a fresh output page.

## Language and names

- Forbidden full-width punctuation in Chapter 8 Chinese prose: 0.
- Registered names first occurring in this source range: 33.
- Exact canonical name forms found: 33.
- Missing or altered registered names: 0.
- New terminology and name entries remain `needs-review`.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch8-regression-20260807-2`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 142 pages, 949074 bytes.
- Undefined references, multiply-defined labels, duplicate destinations, rerun warnings, and overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape; pre-existing math-in-bookmark warnings remain nonfatal.
- Cumulative artifact: `output/book-zh-progress.pdf`.
- Cumulative artifact SHA-256: `c204cddd11db63ba61971996a8390902f8eb0989598cc6572d8bba5442e4462a`.

The Chapter 7/8 boundary and cumulative output pages 113--142 were rendered and visually inspected. No clipping, overflow, broken statement box, blank translated content page, or earlier-chapter layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 8 is complete for the supplied source and may be committed locally. The absent Bibliography and Index do not block Chapter 9.
