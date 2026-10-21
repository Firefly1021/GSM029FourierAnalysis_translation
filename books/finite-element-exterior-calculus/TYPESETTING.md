# 本书两套排版的区别

本书已验收的译文只有一份. `tex/chapters/` 和 `tex/frontmatter.tex` 仍是正文排版输入; 没有为换模板重译、删节或改写正文.

| 项目 | AJbook 版 (当前选用) | 原 Mystyle 版 (保留) |
| --- | --- | --- |
| 入口 | `tex/aljabr-main.tex` | `tex/main.tex` |
| 输出 | `output/book-aljabr-zh.pdf` | `output/book-zh.pdf` |
| 模板 | `template/collections/aljabr-1/upstream/` | `template/style/`、`reference/`、`assets/` |
| 适配 | `template/adapter/aljabr-1/` | 原 `template/adapter/` 顶层文件 |
| 证据 | `qa/template/aljabr-noto-acceptance.json` | `qa/final-report.json` |

上表中的 `template/` 均位于本书 worktree 根目录, 不在 `books/` 内. 两套模板不同时加载. 上游收藏中的 `chapter*.tex` 是原作者的模板示例/上游书稿, 不是 FEEC 译文, 不要编辑或编译它们来修改本书.

## 重建 AJbook 版

在 `finite-element-exterior-calculus` 专属 worktree 根目录运行:

```powershell
$env:PYTHONPATH = Join-Path (Get-Location) 'src'
python books/finite-element-exterior-calculus/workflow/aljabr_workflow.py finite-element-exterior-calculus build
```

构建程序设置独立模板搜索路径和本书 Fontconfig 缓存, 从原有正文生成 `tex/generated/aljabr-layout/` 排版缓存, 再执行干净编译、编号/引用/输入哈希检查和页面渲染. 编译结果及其临时位置记录在 `qa/template/aljabr-compilation.json`. `build` 不自动替换已验收的输出; 验收结果单独保存在上表输出位置. 原 `accept` 只绑定历史回退版, 不用于当前字体修订. `noto_revision.py` 的 `publish` 只接受绑定实际 PDF 哈希、全页人工视检和回归结果的本次字体修订证据, 不是通用自动验收开关.

不要手改 `tex/generated/aljabr-layout/`, 它会重新生成. 需要修改正文时仍应修改原有正文文件, 并按项目规则显式重新审核对应的验收哈希. 原文件的保护不会因换版而取消.

## 上游与差异

上游: https://github.com/wenweili/AlJabr-1 , 固定提交 `1e2d0bf4e5b71194b85958ca6b16a6f396ad25be`. 原模板、许可证和说明全部原样保存. 适配层只做本书的章节/编号兼容和英文环境名. 字体入口直接加载上游原始 `font-setup-open.tex`, 不再改写字体设置或使用字体回退. 没有把上游《代数学方法》的正文、作者信息或数学宏定义导入本书. 新版书尾单独标明模板署名和许可, 不改变原书及译文的权利归属.

## 原始字体已配齐, 2026-10-21

官方 Noto Sans CJK SC 的 Regular、Bold、Medium、Black 四个字重已下载并安装到当前用户 Windows 字体目录. 另在共享模板收藏的 `template/collections/aljabr-1/fonts/noto-sans-cjk-sc/` 中保存固定版本 Sans2.004 的字体文件、SIL OFL 1.1 许可证、来源提交和校验清单. 官方仓库: https://github.com/notofonts/noto-cjk . 编译程序使用项目内这份字体, 不依赖另一台电脑是否已安装它们; 不修改全局 TeX 字体配置.

四个字重均经实际字体解析和哈希验证. 当前 PDF 实际使用并嵌入 Regular、Bold 和 Black. Medium 在本书英文 Proof 标题中没有用到中文字形, 未强制产生无用嵌入. 正文的宋体、楷体、仿宋仍按上游原始配置保留, 并非再用黑体替代 Noto. Windows 用户安装文件和注册表记录见字体验收报告.

之前使用 FandolHei 回退的 AJbook PDF 已原样归档在 `output/archive/book-aljabr-fandol-20261021.pdf`, 对应历史 QA 在 `qa/template/archive/fandol-20261021/`. 历史 `aljabr-acceptance.json` 描述旧版, 当前以 `aljabr-noto-acceptance.json` 为准. 旧 Mystyle 版及所有已验收译文和数学对象仍保持原字节不变.

本次恢复原模板的字体与标题层级, 没有重新设计标题框尺寸. 较长章名仍采用上游自动折行; 美观程度仍以用户查看新版后的判断为准, 不以编译通过代替审美认可.

其余书籍不切换此模板. 全局默认仍为 Mystyle. 本次没有推送远端.
