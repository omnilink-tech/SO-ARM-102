<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Английский оригинал](../../../LICENSING.md)

[Документация](README.md) · [Печать](docs/printing.md) · [Комплектующие](docs/bom.md) · [Сборка](docs/assembly-guide.md) · [Характеристики](docs/specifications.md) · [Модели](models/README.md) · [Участие](CONTRIBUTING.md) · [Лицензирование](LICENSING.md) · [Переводы](docs/translations.md)

> Полный перевод документа. Изображения и исходный PDF-буклет общие для всех языков. Перевод подготовлен с помощью ИИ; проверка носителями языка ещё не проведена.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Лицензирование

Авторские права (c) 2026 Robonine

Разные материалы проекта распространяются по разным лицензиям. Каждый файл покрыт ровно одной из них.

| Материал | Лицензия | Текст |
|---|---|---|
| Аппаратные модели (CAD, геометрия для изготовления) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| ПО (конфигурация, CI) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Документация, рендеры, фотографии и файлы симуляции | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

Машиночитаемое распределение лицензий: [`REUSE.toml`](../../../REUSE.toml). В `LICENSES/` хранятся те же три текста под именами SPDX, как требует спецификация REUSE. Копии в корне используются GitHub для определения лицензии.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. Аппаратные модели: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` — документация, распространяемая по CC-BY-4.0.

Рекомендуемое уведомление при повторном использовании аппаратной разработки:

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
## 2. ПО: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. Документация и файлы симуляции: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

Все файлы в `simulation/` распространяются по CC-BY-4.0, включая описания робота в `simulation/urdf/` и соответствующие сетки STL в `simulation/urdf/meshes/`. Производственные модели в `models/` по-прежнему распространяются по CERN-OHL-P-2.0, как указано выше.

Указание авторства при повторном использовании: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. Сторонние материалы

Ни один файл репозитория не скопирован у третьих лиц. Проекты, на которых основана конструкция, перечислены в [`NOTICE`](NOTICE.md).
<!-- /translated-content -->
