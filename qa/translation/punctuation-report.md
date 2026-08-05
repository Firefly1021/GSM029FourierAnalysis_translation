# Chinese-prose punctuation report

- File: `tex/chapters/sample.tex`
- Scope: translated Chinese prose only; math, comments, code, LaTeX reference commands and their keys are protected.
- Forbidden occurrences before normalization: 0
- Forbidden occurrences after normalization: 0
- Automatic normalization requested: No
- Rule sources: `AGENTS.md`, `style/chinese-mathematical-style.md`, and `config/translation.yaml`.
- Automated checker: `scripts/check_punctuation.py` using protected-region logic from `src/mathbook/qa.py`.
- Protected from rewriting: mathematics, LaTeX commands and keys, labels, reference keys, paths, URLs, comments, and code-like environments.

## Replacements

- None.

## Result

Pass.

The initial repair normalized 419 forbidden full-width punctuation occurrences in translated prose. The final independent scan found zero remaining translated-prose violations. Full-width punctuation that is part of protected mathematical content is intentionally unchanged.
