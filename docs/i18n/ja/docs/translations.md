<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[英語原文](../../../translations.md)

[ドキュメント](../README.md) · [印刷](printing.md) · [部品表](bom.md) · [組立](assembly-guide.md) · [仕様](specifications.md) · [モデル](../models/README.md) · [貢献方法](../CONTRIBUTING.md) · [ライセンス](../LICENSING.md) · [翻訳](translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# ドキュメントの翻訳

メインの README において言語を選択します。各言語フォルダには、完全な README、材料表、印刷指示、アセンブリガイド、仕様書、モデルガイド、貢献ガイドライン、ライセンスガイド、リポジトリガイド、クレジットノートが含まれています。これらの文書間のリンクは選択した言語で残ります。

英語のソース文書は既存のパスに残ります。翻訳は `docs/i18n/<language>/` にあり、ソースフォルダ構造を反映しています。CAD、シミュレーションファイル、画像、ビデオ、オリジナルの PDF ブックレットは共有されます。既存の図面に埋め込まれたテキストとラベルは描かれたままです。アセンブリガイドには翻訳された説明書、部品表、電圧警告および図形の説明が含まれています。オリジナルの法的ライセンステキストと機械読み取れる設定は共有されますが、翻訳されていません。

<a id="translation-status"></a>
## 翻訳の状態

最初の翻訳は AI とローカル翻訳モデルを使って作成され、構造的完全性、リンク、保存された技術値をチェックしました。これらは母語話者によるレビューは行われていません。曖昧さを解消するには英語ソースを使用し、GitHub イベントで翻訳問題を報告してください。言語、文書、影響を受けた文などを含みます。CI チェックに合格することは言語やハードウェアの正確性を証明しません。

<a id="contribute-a-translation"></a>
## 翻訳を提供

1. 指示や技術データを変更するときは、まず英語ソースを編集します。
2. 各言語フォルダのマッチする文書を更新します。表、すべてのステップ、警告、部品識別子、数値、コマンド、外部 URL を保存します。
3. ローカル文書のリンクを同じ言語で保持します。共有アセットへのリンクは相対パスを使います。内部セクションリンクに使用される明示的な英語アンカー ID を保持します。
4. 影響を受けた翻訳を検証した後、ソースのバージョンを `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md` で記録します。このコマンドはバージョンのみを記録します。テキストを翻訳も検証もしません。
5. `python .github/scripts/check_translations.py` と `pre-commit run --all-files` を実行します。プール要求で変更を提出し、どの言語が修正されたかを示します。

ソース Markdown 文書を追加するときは、翻訳マニフェストにそのパスを追加し、各言語フォルダに対応するファイルを提供してください。CIチェックはリストされていないソース文書、変更されたソースハッシュ、欠落した翻訳、破損したローカルリンク、アンカーの欠落、変更された技術識別子、失われた表、欠落したセクションを検出します。

<a id="repository-conventions"></a>
## リポジトリ規約

ルート README は GitHub が自動的に読者ごとに翻訳された README を選択しないため、言語リンクを提供します。翻訳された文書は他のすべての言語で同等な文書と英語ソースへリンクします。言語フォルダは BCP 47 タグを使用します。10 言語は実用的な国際ユーザーの選択であり、話者数による順位ではありません。英語はメンテナンスのためのソース言語として残ります。

- [GitHub README と関連リンク](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Docs 翻訳ワークフロー](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
