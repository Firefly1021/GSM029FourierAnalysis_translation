# Terminology schema

The shared TSV columns are:

1. `English`: exact source expression.
2. `Preferred Chinese`: controlled target form.
3. `Domain`: mathematical field used to separate domain-specific meanings.
4. `Context`: narrower semantic or usage context.
5. `Forbidden Alternatives`: forms that must not be substituted in this context.
6. `Status`: `approved`, `proposed`, `ambiguous`, `rejected`, or `needs-review`.
7. `First Source` and `First Location`: provenance of the first registration.
8. `Last Verified Source` and `Last Verified Location`: latest verification provenance.
9. `Notes`: constraints and review evidence.

An automatic promotion requires a complete `proposed` candidate whose notes contain `[safe-to-promote]`. Duplicate and domain/context conflict checks still run before promotion. Ambiguous or conflicting candidates remain `needs-review`; existing approved rows are never overwritten.
