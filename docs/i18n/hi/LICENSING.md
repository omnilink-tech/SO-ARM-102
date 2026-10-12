<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](LICENSING.md) · [العربية](../ar/LICENSING.md)

[अंग्रेज़ी मूल](../../../LICENSING.md)

[दस्तावेज़](README.md) · [प्रिंटिंग](docs/printing.md) · [सामग्री सूची](docs/bom.md) · [असेंबली](docs/assembly-guide.md) · [विनिर्देश](docs/specifications.md) · [मॉडल](models/README.md) · [योगदान](CONTRIBUTING.md) · [लाइसेंस](LICENSING.md) · [अनुवाद](docs/translations.md)

> यह दस्तावेज़ का पूर्ण अनुवाद है। चित्र और मूल PDF पुस्तिका सभी भाषाओं में साझा हैं। अनुवाद AI की सहायता से तैयार किया गया है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# लाइसेंस संबंधी जानकारी

सर्वाधिकार 2026 Robonine

यह परियोजना विभिन्न लाइसेंस के अंतर्गत विभिन्न प्रकार की सामग्री जारी करती है. इस भंडार में प्रत्येक फ़ाइल को उनमें से एक द्वारा कवर किया जाता है.

| सामग्री | लाइसेंस | पाठ |
|---|---|---|
| हार्डवेयर डिजाइन (CAD, निर्माण योग्य ज्यामिति) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| सॉफ्टवेयर (विन्यास, सीआई) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| दस्तावेज़ीकरण, रेंडर, फोटोग्राफ़ और सिमुलेशन संपत्ति | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

इस नक्शे का मशीन-पढ़ने योग्य संस्करण है [`REUSE.toml`](../../../REUSE.toml). `LICENSES/` अपने SPDX नाम के तहत एक ही तीन पाठ रखता है, जैसा कि REUSE विनिर्देशन की आवश्यकता होती है. रूट पर प्रतिलिपि वे हैं जिन्हें GitHub के लाइसेंस पता लगाना पढ़ता है.

<a id="1-hardware-cern-ohl-p-20"></a>
## 1. हार्डवेयर: CERN-OHL-P-2.0

```
models/step/    *.STEP
models/stl/     *.stl
models/3mf/     *.3mf (geometry and slicer projects)
```

`models/README.md` दस्तावेज़ीकरण है और CC-BY-4.0 के अंतर्गत आता है.

इस हार्डवेयर को फिर से उपयोग करने पर सिफारिश की गई चेतावनी:

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
## 2. सॉफ्टवेयर: Apache-2.0

```
.github/    .pre-commit-config.yaml    .gitignore    .gitattributes
```

<a id="3-documentation-and-simulation-assets-cc-by-40"></a>
## 3. दस्तावेज़ीकरण और सिमुलेशन संपत्ति: CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, CLAUDE.md, NOTICE
docs/             *.md, *.pdf
assets/images/    *.jpg
assets/video/     *.mp4, *.gif
simulation/       all files, including URDF/Xacro descriptions, meshes and export metadata
every other README.md in the repository
```

`simulation/` के नीचे की सभी फ़ाइलें CC-BY-4.0 के तहत लाइसेंस प्राप्त हैं. इसमें `simulation/urdf/` में रोबोट वर्णन तथा `simulation/urdf/meshes/` में उनके संदर्भित STL मेश शामिल हैं. `models/` के नीचे का निर्माण डिजाइन CERN-OHL-P-2.0 के तहत लाइसेंस प्राप्त है जैसा कि ऊपर वर्णित है.

 पुनर्प्रयोग के लिए श्रेय: "Robonine, SO-ARM 102, https://github.com/roboninecom/SO-ARM-102, CC BY 4.0"।

<a id="4-third-party-material"></a>
## 4. तीसरे पक्ष की सामग्री

इस भंडार में कोई फ़ाइल तीसरे पक्ष से नक़ल नहीं है. देखें [`NOTICE`](NOTICE.md) परियोजनाओं के लिए जो इस डिजाइन पर आधारित हैं.
<!-- /translated-content -->
