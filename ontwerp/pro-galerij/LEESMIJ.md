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
Ronde 1 (25 nov 21:06): NIET GESLAAGD, Gemini 3,0 en ChatGPT 1,0 (`organisatie/blindtest/uitslag/click-joints-pro-galerij-delen-2026-11-25-2106.md`). Beide prijzen export per deel en 0,20 mm; beide vragen hetzelfde: laat het zien op een organisch, gedetailleerd personage in plaats van de blokkige robot. Volgende ronde: zelfde opzet met het MakeHuman-figuur (CC0, `commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md`, `FL.laad_figuur("mens")`).

Ronde 2 (#101, 25 nov ±23:55): `delen-mens-*`, zelfde beeld met een organisch figuur: MakeHuman base mesh (CC0 1.0, `commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md`), aangekleed door `figuur_laden.laad_mens_kleding`. Figure from rig van Pro (zip van main) maakte 9 gewrichten en 10 delen; Export schreef 10 STL en 10 3MF (GEZIEN, `beelden/delen-mens.json`). Gelegd als een lichaam uit elkaar: achter dij, bovenarm, romp, bovenarm, dij; voor scheen, onderarm, hoofd, onderarm, scheen (`GB_LEG=lichaam`; welk deel wat is volgt uit de rusthouding).
```
HB_FIGUUR=mens GB_LEG=lichaam GB_MODUS=delen GB_PLAATRAND=18 GB_GAT=20 HB_LICHT=2.6 GB_SHIFT=-0.20 GB_SHIFT_Y=0 GB_OP=0.6 GB_LENS=55 GB_AFSTAND=740 GB_ZIJ=-0.28 (zelfde regel, 32 samples)
python3 bron/tekst.py delen <uit>/render-delen.png <uit>/delen.json <uit> <fonts> ../click-joints/bron/icoon.svg   (daarna hernoemd naar delen-mens-*)
```

Ronde 3 (#101, keuring #113, 26 nov ±01:30): `delen-mens-*` opnieuw met de twee moet-punten van Daan. M1: ronde hals in plaats van de vierkante huidkleurige lap (`CJ_HALS=rond` in `commercie/filmpjes/studio/figuur_laden.py`; zonder die variabele blijft alles zoals het was). M2: camera iets verder (`GB_AFSTAND=850`), zodat de hele plaat in beeld staat, ook op 1920x1080; het kniekaartje staat nu bij het losse onderbeen links (Daans kan-punt) en raakt geen hand. Zelfde compositie, dus geen nieuwe blinde test (Daan, #113).
```
CJ_HALS=rond HB_FIGUUR=mens GB_LEG=lichaam GB_MODUS=delen GB_PLAATRAND=18 GB_GAT=20 HB_LICHT=2.6 GB_SHIFT=-0.20 GB_SHIFT_Y=0 GB_OP=0.6 GB_LENS=55 GB_AFSTAND=850 GB_ZIJ=-0.28 (zelfde regel, 32 samples)
GB_KNIE="Right knee" GB_KNIE_D=-40,-230 python3 bron/tekst.py delen <uit>/render-delen.png <uit>/delen.json <uit> <fonts> ../click-joints/bron/icoon.svg   (daarna hernoemd naar delen-mens-*)
```
Fonts: Bricolage Grotesque en Inter (OFL) uit github.com/google/fonts.

## Strip v3 (issue #205, 26 nov ±18:00): `strip-v3-*`, beide proefsets
Waarom: bij strip v2 zeiden beide rechters elke ronde "lijkt alleen voor kogels" (Gemini 2,0, ChatGPT 2,0, Cleave wint). Pro heeft twee knoppen, Fit test: ball en Fit test: hinge; v3 toont beide, gemaakt door de echte knoppen (zip Pro 1.2.8 in de workflow), plus het kaartje met het MakeHuman-figuur (CC0) uit release pro-videobeeld-1 in plaats van de robot. Kleur, plaats (scharnierset naast de kogelset, `GB_NAAST=40`) en camera zijn van ons; spelingen 0.10 tot 0.30 mm uit `beelden/strip-v3.json` (GEZIEN).
Render: workflow `.github/workflows/pro-galerij-strip3.yml` (drie varianten; gekozen `naast`, de rij-variant was rommelig), release `pro-galerij-strip-3`.
```
GB_INZET=<render-klik.png uit pro-videobeeld-1> GB_INZET_KADER=0.775,0.09,1.0,0.92 python3 bron/tekst.py strip3 render-naast.png naast.json <uit> <fonts> ../click-joints/bron/icoon.svg
```
Fonts: als er statische bestanden `Inter-<gewicht>.ttf` en `Bricolage-<gewicht>.ttf` in de fontmap staan, neemt tekst.py die (Inter uit het systeem, Bricolage Grotesque OFL uit npm @expo-google-fonts/bricolage-grotesque).
Blinde test: set `organisatie/blindtest/sets/click-joints-pro-galerij-strip-v3.json` (v3 en v2 tegen Cleave, CatPin, Split 3D Print).
Ronde 2 (26 nov ±19:00, Daan #207 punt pillen): tekst.py meet de spelingpillen vooraf en kiest de grootste letter (24 tot 19) met minstens 10 px lucht tussen buren; zelfde render, alleen de pillen anders. Set `click-joints-pro-galerij-strip-v3-r2.json`.
Ronde 3 (26 nov ±20:45, Daan #207 M1 en M2, plus kan-punt kaartje): ondertitel "Five gaps, 0.10 to 0.30 mm, for balls and hinges. Keep the one that turns without wobble.", eerste pil "gap 0.10 mm" (zodat 0.30 mm niet als maat van de bal leest), en onder de vijf scharnieren hun speling (0.10 tot 0.30, uit `labels2` in de json; `GB_LABELS2=0` zet ze uit). Kaartje ruimer uitgesneden (`GB_INZET_KADER=0.755,0.09,1.0,0.92`) zodat de linkerhand niet meer afgesneden is. Zelfde render; de rafelige oranje rand bovenop de kogelstukken is de render zelf en bleef. Set `click-joints-pro-galerij-strip-v3-r3.json`.

## Strip v4 (issue #219, 26 nov ±21:00): `strip-v4-*`, strakke goudrand
Daan #215 kan-punt: de oranje rand bovenop de kogelstaven was rafelig (zaagtand), want galerij.py kleurde per driehoek op hoogte en de schuine draairuimte rond de nek viel half binnen, half buiten. Nu (`GB_STRAKKE_RAND=1`, alleen kogelstaven): alles in de bovenhelft goud behalve de buitenwand (opzij gericht en op de volle straal). Zelfde camera, zelfde geometrie (json gelijk aan v3, GEZIEN), zelfde tekst en kaartje (`GB_INZET_KADER=0.755,0.09,1.0,0.92`). Render: workflow `pro-galerij-strip3.yml` ronde 3 (run 45886830491), release `pro-galerij-strip-4`. Lokaal nagemaakt v3 uit strip-3 gaf exact hetzelfde beeld als op main (verschil 0), dus de tekstlaag is gelijk. Blinde test: set `click-joints-pro-galerij-strip-v4.json` (v4 en v3).

## Beeld "From your rig in one click" (`beelden/paneel-rig-*`, 27 nov ±10:15, issue #259)
Waarom: Pro had geen galerijbeeld van het paneel; Cleave en Split 3D Print tonen hun automatische knop als eerste (lat, kop Paneel). Dit beeld toont ons sterkste punt uit 1.2.9: heeft je mesh een rig, dan staat "Rig found" met Figure from rig bovenaan. Hoort bij 1.2.9 (uitbrengen ma 30 nov), niet eerder plakken.

**Schermafbeeldingen:** echte Blender 5.3.0 met interface (Xvfb 2880x1620, schaal 1.5), Pro-zip van main (`e2e/maak_zip.sh betaald`, PRO_VERSIE 1.2.9), de MakeHuman-figuur met Mixamo-rig uit de e2e (`proef_mens.py`, base.obj van github.com/makehumancommunity/makehuman, CC0 1.0, als tekenpop zoals plaatje 19). `beelden/paneel-rig-scherm-voor.jpg`: figuur met zijn botten in beeld, paneel "Rig found: mixamo_rig", Figure from rig, More bones. `beelden/paneel-rig-scherm-na.jpg`: na één druk op die echte knop, rechterknie gebogen met de eigen Bend-schuif (60). Uitslag van de add-on in `beelden/paneel-rig.json` (GEZIEN): 9 joints, 2 rig, 2 mirror, 5 preset; ellebogen 0 tot 140°, knieën 0 tot 120° (uit Limit Rotation van de rig), heupen, schouders en nek kogel ±20°. Het vergrote paneel en het kaartje zijn pixel voor pixel uit die twee schermafbeeldingen; niets nagetekend. Geen AI-beeld, geen foto van een print.
```
cd producten/blender-gewrichten
PR_AFSTAND=390 PR_MIDX=10 PR_MIDZ=108 CJ_MENS_OBJ=<base.obj> xvfb-run -a -s "-screen 0 2880x1620x24" \
  <blender 5.3.0> --factory-startup --gpu-backend opengl --python ../../ontwerp/pro-galerij/bron/paneel_rig.py -- <uit> /tmp/click_joints_betaald.zip
cd ../../ontwerp/pro-galerij
PR_SY0=80 PR_VERGROOT=1.45 PR_PY=330 PR_KH=500 PR_KX=420 python3 bron/tekst_paneel_rig.py <uit>/rig-voor.png <uit>/rig-na.png <uit>/paneel-rig.json beelden <fonts> ../click-joints/bron/icoon.svg
```
Fonts: Bricolage Grotesque en Inter (OFL), variabele bestanden uit github.com/google/fonts.
Blinde test: set `organisatie/blindtest/sets/click-joints-pro-galerij-paneel-rig.json`, tegen de paneelbeelden van Cleave (robot), CatPin (figuur, galerijbeeld 8) en Split 3D Print.

**Ronde 2 (27 nov ±11:00, Daan #260):** bol op Figure from rig is nu "2" (stap 2 links), het kleine echte paneel heeft een dunne grijze lijn in plaats van geel (alleen de vergroting is geel), bovenrand 20 px hoger bijgesneden (PR_SY0=80). Schermafbeeldingen opnieuw gemaakt met dezelfde opdracht; paneel-rig.json is gelijk aan ronde 1 (GEZIEN). Set `click-joints-pro-galerij-paneel-rig-r2.json`.
