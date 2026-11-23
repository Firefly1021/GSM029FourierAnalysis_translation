# Representative sample QA

Status: awaiting-sample-approval. Agent sample QA passed; no human approval yet.

- Source: PDF 12--14, printed 2--4; 24 aligned blocks.
- Source type: scan with hidden, unreliable OCR, not reliable native text.
- English reconstruction: structured/reviewed/sample-restored-en.tex.
- Chinese source: tex/chapters/sample.tex; compiled sample: output/sample-zh.pdf.
- 16 displayed / 38 inline math regions; no low-confidence sample regions.
- Four English Theorem headings. No invented formal Proof or Example headings.
- Five numbered equations and four Theorem numbers checked in aux data.
- Six actual PDF links match their expected equation/Theorem anchors.
- Final clean build: three successful XeLaTeX passes; no undefined references,
  duplicate labels, missing glyphs or overfull boxes. See compile-report.json.
- All three output pages visually inspected, including cross-page Theorem 1.3.
- Nine book-local proposed terms; zero ambiguous unresolved terms. Global glossary unchanged.
- Original PDF and pinned/shared templates unchanged; pre-existing dirty files preserved.

Non-blocking warnings outside the sample remain in issues.jsonl. Review does not
claim all 444 pages have correct OCR or verified page-number mapping. No full
chapter translation or remote push was performed.

## User typography revision, 2026-11-15

Mathematical bold now uses bm rather than mathbf, as explicitly requested by
the user. Restored English, Chinese TeX, structured blocks and formula data are
aligned. This typography authorization is not sample approval. See
bm-revision-report.json for the restricted-change and rebuild checks.

## User typography revision: differential d and display style

The differential operator is upright via mathrm{d}. Formula bodies use
displaystyle, including the iterative integral equations, whose explicit
textstyle overrides were removed. Fractions in matrices and cases use dfrac.
Partial derivatives, variables, ranges, labels and mathematical content remain
unchanged. Restored English, translation and formula registries agree. A new
clean three-pass build and three-page visual inspection passed; see
d-display-revision-report.json. Sample approval remains pending.
