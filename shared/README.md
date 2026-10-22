# 数学著作翻译项目

这是统一后的项目入口. 总目录为 `BOOKTRANSLATION`, 日常只区分两个区域:

| 区域 | 用途 |
| --- | --- |
| `books/` | 每本书独立的原始 PDF、模板快照、章节 TeX、图片、英文恢复稿、译文、公式、QA 和正式输出 |
| `shared/` | 全部书籍共用的说明、规则、模板收藏、权威术语库、程序、配置、测试和项目登记 |

本文件位于 `shared/README.md`. 下文以整个项目总目录为命令起点. Git 的隐藏管理文件留在总目录, 不需要日常操作.

## 我应该用 VS Code 打开哪里

- **只修改一本书**: 打开 `books/<book-id>/`, 然后看该书的 `OPEN-THIS-BOOK.md`.
- **一个窗口管理全部书籍**: 打开 [BOOKTRANSLATION.code-workspace](BOOKTRANSLATION.code-workspace).
- **修改共享程序、模板或项目规则**: 打开本 `shared/` 目录. 原始模板仍然只读.

每本书的正式 TeX 入口和正式 PDF 都已明确登记. 不要只凭 `main.tex` 这个名字判断它是样本还是全书入口. 不要进入 `.legacy-worktrees` 编辑.

## 书籍总览

见 [PROJECTS.md](PROJECTS.md). 总览中的完成状态取自各书自己的现有记录, 不是本次重新进行数学验收. 第一部 Fourier Analysis 的源 PDF 缺少书目和索引, 原有问题记录照旧保留, 不因整理目录而清除.

七本书的目录分别是:

1. `books/fourier-analysis/`
2. `books/the-mathematical-theory-of-finite-element-methods/`
3. `books/navier-stokes-equations-theory-and-numerical-analysis/`
4. `books/mathematical-tools-for-the-study-of-the-incompressible-navier-stokes-equations-and-related-models/`
5. `books/finite-element-methods-for-navier-stokes-equations-theory-and-algorithms/`
6. `books/krylov-subspace-methods-for-linear-systems/`
7. `books/finite-element-exterior-calculus/`

## 编译与日常命令

在一本书的 VS Code 窗口运行“编译本书”任务即可. 也可以在项目总目录执行:

```powershell
.\shared\scripts\mathbook.ps1 list-books
.\shared\scripts\mathbook.ps1 status finite-element-exterior-calculus
.\shared\scripts\mathbook.ps1 build-book finite-element-exterior-calculus
```

编译读取本书正式入口和本书模板快照, 在本书临时目录生成候选 PDF 和日志, **不自动覆盖已验收的正式 PDF**. 改动译文后仍须重新检查公式、引用、姓名、标点及排版.

已具备 Python 环境时, 跨平台入口是:

```text
python shared/scripts/library_cli.py list-books
python shared/scripts/library_cli.py build-book <book-id>
```

共享包配置在 `shared/pyproject.toml`; 测试在 `shared/tests/`. 可以在 `shared/` 下使用原 Makefile. 本机启动器会读取不提交的本地 Python 路径配置, 避免 WindowsApps 空壳命令. 其他电脑需具备 Python 依赖、TeX Live 及模板要求的字体; 原始字体说明和许可随模板保存.

## 新建和继续翻译

```powershell
.\shared\scripts\mathbook.ps1 new-book <book-id> --source "<PDF路径>"
.\shared\scripts\mathbook.ps1 start-book <book-id>
.\shared\scripts\mathbook.ps1 approve-sample <book-id>
.\shared\scripts\mathbook.ps1 translate-book <book-id>
.\shared\scripts\mathbook.ps1 resume <book-id>
```

`new-book` 在 `books/` 中创建完整书籍目录、登记源哈希、固定模板快照并留下本地 checkpoint 分支, 不再创建外部 worktree 目录. 日常工作保留在统一 `main` 工作目录内. `start-book` 等阶段仍要求明确配置的处理程序, 没有处理程序时会明确报错, 不虚构 OCR、翻译或 QA.

## 模板和术语

- 全局唯一权威术语库: [glossary/terminology.tsv](glossary/terminology.tsv). 按 English + Domain + Context 匹配.
- 本书术语候选、姓名和记号保留在各书自己的 `glossary/` 中; 不静默覆盖全局术语.
- 共享原始模板及收藏在 [template/](template/), Mystyle 与 AJbook 分开放置. **只有 FEEC 选用 AJbook**, 其他书籍不切换模板.
- 各书 `template/` 是从其原工作区取得的完整快照. 更改共享模板不会自动影响旧书. 原始 `.sty`、参考 `.tex` 和模板资源仍只读.
- 翻译规则见 [AGENTS.md](AGENTS.md) 和 [style/chinese-mathematical-style.md](style/chinese-mathematical-style.md).

## Git 与恢复

总目录是唯一日常 Git 入口. 每次先检查修改路径, 按需要提交对应书籍或共享修改. 不切换到历史 `book/` 分支操作当前目录. 系统维护仍先使用独立维护分支. 自动化不执行推送、不改远端、不改写历史.

原书籍分支和提交历史均保留. 历史工作区位于 `.legacy-worktrees/`, 已锁定并采用最小稀疏视图, 不再保留一套完整的书籍工作副本. 原扫描、预处理、OCR、版面和编译缓存、过期预览及已完成书籍的过程脚本已按清单清理; 不用隐藏目录继续重复存放这些大文件. 原主目录中发现的六份独有文件另存于 Fourier 书内 `archive/pre-integration-main/`, 没有覆盖当前译稿.

已跟踪的过程文件可从本地整合检查点 `538012e` 或原书分支找回. 未跟踪的图像/OCR/构建缓存没有逐份备份, 需要时须由原始 PDF 重新生成. 不删除或改写 Git 历史来压缩体积.

历史配置、日志、QA 中的旧绝对路径是原始证据, 未批量替换. 当前目录绑定见各书 `config/library-binding.json` 和本项目登记. 迁移清单与核验在 [qa/integration-20261022/](qa/integration-20261022/); 详细组织说明见 [docs/目录与日常编辑.md](docs/目录与日常编辑.md).

## 已完成书籍的保留与清理

永久保留原始 PDF、完整正式 TeX 及依赖图片/宏/文献、正式 PDF、原始模板、恢复的英文原稿、公式登记、术语/姓名/记号、未解决问题和现有文字 QA. `tex/generated/` 中被正式入口实际使用的源文件也是成品工程的一部分, 不能整目录删除. 扫描恢复的少量定位裁剪作为核验依据保留, 大体积全页衍生图和 OCR 临时结果已清理.

两本旧书在完成后更新过原始 `.sty`, 与其旧适配文件存在环境重定义冲突. 用户当前文件原样留在 `template/`; 当时验收的模板按原始清单逐文件校验, 单独放在 `template-accepted/`, 并由 `config/library-binding.json` 明确选择用于编译. 没有修改用户模板或设计新样式.

重新编译会产生新的临时构建目录. 这是可清理缓存, 不是新的正式译本. 共享程序和通用检查工具只保留一套, 不在每本书中复制.
