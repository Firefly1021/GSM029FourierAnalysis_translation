# Cross-reference review

Formula references use eqref; chapter, section and table references use ref. Every referenced object has a semantic label. Source references and Chinese line locations are recorded in cross-reference-registry.json.

| Outside target | Label | Verified source |
| --- | --- | --- |
| (1.1) | eq:linear-system | PDF 14 / printed 1 |
| Section 1.4 | sec:symmetric-direct-methods | PDF 22 / printed 9 |
| Chapter 3 | chap:krylov-classification | PDF 85 / printed 73 |

These targets resolve to an explicitly marked source-location appendix, containing the source equation or heading and links to the original PDF. The appendix does not claim those sections were translated. Full-book integration must replace the locators with actual translated chapter/section targets.

Equations (1.20)--(1.34) retain their source numbers. Statement headings follow the existing shared template counter, without changing its rule:

| Source | Label | Sample output |
| --- | --- | --- |
| Definition 1.2 | def:krylov-subspace | Definition 1.1 |
| Definition 1.3 | def:krylov-grade | Definition 1.2 |
| Proposition 1.1 | prop:projection-equivalences | Proposition 1.3 |
| Remark 1 | rem:scalar-residual-minimization | Remark 1.4 |

Proof remains an English Proof heading. The registry preserves original object numbers; they are not inferred from the sample's counter.

Compilation warnings and PDF internal-link checks are recorded separately.
