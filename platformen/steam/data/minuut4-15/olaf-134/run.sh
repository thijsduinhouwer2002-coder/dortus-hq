#!/bin/bash
# run.sh uitmap zaden herhalingen
cd /home/claude/dortus-hq/producten/steam-hol/godot
G=~/godot/Godot_v4.3-stable_linux.x86_64
out=$1; mkdir -p $out
for z in $2; do for r in $(seq 1 $3); do
 timeout 600 $G --headless --path . --fixed-fps 5 -- hoogte=120 vers=1 zaad=$z uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=900 2>&1 | grep "^HOL" > $out/z$z-r$r.log &
done; done; wait
