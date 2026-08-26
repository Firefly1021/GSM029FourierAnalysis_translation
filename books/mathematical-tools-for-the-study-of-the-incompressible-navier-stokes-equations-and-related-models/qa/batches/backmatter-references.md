# Batch QA: backmatter-references

- Source scope: complete References list from PDF pages 527--532 (printed pages 517--522).
- Source coverage and structure: passed. All 127 entries are present exactly once and remain in source order; the six source-page ranges are recorded in `qa/translation/backmatter-references-source-coverage.tsv`.
- Fidelity: passed by page-by-page comparison. Bibliographic languages, author forms, initials, accents, titles, publication facts, mathematical notation, source URLs, and visible source irregularities are preserved; line-end word division from PDF layout was removed without rewriting content.
- Cross-reference registry: passed. The References target and all 127 stable `bib:source-N` bibliography keys are registered; there are no duplicate or undefined labels and no incorrect reference commands.
- Names and punctuation: passed. Bibliography data is protected from Chinese-prose punctuation rewriting, and natural-person names are not translated, transliterated, reordered, expanded, or normalized.
- Compilation and visual QA: passed in a clean three-pass integrated XeLaTeX build. Output pages 350--358 were inspected and are legible, with no clipping, overlap, or broken entries. The integrated PDF has 358 pages, 2270475 bytes, and SHA-256 `8313650566c0bbf20c86bf0183dcf8657fe127769af271d32f2b8a07c9658f10`.
- Deterministic QA: 41 chapter files, 1204 chapter labels, 1738 reference commands, and zero duplicate labels, undefined references, wrong reference commands, translated environment prefixes, or punctuation violations. The top-level backmatter registry adds one References label and 127 bibliography keys.
- Integrity: source SHA-256 `dd2f1acd5d258334ad45aada857d5699d0a13daa553b89fd839ecab469c465e1`; template manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`; user template files unchanged.
- Blocking issues: none. Result: passed.
