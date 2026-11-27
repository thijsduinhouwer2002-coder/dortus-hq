#!/usr/bin/env bash
# Opname v7 (issue #159): echte Blender met interface onder Xvfb, beeld voor beeld (CJ_BEELD=1, zie regisseur-28/proces.py
# STAP): Blender schrijft zelf scherm-ruw.ts (30 bps, elk beeld 1/30 s), muis.txt, start.txt en film.json.
#   bash neem_op.sh <blender> <start.blend> <map> <zip>
set -u
BL=$1; START=$2; MAP=$3; ZIP=$4
mkdir -p "$MAP"
export CJ_BEELD=1
xsetroot -xcf /usr/share/icons/DMZ-White/cursors/left_ptr 32 2>/dev/null || true
"$BL" --gpu-backend opengl "$START" --python "$(dirname "$0")/proces8.py" -- "$MAP" "$ZIP"
echo "opname klaar: $(du -h "$MAP/scherm-ruw.ts" | cut -f1)"
