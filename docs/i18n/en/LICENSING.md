<!-- translation-navigation -->
[English](LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[English source](../../../LICENSING.md)

[Documentation](README.md) · [Printing](docs/printing.md) · [BOM](docs/bom.md) · [Assembly](docs/assembly-guide.md) · [Specifications](docs/specifications.md) · [Models](models/README.md) · [Contributing](CONTRIBUTING.md) · [Licensing](LICENSING.md) · [Translations](docs/translations.md)

> English reference. Shared illustrations and the original PDF booklet are unchanged.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licensing

Copyright (c) 2026 Robonine

This project releases different kinds of material under different licences. Every file in this repository is covered by exactly one of them.

| Material | Licence | Text |
|---|---|---|
| Hardware designs (CAD, manufacturable geometry) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (configuration, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentation, renders, photographs and simulation assets | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

The machine-readable version of this map is [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` holds the same three texts under their SPDX names, as the REUSE Specification requires. The copies at the root are the ones GitHub's licence detection reads.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Hardware: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` is documentation and falls under CC-BY-4.0.

Recommended notice when reusing this hardware:

```
Copyright (c) 2026 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

<a id="2-software-apache-20"></a>
## 2. Software: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. Documentation and simulation assets: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

All files under `simulation/` are licensed under CC-BY-4.0. This includes the robot descriptions in `simulation/urdf/` and their referenced STL meshes in `simulation/urdf/meshes/`. The fabrication designs under `models/` remain licensed under CERN-OHL-P-2.0 as described above.

Attribution for reuse: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Third-party material

No file in this repository is copied from a third party. See [`NOTICE`](NOTICE.md) for the projects this design builds on.
<!-- /translated-content -->
