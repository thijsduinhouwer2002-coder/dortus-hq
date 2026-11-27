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
