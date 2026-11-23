# Phase 1 completion report

## 1. Template file inventory

All files under `input/template/` are recorded with type, size, and SHA-256 in `qa/template/template-manifest.json`. The substantive user files are:

- `input/template/style/Mystyle.sty` — `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`
- `input/template/reference/main.tex` — `1a5871f7df88fc861cfe01f674460052d8f4446143fb638f688ac5f8c2f5e925`
- `input/template/assets/ref.bib` — `89b952edcb3192ec7eaa210bd962c3d4fae05f885b525a2ab61257669b41a25f`

The reference directory contains exactly one `.tex` file, so no ambiguous candidate selection occurred. Final verification confirmed that every recorded template hash remained unchanged.

## 2. Template compilation method

- Document class: `ctexart` with `a4paper,UTF8,12pt`.
- Build driver: `latexmk` 4.86a.
- Engine: XeLaTeX from TeX Live 2025.
- Bibliography system: `biblatex` numeric style with Biber.
- Index system: none configured; MakeIndex was not required.
- Result: success, exit code 0, six-page PDF generated from an isolated copy.
- Adapter smoke test: success, exit code 0, one-page PDF containing only an explicit template-test notice.

The reference build reported non-blocking warnings: `stmaryrd` has no requested bold font shape and substituted its regular shape; one paragraph produced a 7.09236pt overfull hbox. These warnings were recorded and no user file was changed to suppress them.

The bundled LaTeX doctor smoke test timed out before returning JSON. The bundled compile wrapper invoked the toolchain and produced a PDF but then failed while decoding TeX output as GBK. Direct `latexmk -xelatex` verification succeeded, so the wrapper failures are recorded as tool-wrapper issues rather than template failures.

## 3. Available commands and environment

The CLI supports `status`, `inspect-template`, `verify-template`, `compile-template`, `validate-project`, `inspect-pdf`, `render`, `extract`, `structure`, `terminology`, `check-names`, `translate`, `qa`, and `compile`.

Detected TeX tools: `latexmk`, `xelatex`, `lualatex`, `pdflatex`, `biber`, `bibtex`, `makeindex`, and `kpsewhich`. Full paths are recorded in `qa/template/dependencies.md`.

GNU Make is not installed in the current Windows environment. The attempted `make inspect-template` command could not start for that reason. The commands behind all five required Make targets were run directly and passed; the checked-in Makefile remains ready for an environment with Make.

## 4. Missing dependencies

No template class, package, bibliography asset, font command dependency, or active external input is missing in the detected TeX Live environment. Commented `Section/...` input lines in the reference are not active dependencies.

## 5. Translation rules established

`AGENTS.md` now defines source immutability, mathematical-accuracy, name-preservation, formula, terminology, supported-environment, and template-authority rules. `style/chinese-mathematical-style.md` defines Simplified Chinese mathematical prose, logical connectives, modality, quantifiers, punctuation and formulas, sentence splitting, cross-references, footnotes, bibliography handling, exact personal-name preservation, and prohibitions against added explanation or silent correction.

The four TSV files contain formal headers only; their field definitions are documented in `glossary/README.md`. No terminology or name entry was invented.

## 6. Personal-name protection tests

Tests passed for exact preservation, accents and diacritics, hyphens, initials, abbreviations, and spacing. Tests also confirmed that only the ordinary mathematical noun is translated in the explicitly required eponym examples while the personal-name portion remains unchanged.

## 7. Generic program status

Implemented components include project/config validation, template input validation, manifests and hashes, conservative LaTeX command/environment analysis, dependency resolution, isolated compilation, PDF-kind and renderer protocols, text/layout extraction protocols, stable formula registration, structure classification, terminology records, exact name checks, translation-block interfaces, LaTeX emission/conflict checks, QA issue recording, scripts, and CLI routing.

No concrete PDF inspection, rendering, OCR, extraction, structure inference, terminology extraction, translation, book QA, or final book compilation was run. Without a source PDF, every related CLI command returns exactly `Source PDF has not been supplied. Phase 2 cannot begin.`

## 8. Test results

- Unit tests: 19 passed, 0 failed.
- Python syntax compilation: passed.
- Project/config/Schema validation: passed.
- Reference template compilation: passed.
- Adapter minimal compilation: passed.
- Template SHA-256 integrity verification after all reads and builds: passed.
- Required Make invocations: not runnable because GNU Make is absent; equivalent target commands passed directly.

## 9. PDF-related functions not executed

All Phase 2 operations remain unexecuted: PDF type inspection, page rendering, native/scanned/mixed extraction, OCR, layout extraction, formula extraction/registration from a source, structure classification, terminology extraction, name checking against a source, translation, translation QA, and final book compilation.

## 10. Next command after the user supplies the PDF

After placing exactly one PDF in `input/source/` and installing the project or setting `PYTHONPATH=src`, run:

```text
python -m mathbook inspect-pdf
```
