#!/usr/bin/env bash
# Rendert de plaatjes voor de Reddit-versie uit de echte 3D-modellen van Hats (producten/steam-hol/modellen),
# groter dan de horlogekit, zodat ze op een telefoon scherp zijn. Daarna: python3 kunst/knip.py.
# Gebruik: kunst/render.sh <python met bpy> <uitmap>
# Python met bpy: python3 -m venv /tmp/bpyvenv && /tmp/bpyvenv/bin/pip install bpy (±430 MB, Python 3.13).
# Duur: ±42 s per beeld op 2 kernen, 19 beelden, samen ±14 minuten.
set -euo pipefail
PY="$1"; UIT="$2"
M="$(cd "$(dirname "$0")/../../steam-hol/modellen" && pwd)"
mkdir -p "$UIT"
cd "$M"
for s in rust hap blij knipper kneep; do
  "$PY" gloop.py "$UIT/gloop-$s.png" 1 0 720 720 32 "$s" > "$UIT/log-gloop-$s.txt" 2>&1
done
for s in schrik vallen stap1 stap2; do
  HOL_VERBERG='["hoed"]' "$PY" held.py "$UIT/held-$s.png" ridder "$s" 560 560 32 > "$UIT/log-held-$s.txt" 2>&1
done
for n in 0 1 2 3 4 5 6 7 8 9; do
  "$PY" hoeden.py "$UIT/hoed-$n.png" 360 360 32 "$n" > "$UIT/log-hoed-$n.txt" 2>&1
done
echo klaar > "$UIT/klaar.txt"
