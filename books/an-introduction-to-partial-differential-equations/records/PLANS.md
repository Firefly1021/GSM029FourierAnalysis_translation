# Formal translation plan

## Current completion checkpoint: 2026-11-17

All 12 chapters, front matter, all Appendix A references and the complete source
index are translated and integrated. Technical QA passed with documented source
and legacy-input exceptions. Final output: output/book-zh.pdf, 350 pages.
Current authority: records/qa/final-book-qa.json and records/PROJECT_STATUS.md.
Next: reader review, not more chapter translation. Do not regenerate passed
translation or rerun one-time preparation/finalization scripts. No remote push.
The historical plans below are preserved as execution history, not a current
list of untranslated chapters or unresolved generated forward references.

## Historical working plan

User approved the revised sample on 2026-11-15 and authorized formal translation.
The accepted sample and its standalone PDF remain immutable and are reused.
All readable Chapter 1 material has now been source-reviewed and translated,
through printed page 35 / PDF 45: 1.1, Laplace, heat and wave equations,
equations 1.1--1.145, statement objects 1.1--1.21 and Problems 1.1--1.29.
Problem 1.16 is retained exactly as printed under the user's explicit decision
"不必管,PDF是什么样,就直接保留" on 2026-11-15. No curves are reconstructed,
and the missing source curves are no longer a blocking issue.

Chapter 2 is now translated through its end, PDF 76 / printed 66, including
all proofs, equations 2.1--2.135, statement objects 2.1--2.29 and Problems
2.1--2.22. Chapter 3 is translated through PDF 110 / printed 100 and has passed
chapter-local source-fidelity and technical QA: 135 equations, 40 statements,
14 source figures, the footnote and all 12 Problems. Its 134 reference uses
resolve. Chapter 4 is now complete through PDF 131 / printed 121 and passed
chapter-local QA: 56 numbered equations, 29 statements, 26 Problems, one source
figure and all 67 reference uses. This is not full-book acceptance. Continue
within Chapter 8, Operator Theory. Chapter 5 source translation is complete
through PDF 183 / printed 173: all Sections 5.1--5.5, complete proofs,
equations 5.1--5.216, statements 5.1--5.85, five original footnotes and
Problems 5.1--5.61 are translated and compiled. Its outgoing Chapter 9
references remain explicitly pending; source-stage completion is not whole
chapter acceptance. Chapter 6 is fully translated through PDF 212 / printed
202, including all Sections 6.1--6.3, equations 6.1--6.84, statements
6.1--6.65, every printed proof and Problems 6.1--6.34. Its 69 explicit
chapter references resolve and chapter-local QA passed. Preserve the frozen
Chapter 6 inputs under qa/chapter-06-integration-qa.json. The source PDF 205
relative next-chapter remark is still recorded as ambiguous; no target was
guessed. Chapter 7 source translation is now complete through PDF 237 /
printed 227, with all 50 numbered equations, 61 statements, one footnote,
full printed proofs and all 24 Problems. Its outgoing Chapter 9 target is
pending (52 of 53 explicit chapter reference uses resolve), so no false
full-chapter integration pass is recorded. Continue Chapter 8 from the
first incomplete natural unit, preserving all completed source units.
The Chapter 6 opening
at PDF 184 has logical printed page 174 with suppressed folio, confirmed by
PDF 185 / printed 175.
The exact active unit is recorded in qa/workflow-state.json.
Continue
scan-based reconstruction, mathematical token verification, shared glossary
lookup, proper-name protection, ASCII punctuation, real cross-references,
clean multi-pass compilation and visual QA. Do not regenerate passed batches.

Preserve original Figure 1.1 with its source anomaly recorded; do not draw
missing branches. PDF 71 and 73 have now been visually verified, including the
original diagrams. PDF 90, 114 and 122 have also been source-reviewed. Retain the warning about PDF 341
until that actual page is checked. Do not assume the -10 page offset where
it has not been checked.
Do not modify templates/other books, promote global terms silently or push.

## Acceptance gate

### Compilation cadence (user correction, 2026-11-17)

Continue scan comparison, source reconstruction, translation, formula-token,
name, punctuation and reference-registration checks at block level. Do not
rebuild the whole book after one or two source pages. Aggregate unaccepted
content into complete subsections or approximately 10--20 original-page
batches before a current-chapter-only build and visual review. Use the local
`workflow/chapter_preview.py` driver: previous chapters supply external labels
from the last actual integrated build and are not typeset. Its stable build
cache is reusable. Whole-book clean builds are reserved for chapter integration
and final acceptance; external reference reuse is not full-book link QA.
Use a smaller isolated test only for a concrete layout or compile fault. Never call unbuilt
content compiled or QA-passed. Preserve all existing accepted/frozen inputs.


Chapter 8 source scope is complete through all Sections 8.1--8.7, PDF 292 /
printed 282. Retain every printed argument, equations 8.1--8.191,
statements 8.1--8.104, both original figures and Problems 8.1--8.57.
Continue Chapter 9, now underway from PDF 293 / logical printed 283.
The actual Chapter 9 and Section 9.2.3 anchors now resolve earlier pointers.
Chapters 5, 7 and 8 have passed chapter-local technical QA and their current
source/body snapshots are frozen under their integration receipts. Preserve distinct Banach/Hilbert
times/star notation and the exact original graph crops, without invented curves.
New numbered equations must retain source order in both aligned languages;
all later source anomalies are recorded rather than repaired.

Problem 1.16 source graph data is absent in two independent source renderers.
Keep its exact source crop and translated text, not a guessed reconstruction.
Its exact retention is user-authorized, not a claim that curves were recovered.
The currently pending translated target is Chapter 12.
The actual Chapter 9 and equation (8.173) targets now exist; retain the
recorded suspected original misreference to (8.173), without redirecting it.
The Chapter 6/7 anchors and all Chapter 6 exercise targets now resolve.
The latter is a suspected original misreference, deliberately not changed.
Two previously accepted input lines contain ideographic commas; preserve those
accepted files and report the legacy punctuation exception, not a false clean
whole-chapter punctuation result.

output/book-zh-progress.pdf remains the accepted six-page Batch 01 edition.
output/book-zh-draft.pdf is the evolving translation draft, with visible draft
metadata; the current page count and checks are in qa/active-draft-qa.json.
Source-stage records are not full QA acceptance while later targets remain.
Continue readable sections without treating a batch boundary as a stop request.
