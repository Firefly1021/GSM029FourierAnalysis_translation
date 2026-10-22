# Sample template report

- Template version: `1.0.0-first-book`.
- Pinned manifest hash: `ffd7d44e84a4cf3be3d4322bd420fe6a53b668d5fa1529232b310a35191cf24d`.
- Git blob identity between main and book worktree: passed for `Mystyle.sty`, reference `main.tex` and `ref.bib`.
- Normalized content identity between main and book worktree: passed.
- Git changes under `template/`: none.
- User `.sty`, reference `.tex` and `.bib` modified: no.

The legacy raw-byte manifest checker reports the `.sty`, reference `.tex` and `.gitkeep` files as changed in a newly created worktree because the migration manifest recorded main-worktree CRLF bytes while `.gitattributes` controls checkout line endings. The Git blobs and normalized content are identical. This is recorded as a non-blocking manifest-portability warning; no template file was rewritten to hide it.

The sample compiled with the shared style and translation adapter. Result: passed for content integrity, with the raw-byte portability warning retained.
