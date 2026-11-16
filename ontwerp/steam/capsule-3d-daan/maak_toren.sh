#!/bin/sh
# Daan 16 nov 2026: capsule TOREN (richting "He wears their hats"). Gebruik: sh maak_toren.sh <venv-python>
# Rendert op dubbele grootte en verkleint, zoals Mila's maak_alles.sh.
PY=${1:-python}; T=$(mktemp -d)
export TOREN_ZAK=0.12,0.38,0.32,0.28,0.12
TOREN_GROOT=1.2 TOREN_CZ=3.0 TOREN_LENS=30 TOREN_TZ=0.9 TOREN_TM=1.15 HEADER_RY=-1.3 \
  $PY capsule_toren.py $T/h.png 1840 860 ${SAMPLES:-24} || exit 1
TOREN_KCZ=3.5 TOREN_KLENS=22 TOREN_KTZ=1.45 TOREN_KTM=1.5 TOREN_KTX=-0.2 \
  $PY capsule_toren.py $T/k.png 924 348 ${SAMPLES:-24} klein || exit 1
python3 -c "
from PIL import Image
for a,b,w,h in [('h','toren-header-920x430',920,430),('k','toren-klein-462x174',462,174)]:
    Image.open('$T/'+a+'.png').convert('RGB').resize((w,h),Image.LANCZOS).save(b+'.png')
"
