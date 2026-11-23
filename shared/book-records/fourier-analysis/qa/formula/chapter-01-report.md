# Chapter 1 formula verification report

- Source range: PDF 13--36 / printed 1--24; PDF 36 is blank.
- Source pages visually inspected: 24.
- Translated display groups: 137.
- Numbered equations: 31, in the exact sequence (1.1)--(1.31).
- Unnumbered display groups: 106.
- Numbered equation labels: 31 unique `eq:` labels.
- Reviewed registry: `formulae/chapter-01-reviewed-formulas.jsonl`.
- OCR candidate registry retained unchanged as extraction evidence: `formulae/chapter-01-formula-registry.jsonl`.

Every translated display was checked against the rendered source page for subscripts, superscripts, relations, signs, delimiters, and integration or summation domains. The normalized Hermite-function formula on PDF 34 / printed 22 received an additional enlarged visual check.

Theorem 1.22 contains a source-level index inconsistency: the source defines `M_0` and `M_1` but states the subsequent condition for `j=1,2`. The translation preserves the supplied source. This is recorded as `chapter1-source-theorem-1-22-index-001` in `qa/issues.jsonl`; no correction was guessed.

## Result

Pass for faithful transcription of the supplied source. The source-level Theorem 1.22 inconsistency remains explicitly flagged for review.

