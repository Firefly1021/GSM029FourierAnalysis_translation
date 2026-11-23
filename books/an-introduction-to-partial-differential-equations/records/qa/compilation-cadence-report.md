# Current-chapter compilation policy

The user objected to one- or two-page translation batches causing repeated
whole-book builds. Routine per-unit whole-book compilation has been disabled;
the former operation now requires explicit `--compile-book` for integration.

The current-chapter preview uses the unchanged book preamble and original
pinned template. Only Chapter 10 body inputs are typeset. Other chapters supply
filtered external label data from the real latest integrated auxiliary file;
cross-chapter links target the sibling integrated PDF. No dummy anchors or
hard-coded reference numbers are substituted.

Verification on 2026-11-17:

- Chapter-only preview: 8 pages, rather than the 269-page evolving draft.
- TeX recorder confirms every chapter body input belongs to Chapter 10.
- Original PDF, templates, accepted/frozen inputs and integrated draft hashes
  are preserved by the existing guard and an additional pre/post build check.
- Initial chapter build took 19.58 seconds in this environment. An unchanged
  repeat took 0.59 seconds and latexmk reported Nothing to do. These are actual
  local observations, not a guaranteed speedup or benchmark.
- All preview pages were rendered and visually inspected. External PDF link
  paths and named destinations are also checked by the preview command.

Subsequent translation content is aggregated by subsection or approximately
10--20 source pages before chapter-only compilation. Block-level source,
formula, name, punctuation and reference registration checks continue without
typesetting. Clean whole-book builds and full link QA remain required at
chapter integration and final acceptance. Preview success is not full-book QA.
