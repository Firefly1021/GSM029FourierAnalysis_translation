# Full-book translation plan

## Objective

Translate every supplied source page in table-of-contents order, preserving the accepted Chapter 2 sample unchanged as the style and technical baseline. Continue automatically after each batch that passes QA. Stop only for a genuine blocking issue that cannot be resolved from the source, project data, or reliable context.

## Baseline

- Primary source: `input/source/GSM029 - Fourier Analysis.pdf` (228 PDF pages).
- Read-only source SHA-256: `03baa3bf45ab43bf96ebf8c35dfb6bfb633c91c3106dee879a20f1fa08552fdf`.
- Accepted translation baseline: Chapter 2, PDF pages 37--51 / printed pages 25--39.
- Accepted sample file: `tex/chapters/sample.tex`; it must not be retranscribed or restyled. Reference-only maintenance is permitted when a previously unavailable target becomes available.
- Announced but unavailable source: Bibliography from printed page 217 and Index from printed page 219.

## Batch order

1. Chapter 1, PDF 13--36 / printed 1--24.
2. Complete Chapter 2 by adding only PDF 52--59 / printed 40--47 to the accepted sample.
3. Chapter 3, PDF 61--80 / printed 49--68.
4. Chapter 4, PDF 81--102 / printed 69--90.
5. Chapter 5, PDF 103--126 / printed 91--114.
6. Chapter 6, PDF 127--144 / printed 115--132.
7. Chapter 7, PDF 145--168 / printed 133--156.
8. Chapter 8, PDF 169--206 / printed 157--194. If needed, split only at complete section boundaries.
9. Chapter 9, PDF 207--228 / printed 195--216.
10. Front matter, PDF 1--12, after the mathematical chapter workflow is stable.
11. Bibliography and Index only if the missing source pages are supplied.

## Per-batch workflow

1. Preserve raw extraction and page renders.
2. Restore complete structural blocks with stable IDs and source-page links.
3. Register every display formula and any uncertain inline formula.
4. Register labels, backward references, forward references, figures, tables, and footnotes.
5. Update terminology and exact-form personal names without self-approving new entries.
6. Produce a faithful draft from structured source, then a Chinese mathematical-style review.
7. Generate one chapter file or section files included by a chapter driver.
8. Run punctuation, names, terminology, formula, structure, and cross-reference QA.
9. Compile the current batch and cumulative book from a clean directory with at least two LaTeX passes.
10. Render and visually inspect the new output pages.
11. Recheck all read-only input hashes and the accepted Chapter 2 sample hash.
12. Update status files and create a local Git commit when the full chapter passes.

## Current position

- Completed units: Chapters 1--6, PDF 13--144 / printed 1--132; QA and cumulative compilation passed.
- Active unit: Chapter 7, *Weighted Inequalities*.
- Active untranslated source range: PDF 145--168 / printed 133--156.
- The accepted Chapter 2 range PDF 37--51 remains unchanged in wording; its former unresolved reference to Section 8.6 resolves to the completed Chapter 2 label.
- Remote pushes are not authorized for this workflow; completed chapters receive local commits only.
