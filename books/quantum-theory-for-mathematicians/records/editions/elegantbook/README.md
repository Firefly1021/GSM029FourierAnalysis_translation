# Quantum Theory for Mathematicians 中文 ElegantBook 工程

源书:`C:\Users\Administrator\Downloads\Quantum Theory for Mathematicians(Brian C. Hall).pdf`

编译入口:`src/main.tex`;ElegantBook 类文件与原始参考文献也位于 `src/`.

工程约定:正文 11pt;中文使用 ElegantBook 的 `lang=cn` 原生设置;正文图片全部从 `src/figures/` 读取;数学字体显式设置为 New Computer Modern;章节、定理类环境、公式、图和索引均使用可跳转标签.

建议在包含 `src/main.tex` 的目录中用 XeLaTeX 编译:

```text
cd src
xelatex -interaction=nonstopmode main.tex
biber main
makeindex main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

若使用 `latexmk`,应确保它调用 XeLaTeX,并把 `biber` 与 `makeindex` 纳入构建流程.最终 PDF 应使用 XeLaTeX 运行环境中可用的中文字体、TeX Gyre 正文字体和 New Computer Modern 数学字体;交付前可用 `pdffonts main.pdf` 检查字体是否嵌入.源文件包不包含 `.aux`、`.log`、`.bbl`、`.bcf`、`.idx` 等缓存文件.

封面图 `src/figures/cover-quantum.png` 已校验为 RGB、1536×1024(3:2),并通过 `\cover{figures/cover-quantum.png}` 替换模板默认封面图.

术语统一规则见 `TERMINOLOGY.md`.章节译稿在 `src/chapters/`,图片均在 `src/figures/`,输出目录预留给最终 PDF 与源码图片压缩包.

## 当前构建状态

译稿、章节结构、标签与交叉引用已经完成静态审计,并已用 XeLaTeX、Biber 和 MakeIndex 完整编译.最终 PDF 共 349 页;PDF 中的中文字体、正文/数学字体均已嵌入,封面图为 RGB、1536×1024(3:2).交付的源码压缩包只包含 `.tex`、`.cls`、`.bib`、术语说明和 `figures/` 图片,不包含编译缓存、临时渲染图或 PDF.
