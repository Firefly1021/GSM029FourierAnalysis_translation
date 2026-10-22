# Book translation plan

The source contains nine mathematical chapters. Complete chapters are the preferred batches; Chapter 8 may be divided at complete section boundaries because it spans 38 PDF pages. A batch may never end inside a theorem-like environment, proof, formula group, figure/table with caption, footnote, or continuous enumeration.

| Unit | PDF pages | Printed pages | Planned output | Notes |
|---|---:|---:|---|---|
| Chapter 1 | 13--36 | 1--24 | `tex/chapters/chapter-01.tex` | Completed; QA and cumulative build passed |
| Chapter 2 | 37--59 | 25--47 | `tex/chapters/chapter-02.tex` | Active; preserve accepted PDF 37--51 wording and translate only 52--59 |
| Chapter 3 | 61--80 | 49--68 | `tex/chapters/chapter-03.tex` | PDF 60 is a blank interstitial page |
| Chapter 4 | 81--102 | 69--90 | `tex/chapters/chapter-04.tex` | Chapter number visually confirmed in prior diagnosis |
| Chapter 5 | 103--126 | 91--114 | `tex/chapters/chapter-05.tex` | Complete chapter batch |
| Chapter 6 | 127--144 | 115--132 | `tex/chapters/chapter-06.tex` | Complete chapter batch |
| Chapter 7 | 145--168 | 133--156 | `tex/chapters/chapter-07.tex` | Chapter number visually confirmed in prior diagnosis |
| Chapter 8 | 169--206 | 157--194 | `tex/chapters/chapter-08.tex` plus section files if required | Split only at section boundaries |
| Chapter 9 | 207--228 | 195--216 | `tex/chapters/chapter-09.tex` | Last supplied body page |
| Front matter | 1--12 | roman | `tex/frontmatter.tex` | Title, contents, preface, preliminaries; process after chapter workflow stabilizes |
| Bibliography | absent | 217 onward | pending | Blocking source omission |
| Index | absent | 219 onward | pending | Blocking source omission; regenerate page numbers only after final layout |

Every completed batch produces `qa/translation/<batch-id>-report.md`. Progress is recorded in `qa/chapter-progress.tsv`.
