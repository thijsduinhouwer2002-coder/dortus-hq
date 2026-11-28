# Bewijs #369: waarom Hats "lagt" bij Thijs, en wat er veranderde (Olaf, 28 nov)

## Oorzaak
1. **Het spel tekende met opzet maar 10 beelden per s** (`kern/beeldtempo.gd`, sinds 13 nov). Maar de 3D-helden lopen sinds 25 nov op een klok van **12** stappen per s (`systemen/held_loop.gd` LOOP_FPS). 12 stappen over 10 beelden: elk vijfde beeld zet een held twee stappen in één keer. Een hikje, twee keer per seconde, bij elke lopende held. De eerste held loopt dubbel zo snel (24 per s): dan wisselen 2 en 3 stappen per beeld.
2. **Op 240 px is elke spelpixel 6 schermpixels.** Een stap is dan ±3 schermpixels en een dubbele stap ±6: dat zie je als schokken, ook op een snelle pc. Op 96 px is het een derde daarvan.
3. **Rekenwerk:** het script zelf kost ±1 tot 1,5 ms per beeld (GEZIEN, meting per `_draw` en `_process` in een kopie van het spel). Wat met de hoogte meegroeit is het tekenen. Op deze machine (Linux, software-tekenen op 2 kernen, venster 1920 breed) kostte 240 px **2,0 tot 2,2** CPU-s per 10 s en 96 px **0,99** (GEZIEN, `a240.log`, `a96.log` met de cijfers van het meetscript, losse runs). Op de pc van Thijs tekent de videokaart, dus daar is dit deel kleiner (GOK).
4. Geen echte haperingen: de langste tijd tussen twee beelden was 100 ms bij 10 per s en 83 tot 85 ms bij 12 per s, in elk blok van 10 s (GEZIEN, `langste_ms` in de logs). De "stilstand van 3,3 s" uit de film van Iris is een stuk waarin niets bewoog, geen vastloper.

## Wat er veranderde
- **12 beelden per s** (was 10), **24 tijdens een moment** (was 20). Een gewone held zet nu precies één stap per beeld.
- **Eerste start altijd 96 px**, de stand die Thijs koos (#372). Groter kan in het menu Height.
- **Lichte buitenrand om helden standaard uit** (Sanne #369; aan met `licht=1`).
- De meetregel met `log=` geeft nu ook `langste_ms` (langste beeldtijd) en `script_ms` (scripttijd per 10 s).

## Metingen (zaad 7, vers spel, 1920 breed, 60 s, Linux met Xvfb)
| run | stand | beelden per 10 s | langste beeld | CPU-s per 10 s |
|---|---|---|---|---|
| `a240.log` | oud: 240 px, 10 per s, licht aan | 100 | 100 ms | 2,02 (eerder 2,24) |
| `a96.log` | oud: 96 px, 10 per s | 100 | 100 ms | 0,99 (eerder 1,01) |
| `n240.log` | nieuw: 240 px, 12 per s, licht uit | 120 | 85 ms | 2,46 |
| `nstd.log` | **nieuw standaard: eerste start 96 px**, 12 per s, licht uit | 120 | 85 ms | 1,30 |

Alle cijfers GEZIEN, losse runs na elkaar op dezelfde machine (een los paar kan ±25% schelen, balans.md). Wat Thijs speelde (240, 10 per s) tegen wat hij nu krijgt (96, 12 per s): ±40% minder CPU. Het lichtje uit is in losse runs niet te zien (eerder gemeten op enkele tienden van een procent). De echte maat blijft het Taakbeheer-getal op de pc van Thijs.

**Gelijke stappen** (per held: hoeveel van zijn stappen dezelfde tussentijd en lengte hebben als zijn meest voorkomende, `gelijke_stappen.py` op `stappen-<n>-fps.txt`, 240 px, 60 s, GEZIEN): 10 per s **58%**, 12 per s **74%**, 24 per s 63%. De rest is vooral de aanloop vlak voor een val (3,5 keer zo snel, met opzet). Daarom 12 en niet hoger: 24 kost twee keer zoveel beelden en is minder gelijk, want 12 stappen over 24 beelden geeft bij elke kleine schommeling in beeldtijd 0, 1 of 2 stappen.

## Kijken
`eerste-start-96-links.png` en `-rechts.png`: eerste start met `dpi=120` (schaal 125%), op ware grootte. "Click the dirt to dig." en het goud (29) zijn op 1x leesbaar (GEZIEN).

Toetsen: alle 11 lokaal 0 FOUT (Godot 4.3 Linux), drie nieuwe regels in `toets_held.gd` (96 px, beeldtempo past op de loopklok, licht uit).
