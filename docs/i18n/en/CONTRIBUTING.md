<!-- translation-navigation -->
[English](CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[English source](../../../CONTRIBUTING.md)

[Documentation](README.md) · [Printing](docs/printing.md) · [BOM](docs/bom.md) · [Assembly](docs/assembly-guide.md) · [Specifications](docs/specifications.md) · [Models](models/README.md) · [Contributing](CONTRIBUTING.md) · [Licensing](LICENSING.md) · [Translations](docs/translations.md)

> English reference. Shared illustrations and the original PDF booklet are unchanged.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Contributing

Thank you for helping improve SO-ARM 102.

<a id="report-a-problem"></a>
## Report a problem

Open an issue and include:

- what you were building or printing, with the part number;
- printer, material and slicer settings for print problems;
- photos, if something does not fit.

Build reports are especially welcome, even when everything worked.

<a id="change-a-part"></a>
## Change a part

1. Edit the STEP file in `models/step/`.
2. Export a binary STL with the same name into `models/stl/`.
3. Update `docs/printing.md` and `docs/assembly-guide.md` if names, quantities or fasteners change.
4. Print and fit the part before opening a pull request, and say in the pull request what you tested.

<a id="licence-of-contributions"></a>
## Licence of contributions

Your change is licensed under the licence that already covers the file.

| You are changing | Your contribution is licensed |
|---|---|
| CAD and meshes in `models/` | CERN-OHL-P-2.0 |
| Configuration and CI | Apache-2.0 |
| Documentation and images | CC BY 4.0 |

If a contribution contains material you did not create, say so in the pull request so it can be recorded in `NOTICE`. New files must be covered by `REUSE.toml`. CI runs `reuse lint` and fails otherwise.
<!-- /translated-content -->
