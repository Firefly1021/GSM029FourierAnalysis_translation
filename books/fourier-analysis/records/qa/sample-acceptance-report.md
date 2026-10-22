# Phase 2 sample acceptance report

## Scope and outcome

The current maintenance pass repaired cross-references, translated-prose punctuation, and theorem-like environments in the representative sample (PDF pages 37--51 / printed pages 25--39). No later chapter was translated. The repaired sample compiles and passes the requested regression checks, but full-book translation remains paused because the pre-existing source-completeness, formula-registry, structure, and terminology review queues remain open.

## Requested regression checks

| Check | Result | Evidence |
|---|---|---|
| Stable semantic labels | Pass | 39 unique labels: 10 structural, 16 theorem-like, 12 equation, and 1 chapter label |
| Local references | Pass | 31 local references; formulas use `\eqref`; statement/structural objects use `\ref` |
| Uncertain targets | Pass | 11 external targets are explicitly registered as unresolved; none was guessed |
| Hard-coded local numbering | Pass | No local formula, theorem-like, chapter, or section number is hard-coded in prose |
| Compilation | Pass | Clean build, two XeLaTeX passes, final 12-page PDF |
| Reference diagnostics | Pass | No undefined reference, multiply-defined label, or duplicate PDF destination |
| PDF link layer | Pass | 75 named destinations and 42 link annotations; includes all 12 equations and 16 theorem-like objects |
| Chinese-prose punctuation | Pass | 419 initial prose violations normalized; final protected-region-aware scan reports zero |
| Theorem environment | Pass | Inline title, no frame, `KuangNei` background, breakable box, number before optional name, referenceable counter |
| Related statement environments | Pass | Definition, Lemma, Proposition, Corollary, Example, Remark, and Exercise share stable reference behavior while retaining differing body/background treatment |
| Input integrity | Pass | Source PDF, source style, reference TeX, and reference bibliography hashes are unchanged |
| Automated tests | Pass | `python -m unittest discover -s tests -v`: 22 tests passed |

## Remaining project-level blockers

1. The supplied PDF ends on printed page 216 although its contents announce Bibliography at 217 and Index at 219.
2. The broader 73-item formula registry and inline-formula completeness still require token-level human review. Source equation (2.2) in this sample has now been visually transcribed, but that does not close the wider registry review.
3. 136 of 175 heuristic semantic child blocks remain low-confidence and are not approved as final translation units.
4. Terminology and proper-name candidates remain in review status.

## Reports

- `qa/translation/cross-reference-report.md`
- `qa/translation/cross-reference-registry.tsv`
- `qa/translation/punctuation-report.md`
- `qa/template/theorem-environment-report.md`

## Result

The user-requested maintenance checks pass. Translation of subsequent chapters remains paused.
