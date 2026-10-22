# 已完成书籍的成品目录精简

日期: 2026-10-22. 对象: 用户截图指出的书内流程目录及其余六本已完成书籍. 本次不仅清理缓存体积, 也把每本书的根目录整理成便于手工编辑的成品视图.

## 实际目录

FEEC 从原先 18 个根条目精简为 6 个:

```text
finite-element-exterior-calculus/
├── input/
├── tex/
├── template/
├── output/
├── records/
└── README.md
```

其余书籍使用相同成品布局. 两本旧书因已有模板版本冲突, 仍额外保留必需的 `template-accepted/`, 没有把它与用户后来更新的 `template/` 混用.

`workflow`、`logs`、`workspace`、书内 `.vscode` 和旧 `OPEN-THIS-BOOK.md` 已实际删除, 不是仅设置隐藏属性. 书内的 config、formulae、glossary、qa、structured、独有 translation 记录、archive、原计划/状态/排版说明集中到 `records/`. 这些资料保留在各自书籍内, 未混入共享库.

全书的统一 VS Code 工作区保留一个“编译所选书籍”任务; 单独打开一本书时, README 给出该书准确的编辑与编译入口, 不再每本书重复一份编辑器任务.

## 删除与保留

- 实际删除 617 个文件, 共 6,480,440 字节. 其中 488 个译文或元数据副本与保留文件的 SHA-256 完全一致, 已去重. 其余为退休入口/任务、剩余测试缓存和空流程目录标记.
- 每份去重文件都有保留目标, 并验证其哈希. 旧路径的精确别名及目录搬迁映射保存在书内 `records/path-map.json`, 不批量重写历史 source/QA 内容.
- 10,819 份保留文件重新通过 SHA-256 校验. 本次自建的 7 份构建报告允许刷新, 明确不计作原文内容变化.
- 原始 PDF、所有正式 TeX(包括必需 generated 输入)、图片、模板、字体、正式输出和独有英文恢复资料均保留; 没有改写句子、公式、姓名、标签或编号.
- 原配置、进度、状态及 issues 原字节保留, 只是搬入 records. 原有未解决问题没有因为目录精简被清空.
- 本次回归编译新产生的 7 个 `.build` 目录亦已按清单清除, 合计约 93.94 MB. 该数字与上面的 617 个原有文件分开统计.

删除清单和执行回执分别为 `plan.json`、`plan.receipt.json`; 其中的快照提交可恢复已跟踪的退休文件. 新构建缓存为可再生文件, 不声称逐份备份.

## 编辑入口核实

FEEC AJbook 的正式入口是 `tex/aljabr-main.tex`, 实际正文为 `tex/generated/aljabr-layout/`. 此处虽然名为 generated, 已作为永久成品输入固定保留, 不由被删除的翻译脚本覆盖. 旧 `tex/chapters/`、`tex/main.tex` 是前一 Mystyle 版的验收源文件, 修改它们不会自动改变 AJbook 版. README 明确说明这一点, 没有为了统一目录而重写任一版本的已验收内容.

扫描有限元 Navier--Stokes 书使用 `tex/full-book.tex`; 其他书籍使用各自 README 中登记的主入口. 不根据文件名猜测全书入口.

## 程序兼容与验证

- BookPaths 支持“翻译中的工作布局”和“已完成的 records 布局”, 二者分别解析, 没有改变未完成新书的工作流程.
- 成品书绑定为 `records/config/library-binding.json`. 配置、术语、姓名、公式与问题读取使用正确的新位置; provenance 通过映射解析, 不改写原始记录.
- 对成品书执行 status/resume/finish 不重跑旧批次. start/translate/sample-approval 和翻译过程脚本拒绝重新生成已验收内容. `ensure_structure` 不重建旧流程目录.
- 构建按需创建 Git 忽略的 `.build/`, 不创建旧 workspace/logs/qa 根目录, 不覆盖正式 PDF. 旧 compile-book 入口转交正式绑定构建器.
- 通用姓名、标点、引用与只读 QA 工具适配 records 路径. 对完成书进行单章检查必须显式给出实际正文 `--tex`; 省略时明确报错, 不误用旧模板版的 chapters 或样本. 全书只读 QA/引用总标签集合按实际主入口的输入选择, 不混入旧模板版本的正文.
- 53 项自动测试全部通过, 无失败/错误/跳过. 包含旧布局兼容、成品路径、误重启阻止、旧目录不重建、去重路径解析与实际主入口 QA 选择等回归测试.
- 七本完整主入口均从空 `.build` 目录重新编译成功, 页数分别为 140、324、167、201、361、385、298, 与各自原正式版一致. 原正式 PDF SHA-256 全部不变.
- 七本最终编译记录无 undefined reference、multiply-defined label 或 missing character. 原有 4 处扫描书和 3 处 Mathematical Tools 的轻微 overfull hbox 保留, 未为整理目录改变排版.
- 每本首页/中间页/末页共 21 页在 72 DPI 下与原正式版逐像素一致. 这是构建/显示回归抽查, 不是全书数学内容重新验收.

全部 book 分支头、历史工作区和远端地址保持不变; 没有自动推送, 没有改写历史. 当前日常工作仍在统一 main 目录. 最终机器核验见 `verification.json`, 构建与显示证据见 `builds.json` 和 `rendering-spot-comparison.json`.
