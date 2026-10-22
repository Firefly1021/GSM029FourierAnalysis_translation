# Shared terminology library

`terminology.tsv` is the single authoritative cross-book terminology library. A book records only new candidates and unresolved terms below its own `books/<book-id>/glossary/` directory.

Promotion is keyed by `English + Domain + Context`, never by the English expression alone. Every accepted change is appended to `terminology-history.tsv`.
