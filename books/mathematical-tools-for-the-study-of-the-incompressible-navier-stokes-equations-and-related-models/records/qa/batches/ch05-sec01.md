# Batch QA: ch05-sec01

- Source scope: Chapter V, Section 1 from PDF page 357 through PDF page 380.
- Source coverage: passed. Twenty-four page records are in `qa/translation/ch05-sec01-source-coverage.tsv`; every source statement, proof step, paragraph, bullet, and displayed relation is represented in source order.
- Structure: passed. Subsections 1.1--1.5, Lemmas V.1.1, V.1.2, V.1.5, and V.1.6, Proposition V.1.3 and V.1.7, Theorem V.1.4, all proofs, remarks, and the three-dimensional energy steps were restored.
- Formula fidelity: passed. Equations (V.1)--(V.31) are recorded in `formulae/ch05-sec01-formula-registry.jsonl`; operators, spaces, signs, exponents, limits, projections, integration ranges, and initial data were checked against the source-page images.
- Cross-references: passed for all determinate targets. There are 47 unique batch labels and 111 reference commands. The forward source reference to Subsection 2.3.2 and the printed `(IV.59)` citation remain explicit and unresolved; duplicate labels, undefined targets, and equation/reference-command mismatches are zero.
- Environment headings and numbering: passed. Lemma, Proposition, Theorem, Proof, and Remark headings remain English. The named result renders as `Theorem 1.4 (Leray)` and numbered equations resolve to 5.1--5.31.
- Names and punctuation: passed. Leray, Reynolds, Galerkin, Cauchy--Lipschitz, Hölder, Young, Gronwall, Banach, Lebesgue, Fatou, and de Rham retain source forms or established mathematical forms; no forbidden full-width punctuation occurs in Chinese translated prose.
- Compilation: passed after clean-directory three-pass XeLaTeX compilation. Final log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0. Three sub-point overfull boxes are inherited from previously passed files and this batch adds none. The integrated PDF has 243 pages, 1609445 bytes, and SHA-256 `bc5cf4604208dcf512b389eb47dcb4545c37cfccf339ae561b0c9d1b2940bcad`.
- Visual QA: all integrated output pages 227--243 were rendered and inspected. English headings, theorem boxes, equations (V.1)--(V.31), long energy estimates, the piecewise affine cutoff, and pressure-recovery argument are legible; no clipping, overlap, broken box, or literal LaTeX command appears.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; style hash `8f2a2ea992fa2d43de675a0efe323ff9339d656158f7fe570f0c7f2da4c10555`; reference TeX hash `28ddd3a9e6c24423ce2a1046aeb07ff357f3be6b156778ce4a1496e25582bbd6`. All are unchanged.
- Source issues: the printed `(IV.59)` pressure-proof citation has no reliable target in context. It was preserved without silent correction and recorded as a nonblocking warning in `qa/issues.jsonl`.
- Blocking issues: none.
- Result: passed.
