<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 مع LeRobot

استخدم [إضافة SO-ARM 102](https://github.com/roboninecom/SO-ARM-102-Lerobot) التي تُصان بشكل منفصل مع Hugging Face LeRobot. تدعم مزيج محركات STS3235 وSTS3250 وSTS3215 في الذراع التابع.

<a id="install"></a>
## التثبيت

استخدم Python 3.12 واتبع [دليل تثبيت LeRobot](https://huggingface.co/docs/lerobot/en/installation) لتجهيز متطلبات المنصة. في البيئة المفعّلة:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## الإعداد والتحكم

استخدم `so_arm102_follower` للذراع التابع والنوع القياسي `so101_leader` للذراع القائد SO-101 أو SO-ARM 102.

اتبع تعليمات الإضافة لـ[إعداد المحركات](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up) و[المعايرة](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) و[التحكم عن بُعد](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). تجاوز إعداد المحركات إذا كان الذراع معدّاً بالفعل. استبدل منافذ الأمثلة بمنافذك واحتفظ بمعرّفات الأذرع نفسها بعد المعايرة.

إصدار الحزمة المحدد هو إصدار ألفا. تبقى الشيفرة والاختبارات والإصدارات ودعم البرمجيات في مستودع الإضافة. تبقى الملفات الميكانيكية وتعليمات التجميع هنا.
<!-- /translated-content -->
