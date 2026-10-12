<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Englisches Original](../../../CONTRIBUTING.md)

[Dokumentation](README.md) · [Drucken](docs/printing.md) · [Stückliste](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Technische Daten](docs/specifications.md) · [Modelle](models/README.md) · [Mitwirken](CONTRIBUTING.md) · [Lizenzen](LICENSING.md) · [Übersetzungen](docs/translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Mitwirken

Vielen Dank, dass Sie SO-ARM 102 verbessern.

<a id="report-a-problem"></a>
## Problem melden

Öffnen Sie ein Problem und fügen Sie Folgendes hinzu:

- Was Sie gebaut oder gedruckt haben, mit der Teilenummer;
- Drucker-, Material- und Slicer-Einstellungen für Druckprobleme;
- Fotos, wenn etwas nicht passt.

Build-Reports sind besonders willkommen, auch wenn alles funktioniert hat.

<a id="change-a-part"></a>
## Ein Teil ändern

1. Bearbeiten Sie die STEP-Datei in `models/step/`.
2. Exportieren Sie eine Binärdatei STL mit demselben Namen in `models/stl/`.
3. Aktualisieren Sie `docs/printing.md` und `docs/assembly-guide.md`, wenn sich Namen, Mengen oder Befestigungselemente ändern.
4. Drucken und passen Sie das Teil an, bevor Sie einen Pull Request öffnen, und geben Sie in dem Pull Request an, was Sie getestet haben.

<a id="licence-of-contributions"></a>
## Lizenz der Beiträge

Ihre Änderung ist unter der Lizenz lizenziert, die bereits für die Datei gilt.

| Du veränderst dich | Dein Beitrag ist lizenziert |
|---|---|
| CAD und Netze in `models/` | CERN-OHL-P-2.0 |
| Konfiguration und CI | Apache-2.0 |
| Dokumentation und Bilder | CC BY 4.0 |

Wenn ein Beitrag Material enthält, das Sie nicht erstellt haben, geben Sie dies in der Pull-Anfrage an, damit es in `NOTICE` aufgezeichnet werden kann. Neue Dateien müssen von `REUSE.toml` abgedeckt sein. CI läuft `reuse lint` und schlägt andernfalls fehl.
<!-- /translated-content -->
