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
