# Chapter 3 Section 8 Batch QA Report

- Source range: lower part of PDF page 302 through PDF page 324; PDF page 325 is blank.
- Numbered formulas: 138.
- Unnumbered displays: 59.
- Unique semantic labels: 176.
- Reference commands: 217.
- Problem numbering verified: 8.1--8.2.
- Remark numbering verified: 8.1--8.5.
- Lemma numbering verified: 8.1--8.9.
- Theorem numbering verified: 8.1--8.8.
- Punctuation QA: PASS, 0 violations.
- Personal-name QA: PASS, 0 missing or duplicated records.
- Formula fidelity: six non-blocking source anomalies are recorded in `qa/issues.jsonl`; all printed forms are preserved without silent correction.
- Compilation: PASS after repeated XeLaTeX/latexmk runs.
- Undefined references: 0.
- Multiply-defined labels: 0.
- TeX errors: 0.
- Overfull boxes: 0.
- Visual QA: the shared Section 7/8 boundary, a middle theorem page, and the final formula page were inspected; no clipping or overlap was found.
- Output: `output/chapter-03-section-08.pdf`.
- Output SHA-256: `39F2332AF246E0BCD49300285F10D9DCC804AE14F9262C69601F5EC4AFFAA032`.

Result: PASS. The recorded source anomalies are non-blocking.
