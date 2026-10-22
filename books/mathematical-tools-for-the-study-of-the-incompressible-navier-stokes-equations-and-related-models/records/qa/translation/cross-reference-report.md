# Cross-reference report

| Source object or reference | Target | Semantic LaTeX label | Sample location | Status |
|---|---|---|---|---|
| Chapter I | The equations of fluid mechanics | `chap:fluid-mechanics-equations` | `tex/chapters/ch01-sec01.tex` | Defined |
| Section I.2 | The transport theorem | `sec:chap1-transport-theorem` | `tex/chapters/sample.tex` | Defined |
| Theorem I.2.1 | Transport theorem | `thm:chap1-transport` | `tex/chapters/sample.tex` | Defined and referenced with English prefix `Theorem` |
| Formula (I.6) | Chain-rule identity | `eq:chap1-transport-chain-rule` | `tex/chapters/sample.tex` | Defined and referenced with `\eqref` |
| Remark I.2.1 | Vector generalisation | `rem:chap1-transport-vector` | `tex/chapters/sample.tex` | Defined |
| Formula (I.2) | Earlier velocity definition | `eq:chap1-velocity-definition` | `tex/chapters/ch01-sec01.tex` | Defined; sample reference resolved with `\eqref` |
| Formula (I.3) | Earlier equivalent velocity relation | `eq:chap1-velocity-lagrangian` | `tex/chapters/ch01-sec01.tex` | Defined; sample reference resolved with `\eqref` |
| Appendix A | Definition of `div(F\otimes v)` | `app:vector-operator-identities` | Outside sample | Known target, deferred; no number fabricated |

- Duplicate labels: 0.
- Undefined compiled references: 0.
- Wrong reference commands: 0.
- Verified integrated numbering and destinations after adding Section I.1; all live references resolve to their labelled objects.
- Result: Passed.
