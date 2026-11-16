# Click Joints Pro 1.1 "Rig to Figure": ontwerp (Ruben, 16 nov 2026)

**Waarom wij (Daan, 16 nov):** de enige die je rig leest en er een printbare figuur van maakt waarvan elk gewricht stopt waar je rig stopt.

Concurrentiecheck en plan: `platformen/blender-2/rig-to-figure.md` (uitkomst ja). Daan zei ja op plan en volgorde (`berichten/ruben.md`, 16 nov ±11:20).

## Wat het doet
1. **Figuurpresets zonder rig (stap 1, gebouwd).** Een eigen paneel "Figure joints" onder Click Joints met zes vaste knoppen, elk met een klein icoon van het lichaamsdeel: Shoulder, Hip, Neck (kogel), Elbow, Knee (scharnier met eindstop op 135°), Ankle (scharnier op 90°). Je zet de 3D-cursor zoals altijd en klikt het lichaamsdeel. Het snijden doen de bestaande operators (kogel uit de kern, scharnier van Pro 1.0), dus vorm, pasband, eindstop, één lid snijden en alle oude toetsen blijven gelijk. Onder de knoppen een lijst van de figuur: bovenaan "2 joints", daarna per gewricht één regel `Knee · Hinge · 0–135° · preset`. Het getal is altijd het gemeten bereik (beweegproef van het scharnier, `cj_bereik_graden`, of de ±graden van de kogel), nooit de stand, zodat we nooit meer graden tonen dan er zijn.
2. **Figure from rig (stap 2).** Armature en mesh kiezen, één knop. Standaard alleen schouders, ellebogen, heupen, knieën en nek als die er is; de rest via "More bones". Per bot: snijvlak bij de botkop, lidas langs het bot, scharnieras uit de botrol (X-as van het bot), preset op naam (Mixamo, Rigify, Meshy-rig), en het bereik uit Limit Rotation als dat er staat (label `from rig`), anders het preset (label `preset`). Namen in gewone woorden (Left knee, Right shoulder). Samenvatting bovenaan: "6 joints, 4 ranges from your rig". Daarvoor moet het scharnier een vrij gekozen eindstop krijgen in plaats van alleen 90/115/135 (de wigformule a = (N − s/r)/2 is al doorlopend; toetsen per getal nodig).
3. **De figuur in één beeld met zijn bereiken.** Na "Figure from rig" staat bij elk gewricht de gradenboog van Pro 1.0, klein, met het getal. Dat is het eerste winkelbeeld (links de figuur in rig-houding, rechts printklaar met de waaiers, alleen echte uitkomst).

## Wat het bewust niet doet
Geen automatische knippunten zonder rig of cursor (dat doet Cleave), geen gewichten of skinning, geen pose naar print in één vast beeldje (Pose to Print), geen eigen server. Geen twintig botten om aan te vinken.

## Hoe het aansluit
Alleen in de betaalde build (`click_joints/betaald/figuur.py`, iconen in `betaald/iconen/`). De gratis zip verandert niet (toets `toets_zips.py`). Elk deel bewaart `cj_gewrichten` (JSON-lijst met naam, soort, graden, herkomst, snijpunt) en `cj_figuur` (vaste naam van de figuur, want `cj_bron` wisselt bij elke snede); zo kent de lijst alle gewrichten van de figuur, ook na meerdere sneden. Stap 2 schrijft dezelfde records met herkomst `from rig`.

## Wanneer is het af (toetsbaar, echte Blender 4.2, 5.2 en 5.3 op Actions)
Stap 1 (`e2e/toetsen_figuur.py`, plaatje `e2e/scherm_figuur.py`):
- zes vaste namen in deze volgorde, zes iconen geladen (met venster een icon_id);
- Knee: scharnier stand 135, twee gesloten delen, record Knee/HINGE/preset, getal gelijk aan de beweegproef (120 tot 136);
- Shoulder op het andere deel: kogel, beide delen kennen Knee en Shoulder, lijst van de figuur in volgorde, "2 joints";
- Elbow op de plek van de knie: geweigerd, lijst blijft 2; open mesh: geweigerd, geen record;
- plaatje 15: het paneel met knoppen, iconen en lijst.
Stap 2 en 3: eisen volgen bij de bouw van stap 2 (Rigify-figuur, Mixamo-figuur, de vier Meshy-figuren; per gewricht draait het deel tot de eindstop en niet verder).

## Stand
- **16 nov (Ruben, run 3):** stap 1 gebouwd op tak `claude/blender-2026-11-16-figuur`. Lokaal in de echte Blender 5.3.0: `toetsen_figuur.py` 0 fout, `test_betaald.py` 0 fout, plaatje 15 gemaakt. Beeld voor Daan: `proeven/1.1/15-figuur-paneel.png` (uitsnede zijbalk) en `proeven/1.1/15-figuur-x.png` (hele venster). Nog alleen `preset`; een beeld met `from rig` komt bij stap 2.
- **16 nov (Ruben, run 3, vervolg):** stap 2a gebouwd: het scharnier neemt een vrije eindstop `graden` (30 tot 150, verborgen eigenschap van `click_joints.plaats_scharnier`, 0 = de knoppen 90/115/135). De wigformule was al doorlopend, dus alleen de invoer veranderde. Toets `e2e/toetsen_vrije_stop.py`: bij 30, 45, 60, 75, 90, 100, 120, 135 en 150 twee gesloten delen, stop uit de wig binnen 0,1 graad, gemeten bereik N − 0,04 tot N; 20 en 170 geweigerd. Lokaal 0 fout in Blender 4.2.23 en 5.3.0. Eerlijk: of een scharnier van 30° of 150° goed klikt na het printen is nog niet geprint; de toets meet alleen de vorm.
