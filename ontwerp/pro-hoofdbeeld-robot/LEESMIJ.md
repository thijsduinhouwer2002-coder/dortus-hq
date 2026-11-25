# Hoofdbeeld Click Joints Pro met de robot (issue #1, Beeldmaker, 25 nov 2026)

Waarom: blinde test 24 nov, beide rechters: een gedetailleerd, gestileerd personage in plaats van de tekenpop, en tekst op elk beeld.

**Figuur:** de robot-actiefiguur uit `commercie/filmpjes/studio/figuur_robot.py`, eigen werk van Dortus (licentie: `commercie/filmpjes/studio/modellen/robot-dortus-LICENTIE.md`). Geen download, geen AI-beeld.
**Gewrichten:** gemaakt door de echte knop Figure from rig van Click Joints Pro (zip van main, 1.2.8): 9 gewrichten, ellebogen 0 tot 140°, knieën 0 tot 120°, schouders ±30°, heupen ±22 en ±30°, nek ±20° (GEZIEN, `beelden/hoofdbeeld-uit.json`). Alleen de kleur van de gewrichten is goud gezet; de vorm is wat de add-on maakte. De getallen op de labels komen uit die json.
**Render:** Blender 5.3.0, Cycles 40 samples, 2400x1350, lokaal in de sessie van de Beeldmaker. Vloer met rasterlijnen als printplaat (alleen kleur). Het beeld is een render, geen foto.

Maken:
```
blender -b --factory-startup --python bron/hoofdbeeld.py -- <pro-zip> <uit> 40 100
  (uit elkaar: HB_UIT=22 HB_LICHT=2.6 HB_VUL=0.88 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.2)
  (heldenpose: HB_UIT=0  HB_LICHT=2.6 HB_VUL=0.86 HB_DRAAI=-22 HB_KANTEL=7 HB_SHIFT=-0.2)
python3 bron/tekst.py <render.png> <json> <uit> <fontmap> ontwerp/click-joints/bron/icoon.svg <naam> [labels]
```
Kandidaten in `beelden/`: robot-uit-labels, robot-uit, robot-held (elk 2400x1200 voor Superhive en 1920x1080 voor Gumroad).
Blinde test: sets `click-joints-pro-robot-superhive` en `click-joints-pro-robot-gumroad`.

**Sale-versie (issue #56, 25 nov):** `beelden/robot-uit-labels-sale-1920x1080.jpg` = het GESLAAGDE Gumroad-hoofdbeeld met rechtsboven de gouden sticker "-25% CYBER25 until Dec 1" (zelfde stijl als de tekenpop-sale). Alleen Gumroad, alleen vr 27 nov t/m di 1 dec; daarna terug naar `robot-uit-labels-1920x1080.jpg`. Niet op Superhive (daar 35% zonder code). Maken: `python3 bron/sale.py beelden/robot-uit-labels-1920x1080.jpg beelden/robot-uit-labels-sale-1920x1080.jpg <fontmap met Inter.ttf en Bricolage.ttf>`.

**Vierkant voor Gumroad (issue #94, 25 nov):** `beelden/robot-vierkant-600x600.jpg` en `-1200x1200.jpg` (Discover, profiel, zoeken), plus `robot-vierkant-sale-*` met de gouden sticker (alleen Gumroad, vr 27 nov t/m di 1 dec; wo 2 dec terug naar het gewone vierkant). Zelfde robot en zelfde echte Figure from rig (Pro 1.2.8, zip van main), nu vierkant gerenderd met de robot rechts (`beelden/hoofdbeeld-vierkant.json`). Blinde test: set `click-joints-pro-vierkant-gumroad` tegen de Gumroad-vierkanten van Cleave, Split 3D Print en MACHIN3tools (Buildify en BagaPie hebben geen Gumroad-pagina meer die curl vindt: 404; Cleave en Split zijn de echte concurrenten op Gumroad).
```
HB_W=1200 HB_H=1200 HB_UIT=22 HB_LICHT=2.6 HB_VUL=0.9 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.19 HB_SHIFT_Y=0.015 \
  blender -b --factory-startup --python bron/hoofdbeeld.py -- <pro-zip> <uit> 64 100
python3 bron/vierkant.py <uit>/hoofdbeeld-render.png <uitmap> <fontmap> ontwerp/click-joints/bron/icoon.svg [sale]
```
