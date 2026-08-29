# Sample formula restoration report

- Sample range: PDF 37--55 / printed 23--41.
- Formula/math regions registered: 656.
- Display regions: 137.
- Inline regions: 519.
- High-confidence regions: 654.
- Medium-confidence regions: 2.
- Low-confidence regions: 0.
- Registry: `structured/formulae/sample-formula-registry.jsonl`.
- Formula crops: `workspace/crops/formula/sample-pages-037-055/`.

## Method

Ordinary OCR output was not accepted as final LaTeX. Formula tokens were checked against the original 360 DPI scan, formula-optimized derivatives, local notation, equation numbering, and book-internal repetition. No formula was simplified, rederived, or silently corrected.

## Review note

Two regions on PDF page 43 have medium confidence because a source-scan smudge touches the first energy-norm display. The reconstruction is supported by the same-page variational identity and neighboring notation, but the lower confidence is retained in QA. No low-confidence formula remains in the sample.
