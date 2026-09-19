#!/bin/sh
# Configure le fond d'écran KGI-OS à la première session XFCE seulement.
# Après cette première application, l'utilisateur est libre de le modifier.
set -u

IMAGE="/usr/share/backgrounds/kgi-os/logo.png"
STATE_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/kgi-os"
MARKER="$STATE_DIR/wallpaper-initialized-v1"

[ -s "$IMAGE" ] || exit 0
[ -e "$MARKER" ] && exit 0
command -v xfconf-query >/dev/null 2>&1 || exit 0

# XFCE utilise un identifiant de moniteur variable selon le PC.
# Réutiliser les chemins existants plutôt que supposer 'monitor0'.
PROPS="$(xfconf-query -c xfce4-desktop -lv 2>/dev/null | awk '$1 ~ /^\/backdrop\/.*\/last-image$/ { print $1 }')"
[ -n "$PROPS" ] || exit 0

SUCCESS=0
OLDIFS="$IFS"
IFS='
'
for PROP in $PROPS; do
    if xfconf-query -c xfce4-desktop -p "$PROP" -s "$IMAGE" >/dev/null 2>&1; then
        SUCCESS=1
        STYLE="${PROP%/*}/image-style"
        # XFCE : 4 = image mise à l'échelle sans découpage.
        xfconf-query -c xfce4-desktop -p "$STYLE" -s 4 >/dev/null 2>&1 || true
    fi
done
IFS="$OLDIFS"

if [ "$SUCCESS" -eq 1 ]; then
    mkdir -p "$STATE_DIR"
    : > "$MARKER"
fi
