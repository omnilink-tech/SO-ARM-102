<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 with LeRobot

Use the separately maintained [SO-ARM 102 plugin](https://github.com/roboninecom/SO-ARM-102-Lerobot) with Hugging Face LeRobot. It supports the follower's mixed STS3235, STS3250 and STS3215 motors.

<a id="install"></a>
## Install

Use Python 3.12 and follow the [LeRobot installation guide](https://huggingface.co/docs/lerobot/en/installation) for platform prerequisites. In the activated environment:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Set up and control

Use `so_arm102_follower` for the follower and the standard `so101_leader` type for an SO-101 or SO-ARM 102 leader.

Follow the plugin instructions for [motor setup](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [calibration](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) and [teleoperation](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Skip motor setup on an already configured arm. Replace the example ports with your own and retain the same arm IDs after calibration.

The pinned package is an alpha release. Its source, tests, releases and software support remain in the plugin repository. Hardware files and assembly instructions remain here.
<!-- /translated-content -->
