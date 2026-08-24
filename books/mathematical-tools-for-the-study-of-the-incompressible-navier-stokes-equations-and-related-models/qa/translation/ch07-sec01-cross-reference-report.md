# ch07-sec01 cross-reference report

- Files checked: `tex/chapters/ch07-sec01.tex` and the integrated `tex/main.tex` build.
- Batch labels: 37 unique semantic labels.
- Ordinary reference commands: 81.
- Explicit unresolved source references: 6.
- Formula labels: 20, corresponding to source equations (VII.1)--(VII.20).
- Formula reference command: every numbered formula reference uses `\eqref`.
- Theorem-like, chapter, section, subsection, and figure reference command: `\ref`.
- Duplicate labels: 0.
- Undefined ordinary references after three clean XeLaTeX passes: 0.
- Multiply-defined labels: 0.
- Wrong reference-command findings: 0.
- Figure target: `fig:chap7-truncated-physical-domain`, rendered as Figure VII.1.
- Registry: `qa/translation/ch07-sec01-cross-reference-registry.tsv`.

## Explicit unresolved targets

- Five bibliography keys occur in six source citations.
- The Chapter VII Section 2 forward target remains explicit until `ch07-sec02` is translated and labelled.
- No unresolved target was guessed or replaced by a hard-coded number.

## Result

Pass for all determinate targets. Explicit unresolved source references are nonblocking and recorded in `qa/issues.jsonl`.
