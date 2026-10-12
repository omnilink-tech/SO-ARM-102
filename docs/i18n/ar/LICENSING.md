<div dir="rtl" lang="ar">

<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](LICENSING.md)

[الأصل الإنجليزي](../../../LICENSING.md)

[الوثائق](README.md) · [الطباعة](docs/printing.md) · [قائمة المواد](docs/bom.md) · [التجميع](docs/assembly-guide.md) · [المواصفات](docs/specifications.md) · [النماذج](models/README.md) · [المساهمة](CONTRIBUTING.md) · [التراخيص](LICENSING.md) · [الترجمات](docs/translations.md)

> هذه ترجمة كاملة للوثيقة. الرسوم وكتيب PDF الأصلي مشتركة بين اللغات. أعدت الترجمة بمساعدة الذكاء الاصطناعي ولم يراجعها متحدثون أصليون بعد.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# التراخيص

حقوق النشر (c) 2026 Robonine

ينشر هذا المشروع أنواعا مختلفة من المواد تحت تراخيص مختلفة، وكل ملف في هذا المستودع مغطى بواحد منها بالضبط.

| المادة | الترخيص | النص |
|---|---|---|
| تصميمات المعدات (CAD، هندسة قابلة للتصنيع) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| البرمجيات (التشكيل، ونظام المعلومات الإدارية المتكامل) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| الوثائق والرسوم البيانية والصور وأصول المحاكاة | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

النسخة القابلة للقراءة الآلية من هذه الخريطة هي [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` تحتوي على نفس النصوص الثلاثة تحت أسمائهم SPDX، كما يتطلب المواصفات REUSE. النسخ في الجذر هي التي تقرأها كشف ترخيص GitHub.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1:: المعدات: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` هي وثائق وتندرج تحت CC-BY-4.0.

ملاحظة موصى بها عند إعادة استخدام هذه المعدات:

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
## 2:: البرمجيات: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## (ج) 3 - أصول التوثيق والمحاكاة: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

جميع الملفات تحت `simulation/` مرخصة بموجب الترخيص CC-BY-4.0. وهذا يشمل أوصاف الروبوتات في `simulation/urdf/` وشبكاتها المرجعية STL في `simulation/urdf/meshes/`. وتظل تصاميم التصنيع تحت `models/` مرخصة بموجب الترخيص CERN-OHL-P-2.0 كما هو موصوف أعلاه.

إعادة الاستخدام: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0".

<a id="4-third-party-material"></a>
## 4. مواد الأطراف الثالثة

لا يوجد ملف في هذا المستودع تم نسخه من طرف ثالث. انظر [`NOTICE`](NOTICE.md) للمشاريع التي يستند عليها هذا التصميم.
<!-- /translated-content -->

</div>
