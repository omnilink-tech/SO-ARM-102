<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Original em inglês](../../../CONTRIBUTING.md)

[Documentação](README.md) · [Impressão](docs/printing.md) · [Materiais](docs/bom.md) · [Montagem](docs/assembly-guide.md) · [Especificações](docs/specifications.md) · [Modelos](models/README.md) · [Contribuir](CONTRIBUTING.md) · [Licenças](LICENSING.md) · [Traduções](docs/translations.md)

> Tradução completa do documento. As ilustrações e o manual PDF original são compartilhados entre os idiomas. Tradução feita com auxílio de IA; ainda não revisada por falantes nativos.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Como contribuir

Obrigado por ajudar a melhorar SO-ARM 102.

<a id="report-a-problem"></a>
## Relatar um problema

Abra um problema e inclua:

- o que você estava construindo ou imprimindo, com o número da peça;
- configurações de impressora, material e slicer para problemas de impressão;
- fotos, se algo não se encaixa.

Relatórios de compilação são especialmente bem-vindos, mesmo quando tudo funcionou.

<a id="change-a-part"></a>
## Alterar uma peça

1. Edite o arquivo STEP em `models/step/`.
2. Exporte um binário STL com o mesmo nome para `models/stl/`.
3. Atualize `docs/printing.md` e `docs/assembly-guide.md` se os nomes, quantidades ou fixadores mudarem.
4. Imprima e ajuste a peça antes de abrir um pull request, e diga no pull request o que você testou.

<a id="licence-of-contributions"></a>
## Licença das contribuições

Sua alteração está licenciada sob a licença que já cobre o arquivo.

| Você está mudando | Sua contribuição está licenciada |
|---|---|
| CAD e malhas em `models/` | CERN-OHL-P-2.0 |
| Configuração e CI | Apache-2.0 |
| Documentação e imagens | CC BY 4.0 |

Se uma contribuição contém material que você não criou, diga isso no pull request para que ele possa ser registrado em `NOTICE`. Novos arquivos devem ser cobertos por `REUSE.toml`. CI executa `reuse lint` e falha caso contrário.
<!-- /translated-content -->
