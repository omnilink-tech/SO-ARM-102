<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Original en inglés](../../../LICENSING.md)

[Documentación](README.md) · [Impresión](docs/printing.md) · [Materiales](docs/bom.md) · [Montaje](docs/assembly-guide.md) · [Especificaciones](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licencias](LICENSING.md) · [Traducciones](docs/translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licencias

Copyright (c) 2026 Robonine

Este proyecto publica diferentes tipos de material bajo distintas licencias, cada archivo en este repositorio está cubierto por exactamente una de ellas.

| Material | Licencia | Texto |
|---|---|---|
| Diseños de hardware (CAD, geometría fabricable) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (configuración, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentación, renders, fotografías y activos de simulación | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

La versión legible por máquina de este mapa es [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` contiene los mismos tres textos bajo sus SPDX nombres, como lo requiere la especificación REUSE. Las copias en la raíz son las que lee la detección de licencias de GitHub.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Hardware de hardware: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` es documentación y cae bajo CC-BY-4.0.

Aviso recomendado al reutilizar este hardware:

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
## 3. Documentación y recursos de simulación: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

Todos los archivos bajo `simulation/` están licenciados bajo CC-BY-4.0. Esto incluye las descripciones de robots en `simulation/urdf/` y sus mallas referenciadas STL en `simulation/urdf/meshes/`. Los diseños de fabricación bajo `models/` siguen estando licenciados bajo CERN-OHL-P-2.0 como se describe arriba.

Atribución para reutilizar: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Material de terceros

Ningún archivo en este repositorio es copiado de un tercero.Vea [`NOTICE`](NOTICE.md) para los proyectos sobre los que se basa este diseño.
<!-- /translated-content -->
