<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Original anglais](../../../translations.md)

[Documentation](../README.md) · [Impression](printing.md) · [Composants](bom.md) · [Montage](assembly-guide.md) · [Caractéristiques](specifications.md) · [Modèles](../models/README.md) · [Contribuer](../CONTRIBUTING.md) · [Licences](../LICENSING.md) · [Traductions](translations.md)

> Traduction intégrale du document. Les illustrations et le livret PDF original sont communs aux langues. Traduction assistée par IA, pas encore relue par des locuteurs natifs.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traductions de documentation

Choisissez votre langue dans le README principal. Chaque dossier de langue contient le README complet, la liste des matériaux, les instructions d'impression, le guide d'assemblage, les spécifications, le guide du modèle, les directives de contribution, le guide de licence, l'aide au dépôt et les notes d'attribution.

Les traductions sont dans `docs/i18n/<language>/` et reflètent la structure du dossier source. CAD, les fichiers de simulation, les images, les vidéos et le livret PDF original sont partagés. Le texte et les étiquettes incorporés dans les illustrations existantes restent tels que dessinés; le guide d'assemblage comprend les instructions traduites, les tableaux des pièces, l'avertissement de tension et la légende de l'illustration.

<a id="translation-status"></a>
## État de la traduction

Les premières traductions ont été préparées avec l'aide de l'IA et d'un modèle de traduction local, puis vérifiées pour l'exhaustivité structurelle, les liens et les valeurs techniques préservées. Elles n'ont pas été révisées par des locuteurs natifs. Utilisez la source anglaise pour résoudre les ambiguïtés et signaler les problèmes de traduction via un problème GitHub, y compris la langue, le document et la phrase affectée.

<a id="contribute-a-translation"></a>
## Contribuer une traduction

1. Modifiez d'abord la source anglaise lorsque vous modifiez des instructions ou des données techniques.
2. Préserver les tableaux, toutes les étapes, les avertissements, les identifiants de pièces, les valeurs numériques, les commandes et les URL externes.
3. Gardez les liens de documents locaux dans la même langue. Liez des ressources partagées à l’aide de chemins relatifs. Préservez les identifiants d’ancrage explicites en anglais utilisés par les liens internes de section.
4. Après avoir vérifié les traductions affectées, enregistrez les versions sources avec `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.Cette commande enregistre uniquement les versions ; elle ne traduit ni ne vérifie le texte.
5. Exécutez `python .github/scripts/check_translations.py` et `pre-commit run --all-files`. Soumettez les modifications dans une pull request et indiquez quelles langues ont été révisées.

Lorsque vous ajoutez un document Markdown source, ajoutez son chemin d'accès au manifeste de traduction et fournissez le fichier correspondant dans chaque dossier langue.Le contrôle CI détecte les documents sources non répertoriés, les hachages sources modifiés, les traductions manquantes, les liens locaux brisés, les ancres manquantes, les identifiants techniques modifiés, les tables perdues et les sections manquantes.

<a id="repository-conventions"></a>
## Conventions relatives au dépôt

Le README racine fournit des liens vers les langues car GitHub ne sélectionne pas automatiquement un README traduit pour chaque lecteur. Chaque document traduit est relié au document équivalent dans toutes les autres langues et à sa source en anglais. Les dossiers de langue utilisent les balises BCP 47. Les dix langues sont une sélection pratique d'audience internationale, pas un classement par nombre de locuteurs. L'anglais reste la langue source pour la maintenance.

- [GitHub README et liens relatifs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Docs workflow de traduction](https://github.com/github/docs/blob/main/src/languages/README.md)
<!-- /translated-content -->
