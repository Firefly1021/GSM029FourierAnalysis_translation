# Whole-PDF inspection

- Source: `input/source/GSM029 - Fourier Analysis.pdf`
- Pages inspected individually: 228
- Per-page classifications: {'mixed': 224, 'uncertain': 1, 'scanned': 3}
- Dominant page size: 510.0 x 804.0 pt (228 pages)
- Rotation: Counter({0: 228})
- Column heuristic: {'single': 224, 'uncertain': 4}
- Pages recommended for body OCR or OCR verification: 3
- Problem records: 5 (four visually blank interstitial pages and one blocking source-tail omission)

The PDF is a scanned-image publication with a hidden OCR text layer on many pages. Classification was performed page by page; no whole-file shortcut was used. Ordinary OCR output is not treated as final formula LaTeX. Formula density and column count are heuristics and are visually checked for the selected sample.

The three pages classified as `scanned` contain no text layer and were visually confirmed as blank interstitial pages; OCR is therefore unnecessary for them. Mixed pages retain both hidden OCR and rendered images. Detailed per-page metrics, fonts, image counts, header/footer candidates, footnote/marginal-note indicators, and anomalies are in `qa/pdf-inspection.json`.
