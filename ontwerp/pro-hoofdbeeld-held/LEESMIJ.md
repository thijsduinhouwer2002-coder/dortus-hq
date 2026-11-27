# Hoofdbeeld Click Joints Pro met een gedetailleerd figuur (issue #285, Beeldmaker, 27 nov 2026)

Waarom: mens-r6 blijft bij de rechters op plek 2 achter Cleave, en elke ronde vragen ze "a detailed, high-quality action figure instead of a basic low-poly dummy" (GEZIEN, `organisatie/blindtest/uitslag/click-joints-pro-superhive-mens-r6-*.md`).

**Figuur:** Blender Human Base Meshes v1.4.1, `GEO-body_male_realistic` (CC0 1.0, bron en letterlijke licentiezin in `bron/LICENTIE-figuur.md`). Gebeeldhouwde anatomie (multires op niveau 2 vastgezet, 169.362 punten, gesloten mesh, één stuk; GEZIEN in het log). Geen kleren: elk deel krijgt een eigen kleur, zoals delen in verschillende kleuren filament (romp turquoise, kop crème, armen lila, dijen koraal, schenen blauw). Geen AI-beeld, geen foto van een print: alles is een render (Blender 5.3.0, Cycles, lokaal in de sessie van de Beeldmaker).

**Rig:** `bron/maak_held.py` zet er een eigen rig met Rigify-namen in, op plekken die uit de mesh gemeten worden (doorsneden per hoogte). Figure from rig leest alleen de botten. Gecontroleerd met een röntgenbeeld van de botten in het figuur (voor en zij).

**Gewrichten:** de echte knop Figure from rig van Pro (zip van main als 1.2.9, `PRO_VERSIE=1.2.9 bash e2e/maak_zip.sh betaald`): 6 gewrichten, ellebogen en knieën scharnier 0 tot 135°, heupen kogel ±20° (GEZIEN, `beelden/held-r1.json`, `gewrichten`). Overgeslagen door de add-on, eerlijk gemeld: beide schouders ("no room for a ball joint that can move here (it would be blocked)", de armen hangen in A-houding dicht tegen de romp) en de nek ("only a tiny ball fits here"). De rig heeft geen grenzen, dus 0 tot 135° is de standaard van de add-on ("preset").

**Beelden** (2400x1200, Superhive):
- `beelden/held-r1-2400x1200.jpg`: figuur uit elkaar, labels Hinge 0–135° (elleboog), Ball ±20° (heup), Hinge 0–135° (knie).
- `beelden/held-knie-r1-2400x1200.jpg`: hetzelfde met de knie-inzet zoals mens-r6 (camera langs de as van de rechterknie, onderbeen op de stop van 135°, gradenboog van de add-on 0° en 135°, tekst "Knee hinge, stops at 135°").

Opdracht (map `<fig>` met `held.blend`, `<f>` met Bricolage.ttf en Inter.ttf, OFL):
```
HELD_KLEUR=0 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-held/bron/maak_held.py -- human_base_meshes_bundle.blend <fig>/held.blend 2
K='{"romp": "6EC6C0", "kop": "EDE3D2", "bovenarm": "B9A3E3", "onderarm": "B9A3E3", "dij": "F08A7E", "scheen": "7FA8E8"}'
HB_KOGEL_MINST="Left hip,Right hip" HB_DEELKLEUR="$K" HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 30, "Right knee": 8}' \
HB_FIGUUR=<fig>/held.blend HB_UIT=18 HB_LICHT=2.6 HB_VUL=0.80 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.2 \
  blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <uit> 40 100
HB_DEELKLEUR="$K" HB_POSE='{... "Right knee": 135}' HB_FIGUUR=<fig>/held.blend HB_UIT=4 HB_KNIE_CAM="Right knee" HB_KNIE_KANT=1 HB_KNIE_AFSTAND=78 \
  HB_KNIE_SCHUIF=0,-3 HB_KNIE_LICHT=2.5 HB_KNIE_MAAT=1000 HB_KNIE_BOOG=1 HB_NAAM=knie <HB_* als hierboven> blender ... -- <pro-zip> <uit2> 48 100
TK_PUNT_DY='{"Left hip": -76}' TK_PUNT3="Fit test strip: 0.10 to 0.30 mm clearance" TK_GROOT=1.12 TK_BOVEN=0.08 \
  python3 ontwerp/pro-hoofdbeeld-robot/bron/tekst.py <uit>/hoofdbeeld-render.png <uit>/hoofdbeeld.json <t> <f> ontwerp/click-joints/bron/icoon.svg held-r3 labels
IZ_TEKST="Knee hinge, stops at 135°" IZ_BOOG=<uit2>/knie.json IZ_BOOG_DUN=1 IZ_BOOG_MIDDEN=500,425 IZ_BOOG_STRAAL=175 IZ_BOOG_DIK=10 IZ_BOOG_ALFA=0.9 \
  IZ_SCHADUW=0 IZ_X=1112 IZ_Y=690 IZ_M=380 IZ_SNEDE=0.47,0.42,0.56 python3 ontwerp/pro-hoofdbeeld-mens/bron/inzet.py <t>/held-r3-2400x1200.png <uit2>/knie-render.png <uit>/hoofdbeeld.json beelden/held-knie-r1-2400x1200.jpg <f>
```
Nieuw in de gedeelde scripts (alleen aan met hun eigen variabele, oude beelden veranderen niet): `HB_DEELKLEUR` en `HB_KOGEL_MINST` in `hoofdbeeld.py`, `TK_PUNT_DY` en de heup als derde label zonder schouder in `tekst.py`. `TK_PUNT_DY`: de heupkogel zelf heeft geen goud (alleen de kom in de dij), dus het punt van het label schuift 76 px omhoog naar de kogel (op het oog, GOK binnen ±10 px). Boogmidden van de inzet op het oog gemeten (GOK ±15 px); hoeken 0° en 135° zoals de add-on ze tekent.

**Blinde test:** set `organisatie/blindtest/sets/click-joints-pro-superhive-held.json`: held-knie, held en mens-r6 in dezelfde run tegen Cleave, CatPin en Split 3D Print. Klaar als: GESLAAGD met gemiddeld 1,5 of beter bij Gemini en beter dan mens-r6, plus Daans ja.

**Ronde 2 (27 nov ±18:00, Daan #290 M1):** `beelden/held-knie-r2-2400x1200.jpg` = held-r1 met een nieuwe knie-inzet. In r1 lag het goud van het scharnier in de schaduw (metaalglans die de donkere ruimte spiegelt) en keek de camera precies langs de as, dus je zag alleen het ronde eind van het bovenbeen. Nu: camera 35° om en 8° over de as (`HB_KNIE_SCHUIN=35,8`, nieuw in `hoofdbeeld.py`), goud zonder metaal (`HB_METAAL=0`, alleen in deze close-up), scheen donkerder (`HB_KNIE_DONKER=0.45`, nieuw), alleen bovenbeen en scheen in beeld (`HB_KNIE_STRAAL=12`), uitsnede zonder de lichte wig links. Je ziet het gouden scharnier met de pen en het blok waar het bovenbeen op de stop ligt (GEZIEN, ook op 480 px breed). Render lokaal (Blender 5.3.0, Cycles 48, zip van main als 1.2.9): `beelden/knie-r2-render.jpg`, `beelden/knie-r2.json`. Boogmidden op de pen, op het oog (GOK ±15 px); hoeken 0° en 135° zoals de add-on ze tekent, in perspectief van de schuine camera.
```
HB_DEELKLEUR="$K" HB_KOGEL_MINST="Left hip,Right hip" HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 30, "Right knee": 135}' HB_FIGUUR=<fig>/held.blend \
  HB_LICHT=2.6 HB_VUL=0.80 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.2 HB_UIT=4 HB_KNIE_CAM="Right knee" HB_KNIE_KANT=1 HB_KNIE_AFSTAND=58 HB_KNIE_SCHUIF=0,-4.3 \
  HB_KNIE_LICHT=2.5 HB_KNIE_MAAT=1000 HB_KNIE_BOOG=1 HB_NAAM=knie HB_METAAL=0 HB_KNIE_STRAAL=12 HB_KNIE_DONKER=0.45 HB_KNIE_SCHUIN=35,8 \
  blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <uit2> 48 100
IZ_TEKST="Knee hinge, stops at 135°" IZ_BOOG=<uit2>/knie.json IZ_BOOG_DUN=1 IZ_BOOG_MIDDEN=465,505 IZ_BOOG_STRAAL=150 IZ_BOOG_DIK=10 IZ_BOOG_ALFA=0.9 \
  IZ_SCHADUW=0 IZ_X=1112 IZ_Y=690 IZ_M=380 IZ_SNEDE=0.45,0.46,0.56 python3 ontwerp/pro-hoofdbeeld-mens/bron/inzet.py beelden/held-r1-2400x1200.jpg <uit2>/knie-render.png beelden/held-r1.json beelden/held-knie-r2-2400x1200.jpg <f>
```
Blinde test: set `organisatie/blindtest/sets/click-joints-pro-superhive-held-r2.json` (held-knie-r2, held-knie-r1, mens-r6).

**Ronde 3 (27 nov ±22:00, #320, Thijs 21:34: "het hoofdje nog los en in een ander kleurtje"):** `beelden/held-knie-r3-2400x1200.jpg` en `beelden/held-knie-r3-blendernation-1456x672.jpg` (zelfde beeld, verkleind en boven 20 px, onder 36 px bijgesneden; figuur heel in beeld).
- **Hoofd los door de echte knop.** In r1 en r2 sloeg Figure from rig de nek over ("only a tiny ball fits here (the bone sits near the skin)"). De oorzaak lag in ons eigen rig: het nekbot lag vlak achter de keel (y -0,034 m waar het midden van de hals rond -0,01 ligt, gemeten met doorsneden, GEZIEN). Met `HELD_HALS=-0.01,0.845 HELD_KIN=-0.045,0.875` (nieuw in `maak_held.py`, zonder die variabelen blijft het rig als in r1 en r2) loopt het nekbot door het midden van de hals. Dezelfde knop van Pro (zip van main als 1.2.9) maakt dan 7 gewrichten: ook Neck · Ball · ±20°, kogel 6,0 mm, Good fit (groen), hals 14,9 mm bij de snede (GEZIEN, `beelden/held-r3.json` en de proefrun). Niets met de hand losgemaakt. Schouders nog steeds overgeslagen (armen in A-houding tegen de romp).
- **Hoofd geel** (`F4D03F`, sleutel `kop_los` in `HB_DEELKLEUR`, nieuw in `hoofdbeeld.py`, alleen aan met die sleutel). Lila geprobeerd: onder het paarse licht leek dat op bleke huid. Het geel staat los van het oranje goud van de gewrichten (`FFB938`).
- Inzet, tekst, labels en camera als r2; de knie-inzet is dezelfde render (`beelden/knie-r2-render.jpg`).
```
HELD_HALS=-0.01,0.845 HELD_KIN=-0.045,0.875 HELD_KLEUR=0 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-held/bron/maak_held.py -- human_base_meshes_bundle.blend <fig>/held-r3.blend 2
K='{"romp": "6EC6C0", "kop_los": "F4D03F", "bovenarm": "B9A3E3", "onderarm": "B9A3E3", "dij": "F08A7E", "scheen": "7FA8E8"}'
HB_KOGEL_MINST="Left hip,Right hip" HB_DEELKLEUR="$K" HB_POSE='{"Left elbow": 55, "Right elbow": 25, "Left knee": 30, "Right knee": 8}' HB_FIGUUR=<fig>/held-r3.blend \
  HB_UIT=18 HB_LICHT=2.6 HB_VUL=0.80 HB_DRAAI=-22 HB_KANTEL=9 HB_SHIFT=-0.2 blender -b --factory-startup --python ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py -- <pro-zip> <uit> 40 100
TK_PUNT_DY='{"Left hip": -76}' TK_PUNT3="Fit test strip: 0.10 to 0.30 mm clearance" TK_GROOT=1.12 TK_BOVEN=0.08 python3 ontwerp/pro-hoofdbeeld-robot/bron/tekst.py <uit>/hoofdbeeld-render.png <uit>/hoofdbeeld.json <t> <f> ontwerp/click-joints/bron/icoon.svg held-r3 labels
IZ_* als ronde 2: inzet.py <t>/held-r3-2400x1200.png beelden/knie-r2-render.jpg <uit>/hoofdbeeld.json beelden/held-knie-r3-2400x1200.jpg <f>
```
Render lokaal: Blender 5.3.0, Cycles 40 samples, 210 s (GEZIEN). Blinde test: set `organisatie/blindtest/sets/click-joints-pro-superhive-held-r3.json` (r3 naast r2).
