#!/usr/bin/env bash
# KGI-OS: first experimental Debian Live build.
set -Eeuo pipefail

cd "$(dirname "$0")"

if [[ $EUID -ne 0 ]]; then
  echo "Erreur : executer avec sudo bash build.sh" >&2
  exit 1
fi

if ! command -v lb >/dev/null 2>&1; then
  echo "Erreur : live-build absent. Voir docs/BUILD.md" >&2
  exit 1
fi

# Do not silently reuse configuration from a previous build.
if [[ -e config/common || -e config/binary ]]; then
  echo "Erreur : configuration live-build deja generee." >&2
  echo "Pour recommencer : sudo lb clean --purge puis supprimer les fichiers de configuration generes (voir docs/BUILD.md)." >&2
  exit 1
fi

lb config \
  --mode debian \
  --distribution trixie \
  --architectures amd64 \
  --binary-images iso-hybrid \
  --archive-areas "main contrib non-free non-free-firmware" \
  --debian-installer live \
  --debian-installer-gui true \
  --bootappend-live "boot=live components locales=fr_FR.UTF-8 keyboard-layouts=fr"

lb build 2>&1 | tee build.log

printf '\nISO produite (non validee) :\n'
find . -maxdepth 1 -type f -name '*.iso' -print
printf '\nNE PAS PUBLIER comme stable avant les tests BIOS/UEFI et installation.\n'
