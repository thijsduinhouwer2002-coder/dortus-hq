# Ebb bouw 9: keuring (12 nov, 01:30 NL)

Gekeurd: code 149491a6 (bouw 8-punten plus de eerste drie werelden v1.1 op het inhoudscherm), e2e 43121014228 en plaatjesrun 43121014130 groen, 46 van 46 toetsen, geen crash. Keurders op Opus: visueel, code en veiligheid, en voor het eerst een ideeënronde. Product niet opnieuw gekeurd (winkelkant nauwelijks veranderd; volgende ronde weer).

| Onderdeel | B7 | B8 | B9 |
|---|---|---|---|
| Code | 7 | 7,5 | 7,5 |
| Veiligheid en regels | 7,5 | 7,5 | 7,5 |
| Bouw visueel (bestaande schermen) | 7 | 7,5 | 7,5 (bijna 8) |
| Werelden zoals gebouwd | | | 6 |
| Product | 7,5 | 7,5 | niet gekeurd |
| Dieren in de app | 7 | 8 | 8 |
| Winkelbeelden | 6 tot 7 | 7,5 | niet gekeurd |

## Visueel
Opgelost en nagemeten: scène 19 en 20 (kop vrij: 10 px op 260, 18 px op 454), scène 18 (tijden 12 / 22 px boven de kamlijn), scène 37 (cyaan ring om Today).
**Voor een 8 op de bestaande schermen (Gijs):**
1. Scène 37: staart van de "y" in "Today" raakt de ring; 3 px ruimte rond de inkt of de punt ervoor weg.
2. Scène 19 op fenix 8: "B" van "Breathing pace" raakt de ronde kant van de pil; pil 12 px breder of tekst een maat kleiner.
**Werelden van 6 naar 8 (bouw v1.2 in plaats van v1.1):**
3. Clownvis (41): leest als oranje zigzag achter de roze vingers; vrij zetten met oog en witte banden, hoogstens 2 vingers over hem.
4. Anemoonarm (41): gele top 2 px onder het hartje van "61"; minstens 8 px onder de bpm-regel (top op y 186 of lager op 260).
5. Lucht boven de kam is zwart in plaats van nachtblauw 000055; kam op 260 maar 1 px (ontwerp: golvende schuimband 2 tot 5 px).
6. Drie rechte banden water dwars door "1:45" (vlag); één water, de wereld geeft de diepte. Wereld staat nu in de bijna zwarte band: zeegras dof.
7. Slipper (40) leest als roze vlieger: neem de teenslipper van v1.2. Grote platte grijze keien en het losse oranje vierkantje weg.
**Van 8 naar 9:**
8. Alle schermen nachtblauw met dezelfde golvende kam (nu voelt het als twee apps: inhoud vol water, rest zwart).
9. Drie lagen met lichtstralen, planten die zichtbaar meebuigen, maan, details per weekdoel; in de simulator tonen bij inademen en uitademen en in week 0 en week 4 (scènes).

## Code en veiligheid
Zie berichten/gijs.md, bericht 12 nov 01:20 (9 punten). Kern: werelden als gegevens in plaats van code, graphics pool meten en kleiner, plaatje opnieuw bouwen als het uit de pool valt, `los` aanroepen, watchdog-grens in punten, opzet voor planten in twee standen, toets dat de wereld op 0:30 en 2:30 gelijk is, toets Discard, Nagekeken bijwerken.

## Ideeënronde (besluit 12 nov 01:20)
Today als strand en 8 weeks als kustlijn (versie 1), aankomst en vertrek van het dier (versie 1), glance met slapend of wakker dier (na de werelden, anders 1.1).
