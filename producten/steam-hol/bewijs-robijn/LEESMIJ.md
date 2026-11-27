# Na stap 6 nog iets te kopen: robijnen (Sanne, 27 nov 2026, issue #280 deel 1)

Gat (Iris #279, leuk en aandacht 6 na minuut 25): de laatste koop was rond minuut 20 tot 25 (stap 6 van Gloop en de put). Daarna 35 minuten niets te kopen; het goud liep op tot ±1500 en betekende niets meer.

**Wat er veranderde voor de speler:** Gloop en de put hebben elk drie stappen meer.

| stap | Gloop | put | kost (put +10) | doet | zie je |
|---|---|---|---|---|---|
| 7 | Ruby Gloop | Ruby Spikes | 300 | +2 goud per vangst | 1 van de 3 gouden stenen wordt een robijn |
| 8 | Rubier Gloop | Ruby Pit | 400 | +2 goud per vangst | 2 robijnen |
| 9 | Ruby Rex | Ruby Doom | 500 | +2 goud per vangst | 3 robijnen, daarna "All bought." |

- Zelfde ruit, zelfde plek, alleen de kleur (rood met donkere rand en licht glimvlak), van links naar rechts. De rij blijft even breed, dus niets schuift op het luik of voor Gloop. Geen nieuwe getekende kunst, geen AI: vormen in code.
- Elke stap heeft drie kroniekregels met een grap (concept, Engels, tot Thijs de spelerstekst schrijft), bijvoorbeeld "Gloop found a ruby. Heroes pay more." en "Long live Ruby Rex. Burp."
- Undo en opslaan werken zoals bij stap 1 tot 6 (save tot niveau 9).

**Prijzen gekozen met de echte koper (GEZIEN, Godot 4.3 Linux, `zaad=<z> uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=3600`, kooptijden in s):**
- 150, 200, 250: alles op rond minuut 38 (laatste koop 2290 s), daarna weer 22 min niets. Elke koop geeft meer goud en een koopgeluk-vangst, dus het goud versnelt.
- 250, 350, 450: laatste koop 3315 s (zaad 7) en 3122 s (zaad 3), headless.
- **300, 400, 500 (gekozen):** headless zaad 7: 1591, 1880, 2241, 2600, 3033, 3447; zaad 3: 1530, 1798, 2249, 2578, 2966, 3327.

**Film van 60 min op ware maat onder xvfb (GEZIEN, zaad 7, koper, zelfde instellingen als Iris), `nieuw-60min-zaad7-kort.log`:**
- Kopen na stap 6 (1190 s): 1531, 1876, 2301, 2615, 3109 s. Langste stuk zonder koop 493 s (8,2 min), elke 10 min iets te kopen. Stap 9 van de put (510) is op minuut 60 bijna binnen (499 goud).
- Main ter vergelijking (`main-60min-zaad7-kopen.log`): laatste koop 1221 s, op minuut 60 1571 goud zonder doel.
- Dingen die je op 1x ziet veranderen na minuut 25 (koop, hol-niveau linksboven, berg een hoed groter): langste gat 220 s (3,7 min), daarna 195 en 176 s. De berg-telling is berekend uit de hoedentelling in de log met `berg_zichtbaar` uit `slijm.gd`, ervan uitgaand dat er 21 plekjes passen (GOK voor dit hol; Olaf zag in zijn film 17 op minuut 60). Zonder de berg zijn de koop en het hol-niveau samen nooit verder dan 8,2 min uit elkaar.
- 0 SCRIPT ERROR in 60 min.

**Beelden (GEZIEN, xvfb 1920 x 120, `zaad=5 koper=1 duur=200 slijm_proef=<n> put_proef=<n>`, laatste beeld):**
- `stap6-tot-9-1x.png`: vier volle stroken, stap 6, 7, 8, 9 (bord: "Next: Ruby Gloop, 190 gold to go").
- `stap6-tot-9-uitsnede-2x.png`: de twee putten en Gloop, 2x vergroot: 3 goud, 1, 2, 3 rood.

**Toetsen:** 11 x 0 FOUT (Linux). Nieuw in `toets_systemen.gd`: prijzen en goud van stap 7 tot 9, alles gekocht na 9, robijnen per stap, linker steen rood in het plaatje; kapotte save tot 9; kroniekregels voor stap 4 tot 9 (12).

**Code:** `systemen/upgrades.gd` (MAX_NIVEAU 9, prijzen, namen, regels), `systemen/stap_teken.gd` (`rood()`, robijnkleur in het gebakken plaatje), `systemen/stap_stenen.gd`, één regel in `systemen/slijm.gd` en `hol/hol.gd`, `kern/proef.gd` (proef tot stap 9).

**Na minuut 60:** alles gekocht rond minuut 60 tot 65. Wat goud daarna doet is een volgende stap (`inhoud-100.md`, Hat Closet of Second Vault), niet in dit issue.
