# 偏微分方程的数值逼近

原书: *Numerical Approximation of Partial Differential Equations*, Alfio Quarteroni and Alberto Valli.

本书从已有中译稿导入, 保留前言、三部分 14 章、参考文献及中文索引. 分章源稿位于 `tex/chapters/`; 原书图片位于 `tex/figures/images/`.

- [正式可编辑入口](tex/main.tex).
- [AJbook 版中文 PDF](output/book-zh.pdf).
- [中英文封面文字](tex/frontmatter/cover.tex).
- [本书 AJbook 模板](template/): 类文件、A4 版心、12 pt 字号、字体及封面样式与现有项目同版; `import-compatibility.sty` 仅适配原稿的命令、编号和编译依赖.
- [旧 ElegantBook 译本 PDF](records/editions/elegantbook/book-zh.pdf): 仅供对照, 不参与编译.
- [迁入核验](records/qa/ajbook-import.json).

## 编辑和编译

在 VS Code 中打开本书文件夹, 从 `tex/main.tex` 使用 XeLaTeX 编译. 推荐让 latexmk 调用所需的辅助工具. 在本书根目录执行:

```powershell
Push-Location tex
try {
    $env:BIBINPUTS = "$((Get-Location).Path);"
    latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../.build main.tex
} finally {
    Pop-Location
}
```

本地重新编译写入 `.build/`, 不会自动覆盖 `output/` 中的正式 PDF. 封面和模板均从本书相对路径加载, 不依赖其他书籍.

迁入的是已有译稿, 未重译也未逐页对照英文原书. 迁入项目未附原书英文 PDF, `input/source/` 预留; 英文源文件登记前请用本页的直接编译方式. AJbook 类文件与封面设计出自 Wen-Wei Li 的 AlJabr-1, 许可见 [template/LICENSE](template/LICENSE).
