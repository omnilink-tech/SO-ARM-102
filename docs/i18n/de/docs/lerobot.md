<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 mit LeRobot

Verwenden Sie das separat gepflegte [SO-ARM 102 Plugin](https://github.com/roboninecom/SO-ARM-102-Lerobot) mit Hugging Face LeRobot. Es unterstützt die Kombination aus STS3235, STS3250 und STS3215 im Follower.

<a id="install"></a>
## Installation

Verwenden Sie Python 3.12 und beachten Sie die Plattformvoraussetzungen in der [LeRobot-Installationsanleitung](https://huggingface.co/docs/lerobot/en/installation). In der aktivierten Umgebung:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Einrichtung und Steuerung

Verwenden Sie `so_arm102_follower` für den Follower und den Standardtyp `so101_leader` für einen SO-101 oder SO-ARM 102 Leader.

Folgen Sie den Plugin-Anleitungen zur [Motoreinrichtung](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [Kalibrierung](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) und [Teleoperation](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Überspringen Sie die Motoreinrichtung bei bereits eingerichteten Armen. Ersetzen Sie die Beispielports durch Ihre eigenen und behalten Sie nach der Kalibrierung dieselben Arm-IDs bei.

Die angegebene Paketversion ist eine Alpha-Version. Quellcode, Tests, Releases und Software-Support bleiben im Plugin-Repository. Mechanikdateien und Montageanleitungen bleiben hier.
<!-- /translated-content -->
