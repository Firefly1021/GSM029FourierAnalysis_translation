# First-book pre-migration baseline

## Identity and scope

- Book: *Fourier Analysis*.
- Planned stable book ID: `fourier-analysis`.
- Completed-state commit: `943e53f63453d4ff93ab94ec98b3edf05ca8745f`.
- Supplied source: 228 PDF pages, covering front matter and Chapters 1--9.
- Source-complete limitation: the announced Bibliography and Index pages are absent from the supplied source. This is an existing source limitation, not a migration failure.

## Clean build

- Fresh build directory: `workspace/temporary/migration-baseline-20260810-1`.
- Engine: XeLaTeX through TeX Live 2025 and `latexmk`.
- Result: success, 167 pages.
- Undefined references: 0.
- Multiply-defined LaTeX labels: 0.
- LaTeX errors: 0.
- Final-pass rerun warnings: 0.
- Overfull or underfull boxes: 0.
- Existing driver warning: `xdvipdfmx` reported duplicate PDF object `equation.9.7` twice. No duplicate `\\label` or unresolved LaTeX reference accompanies this warning. It is recorded without changing accepted translation content.

## Content and QA baseline

- Canonical final TeX files: 66.
- Semantic labels: 511, all unique.
- Reference commands: 777, all targets defined.
- Formula-reference command mismatches: 0.
- Forbidden full-width punctuation in translated Chinese prose: 0.
- Proper-name control rows: 270. Existing chapter reports remain the authoritative location-by-location name verification evidence.
- Terminology rows: 122, all retained with their existing `needs-review` status; no contradictory translation was found for the same source term, domain, and context key.
- Existing unit tests: 22 passed.

## Integrity anchors

- Source PDF SHA-256: `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- User style SHA-256: `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- User reference TeX SHA-256: `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- Template bibliography asset SHA-256: `89b952edcb3192ec7eaa210bd962c3d4fae05f885b525a2ab61257669b41a25f`.
- Accepted sample SHA-256: `2963a64bc838c519e60b35b0316959cc19ef9b03cb00cba5c16b734590412e13`.
- Existing final PDF: `output/book-zh-progress.pdf`, 1,049,907 bytes, 167 pages, SHA-256 `b376c39b7c9698443629d086a0b51173a05d09baccbc6f04a6e13aca57a31a33`.
- Fresh baseline PDF: `workspace/temporary/migration-baseline-20260810-1/main.pdf`, 1,049,916 bytes, 167 pages, SHA-256 `c64e1f3acdb2780f587e3566486ef405911acf65b5dd29c6a3b20f4364e2bf23`.

The fresh PDF hash differs from the previously committed artifact by 9 bytes while page count, compilation diagnostics, labels, references, and canonical TeX inputs agree. The committed artifact remains the regression anchor; byte equality is not treated as the only correctness criterion.
