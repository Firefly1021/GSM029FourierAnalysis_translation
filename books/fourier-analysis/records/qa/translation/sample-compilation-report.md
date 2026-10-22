# Sample compilation report

## Result

- Status: **success**.
- Entry file: `tex/sample-main.tex`.
- Sample content: `tex/chapters/sample.tex`.
- Output: `output/sample-translation.pdf`.
- Engine: XeLaTeX through TeX Live; two explicit clean-build passes followed by final PDF generation.
- Output pages: 12.
- Output size: 206,194 bytes.
- Output SHA-256: `fdc341730a68ca37eb777ad95ef942a95ae3f1815dcd7aacf8dc6d27803e1f3f`.
- User style loaded unchanged from `input/template/style/Mystyle.sty`; authorized presentation changes load afterward from `tex/translation-adapter.sty`.

## Diagnostics

- Undefined references: 0.
- Multiply-defined labels: 0.
- Duplicate PDF destinations: 0.
- Semantic label number mismatches: 0.
- Named PDF destinations: 75.
- Link annotations: 42.
- Equation destinations: 12.
- Theorem-counter destinations: 16.

The final transcript is preserved in `logs/sample-compilation.log` and the complete regression transcript in `logs/xref-regression-compilation.log`.

## Warnings

- The supplied style requests a bold `stmry` font shape that is unavailable; TeX substitutes the regular shape.
- Hyperref removes math tokens from two PDF bookmarks whose subsection titles contain mathematical notation.
- No warning affects label resolution or page layout.

## Visual QA

All 12 output pages were rendered to `qa/translation/rendered-xref/` and visually inspected. Theorem titles are inline and referenceable, boxes can break across pages, formulas retain their generated numbers, and no clipping was observed.
