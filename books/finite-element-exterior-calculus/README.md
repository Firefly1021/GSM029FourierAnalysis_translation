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
- 正式 PDF: [output/book-aljabr-zh.pdf](output/book-aljabr-zh.pdf).
- 原始 PDF: [input/source/](input/source/), 只读.
- 模板: [template/](template/), 只含 AJbook 的实际依赖、本书适配文件、字体和许可证.

所有正文文件均为可直接编辑的正式源码, 没有另一套需要同步的 generated 正文. 不要修改原始 PDF; 部分插图通过它直接引用, 因而它也是必要资源.

书目条目中的 `Cited on p. ...` 沿用原书印刷页码; 索引中的可点击引用定位本版相应对象.

## 重新编译

在本目录的终端执行:

```powershell
..\..\shared\scripts\mathbook.ps1 build-book finite-element-exterior-calculus
```

也可以打开共享工作区, 运行“编译所选书籍”并选择本书. 编译引擎为 XeLaTeX, 使用 TeX Live/latexmk 处理多轮引用和书目依赖.

编译按需写入忽略的 `.build/`, 不自动覆盖正式 PDF. 发布新版本前应检查公式、交叉引用、字体和排版; 检查后可清除 `.build/`.

## 字体与模板许可

字体与标题设置直接使用 AJbook 原文件. 附带的 Noto Sans CJK SC 字体位于 `template/fonts/noto-sans-cjk-sc/`, 许可证随字体保存. 其他字体依赖以 `template/font-setup-open.tex` 为准, 不以替代字体改变版式.

AJbook 作者为 Wen-Wei Li (李文威), 采用 CC BY 4.0. 原始许可证见 [template/LICENSE](template/LICENSE), 上游为 [AlJabr-1](https://github.com/wenweili/AlJabr-1). 本书适配文件仅衔接所需环境、原书编号和必要数学符号; 模板许可不改变原书及译文的权利归属.

封面根据该项目的 `coverpage.tex` 改编, 设计归属及 CC BY 4.0 许可保留. 中文书名使用随书附带的 Noto Serif CJK SC Bold, 作者区域沿用 Noto Sans CJK SC. 英文书名根据长度调整字号, 不沿用原书卷次、ISBN 或专属出版说明. 封面及其空白背页置于原书前置页之前, 不改变正文的页码和编号.

项目总说明见 [../../shared/README.md](../../shared/README.md). Git 在项目总目录统一管理, 不自动推送.
