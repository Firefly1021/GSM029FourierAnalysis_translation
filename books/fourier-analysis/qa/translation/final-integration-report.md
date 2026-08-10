# Final integration and supplied-source acceptance report

## Supplied-source coverage

- Supplied PDF: 228 pages.
- Translated content: front matter and Chapters 1--9.
- Visually confirmed blank interstitial pages: PDF 2, 6, 10, 36, and 60; no OCR content was invented for them.
- Chapter units that passed extraction, structure, formula, terminology, name, punctuation, cross-reference, compilation, and visual QA: 9 of 9.
- Front-matter unit: passed.
- Announced but unavailable source: Bibliography from printed page 217 and Index from printed page 219.

## Integrated reference and language audit

- Canonical TeX files scanned: 66.
- Semantic labels: 511, all unique and present in the final auxiliary file.
- LaTeX reference commands: 777.
- Undefined references: 0.
- Explicit unresolved unavailable-source references: 174; these are retained as QA markers rather than guessed.
- Forbidden full-width punctuation in canonical translated Chinese prose: 0.
- Accepted Chapter 1--9 translation files modified during front-matter integration: 0.

## Final clean build

- Build directory: `workspace/temporary/fullbook-final-regression-20260810-1`.
- Engine: XeLaTeX (TeX Live 2025).
- Passes: 3 from a clean directory.
- Output: `output/book-zh-progress.pdf`.
- Pages: 167.
- Bytes: 1049907.
- SHA-256: `b376c39b7c9698443629d086a0b51173a05d09baccbc6f04a6e13aca57a31a33`.
- Undefined references: 0.
- Multiply-defined labels: 0.
- Duplicate PDF destinations: 0.
- Rerun warnings after the final pass: 0.
- Overfull or underfull boxes: 0.
- LaTeX errors: 0.
- Unit tests: 22 passed.

All newly integrated front-matter pages, the Chapter 1 transition, and the final Chapter 9 pages were rendered and visually inspected. Earlier chapter-specific reports record the completed visual inspection for each accepted chapter.

## Read-only input integrity

- User style SHA-256: `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- User reference TeX SHA-256: `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- Supplied PDF SHA-256: `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- All three match their recorded baselines.

## Acceptance result

Pass for every page actually supplied in the PDF. A source-complete book cannot be declared finished because the Bibliography and Index announced by the contents are absent from the supplied source. No reconstruction was attempted.
