# Batch QA: ch04-sec01

- Source scope: PDF pages 241-252, Chapter IV introduction, convention, and Section 1, the complete Nečas inequality section.
- Source coverage: passed. Twelve source-page records are in `qa/translation/ch04-sec01-source-coverage.tsv`; no source page, statement, proof step, displayed relation, or numbered equation in the scope was omitted.
- Structure: passed. The chapter opening, convention, subsections, Theorem IV.1.1, Propositions IV.1.2 and IV.1.5--IV.1.7, Lemmas IV.1.3--IV.1.4 and IV.1.9, Definition IV.1.8, remarks, and proofs were restored in source order.
- Formula fidelity: passed. Equations (IV.1)--(IV.8) are recorded in `formulae/ch04-sec01-formula-registry.jsonl` with reviewed source-page locations and stable semantic labels.
- Cross-references: passed. There are 27 unique labels, 46 resolved references, and 13 explicitly deferred references; duplicate and undefined targets are zero. The unavailable Chapter III Section 1.2.1 target is explicitly deferred rather than guessed.
- Environment headings and numbering: passed. English environment headings are preserved, and statement numbering runs from 1.1 through 1.9 with a separate remark sequence.
- Names and punctuation: passed. `de Rham`, `Leray`, `Hodge`, `Helmholtz`, `Galerkin`, and `Nečas` retain source spelling; no forbidden full-width punctuation was found in translated prose.
- Compilation: passed in a new clean build directory with `latexmk` followed by two explicit XeLaTeX convergence passes. Final log counts: undefined references 0, multiply-defined labels 0, rerun requests 0, LaTeX errors 0.
- Visual QA: output pages 135-143 were inspected. The chapter begins on a new page, and no clipping, overlap, broken environment box, or unreadable formula was found.
- Integrity: source PDF, original style file, reference TeX, and complete template manifest hashes remain unchanged.
- Source issue: the source-domain symbol in Lemma IV.1.3 is preserved and recorded as a nonblocking warning in `qa/issues.jsonl`; no silent correction was made.
- Blocking issues: none.
- Result: passed.
