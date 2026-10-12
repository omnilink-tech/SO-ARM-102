<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Englisches Original](../../../translations.md)

[Dokumentation](../README.md) · [Drucken](printing.md) · [Stückliste](bom.md) · [Montage](assembly-guide.md) · [Technische Daten](specifications.md) · [Modelle](../models/README.md) · [Mitwirken](../CONTRIBUTING.md) · [Lizenzen](../LICENSING.md) · [Übersetzungen](translations.md)

> Vollständige Übersetzung des Dokuments. Abbildungen und die ursprüngliche PDF-Anleitung werden gemeinsam genutzt. Mit KI übersetzt; noch nicht von Muttersprachlern geprüft.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Dokumentationsübersetzungen

Wählen Sie Ihre Sprache im Haupt README aus. Jeder Sprachordner enthält die vollständige README, Stückliste, Druckanleitungen, Montageanleitung, Spezifikationen, Modellanleitung, Beitragsrichtlinien, Lizenzierungsanleitung, Repository-Anleitung und Namensnennungshinweise. Links zwischen diesen Dokumenten bleiben in der ausgewählten Sprache.

Die englischen Quelldokumente bleiben in ihren bestehenden Pfaden. Übersetzungen sind in `docs/i18n/<language>/` und spiegeln die Quellordnerstruktur wider. CAD, Simulationsdateien, Bilder, Videos und das Original-PDF-Broschüren werden geteilt. Texte und Beschriftungen, die in bestehende Abbildungen eingebettet sind, bleiben wie gezeichnet; die Montageanleitung enthält die übersetzten Anweisungen, Teiletabellen, Spannungswarnungen und Bildlegenden. Originalrechtliche Lizenztexte und maschinenlesbare Konfiguration werden geteilt, nicht übersetzt.

<a id="translation-status"></a>
## Übersetzungsstatus

Die ersten Übersetzungen wurden mit KI-Unterstützung und einem lokalen Übersetzungsmodell erstellt, dann auf strukturelle Vollständigkeit, Links und erhaltene technische Werte geprüft. Sie wurden nicht von Muttersprachlern überprüft. Verwenden Sie die englische Quelle, um Zweideutigkeiten zu lösen und Übersetzungsprobleme über ein GitHub-Problem zu melden, einschließlich der Sprache, des Dokuments und des betroffenen Satzes.

<a id="contribute-a-translation"></a>
## Eine Übersetzung beitragen

1. Beim Ändern von Anleitungen oder technischen Daten zuerst die englische Quelle bearbeiten.
2. Aktualisieren Sie das entsprechende Dokument in jedem Sprachordner und behalten Sie Tabellen, alle Schritte, Warnungen, Teilebezeichner, numerische Werte, Befehle und externe URLs bei.
3. Verlinken Sie freigegebene Assets mithilfe relativer Pfade. Behalten Sie die expliziten englischen Anker-IDs bei, die von internen Abschnittsverbindungen verwendet werden, und setzen Sie Links zu lokalen Dokumenten in der gleichen Sprache ein.
4. Nachdem Sie die betroffenen Übersetzungen überprüft haben, zeichnen Sie die Quellversionen mit `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md` auf. Dieser Befehl zeichnet nur Versionen auf. Er übersetzt oder überprüft den Text nicht.
5. Führen Sie `python .github/scripts/check_translations.py` und `pre-commit run --all-files` aus. Übermitteln Sie Änderungen in einem Pull-Request und geben Sie an, welche Sprachen überprüft wurden.

Wenn Sie ein Markdown-Quelldokument hinzufügen, fügen Sie dessen Pfad zum Übersetzungsmanifest hinzu und stellen Sie die entsprechende Datei in jedem Sprachordner zur Verfügung.Die CI-Prüfung erkennt nicht aufgeführte Quelldokumente, geänderte Hashes der Quellen, fehlende Übersetzungen, defekte lokale Links, fehlende Anker, geänderte technische Bezeichner, verlorene Tabellen und fehlende Abschnitte.

<a id="repository-conventions"></a>
## Repository-Konventionen

Das Root README bietet Sprachlinks, da GitHub nicht automatisch eine übersetzte README für jeden Leser auswählt. Jedes übersetzte Dokument verlinkt auf das entsprechende Dokument in jeder anderen Sprache und auf seine englische Quelle. Sprachordner verwenden BCP 47-Tags. Die zehn Sprachen sind eine praktische internationale Zielgruppenauswahl, keine Rangliste nach Sprecherzahl. Englisch bleibt die Quellsprache für die Wartung.

- [GitHub README und relative Links](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Docs Übersetzung Workflow](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
