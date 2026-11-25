# Galerijbeelden Click Joints Pro (issue #49, Beeldmaker, 25 nov 2026)

Waarom: de sale begint vr 27 nov; het hoofdbeeld (robot uit elkaar) is GESLAAGD, de galerij erachter was nog de oude zonder tekst (held-3 plek 4). Beide rechters vroegen om tekst op elk beeld en een gedetailleerd personage (lat `organisatie/lat/click-joints-pro.md`, gat 5).

**Figuur:** dezelfde robot als het hoofdbeeld, eigen werk van Dortus (`commercie/filmpjes/studio/figuur_robot.py`, licentie `commercie/filmpjes/studio/modellen/robot-dortus-LICENTIE.md`). Geen download, geen AI-beeld. Alles is een render, geen foto van een print.
**Add-on:** zip van main (Pro 1.2.8, `bash producten/blender-gewrichten/e2e/maak_zip.sh betaald`). Gewrichten, eindstop en staafjes maakte de add-on zelf; alleen kleur (goud op de gewrichten), pose en camera zijn van ons. Getallen in beeld komen uit de json naast elk beeld.

| Beeld | Wat | Getallen (GEZIEN, json) |
|---|---|---|
| `knie-*` | "Knees stop where your rig stops": zijaanzicht, linkerknie gebogen tot de eindstop, gradenboog 0 tot de stop | stop 120° (`beelden/knie.json`, `stop_graden`) |
| `klik-*` | "Rig in. Parts out.": links het figuur met de botten van de rig (half doorzichtig), rechts de delen uit Figure from rig | 4 scharnieren, 5 kogels (`beelden/klik.json`) |
| `strip-*` | "Find the fit for your printer": de vijf staafjes van Fit test: ball, bovenste helft opgetild en gekanteld zodat je kogel en kom ziet | 0.10 tot 0.30 mm (`beelden/strip.json`) |

Maken (Blender 5.3.0, Cycles 32 samples, 2400x1350, lokaal in de sessie):
```
GB_MODUS=strip GB_TIL=10 GB_KANTEL_TOP=-40 GB_OP=0.3 GB_ZIJ=-0.75 GB_AFSTAND=400 GB_GOUDZONE=12 GB_SHIFT=-0.17 HB_LICHT=2.6 \
  blender -b --factory-startup --python bron/galerij.py -- <pro-zip> <uit> 32 100
GB_MODUS=knie GB_KANT=-1 GB_UIT=6 GB_HEUP=-22 GB_SCHUIN=0.12 GB_AFSTAND=620 GB_HOOG=5 GB_SHIFT=-0.17 HB_LICHT=2.6 (zelfde regel)
GB_MODUS=klik HB_DRAAI=-8 HB_KANTEL=5 HB_SHIFT=0 HB_VUL=0.66 HB_LICHT=2.6 (zelfde regel)
python3 bron/tekst.py <knie|klik|strip> <uit>/render-<modus>.png <uit>/<modus>.json beelden <fontmap met Bricolage.ttf en Inter.ttf> ../click-joints/bron/icoon.svg
```
Uit: `<modus>-2400x1200.jpg` (Superhive) en `<modus>-1920x1080.jpg` (Gumroad).
Blinde test: sets `organisatie/blindtest/sets/click-joints-pro-galerij-{knie,klik,strip}.json`, tegen galerijbeelden van Cleave, CatPin en Split 3D Print.
