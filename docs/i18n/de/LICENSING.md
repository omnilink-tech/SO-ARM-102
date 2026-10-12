<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Englisches Original](../../../LICENSING.md)

[Dokumentation](README.md) · [Drucken](docs/printing.md) · [Stückliste](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Technische Daten](docs/specifications.md) · [Modelle](models/README.md) · [Mitwirken](CONTRIBUTING.md) · [Lizenzen](LICENSING.md) · [Übersetzungen](docs/translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Lizenzierung

Copyright (c) 2026 Robonine

Dieses Projekt veröffentlicht verschiedene Arten von Material unter verschiedenen Lizenzen, jede Datei in diesem Repository ist genau durch eine davon abgedeckt.

| Material | Lizenz | Text |
|---|---|---|
| Hardware-Designs (CAD, herstellbare Geometrie) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (Konfiguration, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Dokumentationen, Renderings, Fotos und Simulationselemente | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

Die maschinenlesbare Version dieser Karte ist [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` enthält dieselben drei Texte unter ihren SPDX Namen, wie es die REUSE Spezifikation verlangt. Die Kopien im Wurzelverzeichnis sind diejenigen, die von GitHubs Lizenz-Erkennung gelesen werden.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Hardware: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` ist Dokumentation und fällt unter CC-BY-4.0.

Empfohlener Hinweis bei Wiederverwendung dieser Hardware:

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
## 3. Dokumentations- und Simulationsressourcen: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

Alle Dateien unter `simulation/` sind unter CC-BY-4.0 lizenziert, einschließlich der Roboterbeschreibungen in `simulation/urdf/` und den zugehörigen STL Meshes in `simulation/urdf/meshes/`. Die Fertigungsentwürfe unter `models/` bleiben wie oben beschrieben unter CERN-OHL-P-2.0 lizenziert.

Namensnennung für die Wiederverwendung: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Material von Drittanbietern

Keine Datei in diesem Repository wird von einem Dritten kopiert.Siehe [`NOTICE`](NOTICE.md) für die Projekte, auf denen dieses Design basiert.
<!-- /translated-content -->
