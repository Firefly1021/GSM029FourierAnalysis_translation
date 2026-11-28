# 直立数学字母及算子修订验收

本记录是上一版的验收存档. 最新版已回到正式路径, 见 [整套数学字体修订验收](edition-revision-full-math-book.md).

- 按用户要求移除 Universitext 丛书页及随附的空白页, 出版信息页仍不印. 丛书页原译文归档为 `edition-omitted-series.tex`. 封面、目录、序言、参考文献和索引保留.
- 旧 PDF 逐字符检查: §3.3 的积分号为 `NewCMMath-Book`, 微分 d 为 `LMRoman12-Regular`; §3.4 同页 16 处正文 exp 采用 `LMRoman12-Regular` 或 `LMRoman8-Regular`.
- 只改本书的 LaTeX 导言区: 让 `\mathrm` 和 `\mathit` 取自数学字体, 并用 `\setoperatorfont{\symup}` 指定直立算子. 新 PDF 同处的 d、exp 和积分号均核实实际使用了 `NewCMMath-Book`. 不改中文或西文正文、公式输入、图内字体、模板或其他书.
- 新版 422 页, 第一章起于 PDF 第 11 页, 索引起于 PDF 第 406 页 (印刷第 396 页). 相对于上版, 576 个编号对象的 PDF 锚点与印刷页码均一致. 128 条目录、2,910 个内部链接、三处直接链接涉及的目标页及两个原书回链通过复核.
- 由空目录完成三轮 XeLaTeX. 无未定义引用、重复标签、缺字或溢出版心的警告. 抽查渲染 PDF 第 7、99、105 页. 原书 PDF、固定模板及已验收 §3.3 源码哈希均未变化.

新版 PDF `tex/build/main-upright.pdf` SHA-256: `b54c25d2e881086b12c2682fe859053ec26f152d4d71b279551ef894d0cf08f9`. 原路径 `tex/build/main.pdf` 被占用, 保留为上次构建版本.
