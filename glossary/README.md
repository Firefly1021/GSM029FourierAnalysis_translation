# Glossary field definitions

The TSV files contain headers only until source material is supplied. No row may be invented to illustrate a field.

## `terminology.tsv`

- `Source Term`: exact source expression.
- `Chinese Translation`: controlled Chinese rendering; blank until proposed or confirmed.
- `Mathematical Context`: field or local context needed to disambiguate meaning.
- `Definition or Scope`: the controlled sense covered by the row.
- `Source Reference` and `First Occurrence`: traceability to source material.
- `Review Status`: `unreviewed`, `needs-review`, `approved`, or `rejected`.
- `Reviewer` and `Notes`: review provenance and non-source commentary.

## `proper-names.tsv`

- `Source Form` and `Canonical Form`: exact source spelling and the exact protected form.
- `Category`: person, organization, or another explicitly reviewed name class.
- `First Occurrence`: source location of the first occurrence.
- `Language or Script`: observed language or writing system without transliteration.
- `Preserve Exactly`: whether exact preservation is mandatory.
- `Review Status` and `Notes`: review state and recorded issues.

## `notation.tsv`

- `Source Notation` and `Canonical Notation`: original and controlled notation.
- `Meaning` and `Scope`: source-grounded meaning and range of applicability.
- `First Occurrence`, `Preserve Exactly`, `Review Status`, and `Notes`: traceability and review controls.

## `unresolved.tsv`

- `Item Type` and `Source Form`: unresolved item classification and exact source form.
- `Context` and `Source Location`: evidence needed for review.
- `Reason Unresolved` and `Proposed Action`: diagnosis and next review action.
- `Review Status` and `Notes`: current disposition and comments.

