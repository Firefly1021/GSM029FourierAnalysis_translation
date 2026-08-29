# Representative sample restoration report

- Sample range: PDF 37--55 / printed 23--41.
- Continuous PDF pages: 19.
- Scan-good sample pages: 15.
- Scan-medium sample pages: 4 (PDF 46, 47, 48, 50).
- Scan-poor sample pages: 0; all scan-poor pages are non-body material, while the sample deliberately includes four medium-quality body pages.
- Rendering: 360 DPI PNG derivatives; the source PDF was not modified.
- Derivative variants per sample page: original, grayscale, contrast-enhanced, OCR-optimized, and formula-optimized.
- Geometric changes: none; measured sample skew did not justify deskewing.
- Binarization: none.
- Denoising: none.
- Cropping/border removal: none for OCR pages; only two figure derivatives were cropped for LaTeX inclusion.
- OCR: hidden overlay retained as navigation evidence and RapidOCR run independently on OCR-optimized derivatives.
- Mathematics: separated from prose OCR; formula crops and token-level reconstruction are stored independently.
- Reconstructed source blocks: 681.
- High-confidence source blocks: 511.
- Medium-confidence source blocks: 170.
- Low-confidence source blocks: 0.
- Heading blocks: 27.
- Ordinary-prose blocks: 237.
- Equation/math-region blocks: 417.

## Provenance

Each restored block records its PDF page, printed page, bounding box, OCR source, image source, kind, confidence, and review status in `structured/restored-source/sample-source-blocks.jsonl`.

## Result

The sample restoration stage is complete. Raw OCR is not treated as reconstructed source and is not used directly as the translation authority.
