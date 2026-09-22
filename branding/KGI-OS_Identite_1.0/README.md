# KGI-OS 1.0 — visuels originaux intégrés

Les images fournies sont désormais les ressources utilisées dans chaque dossier.
Les anciens logos redessinés et les anciens fonds ne sont pas inclus dans ce pack corrigé.
Les sources originales sont conservées, octet pour octet, dans `00-visuels-originaux`.

## Fichiers à sélectionner

| Usage | Fichier principal | Source |
|---|---|---|
| Bienvenue de l’installateur | `01-installateur/kgi-bienvenue-752x448.png` | Logo KGI 03.png + textes des profils à gauche |
| Démarrage et arrêt | `02-plymouth/kgi-demarrage.png` | logo kgi ecran de veille.png |
| Connexion | `03-connexion/kgi-connexion.png` | logo KGI.png |
| Menu | `04-icones/png/kgi-os-64.png` | kapa-greenit-icone-dark.png |
| Installation USB | `04-icones/png/kgi-install-usb-64.png` | Même icône originale, libellé distinct à configurer |
| À propos | `04-icones/png/kgi-a-propos-128.png` | Même icône originale |
| Fond de bureau fixe | `06-fond-ecran/kgi-bureau.png` | Logo KGI 03.png |
| Écran de veille fixe | `07-ecran-veille/kgi-veille.png` | logo kgi ecran de veille.png |
| Fond de bureau animé | `08-fond-anime/kgi-bureau-anime-1920x1080.mp4` | Logo KGI 03.png + effet lumineux animé à gauche |
| Fond animé 720p | `08-fond-anime/kgi-bureau-anime-1280x720.mp4` | Même animation |

Les fichiers principaux sans dimensions sont des copies des versions 1920 × 1080.
`INTEGRATION.json` répertorie les choix par défaut et les exports. Ce manifeste sert
à l’intégrateur ; il n’est pas automatiquement lu par Linux.

## Dimensions et proportions

- Fonds : 1366 × 768, 1920 × 1080, 1920 × 1200 et 1600 × 1200.
- Installateur : 752 × 448 et 960 × 600 ; vérifier la zone réelle disponible.
- Icônes : 16, 24, 32, 48, 64, 128, 256 et 512 pixels.
- Plymouth : fonds complets et visuels réduits de 256, 512 et 1024 pixels de large.

Les fonds sources mesurent 1672 × 941 pixels. Les grands exports sont donc des
agrandissements, sans création de détails supplémentaires. Le redimensionnement
est proportionnel avec marges sombres si nécessaire : aucun recadrage ni étirement.
Choisir un affichage de type « ajuster/contenir » ; éviter « étirer » et le zoom
qui coupe l’image. Les moniteurs ultralarges peuvent utiliser le fond 16:9 avec
des marges latérales.

## Points d’intégration

**Installateur :** le fond original est conservé. Les explications des trois profils
sont ajoutées dans son espace libre à gauche. Les textes sont éditables dans les SVG
et disponibles dans `profils-fr.json` pour une interface accessible. Le choix du
profil reste un écran interactif distinct.

**Plymouth :** ces sources sont opaques. Le pack fournit un fond complet, pas un
logo détouré transparent et pas un thème Plymouth exécutable. Le thème devra
ajuster le fond proportionnellement à l’écran et afficher les messages, la
progression et toute demande de déchiffrement par-dessus sur un panneau lisible.
Ne pas charger ce fond comme un petit logo isolé. Les noms trompeurs
`kgi-logo-transparent` de l’ancien pack sont retirés ; mettre à jour les références.

**Connexion :** utiliser une zone de saisie à gauche, environ x = 6–46 % et
y = 20–75 %, sur un panneau opaque sombre. Le logo et la signature sont à droite.
Si le gestionnaire de connexion impose un formulaire centré, sa disposition devra
être adaptée ou ce fond devra être réévalué. L’ancien conseil « centre dégagé »
ne s’applique plus à ces images originales.

**Icônes :** le logo carré fourni est conservé entier, y compris son texte. À 16 et
24 pixels, son texte est naturellement trop petit pour être lu : toujours afficher
un libellé accessible. Aucun symbole de remplacement n’a été dessiné.

**Veille :** le PNG est une ressource pour l’écran de veille. Il ne configure ni
le déclenchement après inactivité, ni le verrouillage, ni la sortie de veille.

**Animation :** vidéo MP4 H.264, 12 secondes, 24 images/s, sans audio. Le motif
lumineux boucle ; le logo et les textes restent fixes. Ouvrir `08-fond-anime/preview.html`
après extraction pour voir la vidéo avec les commandes de lecture. Une vidéo ne
s’active pas comme un PNG dans tous les bureaux Linux : un moteur compatible et
sa configuration restent nécessaires. Aucune dépendance ni session système n’a
été modifiée. Pour les PC peu puissants, conserver le fond fixe par défaut.

## Préparer les chemins de déploiement

Exécuter depuis le dossier extrait :

```sh
sh preparer-ressources.sh ./rootfs-kgi
```

Ce script copie uniquement les fichiers dans un dossier de préparation, avec des
chemins stables sous `usr/share`. Il refuse la racine `/`. Il n’active aucun thème
et n’écrit aucune configuration de connexion, de démarrage ou de bureau.
Intégrer ensuite ces fichiers au processus de construction de l’ISO et y relier
les configurations. La vidéo est facultative : ne pas l’embarquer si inutile.

## Vérifications et reproduction

`VERIFICATION.json` consigne les dimensions, la vérification des sources et les
paramètres des vidéos. `SHA256SUMS.txt` permet de contrôler les fichiers.
Les PNG ont été ouverts et les aperçus contrôlés. Les essais dans l’ISO restent
nécessaires : Live, installation, démarrage/arrêt, connexion et veille, sur VM BIOS
et UEFI puis sur un Lenovo ThinkCentre de référence.

Les SVG sont des conteneurs autonomes avec PNG intégré, **pas des logos vectorisés**.
Seuls les textes ajoutés à l’accueil sont des éléments vectoriels éditables.

`build_pack.py` régénère les exports depuis les originaux (Python 3, Pillow,
Inkscape et DejaVu Sans). `animate.py` régénère les vidéos (Python 3, Pillow, NumPy
et FFmpeg avec libx264). Ces scripts n’installent pas les ressources sur le système.
