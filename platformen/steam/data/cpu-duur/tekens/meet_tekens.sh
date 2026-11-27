#!/bin/bash
# meet.sh <naam> <args...>: 12 min echt spel, per seconde "<unix> <ticks>" van het Godot-proces
N=$1; shift
D=${UIT:-/tmp/cpu}/$N; rm -rf $D; mkdir -p $D/home
G=${GODOT:-godot}   # Godot 4.3 Linux
cd /home/claude/dortus-hq/producten/steam-hol/godot
HOME=$D/home XDG_DATA_HOME=$D/home xvfb-run -a -s "-screen 0 1920x1080x24" $G --rendering-driver opengl3 --path . -- hoogte=120 vers=1 zaad=5 koper=1 balk=0 duur=740 log=$D/hol.log "$@" > $D/uit.txt 2>&1 &
sleep 5
P=$(pgrep -f "Godot.*$D/hol.log" | tail -1)
while [ -e /proc/$P/stat ]; do echo "$(date +%s.%N | cut -c1-14) $(awk '{print $14+$15}' /proc/$P/stat)" >> $D/cpu.txt; sleep 1; done
wait
