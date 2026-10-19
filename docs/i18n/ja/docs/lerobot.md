<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# SO-ARM 102 と LeRobot

別途保守される [SO-ARM 102 プラグイン](https://github.com/roboninecom/SO-ARM-102-Lerobot)を Hugging Face LeRobot と組み合わせて使用します。フォロワーの STS3235、STS3250、STS3215 の混在構成に対応します。

<a id="install"></a>
## インストール

Python 3.12 を使用し、[LeRobot インストールガイド](https://huggingface.co/docs/lerobot/en/installation)に従ってプラットフォームの前提条件を整えてください。有効化した環境で実行します：

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## 設定と制御

フォロワーには `so_arm102_follower`、SO-101 または SO-ARM 102 リーダーには標準の `so101_leader` 型を使用します。

プラグインの[モーター設定](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up)、[キャリブレーション](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate)、[テレオペレーション](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate)の手順に従ってください。設定済みのアームではモーター設定を省略します。例のポートを実際のポートに置き換え、キャリブレーション後も同じアーム ID を使用してください。

指定されたパッケージはアルファ版です。ソース、テスト、リリース、ソフトウェアのサポートはプラグインのリポジトリで管理します。機械部品ファイルと組み立て手順はこのリポジトリで管理します。
<!-- /translated-content -->
