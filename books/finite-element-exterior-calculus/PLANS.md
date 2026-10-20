# Plan for finite-element-exterior-calculus

1. Run `python -m mathbook start-book finite-element-exterior-calculus` in its dedicated worktree.
2. Review the representative sample.
3. Approve the sample before full translation.

## Current sample-only execution

- Use the registered native PDF and unchanged shared template. Do not read other books' translation or QA data as input.
- All 130 pages have mechanical text/image/font/geometry diagnosis; selected original page images are independently reviewed. Native mathematics still requires image-based transcription because embedded-font text mapping is unreliable.
- Sample scope: Sections 2.4-2.6 main text only, PDF 25-28 / printed 15-18. Section 2.3 material before the start and separate Box 2.1 after the end are outside this sample.
- Preserve all selected prose, formulas, diagrams and proof steps; uncertainty is recorded rather than guessed. Scope does not expand to a whole chapter.
- Source restoration, schema validation, formula alignment, contextual terminology lookup, exact names, English headings, ASCII punctuation, real references, clean two-round compilation and visual QA are complete.
- Keep the 24 terminology candidates proposed. Do not promote them or overwrite the shared glossary.
- Technical sample QA does not equal user approval. Preserve the reviewed sample when resuming after acceptance; do not regenerate it.
- Stop at awaiting-sample-approval. Do not call approve-sample, translate-book or finish-book. Do not push.

## Active full-book authorization

- The user approved the sample and instructed: 可以, 接下来进入全书翻译.
- The sample-only stop above is historical and has now been superseded by that approval. The existing approve-sample command has recorded approval.
- Preserve the accepted Section 2.4-2.6 text, source reconstruction, formula records and sample PDF. Do not run the sample preparation workflow again.
- Continue from frontmatter, then the first unfinished natural units, through all eight chapters, bibliography, index and final integration. Do not reset the progress inventory.
- Every batch requires original-page comparison, complete translation without summarization, unchanged mathematical tokens, exact names, contextual terminology lookup, English headings, ASCII punctuation, semantic references, clean compilation and rendered-output review.
- Keep proposed terms book-local; the accepted sample wording is the baseline, not authorization to replace the shared glossary.
- Final completion requires all natural units and whole-book gates to pass. No remote push is authorized.

## Current verified blocker

- Complete Preface and Chapter 1 are accepted locally. Do not regenerate them.
- A follow-up check of the original PDF's embedded EUFM10 glyphs found three incorrectly transcribed Z/B mathematical alphabets in the already accepted sample. See qa/formula/accepted-sample-font-followup.md.
- Do not overwrite the accepted sample or its formula records without explicit correction authorization. Progress is preserved, not reset. The blocker supersedes the prior sample formula PASS only for these affected expressions.
- Proposed correction is narrowly limited to mathcal Z_k, mathcal Z^k and mathcal B^k -> their mathfrak forms, consistently across source/translation/notation/registry/output. Do not change mathcal H or other material.
- After authorization, verify source font families, recompile at least twice, inspect output and clear the issue before resuming the first incomplete unit, chapter-02-introduction. No push.

## Approved non-Fraktur presentation policy

The user rejected the proposed Fraktur change: 不要,只要不是Fraktur 字体就行. This decision supersedes the historical blocker above. Preserve accepted mathcal Z/B and all accepted sample bytes; retain original font-family evidence and register the explicit presentation exception. Do not introduce Fraktur in translated mathematics. Preserve distinctions between different source objects with documented non-Fraktur mappings. Resume chapter-02-introduction without resetting progress. No push.
