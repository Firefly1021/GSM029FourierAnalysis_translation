# Book-local editing rules

Read `../shared/AGENTS.md` before modifying any book. The user explicitly requested the consolidated books/shared layout on 2026-10-22; old sibling-worktree instructions are historical.

- The only daily project is the parent library, on `main`. Select an explicit book-id. Current locations are in `config/library-binding.json` inside each book and `shared/PROJECTS.md`.
- Edit exactly one `books/<book-id>/` unless the user explicitly requests a multi-book operation. Use ProjectPaths and BookPaths for programmatic writes.
- Shared code and the global terminology library are not book-local scratch space. Shared-system changes use a maintenance branch.
- Original source PDFs, original templates, accepted text, formulas and QA evidence are preserved. Do not rewrite accepted content unless the user asks for that correction.
- Read the selected book's `OPEN-THIS-BOOK.md` for its actual full-book TeX entry. A file named main.tex may instead be a historical sample.
- Each book has a pinned `template/`; do not silently swap it for the shared newest template. Do not mix Mystyle with AJbook.
- Keep exact personal names, formulas, English environment headings, ASCII Chinese-body punctuation and real LaTeX cross-references under the shared rules.
- A clean build writes a new book-local temporary directory. It must not replace an accepted PDF without review.
- Do not edit or run translation jobs in `shared/.legacy-worktrees/`; those are recoverable history. Do not delete their branches/worktrees, rewrite history, change remotes or push without an explicit user request.
