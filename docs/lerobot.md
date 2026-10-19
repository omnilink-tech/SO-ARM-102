# SO-ARM 102 with LeRobot

<!-- documentation-languages -->
[English](i18n/en/docs/lerobot.md) · [Русский](i18n/ru/docs/lerobot.md) · [Español](i18n/es/docs/lerobot.md) · [Français](i18n/fr/docs/lerobot.md) · [Deutsch](i18n/de/docs/lerobot.md) · [Português (Brasil)](i18n/pt-BR/docs/lerobot.md) · [简体中文](i18n/zh-CN/docs/lerobot.md) · [日本語](i18n/ja/docs/lerobot.md) · [हिन्दी](i18n/hi/docs/lerobot.md) · [العربية](i18n/ar/docs/lerobot.md)
<!-- /documentation-languages -->

Use the separately maintained [SO-ARM 102 plugin](https://github.com/roboninecom/SO-ARM-102-Lerobot) with Hugging Face LeRobot. It supports the follower's mixed STS3235, STS3250 and STS3215 motors.

## Install

Use Python 3.12 and follow the [LeRobot installation guide](https://huggingface.co/docs/lerobot/en/installation) for platform prerequisites. In the activated environment:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

## Set up and control

Use `so_arm102_follower` for the follower and the standard `so101_leader` type for an SO-101 or SO-ARM 102 leader.

Follow the plugin instructions for [motor setup](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [calibration](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) and [teleoperation](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Skip motor setup on an already configured arm. Replace the example ports with your own and retain the same arm IDs after calibration.

The pinned package is an alpha release. Its source, tests, releases and software support remain in the plugin repository. Hardware files and assembly instructions remain here.
