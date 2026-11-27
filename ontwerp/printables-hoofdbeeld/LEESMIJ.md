# Printables-hoofdbeeld van de gratis Click Joints (issue #297, Beeldmaker, 27 nov 2026)

Waarom: Thijs vond het huidige hoofdbeeld op Printables (de Extensions-banner) "een raar onduidelijk beeld". Het nieuwe beeld moet in één blik zeggen: met deze gratis Blender-add-on maak je kogelgewrichten in je eigen figuur. De vorige blinde test (`organisatie/blindtest/uitslag/click-joints-printables-addon-2026-11-27-1213.md`) vroeg in beide rondes "show a full character figure in the Blender viewport".

**Beeld r1:** `beelden/printables-r1-2000x1500.jpg` (4:3). Een figuur in twee kleuren: lijf paars, onderbenen geel, beide knieën met een kogelgewricht van de add-on, uit elkaar zodat je de kogel (aan het lijf) en de kom (in het onderbeen) ziet. Rechts een ronde inzet van één knie van dichtbij (aparte render van dezelfde scène), met een lijntje naar die knie. Eén regel tekst: "Ball joints in your own figure". Belangrijke dingen staan niet aan de randen (Printables snijdt de kaart bij).

**Figuur:** Blender Human Base Meshes v1.4.1, `GEO-body_male_stylized` met zijn twee ogen, CC0 1.0 (bron en licentiezin in `bron/LICENTIE-figuur.md`). 200 mm hoog. Geen AI-beeld, geen foto van een print: alles is een render (Blender 5.3.0, Cycles 64 samples, lokaal in de sessie van de Beeldmaker).

**Gewrichten:** de echte knop Place joint van de gratis add-on (`producten/blender-gewrichten/uitgave/click_joints_direct-0.1.2.zip`), Type Ball, Diameter Auto, as langs de 3D-cursor (langs het been naar beneden, cursor midden in de doorsnede 61 mm boven de vloer, maat voor 180 mm). Uitslag van de add-on zelf: beide knieën Good fit, kogel 5,5 mm (GEZIEN, `beelden/r1.json`, `cj_passing` groen, `cj_kogel_r` 2,75). Exploded view staat aan; alleen de afstand is voor het beeld groter gezet (2,2 keer de kogeldiameter), en het lijf staat omhoog in plaats van de onderbenen omlaag, zodat de voeten op de vloer blijven. Dat is alleen weergave; de STL heeft de echte plek.

**Eerlijk, wat ik aanpaste:**
- Normalen opnieuw naar buiten gezet (zoals Recalculate Outside); volume voor en na gelijk (GEZIEN in het log).
- Bij een snede in het been hield deel A (het lijf) 10 kleine losse stukjes van de tenen over; dezelfde tenen zitten ook heel in de onderbenen. Die stukjes (867 punten, onder 2% van het lijf) haalt het script weg vóór beeld en export. Gemeld aan Bram (eigenaar, issue #306), want een gebruiker met zo'n figuur krijgt ze ook.
- Kleuren: alle vlakken van een deel in één kleur (de passingring van de add-on niet), ogen donker.

**STL's voor Printables** (`stl/`, Export van de add-on in mm): `figure-body.stl` (97,8 x 32,2 x 138,7 mm, met de twee kogels en de ogen als losse bollen), `figure-lower-leg-1.stl` en `-2.stl` (17,7 x 31,0 x 70,8 mm, met de kom). In Blender zijn alle delen gesloten (0 open randen, GEZIEN). Na het inlezen van de STL tel ik 77 en 73 randen die niet precies twee vlakken hebben, door afronding in het STL-formaat (float32) bij hele kleine driehoeken; slicers herstellen dat gewoon (GOK, niet geprint). Zo voldoet het beeld aan de Printables-regel dat het toont wat je downloadt: het figuur uit het beeld staat erbij.

**Opdracht** (map `<f>` met `Bricolage-800.ttf` en `Inter-700.ttf`, OFL, uit npm `@fontsource/bricolage-grotesque` en `@fontsource/inter`, omgezet van woff2):
```
export PR_INZET=rechterknie PR_HOOGTE=200 PR_KANTEL=10 PR_AFSTAND=640 PR_DOEL=0,0,104 PR_SHIFT_X=0.17 PR_SHIFT_Y=0.02 PR_DRAAI=-28 \
  PR_KLEUR_ROMP=7D5BD6 PR_KLEUR_DEEL=F2B035 PR_IZ_AFSTAND=58 PR_IZ_KANTEL=30 PR_IZ_DRAAI=-20
blender -b --factory-startup --python ontwerp/printables-hoofdbeeld/bron/maak_beeld.py -- human_base_meshes_bundle.blend \
  producten/blender-gewrichten/uitgave/click_joints_direct-0.1.2.zip <uit> 64 100
OP_MAAT=66 python3 ontwerp/printables-hoofdbeeld/bron/opmaak.py <uit>/beeld.png <uit>/inzet.png <uit>/beeld.json beelden/printables-r1-2000x1500.jpg <f>
```

**Blinde test:** set `organisatie/blindtest/sets/click-joints-printables-figuur.json`: r1 en de huidige tijdelijke cover (kogelpaar) in dezelfde run, tegen TrailPrint3D, Snap-fit ball joint en Generic lockable ball joint (dezelfde drie als bij #257).

**Uitslag r1 (27 nov 19:05):** GESLAAGD, Gemini 1,0 (plek 1 in beide rondes); huidige cover kogelpaar 2,0 in dezelfde run (`organisatie/blindtest/uitslag/click-joints-printables-figuur-2026-11-27-1905.md`). Wens van Gemini in beide rondes: een stukje van het paneel van de add-on in beeld. Keuring #305 bij Daan.

## Ronde 2 (27 nov ±21:15 NL, Daan #305 M1, M2 en K1)
**Beeld r2:** `beelden/printables-r2-2000x1500.jpg` (4:3), zelfde scène en camera als r1.
- M1, geen facetten in de inzet: het figuur is vóór de snede één keer fijner gemaakt (Subdivision Surface niveau 1 vastgezet, 56.534 punten, `PR_SUBDIV=1`); dat is de invoer, zoals een gebruiker met een fijner figuur. De snede maakt daarna gewoon de add-on. Bij het renderen Shade Smooth by Angle 45 graden (`PR_HOEK=45`) en minder glans (`PR_RUW=0.6`, `PR_GLANS=0.05`), zodat platte vlakjes geen lichtvlekken meer geven.
- Kogel nu 4,5 mm vast in plaats van Auto (5,5): met het fijnere figuur liggen de knieën 19,0 mm uit elkaar (GEZIEN, `cj_centrum` in `beelden/r2.json`) en de add-on wil dan bij 5,5 mm minstens 20 mm ("Too close to another joint"). Bij 4,5 mm beide knieën Good fit (`cj_passing` groen, GEZIEN in `beelden/r2.json`).
- M2: tweede regel "Free Blender add-on" onder de kop.
- K1: ogen in de lijfkleur, mat (`PR_KLEUR_OOG=5A3FB0`, `PR_OOG_RUW=0.6`, `PR_OOG_GLANS=0`).
- STL's in `stl/` vervangen door die van r2 (zelfde figuur als het beeld): lijf 97,5 x 32,0 x 137,6 mm, onderbenen 17,7 x 30,7 x 71,3 mm (GEZIEN, gemeten uit de STL).
- Blinde test niet opnieuw: Daan zei in #305 dat dat na alleen M1 en M2 niet hoeft.

Opdracht r2: zoals r1, plus
```
export PR_SUBDIV=1 PR_HOEK=45 PR_RUW=0.6 PR_GLANS=0.05 PR_KLEUR_OOG=5A3FB0 PR_OOG_RUW=0.6 PR_OOG_GLANS=0 PR_IZ_AFSTAND=50 \
  PR_GEWRICHTEN='[{"naam": "rechterknie", "x0": 1, "x1": 30, "z": 61, "richting": "neer", "mm": 4.5}, {"naam": "linkerknie", "x0": -30, "x1": -1, "z": 61, "richting": "neer", "mm": 4.5}]'
OP_MAAT=66 OP_ONDER="Free Blender add-on" OP_MAAT2=44 python3 ontwerp/printables-hoofdbeeld/bron/opmaak.py <uit>/beeld.png <uit>/inzet.png <uit>/beeld.json beelden/printables-r2-2000x1500.jpg <f>
```
