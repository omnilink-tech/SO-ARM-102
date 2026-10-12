<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[英文原文](../../../translations.md)

[文档](../README.md) · [打印](printing.md) · [物料清单](bom.md) · [装配](assembly-guide.md) · [规格](specifications.md) · [模型](../models/README.md) · [参与贡献](../CONTRIBUTING.md) · [许可说明](../LICENSING.md) · [翻译](translations.md)

> 本文为完整译文。各语言共用插图和原始 PDF 手册。翻译由人工智能辅助完成，尚未经母语使用者审校。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# 文件翻译

在主要的 README 中选择您的语言。 每个语言文件夹都包含完整的 README、材料表、打印说明书、组装指南、规格、模型指南、贡献指南、许可证指南、存储库指南和来源声明,这些文档之间的链接保持在所选语言中。

英文源文档保留在现有路径中,翻译文件位于 `docs/i18n/<language>/` 中并反映源文件夹结构。 CAD、仿真文件、图片、视频和原始 PDF 小册子共享。 嵌入到现有插图中的文本和标签保持原样;装配指南包括翻译的说明书、零部件表、电压警告和插图图例。

<a id="translation-status"></a>
## 翻译状况

首批翻译是通过人工智能和本地翻译模型编制的,然后检查结构完整性、链接和保留的技术值。 它们没有被母语使用者审阅。 请使用英语源文件解决含糊不清之处并通过GitHub问题报告翻译问题,包括语言、文档和受影响句子。

<a id="contribute-a-translation"></a>
## 贡献一个翻译

1. 更改说明或技术数据时,请首先编辑英文源代码。
2. 更新每个语言文件夹中的匹配文档,保留表格、所有步骤、警告、零件标识符、数值、命令和外部 URL。
3. 使用相对路径链接到共享资源。 保留内部部分链接所用的显式英文锚点 ID。
4. 在检查受影响的翻译后,用 `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md` 记录源版本。 此命令只记录版本;它不会翻译或检查文本。
5. 运行 `python .github/scripts/check_translations.py` 和 `pre-commit run --all-files`。 在 pull request 中提交变更,并说明哪些语言被审核过。

当添加源Markdown文档时,请将其路径添加到翻译清单并在每个语言文件夹中提供相应的文件。 CI检查可检测未列出的源文档、更改的源哈希、缺少的翻译、断开的本地链接、缺少的锚点、更改的技术标识符、丢失的表格和缺少的部分。

<a id="repository-conventions"></a>
## 存储库协议

根 README 提供语言链接,因为 GitHub 不会为每个读者自动选择翻译的 README。 每个翻译文档都链接到其他语言的相应文档和其英文源文件。 语言文件夹使用 BCP 47 标签。 这十种语言是国际受众实际选择的结果,而不是按说话人数排序的结果。

- [GitHub README 和相关链接 ](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub 文档翻译工作流程 ](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
