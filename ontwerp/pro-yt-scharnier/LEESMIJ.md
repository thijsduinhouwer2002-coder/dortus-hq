# YouTube-miniatuur scharniervideo Click Joints Pro (issue #352, Beeldmaker, 28 nov 2026)

Voor video m3sNvDOJYQ0 (nieuwe titel van #345: "Hinges for Poseable 3D Printed Figures in Blender: Stops at 115°"). Waarom: plek 16 van 16 bij "ball joint blender addon" met 24 views (GEZIEN door de Afkijker, `organisatie/lat/vindbaar/uitslag-2026-11-28.json`); de huidige miniatuur is een schermbeeld met ondertitel.

**Beeld:** `beelden/yt-scharnier-r1-1280x720.jpg` (ook `-320.jpg`).
- Figuur: de held (Blender Human Base Meshes v1.4.1, CC0, bron en licentie in `ontwerp/pro-hoofdbeeld-held/bron/LICENTIE-figuur.md`), kleuren als held-knie-r4.
- In de rig staat op beide knieën een Limit Rotation van 0 tot 115° (`bron/knie_grens.py`), zoals een koper zijn rig begrenst. De echte knop Figure from rig (Pro, zip van main als 1.2.9) las dat en maakte "Left knee · Hinge · 0–115° · from rig" (GEZIEN in de log; `beelden/knie-115.json`, `knie_cam.bereik` 115). Linkerknie in de pose op 115°, camera langs de scharnieras.
- Gradenboog 0° tot 115°: het getal komt van de add-on; draaipunt en richting van de scheen op het oog (GOK ±10 px en ±3°).
- Paneel: uitsnede van het echte paneel van 1.2.9 in Blender 5.3.0 (`ontwerp/pro-galerij/beelden/paneel-rig-scherm-na.jpg`): kop "Click Joints" en de rij "Or a hinge that bends up to: 90° 115° 135°", gouden rand om 115° en een getekende muispijl. Die knop maakt hetzelfde scharnier op een los model; op dit figuur kwam de 115° uit de rig. Beide zijn echte wegen naar 115°.
- Tekst: "HINGES" en "STOP AT 115°" (Bricolage Grotesque Bold, OFL). Geen bewering over printen. Geen AI, geen foto.
- Render: lokaal Blender 5.3.0, Cycles 64 samples, 1440x1440, 159 s (GEZIEN).

```
PRO_VERSIE=1.2.9 bash producten/blender-gewrichten/e2e/maak_zip.sh betaald
HELD_HALS=-0.01,0.845 HELD_KIN=-0.045,0.875 HELD_KLEUR=0 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-held/bron/maak_held.py -- human_base_meshes_bundle.blend <fig>/held-r3.blend 2
blender -b <fig>/held-r3.blend --python ontwerp/pro-yt-scharnier/bron/knie_grens.py -- <fig>/held-115.blend
K='{"romp": "6EC6C0", "kop_los": "F4D03F", "bovenarm": "B9A3E3", "onderarm": "B9A3E3", "dij": "F08A7E", "scheen": "7FA8E8"}'
HB_DEELKLEUR="$K" HB_KOGEL_MINST="Left hip,Right hip" HB_NEK_TINT=0.78 HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 115, "Right knee": 10, "Right hip": [[[1,0,0], -20]]}' \
  HB_FIGUUR=<fig>/held-115.blend HB_LICHT=2.6 HB_VUL=0.80 HB_UIT=4 HB_KNIE_CAM="Left knee" HB_KNIE_KANT=-1 HB_KNIE_AFSTAND=340 HB_KNIE_SCHUIF=8,8 \
  HB_KNIE_STRAAL=2000 HB_KNIE_LICHT=1.2 HB_KNIE_MAAT=1440 HB_KNIE_BOOG=1 HB_NAAM=knie HB_METAAL=0 \
  blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <uit> 64 100
ST_KNIE=0.422,0.55 ST_SCHEEN=-23 ST_PANEEL=2468,708,2826,776 ST_KOP_Y=118 ST_KOP_Y2=160 ST_KNOP=2590,745,2702,771 \
  python3 ontwerp/pro-yt-scharnier/bron/scharnier_tekst.py <uit>/knie-render.png ontwerp/pro-galerij/beelden/paneel-rig-scherm-na.jpg beelden/yt-scharnier-r1-1280x720.jpg BricolageGrotesque-Bold.ttf
```
Nieuw in `ontwerp/pro-galerij/bron/galerij.py` (modus knie): `HB_DEELKLEUR` en `HB_NEK_TINT` werken nu ook daar (alleen aan met hun variabele; oude beelden veranderen niet). Niet gebruikt voor r1, wel voor de proeven.

**Blinde test:** set `organisatie/blindtest/sets/click-joints-pro-yt-scharnier.json` (r1 tegen Cleave, CatPin en UArtsy "Swivel Hinge Joint", 71.430 views, top 20 op "articulated figure blender", GEZIEN in de uitslag van de Afkijker) en `...-yt-scharnier-kop.json` (r1 tegen de huidige miniatuur, Cleave en UArtsy).

**r2 (28 nov ±06:55):** `beelden/yt-scharnier-r2-1280x720.jpg`, gelijk aan r1 plus de regel "BLENDER ADD-ON" boven "HINGES" (wens Gemini in de kop-aan-kop-uitslag: laat zien dat het om Blender gaat). Geen Blender-logo (merk van de Blender Foundation). Zelfde opdracht als r1 met `ST_LABEL="BLENDER ADD-ON" ST_Y=250`.
