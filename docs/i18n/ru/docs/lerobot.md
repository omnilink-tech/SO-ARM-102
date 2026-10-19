<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 с LeRobot

Используйте отдельно поддерживаемый [плагин SO-ARM 102](https://github.com/roboninecom/SO-ARM-102-Lerobot) с Hugging Face LeRobot. Он поддерживает сочетание моторов STS3235, STS3250 и STS3215 ведомой руки.

<a id="install"></a>
## Установка

Используйте Python 3.12 и выполните требования платформы из [инструкции установки LeRobot](https://huggingface.co/docs/lerobot/en/installation). В активированном окружении:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Настройка и управление

Для ведомой руки используйте `so_arm102_follower`, для ведущей SO-101 или SO-ARM 102 — стандартный тип `so101_leader`.

Следуйте инструкциям плагина по [настройке моторов](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [калибровке](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) и [телеуправлению](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Пропустите настройку моторов, если рука уже настроена. Замените порты из примеров своими и сохраняйте те же ID рук после калибровки.

Указанная версия пакета — альфа-релиз. Исходники, тесты, релизы и поддержка ПО остаются в репозитории плагина. Файлы механики и инструкции сборки остаются здесь.
<!-- /translated-content -->
