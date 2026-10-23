# Finite Element Exterior Calculus: representative sample

Technical sample QA: passed. User acceptance: pending. Required stop state: awaiting-sample-approval.

Book ID: finite-element-exterior-calculus. Branch: book/finite-element-exterior-calculus. Registered worktree: D:\CelianFile\BOOKTRANSLATION-worktrees\finite-element-exterior-calculus. All book-specific artifacts are below books/finite-element-exterior-calculus/.

## Scope and source strategy

The supplied PDF has 130 pages and is native typeset, with 117 native text/vector pages, 12 pages containing raster illustrations, and one blank page. No full-page scans or text-mode-3 hidden text operators were found. The mathematical font text mappings are unreliable on 108 pages, so this sample does not copy formulas blindly from extracted text. Prose/layout extraction is combined with original-image transcription and verification. No OCR is used. Full diagnostic evidence is in pdf-diagnosis.json and pdf-diagnosis-report.md.

The selected sample is the complete main text of Sections 2.4-2.6, PDF 25-28 / printed 15-18. The previous section's residual material on PDF 25 and the independent chapter summary Box 2.1 on PDF 29 are explicitly outside the sample. No selected paragraph is summarized or omitted. This sample is not a claim that Chapter 2 or the entire book is translated.

## Content and QA

There are 41 aligned source/translation blocks and 129 registered mathematical-expression occurrences. The sample includes two commuting diagrams, four numbered equations, implicit definitions in their original prose form, Proposition 2.1 with its complete Proof, Theorem 2.2, Remark 2.3, and chapter/section/bibliographic references. Original formula tokens, indices, primes, bars, domains and arrow labels are preserved. Translated prose inside calculation annotations is separated from mathematical annotation tokens. Source and formula records pass the existing shared JSON schemas.

The existing user template and English environment headings are retained without modifying the original style or reference TeX. The sample has 14 unique labels and 8 explicit reference commands. All references are defined, and 13 principal object destinations were checked against their compiled page numbers. Three verified outside-sample references are explicitly identified as source locators, not completed translated material.

Exact name counts agree for de Rham (16), De Rham (3), Élie Cartan (1), Betti (1), and Stokes (1). The sample has 24 book-local proposed terminology candidates and zero unresolved ambiguities. The authoritative global glossary was queried by English/domain/context and left unchanged; no term was promoted or falsely approved. In particular, 上链/闭上链/上边界链 and related terminology remain open for the user's sample-style acceptance, not marked globally approved.

Clean-directory compilation completes at least two XeLaTeX rounds. Undefined references, duplicate labels, missing glyphs, overfull boxes, translated environment-reference prefixes and Chinese-body punctuation violations are all zero. All five output pages and the four original sample pages were individually visually inspected. Current output has no observed clipping or formula overlap. One original wording imprecision is retained as a reviewed nonblocking source note rather than silently strengthened.

## Output and stop condition

Sample PDF: output/sample-zh.pdf, five pages (four translated-content pages and one clearly marked external-reference locator page). SHA-256: af2e58b629a6be9dbde698544d4c2a6419c2545a6b7c8295c63b9868179a366c.

Reviewed Chinese TeX: translation/reviewed/sample.tex and tex/chapters/sample.tex. Restored English: structured/reviewed/sample.tex. Block provenance: structured/source/sample-provenance.json. Mathematical registry: formulae/sample.jsonl. Global code and terminology, original PDFs and user templates are protected and unchanged.

Blocking issues: none. Unresolved terminology: zero. User should inspect the prose fidelity and homological-algebra terminology in Sections 2.4-2.6, the two diagrams and displayed derivation, the English environment headings, and the name/diacritic rendering. This is not permission to start the full book. No approve-sample, translate-book, finish-book or remote push is executed.

The initial new-book command created and committed registration automatically. The first start-book command correctly reported the absence of a configured processor; the existing start_book processor callback completes this agent-authored sample without changing shared automation configuration. Schema validation uses a pinned optional jsonschema dependency installed only under this book's ignored temporary directory; no shared requirements were changed.
