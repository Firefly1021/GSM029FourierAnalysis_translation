# Mathematical book translation project rules

## Scope and phase control

- Phase 1 integrates and verifies the user-supplied LaTeX template. No source PDF is present.
- Do not create, infer, analyze, or translate a book until a source PDF is supplied and Phase 2 is explicitly started.
- Never fabricate inspection, extraction, OCR, formula, terminology, translation, compilation, or QA results.

## Read-only source material

- Everything under `input/template/` and any future content under `input/source/` is read-only source material.
- Never modify, overwrite, delete, rename, auto-format, or normalize user source files.
- Copy source files only into an isolated build or processing directory when required.
- Record suspected source errors in QA data; never silently correct them.
- Verify SHA-256 hashes before and after any workflow that reads source material.

## Mathematical accuracy

- Preserve every assumption, conclusion, condition, quantifier, and negation.
- Do not change necessity, sufficiency, implication direction, or logical strength.
- Do not add explanations that are absent from the source.
- Do not simplify, rewrite, normalize, or rederive formulas without explicit review authorization.

## Personal names

- Do not translate, transliterate, or transcribe natural-person names.
- Preserve the original language and writing system, accents, diacritics, hyphens, initials, abbreviations, spaces, capitalization, and name order exactly.
- Do not replace a name with a conventional Chinese rendering or expand information absent from the source.
- If the source gives only a surname or an abbreviation, preserve exactly that form.
- In eponymous mathematical terms, translate only the ordinary mathematical noun: `Hilbert space` -> `Hilbert 空间`, `Poincaré inequality` -> `Poincaré 不等式`, and `Lax--Milgram theorem` -> `Lax--Milgram 定理`.
- Never modify, translate, reorder, or expand author names in bibliographies.

## Formulas

- Every formula receives a stable ID.
- Preserve formula tokens, subscripts, superscripts, delimiters, signs, summation ranges, integration domains, numbers, labels, and references.
- Route uncertain formulas to manual review.
- Compilation success does not establish formula correctness.

## Terminology

- `glossary/terminology.tsv` is the terminology control file.
- Never mark an unconfirmed term as `approved`.
- The same English expression may have different translations in different mathematical contexts.
- Fluency must never override mathematical meaning.

## Supported document block types

Use only: `chapter`, `section`, `subsection`, `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `proof`, `example`, `remark`, `exercise`, `equation`, `figure`, `table`, `footnote`, `ordinary-paragraph`, and `unknown`. Use `unknown` whenever classification is uncertain.

## Template authority

- User `.sty` and `.cls` files are authoritative for visual style.
- User reference `.tex` files are authoritative for actual usage.
- Do not redefine user environments or design a competing visual style unless the user explicitly authorizes a translation-only override in `tex/translation-adapter.sty`; never edit the source template file itself.
- Put translation-only internal commands in `tex/translation-adapter.sty` or `tex/translation-macros.tex`, using project-specific names.

## Chinese-body punctuation

- Chinese prose in translations uses ASCII half-width punctuation only: `, . : ; ? ! () [] ...`.
- Do not use `， 。 ： ； ？ ！ （ ） 【 】 ……` in Chinese prose.
- Punctuation QA applies only to translated Chinese prose. It must not rewrite mathematics, LaTeX commands, labels, reference or citation keys, file paths, URLs, BibTeX data, code environments, raw template files, or source inputs.
- Translation generation must run the punctuation checker before a draft can be marked reviewed.

## Cross-references

- Every referenceable object in translated LaTeX receives a unique semantic label whose identity does not depend on the rendered number.
- Formula references use `\eqref`; theorem-like, chapter, section, subsection, figure, and table references use `\ref` unless the project later adopts `cleveref` consistently.
- Do not hard-code local object numbers in translated prose. Record unresolved external or unavailable targets in QA instead of guessing.
- User source files remain read-only. Explicitly authorized environment adaptations belong in `tex/translation-adapter.sty`.
