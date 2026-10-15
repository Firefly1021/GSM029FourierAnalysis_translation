# Representative sample acceptance record

Status: awaiting-sample-approval.

The agent has completed the sample workflow. User approval is pending; the rest of the book has not been translated.

## Identity and isolation

- Book ID: krylov-subspace-methods-for-linear-systems.
- Branch: book/krylov-subspace-methods-for-linear-systems.
- Worktree: D:/CelianFile/BOOKTRANSLATION-worktrees/krylov-subspace-methods-for-linear-systems.
- Exactly this book is materialized under books/ in the isolated worktree.
- Source PDF SHA-256: 1e5e8bffab227a238c29f9dbb8e9746fc632d21429ddc2cb639a28e18cf2e375.
- User template manifest and raw file hashes are unchanged.
- Shared code, policies, templates and global terminology have no book-branch edits.

## Scope and results

234 source PDF pages: 232 native, 1 mixed illustrated cover, 1 blank. The complete page mapping is explicit rather than a constant offset.

The sample is complete Section 1.8: PDF 32--36 / printed 19--23, ending before Section 1.9. Output is output/sample-zh.pdf (5 pages: four pages of translated content and a clearly marked source-locator appendix).

| Check | Actual result |
| --- | --- |
| Aligned source/translation blocks | 23 / 23 |
| Math expressions registered and token-compared | 96 |
| Numbered equations | 15 |
| Tables / footnotes | 2 / 2 |
| Exact name records | 7 |
| Semantic labels in compiled document | 26 |
| Internal PDF links checked | 32 |
| Undefined references | 0 |
| Duplicate labels | 0 |
| Wrong reference commands | 0 |
| Chinese-body punctuation violations | 0 |
| Translated environment prefixes | 0 |
| Missing characters / overfull boxes | 0 / 0 |
| Structural/formula schema rows validated | 23 / 96 |
| Blocking issues | 0 |

Source pages and all output pages were visually reviewed. Compilation used the LaTeX skill's existing TeX Live driver from a clean directory plus an explicit additional XeLaTeX round. Actual build evidence is in latest-compilation.json and the book's logs/.

The shared CLI has no configured shell sample processor. After the requested start-book command completed mechanical diagnosis, this task used the controller's existing explicit agent callback. The book-local workflow script validates actual reviewed artifacts; it does not generate translations or mathematical reconstructions. No shared automation configuration was changed.

## Review choices

17 book-local terminology candidates are proposed. One nonblocking unresolved choice remains: grade is provisionally 级; 阶数 is an alternative for user review. No global approved term was overwritten.

Statement headings follow the existing shared counter, so source Definition 1.2 / 1.3, Proposition 1.1 and Remark 1 render as Definition 1.1 / 1.2, Proposition 1.3 and Remark 1.4. Their source numbering is separately preserved. Formula numbers (1.20)--(1.34) are retained.

Three sample-external references point to explicitly marked source locators, not fabricated translated chapters. Full-book integration must replace those locators with real translated chapter/section targets.

Please review translation fidelity, grade terminology, statement numbering, bold math symbols, the Proposition proof and both table contents. No remote push was performed.
