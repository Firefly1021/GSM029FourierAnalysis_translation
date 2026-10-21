# Official Noto Sans CJK SC dependencies

Unmodified OTF files from https://github.com/notofonts/noto-cjk , tag `Sans2.004`, commit `523d033d6cb47f4a80c58a35753646f5c3608a78`, directory `Sans/OTF/SimplifiedChinese/`.

Regular, Bold, Medium and Black cover the exact family/weight requests in the original AJbook `font-setup-open.tex`. Do not replace these with Fandol or synthesize a weight. `manifest.json` records SHA-256, official Git blob identity, OpenType weight classes and scanned font names. The original SIL Open Font License 1.1 is retained in `LICENSE`; the font software is not modified.

The FEEC builder exposes this directory through a book-local Fontconfig configuration, so XeLaTeX finds the real original family without modifying TeX Live's global configuration. The original upstream font setup still intentionally uses Fandol for its Song/Kai/FangSong and other declared roles; retaining those is not a substitution for Noto.
