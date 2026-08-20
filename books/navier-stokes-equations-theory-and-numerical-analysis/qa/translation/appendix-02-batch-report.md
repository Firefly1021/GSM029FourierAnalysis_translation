# Appendix II Batch QA Report

- Source range: PDF pages 336--351; PDF page 351 is blank.
- Numbered formulas: 13.
- Unnumbered displays: 46.
- Unique semantic labels: 34.
- Reference commands: 21.
- Source figures: eight numbered figures and five unnumbered diagram groups were cropped directly from the source rendering without redrawing.
- Punctuation QA: PASS, 0 violations.
- Personal-name QA: PASS, 0 missing or duplicated records.
- Formula fidelity: the displayed formulas were compared with the rendered source pages. One non-blocking source anomaly is recorded in `qa/issues.jsonl`; the printed forms are preserved without silent correction.
- Compilation: PASS after repeated XeLaTeX runs.
- Undefined references: 0.
- Multiply-defined labels: 0.
- TeX errors: 0.
- Overfull boxes: 0.
- Visual QA: the first page, the Uzawa algorithm page, and the final streamlines page were inspected; no clipping, overlap, or literal reference keys remain.
- Output: `output/appendix-02.pdf`.
- Output SHA-256: `B18C15E780ACE7ABEF33A1965A069DF71547E0031CAE683466DE87194FFF6A44`.

Result: PASS. The recorded source anomaly is non-blocking.
