<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Original em inglês](../../../translations.md)

[Documentação](../README.md) · [Impressão](printing.md) · [Materiais](bom.md) · [Montagem](assembly-guide.md) · [Especificações](specifications.md) · [Modelos](../models/README.md) · [Contribuir](../CONTRIBUTING.md) · [Licenças](../LICENSING.md) · [Traduções](translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traduções de documentação

Escolha seu idioma no README principal. Cada pasta de idioma contém o README completo, lista de materiais, instruções de impressão, guia de montagem, especificações, guia de modelo, diretrizes de contribuição, guia de licenciamento, orientação para repositório e avisos de atribuição.Links entre estes documentos permanecem no idioma selecionado.

Os documentos de origem em inglês permanecem em seus caminhos existentes. As traduções estão em `docs/i18n/<language>/` e espelham a estrutura da pasta de origem. CAD, arquivos de simulação, imagens, vídeos e o livreto PDF original são compartilhados. Texto e rótulos incorporados nas ilustrações existentes permanecem como desenhado; o guia de montagem inclui as instruções traduzidas, tabelas de peças, aviso de tensão e legenda da ilustração.

<a id="translation-status"></a>
## Status da tradução

As primeiras traduções foram preparadas com assistência de IA e um modelo de tradução local, depois verificadas quanto à integridade estrutural, links e valores técnicos preservados. Elas não foram revisadas por falantes nativos. Use o código-fonte em inglês para resolver ambigüidades e relatar problemas de tradução através de uma questão do GitHub, incluindo o idioma, documento e frase afetada.

<a id="contribute-a-translation"></a>
## Contribuir com uma tradução

1. Edite a fonte em inglês primeiro ao alterar instruções ou dados técnicos.
2. Atualize o documento correspondente em cada pasta de idioma.Preservar tabelas, todas as etapas, avisos, identificadores de peças, valores numéricos, comandos e URLs externos.
3. Mantenha os links de documentos locais no mesmo idioma. Vincule ativos compartilhados usando caminhos relativos. Preserve os IDs de âncora em inglês explícitos usados pelos links internos da seção.
4. Após revisar as traduções afetadas, registre as versões de origem com `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.Este comando registra somente versões; ele não traduz ou revisa o texto.
5. Execute `python .github/scripts/check_translations.py` e `pre-commit run --all-files`. Envie as alterações em um pull request e informe quais idiomas foram revisados.

Ao adicionar um documento Markdown de origem, adicione seu caminho ao manifesto de tradução e forneça o arquivo correspondente em cada pasta de idioma.A verificação CI detecta documentos de origem não listados, hashes de fonte alterados, traduções ausentes, links locais quebrados, âncoras ausentes, identificadores técnicos alterados, tabelas perdidas e seções ausentes.

<a id="repository-conventions"></a>
## Convenções de repositório

O README raiz fornece links de idiomas porque o GitHub não seleciona automaticamente um README traduzido para cada leitor. Cada documento traduzido tem links para o documento equivalente em todos os outros idiomas e para sua fonte em inglês. As pastas de idioma usam tags BCP 47. Os dez idiomas são uma seleção prática do público internacional, não uma classificação pelo número de falantes.

- [GitHub README e links relativos](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Fluxo de trabalho de tradução do GitHub Docs](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
