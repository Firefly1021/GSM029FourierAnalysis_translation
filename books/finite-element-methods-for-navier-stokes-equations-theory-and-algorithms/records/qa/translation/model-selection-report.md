# Full-book draft model selection report

Status: no model is approved as a source of reviewed translation.

## Evaluated models

- Argos Translate English to Chinese 1.9: rejected. It mistranslates mathematical terms, translates protected environment headings, and emits full-width punctuation.
- Helsinki-NLP/opus-mt-en-zh: rejected. It mistranslates `mapping`, `equation`, and mathematical phrasing, and emits full-width punctuation.
- Qwen/Qwen2.5-1.5B-Instruct: rejected for unattended translation. After structural handling it preserves English environment headings and ASCII punctuation, but it can silently omit protected-term placeholders and transliterate protected names.
- facebook/nllb-200-distilled-600M: rejected. It preserves placeholders after controlled substitution, but mathematical terminology and sentence semantics remain inadequate, including `mapping` as `绘图` and an incomplete Sobolev-space sentence.
- Qwen/Qwen2.5-3B-Instruct: operational benchmark stopped. Six-sentence CPU inference caused sustained paging and did not finish within a practical diagnostic interval. No translation content was written from this run.

## Consequence

Machine output may be retained only as an explicitly unreviewed candidate when all protected tokens survive. It must never be promoted to reviewed translation without comparison against a QA-passed reconstructed English source. Low-confidence prose and every mathematical formula remain blocking until checked against the original scan.

The accepted representative sample remains unchanged and is not part of these experiments.
