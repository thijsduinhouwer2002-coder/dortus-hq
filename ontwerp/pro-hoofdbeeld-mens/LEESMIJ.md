# Hoofdbeeld Click Joints Pro met een organisch figuur (issue #38, Beeldmaker, 26 nov 2026)

Waarom: het robotbeeld staat op Superhive op plek 1,75 (Gemini 2,0, ChatGPT 1,5; GEZIEN, #1). Gemini vroeg 3 van de 4 keer om een organisch personage. Weekdoel Pro: hoofdbeeld op plek 1 vóór de sale van vr 27 nov.

**Figuur:** MakeHuman base mesh (CC0 1.0, `commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md`), aangekleed door `commercie/filmpjes/studio/figuur_laden.py` (CJ_HALS=rond). Geen AI-beeld, geen foto van een print: alles is een render (Blender 5.3.0, Cycles, lokaal in de sessie van de Beeldmaker).
**Gewrichten:** gemaakt door de echte knop Figure from rig van Pro (zip van main, als 1.2.8): 9 gewrichten, ellebogen 0 tot 140°, knieën 0 tot 120°, nek en schouders ±20° (GEZIEN, `beelden/mens-uit.json`, `gewrichten`). De getallen op de labels komen uit die json.

Twee kandidaten, elk 2400x1200 voor Superhive:
- `mens-uit-labels-*`: zelfde opzet als het robotbeeld (`ontwerp/pro-hoofdbeeld-robot/`), nu met het mens-figuur, delen 18 mm uit elkaar (hoofd dichter bij de romp, Daan #17), tekst 12% groter (Daan #17). Ook 1920x1080.
  ```
  HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 30, "Right knee": 8, "Neck": [[[0,0,1], -12]]}' \
  CJ_HALS=rond HB_FIGUUR=mens HB_UIT=18 HB_LICHT=2.6 HB_VUL=0.88 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.2 \
    blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <uit> 40 100
  TK_GROOT=1.12 TK_BOVEN=0.08 python3 ontwerp/pro-hoofdbeeld-robot/bron/tekst.py <uit>/hoofdbeeld-render.png <uit>/hoofdbeeld.json <uitmap> <fontmap> ontwerp/click-joints/bron/icoon.svg mens-uit-labels labels
  ```
- `mens-klik-2400x1200.jpg`: het GESLAAGDE videobeeld 'Rig in. Parts out.' (`ontwerp/pro-videobeeld/`, YouTube plek 1,0 en 1,0) als 2:1, opnieuw gerenderd op 2400x1200 zodat het hele figuur in beeld staat; "9 joints" onder de pijl in plaats van over de voeten (json: `beelden/mens-klik.json`).
  ```
  CJ_HALS=rond HB_FIGUUR=mens GB_MODUS=klik HB_DRAAI=-8 HB_KANTEL=5 HB_LICHT=2.6 GB_AFSTAND_X=1.30 HB_W=2400 HB_H=1200 HB_VUL=0.72 HB_SHIFT=-0.15 \
    blender -b --factory-startup --python ontwerp/pro-galerij/bron/galerij.py -- <pro-zip> <uit> 48 100
  VB_SUPERHIVE=1 VB_TELLER_PIJL=1 python3 ontwerp/pro-videobeeld/bron/videobeeld.py <uit>/render-klik.png <uit>/klik.json <uitmap> <fontmap> ontwerp/click-joints/bron/icoon.svg mens-klik
  ```
Letters: Bricolage Grotesque en Inter (OFL, google/fonts).

**Blinde test:** set `organisatie/blindtest/sets/click-joints-pro-superhive-mens.json` tegen Cleave, CatPin en Split 3D Print (Superhive-hoofdbeelden, curl 200 op 26 nov). Klaar als: gemiddeld plek 1,5 of beter bij Gemini én ChatGPT.
