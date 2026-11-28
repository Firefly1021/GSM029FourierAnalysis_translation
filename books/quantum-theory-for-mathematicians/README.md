# 数学家的量子理论

原书: *Quantum Theory for Mathematicians*, Brian C. Hall.

本书从已有中译稿导入, 保留前言、23 章、附录 A、参考文献及中文索引. 前言在主文件内, 其余源稿位于 `tex/chapters/`, 图片位于 `tex/figures/`, BibTeX 位于 `tex/reference.bib`. 现用版与《偏微分方程引论》共用数学字体配置, 不再单独加载 New Computer Modern; 公式源码未改.

- [正式可编辑入口](tex/main.tex).
- [AJbook 版中文 PDF](tex/build/main.pdf).
- [中英文封面文字](tex/frontmatter/cover.tex).
- [本书 AJbook 模板](template/): 类文件、A4 版心、12 pt 字号、字体及封面样式与现有项目同版; `import-compatibility.sty` 仅适配原稿的命令、编号和编译依赖.
- [旧 ElegantBook 译本 PDF](../../shared/book-records/quantum-theory-for-mathematicians/editions/elegantbook/book-zh.pdf): 仅供对照, 不参与编译.
- [迁入核验](../../shared/book-records/quantum-theory-for-mathematicians/qa/ajbook-import.json).
- [统一版式核验](../../shared/book-records/quantum-theory-for-mathematicians/qa/pde-typography-20261122.json).

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

迁入的是已有译稿, 未重译也未逐页对照英文原书. 正文中的 30 处插图直接选取 `input/source/` 内原书 PDF 的页面区域. 原图是矢量的部分保持矢量. 编译时须保留该 PDF 的文件名和相对路径.

AJbook 类文件与封面设计出自 Wen-Wei Li 的 AlJabr-1, 许可见 [template/LICENSE](template/LICENSE).
