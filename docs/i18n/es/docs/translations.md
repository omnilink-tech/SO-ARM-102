<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Original en inglés](../../../translations.md)

[Documentación](../README.md) · [Impresión](printing.md) · [Materiales](bom.md) · [Montaje](assembly-guide.md) · [Especificaciones](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licencias](../LICENSING.md) · [Traducciones](translations.md)

> Traducción completa del documento. Las ilustraciones y el manual PDF original se comparten entre idiomas. Traducción realizada con ayuda de IA; aún no revisada por hablantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traducciones de documentación

Elija su idioma en el README principal. Cada carpeta de idioma contiene el README completo, lista de materiales, instrucciones de impresión, guía de montaje, especificaciones, guía del modelo, pautas de contribución, guía de licenciamiento, guía del repositorio y avisos de atribución. Los enlaces entre estos documentos permanecen en el idioma seleccionado.

Los documentos de origen en inglés permanecen en sus rutas existentes. Las traducciones están en `docs/i18n/<language>/` y reflejan la estructura de carpetas de origen. CAD, los archivos de simulación, imágenes, videos y el folleto PDF original se comparten. El texto y las etiquetas incrustadas en ilustraciones existentes permanecen como se dibujan; la guía de montaje incluye las instrucciones traducidas, tablas de piezas, advertencia de voltaje y leyenda de ilustración.

<a id="translation-status"></a>
## Estado de la traducción

Las primeras traducciones se prepararon con ayuda de IA y un modelo de traducción local, luego se verificaron para la integridad estructural, los enlaces y los valores técnicos preservados. No han sido revisados por hablantes nativos. Utilice el origen en inglés para resolver ambigüedades e informar problemas de traducción a través de un problema de GitHub, incluyendo el idioma, el documento y la oración afectada.

<a id="contribute-a-translation"></a>
## Contribuir con una traducción

1. Edite primero la fuente en inglés cuando cambie instrucciones o datos técnicos.
2. Actualice el documento correspondiente en cada carpeta de idioma y conserve las tablas, todos los pasos, advertencias, identificadores de piezas, valores numéricos, comandos y URL externas.
3. Mantenga los enlaces de documentos locales en el mismo idioma. Enlace a activos compartidos mediante rutas relativas. Preserve los identificadores de anclaje explícitos en inglés utilizados por los enlaces internos de sección.
4. Después de revisar las traducciones afectadas, registre las versiones de origen con `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md` Este comando solo registra versiones; no traduce ni revisa texto.
5. Ejecute `python .github/scripts/check_translations.py` y `pre-commit run --all-files`.Envíe los cambios en una solicitud de extracción e indique qué idiomas se revisaron.

Al agregar un documento Markdown fuente, agregue su ruta al manifiesto de traducción y proporcione el archivo correspondiente en cada carpeta de idioma.La comprobación CI detecta documentos fuente no listados, hashes de fuente cambiados, traducciones faltantes, enlaces locales rotos, anclajes faltantes, identificadores técnicos cambiados, tablas perdidas y secciones faltantes.

<a id="repository-conventions"></a>
## Convenciones de repositorio

El README raíz proporciona enlaces de idioma porque GitHub no selecciona automáticamente un README traducido para cada lector. Cada documento traducido enlaza al documento equivalente en todos los otros idiomas y a su fuente en inglés. Las carpetas de idioma usan etiquetas BCP 47. Los diez idiomas son una selección práctica de audiencia internacional, no un ranking por número de hablantes.

- [GitHub README y enlaces relativos](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Flujo de trabajo de traducción de GitHub Docs](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
