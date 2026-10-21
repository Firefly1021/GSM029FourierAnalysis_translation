# AlJabr-1 / AJbook 模板收藏

- 上游: https://github.com/wenweili/AlJabr-1
- 固定版本: `1e2d0bf4e5b71194b85958ca6b16a6f396ad25be`.
- 作者及许可: 李文威 (Wen-Wei Li), CC BY 4.0. 完整许可证在 `upstream/LICENSE`.
- `upstream/` 是该版本全部 Git 跟踪文件的只读原样快照, 不含 `.git`. 包括文档类、字体/标题配置、示例、说明、图片、许可证和上游书稿. 上游示例和书稿不是本项目译文, 不得导入到译书正文.
- 本项目适配层位于 `template/adapter/aljabr-1/`. 原始 `.cls`、`.sty` 和 `.tex` 不作修改.
- 只为 `finite-element-exterior-calculus` 显式选择此模板. 其他书籍和默认 `Mystyle` 配置不变.
- 原模板仍位于 `template/style/`, `template/reference/`, `template/assets/` 和原顶层适配文件. 不移动、不覆盖、不混合加载.
- 本机缺少 Noto Sans CJK SC 时, 字体适配只为这几个 Noto 字族回退到上游同样使用的 FandolHei. 不安装或替换系统字体.
- 接入改动: 原已验收的 section/ subsection 层级在生成副本中对应到 AJbook 的 chapter/section; 保持原标签、数学标记、译文和对象编号. 环境标题仍使用英文, 数学显示遵循本书获批的非 Fraktur 策略.
- 这不改变原书及译文的权利归属. 本项目接入文件的改动说明不表示上游作者认可本译本.
