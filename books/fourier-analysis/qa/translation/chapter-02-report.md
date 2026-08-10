# Chapter 2 translation and regression report

## Scope

- Unit: Chapter 2, *The Hardy--Littlewood Maximal Function*.
- Source range: PDF 37--59 / printed 25--47.
- Accepted baseline retained: PDF 37--51 / printed 25--39 in `tex/chapters/sample.tex`.
- Newly completed range: PDF 52--59 / printed 40--47 in `tex/chapters/chapter-02-tail.tex`.
- Chapter driver: `tex/chapters/chapter-02.tex`.
- Reviewed page metadata: `structured/reviewed/chapter-02.jsonl` and `translation/reviewed/chapter-02.jsonl`.

## Extraction and structure

- Newly completed source pages: 8.
- Conservative raw blocks retained for the new range: 115.
- Reviewed page containers for the new range: 8.
- New statement environments: 4, continuing the chapter sequence as 2.17--2.20.
- Cumulative Chapter 2 statement environments: 20, numbered 2.1--2.20.
- New reviewed display groups: 31; 5 are numbered equations 2.13--2.17.
- Cumulative numbered equations: 17, numbered 2.1--2.17.

## Cross-references

- Semantic labels in Chapter 2: 55, all unique.
- Determinable LaTeX reference commands in Chapter 2: 59.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved source citations or forward references: 9; all remain `\MBUnresolvedReference` entries and none was guessed.
- Detailed ledger: `qa/translation/chapter-02-cross-reference-registry.tsv`.

The only change to the accepted sample is reference-only maintenance: its former textual reference to Section 8.6 now uses `\ref{subsec:ch2-covering-lemmas}`. No accepted translation wording or styling was revised.

## Language and names

- Forbidden full-width punctuation in the accepted sample: 0.
- Forbidden full-width punctuation in the newly completed range: 0.
- Registered names first occurring in the new range: 35.
- Exact canonical name forms found: 35.
- Missing or altered registered names: 0.
- New terminology and name entries remain `needs-review`; none was silently marked approved.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-ch2-regression-20260805-2`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final PDF: 37 pages, 392538 bytes.
- Final pass undefined references: 0.
- Final pass multiply-defined labels: 0.
- Final pass duplicate destinations: 0.
- Final pass rerun warnings: 0.
- Final pass overfull or underfull boxes: 0.
- Nonblocking template/runtime warning: unavailable bold `stmaryrd` font shape falls back to its regular shape.
- Cumulative artifact: `output/book-zh-progress.pdf`.

All 37 rendered cumulative pages were visually inspected. The newly completed pages were additionally inspected at full rendered resolution. No clipping, overflow, broken statement box, blank translated content page, or accepted-sample layout regression was found.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Template manifest verification: passed.
- Unit tests: 22 passed.

## Result

Pass. Chapter 2 is complete for the supplied source and may be committed locally. The missing Bibliography and Index source pages remain a project-level completion blocker but do not block Chapter 3.
