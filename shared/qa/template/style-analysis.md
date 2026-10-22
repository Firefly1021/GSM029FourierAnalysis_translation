# Style analysis

- Style source: `template/style/Mystyle.sty`
- Document class used by the reference: `ctexart` with options `a4paper, UTF8, 12pt`
- Required engine: XeLaTeX (`fontspec` and `ctexart`; verified by isolated build)
- Bibliography: biblatex numeric style with Biber; resource `ref.bib`; URL fields use `\url`.
- Page: A4; geometry left 2.0cm, right 2.0cm, top 1.66cm, bottom 1.27cm.
- Page background: `sublight yellow`; the current style color names include `SectionColor` and `PageColor`.
- Page style: plain. `fancyhdr` is loaded but not configured, so no custom header or footer is defined.
- Formula numbering: reset within subsection. Inline math is globally forced to display style by `\everymath{\displaystyle}`.
- Hyperlinks: color links enabled; internal links black and citations blue.
- Explicit user font commands: none. The successful reference build selected the ctex Windows fontset and logged SimSun for CJK text.
- Index system: none configured; MakeIndex is not required by the reference.

## Packages

- `algorithm`
- `algpseudocode`
- `amsmath`
- `amssymb`
- `array`
- `biblatex` with options `backend=biber, style=numeric`
- `bm`
- `caption`
- `cases`
- `empheq`
- `enumitem`
- `esint`
- `fancyhdr`
- `float`
- `flowchart`
- `fontspec`
- `geometry`
- `graphicx`
- `hyperref` with options `colorlinks=true`
- `listings`
- `marvosym`
- `mathalpha` with options `scr=boondoxo`
- `mathrsfs`
- `mathtools`
- `multirow`
- `Mystyle`
- `pgfplots`
- `physics2`
- `stmaryrd`
- `subfigure`
- `tabularx`
- `tcolorbox` with options `most`
- `tikz`
- `url`
- `xcolor`
- `xparse`

## Custom commands and mathematical operators

All discovered definitions and reference usage counts are recorded in `style-commands.json`. Operator-style commands are: \curl, \diam, \im, \re, \sgn, \supp, \tr.

## Custom environments

- `Corollary`: 0 use(s) in the reference
- `Definition`: 0 use(s) in the reference
- `Example`: 0 use(s) in the reference
- `Exercise`: 0 use(s) in the reference
- `Lemma`: 0 use(s) in the reference
- `Proof`: 2 use(s) in the reference
- `Proposition`: 0 use(s) in the reference
- `Theorem`: 3 use(s) in the reference

The theorem-like environments share the section-scoped `statement` counter. The user style defines distinct visual treatments for theorem, definition, lemma, proposition, corollary, example, and exercise; the translation adapter preserves those distinctions while localizing headings and retaining referenceable counters.

## Section and contents behavior

The reference class is article-based and defines no chapter usage. Sections, subsections, and subsubsections are styled through `ctexset`, with colored numbers and black Chinese titles. The reference invokes `\tableofcontents`.

## Figures, tables, labels, and cross-references

Figure/table support is loaded through graphicx, float, subfigure, caption, array, multirow, and tabularx. The reference contains no active figure, table, label, ref, eqref, or autoref usage.

## External dependencies

The only active user auxiliary dependency is `ref.bib`. Commented `Section/...` input lines are not active dependencies. Installed package and tool resolution is recorded in `dependencies.md`.

## Observed usage issues

- None observed.
