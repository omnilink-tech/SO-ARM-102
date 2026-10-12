<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[英文原文](../../../LICENSING.md)

[文档](README.md) · [打印](docs/printing.md) · [物料清单](docs/bom.md) · [装配](docs/assembly-guide.md) · [规格](docs/specifications.md) · [模型](models/README.md) · [参与贡献](CONTRIBUTING.md) · [许可说明](LICENSING.md) · [翻译](docs/translations.md)

> 本文为完整译文。各语言共用插图和原始 PDF 手册。翻译由人工智能辅助完成，尚未经母语使用者审校。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# 许可说明

版权(c) 2026 Robonine

这个项目在不同的许可证下发布不同类型的材料,本存储库中的每个文件都由其中一个许可证覆盖。

| 材料 | 许可证 | 文本 |
|---|---|---|
| 硬件设计 (CAD, 可制造几何形状) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| 软件(配置、集成电路) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| 文档、渲染图、照片和模拟资产 | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

该映射的机器可读版本是 [ `REUSE.toml` ](../../../REUSE.toml) 。 `LICENSES/` 包含了SPDX名下相同的三个文本,正如 REUSE 规范所要求的那样。 在根目录中的副本是 GitHub 许可证检测读取的。

<a id="1-hardware-cern-ohl-p-20"></a>
## 1硬件： CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` 是文档,属于 CC-BY-4.0。

重新使用此硬件时建议注意:

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
## 2软件:Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. 文档和模拟资产:CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

`simulation/` 下的所有文件都在 CC-BY-4.0 下授权,包括 `simulation/urdf/` 中的机器人描述和 `simulation/urdf/meshes/` 中的参考 STL 网格。 `models/` 下的制造设计仍然如上所述在 CERN-OHL-P-2.0 下授权。

 重用的归属：“Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0”。

<a id="4-third-party-material"></a>
## 4 。 第三方材料

此存储库中的文件没有从第三方复制。 请参阅 [`NOTICE` ](NOTICE.md) 以了解此设计基于的项目。
<!-- /translated-content -->
