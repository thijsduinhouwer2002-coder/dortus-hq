# YouTube-miniatuur Click Joints Pro (issue #346, Beeldmaker, 28 nov 2026)

Voor de lange video 4-3l3MZZWPc ("Ball Joints for 3D Printed Action Figures in Blender", titel van Bram #345). Waarom: op YouTube bij "ball joint blender addon" staat die video op plek 14 van 16 met 18 views (GEZIEN door de Afkijker, `organisatie/lat/vindbaar/uitslag-2026-11-28.json`), met een schermbeeld als miniatuur.

**Beeld:** `beelden/yt-pro-r1-1280x720.jpg` (ook `-320.jpg` om te zien hoe hij klein leest).
- Figuur: de held uit `ontwerp/pro-hoofdbeeld-held/` ronde 3/4 (Human Base Meshes, CC0, bron en licentie in `ontwerp/pro-hoofdbeeld-held/bron/LICENTIE-figuur.md`). Alle delen, kogels, kommen en scharnieren maakte de echte knop Figure from rig van Pro (zip van main als 1.2.9). Uit elkaar 18 mm, zelfde pose en kleuren als held-knie-r4.
- Nieuw: de twee heupkogels in goud (`bron/miniatuur.py`, alleen kleur, 3.872 vlakken, GEZIEN in `beelden/miniatuur.json`), zodat de kogels op de duim opvallen. Vorm en plek zijn die van de add-on.
- Inzet: kogel en kom van de heup met het echte gaas (`ontwerp/pro-galerij/bron/kom_kogel.py`, zelfde scène als het galerijbeeld kom-kogel, 1000x1000, maten in `beelden/inzet-kom-kogel.json`: kogel 13,0 mm, speling gemeten 0,1996 mm).
- Tekst: 3 woorden, "BALL JOINTS" en "1-CLICK" (Bricolage Grotesque Bold, OFL). Geen bewering over printen.
- Render: lokaal Blender 5.3.0, Cycles 64 samples op 2560x1440, 429 s; inzet 48 samples, 54 s (GEZIEN). Geen AI, geen foto.

```
PRO_VERSIE=1.2.9 bash producten/blender-gewrichten/e2e/maak_zip.sh betaald
HELD_HALS=-0.01,0.845 HELD_KIN=-0.045,0.875 HELD_KLEUR=0 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-held/bron/maak_held.py -- human_base_meshes_bundle.blend <fig>/held-r3.blend 2
K='{"romp": "6EC6C0", "kop_los": "F4D03F", "bovenarm": "B9A3E3", "onderarm": "B9A3E3", "dij": "F08A7E", "scheen": "7FA8E8"}'
HB_BEWAAR=1 HB_NEK_TINT=0.78 HB_KOGEL_MINST="Left hip,Right hip" HB_DEELKLEUR="$K" HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 30, "Right knee": 8}' HB_FIGUUR=<fig>/held-r3.blend \
  HB_UIT=18 HB_LICHT=2.6 HB_VUL=1.0 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.22 HB_W=1280 HB_H=720 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <basis> 1 10
MN_LENS_X=1.3 MN_SHIFT=-0.15,0.11 blender -b <basis>/hoofdbeeld.blend --python ontwerp/pro-yt-miniatuur/bron/miniatuur.py -- <m> 64 200
HB_BEWAAR=1 HB_NEK_TINT=0.78 HB_KOGEL_MINST="Left hip,Right hip" HB_DEELKLEUR="$K" HB_POSE='{"Left knee": 0}' HB_FIGUUR=<fig>/held-r3.blend HB_UIT=0 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <basis0> 1 10
KK_DOORZICHTIG=1 KK_SHIFT=0 KK_MEE="Left knee" KK_ANDER="" KK_LICHT=6 KK_CAM=240,34,10 KK_DOEL=0,0,0 KK_UIT=22 KK_KANTEL=40 KK_MAAT=1000x1000 blender -b <basis0>/hoofdbeeld.blend --python ontwerp/pro-galerij/bron/kom_kogel.py -- <kk> 48 100
MT_INZET=500,505,225 MT_PLEK=0.862,0.25,0.215 MT_KOGEL=0.686,0.752 python3 ontwerp/pro-yt-miniatuur/bron/miniatuur_tekst.py <m>/miniatuur-render.png <kk>/kom-kogel-render.png beelden/yt-pro-r1-1280x720.jpg BricolageGrotesque-Bold.ttf
```
Plek van de lijn naar de kogel en van de uitsnede op het oog (GOK ±10 px).

**Blinde test:** set `organisatie/blindtest/sets/click-joints-pro-yt-miniatuur.json`: r1 en de huidige miniatuur tegen Cleave (Ball Joints Quick Tip), CatPin en Print That Thing (plek 1 op de zoekterm). Miniaturen van i.ytimg.com (curl 200, GEZIEN).

**Uitslag r1** (`organisatie/blindtest/uitslag/click-joints-pro-yt-miniatuur-2026-11-28-0359.md`): GESLAAGD, Gemini 1,0 tegen Cleave, CatPin en Print That Thing. De huidige miniatuur haalde in diezelfde set ook 1,0, dus daarna kop aan kop (huidige miniatuur als concurrent, set `...-kop.json`): r1 1,5 en later 2,0. Gemini vroeg in elke ronde om het echte paneel van de add-on.

**Ronde 2:** `beelden/yt-pro-r2-1280x720.jpg` = r1 plus een uitsnede van het echte paneel uit Blender 5.3.0 (`ontwerp/pro-galerij/beelden/paneel-rig-scherm-voor.jpg`: kop "Click Joints", "Rig found: mixamo_rig", knop "Figure from rig") met een gouden rand om de knop en een getekende muispijl. Let op: dat schermbeeld is van het CC0-figuur van de paneel-rig-beelden, niet van de held; de rignaam is die van dat bestand.
```
MT_Y=140 MT_PANEEL=ontwerp/pro-galerij/beelden/paneel-rig-scherm-voor.jpg,2462,122,2828,268 MT_KNOP=2477,220,2817,262 <MT_* als r1> python3 ontwerp/pro-yt-miniatuur/bron/miniatuur_tekst.py ... beelden/yt-pro-r2-1280x720.jpg BricolageGrotesque-Bold.ttf
```
Uitslag r2: GESLAAGD Gemini 1,0 tegen Cleave, CatPin en Print That Thing (`click-joints-pro-yt-miniatuur-2026-11-28-0407.md`); kop aan kop met de huidige miniatuur 1,5 (één ronde plek 1, één ronde plek 2 achter de huidige; `click-joints-pro-yt-miniatuur-kop-*`). Zelfde render als r1.
