# An Introduction to Partial Differential Equations

Authors: Michael Renardy and Robert C. Rogers. Second Edition, as printed on the source title page.

This is a sample-only active book in the unified books/shared library. Active
branch: main. The book/... branch is a local registration checkpoint, not a worktree.

- Edit or compile: `tex/main.tex` (XeLaTeX; pinned Mystyle and shared English-heading adapter).
- Sample scope: original PDF 12--14, printed 2--4. All body material on these pages is included.
- Reconstructed English: `structured/reviewed/sample-restored-en.tex`.
- Chinese source: `tex/chapters/sample.tex`; aligned record: `structured/reviewed/sample.json`.
- Sample PDF: `output/sample-zh.pdf`.
- Page diagnosis and mapping: `qa/page-diagnosis.json`, `structured/source/page-map.json`.
- Integrity and sample QA: `qa/registration-integrity.json`, `qa/sample-qa.json`.

The scan has hidden OCR; its text is not mathematically authoritative. Only the
sample is restored and translated. No full-book OCR or translation has begun.
Template files are read-only. Existing other-book pending changes are preserved.
New terms are proposed book-local candidates, not global approvals.

The normal new-book command refused a dirty main checkout. The book-local
registration helper reused BookPaths/config/registry helpers with narrower,
user-authorized conflict checks; its first commit excludes existing edits.
The normal start-book entry uses an unconfigured global processor. This book
uses the existing `start_book(..., processor=...)` extension instead, without
changing shared automation. See `workflow/sample_workflow.py`.
