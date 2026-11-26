#!/bin/bash
# meet.sh uitmap: zaad 2 tot 9, elk 3 runs, 1200 s, zelfde args als Iris en Olaf (#134, #145)
cd ${GODOT_MAP:-/home/claude/dortus-hq/producten/steam-hol/godot}
G=~/godot/Godot_v4.3-stable_linux.x86_64
out=$1; mkdir -p $out
for z in 2 3 4 5 6 7 8 9; do for r in 1 2 3; do
 timeout 300 $G --headless --path . --fixed-fps 5 -- hoogte=120 vers=1 zaad=$z uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200 2>&1 | grep "^HOL" > $out/z$z-r$r.log &
done; wait; done
