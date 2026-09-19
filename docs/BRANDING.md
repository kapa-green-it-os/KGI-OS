# Identité visuelle KGI-OS — prochaine compilation

Cette personnalisation est **prévue, pas encore intégrée** à l'ISO expérimentale actuelle. Ne pas modifier les menus de démarrage tant que la base Live et l'installateur ne sont pas validés.

## Identité KAPA Green IT

- Nom de la distribution : **KGI-OS — KAPA Green IT OS**.
- Reprendre le logo officiel KAPA Green IT fourni par l'association, sans le déformer. Conserver le fichier source et ses droits dans le dossier de travail du projet ; vérifier sa licence de diffusion avant publication publique.
- Préparer un fond d'écran 1920×1080 et une déclinaison pour les écrans plus petits, avec contraste suffisant et texte lisible.
- Définir le fond d'écran XFCE par défaut sans verrouiller les préférences : l'utilisateur pourra le remplacer.
- Personnaliser l'écran de connexion LightDM de manière sobre, sans autologin ni mot de passe par défaut.

## Démarrage de la clé USB et du système installé

- Afficher **KGI-OS — KAPA Green IT** sur le menu de démarrage Live.
- Préserver **toutes les entrées de démarrage et d'installation** ainsi que leurs paramètres existants, en BIOS et en UEFI.
- N'ajouter un thème GRUB ou un fond ISOLINUX qu'après un essai réussi du démarrage de base et une inspection des fichiers de bootloader effectivement générés par live-build.
- Ne pas masquer les messages d'erreur critiques derrière une animation ; tester le mode de récupération et le retour au menu.

## Distribution technique des ressources

Le manuel Debian Live prévoit les fichiers à ajouter dans le système Live sous `config/includes.chroot/`, par exemple un fond d'écran dans `usr/share/backgrounds/kgi-os/` et une configuration de bureau adaptée sous `etc/xdg/` ou `etc/skel/`.

Les thèmes de menus d'amorçage relèvent du paramétrage spécifique du chargeur BIOS ou UEFI. **Ne pas copier un thème prévu pour un autre chargeur** : vérifier le format et la résolution nécessaires.

## Applications

Conserver la liste d'applications déjà présente dans `config/package-lists/kgi-desktop.list.chroot`. La seule addition demandée est une logithèque graphique `gnome-software` définie dans `config/package-lists/kgi-software-center.list.chroot`. Ce n'est **pas** le Google Play Store pour applications Android. La boutique est à tester dans XFCE pour confirmer que les dépôts APT, la recherche, l'installation et les autorisations fonctionnent bien. Ne pas activer Flatpak/Flathub ou ajouter d'autres applications sans décision explicite.

## Critères d'acceptation

- [ ] Fond d'écran KAPA affiché en session Live et après installation.
- [ ] Logo et nom KGI-OS sur le démarrage BIOS et UEFI.
- [ ] Menus Live et installation toujours accessibles et fonctionnels.
- [ ] Bureau et écran de connexion utilisables après redémarrage.
- [ ] Logithèque visible, pouvant installer puis désinstaller une application de test via APT.
- [ ] Le système reste fluide sur une machine reconditionnée de référence.
- [ ] Aucune ancienne ISO instable présentée comme stable.
