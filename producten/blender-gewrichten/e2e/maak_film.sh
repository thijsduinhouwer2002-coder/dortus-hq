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
P=$(deel plaats); BU=$(deel buig); R=$(deel rood); K=$(deel kogel); E=$(deel eind)
t() { python3 -c "print(round(($1 - 1) / $fps, 3))"; }
tP=$(t "$P"); tB=$(t "$BU"); tR=$(t "$R"); tK=$(t "$K"); tE=$(t "$E")
# Place hinge gebeurt na de draai van het hele been: 75 beelden (film_pro.py)
tH=$(t $((P + 75)))
VET=$(fc-match -f '%{file}' 'Inter:style=Bold')
GEW=$(fc-match -f '%{file}' 'Inter:style=Regular')
onder() {   # tekst, van, tot
  printf "drawtext=fontfile='%s':text='%s':fontsize=46:fontcolor=0xF1F3F7:x=60:y=h-120:box=1:boxcolor=0x23262D@0.88:boxborderw=22:enable='between(t,%s,%s)'" "$VET" "$1" "$2" "$3"
}
F="$(onder 'One piece. Pick the bend you need.' "$tP" "$tH"),"
F+="$(onder 'Place hinge  115°' "$tH" "$tB"),"
F+="$(onder 'Bend it. The arc shows the real range.' "$tB" "$tR"),"
F+="$(onder 'Past the stop, the parts that collide turn red.' "$tR" "$tK"),"
F+="$(onder 'Ball joints show their fit in green.' "$tK" "$tE")"
ffmpeg -y -loglevel error -framerate "$fps" -i "$IN/beelden/b%05d.png" -vf "$F,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 18 -r "$fps" "$UIT/deel1.mp4"
# Eindbeeld 3 s: naam en "on Superhive", zonder prijs
ffmpeg -y -loglevel error -f lavfi -i "color=c=0x23262D:s=1920x1080:r=$fps:d=3" -vf \
"drawtext=fontfile='$VET':text='Click Joints Pro':fontsize=120:fontcolor=0xF1F3F7:x=(w-tw)/2:y=h/2-130,\
drawtext=fontfile='$GEW':text='Print-ready joints for Blender':fontsize=48:fontcolor=0xC9CDD8:x=(w-tw)/2:y=h/2+30,\
drawtext=fontfile='$VET':text='on Superhive':fontsize=56:fontcolor=0x3BE6B0:x=(w-tw)/2:y=h/2+130,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 18 "$UIT/eind.mp4"
printf "file '%s'\nfile '%s'\n" "$UIT/deel1.mp4" "$UIT/eind.mp4" > "$UIT/lijst.txt"
ffmpeg -y -loglevel error -f concat -safe 0 -i "$UIT/lijst.txt" -c:v libx264 -preset veryfast -crf 18 \
  -pix_fmt yuv420p -movflags +faststart -an "$UIT/click-joints-pro-demo.mp4"
rm -f "$UIT/deel1.mp4" "$UIT/eind.mp4" "$UIT/lijst.txt"
# GIF: buig en rood (vanaf 1,5 s in de buig tot vlak voor de kogel), 15 fps, 960 breed
gA=$(python3 -c "print($tB + 1.5)"); gB=$(python3 -c "print($tK - 0.5)")   # ±7,4 s (opdracht 5 tot 8)
ffmpeg -y -loglevel error -ss "$gA" -to "$gB" -i "$UIT/click-joints-pro-demo.mp4" \
  -vf "fps=15,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" \
  "$UIT/click-joints-pro-demo.gif"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate,codec_name -of compact "$UIT/click-joints-pro-demo.mp4"
ls -la "$UIT"
