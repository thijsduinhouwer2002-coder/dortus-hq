#!/bin/bash
# Vera, 16 nov 2026. Eén meetpunt voor het effect van de Reddit-post (16 nov 20:05 UTC) en
# BlenderNation (ingezonden 16 nov ±21:20 UTC) op de gratis Click Joints.
# Gebruik vanuit de hoofdmap: bash platformen/verkenner/data/click-joints-uur-script.sh
# Voegt een regel toe aan platformen/verkenner/data/click-joints-uur.csv. Alleen openbare pagina's.
uit=platformen/verkenner/data/click-joints-uur.csv
[ -f "$uit" ] || echo "datum_utc,downloads,blendernation_artikel,bron" > "$uit"
d=$(curl -s https://extensions.blender.org/add-ons/click-joints/ | tr -s ' \n' ' ' \
  | grep -o -E "<dt> ?Downloads ?</dt> ?<dd> ?[0-9,.]+" | grep -o -E "[0-9,.]+$" | tr -d ',.')
# BlenderNation: alleen "ja" als er een artikellink met click-joints in de zoekresultaten staat
bn=$(curl -s "https://www.blendernation.com/?s=click+joints" \
  | grep -o -i -E 'href="https://www\.blendernation\.com/20[0-9]{2}/[^"]*click-joints[^"]*"' | head -1)
[ -n "$bn" ] && bn="ja" || bn="nee"
echo "$(date -u '+%Y-%m-%d %H:%M'),${d:-?},$bn,curl" >> "$uit"
tail -1 "$uit"
