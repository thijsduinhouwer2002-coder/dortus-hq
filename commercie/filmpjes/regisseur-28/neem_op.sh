#!/usr/bin/env bash
# Echte schermopname (issue #159, kopie van regisseur-26 met echt_held.py): ffmpeg x11grab neemt het hele X-scherm op, 30 beelden per seconde, terwijl Blender
# met de interface draait en echt_opname.py de gebruiker speelt. Draait binnen xvfb-run (met -noreset).
# - Tijd: x11grab geeft elk beeld de wandkloktijd; met -copyts en muxdelay 0 blijft die in de .ts staan (lokaal getoetst
#   25 nov). start.txt = wandkloktijd van het eerste beeld, zodat de delen uit film.json precies op de opname vallen.
# - Muis: x11grab tekent de pijl onder Xvfb maar af en toe; muisspoor.py schrijft de echte plek 60 keer per seconde
#   in muis.txt en montage3.py zet de pijl daar neer (zoals OBS).
#   bash neem_op.sh <blender> <start.blend> <map> <zip> <breed>x<hoog>
set -u
BL=$1; START=$2; MAP=$3; ZIP=$4; MAAT=$5
mkdir -p "$MAP"
xsetroot -xcf /usr/share/icons/DMZ-White/cursors/left_ptr 32 || echo "LET OP: geen pijl gezet"
python3 "$(dirname "$0")/../regisseur-26/muisspoor.py" "$MAP/muis.txt" &
MS=$!
STARTGOK=$(date +%s.%N)
ffmpeg -y -loglevel error -f x11grab -draw_mouse 0 -framerate 30 -video_size "$MAAT" -thread_queue_size 1024 \
  -i "$DISPLAY" -copyts -muxdelay 0 -muxpreload 0 -c:v libx264 -preset ultrafast -crf 12 -pix_fmt yuv420p \
  -f mpegts "$MAP/scherm-ruw.ts" &
FF=$!
sleep 1
"$BL" --gpu-backend opengl "$START" --python "$(dirname "$0")/echt_held.py" -- "$MAP" "$ZIP"
sleep 1
kill -INT $FF
wait $FF
kill $MS
python3 - "$MAP" "$STARTGOK" <<'PY'
import subprocess, sys
m, gok = sys.argv[1], float(sys.argv[2])
s = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=start_time", "-of", "csv=p=0",
                          f"{m}/scherm-ruw.ts"], capture_output=True, text=True).stdout.split()[0])
P = 2 ** 33 / 90000
start = s + round((gok - s) / P) * P
open(f"{m}/start.txt", "w").write(f"{start:.4f}\n")
print(f"eerste beeld op {start:.3f} (start ffmpeg {gok:.3f}, verschil {start - gok:.3f} s)")
PY
echo "opname klaar: $(du -h "$MAP/scherm-ruw.ts" | cut -f1)"
