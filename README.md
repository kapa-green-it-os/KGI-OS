# KGI-OS — KAPA Green IT OS

**Projet en développement : aucune ISO stable n'est encore publiée.**

KGI-OS est un projet de distribution Linux légère porté par KAPA Green IT pour faciliter le réemploi des ordinateurs, leur reconditionnement et l'inclusion numérique.

## Objectifs

- Prolonger la durée de vie de PC reconditionnés avec un système simple à utiliser.
- Proposer un bureau léger, un navigateur et une suite bureautique.
- Permettre le démarrage sur clé USB et l'installation sur disque, y compris sur des machines BIOS et UEFI compatibles.
- Produire une image ISO reproductible, testée et maintenable.

## État du projet

La base technique de l'ISO est en cours de réévaluation, car les prototypes précédents ne sont pas suffisamment stables. Le choix définitif de la distribution de base, de l'environnement de bureau et de l'installateur sera documenté après validation.

**Ne pas utiliser les prototypes pour remettre un ordinateur à un bénéficiaire ou écraser un disque contenant des données importantes.** Aucune compatibilité matérielle générale n'est garantie à ce stade.

## Développement et publication

Le dépôt accueillera progressivement :

- les scripts et fichiers de configuration permettant de reconstruire l'ISO ;
- les personnalisations graphiques KAPA Green IT ;
- les procédures de test (Live USB, BIOS/UEFI, installation, redémarrage, réseau, applications) ;
- la documentation d'installation et les notes de version.

Les fichiers de construction sont destinés au dépôt Git ; les images ISO validées et leurs empreintes SHA-256 seront proposées dans [Releases](https://github.com/kapa-green-it-os/KGI-OS/releases), ou sur un hébergement de téléchargement adapté si leur taille dépasse les limites de la plateforme. **Aucun téléchargement stable n'est encore disponible.**

## Contribuer et signaler un problème

Les retours sur le démarrage, l'installation et la compatibilité des ordinateurs reconditionnés sont bienvenus via les [Issues](https://github.com/kapa-green-it-os/KGI-OS/issues). Précisez le modèle du PC, la configuration, le mode de démarrage BIOS/UEFI et les étapes permettant de reproduire le problème. Ne publiez pas de mots de passe, clés privées ni de données personnelles dans les rapports.

## Licences et attribution

La licence du code propre à KGI-OS sera précisée après le choix de la base technique et la vérification des licences des composants repris. Les licences et mentions de paternité des projets tiers devront être conservées ; chaque logiciel inclus conserve sa propre licence.

---
Projet KAPA Green IT — Réemploi informatique et inclusion numérique.
