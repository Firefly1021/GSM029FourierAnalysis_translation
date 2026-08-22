# MathBookTranslation

This repository is a local-first, multi-book mathematical translation system. Shared code, the read-only LaTeX template, translation policy, QA rules, and the global terminology library live once at repository level. Every book's source and generated state are isolated below `books/<book-id>/` and, while active, on a dedicated Git branch and worktree.

The completed first book is registered as `fourier-analysis` in [PROJECTS.md](PROJECTS.md). Its accepted translation, QA evidence, source, and final PDF were migrated without retranslation.

## Daily commands

Create a new book from `main`:

```bash
python -m mathbook new-book <book-id> --source "/path/to/book.pdf"
```

The command validates the ID and PDF, records hashes and template version, creates `books/<book-id>/`, commits the registration locally, creates `book/<book-id>`, and creates a dedicated sibling worktree. The new worktree uses worktree-local cone sparse checkout: all shared system directories remain visible, while `books/` materializes only `books/<book-id>/`. Other books remain tracked in branch history and are never deleted. The command prints the worktree location.

Start diagnosis and the representative-sample workflow from that worktree:

```bash
python -m mathbook start-book <book-id>
```

After sample review:

```bash
python -m mathbook approve-sample <book-id>
python -m mathbook translate-book <book-id>
```

Resume safely after interruption:

```bash
python -m mathbook resume <book-id>
```

Run final whole-book QA and completion:

```bash
python -m mathbook finish-book <book-id>
```

Inspect state:

```bash
python -m mathbook status <book-id>
python -m mathbook list-books
```

Repair or retrofit the local view of an existing registered book worktree:

```bash
python -m mathbook isolate-worktree <book-id>
```

This command refuses to proceed if the selected worktree contains uncommitted files under another book. It preserves current-book and shared-file modifications byte-for-byte, does not remove any book from Git, and does not push or rewrite history. Sparse-checkout configuration is local Git metadata, so it is intentionally not committed or transferred by `git push`.

Users do not need to create directories, switch branches, or manage worktrees manually. Mathematical translation stages are executed by an explicitly configured Codex/agent processor; if none is available, the controller stops truthfully instead of fabricating translation or QA output.

## Terminology

```bash
python -m mathbook terminology review <book-id>
python -m mathbook terminology promote <book-id>
python -m mathbook terminology conflicts
python -m mathbook terminology history
```

Books write candidates and unresolved terms only inside their own directory. Controlled promotion uses `English + Domain + Context`, refuses silent overwrite, and appends every accepted change to `glossary/terminology-history.tsv`.

## Make interface

The same workflows are available as `make new-book`, `make start-book`, `make approve-sample`, `make translate-book`, `make resume`, `make finish-book`, `make status`, `make list-books`, and `make isolate-worktree` with `BOOK` and, for new books, `SOURCE` variables.

All commits and worktrees created by project automation are local. No workflow pushes to GitHub or modifies `origin`.
