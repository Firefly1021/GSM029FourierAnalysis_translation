# Navier Stokes Equations Theory and Numerical Analysis

这是本书的成品编辑目录. 用 VS Code 打开本目录即可. 不需要接触原来的翻译流程目录.

## 修改与阅读

- 正式主入口: [tex/main.tex](tex/main.tex).
- 当前版本的正文: [tex/chapters/](tex/chapters/). 修改句子、符号和段落时从这里进入.
- 图片: [tex/figures/](tex/figures/). 不要删除主文件仍引用的宏、图片或文献.
- 正式 PDF: [output/book-zh.pdf](output/book-zh.pdf).
- 原始 PDF: [input/source/](input/source/), 只读.
- 模板: 编译使用 [template-accepted/](template-accepted/); 用户后来更新的原始文件在 [template/](template/), 两版明确隔离且均不改写.

## 重新编译

在本目录的终端执行:

```powershell
..\..\shared\scripts\mathbook.ps1 build-book navier-stokes-equations-theory-and-numerical-analysis
```

也可以打开共享工作区, 运行“编译所选书籍”并选择本书. 无需每本书再复制一套编辑器任务.

编译按需写入忽略的 `.build/`, 不再建立 `workspace/`、`logs/` 或 `workflow/`. 生成的是待检查的候选 PDF, 不自动覆盖上面的正式 PDF. 修改正文后仍需核对原文、公式、引用、姓名和排版.

## 不需要日常编辑的资料

[records/](records/) 集中保留结构化英文/恢复原稿、独有双语稿、公式登记、术语与姓名、问题和 QA, 以及原配置、状态和排版说明. 这些不是另一份日常编辑入口. 空流程目录和能够确认逐字节重复的副本已删除, 不只是隐藏.

当前程序绑定在 [records/config/library-binding.json](records/config/library-binding.json). 旧来源记录中的路径不批量改写; [records/path-map.json](records/path-map.json) 记录搬迁和去重后的去向, 原始 PDF 页码与块定位信息保持不变.

共享规则: [../../shared/AGENTS.md](../../shared/AGENTS.md). Git 在整个项目总目录统一管理, 不自动推送.
