# Riemann 几何引论

Leonor Godinho 和 José Natário 著. 全书翻译及验收已完成.

- [正式 PDF](tex/build/main.pdf) (420 页，已修正目录和序言；整套正文数学字体为 New Computer Modern Math Book)
- [LaTeX 主文件](tex/main.tex)；正文位于 `tex/chapters/`，插图位于 `tex/figures/`
- [全书验收报告](../../shared/book-records/an-introduction-to-riemannian-geometry/qa/whole-book-acceptance.md)

直接用 VS Code 打开本书目录并编辑 `tex/main.tex` 或对应章节. 从 `tex/` 目录编译:

```powershell
latexmk -xelatex -synctex=1 -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

原始英文 PDF 位于 `input/source/`，本书使用的 AJbook 模板位于 `template/`. 保持 PDF 在 `tex/build/`，以便两条保留的原书引用能够打开正确的相对路径.
