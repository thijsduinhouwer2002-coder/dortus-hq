#!/bin/sh
# Mila ronde 5b: render op dubbele grootte en verklein (scherper; frisse kijker vond 1x "zacht, alsof opgeschaald").
# Gebruik: sh maak_alles.sh <venv-python>
PY=${1:-python}; T=$(mktemp -d)
$PY capsule3d.py $T/h.png 1840 860 32 && $PY capsule3d.py $T/k.png 924 348 32 klein && $PY capsule3d.py $T/m.png 2464 1412 24 || exit 1
python3 -c "
from PIL import Image
for a,b,w,h in [('h','header-920x430',920,430),('k','klein-462x174',462,174),('m','hoofdbeeld-1232x706',1232,706)]:
    Image.open('$T/'+a+'.png').convert('RGB').resize((w,h),Image.LANCZOS).save(b+'.png')
"
