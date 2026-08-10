# Multi-book refactor report

## 1. Migration identity

- Pre-migration commit: `943e53f63453d4ff93ab94ec98b3edf05ca8745f`.
- Safety tag: `first-book-complete-before-multibook-refactor`.
- Refactor commit: the local commit containing this report, with message `Refactor translation system for automated multi-book workflow`. Its resolved hash is reported by `git log` after commit creation because a commit cannot contain its own hash.
- First-book ID: `fourier-analysis`.
- Remote before and after: `https://github.com/Firefly1021/GSM029FourierAnalysis_translation.git`.
- Remote changed: No.
- Push performed: No.

## 2. First-book migration

The following first-book state was moved, not regenerated, into `books/fourier-analysis/`:

- source PDF and source manifest;
- all page images, raw text, layout, OCR evidence, formula crops, and temporary build evidence;
- structured source and reviewed structures;
- formula registries and formula QA;
- draft and reviewed translations;
- canonical TeX, all chapters, figures, generated markers, and accepted sample;
- names, notation, unresolved terminology, and a new empty per-book candidate file;
- QA reports, issues, progress, logs, plans, status, and output PDFs.

The shared user template moved once to `template/`; the translation adapter moved once to `template/adapter/`. No per-book copy of `.sty`, shared source code, scripts, schemas, or tests was created.

First-book status is `completed` for every supplied page. The existing source limitation remains recorded: the PDF ends at printed page 216 although the contents announce a Bibliography and Index afterward.

## 3. Pre/post regression

| Check | Pre-migration | Post-migration | Result |
|---|---:|---:|---|
| Output pages | 167 | 167 | Pass |
| Canonical TeX files | 66 | 66 | Pass |
| Semantic labels | 511 | 511 | Pass, all unique |
| Reference commands | 777 | 777 | Pass, all targets defined |
| Formula/non-formula command mismatches | 0 | 0 | Pass |
| Chinese-prose forbidden punctuation | 0 | 0 | Pass |
| Undefined-reference warnings | 0 | 0 | Pass |
| Multiply-defined-label warnings | 0 | 0 | Pass |
| LaTeX errors | 0 | 0 | Pass |
| Unit tests | 22 | 29 | Pass |

- Pre-migration accepted PDF: 1,049,907 bytes, SHA-256 `b376c39b7c9698443629d086a0b51173a05d09baccbc6f04a6e13aca57a31a33`.
- Pre-migration fresh build: 1,049,916 bytes, SHA-256 `c64e1f3acdb2780f587e3566486ef405911acf65b5dd29c6a3b20f4364e2bf23`.
- Post-migration fresh build: 1,049,897 bytes, SHA-256 `910e02eecac6db3e9f77748024c6ef1f0806fd3c50545bc75313a487f90dc75b`.
- Post-migration build directory: `books/fourier-analysis/workspace/temporary/migration-post-20260810-1`.
- Extracted text from the pre- and post-migration fresh PDFs is byte-identical, SHA-256 `308a022a8b013b7777ff64deb8b798389857547153dd7fc57fb51d2ee5c05015`.
- Rendered pages 1, 3, 12, 13, 36, 60, 80, 100, 120, 149, 160, and 167 are pixel-identical at 120 DPI. Visual inspection of the title page and a formula-dense Chapter 9 page found no clipping, overlap, missing glyph, or layout change.
- `structured/`, `formulae/`, `logs/`, and `output/` migration tree manifests exactly match their pre-migration file counts, byte counts, and aggregate SHA-256 values.
- All relocated tracked text was compared with the completed commit after newline normalization. No translation, TeX, structured source, formula, template, or binary semantic mismatch was found. The only semantic difference in historical material was the expected dynamic build-directory value in a template compilation report generated during baseline verification.
- The existing `xdvipdfmx` warning for duplicate PDF object `equation.9.7` occurs before and after migration. It is not a duplicate LaTeX label or unresolved reference and was not altered because accepted book content is immutable in this refactor.

## 4. Source and template integrity

- Source PDF: 228 pages, SHA-256 `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- User style: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- User reference TeX: SHA-256 `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- User template bibliography asset: SHA-256 `89b952edcb3192ec7eaa210bd962c3d4fae05f885b525a2ab61257669b41a25f`.
- Shared template plus adapter manifest: SHA-256 `ffd7d44e84a4cf3be3d4322bd420fe6a53b668d5fa1529232b310a35191cf24d`.
- Recorded template version: `1.0.0-first-book`.

The first book is pinned to this manifest. A future shared-template change causes compilation refusal rather than silently changing an old book. Historical template bytes remain recoverable from the safety tag and Git history.

## 5. New architecture

```text
AGENTS.md
README.md
PROJECTS.md
config/
glossary/
template/
    style/
    reference/
    assets/
    adapter/
style/
src/mathbook/
scripts/
schemas/
tests/
qa/migration/
books/
    fourier-analysis/
        PROJECT_STATUS.md
        PLANS.md
        config/book.yaml
        input/source/
        glossary/
        workspace/
        structured/
        formulae/
        translation/
        tex/
        qa/
        logs/
        output/
```

`ProjectPaths` owns shared roots and Git worktree discovery. `BookPaths` validates book IDs, prevents path traversal, and refuses writes outside the selected `books/<book-id>/` root.

## 6. Global terminology library

- Initial contribution from `fourier-analysis`: 122 rows.
- Preserved status: 122 `needs-review`; no entry was silently approved.
- Semantic legacy fields preserved: 122 of 122.
- Conflicting `English + Domain + Context` keys: 0.
- Required fields supported: English, Preferred Chinese, Domain, Context, Forbidden Alternatives, Status, first/last source and location, and Notes.
- Supported statuses: `approved`, `proposed`, `ambiguous`, `rejected`, and `needs-review`.
- History: 122 auditable initial-import records in `glossary/terminology-history.tsv`.

Promotion requires a complete `proposed` candidate marked `[safe-to-promote]`, performs exact-key duplicate and domain/context conflict checks, never overwrites an existing meaning, writes history, commits through the clean main worktree, and synchronizes main back to the book branch locally.

## 7. Branch/worktree and double isolation

- Stable system branch: `main`.
- Active-book branch format: `book/<book-id>`.
- Worktree root format: sibling directory `<repository-name>-worktrees/<book-id>`.
- Completed `fourier-analysis` does not maintain an active worktree. Its historical branch points to the completed refactor state.
- Git isolation: one branch and worktree per active book.
- Data isolation: every book-specific write remains inside `books/<book-id>/`.
- Shared state is read-only on book branches except controlled main-worktree terminology promotion.
- Automation blocks `git push`, remote URL mutation, and history-rewriting operations.

## 8. Automation and isolation test results

- `new-book`: passed in a real temporary Git repository for `test-book-a` and `test-book-b`; verified PDF signature/hash, local registration commits, independent branches, external worktrees, and post-checkout PDF hashes.
- `start-book`: passed with an injected deterministic test processor; verified full-PDF page inspection, representative-page plan, required artifacts, and book-only state changes.
- `approve-sample`: passed and refused to bypass its required template, formula, cross-reference, compilation, and blocking-issue gates.
- `resume`: passed; the completed unit was not selected again.
- `finish-book`: passed; created local completion history and left the book branch and worktree intact.
- Same LaTeX label in two books: passed.
- A-to-B and B-to-A write isolation: passed.
- Shared global terminology with independent candidates: passed.
- Domain-specific same-English meanings: passed.
- Promotion deduplication and history: passed.
- Illegal ID and path traversal: rejected.
- Missing explicit book ID: rejected.
- Branch/book-id/worktree/path mismatch: rejected.
- Remote push through automation: rejected.
- Full suite: 29 tests passed.

Temporary test repositories, branches, worktrees, and book data were removed with their temporary test root. The real first book was not touched by test cleanup.

## 9. High-level interfaces

Implemented commands:

```bash
python -m mathbook new-book <book-id> --source "/path/to/book.pdf"
python -m mathbook start-book <book-id>
python -m mathbook approve-sample <book-id>
python -m mathbook translate-book <book-id>
python -m mathbook resume <book-id>
python -m mathbook finish-book <book-id>
python -m mathbook status <book-id>
python -m mathbook list-books
python -m mathbook terminology review <book-id>
python -m mathbook terminology promote <book-id>
python -m mathbook terminology conflicts
python -m mathbook terminology history
```

Equivalent Make targets are present. Users do not need to run `mkdir`, copy source PDFs, edit registries, switch branches, or create worktrees manually.

## 10. Remaining issues and boundary

1. The first source PDF does not contain the announced Bibliography and Index. No reconstruction was attempted.
2. Mathematical sample/full translation cannot be truthfully generated by a deterministic local Python program alone. The controller therefore requires an explicitly configured Codex/agent processor for those semantic stages and stops without fabricated output when no processor is present. Path management, Git/worktree management, diagnosis, state transitions, QA gates, compilation orchestration, commit control, and recovery are automated.
3. The pre-existing `xdvipdfmx` duplicate object warning for `equation.9.7` remains recorded. LaTeX labels and references pass.
4. Shared template upgrades are hash-gated. Compiling an old book against a different manifest requires explicit review or recovery of its recorded version from Git history.

## 11. Minimal next-book use

From a clean local `main` worktree:

```bash
python -m mathbook new-book <book-id> --source "/path/to/book.pdf"
```

Then enter the printed worktree path and run:

```bash
python -m mathbook start-book <book-id>
```

No second formal book was created, no next-book translation was started, no remote setting was changed, and no GitHub push was performed during this refactor.
