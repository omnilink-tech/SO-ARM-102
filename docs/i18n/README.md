# Documentation languages

Choose a language for descriptions of all 18 existing repository documents:

[English](en/README.md) · [Русский](ru/README.md) · [Deutsch](de/README.md) · [Français](fr/README.md) · [Español](es/README.md) · [Português (Brasil)](pt-BR/README.md) · [简体中文](zh-CN/README.md) · [日本語](ja/README.md) · [हिन्दी](hi/README.md) · [العربية](ar/README.md)

The language guides describe documents and link to their full English originals.
They do not translate the complete instructions, tables or PDF booklet. Original
license texts remain authoritative; their descriptions do not replace license terms.
CAD, media and simulation assets are shared and are not duplicated per language.

## Folder layout

Each BCP 47 language tag has its own folder and `README.md` in `docs/i18n/`.
The ten supported languages are a practical selection for an international audience,
not a statistical ranking of the world's ten most spoken languages.
The existing English files remain at their current paths to preserve incoming links.
The `en/` guide is the English reference for the localized descriptions.

## Maintain the descriptions

1. Update the original document first, then review its English description in `en/README.md`.
2. Update the corresponding description in all nine other language folders. Keep
   filenames, part numbers, units and SPDX license identifiers unchanged.
3. Keep links relative to the guide. Each guide must link to every source document
   and all ten language guides. Do not translate or duplicate license texts.
4. After reviewing all affected descriptions, run
   `python .github/scripts/check_i18n.py --refresh-source-hashes` to record the reviewed
   source versions. This command only records hashes; it does not translate or review text.
5. Run `python .github/scripts/check_i18n.py` and the repository pre-commit checks.
   Submit translation changes through a pull request. Native-speaker review is welcome;
   this initial set was prepared with AI assistance and has not had native-speaker review.

The manifest records SHA-256 hashes of the source documents. CI detects changed
sources, missing guides, broken local links and incomplete document coverage. It
cannot verify translation quality. When adding a document, add its description in
every language and refresh the source manifest. The check also detects newly added
Markdown, PDF and license text files outside this translation directory.

## GitHub conventions

GitHub displays the main README and supports relative links; language navigation
is provided explicitly here and in the root README. This repository uses one source
language and separate language folders, without a documentation build service.

- [GitHub README and relative-link guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [How GitHub Docs maintains translations](https://github.com/github/docs/blob/main/src/languages/README.md)
