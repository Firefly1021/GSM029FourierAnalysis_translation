# 偏微分方程的数值逼近

原书: *Numerical Approximation of Partial Differential Equations*, Alfio Quarteroni and Alberto Valli.

本书从已有中译稿导入, 保留前言、三部分 14 章、参考文献及中文索引. 分章源稿位于 `tex/chapters/`; 原书图片位于 `tex/figures/images/`.

- [正式可编辑入口](tex/main.tex).
- [AJbook 版中文 PDF](tex/build/main.pdf).
- [中英文封面文字](tex/frontmatter/cover.tex).
- [本书 AJbook 模板](template/): 类文件、A4 版心、12 pt 字号、字体及封面样式与现有项目同版; `import-compatibility.sty` 仅适配原稿的命令、编号和编译依赖.
- [旧 ElegantBook 译本 PDF](../../shared/book-records/numerical-approximation-of-partial-differential-equations/editions/elegantbook/book-zh.pdf): 仅供对照, 不参与编译.
- [迁入核验](../../shared/book-records/numerical-approximation-of-partial-differential-equations/qa/ajbook-import.json).

## 编辑和编译

在 VS Code 中打开本书文件夹, 从 `tex/main.tex` 使用 XeLaTeX 编译. 推荐让 latexmk 调用所需的辅助工具. 在本书根目录执行:

```powershell
Push-Location tex
try {
    $env:BIBINPUTS = "$((Get-Location).Path);"
    latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
} finally {
    Pop-Location
}
```

直接编译时, PDF 和辅助文件写入 `tex/build/`; 不另设 `output/`. 封面和模板均从本书相对路径加载, 不依赖其他书籍.

迁入的是已有译稿, 未重译也未逐页对照英文原书. 正文中的 63 处图件直接选取 `input/source/` 内原书 PDF 的页面区域. 原书插图来自扫描, 保留原有清晰度. 编译时须保留该 PDF 的文件名和相对路径.

AJbook 类文件与封面设计出自 Wen-Wei Li 的 AlJabr-1, 许可见 [template/LICENSE](template/LICENSE).
