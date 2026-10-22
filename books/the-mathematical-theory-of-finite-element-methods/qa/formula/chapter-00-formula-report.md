# Chapter 0 formula report

- Explicit stable formula IDs: 115.
- Unique formula IDs: 115.
- Numbered equation labels: 31.
- Duplicate LaTeX labels: 0.
- Subscripts, superscripts, signs, delimiters, summation ranges and integration domains were compared with the 22 rendered source pages.
- Registry: `formulae/chapter-00-formula-registry.jsonl`.

Source anomaly retained: PDF page 29 prints equation number `0.8.3` twice. The two objects have distinct semantic labels, while their rendered source numbers remain `0.8.3`. This is recorded as `chapter-00-source-duplicate-equation-0-8-3` in `qa/issues.jsonl`.

Result: passed with one nonblocking source anomaly.

