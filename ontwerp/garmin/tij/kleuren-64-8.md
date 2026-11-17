# Tij: kleuren op schermen met 64 en 8 kleuren (Mila, 17 nov)

Vraag van Daan en Gijs (17 nov): op 64 kleuren was Kelp neon groen en Dusk bloedrood, en het zeil viel weg tegen het water.
Blad: `mila-tij-kleuren-64-8.png` (Forerunner 255, 245 en 55 naast elkaar). Gemaakt door in de echte opnames van run 44015762562
alleen de kleuren te vervangen (`tij_kleuren_kleur.py`, `tij_kleuren_blad.py`); de vorm is dus precies wat het horloge tekent.
Het dunne rode randje onderaan de cirkel op de 245 is een rest van de oude opname (gladde rand van de simulator), geen kleur van ons.

## Keuze 64 kleuren (elk kanaal 00, 55, AA of FF)
| thema | band 0 (boven) | band 1 | band 2 | band 3 (onder) | waterlijn | zeil | minuten |
|---|---|---|---|---|---|---|---|
| Dusk | AA5555 | AA0055 | 550055 | 000055 | FFAAAA | FFFFFF | FFAA55 |
| Tide | 55AAAA | 0055AA | 0000AA | 000055 | AAFFFF | FFFFFF | 55FFFF |
| Kelp | AAAA55 | 55AA55 | 005555 | 000055 | FFFFAA | FFFFFF | AAFFAA |
| Night | 5555AA | 5500AA | 0000AA | 000055 | AAAAFF | FFFFFF | AAAAFF |

Waarom zo:
- **Gedempt boven, diep onder.** Elke bovenste band heeft één kanaal op AA en twee op 55 of minder: kleur, maar niet fel. Alle vier eindigen in hetzelfde nachtblauw 000055: de diepe zee is bij elk thema dezelfde, het thema zit in de bovenkant. Dat maakt de reeks herkenbaar als één familie.
- **Dusk** is nu een zee bij zonsondergang: roze, framboos, pruim, nachtblauw. Geen rood meer. **Kelp** is olijf, salie, zeegroen: wier, geen neon. **Night** paars en blauw met de gele maanboot erop.
- **Zeil altijd wit**: het lichtste vlak van het beeld en nooit een kleur uit het water. Het staat tegen de zwarte lucht, dus het springt eruit.
- **Waterlijn** is band 0 een stap lichter (zelfde formule als nu: plus 55 per kanaal), behalve waar dat wit zou worden; dan de lichte themakleur uit de tabel. Gijs mag de waterlijn dus als vaste kleur in de tabel zetten.
- **Minuten** op 64 kleuren: de lichte themakleur uit de tabel, want AAFF55 (Kelp) en FFAA55 met oranje water lazen samen als één neon vlek. Kelp krijgt munt AAFFAA.
- **Rand om het getal**: zwart op 64 en 8 kleuren.

## Keuze 8 kleuren (Forerunner 55 en andere met 8 kleuren)
Eén vaste zee voor alle thema's: band 0 en 1 cyaan 00FFFF, band 2 en 3 blauw 0000FF, waterlijn cyaan, zeil wit, minuten cyaan, dubbele punt cyaan, uren wit. Met 8 kleuren is er geen gedempte reeks te maken; rood en geel lazen als brand. Cyaan boven en blauw onder is gewoon water.

## Wat het zou veranderen
Een echte opname op de 245 of 255 waarop het nachtblauw 000055 onderaan wegvalt tegen de zwarte rand. Dan wordt band 3 per thema: Dusk 550055, Tide 0000AA, Kelp 005555, Night 0000AA (en schuiven de andere een stap op).

## Startpictogram (17 nov)
Bestanden `icoon/icoon-<px>.png` in 35, 36, 40, 54, 56, 60, 61, 62, 65 en 70 px, blad `mila-tij-icoon-blad.png` (6x en 1x), bron `tij_icoon.py`.
Wat erop staat: zwarte schijf, de stijgende zee van Tide in drie banden met de lichte waterlijn, en het witte bootje dat op de golf meevaart. Precies het verhaal van de plaat (je lijn stijgt, het bootje vaart mee), dus eerlijk. Elke maat is apart op de pixel getekend (geen schalen), alleen kleuren uit het palet van 64 (00AAFF, 0055AA, 000055, AAFFFF, wit), harde randen, de hoeken doorzichtig.
Besluit: geen zon of maan erbij (stond in een proef, GEZIEN), want die zit niet in het product. Zeil los van de romp met een zwarte spleet, anders werd het op 40 px één witte klont (GEZIEN).
