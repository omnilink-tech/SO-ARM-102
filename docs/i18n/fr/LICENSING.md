<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Original anglais](../../../LICENSING.md)

[Documentation](README.md) · [Impression](docs/printing.md) · [Composants](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Caractéristiques](docs/specifications.md) · [Modèles](models/README.md) · [Contribuer](CONTRIBUTING.md) · [Licences](LICENSING.md) · [Traductions](docs/translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licences

Copyright (c) 2026 Robonine

Ce projet publie différents types de matériel sous différentes licences, chaque fichier dans ce dépôt est couvert par exactement une d'entre elles.

| Matériau | Licence | Texte |
|---|---|---|
| Conception de matériel (CAD, géométrie fabriquable) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Logiciels (configuration, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentation, rendus, photographies et ressources de simulation | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

La version lisible par machine de cette carte est [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` contient les mêmes trois textes sous leurs SPDX noms, comme l'exige la spécification REUSE. Les copies à la racine sont celles que lit la détection de licence de GitHub.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Matériel: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` est une documentation et relève de CC-BY-4.0.

Remarque recommandée lors de la réutilisation de ce matériel:

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
## 2. Logiciels: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. Documentation et ressources de simulation: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

Tous les fichiers sous `simulation/` sont licenciés sous CC-BY-4.0. Cela inclut les descriptions de robots dans `simulation/urdf/` et leurs maillages référencés STL dans `simulation/urdf/meshes/`. Les conceptions de fabrication sous `models/` restent sous licence CERN-OHL-P-2.0 comme décrit ci-dessus.

Attribution pour réutilisation : "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Matériel de tiers

Aucun fichier dans ce dépôt n'est copié d'un tiers.Voir [`NOTICE`](NOTICE.md) pour les projets sur lesquels cette conception est basée.
<!-- /translated-content -->
