# Chapter 1 cross-reference report

- Unique Chapter 1 labels: 104.
- Duplicate labels: 0.
- Reference occurrences registered: 124.
- Direct `\ref` or `\eqref` occurrences: 122.
- Resolved direct reference occurrences: 122.
- Semantic unresolved occurrences: 2.
- Missing direct reference targets: 0.
- Formula references using `\ref` instead of `\eqref`: 0.
- PDF link annotations: 122.
- Registry: `qa/translation/chapter-01-cross-reference-registry.tsv`.

The two unresolved occurrences share the target `chap:ch04-polynomial-approximation`, because source Chapter 4 is not yet translated. Both use `\MBUnresolvedReference` and are recorded in `qa/issues.jsonl`; no destination was guessed.

The auxiliary-file number audit reproduces the source sequences `1.1.1`--`1.1.13`, `1.2.1`--`1.2.7`, `1.3.1`--`1.3.7`, `1.4.1`--`1.4.8`, `1.5.1`, `1.6.1`--`1.6.8`, `1.7.1`--`1.7.6`, and exercises `1.x.1`--`1.x.44`.

Result: passed with one nonblocking external target recorded at two locations.
