# Frontmatter preface source QA

Status: passed for the preface on PDF pages 9--10 / printed pages v--vi.

- Compared the reconstructed English prose directly with the original 360-DPI scan images.
- Restored all scan-induced line-break hyphenation without removing source hyphens.
- Excluded running headers and printed page numbers from body text.
- Verified $H(\operatorname{div};\Omega)$ and $H(\operatorname{curl};\Omega)$ directly from the original scan.
- Preserved personal names, initials, accents, and the `Pierre-Arnaud` hyphen exactly.
- Recorded block-level page, bounding-box, source-image, and source-block provenance.
- PDF pages 11--14 are a table of contents. Their final Chinese text and page numbers must be generated from the reviewed chapter and section headings; they are not duplicated as ordinary body text.

The generated table of contents was integrated with the reviewed chapter and section headings and compiled successfully; the complete `frontmatter` source QA passed.
