<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[英文原文](../../../CONTRIBUTING.md)

[文档](README.md) · [打印](docs/printing.md) · [物料清单](docs/bom.md) · [装配](docs/assembly-guide.md) · [规格](docs/specifications.md) · [模型](models/README.md) · [参与贡献](CONTRIBUTING.md) · [许可说明](LICENSING.md) · [翻译](docs/translations.md)

> 本文为完整译文。各语言共用插图和原始 PDF 手册。翻译由人工智能辅助完成，尚未经母语使用者审校。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# 参与贡献

感谢您帮助改进 SO-ARM 102。

<a id="report-a-problem"></a>
## 报告问题

打开一个问题,并包括:

- 您正在构建或打印的内容,以及零件编号;
- 打印机、材料和切片器设置以解决打印问题;
- 照片,如果有东西不适合。

构建报告特别受欢迎,即使一切都正常。

<a id="change-a-part"></a>
## 修改零件

1. 在 `models/step/` 中编辑 STEP 文件。
2. 将具有相同名称的二进制文件 STL 导出到 `models/stl/`。
3. 如果名称、数量或紧固件发生变化,请更新 `docs/printing.md` 和 `docs/assembly-guide.md` 。
4. 在打开 pull 请求之前打印并配合零件,并在 pull 请求中说明您测试了什么。

<a id="licence-of-contributions"></a>
## 贡献内容的许可证

您的修改是根据已经涵盖文件的许可协议授权的。

| 你正在改变 | 您的贡献已被授权 |
|---|---|
| CAD和网格在`models/` | CERN-OHL-P-2.0 |
| 配置和 CI | Apache-2.0 |
| 文档和图像 | CC BY 4.0 |

如果贡献中包含的材料不是你创建的,请在 pull 请求中说明这一点,以便它可以被记录到 `NOTICE` 中。 新文件必须由 `REUSE.toml` 覆盖,否则 CI 会运行 `reuse lint` 并失败。
<!-- /translated-content -->
