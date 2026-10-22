# 样本交叉引用报告

Status: passed. 原文引用、来源块、原 PDF/印刷页、目标对象、稳定标签、LaTeX 引用命令、译文块位置和编译后页码均在 cross-reference-report.json 登记.

样本中的四个编号公式使用唯一语义标签, 保持原书 2.1-2.4 编号. 三个节标题保持 2.4-2.6 编号. Proposition, Theorem 和 Remark 复用共享模板的 statement 计数器, 分别正确显示 2.1, 2.2, 2.3. 未编号公式不擅自编号, 通过稳定的 formula ID 保留来源.

公式引用使用 eqref, 章节/节/文献引用使用 ref. 正文的 8 个显式引用均有真实链接. 已核验 13 个主要目标的编号及 PDF 跳转页, 另有章节上下文标签. 样本外三个目标已核实且仅作为源文定位, 不是已翻译章节的占位冒充.

干净构建目录至少完成两轮编译; undefined reference 和 multiply-defined label 为 0. 编译通过不代替公式的原页核验.
