# Mathematical Book English-to-Chinese Translation Project

Phase 1 integrates and verifies the user-supplied LaTeX template. No source PDF has been supplied, and no book analysis or translation has started.

## Read-only inputs

- Template `.sty` or `.cls`: `input/template/style/`
- Reference `.tex`: `input/template/reference/`
- Reference images, `.bib`, fonts, and auxiliary files: `input/template/assets/`
- Future source PDF: `input/source/`

Everything below `input/template/` and `input/source/` is treated as read-only. Commands copy files into isolated temporary directories when compilation or processing is required.

## Environment

The Python implementation has no third-party runtime dependency. From a development checkout, either install the package with `python -m pip install -e .` or set `PYTHONPATH=src`. Template compilation requires the TeX tools identified in `qa/template/dependencies.md`.

## Commands

```text
python -m mathbook status
python -m mathbook inspect-template
python -m mathbook verify-template
python -m mathbook compile-template
python -m mathbook validate-project
python -m mathbook inspect-pdf
python -m mathbook render
python -m mathbook extract
python -m mathbook structure
python -m mathbook terminology
python -m mathbook check-names
python -m mathbook translate
python -m mathbook qa
python -m mathbook compile
```

Until a source PDF is supplied, every PDF-dependent command exits safely with:

```text
Source PDF has not been supplied. Phase 2 cannot begin.
```

## Make targets

`make test`, `make lint`, `make inspect-template`, `make verify-template`, and `make compile-template` perform the Phase 1 checks.

