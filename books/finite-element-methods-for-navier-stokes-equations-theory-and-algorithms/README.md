# Finite Element Methods for Navier-Stokes Equations: Theory and Algorithms

这是本书的成品编辑目录. 用 VS Code 打开本目录即可. 不需要接触原来的翻译流程目录.

## 修改与阅读

- 正式主入口: [tex/full-book.tex](tex/full-book.tex).
- 当前版本的正文: [tex/chapters/](tex/chapters/). 修改句子、符号和段落时从这里进入.
- 图片: [tex/figures/](tex/figures/). 不要删除主文件仍引用的宏、图片或文献.
- 编译生成的 PDF: [tex/build/full-book.pdf](tex/build/full-book.pdf).
- 原始 PDF: [input/source/](input/source/), 只读.
- AJbook 模板: 本书 [template/](template/) 集中存放类文件、标题格式、封面样式、字体和适配文件. 纸张和版心在本书的 [ajbook-page-layout.sty](template/ajbook-page-layout.sty) 修改, 不写在译文中.
- 已验收的旧版 PDF 保留, 旧模板已停用并移出本书. 旧版 PDF 见 [mystyle](../../shared/book-records/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/editions/mystyle/); 本次换版核验见 [ajbook-migration.json](../../shared/book-records/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/qa/ajbook-migration.json).

## 重新编译

在本目录的终端执行:

```powershell
..\..\shared\scripts\mathbook.ps1 build-book finite-element-methods-for-navier-stokes-equations-theory-and-algorithms
```

也可以打开共享工作区, 运行“编译所选书籍”并选择本书. 无需每本书再复制一套编辑器任务.

直接编译主入口时, PDF 和辅助文件写入 `tex/build/`; 不另设 `output/`. 共享工作区的验证任务只在 `tex/build/` 的独立子目录生成候选版, 不会覆盖直接编译的 PDF. 修改正文后仍需核对原文、公式、引用、姓名和排版.

## 不需要日常编辑的资料

[书籍记录](../../shared/book-records/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/) 集中保留结构化英文/恢复原稿、独有双语稿、公式登记、术语与姓名、问题和 QA, 以及原配置、状态和排版说明. 这些不是另一份日常编辑入口. 空流程目录和能够确认逐字节重复的副本已删除, 不只是隐藏.

当前程序绑定在 [library-binding.json](../../shared/book-records/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/config/library-binding.json). 旧来源记录中的路径不批量改写; [path-map.json](../../shared/book-records/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/path-map.json) 记录搬迁和去重后的去向, 原始 PDF 页码与块定位信息保持不变.

共享规则: [../../shared/AGENTS.md](../../shared/AGENTS.md). Git 在整个项目总目录统一管理, 不自动推送.
