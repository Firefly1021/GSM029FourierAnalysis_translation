# 《不可压缩流问题的有限元方法》中文版

本工程包含全书简体中文 LaTeX 源稿,使用 ElegantBook v4.7 类文件、原书图稿和英文参考文献数据.译文从前言开始,覆盖第 1–9 章、附录 A–D 和中文索引;出版信息未译,参考文献保留英文.

## 文件结构

- `main.tex`:主文件.
- `chapters/`、`appendices/`:分章和附录源文件.
- `figures/`:原书图稿.
- `references/references.bib`:参考文献数据.
- `elegantbook.cls`、`cover.png`:模板类文件和替换封面图.
- `TERMS.md`:术语表.

## 编译

需要 XeLaTeX、Biber、MakeIndex、ElegantBook 所需宏包,以及 SimSun、SimHei、KaiTi、FangSong 等中文字体.Windows 下可使用 MiKTeX 或 TeX Live.在项目目录的 PowerShell 中执行:

```powershell
New-Item -ItemType Directory -Force build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
biber --input-directory build --output-directory build main
makeindex -o build/main.ind build/main.idx
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

最终 PDF 采用 11pt 正文字号和约 155 × 241 mm 页面.字体已嵌入 PDF,阅读时不要求设备另装这些字体;重新编译源文件时仍需安装相应字体和 TeX 工具.
