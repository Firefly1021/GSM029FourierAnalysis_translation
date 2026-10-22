# 统一目录与已完成书籍清理验收

日期: 2026-10-22. 范围: 用户授权的项目整合、缓存/过程脚本清理及构建回归. 不重译任何已验收章节, 不把本次构建回归冒充新的全书数学验收.

## 最终入口

唯一总目录: `D:\CelianFile\BOOKTRANSLATION`. 可见顶层只有 `books/` 与 `shared/`. Git 的隐藏元数据留在总目录. 原外部 `BOOKTRANSLATION-worktrees` 容器已经移空并移除.

日常逐书打开 `books/<book-id>/`, 以 `OPEN-THIS-BOOK.md` 为入口. 全部书籍可在 `shared/BOOKTRANSLATION.code-workspace` 中统一打开. 共享规则、权威术语、模板收藏、程序和测试只保留一套.

## 实际清理

删除均有先行清单及执行回执; 数字为文件逻辑大小, 不是磁盘空闲空间测量值. GB 为十进制.

| 类别 | 文件数 | 删除字节 | 约 GB |
| --- | ---: | ---: | ---: |
| 本次迁移产生的部分重复缓存副本 | 3,796 | 35,839,079,620 | 35.84 |
| 七本书的页面/OCR/版面/编译缓存、旧预览和过程脚本 | 72,712 | 42,391,037,001 | 42.39 |
| 冗余旧主目录副本及旧工作区被忽略缓存/虚拟环境 | 17,468 | 2,806,118,809 | 2.81 |
| 清理后回归编译新产生的缓存及 Python/历史工作区缓存 | 824 | 106,861,026 | 0.11 |
| 合计 | 94,800 | 81,143,096,456 | 81.14 |

其中 35.84 GB 是整理过程中产生后随即清除的重复副本, 不计作原项目自身的膨胀. `books/` 从清理前清单的 42,673,042,901 字节下降到验收时的约 430,106,479 字节, 即约 42.67 GB -> 0.43 GB. 这些数值不包含隐藏 Git 历史, 也不宣称精确等于实际磁盘释放量.

每本书的翻译过程 Python 脚本均已清除. 共享自动化和通用检查工具保留. 没有通过删除或改写 Git 历史来缩小项目.

## 保留内容与无损边界

- 原始 PDF、完整正式 TeX、全部实际编译依赖、图片、宏、文献、正式 PDF、用户模板与依赖字体均保留.
- 恢复的英文原稿、结构化英文、译文、公式登记、术语/姓名/记号、问题和文字 QA 保留. 少量定位裁剪保留为扫描核验依据, 不与已删除的全页衍生图混淆.
- 清理前后逐文件重新核验 11,423 份保留文件、429,999,301 字节. 自建的 7 份入口指南和 7 份构建报告允许更新, 在核验报告中显式列为例外, 不算作原文改动.
- 七本书原始配置、PROJECT_STATUS 和 issues 原字节保持不变. 当前路径由 `config/library-binding.json` 和共享 PROJECTS 决定, 原记录中的旧路径仍作为历史证据保留.
- 原主目录发现的六份独有小文件逐字节保存到 Fourier 书内 `archive/pre-integration-main/`, 不覆盖当前译稿.

## 模板版本冲突处理

两本旧书在完成后更新了用户 `.sty`, 与旧适配文件产生环境重复定义. 新的用户文件原样保留于各书 `template/`; 另从原提交 `d012545` 恢复与原验收清单全部 SHA-256 相符的历史文件, 放在 `template-accepted/`. 当前绑定明确选择历史验收版用于这两本书的编译, 不是修改新模板来假造一致. 详情见 `accepted-template-recovery.json`.

第一本书等旧配置中还保留早期目录哈希算法/版本的值; 本次分别记录历史值和当前快照值, 没有篡改旧记录. 当前用户文件的迁移前后字节一致已经独立核验.

## 构建与显示回归

清理前、清理后均从新的空构建目录编译七本完整主入口. 使用 LaTeX 编译技能及本机 TeX Live/latexmk, 没有改动章节正文. 修正共享构建器的图片/源 PDF 搜索路径和 Windows 子进程 UTF-8 日志读取问题. 使用实际 `.fls` 记录保护主入口的本书依赖, 不把 `generated/` 当作可整目录删除的缓存.

| 书籍 | 正式入口 | 清理后页数 | 与原正式版页数一致 |
| --- | --- | ---: | --- |
| Finite Element Exterior Calculus | `tex/aljabr-main.tex` | 140 | Yes |
| Finite Element Methods for Navier-Stokes Equations: Theory and Algorithms | `tex/full-book.tex` | 324 | Yes |
| Fourier Analysis | `tex/main.tex` | 167 | Yes |
| Krylov Subspace Methods for Linear Systems | `tex/main.tex` | 201 | Yes |
| Mathematical Tools for the Study of the Incompressible Navier-Stokes Equations and Related Models | `tex/main.tex` | 361 | Yes |
| Navier Stokes Equations Theory and Numerical Analysis | `tex/main.tex` | 385 | Yes |
| The Mathematical Theory of Finite Element Methods | `tex/main.tex` | 298 | Yes |

- 原正式 PDF 全部 SHA-256 不变, 候选 PDF 未覆盖正式输出. FEEC 既有 Mystyle 正式版另行保留.
- 七本最终原生日志均无 undefined reference、multiply-defined label 或 missing character. 扫描有限元书保留 4 处既有 overfull hbox, Mathematical Tools 保留 3 处轻微 overfull hbox; 没有为此次整理改变其排版.
- 清理后每本首页/中间页/末页共 21 页在 72 DPI 下与原正式版逐像素一致. 这是抽查, 不冒充全部页面或数学内容的重新审核.
- 自动测试 45/45 通过, 没有失败/错误/跳过.
- 本次验证生成的候选 PDF、原生日志和缓存亦已按单独清单清除. `builds.json` 和书内 `qa/unified-build.json` 明确标记其中路径为历史验证路径.

## Git 与恢复

原七个 book 分支的提交头不变. 原工作区注册均保留并锁定, 以最小稀疏视图隐藏重复的跟踪文件; 不删除真实分支或工作区. 扫描书原有未提交 `uv.lock` 保留. 原 remote URL 不变, 没有任何远端写入.

已跟踪的过程文件可从本地整合检查点 `538012e` 或原书分支恢复; 原主目录旧版本可从 `e70714f` 恢复. 未跟踪的衍生图/OCR/构建缓存没有逐份备份, 需要时由保留的原始 PDF 重新生成. 这不是对缓存的无损保留, 而是用户明确授权的删除.

`verification.json` 是清理前迁移核验; `cleanup-verification.json` 才是清理后的保留与构建核验. 源书既有缺失、未解决引用或数学问题继续保留于各书原 QA 中, 不因编译成功而宣称解决.
