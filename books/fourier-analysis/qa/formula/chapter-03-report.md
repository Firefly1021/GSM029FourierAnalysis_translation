# Chapter 3 formula verification report

- Source range: PDF 61--80 / printed 49--68.
- Source pages visually inspected: 20.
- Reviewed translated display groups: 103.
- Numbered equations: 11, in the exact sequence (3.1)--(3.11).
- Numbered equation labels: 11 unique `eq:` labels.
- Reviewed registry: `formulae/chapter-03-reviewed-formulas.jsonl`.
- OCR candidate registry retained unchanged as extraction evidence: `formulae/chapter-03-formula-registry.jsonl`.

Every translated display was checked against the rendered source pages for subscripts, superscripts, signs, relations, convolution and transform notation, integration domains, summation ranges, norm indices, and delimiters. The OCR review queue remains preserved as raw extraction evidence and was not used as final mathematical LaTeX.

The example in §6.5 on PDF 77 / printed 65 prints `Hf(x)=log(|x^2-1|/x^2)`. This exact equality conflicts with the earlier `1/pi` normalization and direct evaluation under the stated convention. The translation preserves the supplied source; the inconsistency is recorded as `chapter3-source-l1-example-normalization-001` in `qa/issues.jsonl`.

## Result

Pass for faithful transcription of the supplied source. The source-level §6.5 normalization inconsistency remains explicitly flagged for review and was not silently repaired.
