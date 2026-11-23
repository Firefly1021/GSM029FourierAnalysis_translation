# Batch QA: ch02-sec01

- Source scope: PDF pages 61-63, ending immediately before Chapter II, Section 2.
- Fidelity: passed after a fresh page-by-page review. All 19 source blocks are mapped in `qa/translation/ch02-sec01-source-coverage.tsv`.
- Corrective finding: the first case of source equation (II.1) is `x\in\overline{\Omega}`. The prior translation incorrectly used `x\in\Omega`; the source domain and the preceding sentence have been restored without altering the source convention.
- Structure: passed; Chapter II introduction, Section 1 heading, six function-space conventions, zero extension, and signed distance are present in source order.
- Formula fidelity: passed; the multi-index derivative, Lipschitz seminorm, zero extension, and source equation (II.1) were checked against rendered source pages.
- Cross-references: passed. Section 2-6 targets use `\ref` with existing semantic labels. Two bibliography groups remain explicitly deferred in `qa/translation/ch02-sec01-cross-reference-registry.tsv`; no bibliography key was guessed.
- Names: passed; six names first occurring in this range were found byte-for-byte in the TeX source, with LaTeX double hyphens used to render source en dashes where applicable.
- Chinese-prose punctuation: passed; zero forbidden full-width punctuation occurrences.
- Deterministic LaTeX QA: passed; 480 labels, 261 references, zero duplicate labels, zero undefined labels, zero wrong reference commands, and zero translated environment-reference prefixes.
- Integrated compilation: passed in two explicit latexmk/XeLaTeX invocations from a clean short-path build directory. The native log contains zero LaTeX errors, zero undefined-reference warnings, and zero multiply-defined-label warnings.
- Visual QA: passed for translated pages 27-28; overlines in the zero extension and equation (2.1) render correctly.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; both unchanged.
- Blocking issues: none for this unit. Deferred bibliography keys are non-blocking and remain registered.
- Result: passed.

This result applies only to `ch02-sec01`. It does not restore acceptance of the remaining Phase 2 units.
