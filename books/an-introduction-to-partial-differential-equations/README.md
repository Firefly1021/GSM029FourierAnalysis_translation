# An Introduction to Partial Differential Equations

Michael Renardy and Robert C. Rogers, Second Edition.

## 当前成果

全书翻译和最终技术 QA 已完成, 等待读者通读验收. 不是只完成样本或部分章节.

- 中文全书: [tex/build/book.pdf](tex/build/book.pdf), AJbook 版, 随本地编译更新.
- 完整可编辑入口: [tex/book.tex](tex/book.tex).
- 正文: `tex/chapters/chapter-*.tex`, 保持已有通过 QA 的文本, 不要重新生成覆盖.
- 卷首: `tex/chapters/front-matter.tex`.
- 完整原书参考文献: `tex/chapters/reference-appendix.tex`.
- 中文译本索引: `tex/chapters/source-index.tex`, 页码和链接随全书编译自动更新.
- 原始扫描: `input/source/An Introduction to Partial Differential Equations.pdf`.
- AJbook 模板: 本书 [template/](template/) 集中存放类文件、标题格式、封面样式、字体和适配文件. 纸张和版心在本书的 [ajbook-page-layout.sty](template/ajbook-page-layout.sty) 修改, 不写在译文中.
- 原 Mystyle 模板已停用并移出本书; `template/` 只保留现用 AJbook.

完成范围包括全部 12 章及习题, 丛书序言, 作者序言, 第二版说明,
自动目录, 附录 A 五组 62 条参考文献, 以及原书索引全部 300 个词条.
索引沿用原书词条顺序, 335 个定位链接显示当前中文译本页码并跳转到相应的
章节、定理、公式、习题或段落. 原书页码保留在
[原索引页码登记](../../shared/book-records/an-introduction-to-partial-differential-equations/structured/reviewed/source-index-locators.json)中, 不再作为译本索引页码显示.
正文引用仍使用实际的 LaTeX label/ref/eqref.

## 打开和编译

用 VS Code 打开本书文件夹, 修改 `tex/book.tex` 或它实际引用的分章文件.
唯一的全书编译入口是 **book.tex**。原样本正文已原样纳入第一章，不再提供独立样本入口。

本机需有 XeLaTeX, Biber 和 latexmk; Noto 字体随书提供. 在本书文件夹执行:

```powershell
$env:BIBINPUTS = "$(Resolve-Path 'tex');"
latexmk -cd -xelatex -interaction=nonstopmode -halt-on-error -outdir=build tex/book.tex
```

直接编译 `tex/book.tex` 时, PDF 和辅助文件放入 `tex/build/`; 不另设 `output/`. 清理辅助文件后, 下次编译会重新生成它们.
本书通过相对路径查找 `template/` 内的模板和随书 Noto 字体, 不依赖 `shared/` 中的其他模板.
AJbook 模板与封面设计来自 Wen-Wei Li 的 AlJabr-1, 按模板中的许可文件使用.

行间公式的间距统一由 [ajbook-pde-profile.sty](template/ajbook-pde-profile.sty) 管理.
正文与公式块之间的额外间距为 8pt. 两个直接相邻的公式块之间只加 3pt 的额外间距,
源码空行不再把它们撑开. 无须逐式改写环境或添加手工间距; 编号与交叉引用保持原样.

## QA 与原书问题

翻译验收依据为 [final-book-qa.json](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/final-book-qa.json) 和
[final-book-report.md](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/final-book-report.md)，历史日志在 `shared/book-records/an-introduction-to-partial-differential-equations/logs/`。
交付版整理及重新编译结果见 [delivery-cleanup.json](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/delivery-cleanup.json)。
AJbook 换版的编译和引用回归结果见 [ajbook-migration.json](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/ajbook-migration.json).
译本索引的页码、跳转核验及原书对照见 [translated-index-qa.json](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/translated-index-qa.json)
和 [translated-index-locators.json](../../shared/book-records/an-introduction-to-partial-differential-equations/qa/translated-index-locators.json).
早期批次 pending 报告作为历史保留, 不代表当前仍待翻译.

- 1,667 个编号公式位置, 包括原书本来为空的 9.192.
- 616 个定理类对象, 339 道 Problems.
- 1,436 处正文/序言引用解析通过, 207 个目录链接目标有效.
- 没有未定义生成引用, 重复标签, 新增缺字或溢出框.
- 没有新增姓名丢失或禁止的正文标点.
- 两处旧已验收输入含 `、`, 为避免覆盖已验收文本而明确保留; 最终 QA 列出位置.

原书的 refWHYP, 若干疑似误引, 扫描中缺失的曲线和可辨认的印刷公式异常
均保留并登记, 没有猜补或静默修正. Problem 1.16 按用户要求照原扫描保留.
原书两条不同文献重复使用 [La], 也按原书保留, 不改变正文 La 键的含义.

恢复后的英文 TeX 片段及双语 JSON 保存在 `shared/book-records/an-introduction-to-partial-differential-equations/structured/reviewed/`，
英文清单为 `book-restored-en-manifest.json`。页码映射在 `shared/book-records/an-introduction-to-partial-differential-equations/structured/source/`，
公式、术语及核验图像在 `shared/book-records/an-introduction-to-partial-differential-equations/formulae/`、`shared/book-records/an-introduction-to-partial-differential-equations/glossary/` 和 `shared/book-records/an-introduction-to-partial-differential-equations/evidence/`。
历史报告保留原路径，用 `shared/book-records/an-introduction-to-partial-differential-equations/path-map.json` 查找现位置。

## 固定规则

数学粗体用 `\bm`, 微分算子用 `\mathrm{d}`, 公式主体用 `\displaystyle`.
姓名保留原文, 环境标题保持英文, 中文正文使用英文半角标点.
不猜补公式, 不静默纠正原书, 不重新决定已有术语和排版.

本次索引更新未改写译文正文或公式, 只为需要定位的段落添加不可见的索引标签.
原始 PDF 未修改. 序言中的旧标题页已由 AJbook 封面取代.
原 350 页版归档在 `shared/book-records/an-introduction-to-partial-differential-equations/editions/mystyle/`.
全书仍在统一库 main 工作区内隔离保存. 本次更新未创建 Git 提交, 也未推送.
