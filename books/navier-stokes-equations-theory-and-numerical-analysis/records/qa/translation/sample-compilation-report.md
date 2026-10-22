# Sample compilation report

- Root file: `tex/main.tex`.
- Engine: XeLaTeX, TeX Live 2025, driven by latexmk.
- Shared template source: the verified read-only template in the main worktree.
- Output: `output/sample-translation.pdf`.
- Pages: 3.
- SHA-256: `f1eb86b6db295795db0ba14c7553d823e989bd0b0f2813e5cc38a8bfc97e4e34`.
- Final undefined-reference warnings: 0.
- Multiply-defined labels: 0.
- LaTeX errors: 0.
- Rerun warnings: 0.
- Visual inspection: 3 of 3 pages passed; no clipping, overlap, missing content or unreadable glyphs.

The generic book compiler refused the book-worktree template directory because Windows checkout line endings produce a different byte manifest from the hash recorded by `new-book`. Git reports no template changes. Compilation therefore loaded the verified, pinned, read-only template from the main worktree; no template hash or template file was altered.

Result: passed.
