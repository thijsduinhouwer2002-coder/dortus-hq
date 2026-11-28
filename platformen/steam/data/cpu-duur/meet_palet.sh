#!/bin/bash
# meet.sh <map> <extra args...>: draait het spel 6 min op 1920x1080 xvfb, schrijft per seconde CPU-ticks
d=$1; shift; mkdir -p $d
cd /home/claude/dortus-hq/producten/steam-hol/godot
xvfb-run -a -s "-screen 0 1920x1080x24" ~/godot/Godot_v4.3-stable_linux.x86_64 --path . -- hoogte=200 vers=1 zaad=5 duur=370 balk=0 log=$d/hol.log "$@" > $d/uit.txt 2>&1 &
sleep 4
pid=$(pgrep -n -f "Godot_v4.3-stable_linux.x86_64 --path")
: > $d/cpu.txt
while kill -0 $pid 2>/dev/null; do
  read -a f < /proc/$pid/stat 2>/dev/null && echo "$(date +%s.%N) $(( ${f[13]} + ${f[14]} ))" >> $d/cpu.txt
  sleep 1
done
