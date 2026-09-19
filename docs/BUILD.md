# Construire l'ISO de développement KGI-OS

> Version expérimentale : la compilation et l'installation ne sont pas encore validées.

## Machine de compilation recommandée

Utiliser une machine/VM **Debian 13 (trixie) amd64** avec connexion Internet, accès sudo, suffisamment de RAM et au moins **25 Go d'espace libre** pour commencer (prévoir davantage selon les caches et les paquets). Compiler sur un Linux natif ou une VM Linux, pas directement depuis l'invite de commandes Windows.

Installer les outils :

```bash
sudo apt update
sudo apt install -y live-build debootstrap xorriso squashfs-tools \
  grub-pc-bin grub-efi-amd64-bin isolinux syslinux-common
```

Récupérer la branche de développement :

```bash
git clone --branch dev/base-debian-live https://github.com/kapa-green-it-os/KGI-OS.git
cd KGI-OS
sudo bash build.sh
```

Le script configure une image Debian 13 amd64 Live ISO hybride, XFCE et l'installateur Debian en mode Live. La compilation télécharge les paquets Debian nécessaires. Le nom et la taille du fichier ISO résultant ne sont pas garantis.

**Ne pas graver sur un disque contenant des données importantes avant validation.** L'installateur peut effacer le disque cible.

## Relancer proprement une compilation

Depuis la racine du dépôt, après avoir vérifié que vous n'avez aucune modification locale à conserver :

```bash
sudo lb clean --purge
sudo rm -f config/common config/bootstrap config/chroot config/binary config/source
sudo bash build.sh
```

Les fichiers listés par `rm` sont générés par `lb config`. Ne supprimez **pas** les dossiers `config/package-lists/` ou vos futurs fichiers de personnalisation.

## Vérifier le fichier obtenu

```bash
sha256sum ./*.iso
```

Une somme de contrôle vérifie l'intégrité du fichier, **pas** la réussite du démarrage ni la stabilité du système. Suivre ensuite [TESTING.md](TESTING.md).

## Limitations de cette première base

- Architecture **amd64 seulement** ; pas de version pour les très anciens CPU 32 bits.
- La liste de firmwares inclut des logiciels redistribuables sous licences distinctes ; vérifier les licences avant publication.
- L'installateur, le démarrage UEFI/BIOS, la session Live et le réseau restent **à tester** sur VM et sur les modèles réels de l'atelier.
- Les sources Debian évoluent : conserver les manifests, les journaux de compilation et l'empreinte SHA-256 pour chaque version testée.
