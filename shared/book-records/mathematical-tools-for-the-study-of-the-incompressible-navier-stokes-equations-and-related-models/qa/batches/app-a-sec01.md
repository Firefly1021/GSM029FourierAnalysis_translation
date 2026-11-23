# Batch QA: app-a-sec01

- Source scope: Appendix A opening and complete Section 1 from PDF page 517 through the Section 1 conclusion on the upper part of PDF page 519. Section 2 begins later on PDF page 519 and is excluded.
- Source coverage: passed. Three page records are in `qa/translation/app-a-sec01-source-coverage.tsv`; every source paragraph, definition item, proposition statement, display, and concluding sentence in the natural unit is represented in source order.
- Structure: passed. Appendix A, Section 1, Subsections 1.1--1.2, Definition A.1.1, Proposition A.1.2, and the complete formula list were restored. The progress boundary was corrected from PDF page 518 to the actual Section 1 endpoint on PDF page 519.
- Formula fidelity: passed. Equations (A.1)--(A.9) are recorded as reviewed in `formulae/app-a-sec01-formula-registry.jsonl`. All numbered and unnumbered displays retain the printed variables, derivatives, factors, products, signs, and order without normalization.
- Cross-references: passed. Sixteen unique batch labels are defined, including nine equation labels. Duplicate labels, undefined ordinary targets, multiply-defined labels, and wrong reference commands are zero.
- Source anomaly: passed without silent correction. The printed cylindrical-coordinate curl formula omits the standard factor `1/r` before its first angular derivative; the source form is preserved and registered as a nonblocking warning in `qa/issues.jsonl`.
- Environment headings and numbering: passed. Definition A.1.1 and Proposition A.1.2 use English headings and stable semantic labels.
- Names and punctuation: passed. No personal names occur in the natural unit, and no forbidden full-width punctuation occurs in Chinese translated prose.
- Compilation: passed after a clean-directory three-pass XeLaTeX build. Final native-log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0. Three sub-point overfull boxes are inherited from previously passed files and this batch adds none. The integrated PDF has 344 pages, 2212226 bytes, and SHA-256 `97d25557a030b2328085d90c9f86aa3905bafbc26361b6f7f01b773c6d8602d4`.
- Visual QA: integrated output pages 343--344 containing the batch were rendered and inspected. Headings, English environment names, matrices, cylindrical-coordinate identities, and equations (A.1)--(A.9) are legible; no clipping, overlap, broken line, or literal LaTeX command remains.
- Deterministic QA: 36 project files, 1183 labels, 1731 reference commands, zero duplicate labels, zero undefined references, zero wrong reference commands, zero translated environment-reference prefixes, and zero punctuation violations. All 34 tests pass.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; style hash `8f2a2ea992fa2d43de675a0efe323ff9339d656158f7fe570f0c7f2da4c10555`; reference TeX hash `28ddd3a9e6c24423ce2a1046aeb07ff357f3be6b156778ce4a1496e25582bbd6`.
- Blocking issues: none.
- Result: passed.
