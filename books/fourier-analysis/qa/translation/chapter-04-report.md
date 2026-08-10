# Chapter 4 translation and regression report

## Scope

- Unit: Chapter 4, *Singular Integrals (I)*.
- Source range: PDF 81--102 / printed 69--90.
- Canonical TeX: `tex/chapters/chapter-04.tex` and `tex/chapters/chapter-04/`.
- Reviewed page metadata: `structured/reviewed/chapter-04.jsonl` and `translation/reviewed/chapter-04.jsonl`.

## Extraction and structure

- Source page containers: 22.
- Conservative raw blocks retained: 221.
- Translation anchors: one for each source page.
- Statement environments: 20, numbered consecutively as 4.1--4.20.
- Display groups: 85; 27 are numbered equations 4.1--4.27.

## Cross-references

- Semantic labels: 62, all unique.
- Determinable LaTeX reference commands: 96.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved forward or bibliographic references: 12; all remain `\MBUnresolvedReference` entries and none was guessed.
- Detailed ledger: `qa/translation/chapter-04-cross-reference-registry.tsv`.

No accepted Chapter 1, Chapter 2, or Chapter 3 translation file changed in this batch. Chapter 4 begins on a fresh output page.

## Language and names

- Forbidden full-width punctuation in Chapter 4 Chinese prose: 0.
- Registered names first occurring in this source range: 22.
- Exact canonical name forms found: 22.
- Missing or altered registered names: 0.
- Chapter 4 terminology and name additions remain `needs-review`; none was silently marked approved.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch4-regression-20260805-2`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 68 pages, 566735 bytes.
- Final pass undefined references: 0.
- Final pass multiply-defined labels: 0.
- Final pass duplicate destinations: 0.
- Final pass rerun warnings: 0.
- Final pass overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape.
- Cumulative artifact: `output/book-zh-progress.pdf`.

The Chapter 3/4 boundary and every cumulative output page 53--68 were rendered and visually inspected. No clipping, overflow, broken statement box, blank translated content page, or earlier-chapter layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 4 is complete for the supplied source and may be committed locally. The missing Bibliography and Index source pages remain a project-level completion blocker but do not block Chapter 5.
