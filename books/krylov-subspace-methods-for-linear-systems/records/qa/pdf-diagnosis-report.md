# Source PDF diagnosis

234 pages: 232 native, 1 mixed (illustrated cover), 1 blank, 0 scanned. Per-page glyph count/size, fonts, image area, dimensions, rotation and extraction errors are recorded in pdf-diagnosis.json. Representative text layers were checked against rendered original pages.

Native mathematical extraction has damaged spacing, fractions, superscripts and delimiters. Strategy: native prose extraction plus visual mathematical reconstruction; no ordinary OCR is needed. Raw pypdf and pdfplumber text and positioned glyphs are retained separately.

## Mapping and outline

The complete page-map.json records all indices, PDF PageLabels and logical positions. The offset is not constant.

| Object | PDF page | Printed page |
| --- | --- | --- |
| Chapter 1 | 14 | 1 |
| Chapter 2 | 43 | 31 |
| Chapter 3 | 85 | 73 |
| Chapter 4 | 175 | 163 |
| Chapter 5 | 201 | 189 |
| Software | 222 | 211 |
| References | 223 | 213 |
| Index | 232 | 223 |
| Sample Section 1.8 | 32--36 | 19--23 |

PageLabels jump from 29 to 31 and have preliminary gaps and a duplicate ii label on a blank page. No missing mathematical content is inferred from pagination alone. A full-book pass should check chapter transitions.

The raw outline contains a damaged dash in a Gauss--Seidel heading. It is retained as raw evidence; visible source headings, rather than corrupted bookmarks, must control future translation.

The complete Section 1.8 sample ends before Section 1.9 on PDF 36. It includes two Definitions, one Proposition and Proof, one Remark, two tables, two footnotes, and 15 numbered equations. Other books were not used as content sources.
