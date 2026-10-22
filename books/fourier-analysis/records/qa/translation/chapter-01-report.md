# Chapter 1 translation and regression report

## Scope

- Unit: Chapter 1, *Fourier Series and Integrals*.
- Source range: PDF 13--36 / printed 1--24.
- Content pages: PDF 13--35; PDF 36 is blank.
- Canonical TeX: `tex/chapters/chapter-01.tex` and `tex/chapters/chapter-01/`.
- Reviewed page metadata: `structured/reviewed/chapter-01.jsonl` and `translation/reviewed/chapter-01.jsonl`.

## Extraction and structure

- Source page containers: 24.
- Conservative source blocks retained: 280.
- Translation anchors: one for each nonblank source page.
- Statement environments: 23, numbered consecutively as 1.1--1.23.
- Display groups: 137; 31 are numbered equations 1.1--1.31.

## Cross-references

- Semantic labels: 73, all unique.
- Determinable LaTeX reference commands: 60.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate destinations: 0.
- Equation/non-equation command mismatches: 0.
- Hard-coded equation, theorem, chapter, section, figure, or table numbers in translated Chapter 1 prose: 0.
- Explicit unresolved forward or bibliographic references: 21; all remain `\MBUnresolvedReference` entries and none was guessed.
- Detailed ledger: `qa/translation/chapter-01-cross-reference-registry.tsv`.

The accepted Chapter 2 sample received reference-only maintenance: its references to equations (1.24), (1.30), (1.31), Chapter 1 §9, and Chapter 1 now resolve to the corresponding Chapter 1 labels. No sample translation wording was changed.

## Language and names

- Forbidden full-width punctuation in Chapter 1 Chinese prose: 0.
- Registered names first occurring in this source range: 39.
- Exact canonical name forms found: 39.
- Missing or altered registered names: 0.
- Chapter 1 terminology additions remain `needs-review`; none was silently marked approved.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch1-regression-20260805-4`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3; the third pass was added because the second requested another rerun.
- Final PDF: 31 pages, 348498 bytes.
- Final pass undefined references: 0.
- Final pass multiply-defined labels: 0.
- Final pass duplicate destinations: 0.
- Final pass rerun warnings: 0.
- Nonblocking template/runtime warning: bold `stmaryrd` font shape falls back to its regular shape.
- Cumulative artifact: `output/book-zh-progress.pdf`.

All 31 rendered pages were visually inspected, including all Chapter 1 pages and the accepted Chapter 2 sample. No clipping, overflow, broken statement box, blank translated content page, or sample-layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 1 is complete for the supplied source and may be committed locally. The missing Bibliography and Index source pages remain a project-level completion blocker but do not block the next supplied chapter batch.

