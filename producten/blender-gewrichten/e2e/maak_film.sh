#!/usr/bin/env bash
# Demofilm Click Joints Pro in elkaar zetten uit de beelden van film_pro.py (opdracht hoofdchat 15 nov 17:55).
#   bash e2e/maak_film.sh <map met beelden/ en film.json> <uitmap>
# Geeft click-joints-pro-demo.mp4 (1920x1080, 30 fps, H.264, -preset veryfast, geen geluid) en
# click-joints-pro-demo.gif (de buig en het rood, ±7 s, 960 breed, voor fora).
# Onderschriften en eindbeeld in de huisstijl van de poster (Inter, #23262D, mint #3BE6B0). Geen prijs in beeld.
set -euo pipefail
IN="$1"; UIT="$2"; mkdir -p "$UIT"
J="$IN/film.json"
fps=$(python3 -c "import json;print(json.load(open('$J'))['fps'])")
deel() { python3 -c "import json;print(json.load(open('$J'))['delen']['$1'])"; }
HA=$(deel haak); P=$(deel plaats); KN=$(deel knop); BU=$(deel buig); R=$(deel rood); K=$(deel kogel); E=$(deel eind)
t() { python3 -c "print(round(($1 - 1) / $fps, 3))"; }
tP=$(t "$P"); tH=$(t "$KN"); tB=$(t "$BU"); tR=$(t "$R"); tK=$(t "$K"); tE=$(t "$E")
VET=$(fc-match -f '%{file}' 'Inter:style=Bold')
GEW=$(fc-match -f '%{file}' 'Inter:style=Regular')
onder() {   # tekst, van, tot
  printf "drawtext=fontfile='%s':text='%s':fontsize=46:fontcolor=0xF1F3F7:x=60:y=h-120:box=1:boxcolor=0x23262D@0.88:boxborderw=22:enable='between(t,%s,%s)'" "$VET" "$1" "$2" "$3"
}
# v2 (Daan M4): de film opent met de knie die buigt (deel haak), zonder onderschrift; daarna pas de tekst.
F="$(onder 'One piece. Pick the bend you need.' "$tP" "$tH"),"
F+="$(onder 'Place hinge  115°' "$tH" "$tB"),"
F+="$(onder 'Bend it. The arc shows the real range.' "$tB" "$tR"),"
F+="$(onder 'Past the stop, the parts that collide turn red.' "$tR" "$tK"),"
F+="$(onder 'Ball joints show their fit in green.' "$tK" "$tE")"
# Kan (Daan): bij Place hinge de knop uit de zijbalk 2x vergroot ernaast, met een mint rand (zelfde beeld, uitsnede).
KX=${KNOP_X:-1555}; KY=${KNOP_Y:-785}
ffmpeg -y -loglevel error -framerate "$fps" -i "$IN/beelden/b%05d.png" -filter_complex \
"[0:v]split[a][b];[b]crop=316:70:$KX:$KY,scale=632:140:flags=lanczos,pad=640:148:4:4:color=0x3BE6B0[z];\
[a][z]overlay=x=840:y=210:enable='between(t,$tH,$tB)',$F,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 18 -r "$fps" "$UIT/deel1.mp4"
# Eindbeeld 3 s (Daan kan): titel links, het gebogen been van poster 3 rechts; geen prijs
POSTER="$(dirname "$0")/../../../ontwerp/click-joints/pro/poster-3.png"
ffmpeg -y -loglevel error -f lavfi -i "color=c=0x23262D:s=1920x1080:r=$fps:d=3" -loop 1 -t 3 -i "$POSTER" -filter_complex \
"[1:v]crop=1000:760:830:120,scale=900:-1:flags=lanczos[p];[0:v][p]overlay=x=930:y=(H-h)/2,\
drawtext=fontfile='$VET':text='Click Joints Pro':fontsize=96:fontcolor=0xF1F3F7:x=110:y=h/2-130,\
drawtext=fontfile='$GEW':text='Print-ready joints for Blender':fontsize=44:fontcolor=0xC9CDD8:x=110:y=h/2+10,\
drawtext=fontfile='$VET':text='on Superhive':fontsize=52:fontcolor=0x3BE6B0:x=110:y=h/2+100,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 18 -r "$fps" "$UIT/eind.mp4"
printf "file '%s'\nfile '%s'\n" "$UIT/deel1.mp4" "$UIT/eind.mp4" > "$UIT/lijst.txt"
ffmpeg -y -loglevel error -f concat -safe 0 -i "$UIT/lijst.txt" -c:v libx264 -preset veryfast -crf 18 \
  -pix_fmt yuv420p -movflags +faststart -an "$UIT/click-joints-pro-demo.mp4"
rm -f "$UIT/deel1.mp4" "$UIT/eind.mp4" "$UIT/lijst.txt"
# GIF: buig en rood (vanaf 1,5 s in de buig tot vlak voor de kogel), 15 fps, 960 breed
gA=$(python3 -c "print($tB + 0.8)"); gB=$(python3 -c "print($tK - 0.2)")   # buig en rood met de stilstand (opdracht 5 tot 8 s)
ffmpeg -y -loglevel error -ss "$gA" -to "$gB" -i "$UIT/click-joints-pro-demo.mp4" \
  -vf "fps=15,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" \
  "$UIT/click-joints-pro-demo.gif"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate,codec_name -of compact "$UIT/click-joints-pro-demo.mp4"
ls -la "$UIT"
