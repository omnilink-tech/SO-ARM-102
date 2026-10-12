<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[英語原文](../../../README.md)

[ドキュメント](README.md) · [印刷](docs/printing.md) · [部品表](docs/bom.md) · [組立](docs/assembly-guide.md) · [仕様](docs/specifications.md) · [モデル](models/README.md) · [貢献方法](CONTRIBUTING.md) · [ライセンス](LICENSING.md) · [翻訳](docs/translations.md)

> この文書の全文翻訳です。図と元のPDF冊子は各言語で共用します。AIを使用した翻訳であり、母語話者による確認は未実施です。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102"></a>
# SO-ARM 102

<div align="center">

[![SO-ARM 102](../../../assets/images/photos/so-arm-102-live.jpg)](../../../assets/video/so-arm-102-preview.mp4)

**🎥 [プレビュービデオを見る](../../../assets/video/so-arm-102-preview.mp4)**·**🛒[キットを買う](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

**オープンソースのリーダーロボットアーム＋フォローアームロボットアームキット 5 テレオペレーションと模倣学習のための グリップに加えて [Robonine](https://robonine.com) より硬く速い後継機として SO-ARM 101.**

[![ハードウェア: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt) [![ソフトウェア: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt) [![ドキュメント: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt) [![状態: v0.1予備リリース](https://img.shields.io/badge/Status-v0.1%20pre--release-orange.svg)](#-known-issues)

📩 [hello@robonine.com](mailto:hello@robonine.com)

**DIY予算: ~$404 コンポーネントのために ~$444 印刷材料も含めて** [BOMサマリー](#bill-of-materials) · [各種費用・購入リンク](docs/bom.md#estimated-kit-cost)

> 部品をソースして自分で印刷するのではなく、 **[SO-ARM 102キットを買う](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**。

</div>

---

<a id="-what-changed-against-so-arm-101"></a>
## SO-ARM 101に対して何が変わったか

|  | SO-ARM 101 | SO-ARM 102 |
|---|---|---|
| グリッパー | 角度式ジョー | パラレルグリップ, 85 mm スパン |
| フレーム材料 | PLA | PET-CF (Fiberon PET-CF17 テスト済み) |
| 構造 | 中実リンク | トポロジー最適化リンク |
| ベース回転範囲 | 220° | **352°** |
| 水平リーチ | 441 mm | **483 mm** |
| グリップの偏向，300 g荷重¹ | 7.5 mm | **3.4–3.9 mm** |
| 肩・肘速度 | 45 RPM (STS3215) | **75 RPM (STS3250)** |
| 1 m のノイズ | 70 dB | **60 dB** |

¹ 両アームには印刷したサーボのダミーを使用しているため、比較対象はモーターではなくフレームです。詳しい結果と試験条件は [docs/specifications.md](docs/specifications.md) を参照してください。

アームは SO-ARM 101 の関節構成を引き継いでいるため、[Hugging Face LeRobot](https://github.com/huggingface/lerobot) のデータセットとポリシーに対応します。

---

<a id="-preview"></a>
## プレビュー

<div align="center">

[![SO-ARM 102 プレビュー](../../../assets/video/so-arm-102-preview.gif)](../../../assets/video/so-arm-102-preview.mp4)

*ビデオをクリックして 21 s*

</div>

---

<a id="-configurations"></a>
## 設定

<a id="single-arm-one-leader--one-follower"></a>
### 単一ロボットアーム：リーダーアーム１本＋フォローアーム１本

標準キットです。リーダーロボットアームを手で動かし、フォローアームがその動きを繰り返します。遠隔操作や模倣学習のための実演録音に使用してください。

![リーダー1台とフォロワー1台](../../../assets/images/renders/config-single-arm.jpg)

<a id="bimanual-two-leaders--two-followers"></a>
### 二手（にしゅ）：先頭2名、従者2名

2セットを並べて配置します。それぞれの手でリーダーアームを操作することで、フォロワーは物を受け渡したり、部品を保持して作業したり、両手を必要とする作業を行えます。

![リーダー2台とフォロワー2台](../../../assets/images/renders/config-dual-arm.jpg)

<a id="the-two-arms"></a>
### 二つのロボットアーム

| フォロワー | リーダー |
|:-:|:-:|
| ![フォロワーアーム](../../../assets/images/renders/follower.jpg) | ![リーダーアーム](../../../assets/images/renders/leader.jpg) |
| パラレル・グリップ　手首カメラ 12 V | 5 V のトリガーを持つハンドル |

---

<a id="-build-it-in-four-steps"></a>
## 4つのステップで作る

準備済みのキットが好きですか？ **[SO-ARM 102キットを購入](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**。

<a id="1-print-the-parts"></a>
### 1. 部分を印刷

個々の部品は 180 × 180 mm 3D プリンタビルドプレートに入ります。最大の部分は 160 mm 長さです。提供された 3MF プレートレイアウトは 256 × 256 mm 3D プリンタビルドプレートを使用します。

- 3MF スライサープロジェクトの保存された方向と支援設定: [`models/3mf/`](../../../models/3mf) - [リーダーロボットアーム](../../../models/3mf/SO102_leader.3mf), [フォローアーム](../../../models/3mf/SO102_follower.3mf), [フォローアームグリップとボードケース](../../../models/3mf/SO102_follower_gripper_box.3mf)
- プロジェクトの内容とプリンタプロファイル: [models/README.md](models/README.md)
- STL ファイル、スライス準備: [`models/stl/`](../../../models/stl)
- STEP ソース: [`models/step/`](../../../models/step)
- 材料、設定、部品数量: [docs/printing.md](docs/printing.md)

以前の試験用アーム設定では、グリッパーを除くアーム部品のスライサー推定値はフィラメント約 500 g、印刷時間約 21 h でした。現在の推定値は 3MF プロジェクトを再スライスして確認してください。

<a id="2-buy-the-hardware"></a>
### 2。ハードウェアを購入

コンポーネントを [BOM 概要](#bill-of-materials) と [購入リンク付きの完全な BOM](docs/bom.md) からソースします。コンポーネントに対する予算 **$404.09**、または印刷材料を含む **$443.68**、輸送と税金前です。

| アーム | サーボ | コントローラー | 電源 |
|---|---|---|---|
| フォロワー | 2 × STS3235, 2 × STS3250, 2 × STS3215 | Waveshare Bus Servo Driver HAT | **12 V** |
| リーダー | 6 × STS3215 | Waveshare Bus Servo Adapter | **5 V** |

> ⚠️ **リーダーアームは 5 V、フォロワーアームは 12 V で動作します。** 電源を取り違えないでください。

<a id="3-assemble"></a>
### 3. アセンブリ

- 印刷可能なブックレット、36ページA5：[docs/SO-ARM102_assembly_A5_v0.6.pdf](../../SO-ARM102_assembly_A5_v0.6.pdf)
- 部品とファスナーのステップリスト: [docs/assembly-guide.md](docs/assembly-guide.md)

ツール：六角キー 1.5 mm (M2 スクリュー) と 2 mm (M3 スクリュー)。

<a id="4-set-up-the-software"></a>
### 4。ソフトウェアを設定します

サーボID、校正とレッスン: **[lab.robonine.com](https://lab.robonine.com)**ロボットアームは LeRobot SO-101 リーダーロボットアームとフォローアームのワークフローです

---

<a id="bill-of-materials"></a>
## 部品表

１）リードロボットアーム１本＋フォローロボットアーム１本の数量と参考費用：

| カテゴリ/購入リンク | キット内容 | 合計 (USD) |
|---|---|---:|
| [サーボ](docs/bom.md#servos) | 6 × STS3215 7.4 V, 2 × STS3215 12 V, 2 × STS3235, 2 × STS3250 | $283.62 |
| [電子部品](docs/bom.md#electronics) | 2 コントローラ、2 電源、2 USBケーブル、1 手首カメラ | $71.50 |
| [機械部品](docs/bom.md#mechanical-parts) | 軸受4、鋼製ガイドロッド2、テーブルクランプ4 | $37.76 |
| [締結部品](docs/bom.md#fasteners) | ねじとナット;特定サーボモーターキットねじを含む | $11.21 |
| **部品小計** |  | **$404.09** |
| [印刷素材](docs/bom.md#printing-materials) | 0.6 kg PET-CF17 + 0.6 kg PETG 割当 | $39.59 |
| **印刷材料込み合計** |  | **$443.68** |

例のフルパッケージとフィラメントスプールを買う場合、未使用のスペアパーツを含めたコストは **$504**です。これらは参考値であり、新しい供給者からの提案ではありません。輸送、税金、工具、コンピュータ、プリンタ、電気、組立労働は除外されます。注文する前に供給者価格、バリエーション、最小注文数量を確認してください。 3MFプロジェクトを 3D 印刷スライサーで再スライスし、フィラメント消費量をチェックしてください。

[部品表の詳細、購入リンク、費用の前提条件](docs/bom.md#estimated-kit-cost)。

---

<a id="urdf-export"></a>
## URDF エクスポート

現在の独立したエクスポートは [`simulation/urdf/`](../../../simulation/urdf): [URDF](../../../simulation/urdf/so_arm_102.urdf) · [Xacro](../../../simulation/urdf/so_arm_102.xacro) にあります。 `meshes/` を説明ファイルの隣に保存してください。メッシュパスはこのフォルダに対するものです。

- **ビジュアル：** STL 衝突は8つのリンクに 独立して回転するボックスが
- **質量推定:**PLA, 30% フィル、 6 周辺警備 6 上下の層が 0.2 mm レイヤーの高さと**0.40 mm 押出し幅**これらはシミュレーションの仮定であり、使用する [印刷ガイド](docs/printing.md) 製造設定に使うのです
- **ハードウェアの質量：**モーター6個は各 70 g、ベースのベアリングは 105 g です。モデルの推定総質量は**0.889 kg** です。
- **グリップ：** `clamp2` は乗数 `-1` を持つ `clamp1` を模倣します。

[エクスポート設定](../../../simulation/urdf/export_settings.json) と [質量プロパティ](../../../simulation/urdf/mass_properties.json) は仮定を記録します。形状と慣性チェックは [export_verification.json](../../../simulation/urdf/export_verification.json).

---

<a id="-repository-structure"></a>
## リポジトリ構造

```
├── models/
│   ├── 3mf/                 # スライサープロジェクト：リーダロボットアーム，フォローラロボットアーム，グリップ，ボードケース
│   ├── stl/                 # 印刷可能なメッシュ
│   │   ├── common/          # 両方のロボットアームに使われる部品
│   │   ├── follower/        # パラレルグリップ カメラマウント ボードケース
│   │   └── leader/          # ハンドル トリガー 手首巻き ボードケース
│   └── step/                # CAD ソース、stl/と同じレイアウト
├── docs/
│   ├── printing.md          # 素材、スライサーの設定、量
│   ├── bom.md               # 部品表
│   ├── assembly-guide.md    # 部品・ファスナーのステップリスト
│   ├── specifications.md    # 形状，サーボモータ，測定結果と比較した。 SO-ARM 101
│   └── SO-ARM102_assembly_A5_v0.6.pdf
├── assets/
│   ├── images/              # 写真、レンダリング、ブックレットページ、テスト写真
│   └── video/               # 動画とGIFのプレビュー
├── LICENSING.md             # ファイルに適用されるライセンス
└── NOTICE                   # 第三者の著作権
```

---

<a id="-known-issues"></a>
## 既知の問題

これは最初の公開リリースです。独立したテストビルドで以下の問題が発見されました。修正中で、次のリリースで解決します。

1. **リリース一式にはモデルが2つ不足しているとの報告があります。** うち1つは判明しており、カメラホルダーの STEP ソースがまだありません。
2. **M2スクリューはいくつかの場所で手に入りにくいです。** 数個戦うことを期待してください。
3. **グリッパーのクランプはカーボンロッド上で動きが固くなります。** クランプの穴は 6.1 mm に合わせてあります。ロッドの直径は供給元により異なるため、組立前に適合を確認してください。
4. サーボモータケーブルの長さを確認するために，各接続部を閉じる前に，特にベースから肩までをチェックした。
5. ブックレットの組み立て順序が２箇所不明瞭です 固定する前に２段階読んでください。
6. **リーダーの関節に緩さを感じる場合があります。** 各サーボとホーンの間に 8 × 2 mm のゴム製 O リングを入れると、滑らかで静かな摩擦が得られます。関節 1–4 はサーボごとに2個、関節 5–6 は1個使用します。

他に何か見つけましたか？ [問題を開く](https://github.com/roboninecom/SO-ARM-102/issues) をお願いします。

---

<a id="-related-projects"></a>
## 関連プロジェクト

- [SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper), SO-ARM 102 グリップが成長したグリップ
- [SO-ARM101](https://github.com/TheRobotStudio/SO-ARM100) — TheRobotStudio による、この設計の先行モデル
- [スマートシリアルサーボモータの実用的な比較](https://robonine.com/smart-serial-servo-motor-comparison-robotics/)サーボモーターの選択に関わるテストは
- [ロボットアーム用フィラメントの選定](https://robonine.com/choosing-filament-for-robotic-arm-applications/)テストの背後には PET-CF

---

<a id="-license"></a>
## ライセンス

著作権 (c) 2026 Robonine。異なる種類の素材は異なるライセンスを持っています:

| 材料 | ライセンス |
|---|---|
| `models/` のハードウェア設計 | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| ソフトウェアと設定 | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| `docs/`、`assets/`、すべての `README.md` におけるドキュメントと画像 | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

ファイルごとのマップは [LICENSING.md](LICENSING.md)と [REUSE.toml](../../../REUSE.toml)を参照してください。

---

<a id="-team"></a>
## チーム

| 名称 | 役割 | 連絡先 |
|------|------|---------|
| **Alan Subin** | 設計エンジニア：機械設計、CAD、組立ブックレット | [LinkedIn](https://www.linkedin.com/in/alan-subin/) |
| **Boris Kotov** | ソフトウェアとテストエンジニア：プロトタイプ、印刷、テストリグ | [Telegram](https://t.me/bkotov) |
| **Nikita Bragin** | プロジェクト管理者 | [LinkedIn](https://www.linkedin.com/in/nikita-bragin-82296b29/) |
| **Mikhail Chistiakov** | インダストリアルデザイナー：ロボットアームの外観と形状 | [Telegram](https://t.me/brrryska) |
| **Mikhail Zhmaylo** | 構造技術者：剛性モデル，変形削減のための設計変更 | [Telegram](https://t.me/mikhail_zhmaylo) |
| **Vladislav Eremenko** | 構造エンジニア：強度と熱解析，トポロジー最適化 | [Telegram](https://t.me/v1ad_eremenko) |
| **Vladimir Osipov** | テスターとコンサルタント:独立したテストビルド | [LinkedIn](https://www.linkedin.com/in/vladimirosipov/) |

<div align="center">

**ロボットコミュニティ向けに [Robonine](https://robonine.com)** によって作成

</div>
<!-- /translated-content -->
