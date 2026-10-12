<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Original anglais](../../../CONTRIBUTING.md)

[Documentation](README.md) · [Impression](docs/printing.md) · [Composants](docs/bom.md) · [Montage](docs/assembly-guide.md) · [Caractéristiques](docs/specifications.md) · [Modèles](models/README.md) · [Contribuer](CONTRIBUTING.md) · [Licences](LICENSING.md) · [Traductions](docs/translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing"></a>
# Contribuer

Merci de nous aider à améliorer SO-ARM 102.

<a id="report-a-problem"></a>
## Signaler un problème

Ouvrez un problème et incluez:

- ce que vous avez construit ou imprimé, avec le numéro de pièce;
- Réglages de l'imprimante, du matériel et du trancheur pour les problèmes d'impression;
- Photos, si quelque chose ne correspond pas.

Les rapports de construction sont particulièrement bienvenus, même lorsque tout a fonctionné.

<a id="change-a-part"></a>
## Modifier une pièce

1. Modifiez le fichier STEP dans `models/step/`.
2. Exporter un binaire STL avec le même nom dans `models/stl/`.
3. Mettre à jour `docs/printing.md` et `docs/assembly-guide.md` si les noms, quantités ou attaches changent.
4. Imprimez et ajustez la pièce avant d'ouvrir une requête de pull, et indiquez dans la requête ce que vous avez testé.

<a id="licence-of-contributions"></a>
## Licence des contributions

Votre modification est autorisée sous la licence qui couvre déjà le fichier.

| Vous êtes en train de changer | Votre contribution est sous licence |
|---|---|
| CAD et mailles dans `models/` | CERN-OHL-P-2.0 |
| Configuration et CI | Apache-2.0 |
| Documentation et images | CC BY 4.0 |

Si une contribution contient du matériel que vous n'avez pas créé, indiquez-le dans la demande de pull afin qu'elle puisse être enregistrée dans `NOTICE`. Les nouveaux fichiers doivent être couverts par `REUSE.toml`. CI exécute `reuse lint` et échoue sinon.
<!-- /translated-content -->
