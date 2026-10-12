<!-- translation-navigation -->
[English](translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[English source](../../../translations.md)

[Documentation](../README.md) · [Printing](printing.md) · [BOM](bom.md) · [Assembly](assembly-guide.md) · [Specifications](specifications.md) · [Models](../models/README.md) · [Contributing](../CONTRIBUTING.md) · [Licensing](../LICENSING.md) · [Translations](translations.md)

> English reference. Shared illustrations and the original PDF booklet are unchanged.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Documentation translations

Choose your language in the main README. Each language folder contains the complete README, bill of materials, printing instructions, assembly guide, specifications, model guide, contribution guidelines, licensing guide, repository guidance and attribution notices. Links between these documents stay in the selected language.

English source documents stay at their existing paths. Translations are in `docs/i18n/<language>/` and mirror the source folder structure. CAD, simulation files, images, videos and the original PDF booklet are shared. Text and labels embedded in existing illustrations remain as drawn; the assembly guide includes the translated instructions, parts tables, voltage warning and illustration legend. Original legal license texts and machine-readable configuration are shared, not translated.

<a id="translation-status"></a>
## Translation status

The first translations were prepared with AI assistance and a local translation model, then checked for structural completeness, links and preserved technical values. They have not been reviewed by native speakers. Use the English source to resolve ambiguities and report translation problems through a GitHub issue, including the language, document and affected sentence. A passing CI check does not certify linguistic or hardware correctness.

<a id="contribute-a-translation"></a>
## Contribute a translation

1. Edit the English source first when changing instructions or technical data.
2. Update the matching document in each language folder. Preserve tables, all steps, warnings, part identifiers, numerical values, commands and external URLs.
3. Keep local document links in the same language. Link to shared assets using relative paths. Preserve the explicit English anchor IDs used by internal section links.
4. After reviewing the affected translations, record the source versions with `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`. This command records versions only; it does not translate or review text.
5. Run `python .github/scripts/check_translations.py` and `pre-commit run --all-files`. Submit changes in a pull request and state which languages were reviewed.

When adding a source Markdown document, add its path to the translation manifest and provide the corresponding file in every language folder. The CI check detects unlisted source documents, changed source hashes, missing translations, broken local links, missing anchors, changed technical identifiers, lost tables and missing sections.

<a id="repository-conventions"></a>
## Repository conventions

The root README provides language links because GitHub does not automatically select a translated README for each reader. Each translated document links to the equivalent document in every other language and to its English source. Language folders use BCP 47 tags. The ten languages are a practical international audience selection, not a ranking by speaker count. English remains the source language for maintenance.

- [GitHub README and relative links](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Docs translation workflow](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
