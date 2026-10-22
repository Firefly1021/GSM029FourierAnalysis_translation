# Batch QA: ch04-sec09

- Source scope: Section 9 from PDF page 341 through the end of Chapter IV on PDF page 355.
- Source coverage: passed. Fifteen page records are in `qa/translation/ch04-sec09-source-coverage.tsv`; every definition, statement, proof step, remark, bullet, and displayed relation is represented in source order.
- Structure: passed. Subsections 9.1--9.3, Definition IV.9.1, Lemmas IV.9.2, IV.9.4, and IV.9.7, Proposition IV.9.3 and IV.9.9, Theorems IV.9.5, IV.9.6, IV.9.8, and IV.9.10, all proofs, and Remarks IV.9.1--IV.9.5 were restored.
- Formula fidelity: passed. Equations (IV.98)--(IV.115) are recorded in `formulae/ch04-sec09-formula-registry.jsonl`; systems, weak traces, cutoff identities, boundary limits, commutators, signs, exponents, spaces, and indices were checked against all source-page images.
- Cross-references: passed. There are 37 unique batch labels and 81 resolved reference commands. Source references (I.37) and (A.9) remain explicit and unresolved; duplicate labels, undefined targets, and equation/reference-command mismatches are zero.
- Environment headings and numbering: passed. Definition, Lemma, Proposition, Theorem, Proof, and Remark headings remain English. Object numbering is 9.1--9.10 and numbered equations resolve to 4.98--4.115.
- Names and punctuation: passed. Banach, Steinhaus, Hardy, Jensen, Galerkin, de Rham, and Lax--Milgram preserve registered source forms; no new personal-name record is needed and no forbidden full-width punctuation occurs in Chinese translated prose.
- Compilation: passed after clean-directory three-pass XeLaTeX compilation. Final log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0. The three sub-point overfull boxes are inherited from previously passed files; this batch adds none. The integrated PDF has 226 pages, 1525755 bytes, and SHA-256 `6d61cfa6d02291ee9a87602734b593e653bfc5e63e2378af8221eea6635211ec`.
- Visual QA: all integrated output pages 214--226 were rendered and inspected. English headings, theorem boxes, equations (IV.98)--(IV.115), long commutator formulas, weak boundary traces, bullets, and final proof are legible; no clipping, overlap, broken box, or literal LaTeX command appears.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; style hash `8f2a2ea992fa2d43de675a0efe323ff9339d656158f7fe570f0c7f2da4c10555`; reference TeX hash `28ddd3a9e6c24423ce2a1046aeb07ff357f3be6b156778ce4a1496e25582bbd6`. All are unchanged.
- Source issues: nine printed reference, symbol, dimension, or variable inconsistencies were preserved without silent correction and recorded as nonblocking warnings in `qa/issues.jsonl`.
- Blocking issues: none.
- Result: passed.
