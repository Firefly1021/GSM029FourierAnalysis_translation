# Plan for krylov-subspace-methods-for-linear-systems

## Sample work completed in this task

- Existing new-book registration and isolated worktree.
- Per-page PDF diagnosis, page map and full-book outline.
- Complete Section 1.8 source restoration and translation.
- Formula registry, source provenance, names, terminology and cross-references.
- Clean sample compilation, automated checks and rendered-page review.
- Historical sample stopping point: awaiting-sample-approval. Superseded by the user's instruction to translate the whole book on 2026-10-15. Remote push remains unauthorized.

## After user approval

- Apply the user-approved term grade -> 阶. Review the remaining proposed terminology.
- Use existing approval and natural-unit translation workflows.
- Replace sample-only source locators with actual translated chapter targets.
- Never regenerate an accepted unit.

## Active full-book task

- User instruction: 接下来翻译全书.
- Sample approval is recorded through the existing approve-sample command.
- Resume at the first incomplete unit; retain Section 1.8 byte-for-byte.
- Complete the Preface, Acknowledgements and Chapter 1 as the first integrated batch, then continue Chapters 2--5, Software, References and Index.
- No content is omitted to accelerate progress. Suspected source errors are preserved and recorded.
- Every completed batch requires source/translation alignment, mathematical token checks, proper-name checks, ASCII punctuation, real cross-references, clean compilation and visual review.
- Full-book extraction is unreviewed input, not completed translation. Pending chapter references remain explicit source locators until their translated targets exist.
- Only mark the book completed after all natural units and final integration pass. Do not push.

The original startup steps below remain a record of the controller workflow.

1. Run `python -m mathbook start-book krylov-subspace-methods-for-linear-systems` in its dedicated worktree.
2. Review the representative sample.
3. Approve the sample before full translation.

## Full-book completion record

- All 39 natural units passed; no next translation unit remains.
- The accepted sample and all earlier accepted chapter text remain unchanged.
- The final 201-page PDF, generated contents and concept-block index passed final integrity, numbering, destination, name, punctuation, compilation and visual gates.
- Detailed evidence: qa/final/full-book-report.md and qa/final-report.json.
- Source anomalies are retained in QA, not silently repaired.
- Approved grade -> 阶 and the shared glossary are unchanged. No automatic terminology promotion or remote push is performed.
