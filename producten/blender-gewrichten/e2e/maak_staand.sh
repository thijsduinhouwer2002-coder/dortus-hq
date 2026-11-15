#!/usr/bin/env bash
# Losse staande opnames voor de korte filmpjes van Chris (opdracht hoofdchat 15 nov 23:00).
#   bash e2e/maak_staand.sh <map met beelden/ en film.json van film_pro.py met FILM_STAAND=1> <uitmap>
# Geeft per deel een mp4 van 1080x1920, 30 fps, H.264 (-preset veryfast), zonder geluid en zonder tekst
# (Chris zet de onderschriften), plus staand-beelden.jpg (het middelste beeld van elk deel) om te keuren.
# Alles in beeld komt van de add-on in de echte Blender; het script knipt alleen.
set -euo pipefail
IN="$1"; UIT="$2"; mkdir -p "$UIT"
J="$IN/film.json"
fps=$(python3 -c "import json;print(json.load(open('$J'))['fps'])")
n=$(python3 -c "import json;print(json.load(open('$J'))['n'])")
deel() { python3 -c "import json;print(json.load(open('$J'))['delen']['$1'])"; }
HA=$(deel haak); P=$(deel plaats); KN=$(deel knop); BU=$(deel buig); R=$(deel rood); K=$(deel kogel); E=$(deel eind)
knip() {   # naam, eerste beeld, laatste beeld
  local tel=$(( $3 - $2 + 1 ))
  ffmpeg -y -loglevel error -framerate "$fps" -start_number "$2" -i "$IN/beelden/b%05d.png" -frames:v "$tel" \
    -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -crf 18 -r "$fps" \
    -movflags +faststart -an "$UIT/click-joints-staand-$1.mp4"
  ffmpeg -y -loglevel error -framerate "$fps" -start_number $(( ($2 + $3) / 2 )) -i "$IN/beelden/b%05d.png" \
    -frames:v 1 -vf "scale=360:640:flags=lanczos" "$UIT/.midden-$1.png"
}
knip 1-knie-buigt "$HA" $((P - 1))        # de knie buigt door zijn bereik met de boog (haak)
knip 2-plaatsen "$P" $((BU - 1))          # het hele been, dan Place hinge (twee delen, groen)
knip 3-buigen "$BU" $((R - 1))            # de buig van 0 naar 115 graden met de gradenboog
knip 4-rood "$R" $((K - 1))               # voorbij de stop: de botsende delen worden rood
knip 5-kogel "$K" $((E - 1))              # de kogel met de groene pasband
ffmpeg -y -loglevel error -i "$UIT/.midden-1-knie-buigt.png" -i "$UIT/.midden-2-plaatsen.png" -i "$UIT/.midden-3-buigen.png" \
  -i "$UIT/.midden-4-rood.png" -i "$UIT/.midden-5-kogel.png" -filter_complex "hstack=inputs=5" -q:v 3 "$UIT/staand-beelden.jpg"
rm -f "$UIT"/.midden-*.png
for f in "$UIT"/*.mp4; do
  printf '%s ' "$(basename "$f")"
  ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 "$f" | tr '\n' ' '; echo
done
echo "beelden totaal $n"
