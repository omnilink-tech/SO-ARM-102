<div dir="rtl" lang="ar">

<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](CONTRIBUTING.md)

[الأصل الإنجليزي](../../../CONTRIBUTING.md)

[الوثائق](README.md) · [الطباعة](docs/printing.md) · [قائمة المواد](docs/bom.md) · [التجميع](docs/assembly-guide.md) · [المواصفات](docs/specifications.md) · [النماذج](models/README.md) · [المساهمة](CONTRIBUTING.md) · [التراخيص](LICENSING.md) · [الترجمات](docs/translations.md)

> هذه ترجمة كاملة للوثيقة. الرسوم وكتيب PDF الأصلي مشتركة بين اللغات. أعدت الترجمة بمساعدة الذكاء الاصطناعي ولم يراجعها متحدثون أصليون بعد.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# المساهمة

شكراً لك على مساعدتك في تحسين SO-ARM 102.

<a id="report-a-problem"></a>
## الإبلاغ عن مشكلة

فتح قضية وتضمينها ما يلي:

- ماذا كنت تصنع أو تطبع، مع رقم الجزء؛
- (أ) إعدادات الطابعة والمادة والمقطعة لمشاكل الطباعة؛
- صور، إذا كان هناك شيء لا يتناسب.

تقارير البناء هي موضع ترحيب خاص، حتى عندما كل شيء يعمل.

<a id="change-a-part"></a>
## تعديل جزء

1. تحرير الملف STEP في `models/step/`.
2. تصدير ثنائي STL بنفس الاسم إلى `models/stl/`.
3. تحديث `docs/printing.md` و`docs/assembly-guide.md` إذا تغيرت الأسماء أو الكميات أو الملحقات.
4. طبع وتطابق الجزء قبل فتح طلب سحب، وقول في طلب السحب ما قمت باختباره.

<a id="licence-of-contributions"></a>
## ترخيص المساهمات

تغييرك مرخص بموجب الرخصة التي تغطي الملف بالفعل.

| أنت تتغير | مساهمتك مرخصة |
|---|---|
| CAD وشبكة في `models/` | CERN-OHL-P-2.0 |
| التشكيل والاتصالات المتكاملة | Apache-2.0 |
| الوثائق والصور | CC BY 4.0 |

إذا كانت المساهمة تحتوي على مواد لم تنشئها، ذكر ذلك في طلب السحب بحيث يمكن تسجيلها في `NOTICE`. يجب أن تكون الملفات الجديدة مغطاة بواسطة `REUSE.toml`. سيعمل CI `reuse lint` ويفشل خلاف ذلك.
<!-- /translated-content -->

</div>
