<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 com LeRobot

Use o [plugin SO-ARM 102](https://github.com/roboninecom/SO-ARM-102-Lerobot), mantido separadamente, com Hugging Face LeRobot. Ele oferece suporte à combinação de motores STS3235, STS3250 e STS3215 do braço seguidor.

<a id="install"></a>
## Instalação

Use Python 3.12 e siga o [guia de instalação do LeRobot](https://huggingface.co/docs/lerobot/en/installation) para os requisitos da plataforma. No ambiente ativado:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## Configuração e controle

Use `so_arm102_follower` para o seguidor e o tipo padrão `so101_leader` para um líder SO-101 ou SO-ARM 102.

Siga as instruções do plugin para [configurar os motores](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [calibrar](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) e [teleoperar](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate). Pule a configuração dos motores se o braço já estiver configurado. Substitua as portas dos exemplos pelas suas e mantenha os mesmos IDs dos braços após a calibração.

A versão fixada do pacote é uma versão alfa. Código, testes, versões e suporte de software permanecem no repositório do plugin. Os arquivos mecânicos e as instruções de montagem permanecem aqui.
<!-- /translated-content -->
