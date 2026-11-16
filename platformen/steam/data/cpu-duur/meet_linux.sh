#!/bin/bash
# meet.sh <naam> <extra args...>
N=$1; shift
D=/tmp/claude-0/-home-claude/7a508a48-b30d-54e1-88da-597464a5e9c6/scratchpad/run-$N; rm -rf $D; mkdir -p $D/home
G=/tmp/claude-0/-home-claude/7a508a48-b30d-54e1-88da-597464a5e9c6/scratchpad/Godot_v4.3-stable_linux.x86_64
cd /home/claude/dortus-hq/producten/steam-hol/godot
HOME=$D/home XDG_DATA_HOME=$D/home xvfb-run -a -s "-screen 0 1920x1080x24" $G --rendering-driver opengl3 --path . -- hoogte=120 vers=1 zaad=4242 duur=250 log=$D/hol.log "$@" > $D/uit.txt 2>&1 &
sleep 8
P=$(pgrep -n -f "run-$N/hol.log" | head -1); P=$(pgrep -f "Godot.*run-$N" | tail -1)
T=$(getconf CLK_TCK); prev=0
for i in $(seq 1 23); do sleep 10; [ -e /proc/$P/stat ] || break; s=$(awk '{print $14+$15}' /proc/$P/stat); echo "scale=3; ($s-$prev)/$T" | bc >> $D/cpu.txt; prev=$s; done
wait
