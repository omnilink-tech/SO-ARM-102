<div dir="rtl" lang="ar">

<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../README.md)

[الوثائق](README.md) · [الطباعة](docs/printing.md) · [قائمة المواد](docs/bom.md) · [التجميع](docs/assembly-guide.md) · [المواصفات](docs/specifications.md) · [النماذج](models/README.md) · [المساهمة](CONTRIBUTING.md) · [التراخيص](LICENSING.md) · [الترجمات](docs/translations.md)

> هذه ترجمة كاملة للوثيقة. الرسوم وكتيب PDF الأصلي مشتركة بين اللغات. أعدت الترجمة بمساعدة الذكاء الاصطناعي ولم يراجعها متحدثون أصليون بعد.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [مشاهدة الفيديو المسبق](../../../assets/video/so-arm-102-preview.mp4)**·**🛒 [شراء المجموعة](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**طقم مفتوح المصدر يضم ذراعًا قائدة وذراعًا تابعة مع 5 درجات حرية وماسك، للتشغيل عن بعد والتعلم بالتقليد. صممه [Robonine](https://robonine.com) ليكون خلفًا أكثر صلابة وسرعة للطراز SO-ARM 101.**

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![الحالة:0.1 قبل اﻹصدار](https://img.shields.io/badge/Status-v0.1%20pre--release-orange.svg)](#-known-issues)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**ميزانية التجميع الذاتي: ~$404 للمكونات، أو ~$444 مع مواد الطباعة.** [ملخص قائمة المواد](#bill-of-materials) · [التكاليف التفصيلية وروابط الشراء](docs/bom.md#estimated-kit-cost)

> هل تفضل عدم الحصول على الأجزاء وطباعتها بنفسك؟ **[شراء مجموعة SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## ✨ ما الذي تغير مقابل SO-ARM 101

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| القابض | فك زاوي | مقبض متوازي، نطاق 85 mm |
| مادة الهيكل | PLA | PET-CF (Fiberon PET-CF17 مختبر) |
| البنية | وصلات مصمتة | وصلات محسنة طوبولوجيًا |
| نطاق دوران القاعدة | 220° | **352°** |
| المدى الأفقي | 441 mm | **483 mm** |
| الانحراف عند الممسكة، 300 g الحمولة(1) | 7.5 mm | **3.4–3.9 mm** |
| سرعة الكتف والمرفق | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| الضجيج عند 1 م | 70 dB | **60 dB** |

(1) كلا الذراعين الروبوتيين مصنوعان من نماذج مطبوعة لمحركات الخدمة، وبالتالي فإن الإطار هو الذي يتم مقارنته، لا المحركات. وترد النتائج الكاملة وظروف الاختبار في [docs/specifications.md](docs/specifications.md).

الذراع الروبوتية تحتفظ بالتخطيط المشترك SO-ARM 101، لذا فهي تعمل مع [Hugging Face LeRobot](https://github.com/huggingface/lerobot) مجموعات البيانات والسياسات.

---

<a id="-preview"></a>
## فيديو:

<div align="center">

[![SO-ARM 102 استعراض](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*انقر للفيديو الكامل، 21 s*

</div>

---

<a id="-configurations"></a>
## 🤝 التشكيلات

<a id="single-arm-one-leader--one-follower"></a>
### ذراع آلي واحد: ذراع آلي رئيسي + ذراع آلي متابعة

المجموعة القياسية، تحرك ذراع الروبوت القائد يدويا، ويكرر ذراع الروبوت المتتبع الحركة، استخدمه للتشغيل من بعد ولتسجيل العروض للتعلم عن طريق المحاكاة.

![ذراع قائدة وذراع تابعة](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### ثنائية: قائدان + متبعان

هناك مجموعتان من الروبوتات جنبا إلى جنب، كل يد تقود ذراع روبوت القائد الخاص بها، بحيث يمكن للمتتبعين نقل الأشياء، أو الحصول على جزء والعمل عليه، أو القيام بأي مهمة تتطلب يديك.

![ذراعان قائدتان وذراعان تابعتان](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### الذراعان الروبوتيان

| الذراع التابع | الذراع القائد |
|:-:|:-:|
| ![الذراع التابعة](../../../assets/images/renders/follower.jpg) | ![الذراع القائدة](../../../assets/images/renders/leader.jpg) |
| أجهزة تصوير موازية، آلة تصوير بالمعصم، 12 V | يد مع زناد، 5 V |

---

<a id="-build-it-in-four-steps"></a>
## بنّيه في أربع خطوات

هل تفضل مجموعة جاهزة؟ **[شراء المجموعة SO-ARM 102](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

<a id="1-print-the-parts"></a>
### 1. طباعة الأجزاء

تتناسب الأجزاء الفردية مع لوحة بناء طابعة ثلاثية الأبعاد 180 × 180 mm. الجزء الأكبر طوله 160 mm. وتستخدم أشكال اللوحات 3MF الموردة لوحة بناء طابعة ثلاثية الأبعاد 256 × 256 mm.

- مشاريع 3MF لقطع اللحوم مع حفظ إعدادات التوجيه والدعم: [`models/3mf/`](../../../models/3mf) - [ذراع روبوت رئيسي](../../../models/3mf/SO102_leader.3mf)، [ذراع روبوت متابعة](../../../models/3mf/SO102_follower.3mf)، [ممسكة ذراع روبوت متابعة وحقيبة لوحة](../../../models/3mf/SO102_follower_gripper_box.3mf)
- محتويات المشروع وملامح الطابعات: [نماذج/README.md](models/README.md)
- STL ملف جاهز للتقطيع: [`models/stl/`](../../../models/stl)
- مصادر STEP: [`models/step/`](../../../models/step)
- كميات المواد والترتيبات والأجزاء: [docs/printing.md](docs/printing.md)

وقد أعطت الوضعيات السابقة لاختبار الذراع الروبوتي تقديرات للشرائح تبلغ نحو 500 g من الفتيل و21 h لأجزاء الذراع الروبوتي، باستثناء الملقط. شق مرة أخرى باستخدام شرائح الطباعة الثلاثية الأبعاد مشاريع 3MF للتقديرات الحالية.

<a id="2-buy-the-hardware"></a>
### 2. شراء المعدات

مصادر المكونات من [موجز قائمة المواد](#bill-of-materials) و[قائمة المواد الكاملة مع روابط الشراء](docs/bom.md). ميزانية ** $404.09**للمكونات، أو** $443.68** بما في ذلك مواد الطباعة، قبل الشحن والضرائب.

| الذراع | محركات السيرفو | وحدة التحكم | التغذية الكهربائية |
|---|---|---|---|
| الذراع التابع | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Driver HAT | **12 V** |
| الذراع القائد | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **تعمل الذراع القائدة بجهد 5 V والذراع التابعة بجهد 12 V.** لا تبدّل مزوّدي الطاقة بينهما.

<a id="3-assemble"></a>
### 3. جمع

- كتيب قابل للطباعة، 36 صفحة A5: [docs/SO-ARM102_assembly_A5_v0.6.pdf](../../SO-ARM102_assembly_A5_v0.6.pdf)
- قائمة الخطوات مع الأجزاء ووسائل التثبيت: [docs/assembly-guide.md](docs/assembly-guide.md)

الأدوات: المفاتيح السداسية 1.5 mm (M2 مسمار) و 2 mm (M3 مسمار).

<a id="4-set-up-the-software"></a>
### 4. تثبيت البرمجيات

هويات السيرفو، المعايرة والدروس: **[lab.robonine.com](https://lab.robonine.com)**. يستخدم الذراع الروبوتي تدفق العمل LeRobot SO-101 الذراع الروبوتي الرائد/ذراع الروبوت المتتبع.

---

<a id="bill-of-materials"></a>
## قائمة المواد

الكميات والتكاليف المرجعية لـ ** ذراع روبوتي رئيسي واحد + ذراع روبوتي تابع واحد**:

| روابط الفئة/الشراء | محتويات الطقم | الإجمالي (USD) |
|---|---|---:|
| [محركات السيرفو](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $283.62 |
| [الإلكترونيات](docs/bom.md#electronics) | 2 أجهزة تحكم، 2 إمدادات كهربائية، 2 كابلات USB، 1 كاميرات للمعصم | $71.50 |
| [الأجزاء الميكانيكية](docs/bom.md#mechanical-parts) | 4 محامل، 2 قضبان توجيهية من الفولاذ، 4 صمامات طاولة | $37.76 |
| [المثبتات](docs/bom.md#fasteners) | مسننات وملحقات؛ تشمل مسننات محددة لمجموعات محركات الخدمة | $11.21 |
| **المجموع الفرعي للمكونات** |  | **$404.09** |
| [المواد المطبوعة](docs/bom.md#printing-materials) | 0.6 kg PET-CF17 + 0.6 kg PETG مخصص | $39.59 |
| **الإجمالي مع مواد الطباعة** |  | **$443.68** |

تبلغ تكلفة شراء العبوات الكاملة وأسلاك الفتيل من الصفر حوالي **$504**، بما في ذلك قطع الغيار غير المستخدمة. هذه تقديرات مرجعية، وليست عروضا جديدة من الموردين. لا يشمل الشحن والضرائب والأدوات والحاسوب والطابعة والكهرباء وعمالة التجميع. تأكد من أسعار الموردين والمتغيرات والحد الأدنى لكميات الطلب قبل الشراء؛ تقطيع مرة أخرى باستخدام شريحة الطباعة ثلاثية الأبعاد 3MF مشاريع للتحقق من استهلاك الفتيل.

[قائمة المشتريات الكاملة، وصلات الشراء وافتراضات التكلفة](docs/bom.md#estimated-kit-cost).

---

<a id="urdf-export"></a>
## URDF تصدير

التصدير الحالي المستقل هو في [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro). إبق `meshes/` بجانب ملفات الوصف؛ مسارات الشبكة هي نسبية لهذا المجلد.

- **المواد البصرية:**STL** الاصطدامات:** صناديق مركبة تدور بصورة مستقلة على جميع الوصلات الثماني.
- ** تقدير الكتلة:** PLA، 30 في المائة ملء، 6 محيطات، 6 طبقات أعلى/أسفل، 0.2 mm ارتفاع الطبقة، و**0.40 mm عرض الانبثاق**. هذه افتراضات محاكاة؛ استخدم [دليل الطباعة](docs/printing.md) لتحديد إعدادات التصنيع.
- ** كتلة المعدات:** ستة محركات عند 70 g كل منها؛ 105 gالكتلة الكلية المقدرة للنموذج:**0.889 kg** ﻻ ينطبق.
- **المقبض:** `clamp2` يحاكي `clamp1` مع مضاعف `-1`.

وتسجل الافتراضات في [إعدادات التصدير](../../../simulation/urdf/export_settings.json) و[خواص الكتلة](../../../simulation/urdf/mass_properties.json). [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## هيكل المستودع

```
├── models/
│   ├── 3mf/                 # مشاريع تقطيع: ذراع روبوتي رئيسي، وذرع روبوتي متابعة، وممسك وحالة لوحة
│   ├── stl/                 # شبكات جاهزة للطباعة
│   │   ├── common/          # أجزاء تستخدمها ذراعي الروبوتين
│   │   ├── follower/        # أجهزة تمسّك متوازية، ومثبتات للكاميرات، وحقيبة لوحات
│   │   └── leader/          # يد، زناد، معصم، علبة لوحة
│   └── step/                # مصادر CAD، نفس التصميم كما في stl/
├── docs/
│   ├── printing.md          # المادة، وضوابط المقطعة، والكميات
│   ├── bom.md               # قائمة المواد
│   ├── assembly-guide.md    # قائمة الخطوات مع الأجزاء والملحقات
│   ├── specifications.md    # الهندسة، محركات الخدمة، نتائج القياسات مقابل SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.6.pdf
├── assets/
│   ├── images/              # صور فوتوغرافية، ورسوم بيانية، وصفحات كتيب، وصور اختبار
│   └── video/               # عرض مسبق للفيديو والصورة المتحركة
├── LICENSING.md             # ما هو الترخيص الذي يغطي أي ملف
└── NOTICE                   # إسناد الحقوق إلى طرف ثالث
```

---

<a id="-known-issues"></a>
## المسائل المعروفة

هذا هو أول إصدار عام. وجدت عملية بناء اختبار مستقلة ما يلي. يجري تصحيحها وسوف تهبط في الإصدار القادم.

1. **أُبلغ عن نقص نموذجين من مجموعة الإطلاق**. واحد معروف: حامل الكاميرا لا يزال يفتقر إلى مصدر STEP.
2. **M2 البراغي يصعب الوصول إليها في أماكن عديدة.** توقع القتال مع عدد قليل منها.
3. ** تسير المشابك الشديدة على قضبان كربونية.** وثقوب المشابك مصممة لـ 6.1 mm وتختلف أقطار القضبان بين الموردين، ولذلك يتعين التحقق من ملاءمتها قبل التجميع.
4. **فحص أطوال كابلات المحركات المساعدة** قبل إغلاق كل مفصل، وخاصة من القاعدة إلى الكتف.
5. ** ترتيب التجميع غير مناسب في مكانين** من الكتيب، اقرأ خطوتين قبل تثبيتها.
6. **قد تبدو مفاصل الذراع القائدة مرتخية.** إضافة حلقات مطاطية على شكل O بمقاس 8 × 2 mm بين كل سيرفو وذراعه تمنح الذراع القائدة احتكاكًا سلسًا وهادئًا. استخدم حلقتين لكل سيرفو في المفاصل 1–4 وحلقة واحدة في المفاصل 5–6.

هل وجدت شيئًا آخر؟ الرجاء [فتح قضية](https://github.com/roboninecom/SO-ARM-102/issues).

---

<a id="-related-projects"></a>
## المشاريع ذات الصلة

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)، المضخة التي نمت منها المضخة SO-ARM 102
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) بحلول TheRobotStudio، الذراع الروبوتية هذا التصميم ينجح
- [مقارنة عملية لمحركات الخدمة المتسلسلة الذكية](https://robonine.com/smart-serial-servo-motor-comparison-robotics/)، الاختبارات التي تستند إليها اختيار محرك الخدمة
- [اختيار خيوط لأذرع الروبوتات](https://robonine.com/choosing-filament-for-robotic-arm-applications/)، الاختبارات التي تجريها PET-CF

---

<a id="-license"></a>
## الترخيص

حقوق التأليف والنشر (ج) 2026 Robonine. وتحمل الأنواع المختلفة من المواد تراخيص مختلفة:

| المادة | الترخيص |
|---|---|
| تصاميم المعدات في `models/` | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| البرمجيات وتشكيلها | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| الوثائق والصور في `docs/` و`assets/` وجميع `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

انظر [LICENSING.md](LICENSING.md) و[REUSE.toml](../../../REUSE.toml) للحصول على خريطة الملف حسب الملف.

---

<a id="-team"></a>
## 👥 الفريق

| الاسم | الدور | التواصل |
|------|------|---------|
| **Alan Subin** | مهندس تصميم: التصميم الميكانيكي، CAD، كتيب التجميع | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | مهندس برامجيات واختبارات: النماذج الأولية، والطباعة، وأدوات الاختبار | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | مدير مشروع | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | المصمم الصناعي: مظهر وشكل ذراع الروبوت | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | مهندس هيكلي: نماذج الجاذبية، تغييرات التصميم للحد من الانحراف | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | مهندس هيكلي: تحليل القوة والتحليل الحراري، وتحقيق الاستفادة المثلى من الطوبولوجيا | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | مختبر وخبير استشاري: بناء مستقل للاختبار | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**بنيت لمجتمع الروبوتات من قبل [Robonine](https://robonine.com)** 🤖

</div>
<!-- /translated-content -->

</div>
