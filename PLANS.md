# Phase 2 sample validation plan

## Objective

Diagnose the complete supplied PDF, establish a preliminary whole-book structure, and validate the workflow on one representative continuous sample of 15 pages. Do not translate the complete book.

## Implementation steps

1. Inventory read-only source files, hash them, and select the primary PDF with a recorded reason.
2. Inspect every page for text layer, extraction quality, scan/mixed state, rotation, size, images, fonts, columns, recurring matter, formula density, and anomalies.
3. Establish preliminary whole-book structural ranges and a table-of-contents outline.
4. Select a continuous representative sample based on observed document elements.
5. Preserve raw text and layout data; render and visually inspect the sample.
6. Build structured source blocks and record automatic repairs.
7. Register sample formula candidates with stable IDs and review metadata.
8. Extract unapproved terminology and exact-form personal-name candidates.
9. Produce draft and reviewed Chinese translations from structured source blocks only.
10. Generate sample LaTeX with the user template, compile it, render it, and inspect the result.
11. Run acceptance QA, recheck source hashes, and update project status.

## Current progress

- Phase 2 sample validation deliverables are complete.
- Cross-references, translated-prose punctuation, and theorem-like adapter environments have been repaired and regression-tested.
- Stopped before later-chapter/full-book translation because the remaining review queues are outside this maintenance pass.

## Completed validation

- Phase 1 rules, configuration, translation style, template reports, glossary controls, and reference TeX were read before source processing.
- The sole substantive PDF was selected without ambiguity and hashed.
- All 228 PDF pages were individually diagnosed.
- Title, contents, chapter openings, blank interstitial pages, and final page were visually checked.
- Preliminary front-matter and nine-chapter ranges were mapped.
- PDF pages 37--51 (printed pages 25--39) were selected as a continuous representative sample.
- All sample pages were rendered, visually inspected, and extracted to raw text, word layout, and structured-source layers.
- Display-formula candidates were assigned stable IDs and queued for manual review; OCR candidates were not accepted as final LaTeX.
- Terminology and exact-form name candidates were added with `needs-review` status only.
- Fifteen source page containers map one-to-one to fifteen draft and fifteen reviewed translation records.
- The repaired sample compiled through the unchanged user style plus the authorized adapter to a 12-page PDF; every output page was rendered and visually checked.
- Twenty-two unit tests passed and all source/template hashes remained unchanged.
- Thirty-nine stable semantic labels, thirty-one local reference commands, and eleven explicitly unresolved external references are recorded in the cross-reference registry.
- The final protected-region-aware punctuation scan reports zero forbidden full-width punctuation occurrences in translated Chinese prose.

## Issues found

- Blocking: the supplied file ends at printed page 216; the contents announce a Bibliography at 217 and an Index at 219.
- Blocking: hidden OCR substantially corrupts mathematical symbols; formula token-level verification is incomplete.
- Major: heuristic source structure contains low-confidence blocks requiring manual review.
- Resolved in this maintenance pass: source equation (2.2) was visually transcribed and labeled; broader formula-registry review remains open.
- Resolved in this maintenance pass: the authorized adapter supplies referenceable, unified theorem-like environments without modifying the user's style file.
- Resolved in this maintenance pass: translated output uses the Chinese proof heading with ASCII punctuation.

## Pending human review

- Confirm or supply the source tail containing the announced Bibliography and Index.
- Review formula crops against every proposed LaTeX transcription, including subscripts, superscripts, relations, signs, brackets, integral domains, and summation ranges.
- Confirm unresolved terminology and all low-confidence structure blocks.
- Review the sample translation and compiled template behavior before authorizing full-book translation.
