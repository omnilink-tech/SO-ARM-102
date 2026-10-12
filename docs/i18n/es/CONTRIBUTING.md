<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Original en inglés](../../../CONTRIBUTING.md)

[Documentación](README.md) · [Impresión](docs/printing.md) · [Materiales](docs/bom.md) · [Montaje](docs/assembly-guide.md) · [Especificaciones](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licencias](LICENSING.md) · [Traducciones](docs/translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Cómo contribuir

Gracias por ayudar a mejorar SO-ARM 102.

<a id="report-a-problem"></a>
## Informar de un problema

Abra un problema e incluya:

- lo que estabas construyendo o imprimiendo, con el número de pieza;
- Ajustes de impresora, material y slicer para problemas de impresión;
- Fotos, si algo no encaja.

Los informes de compilación son especialmente bienvenidos, incluso cuando todo funcionó.

<a id="change-a-part"></a>
## Modificar una pieza

1. Edite el archivo STEP en `models/step/`.
2. Exporta un binario STL con el mismo nombre a `models/stl/`.
3. Actualice `docs/printing.md` y `docs/assembly-guide.md` si cambian los nombres, cantidades o sujetadores.
4. Imprima y ajuste la pieza antes de abrir una solicitud de pull, y diga en la solicitud de pull lo que ha probado.

<a id="licence-of-contributions"></a>
## Licencia de las contribuciones

Tu cambio está licenciado bajo la licencia que ya cubre el archivo.

| Estás cambiando | Tu contribución está licenciada bajo |
|---|---|
| CAD y mallas en `models/` | CERN-OHL-P-2.0 |
| Configuración y CI | Apache-2.0 |
| Documentación e imágenes | CC BY 4.0 |

Si una contribución contiene material que usted no creó, indíquelo en la solicitud de extracción para que se pueda registrar en `NOTICE`. Los nuevos archivos deben estar cubiertos por `REUSE.toml`. CI ejecuta `reuse lint` y falla de lo contrario.
<!-- /translated-content -->
