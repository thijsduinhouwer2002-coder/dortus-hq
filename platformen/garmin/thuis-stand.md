# Thuiswater: startscherm, pauze en sea log (Bas, stap 4)

**groen en gezien** (12 nov 2026, commit `a4f17d006` op tak `claude/garmin-thuis-proef-bas`)

Gijs: de tak kan samengevoegd worden. Lees eerst het kopje "Voor het samenvoegen".

## Wat gebouwd is

Startscherm (menu), pauzemenu en sea log hebben dezelfde rustige zee onder water in plaats van zwart:

- Water: op AMOLED het verloop van inhouden (20 stroken), op MIP bij dag het raster van inhouden over het hele scherm (geen grens die achter tekst loopt), bij nacht nachtblauw.
- Onderaan een zandbodem met een flauwe bolling. Op het menu staat je dier op het zand. Op pauze en sea log begint het zand 6/260 onder de laatste tekst, dus daar is het een smalle rand.
- Een pluk zeegras links en rechts en drie belletjes per scherm. Ze worden alleen getekend als ze 6/260 van elk tekstvak en 10/260 van de ronde rand blijven; past het gras niet, dan korter, anders weg. Daardoor staat het gras nu alleen op het menu met dier.
- Dag en nacht: elke kleur gaat via `EbbThuis.kleur` door de nachtregel (`EbbNacht.k`). Nacht is 21 tot 6 uur (`EbbLucht.deelNu`), net als in de sessie van Gijs. Bij nacht krijgt het dier op menu en pauze de nachtkleuren (`EbbDierPlaatje.NACHT`).
- Geen dier erbij, geen nieuw getekend voorwerp, geen hartje, geen kiezels, geen ruggen.
- Tekst, knoppen, tikken en navigatie zijn niet veranderd.

Kleine dingen die nodig waren voor de leesbaarheid op water:

- Menu: de rand van de niet gekozen pil is 00AAFF (0055AA viel weg tegen het water), de binnenkant van de pillen nachtblauw in plaats van zwart.
- Sea log: de telling ("8 of 24") is wit en de regel onder de naam en de lege bladstippen zijn lichtcyaan (00AAFF haalde op het raster geen 4,5 op 1). Het blad met de dieren is nu een doorzichtig plaatje zonder palet (zoals `DierPlaatje.mc`), zodat het water erachter te zien is.

Het is licht: een beurt van het thuiswater kost in de simulator 0 tot 1 ms op de FR255 en 5 tot 7 ms op de fenix 8. Er is geen groot plaatje; op MIP één strookje raster van 16 regels.

## Bestanden

Nieuw:
- `source/Thuis.mc` (200 regels): `EbbThuis.teken`, water, zand, gras, belletjes, nacht.
- `source/ThuisSchermen.mc` (56 regels): de tekstvakken van de sea log en de acht proefscènes.

Gewijzigd (de drie schermen):
- `source/Start.mc` (257), `source/Pauze.mc` (169), `source/SeaLog.mc` (271).

Gedeeld, een paar regels:
- `source/Scenes.mc`: vijf regels, een haak naar `EbbThuisSchermen.scene(k)` vlak voor `if (k >= 53)`.
- `source/Bouw.mc`: `SCENES` 77 naar 85 (de workflow rekent het toch zelf uit).
- `.github/workflows/garmin-adem-iq.yml`: `LAATSTE` plus 8, acht namen `thuis-*` erbij, en een tak met `thuis-proef` in de naam draait alleen die acht scènes en zet de beelden in `garmin-adem/plaatjes-thuis/` op tak `schermen` (zodat ik `plaatjes-proef` van Gijs niet overschrijf).
- `REGELS.md`: één regel in de kaart.

Niet aangeraakt: alle `KrabV2*.mc`, de sessie, de werelden. `KrabV2Thuis.mc` en de scènes 51 en 52 (de oude proef van het thuiswater) staan er nog; die kunnen weg als Gijs dat wil. `EbbZee.stil` wordt niet meer gebruikt.

## Uitslag van de runs (commit a4f17d006)

- Toetsen "Garmin Ebb (Connect IQ simulator)", run 43206672088: groen.
- Plaatjes "Garmin Ebb .iq (winkelbestand)", run 43206672091: groen op alle dertien horloges, geen crash, geen watchdog.
- De eerste commit (6915d5a62) was ook groen op de plaatjes (run 43205737780); de toetsrun daarvan is afgebroken door de tweede push.

Scènes (de laatste acht): `thuis-menu-dag`, `thuis-menu-nacht`, `thuis-pauze-dag`, `thuis-pauze-nacht`, `thuis-sealog-dag`, `thuis-sealog-nacht`, `thuis-menu-leeg-dag` (eerste start, nog geen dier), `thuis-sealog-alle-nacht` (zwaarste blad, alle dieren).

## Zelf gezien (met Read, FR255 en fenix 8 47 mm)

| Scherm | FR255 dag | FR255 nacht | fenix 8 dag | fenix 8 nacht |
|---|---|---|---|---|
| Menu met dier | ja | ja | ja | ja |
| Menu zonder dier | ja | niet gemaakt | ja | niet gemaakt |
| Pauze | ja | ja | ja | ja |
| Sea log (8 gevonden) | ja | ja | ja | ja |
| Sea log (alle dieren) | niet gemaakt | ja | niet gemaakt | ja |

Op alle beelden: tekst vrij, niets achter tekst, niets afgesneden door de rand behalve het zand, niets wat ik niet herken. De andere elf horloges zijn groen maar niet bekeken.

Beelden: `ontwerp/garmin/thuis-bas/` (menu, pauze en sea log bij dag en het menu bij nacht, FR255, twee keer vergroot). Alle beelden van de run: tak `schermen`, map `garmin-adem/plaatjes-thuis/namen/`.

## Voor het samenvoegen (Gijs)

- De tak is afgetakt van de bouwtak op 5c4f14697. Met de bouwtak van nu (958885cfb) voegt hij samen zonder botsing (geprobeerd met `git merge-tree`).
- Met de sessiescènes van proef62b botst hij wel, op drie plekken, omdat we allebei "de laatste acht scènes" gebruiken: `Scenes.mc` (`EbbBouw.SCENES - 8`), `Bouw.mc` (`SCENES`) en de workflow (`LAATSTE` en `NAMEN`). Oplossing: laat de mijne de laatste acht blijven en zet de jouwe ervoor: in jouw blok `ns = EbbBouw.SCENES - 16`, `LAATSTE` plus 16, en in `NAMEN` eerst de `sessie-*` namen en dan de `thuis-*` namen.
- Na het samenvoegen op de bouwtak draaien ook de oude scènes van deze schermen (start, menu-leeg, menu-krab, menu-today, pauze, sealog-1, sealog-2, sealog-3-alle25) op het thuiswater. Die heb ik niet apart gedraaid; mijn acht scènes dekken dezelfde schermen. Kijk ze één keer na.

## Open punten

- Bij nacht op MIP valt het vlak van een nog niet gevonden dier in de sea log samen met het water; je ziet alleen de blauwe omtrek. Leesbaar, maar het is een keuze.
- Op pauze en sea log is het zand maar een smalle rand, omdat de tekst tot onderaan loopt en er niets achter tekst mag.
- Tekstkleuren bij nacht zijn niet gedimd (Mila stelde dat in haar v1.1 voor); tekst gaat volgens de regel niet door de nachtregel.
- Op een echt horloge is het niet gezien, alleen in de simulator.
