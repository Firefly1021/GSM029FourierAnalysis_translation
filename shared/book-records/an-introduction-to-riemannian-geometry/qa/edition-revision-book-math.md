# 正式版修订验收

本报告为上一次正式版存档. 最新版本见 [直立数学字母及算子修订验收](edition-revision-upright-math.md).

- 按用户要求移除“出版信息”页及它对应的空白对开页. 封面、Universitext 丛书页、序言和各章参考文献保留. 已排除的出版信息译文保存在本目录的 `edition-omitted-publication.tex`, 不参与编译.
- 正文数学使用 TeX Live 的 `NewCMMath-Book.otf`. 在正式 PDF 页面字体资源中核实了 `NewCMMath-Book-Identity-H`, 无 Regular 正文数学资源. 不改插图内部字体、正文文字或固定 AJbook 模板.
- 正式 PDF 共 424 页. 第一章自 PDF 第 13 页起. 索引自 PDF 第 408 页起, 印刷页码仍为 396. 更换字重前后 667 个抽取到的语义标签编号及印刷页码保持一致.
- 从干净目录完成三轮 XeLaTeX. 128 条目录、2,910 个内部链接以及两个已知的原书回链均检查通过. 未发现未定义引用、重复标签、缺字或超出版心的警告. 已渲染复核序言、第 3.3 节和索引首页.
- 英文源 PDF、模板和已验收 §3.3 源文的哈希保持不变.

本版 `tex/build/main.pdf` 的 SHA-256: `fdc30ad6e1b2e3becab819e710796f95236363cfd9024a5f4afb5db4179b610e`.
