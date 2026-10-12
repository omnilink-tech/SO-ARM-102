<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[英語原文](../../../LICENSING.md)

[ドキュメント](README.md) · [印刷](docs/printing.md) · [部品表](docs/bom.md) · [組立](docs/assembly-guide.md) · [仕様](docs/specifications.md) · [モデル](models/README.md) · [貢献方法](CONTRIBUTING.md) · [ライセンス](LICENSING.md) · [翻訳](docs/translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# ライセンス

著作権 (c) 2026 Robonine

このプロジェクトは様々なライセンスのもとで様々な種類の素材をリリースしています。このリポジトリにあるすべてのファイルは、正確に一つのライセンスで保護されています。

| 材料 | ライセンス | 本文 |
|---|---|---|
| ハードウェア設計 (CAD、製造可能な幾何学) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| ソフトウェア（設定、CI） | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| 文書、レンダリング、写真、シミュレーション資産 | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

このマップの機械読み取れるバージョンは [`REUSE.toml`](../../../REUSE.toml)です。 `LICENSES/` は REUSE 仕様が要求するように SPDX 名前で同じ三つのテキストを含んでいます。ルートにあるコピーは GitHub のライセンス検出が読むものです。

<a id="1-hardware-cern-ohl-p-20"></a>
## 1。ハードウェア:CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` は文書であり、CC-BY-4.0 に属します。

このハードウェアを再利用する際の注意事項:

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
## 2。ソフトウェア:Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3。文書化とシミュレーション資産:CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

`simulation/` のファイルはすべて CC-BY-4.0 でライセンスされています。これには `simulation/urdf/` のロボット記述と `simulation/urdf/meshes/` の参照 STL メッシュが含まれています。`models/` の製造設計は上記のように CERN-OHL-P-2.0 でライセンスされています。

再利用のための属性: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0"。

<a id="4-third-party-material"></a>
## 4. サードパーティ素材

このリポジトリのファイルは第三者からコピーされていません。このデザインを構築するプロジェクトについては [`NOTICE`](NOTICE.md) を参照してください。
<!-- /translated-content -->
