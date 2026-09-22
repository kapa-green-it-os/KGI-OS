#!/bin/sh
# Prépare uniquement un arbre de fichiers. N'active aucune configuration.
set -eu
if [ "$#" -ne 1 ]; then
  echo "Usage : sh preparer-ressources.sh DOSSIER_DE_PREPARATION" >&2
  exit 2
fi
src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
mkdir -p -- "$1"
dest=$(CDPATH= cd -- "$1" && pwd)
if [ "$dest" = / ] || [ "$dest" = "$src" ]; then
  echo "Choisir un dossier de préparation distinct, jamais la racine système." >&2
  exit 2
fi
install -d "$dest/usr/share/backgrounds/kgi-os" "$dest/usr/share/kgi-os/installateur" "$dest/usr/share/kgi-os/plymouth" "$dest/usr/share/kgi-os/animation"
install -m 644 "$src/06-fond-ecran/kgi-bureau.png" "$dest/usr/share/backgrounds/kgi-os/"
install -m 644 "$src/03-connexion/kgi-connexion.png" "$dest/usr/share/backgrounds/kgi-os/"
install -m 644 "$src/07-ecran-veille/kgi-veille.png" "$dest/usr/share/backgrounds/kgi-os/"
install -m 644 "$src/02-plymouth/kgi-demarrage.png" "$dest/usr/share/kgi-os/plymouth/"
install -m 644 "$src/01-installateur/kgi-bienvenue-752x448.png" "$src/01-installateur/kgi-bienvenue-960x600.png" "$src/01-installateur/profils-fr.json" "$dest/usr/share/kgi-os/installateur/"
for size in 16 24 32 48 64 128 256 512; do
  icon_dir="$dest/usr/share/icons/hicolor/${size}x${size}/apps"
  install -d "$icon_dir"
  for name in kgi-os kgi-install-usb kgi-a-propos; do
    install -m 644 "$src/04-icones/png/$name-$size.png" "$icon_dir/$name.png"
  done
done
install -m 644 "$src/08-fond-anime/kgi-bureau-anime-1280x720.mp4" "$dest/usr/share/kgi-os/animation/"
echo "Ressources préparées dans $dest — configurations et tests ISO à réaliser."
