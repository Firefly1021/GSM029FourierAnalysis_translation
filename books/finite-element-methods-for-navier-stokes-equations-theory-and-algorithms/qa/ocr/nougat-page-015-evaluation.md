# Nougat auxiliary OCR evaluation: PDF page 15

Status: useful auxiliary source; not authoritative and not source-QA approved by itself.

## Correctly improved over ordinary OCR

- Recovered `\Omega`, `\Gamma`, `\mathbb{R}^{N}`, `\mathcal{D}`, `\operatorname{div}`, and `\operatorname{curl}`-style mathematical typography far more reliably than the hidden OCR.
- Reconstructed complete prose paragraphs and removed scan-induced line-break hyphenation.
- Recovered the displayed duality-pairing formula in a usable LaTeX candidate form.
- Excluded the printed page number from body text.

## Mismatches found by original-scan comparison

- Dropped the accent from `Nečas`.
- Misclassified or normalized source numbering in the heading hierarchy; final numbering must come from the book structure and semantic labels.
- Dropped the prime from `\mathcal{D}'(\Omega)` in the distribution-space sentence and in the corresponding duality-pairing description.
- The first `\mathcal{D}` display requires direct scan review for the overbar on `\Omega`; it must not be silently normalized from mathematical expectation.

## Decision

Nougat output may be used as a second OCR candidate to accelerate prose and formula comparison. Every formula, personal name, heading number, and cross-reference remains subject to direct verification against the original scan. The accepted representative sample remains unchanged.
