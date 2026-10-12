<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Original em inglês](../../../LICENSING.md)

[Documentação](README.md) · [Impressão](docs/printing.md) · [Materiais](docs/bom.md) · [Montagem](docs/assembly-guide.md) · [Especificações](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licenças](LICENSING.md) · [Traduções](docs/translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licenciamento

Direitos autorais (c) 2026 Robonine

Este projeto libera diferentes tipos de material sob licenças diferentes, cada arquivo neste repositório é coberto por exatamente uma delas.

| Material | Licença | Texto |
|---|---|---|
| Projetos de hardware (CAD, geometria manufaturável) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (configuração, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentação, renderizações, fotografias e ativos de simulação | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

A versão legível por máquina deste mapa é [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` contém os mesmos três textos sob seus SPDX nomes, como a Especificação REUSE requer. As cópias na raiz são as que a detecção de licença do GitHub lê.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Hardware: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` é documentação e se enquadra em CC-BY-4.0.

Aviso recomendado ao reutilizar este hardware:

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
## 2. Software de software: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. Ativos de documentação e simulação: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

Todos os arquivos sob `simulation/` são licenciados sob CC-BY-4.0. Isso inclui as descrições de robôs em `simulation/urdf/` e suas malhas referenciadas STL em `simulation/urdf/meshes/`. Os projetos de fabricação sob `models/` permanecem licenciados sob CERN-OHL-P-2.0 como descrito acima.

Atribuição para reutilização: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Material de terceiros

Nenhum arquivo neste repositório é copiado de terceiros.Veja [`NOTICE`](NOTICE.md) para os projetos em que este design se baseia.
<!-- /translated-content -->
