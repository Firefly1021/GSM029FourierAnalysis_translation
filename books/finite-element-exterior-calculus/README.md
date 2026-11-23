# Finite Element Exterior Calculus

本目录只使用 AJbook, 正式入口为 `tex/main.tex`.

## 修改与阅读

- 正式主入口: [tex/main.tex](tex/main.tex).
- 正文: [tex/chapters/](tex/chapters/). 修改句子、符号和段落时直接编辑这里的文件.
- 前置页及前言: [tex/frontmatter/](tex/frontmatter/).
- 封面: [tex/frontmatter/cover.tex](tex/frontmatter/cover.tex), 沿用 AJbook 原书封面的字体、构图和装饰, 替换为本书书名与作者.
- 参考文献和索引: [tex/backmatter/](tex/backmatter/).
- 本书必要的数学符号宏: [tex/macros.tex](tex/macros.tex).
- 图片: [tex/figures/](tex/figures/). 不要删除主文件仍引用的宏、图片或文献.
- 编译生成的 PDF: [tex/build/main.pdf](tex/build/main.pdf).
- 原始 PDF: [input/source/](input/source/), 只读.
- AJbook 模板: 本书 [template/](template/) 集中存放类文件、标题格式、封面样式、字体和适配文件. 纸张和版心在本书的 [ajbook-page-layout.sty](template/ajbook-page-layout.sty) 修改, 不写在译文中.

所有正文文件均为可直接编辑的正式源码, 没有另一套需要同步的 generated 正文. 不要修改原始 PDF; 部分插图通过它直接引用, 因而它也是必要资源.

书目条目中的 `Cited on p. ...` 沿用原书印刷页码; 索引中的可点击引用定位本版相应对象.

## 重新编译

直接用 VS Code 打开本书文件夹, 从 `tex/main.tex` 使用 XeLaTeX 或 LaTeXmk(XeLaTeX) 编译. 主文件通过相对路径加载本书 `template/` 内的模板和随书 Noto 字体, 无需全局安装模板或字体.

所有编译产物统一放在 `tex/build/`: PDF、日志、辅助文件、目录和 SyncTeX 文件均属于这里. 不再使用 `output/` 或 `.build/`. 编译生成的 PDF 为 `tex/build/main.pdf`, 再次编译会更新它; 原始 PDF 位于 `input/source/`, 不会被覆盖.

本次旧目录删除被执行环境安全策略阻止, `output/` 和 `.build/` 暂时仍在磁盘上, 不再是有效编译或 PDF 入口. 当前 PDF 已校验复制到 `tex/build/main.pdf`, 清理这两个旧目录前请确认该文件存在.

也可以选择共享构建入口. 在本目录的终端执行:

```powershell
..\..\shared\scripts\mathbook.ps1 build-book finite-element-exterior-calculus
```

也可以打开共享工作区, 运行“编译所选书籍”并选择本书. 编译引擎为 XeLaTeX, 使用 TeX Live/latexmk 处理多轮引用和书目依赖.

共享构建也只在 `tex/build/` 内生成候选文件, 不会重建 `output/` 或 `.build/`. 发布新版本前应检查公式、交叉引用、字体和排版.

## 字体与模板许可

编译使用 `template/fonts/` 中的随书 Noto 字体, 无需另装. `template/` 只保留现用 AJbook.

AJbook 作者为 Wen-Wei Li (李文威), 采用 CC BY 4.0. 原始许可证见 [template/LICENSE](template/LICENSE), 上游为 [AlJabr-1](https://github.com/wenweili/AlJabr-1). 本书适配文件仅衔接所需环境、原书编号和必要数学符号; 模板许可不改变原书及译文的权利归属.

封面根据该项目的 `coverpage.tex` 改编, 设计归属及 CC BY 4.0 许可保留. 中文书名使用随书附带的 Noto Serif CJK SC Bold, 作者区域沿用 Noto Sans CJK SC. 英文书名根据长度调整字号, 不沿用原书卷次、ISBN 或专属出版说明. 封面及其空白背页置于原书前置页之前, 不改变正文的页码和编号.

项目总说明见 [../../shared/README.md](../../shared/README.md). Git 在项目总目录统一管理, 不自动推送.
