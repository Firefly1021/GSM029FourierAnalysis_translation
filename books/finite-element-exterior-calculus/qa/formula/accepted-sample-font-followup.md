# Accepted sample follow-up: wrong mathematical alphabet

Current status: blocking, explicit correction authorization required. This is an agent source-reconstruction error, not an original-book error.

While restoring Chapter 2's earlier definitions, inspection of the actual embedded source fonts established that the cycle and boundary letters are Fraktur. The original source uses TCWNOI+EUFM10 for Z on PDF 25 / printed 15 and for Z and B on PDF 26 / printed 16. Coordinates and affected deterministic formula IDs are in accepted-sample-font-followup.json. The installed primary amsfonts.sty definition maps mathfrak to the euf alphabet.

The previously accepted sample instead contains these three logical expressions:

| Current restored expression | Source-faithful correction proposed |
|---|---|
| `\mathcal Z_k` | `\mathfrak Z_k` |
| `\mathcal Z^k` | `\mathfrak Z^k` |
| `\mathcal B^k` | `\mathfrak B^k` |

They occur in the chain-map-induced-homology and cohomology-definition blocks. The exact source/translation equality test passed because both English reconstruction and Chinese used the same wrong transcription. Compilation likewise cannot detect a mathematically wrong source alphabet. This discovery supersedes the previous sample formula PASS for these symbols.

The proposed correction would update only the affected symbols consistently across authored bilingual source, reconstructed English, reviewed Chinese, structured/formula/notation records and compiled output. The correct mathcal H and mathcal S and all other prose, mathematical content, names, approved terminology and layout rules would remain unchanged. No such correction has yet been made: accepted content is immutable until the user authorizes it.

The new complete Preface and Chapter 1 have passed their own source-image, math, name, reference, punctuation, compilation and visual checks and remain committed. The sample TeX/PDF and its accepted source records have not been overwritten. Progress rows are not reset. Other books, shared code, shared glossary, original PDF and user template files are unchanged. No remote push was performed.

The global blocking gate now prevents automatic continuation into Chapter 2. Resume only after explicit approval of this narrowly scoped correction and successful source-font verification, updated mathematical records, clean multi-round compilation and visual regression.

## User decision superseding the historical blocker

The user instructed: 不要,只要不是Fraktur 字体就行. Current status: resolved as a user-approved presentation exception, not corrected to source Fraktur. Keep the accepted mathcal Z/B, source reconstruction and PDF unchanged. Original EUFM10 evidence above remains true and permanently recorded. Do not claim original glyph-family identity. Preserve semantic distinctions if additional alphabets occur. See config/math-alphabet-policy.json.
