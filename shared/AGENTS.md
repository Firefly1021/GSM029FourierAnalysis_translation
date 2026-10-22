# Mathematical book translation system rules

## Global shared state

- The user's 2026-10-22 consolidation instruction supersedes the old sibling-worktree layout. The visible project has exactly two top-level directories: `books/` and `shared/`. Hidden Git metadata remains at the library root.
- Shared code, CLI, scripts, schemas, tests, template files, policies, README, registry and the authoritative terminology library live under `shared/`.
- The only authoritative cross-book terminology file is `shared/glossary/terminology.tsv`. Match terms by `English + Domain + Context`, not by English alone.
- User files under `shared/template/` and pinned `books/<book-id>/template/` are read-only. Never modify, overwrite, rename, normalize, or auto-format their contents.
- Shared translation-only template integration belongs in `shared/template/adapter/`. An existing book keeps its exact pinned template; updating shared templates is not authorization to change old books. Do not create a competing visual style.
- Verify template manifest hashes before and after workflows that compile or inspect the template.

## Per-book state

- Every book-specific artifact must be below `books/<book-id>/`: source PDF and auxiliaries, page images, OCR, raw text, layout, structured data, formulae, names, notation, candidates, unresolved terms, translations, TeX, figures, generated files, QA, issues, logs, plans, status, and output.
- A book-specific command always requires an explicit `book-id`. Implicit current-book selection is forbidden.
- Book-specific writes must pass through `ProjectPaths` and `BookPaths` and remain inside `books/<book-id>/`. Never write to another book's directory.
- Completed translation text is immutable unless the user explicitly authorizes a correction. Resume from the first incomplete natural unit and never regenerate a unit that already passed QA.
- The user explicitly requested completed-book cleanup on 2026-10-22. Retain the editable final TeX dependency closure, original PDFs/templates, accepted outputs, restored English, formula/terminology/provenance and issue/QA records. Remove reproducible page/OCR/build caches, obsolete previews and translation-only per-book scripts after a dry-run manifest and successful clean builds. Required generated macros/Bib/figures are final sources, not disposable cache.
- Later user template updates never silently alter an accepted book. An exact historical acceptance-manifest snapshot may be separately pinned as `template-accepted/` and explicitly selected by the binding; preserve the newer user files untouched in `template/`.

## Git and worktree safety

- `main` is the single active library checkout. An explicit book-id, registry workspace, `config/library-binding.json` and physical `books/<book-id>/` path must agree before any book-specific write.
- Book writes remain contained by BookPaths; shared state and other books are never writable as a side effect of translating the selected book. Do not switch to a historical book branch in the unified directory.
- Historical `book/<book-id>` branches and their worktrees are preserved under `shared/.legacy-worktrees/`, locked against pruning/removal and excluded from daily editing. Historical absolute paths in original configs, QA and logs are evidence, not active location settings. The binding and shared registry are authoritative for current locations.
- Shared-system fixes use a dedicated maintenance branch and are merged to `main` after verification. Newly registered books get contained directories and local checkpoint branches, not new sibling worktrees.
- Never force push, rewrite history, delete a real book branch/worktree, modify the remote URL, or perform a remote write without an explicit user request. Project automation must never execute `git push`.
- Terminology promotion is controlled and audited. It updates main's shared terminology library without whole-file replacement, creates history records, and never silently overwrites another meaning.

## Source and mathematical fidelity

- Treat every source PDF and supplied auxiliary file as read-only. Verify SHA-256 before and after any workflow that reads it.
- Preserve every assumption, conclusion, condition, quantifier, negation, implication direction, and logical strength.
- Do not add explanations absent from the source. Never fabricate extraction, OCR, structure, formula, terminology, translation, compilation, or QA results.
- Do not simplify, rederive, normalize, or rewrite formulas. Preserve tokens, variables, subscripts, superscripts, delimiters, signs, ranges, domains, labels, and references. Route uncertainty to QA.
- Compilation success is not proof of formula correctness.

## Personal names

- Never translate, transliterate, transcribe, expand, reorder, or normalize natural-person names.
- Preserve the original script, accents, diacritics, hyphens, initials, abbreviations, spaces, capitalization, and name order exactly.
- In eponymous terms, translate only the ordinary mathematical noun: `Hilbert space` -> `Hilbert 空间`, `Poincaré inequality` -> `Poincaré 不等式`, and `Lax--Milgram theorem` -> `Lax--Milgram 定理`.
- Never alter names in bibliographies. Book-specific exact name records belong in `books/<book-id>/glossary/proper-names.tsv`.

## Chinese-body punctuation

- Chinese translated prose uses ASCII half-width punctuation only: `, . : ; ? ! () [] ...`.
- Forbidden in Chinese translated prose: `， 。 ： ； ？ ！ （ ） 【 】 ……`.
- Punctuation QA must not rewrite mathematics, LaTeX commands, labels, reference/citation keys, paths, URLs, BibTeX, code, raw templates, or source inputs.
- Punctuation QA must pass before a draft is reviewed.

## Cross-references and LaTeX

- Every referenceable chapter, section, subsection, theorem-like object, equation, figure, and table receives a unique stable semantic label independent of rendered numbering.
- Formula references use `\eqref`; other supported references use `\ref` unless the project adopts `cleveref` consistently.
- Never hard-code local object numbers. Record unavailable or uncertain targets in QA instead of guessing.
- Preserve the accepted `Theorem`, `Definition`, `Lemma`, `Proposition`, `Corollary`, `Proof`, `Example`, `Remark`, and `Exercise` environments and their established visual distinctions.
- Render those environment headings and object-reference prefixes in English exactly as `Theorem`, `Definition`, `Lemma`, `Proposition`, `Corollary`, `Proof`, `Example`, `Remark`, and `Exercise`; never translate an environment name into Chinese. This does not prevent translating the ordinary mathematical noun in Chinese prose when it is not functioning as an environment name or reference prefix.

## Supported block types

Use only: `chapter`, `section`, `subsection`, `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `proof`, `example`, `remark`, `exercise`, `equation`, `figure`, `table`, `footnote`, `ordinary-paragraph`, and `unknown`. Use `unknown` whenever classification is uncertain.
