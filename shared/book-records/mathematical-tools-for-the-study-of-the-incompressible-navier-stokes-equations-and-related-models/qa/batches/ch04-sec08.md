# Batch QA: ch04-sec08

- Source scope: Section 8 from its heading on PDF page 335 through the end of Theorem IV.8.2 on PDF page 340. The passed Section 7 conclusion above the heading on page 335 is excluded.
- Source coverage: passed. Six page records are in `qa/translation/ch04-sec08-source-coverage.tsv`; every statement, proof step, bullet, physical interpretation, and displayed relation is represented in source order.
- Structure: passed. Subsections 8.1--8.2, Theorems IV.8.1--IV.8.2, both proofs, all bullet points, and all intervening exposition were restored.
- Formula fidelity: passed. Equations (IV.91)--(IV.97) are recorded in `formulae/ch04-sec08-formula-registry.jsonl`; the unnumbered time-discrete model, domain decomposition, trace maps, all weak forms, commutators, factors, signs, spaces, indices, and interface terms were checked against source-page images.
- Cross-references: passed. There are 12 unique batch labels and 24 resolved reference commands. The Chapter VI forward reference remains explicit and unresolved; duplicate labels, undefined targets, and equation/reference-command mismatches are zero. A visual-QA-discovered set of literal `eqref` strings was corrected before acceptance.
- Environment headings and numbering: passed. Theorem and Proof headings remain English. Theorem numbering is 8.1--8.2 and all numbered equations resolve to 4.91--4.97.
- Names and punctuation: passed. No personal name first occurs in this source range, prior exact forms are unchanged, and no forbidden full-width punctuation occurs in Chinese translated prose.
- Compilation: passed after clean-directory multi-pass XeLaTeX compilation and two final convergence passes after the last reference correction. Final log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0. The three sub-point overfull boxes are inherited from previously passed files; this batch adds none. The integrated PDF has 214 pages, 1472247 bytes, and SHA-256 `564e869b08fc8f6105c8642c985231f73584f5ec6d5f3ebf304e5fb2d478c7ea`.
- Visual QA: all integrated output pages 210--214 were rendered and inspected, with page 210 re-rendered after correcting the Theorem IV.2.3 target. English headings, theorem boxes, equation references, long systems, bullets, and final proof are legible; no clipping, overlap, broken box, or literal LaTeX command remains.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; style hash `8f2a2ea992fa2d43de675a0efe323ff9339d656158f7fe570f0c7f2da4c10555`; reference TeX hash `28ddd3a9e6c24423ce2a1046aeb07ff357f3be6b156778ce4a1496e25582bbd6`. All are unchanged.
- Source issues: five printed space, regularity, or symbol inconsistencies were preserved without silent correction and recorded as nonblocking warnings in `qa/issues.jsonl`.
- Blocking issues: none.
- Result: passed.
