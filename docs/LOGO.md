# Ajouter le fond d'écran officiel KAPA Green IT

Le fond d'écran original n'est pas encore versionné dans le dépôt. **Ne lancez pas une nouvelle compilation branding sans avoir ajouté le PNG.** L'ISO de référence déjà compilée et testée reste utilisable indépendamment de ce travail.

## Chemin attendu

Enregistrez **le PNG officiel non modifié** à cet emplacement exact :

`config/includes.chroot/usr/share/backgrounds/kgi-os/wallpaper.png`

Le fichier doit conserver son extension `.png` et être une image PNG valide. N'enregistrez pas son contenu en texte/base64. GitHub permet de déposer le fichier via **Add file → Upload files** sur la branche `dev/base-debian-live` ; le chemin parent peut aussi être créé localement puis envoyé avec Git.

**Après l'ajout du PNG dans le dépôt**, sa copie dans l'ISO est automatique grâce au mécanisme `config/includes.chroot/` de Debian live-build.

## Ce qui est déjà préparé

- Au premier démarrage d'une session XFCE, `/etc/xdg/autostart/kgi-os-wallpaper.desktop` lance le script `/usr/local/lib/kgi-os/set-wallpaper.sh`.
- Le script utilise le fond d'écran PNG en fond d'écran, ajuste le rendu à l'écran et ne modifie plus le réglage après cette première application : chacun pourra ensuite choisir son propre fond d'écran.
- Le script détecte les identifiants réels des moniteurs plutôt que de supposer un nom fixe.
- Si le fond d'écran est absent, ou si XFCE n'a pas encore chargé ses paramètres, le script n'écrase aucun réglage. Dans ce dernier cas, il pourra être relancé à la prochaine connexion.

## Démarrage BIOS / UEFI

Le **thème du menu de démarrage n'est pas encore modifié**. Il sera intégré et validé séparément pour BIOS et UEFI afin de ne pas casser les options Live/Install. Le fond d'écran et le script ci-dessus concernent uniquement le bureau XFCE.

## Vérifications avant diffusion

Vérifier le fond d'écran avec une session Live, une session après installation et deux tailles d'écran différentes. Changer ensuite manuellement le fond d'écran et redémarrer : KGI-OS ne doit pas le remplacer.
