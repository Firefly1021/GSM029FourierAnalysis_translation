# 本书两套排版的区别

本书已验收的译文只有一份. `tex/chapters/` 和 `tex/frontmatter.tex` 仍是正文排版输入; 没有为换模板重译、删节或改写正文.

| 项目 | AJbook 版 (当前选用) | 原 Mystyle 版 (保留) |
| --- | --- | --- |
| 入口 | `tex/aljabr-main.tex` | `tex/main.tex` |
| 输出 | `output/book-aljabr-zh.pdf` | `output/book-zh.pdf` |
| 模板 | `template/collections/aljabr-1/upstream/` | `template/style/`、`reference/`、`assets/` |
| 适配 | `template/adapter/aljabr-1/` | 原 `template/adapter/` 顶层文件 |
| 证据 | `qa/template/aljabr-acceptance.json` | `qa/final-report.json` |

上表中的 `template/` 均位于本书 worktree 根目录, 不在 `books/` 内. 两套模板不同时加载. 上游收藏中的 `chapter*.tex` 是原作者的模板示例/上游书稿, 不是 FEEC 译文, 不要编辑或编译它们来修改本书.

## 重建 AJbook 版

在 `finite-element-exterior-calculus` 专属 worktree 根目录运行:

```powershell
$env:PYTHONPATH = Join-Path (Get-Location) 'src'
python books/finite-element-exterior-calculus/workflow/aljabr_workflow.py finite-element-exterior-calculus build
```

构建程序设置独立模板搜索路径, 从原有正文生成 `tex/generated/aljabr-layout/` 排版缓存, 再执行干净编译、编号/引用/输入哈希检查和页面渲染. 编译结果及其临时位置记录在 `qa/template/aljabr-compilation.json`. `build` 不自动替换已验收的输出; 本次已验收结果单独保存在上表输出位置. `accept` 是绑定本次人工页面检查证据的操作, 不是通用自动验收开关.

不要手改 `tex/generated/aljabr-layout/`, 它会重新生成. 需要修改正文时仍应修改原有正文文件, 并按项目规则显式重新审核对应的验收哈希. 原文件的保护不会因换版而取消.

## 上游与差异

上游: https://github.com/wenweili/AlJabr-1 , 固定提交 `1e2d0bf4e5b71194b85958ca6b16a6f396ad25be`. 原模板、许可证和说明全部原样保存. 适配层只做本书的章节/编号兼容、英文环境名和字体回退. 没有把上游《代数学方法》的正文、作者信息或数学宏定义导入本书. 新版书尾单独标明模板署名和许可, 不改变原书及译文的权利归属.

其余书籍不切换此模板. 全局默认仍为 Mystyle. 本次没有推送远端.
