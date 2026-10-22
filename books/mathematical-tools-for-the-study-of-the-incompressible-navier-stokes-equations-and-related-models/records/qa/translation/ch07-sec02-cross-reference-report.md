# ch07-sec02 cross-reference report

- Files checked: `tex/chapters/ch07-sec02.tex` and the integrated `tex/main.tex` build.
- Registry targets: 94 unique semantic targets.
- Resolved reference rows: 139.
- Explicit unresolved source-reference rows: 12.
- Formula labels: 69, corresponding to source equations (VII.21)--(VII.89).
- Formula reference command: every numbered formula reference uses `\eqref`.
- Theorem-like, chapter, section, subsection, and figure reference command: `\ref`.
- Duplicate labels: 0.
- Undefined ordinary references after three clean XeLaTeX passes: 0.
- Multiply-defined labels: 0.
- Wrong reference-command findings: 0.
- Figure targets: four, corresponding to source Figures VII.2--VII.5.
- Registry: `qa/translation/ch07-sec02-cross-reference-registry.tsv`.

## Explicit unresolved targets

- Twelve bibliography groups remain explicit: `[97,98]`, `[74]`, `[75]`, `[13,103]`, `[34]`, `[9,11,31,35,36]`, `[9,28,29,30,75]`, `[20,81]`, `[10]`, `[35,37]`, `[32]`, and `[38]`.
- No unresolved target was guessed or replaced by a hard-coded number.

## Result

Pass for all determinate targets. Explicit unresolved bibliography references are nonblocking and recorded in `qa/issues.jsonl`.
