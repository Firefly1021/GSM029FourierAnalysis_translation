# Krylov Subspace Methods for Linear Systems: final acceptance

Status: passed. All 39 natural units have passed their source, translation, mathematical, terminology, name, reference, punctuation, compilation and visual gates. The accepted sample was retained, not retranslated.

## Complete scope

The translation includes the Preface, Acknowledgements, complete Chapters 1-5, Software, all 212 references and all 179 index entries. The bibliography retains original-language titles, names and publication metadata rather than fabricating translated or updated records. The original index order and original printed-page provenance are preserved; displayed translated-page numbers are generated from real LaTeX page references.

There are 1,025 authored aligned blocks and 5,190 mathematical-expression comparisons, plus the previously accepted sample's 23 blocks and 96 comparisons: 1,048 blocks and 5,286 expression comparisons in total. These are occurrence-based source/target checks, not a count of distinct equations or an independent proof of the source mathematics.

| Chapter | Numbered equations | Algorithms |
|---|---:|---:|
| 1 | 43 | 11 |
| 2 | 75 | 0 |
| 3 | 138 | 35 |
| 4 | 58 | 11 |
| 5 | 25 | 12 |
| Total | 339 | 69 |

## Final integration gates

- Fresh-directory compilation: at least two XeLaTeX rounds, using the existing user template and adapter.
- Final PDF: 201 pages; SHA-256 `95c11cbf57ff9cd86be9046a60b02ec40a27c4640350d9644997ee683f8201f2`.
- Actual TeX input graph: 42 files, 877 labels and 1,125 reference-command occurrences. Undefined references, duplicate labels, wrong reference commands, translated environment-reference prefixes and Chinese-body punctuation violations: zero.
- Compiled PDF: all 877 object destinations agree with the corresponding auxiliary-file pages; all 1,516 internal PDF links resolve. Numbered equation and algorithm sequences are complete for every chapter.
- Index: 179 entries, 181 generated page links and 104 distinct original indexed source pages. Navigation targets are reviewed concept blocks on the original indexed page, not token-tight positions. Original index source-page choices are not silently moved to different source pages.
- Names: 628 source/target exact-form checks pass. The separate bibliography gate verifies all 212 complete author fields. Source accents, initials, hyphens, ordering and Unicode forms are preserved.
- Compile warnings checked: undefined references 0, multiply-defined labels 0, missing glyphs 0, overfull boxes 0.
- Accepted output regression: all 190 body/bibliography pages from the last accepted pre-index PDF retain identical extracted body text at their final page offset, ignoring whitespace and page footers. The final three-page contents and six-page index are separately reviewed.
- Visual evidence: final title/frontmatter, contents, first body page, the protected theorem page and all index pages were individually inspected. Earlier accepted pages retain their batch visual evidence. A prior exact-pixel diagnostic flagged one 0.01 pt glyph-position variation with identical text; it is documented, reviewed and nonblocking. Pixel-identical rendering is not claimed.

## Source and isolation protection

Original/external PDF SHA-256: `1e5e8bffab227a238c29f9dbb8e9746fc632d21429ddc2cb639a28e18cf2e375`.

User template version: `2.0.1-english-environment-headings-20260822`; manifest hash `9c405f97accf0b769854f4fadf93c22b473ad72435ddf0fc27f58c9a302a882c`. Source PDFs, user template files, accepted sample TeX/PDF and previously accepted translation text remain unchanged. Shared code and global terminology are unchanged. All book-specific artifacts remain below this book's directory.

Extra navigation anchors, book-ending contents entries and the Theorem 1.4 pagination guard live only in reproducible generated copies. Removing only those additions recovers the accepted canonical inputs exactly. The accepted TeX files were not overwritten to add index anchors.

Approved `grade -> 阶` is retained. No candidate is promoted, downgraded or silently substituted in the shared glossary. Completion uses the existing registry APIs without the finish wrapper's automatic terminology-promotion side effect. Normal local completion updates only this book's PROJECTS row; it does not modify another book's data or branch.

## Epistemic status and outstanding issues

Blocking issues: none. Unresolved terminology: zero. Twenty-five source-observation records remain in qa/issues.jsonl, with detailed reports under qa/source/. Each record may cover multiple source anomalies. They are reviewed provenance notes, not silently corrected mathematics or omitted content.

Formula fidelity relies on accepted original-page reviews plus exact paired-source/translation checks. Compilation success is not treated as proof that every source formula is mathematically correct. This final gate does not claim a new independent manual token-by-token review of previously accepted chapters.

## Deliverables and reproduction

- Final PDF: `output/book-zh.pdf`.
- Accepted Chinese TeX: `translation/reviewed/` and `tex/chapters/`; main document: `tex/main.tex`.
- Paired English/Chinese authored records: `translation/authored/`; structured source and source-page provenance: `structured/reviewed/`.
- Machine-readable acceptance: `qa/final-report.json` and `qa/final/automated-qa.json`.
- Link evidence: `qa/translation/final-destination-regression.json` and `qa/translation/index-reference-report.json`.
- Preservation and output regression: `qa/final/protected-inputs.json`, `qa/translation/index-linked-copies.json`, `qa/final/accepted-output-regression.json`.
- Last compile log: `logs/latest-compilation.log`; compile metadata: `qa/latest-compilation.json`.

Generated caches are reproducible, not alternate authoritative translations. In the registered book worktree, set PYTHONPATH to the repository src directory and invoke this book's workflow/full_workflow.py assemble function with final=True, then compile_preview(), to regenerate index-linked TeX copies and compile the same accepted content. Do not run metadata on passed units. The final packaged PDF must match its recorded hash; a later rebuild may have different PDF metadata.

All completion commits and registry synchronization are local. No GitHub push, remote-URL change, history rewrite, branch deletion or worktree deletion is performed.
