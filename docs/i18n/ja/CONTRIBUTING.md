<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[英語原文](../../../CONTRIBUTING.md)

[ドキュメント](README.md) · [印刷](docs/printing.md) · [部品表](docs/bom.md) · [組立](docs/assembly-guide.md) · [仕様](docs/specifications.md) · [モデル](models/README.md) · [貢献方法](CONTRIBUTING.md) · [ライセンス](LICENSING.md) · [翻訳](docs/translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# 貢献方法

SO-ARM 102 の改善を手伝ってくれてありがとう。

<a id="report-a-problem"></a>
## 問題の報告

問題を開き、以下の内容を含めます。

- 製作したり印刷したものを 部品番号で表示します
- 印刷問題に対するプリンタ、素材、スライサーの設定
- 写真を見て 何か合わないときは

すべてがうまくいった場合でも、ビルドレポートは特に歓迎されます。

<a id="change-a-part"></a>
## 部品の変更

1. STEP ファイルを `models/step/` で編集します。
2. 同じ名前のバイナリ STL を `models/stl/` にエクスポートします。
3. 名前、数量またはファスナーが変更されたら `docs/printing.md` と `docs/assembly-guide.md` を更新します。
4. プールリクエストを開く前に部品を印刷してフィットし、プールリクエストでテストしたことを言います。

<a id="licence-of-contributions"></a>
## 貢献内容のライセンス

あなたの変更は、ファイルに既に適用されているライセンスでライセンスされています。

| 変更する対象 | あなたの貢献はライセンスされています |
|---|---|
| CAD と `models/` のメッシュ | CERN-OHL-P-2.0 |
| コンフィギュレーションとCI | Apache-2.0 |
| ドキュメンテーションと画像 | CC BY 4.0 |

あなたが作成していない素材を含むコンポジットがあれば、 `NOTICE` に記録するために pull リクエストでそれを指定してください。新しいファイルは `REUSE.toml` でカバーされる必要があります。そうでなければ CI は `reuse lint` を実行し失敗します。
<!-- /translated-content -->
