<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 con LeRobot

Utilice el [plugin SO-ARM 102](https://github.com/roboninecom/SO-ARM-102-Lerobot), mantenido por separado, con Hugging Face LeRobot. Admite la combinación de motores STS3235, STS3250 y STS3215 del brazo seguidor.

<a id="install"></a>
## Instalación

Utilice Python 3.12 y siga la [guía de instalación de LeRobot](https://huggingface.co/docs/lerobot/en/installation) para los requisitos de su plataforma. En el entorno activado:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Configuración y control

Utilice `so_arm102_follower` para el seguidor y el tipo estándar `so101_leader` para un líder SO-101 o SO-ARM 102.

Siga las instrucciones del plugin para [configurar motores](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [calibrar](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) y [teleoperar](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Omita la configuración de motores si el brazo ya está configurado. Sustituya los puertos de ejemplo por los suyos y conserve los mismos ID de brazo después de calibrar.

La versión fijada del paquete es una versión alfa. El código, las pruebas, las versiones y el soporte de software permanecen en el repositorio del plugin. Los archivos mecánicos y las instrucciones de montaje permanecen aquí.
<!-- /translated-content -->
