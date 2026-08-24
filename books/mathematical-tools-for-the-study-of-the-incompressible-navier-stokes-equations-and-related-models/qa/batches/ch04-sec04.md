# Batch QA: ch04-sec04

- Source scope: Section 4 from PDF page 264 through its conclusion at the top of PDF page 285, Chapter IV, the complete curl-operator and related-spaces section.
- Source coverage: passed. Twenty-two page records are in `qa/translation/ch04-sec04-source-coverage.tsv`; the proof ending on PDF page 285 is included, while Section 5 material on that page is reserved for the next unit.
- Structure: passed. Subsections 4.1--4.4, Lemmas IV.4.1--IV.4.3, Definition IV.4.4, Proposition IV.4.5, Lemma IV.4.6, Theorems IV.4.7--IV.4.9, Lemma IV.4.10, Theorems IV.4.11--IV.4.13, Remarks IV.4.1--IV.4.2, Figure IV.1, all proofs, and all intervening exposition were restored in source order.
- Formula fidelity: passed. Equations (IV.12)--(IV.30) are recorded in `formulae/ch04-sec04-formula-registry.jsonl`; all unnumbered displays, differential operators, traces, domains, subscripts, superscripts, signs, and compatibility conditions were checked against the source.
- Cross-references: passed. There are 40 unique labels, 99 resolved reference commands, and 11 explicitly deferred appendix, later-section, later-chapter, or bibliography targets; duplicate and undefined targets are zero.
- Environment headings and numbering: passed. English headings are preserved, statement numbering runs from 4.1 through 4.13, Remarks run from 4.1 through 4.2, and the exact source Figure IV.1 is labelled and referenced.
- Names and punctuation: passed. Previously registered source names remain unchanged, including `Poincaré`, `Stokes`, `Leray`, `Neumann`, `Laplace`, `Young`, and `Navier--Stokes`; no forbidden full-width punctuation was found.
- Compilation: passed in a new clean build directory with `latexmk` followed by two explicit XeLaTeX convergence passes. Final log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0. The integrated PDF has 170 pages and SHA-256 `0014e890df0536f215578890f11c7cdce3c3aff269ae9e62089aa7048c68f55c`.
- Visual QA: output pages 153--170 were rendered and inspected. Theorem boxes, long proofs, displays, page breaks, and Figure IV.1 are legible; no clipping, overlap, broken box, literal LaTeX spacing command, or incorrect figure number remains.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; style hash `8f2a2ea992fa2d43de675a0efe323ff9339d656158f7fe570f0c7f2da4c10555`; reference TeX hash `28ddd3a9e6c24423ce2a1046aeb07ff357f3be6b156778ce4a1496e25582bbd6`. All are unchanged.
- Source issues: five printed notation/dimension/index inconsistencies were preserved without silent correction and recorded in `qa/issues.jsonl` as nonblocking warnings.
- Blocking issues: none.
- Result: passed.
