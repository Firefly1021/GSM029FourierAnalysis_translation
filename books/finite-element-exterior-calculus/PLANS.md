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

## Final completion

All 47 natural units, the supplementary publication front matter, generated contents, eight chapters, bibliography and index are complete. Final whole-book source coverage, mathematical alignment, names, configured punctuation, real cross-references, clean compilation, rendered regression and 34 repository tests pass. See qa/final-report.md. Prior phase stops and font blockers above are historical, not current. No further translation unit remains. Keep terminology proposals book-local and the approved non-Fraktur mapping; do not auto-promote or push.

## User-requested AJbook layout edition, 2026-10-21

The user selected AlJabr-1 for FEEC only. The original input template and all accepted translation/source/formula files remain immutable. The full pinned upstream collection is archived separately under template/collections/aljabr-1; its adapter is namespaced under template/adapter/aljabr-1. Shared changes were tested on the dedicated maintenance branch and merged to main before synchronization here. The expanded collection manifest is recorded separately from the historical legacy baseline; original file hashes are unchanged.

The new entry is tex/aljabr-main.tex and the selected output is output/book-aljabr-zh.pdf. The original tex/main.tex and output/book-zh.pdf remain unchanged and usable as the legacy edition. All 47 accepted natural units are reused, not regenerated. The 138-page B5 edition preserves all 537 labels and their numbers, passes clean compilation and all 34 regression tests, and has completed rendered-page inspection. See TYPESETTING.md and qa/template/aljabr-acceptance.json. No other book switches template; no remote push.

## User-requested original-font correction, 2026-10-21

The user rejected the fallback appearance and asked to download missing fonts. This supersedes only the prior AJbook font fallback, not any translation approval. Official Noto Sans CJK SC Regular/Bold/Medium/Black (Sans2.004) are installed at Windows current-user scope and pinned beside the upstream collection with their license and independent Git-blob/SHA-256 checks. The FEEC builder now loads upstream font-setup-open.tex unchanged with scoped Fontconfig discovery, and fails if the required fonts cannot resolve. No substitute font is accepted.

Current font-correction evidence: qa/template/aljabr-noto-acceptance.json. Preserve the previous fallback PDF and evidence as explicit history. Reuse all 47 accepted units and original math/source records. Keep upstream title geometry, body fonts, non-Fraktur policy and English environment headings. Inspect every newly rendered page and representative pages at higher resolution; preserve numbering and actual PDF destinations. Repository regression is now 36 tests including official font-file verification and no-fallback setup. No remote push is authorized.

## Current authority: exact template settings, 2026-10-21

The user rejected the enlarged readability experiment and required all settings to follow the template. This supersedes every proposed enlargement, density adjustment or independent visual override. Load pinned AJbook source settings unchanged, including original font/titles setup, native 10pt/B5 geometry, native integral symbols/limits, arraystretch 1.5, heading depths, theorem spacing/separators and bibliography/index styles. Keep only documented book-content/numbering/English-heading compatibility and the approved non-Fraktur presentation exception.

The resulting 140-page PDF is accepted for technical layout QA in qa/template/aljabr-template-parity-acceptance.json. Runtime parameters match 39/39, repository tests pass 39/39, all 140 rendered pages and five enlarged details were viewed, all 537 object label numbers are unchanged, and all 753 actual internal destinations are valid. Reuse all 47/47 accepted units; no source, translated wording or formula content was rewritten. Ten explicitly recorded prose-only newlines exist only in the generated layout copy. Preserve prior PDFs and QA as history. A future rebuild requires new hash-bound visual QA, not reuse of a historical publish action. User aesthetic approval is still separate. No remote push.
