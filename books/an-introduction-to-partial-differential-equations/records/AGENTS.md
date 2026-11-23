# Book-specific typography

Read ../../shared/AGENTS.md and ../AGENTS.md. This book remains in the unified
library, with all book-specific writes contained by BookPaths.

The user selected `\bm{...}` for mathematical bold on 2026-11-15. Use it for
bold vectors, matrices and other source-bold mathematical objects, rather than
`\mathbf` or `\boldsymbol`. Preserve the source's distinction between bold and
non-bold symbols. Keep scalar subscripts outside the bold command unless the
source explicitly makes them bold: `\bm{y}_0`. Preserve hats and other accents.
This is an authorized typography choice, not permission to change mathematics.

Do not replace `\mathbb`, `\mathcal`, or prose `\textbf` with `\bm`. The pinned
Mystyle already loads bm; leave all original template files unchanged. Record
the same bold convention in restored English, translated TeX and formula data.

The user additionally selected upright differential operators `\mathrm{d}` and
display style on 2026-11-15. Write `\mathrm{d}t`, `\mathrm{d}s` and
`\frac{\mathrm{d}y}{\mathrm{d}t}`; do not change an ordinary variable named d,
partial derivatives, domains or limits. Set formula-body style to `\displaystyle`
in both inline and display mathematics. Do not locally force `\textstyle`.
Use `\dfrac` for fractions inside matrices and cases as well, since those inner
environments otherwise choose smaller fractions. Superscripts and subscripts
retain their normal TeX sizing; do not force display style into scripts.

The user approved the revised sample and authorized formal translation on
2026-11-15 ("现在可以了,接下来进行正式的任务"). Proceed through the remaining
natural units. Reuse the accepted sample without rewriting its content. Retain
its standalone PDF and source. New batches require scan-based English
restoration, provenance, formula/name/punctuation/reference QA, clean compilation
and visual review. Do not alter other books or original templates or push.
