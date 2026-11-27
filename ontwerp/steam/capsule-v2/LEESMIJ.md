# Steam-header v2 (Mila, 27 nov 2026, issue #30)

Bestanden: `header-920x430.png` (de header), `header-460x215.png` (klein, om te kijken), `rechts-2x.png` (Gloop en de vallende held op 2x), `voor-na.png` (v1 boven, v2 onder).

Maken: `<venv>/bin/python header_v2.py r.png 1840 860 28` (bpy 5.2.4, ±2,5 min op 2 kernen), dan `python3 samenstellen.py r.png header-920x430.png`. Render op 2x en verkleind: scherp zonder opschalen.

## Het idee (keuzes van Sanne in #30)
- Bovenaan een rustig bureaublad (lucht, wolken, heuvels), onderaan een taakbalk met het icoon van Hats; daartussen het hol als kelder, in de look van het speelscherm dat blind won. Ondertitel als concept: "Your taskbar has a basement now" (Thijs schrijft de echte tekst voor live).
- Grote figuur: Gloop met zijn hoedentoren (helm, kroon, heksenhoed) op het goud, in een kamer van licht metselwerk.
- De grap: een held valt kop eerst door een gat in het gras de kamer in, zijn rode pet vliegt los in de lucht. In de gang loopt de volgende ridder nietsvermoedend naar de kamer.
- Feller en warmer dan v1, minder muur: lucht blauw, gras fel groen, aarde terracotta, kamer zandsteen, Gloop mint, held paars, ridder blauw.

## Eigen toets (GEZIEN met Read, op 920, 460 en 2x)
- Titel en ondertitel lezen op 460. Gloop, pet en vallende held lezen op 460; de laarzen omhoog zie je op 2x goed.
- Frisse kijker (een losse Claude, blind tussen de drie concurrenten op 460, ronde v4): plek 3 van 4, na Spirit City en Rusty, vóór Desktop Defender. Letterlijk: "The taskbar hook is the only image that says 'lives on your desktop', but the scene is cramped and busy at this size." Tip: figuren groter, minder losse dingetjes, ondertitel groter. Daarna gedaan: Gloop ±10% en de held ±15% groter, de helft minder kiezels, ondertitel 25 naar 29. Dit is geen blinde test volgens regel 9.
- Blinde test `organisatie/blindtest/sets/hats-header-v2.json`: run 45914452636 gaf geen uitslag, de ChatGPT-sleutel heeft geen tegoed (HTTP 429, GEZIEN in het log). Opnieuw starten zodra er tegoed is (skill `actions`, set `hats-header-v2`).

## Ronde 3 (27 nov ±03:00 NL, na keuring Daan #236: nee, 6 van 10)
- **M1 vallende held:** niet meer kop eerst (het omgekeerde gezicht las als een los ei), maar voeten eerst met armen omhoog van schrik, iets schuin, gezicht rechtop. Eén silhouet; hij zakt net uit het gat. Valstreepjes erboven getekend in Pillow (in Blender lazen ze als stokjes).
- **M2 gat in het gras:** breder en donker van binnen, met overhangende sprieten aan de randen en kluitjes die meevallen (licht op de donkere schacht, donker op het metselwerk).
- **M3 bureaublad:** taakbalk van 30 naar 40 px, knoppen groter, Hats-knop groter en opgelicht als open app, startknop met vier vakjes, en een witte muispijl in de lucht.
- **Kan:** gang hoger en ridder groter (minder lege aarde links midden, bot weg), Gloop één mond (losse tand weg), zachter sleutellicht (vlak 10 naar 18).
- Na een frisse kijker (een losse Claude, blind op 460, telt niet als test: plek 3 van 4, tip "logo groter, minder rommel"): titel ±22% groter, HATS nu ±38% van de breedte.
- Bekeken met Read op 920, 460 en 2x (`rechts-2x.png`). Voor en na: `voor-na.png` (v2 boven, v3 onder).
- Blinde test: set `hats-header-v2.json` wijst nu naar v3. ChatGPT had om 01:19 nog geen tegoed (run 45921830896, HTTP 429, GEZIEN), dus een uitslag komt pas als er weer tegoed is.

## Ronde 4 (27 nov ±05:30 NL, kan-punten 1 en 2 van Daan #243)
- **Gat:** geen zwart vak meer maar een rafelige trechter (golvende wanden, bovenaan rond uitlopend, geen rechte hoeken). Langs beide wanden lichte kluiten aarde, drie wortels hangen van boven het donker in, en de verre rand is gras met sprieten die naar binnen hangen. De donkere achterkant loopt onderaan mee met de boog van de kamer.
- **Valstreepjes:** drie in plaats van vier, elk een andere lengte (30, 18, 12 px), dunner, spits naar boven en iets schuin mee met de val.
- De rest van het beeld is gelijk aan v3 (eigen dobbelsteen voor het gat, zodat kiezels en sprieten niet verschuiven).
- Bekeken met Read op 920, 460 en 2x. Voor en na van het gat: `voor-na.png` (v3 links, v4 rechts).
- Set `hats-header-v2.json` wijst nu naar v4 (`?v=4`); de push start de test vanzelf. Geen tegoed bij de rechters = geen uitslag, dan opnieuw starten zodra er tegoed is.

## Ronde 5 (27 nov ±07:15 NL, eigen kijken terwijl de blinde test op tegoed wacht)
- **Pet:** de rode pet in de lucht las op 460 als rode lippen (wit band als tanden, koepel van opzij). Nu koepel boven, witte band als rand en de klep steekt rechts opzij (`PETK` 15, `PETD` -30): op 920 en 460 een pet, op 2x ook. Gekozen uit zes standen die ik los renderde.
- Rest gelijk aan v4. Voor en na van de pet: `voor-na.png` (v4 links, v5 rechts). Bekeken met Read op 920, 460 en 2x.
- Set `hats-header-v2.json` wijst nu naar v5 (`?v=5`).

## Blinde test v5 (27 nov 10:50 NL): NIET GESLAAGD, Gemini gemiddeld plek 3,0
Uitslag: `organisatie/blindtest/uitslag/hats-header-v2-2026-11-27-1050.md` (GEZIEN). Beide rondes plek 3 van 4 (eerste keus Spirit City en Rusty). Gemini letterlijk: "The concept of a taskbar basement is clever and clearly displayed, but the 3D graphic style looks a bit cheap and mobile-esque." Beter maken: "Refine the lighting and 3D asset quality to give the game a more premium aesthetic." Het idee werkt dus (de taakbalk leest), de afwerking niet.

Proef in dezelfde run (`proef-v6-licht.jpg`, boven v5, midden en onder twee proeven), alles als schakelaar in de scripts, standaard uit, zodat v5 gelijk blijft:
- `HV2_AGX=1` (AgX met Punchy): alles valt flets en grijs uit, titel crème. Niet doen.
- `HV2_LIJN=1` (warme inktlijn om Gloop, helden, pet en hoeden) en `HV2_MAT=1` (matter, minder glans): iets meer getekend, maar op 920 nauwelijks verschil.
- `GLOED=1` in `samenstellen.py` (gloed om fel licht, warme toon, vignet): maakt het waziger, de titel verliest zijn rand. Niet doen in deze vorm.
- Mijn oordeel (GEZIEN met Read op 920): geen van de proeven is duidelijk beter dan v5, dus geen nieuwe testronde op de gratis daglimiet.

Wat de volgende stap moet zijn: niet nog meer poetsen aan licht, maar de stijl zelf. De drie concurrenten zijn getekend (Rusty pixels, Spirit City en Desktop Defender vlak getekend met harde schaduwvlakken). Plan v6: toon-schaduw (twee of drie vlakke tinten per materiaal in plaats van glad plastic), een dikke inktlijn op 2x om de figuren, en minder glimmende hoogtelichten; eerst één losse proef op Gloop alleen, dan pas het hele beeld.

## Ronde 6 (27 nov ±13:30 NL): getekende stijl in plaats van glad plastic
Na Gemini ("3D looks a bit cheap and mobile-esque") de stijl zelf veranderd, niet het licht. Schakelaar `HV2_TOON=1` in `header_v2.py` (standaard uit, v5 blijft te maken):
- Elk materiaal is nu lichtkant plus vlakke schaduwkant: een harde Toon-schaduw (Cycles Toon BSDF) op de basiskleur en een vaste, iets koelere en paarsere schaduwtint, zoals een getekend spel met twee tinten per vlak.
- Smalle warme randlijn langs de buitenkant van de figuren (Gloop, helden, hoeden, pet), niet op muur en aarde.
- Inktlijn om de figuren (`HV2_LIJN=1`, dikte 3,4 op 2x). Kleine harde glimvlek alleen op goud en kroon.
- Eén harde zon als licht (vul-, sleutel- en titellamp uit), dus duidelijke schaduwen; de titel ook getekend, feller geel.
- Maken: `HV2_TOON=1 HV2_LIJN=1 HV2_TZON=4.2 HV2_LIJNDIK=3.4 HV2_SCHADUW=0.5 HV2_STR=0.85 HV2_STG=0.72 <venv>/bin/python header_v2.py r.png 1840 860 28`, dan `python3 samenstellen.py r.png header-v6-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v6-2x.png`). Voor en na: `voor-na.png` (v5 boven, v6 onder).
- Mijn oordeel (GOK tot de blinde test): meer getekend en de titel leest beter; de helmen lezen als witte kommen, minder metaal.
- Blinde test: set `hats-header-v2.json` heeft nu v5 en v6 als twee kandidaten, zodat de rechter zegt welke beter is.
