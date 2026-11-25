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
[GB_INZET=<uit>/render-klik.png bij strip] python3 bron/tekst.py <knie|klik|strip> <uit>/render-<modus>.png <uit>/<modus>.json beelden <fontmap met Bricolage.ttf en Inter.ttf> ../click-joints/bron/icoon.svg
```
Uit: `<modus>-2400x1200.jpg` (Superhive) en `<modus>-1920x1080.jpg` (Gumroad).
Blinde test: sets `organisatie/blindtest/sets/click-joints-pro-galerij-{knie,klik,strip}.json`, tegen galerijbeelden van Cleave, CatPin en Split 3D Print.

Ronde 1 (07:23 tot 07:28): klik GESLAAGD (Gemini 1,0, ChatGPT 1,0); knie 2,5 en 3,0, strip 2,5 en 3,5 niet geslaagd. Rechters: bij de strip "alleen proefstukjes, laat zien dat het gewrichten in je model zet"; bij de knie "laat de echte scharniervorm en speling zien". Ronde 2: strip met kaartje van de robot ("Then one click and every joint on your figure gets that clearance", robot uit dezelfde render als klik), knie met regel over het gemaakte scharnier en 0,20 mm speling. Een close-up met de delen ver uit elkaar (GB_UIT=12) werd onleesbaar en is niet gebruikt.

Ronde 3 knie (25 nov ±09:00): nieuw beeld `bereik-*`, **"Every joint knows its limit"**, in plaats van `knie-*` (dat twee keer niet slaagde). Heel figuur in een pose die elk bereik laat zien, met kaartjes bij vier gewrichten van twee soorten (nek kogel ±20°, schouder kogel ±30°, elleboog scharnier 0–140°, knie scharnier 0–120°; GEZIEN in `beelden/bereik.json`, `punten`), plus een kaartje met het scharnier van de linkerknie van dichtbij bij de stop (alleen dat been in beeld, delen 9 mm uit elkaar). Antwoord op de rechters: meer soorten gewrichten in één beeld en de scharniervorm van dichtbij.
```
GB_MODUS=bereik GB_SCH_R=-28 GB_UIT=9 HB_DRAAI=48 HB_KANTEL=6 HB_SHIFT=-0.2 HB_VUL=0.86 HB_LICHT=2.6 GB_ZAFSTAND=230 GB_ZSCHUIN=-0.2 GB_ZLENS=90 (zelfde regel, 32 samples)
GB_ZOOM=<uit>/render-bereik-knie.png GB_ZOOM_KADER=0.17,0.27,0.77,0.87 python3 bron/tekst.py bereik <uit>/render-bereik.png <uit>/bereik.json beelden <fonts> ../click-joints/bron/icoon.svg
```

## Beeld 4 (issue #101, 25 nov ±21:30): `delen-*`, "Every part, ready to print"
Waarom: Superhive vraagt minimaal 4 galerijbeelden (nu 3). ChatGPT miste in eerdere rondes (#1) dat je losse printbare delen krijgt; dit beeld laat precies dat zien. Alle 10 delen uit Figure from rig naast elkaar op een printplaat, met kaartjes bij een kogelkom (heup) en een kniescharnier, en wat de knop Export schreef: 10 STL- en 10 3MF-bestanden (GEZIEN, `beelden/delen.json`, `export`). Leggen, plaat en camera zijn van ons; de add-on legt de delen niet zelf neer. Add-on: zip van 21bfad0 (Pro 1.2.8, vóór het paneel van 1.2.9; zelfde export).
```
GB_MODUS=delen GB_RIJ=330 GB_PLAATRAND=20 GB_GAT=24 HB_LICHT=2.6 GB_SHIFT=-0.17 GB_SHIFT_Y=-0.03 GB_OP=0.95 GB_LENS=55 GB_AFSTAND=820 GB_ZIJ=-0.28 (zelfde regel, 32 samples)
python3 bron/tekst.py delen <uit>/render-delen.png <uit>/delen.json beelden <fonts> ../click-joints/bron/icoon.svg
```
Blinde test: set `organisatie/blindtest/sets/click-joints-pro-galerij-delen.json` (zelfde drie concurrenten als bereik).
