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
