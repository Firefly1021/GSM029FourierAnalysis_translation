# chapter-01-section-01 template integrity report

- Compilation used the authoritative read-only template at `D:/CelianFile/BOOKTRANSLATION/template/`.
- Authoritative `template/style/Mystyle.sty` SHA-256 before and after: `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- Authoritative `template/reference/main.tex` SHA-256 before and after: `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`.
- These hashes equal the recorded per-file hashes in `config/template-manifest.json`.
- Book-pinned aggregate template hash remains `ffd7d44e84a4cf3be3d4322bd420fe6a53b668d5fa1529232b310a35191cf24d`.
- `git diff -- template` and `git status --short -- template` were empty before compilation.
- The book-worktree checkout continues to have the already-recorded byte-level line-ending difference (`worktree-template-line-endings`); its pre/post hashes did not change, and the corresponding Git blobs are identical to `main`.
- No user file under `template/style/`, `template/reference/`, or `template/assets/` was modified.
- The book-only numbering helper is `tex/book-macros.tex`; it preserves the accepted shared environments and does not alter the template.

Result: Pass. The known line-ending materialization issue is non-blocking and unchanged.
