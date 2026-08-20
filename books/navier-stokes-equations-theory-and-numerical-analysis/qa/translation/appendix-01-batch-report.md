# Appendix I Batch QA Report

- Source range: PDF pages 326--335.
- Numbered formulas: 35.
- Unnumbered displays: 22.
- Unique semantic labels: 66.
- Reference commands: 53.
- Punctuation QA: PASS, 0 violations.
- Personal-name QA: PASS, 0 missing or duplicated records.
- Formula fidelity: the displayed formulas were compared with the rendered source pages. One initial transcription error in the unnumbered higher-order boundary derivative expansion was corrected before acceptance. One non-blocking source anomaly is recorded in `qa/issues.jsonl`; the printed form is preserved without silent correction.
- Compilation: PASS after two clean XeLaTeX runs.
- Undefined references: 0.
- Multiply-defined labels: 0.
- TeX errors: 0.
- Overfull boxes: 0.
- Visual QA: the first page, a middle lemma page, and the final page were inspected; no clipping or overlap was found.
- Output: `output/appendix-01.pdf`.
- Output SHA-256: `1136DE67D3F5041EE48C1EDB892DF889ADF40A15D20F259F82D1B85DAF7AF753`.

Result: PASS. The recorded source anomaly is non-blocking.
