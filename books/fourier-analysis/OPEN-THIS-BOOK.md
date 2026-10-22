# Fourier Analysis

这是本书唯一的日常编辑目录. 用 VS Code 打开本目录即可, 不再打开历史 worktree.

- 正式 TeX 入口: [tex/main.tex](tex/main.tex).
- 章节: [tex/chapters/](tex/chapters/). 图片: [tex/figures/](tex/figures/); 保留原有图片引用方式.
- 原始 PDF: [input/source/](input/source/), 只读.
- 本书实际模板快照: [template/](template/), 不自动跟随共享模板更新.
- 当前正式输出: [output/book-zh-progress.pdf](output/book-zh-progress.pdf).
- 恢复英文原稿、完整译文、公式、术语和文字 QA 均保留. 全页/OCR/编译缓存、过期预览和书内翻译过程脚本已清理; 实际编译依赖未删除, 没有删节或重新翻译.

编译: VS Code 运行“编译本书”任务, 或在总目录运行:

```powershell
.\shared\scripts\mathbook.ps1 build-book fourier-analysis
```

新构建只写本书临时目录, 不自动覆盖正式 PDF. 历史 config/book.yaml、PROJECT_STATUS 和 QA 中的旧绝对路径保留为证据; 当前位置以 config/library-binding.json 和共享 PROJECTS.md 为准.

共享规则: [../../shared/AGENTS.md](../../shared/AGENTS.md). Git 提交与推送在总目录统一进行; 不自动推送.
