<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 avec LeRobot

Utilisez le [plugin SO-ARM 102](https://github.com/roboninecom/SO-ARM-102-Lerobot), maintenu séparément, avec Hugging Face LeRobot. Il prend en charge les moteurs STS3235, STS3250 et STS3215 du bras suiveur.

<a id="install"></a>
## Installation

Utilisez Python 3.12 et suivez le [guide d’installation de LeRobot](https://huggingface.co/docs/lerobot/en/installation) pour les prérequis de votre plateforme. Dans l’environnement activé :

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Configuration et contrôle

Utilisez `so_arm102_follower` pour le suiveur et le type standard `so101_leader` pour un leader SO-101 ou SO-ARM 102.

Suivez les instructions du plugin pour la [configuration des moteurs](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), la [calibration](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) et la [téléopération](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Ignorez la configuration des moteurs si le bras est déjà configuré. Remplacez les ports des exemples par les vôtres et conservez les mêmes ID de bras après la calibration.

La version spécifiée du paquet est une version alpha. Le code, les tests, les versions et le support logiciel restent dans le dépôt du plugin. Les fichiers mécaniques et les instructions de montage restent ici.
<!-- /translated-content -->
