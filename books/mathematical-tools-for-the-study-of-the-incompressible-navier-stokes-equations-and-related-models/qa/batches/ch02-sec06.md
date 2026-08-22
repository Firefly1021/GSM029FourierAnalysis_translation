# Batch QA: ch02-sec06

- Source scope: PDF pages 122-132, from the Section 6 heading through Remark II.6.4 immediately before Chapter III.
- Fidelity: passed after a fresh page-by-page comparison. All source pages and their translation targets are recorded in `qa/translation/ch02-sec06-source-coverage.tsv`.
- Corrective work: the finite-to-infinite-dimensional motivation, unbounded-operator data, complete proof of Remark II.6.1, adjoint extension and uniqueness, graph-norm motivation, compact-inverse setup, complete proofs of Theorem II.6.6 and Proposition II.6.7, power-operator motivation, the complete finite-cover proof of Proposition II.6.8, negative-power construction, and both semigroup proofs were restored. No proof remains as a summary.
- Source anomaly: the source indexes the spectral basis by `k>=1` but writes `k>=0` at two proof points. Those occurrences are retained and explicitly identified; they were not silently normalized.
- Formula fidelity: passed. Source-numbered formulae (II.29)--(II.35) are registered in `formulae/ch02-sec06-formula-registry.jsonl` and resolve as 2.29--2.35.
- Cross-references: passed. Twenty source references, remarks, and citations are recorded in `qa/translation/ch02-sec06-cross-reference-registry.tsv`; known formula targets use `\eqref`, known theorem-like targets use `\ref`, and unavailable bibliography or future-chapter targets remain explicitly deferred.
- Environment headings: passed. `Theorem`, `Definition`, `Proposition`, `Proof`, and `Remark` remain English. Named theorem arguments use the adapter's brace form and render in English parentheses. Objects II.6.1--II.6.12 resolve to unique semantic labels; Remarks II.6.1--II.6.4 use a separate referenceable counter and do not disturb the shared theorem counter.
- Names: passed. `Hilbert`, `Sobolev`, `Stokes`, `Laplace`, `Cauchy`, `Riesz`, and `Duhamel` preserve their exact source forms.
- Chinese-prose punctuation: passed; zero forbidden full-width punctuation occurrences.
- Regression tests: passed; all 32 repository unit tests succeeded.
- Deterministic LaTeX QA: passed; 488 labels, 305 references, zero duplicate labels, zero undefined labels, zero wrong reference commands, and zero translated environment-reference prefixes.
- Integrated compilation: passed in three XeLaTeX invocations from the clean build directory `workspace/temporary/build-fidelity-ch02-sec06-clean1`. The native log contains zero LaTeX errors, zero undefined-reference warnings, and zero multiply-defined-label warnings.
- Output artifact: `workspace/temporary/build-fidelity-ch02-sec06-clean1/main.pdf`, 794479 bytes, SHA-256 `424fa3e032190b0c8affb6c4a2dcd4d3c9a1d3d1248a210cd512234869fc219a`.
- Visual QA: passed for integrated PDF pages 69-77, including both the preceding Section 5 boundary and the Chapter III boundary. Long theorem boxes, multi-line spectral expansions, equations (2.29)--(2.35), proof endings, and page breaks render without clipping or overlap.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; both unchanged.
- Blocking issues: none for this unit. Deferred bibliography and future-chapter targets are non-blocking and are never assigned fabricated numbers.
- Result: passed.

This result applies only to `ch02-sec06`. It does not restore acceptance of later Phase 2 units.
