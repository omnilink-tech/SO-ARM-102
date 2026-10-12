<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Английский оригинал](../../../CONTRIBUTING.md)

[Документация](README.md) · [Печать](docs/printing.md) · [Комплектующие](docs/bom.md) · [Сборка](docs/assembly-guide.md) · [Характеристики](docs/specifications.md) · [Модели](models/README.md) · [Участие](CONTRIBUTING.md) · [Лицензирование](LICENSING.md) · [Переводы](docs/translations.md)

> Полный перевод документа. Изображения и исходный PDF-буклет общие для всех языков. Перевод подготовлен с помощью ИИ; проверка носителями языка ещё не проведена.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Участие в проекте

Спасибо за помощь в развитии SO-ARM 102.

<a id="report-a-problem"></a>
## Сообщить о проблеме

Создайте issue и укажите:

- что вы собирали или печатали, с номером детали;
- принтер, материал и настройки слайсера для проблем печати;
- фотографии, если что-то не подходит.

Отчёты о сборке особенно полезны, даже если всё получилось.

<a id="change-a-part"></a>
## Изменить деталь

1. Отредактируйте файл STEP в `models/step/`.
2. Экспортируйте бинарный STL с тем же именем в `models/stl/`.
3. При изменении имён, количества или крепежа обновите `docs/printing.md` и `docs/assembly-guide.md`.
4. Перед открытием pull request напечатайте деталь и проверьте посадку. Укажите в PR, что вы проверили.

<a id="licence-of-contributions"></a>
## Лицензия вклада

Изменение распространяется по лицензии, которая уже покрывает файл.

| Что вы изменяете | Лицензия вашего вклада |
|---|---|
| CAD и сетки в `models/` | CERN-OHL-P-2.0 |
| Конфигурация и CI | Apache-2.0 |
| Документация и изображения | CC BY 4.0 |

Если вклад содержит чужой материал, укажите это в PR для записи в `NOTICE`. Новые файлы должны быть покрыты `REUSE.toml`. CI запускает `reuse lint` и иначе завершится ошибкой.
<!-- /translated-content -->
