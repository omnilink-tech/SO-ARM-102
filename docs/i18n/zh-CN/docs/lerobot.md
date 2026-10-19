<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 与 LeRobot

将独立维护的 [SO-ARM 102 插件](https://github.com/roboninecom/SO-ARM-102-Lerobot)与 Hugging Face LeRobot 配合使用。该插件支持从动臂中混合使用的 STS3235、STS3250 和 STS3215 电机。

<a id="install"></a>
## 安装

使用 Python 3.12，并按照 [LeRobot 安装指南](https://huggingface.co/docs/lerobot/en/installation)准备平台依赖。在已激活的环境中运行：

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## 配置与控制

从动臂使用 `so_arm102_follower`，SO-101 或 SO-ARM 102 主动臂使用标准类型 `so101_leader`。

按照插件说明进行[电机配置](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up)、[校准](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate)和[遥操作](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate)。已配置的机械臂应跳过电机配置。将示例端口替换为实际端口，并在校准后保持相同的机械臂 ID。

指定的软件包版本为 alpha 版本。源代码、测试、版本发布和软件支持保留在插件仓库中。机械文件和装配说明保留在本仓库中。
<!-- /translated-content -->
