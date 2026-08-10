# Front matter translation and regression report

## Scope

- Unit: title page, contents, preface, and preliminaries.
- Source range: PDF 1--12 / roman pages.
- Canonical TeX: `tex/main.tex` and `tex/frontmatter.tex`.
- Reviewed page metadata: `structured/reviewed/frontmatter.jsonl` and `translation/reviewed/frontmatter.jsonl`.

## Extraction and structure

- Source page containers: 12.
- Visually confirmed source-blank pages: PDF 2, 6, and 10.
- Conservative raw blocks retained: 114.
- Structure-review records: 63.
- Hidden-text formula candidates retained: 4.
- Canonical reviewed display formulas: 8; none is numbered in the source.
- The generated Chinese contents contains the supplied chapter and section entries. Its two output pages share the stable source-contents anchor for PDF 3--5.

## Cross-references

- Semantic labels: 2, both unique.
- Determinable LaTeX reference commands: 8.
- Undefined cumulative-project references after final compilation: 0.
- Duplicate labels or duplicate PDF destinations: 0.
- Equation/non-equation command mismatches: 0.
- Explicit unresolved source citations: 1, Rudin `[14]`; its target was not guessed because the bibliography is absent.
- Detailed ledger: `qa/translation/frontmatter-cross-reference-registry.tsv`.

No accepted Chapter 1--9 translation file changed in this batch.

## Language and names

- Forbidden full-width punctuation in front-matter Chinese prose: 0.
- Registered exact name forms in this source range: 8.
- Exact canonical name forms found: 8.
- Missing or altered registered names: 0.
- New name entries remain `needs-review`.

## Clean compilation

- Build directory: `workspace/temporary/fullbook-final-regression-20260810-1`.
- Engine: XeLaTeX (TeX Live 2025).
- Explicit passes: 3.
- Final cumulative PDF: 167 pages, 1049907 bytes.
- Undefined references, multiply-defined labels, duplicate destinations, rerun warnings, and overfull or underfull boxes: 0.
- Nonblocking runtime warnings: unavailable bold `stmaryrd` font shape falls back to its regular shape; math tokens in PDF bookmarks are omitted by `hyperref`.
- Cumulative artifact: `output/book-zh-progress.pdf`.
- Cumulative artifact SHA-256: `b376c39b7c9698443629d086a0b51173a05d09baccbc6f04a6e13aca57a31a33`.

Output pages 1--14 and 160--167 were rendered and visually inspected. The title, contents, source-blank separations, preface, preliminaries, Chapter 1 boundary, and final Chapter 9 pages show no clipping, overflow, broken statement box, or accidental content loss.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- `input/template/reference/main.tex`: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- `input/source/GSM029 - Fourier Analysis.pdf`: SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Accepted Chapter 2 sample SHA-256: `2963a64bc838c519e60b35b0316959cc19ef9b03cb00cba5c16b734590412e13`; unchanged from Git.
- Unit tests: 22 passed.

## Result

Pass. Every supplied front-matter page has been translated, represented as a source blank, or mapped to the generated contents. Source-complete finalization remains blocked only by the absent Bibliography and Index.
