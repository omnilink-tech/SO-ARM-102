<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[अंग्रेज़ी मूल](../../../CONTRIBUTING.md)

[दस्तावेज़](README.md) · [प्रिंटिंग](docs/printing.md) · [सामग्री सूची](docs/bom.md) · [असेंबली](docs/assembly-guide.md) · [विनिर्देश](docs/specifications.md) · [मॉडल](models/README.md) · [योगदान](CONTRIBUTING.md) · [लाइसेंस](LICENSING.md) · [अनुवाद](docs/translations.md)

> यह दस्तावेज़ का पूर्ण अनुवाद है। चित्र और मूल PDF पुस्तिका सभी भाषाओं में साझा हैं। अनुवाद AI की सहायता से तैयार किया गया है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# योगदान

SO-ARM 102 को बेहतर बनाने में मदद के लिए धन्यवाद.

<a id="report-a-problem"></a>
## समस्या बताएँ

एक मुद्दा खोलें और शामिल करें:

- आप क्या निर्माण या मुद्रण कर रहे थे, भाग संख्या के साथ;
- छपाई समस्याओं के लिए प्रिंटर, सामग्री तथा स्लाइसर विन्यास;
- फोटो, अगर कुछ फिट नहीं है.

बिल्ड रिपोर्ट विशेष रूप से स्वागत है, यहां तक कि जब सब कुछ काम किया.

<a id="change-a-part"></a>
## पुर्ज़ा बदलें

1. STEP फ़ाइल को `models/step/` में संपादित करें.
2. `models/stl/` में समान नाम के साथ बाइनरी STL निर्यात करें.
3. `docs/printing.md` और `docs/assembly-guide.md` को अद्यतन करें यदि नाम, मात्रा या फास्टनर बदलें.
4.  एक pull अनुरोध खोलने से पहले भाग को प्रिंट और फिट करें, और pull अनुरोध में कहें कि आपने क्या परीक्षण किया है।

<a id="licence-of-contributions"></a>
## योगदान का लाइसेंस

आपका परिवर्तन लाइसेंस के तहत है जो पहले से ही फ़ाइल को कवर करता है.

| आप बदल रहे हैं | आपका योगदान लाइसेंस है |
|---|---|
| CAD और `models/` में मेश | CERN-OHL-P-2.0 |
| कॉन्फ़िगरेशन तथा सीआई | Apache-2.0 |
| दस्तावेज़ीकरण तथा छवियाँ | CC BY 4.0 |

यदि योगदान में सामग्री है जिसे आपने नहीं बनाया है, पुल अनुरोध में ऐसा कहें ताकि इसे `NOTICE` में रिकॉर्ड किया जा सके. नई फ़ाइलें `REUSE.toml` द्वारा कवर की जानी चाहिए. CI चलाता है `reuse lint` और अन्यथा असफल होता है.
<!-- /translated-content -->
