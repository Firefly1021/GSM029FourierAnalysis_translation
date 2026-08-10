# Chapter 0 cross-reference report

- Unique labels: 76.
- Duplicate labels: 0.
- Reference occurrences registered: 120.
- Resolved local reference occurrences: 116.
- Semantic unresolved targets: 4.
- Missing direct `\ref` or `\eqref` targets: 0.
- Formula references using `\ref` instead of `\eqref`: 0.
- PDF link annotations: 117.
- Registry: `qa/translation/chapter-00-cross-reference-registry.tsv`.

The four unresolved targets are the source inconsistency called `Theorem 0.2.3`, later Chapter 1, later Chapter 4 and later Section 2.1. They use `\MBUnresolvedReference` and are recorded in `qa/issues.jsonl`; no target was guessed.

The auxiliary-file number audit reproduced all sampled source numbers, including theorem `0.1.4`, theorem `0.2.2`, theorem `0.3.3`, the sequence `0.4.1`--`0.4.8`, theorem `0.7.2`, theorem `0.9.7`, and both source occurrences of equation `0.8.3`.

Result: passed with four nonblocking unresolved targets.

