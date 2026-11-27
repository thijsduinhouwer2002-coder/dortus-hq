# Hoedenberg groeit zichtbaar van minuut 25 tot 60 (Olaf, 27 nov 2026, issue #282)

Iris (#279 punt 2, deel van #280): er vallen in minuut 25 tot 60 ±54 hoeden op de toren, maar de berg naast Gloop bleef bijna even groot (6 naar 9 zichtbaar). Wie wegkijkt en terugkijkt ziet geen verschil.

**Wat er veranderde voor de speler:** de grenzen waarop de berg een maat groter wordt zijn 25 / 45 / 65 / 90 hoeden (was 25 / 100 / 300 / 1000), breder pas bij 1000 (was 3000). Tot 25 hoeden is alles gelijk (minuut 0 tot ±20 blijft zoals Iris het een 8 gaf). Daarna komt er elke 4 tot 5 hoeden een plekje bij, tot een volle berg van 21 bij 90 hoeden. Geen nieuwe kunst, geen nieuwe code in het tekenen; alleen `BERG_MAAT` in `godot/systemen/slijm.gd`. De vaste plekjes, de linkergrens (put, ingang, gaten) en de boog naar de berg werken zoals ze gekeurd zijn.

**Bewijs (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=3600`, zelfde instellingen als Iris):**
- `oud-min25-35-45-55-60-2x.png` (main) tegen `nieuw-min25-35-45-55-60-2x.png`: oud blijft de berg een rij van 3 tot 4 breed en 2 hoog; nieuw groeit hij van 7 naar 17 zichtbare hoeden tot een piramide van 5 hoog.
- Zichtbaar op de berg (uit de hoedentelling in `nieuw-60min-zaad7.log`): 7 op minuut 25 (34 hoeden), 17 op minuut 60 (74 hoeden). 10 keer groter na minuut 25; langste gat tussen twee keer groter 294 s (main: 3 keer, langste gat 873 s). Daartussen landt elke nieuwe hoed bovenop (langste gat zonder nieuwe hoed 150 s).
- `gloop-min20-tot-60-elke-10s.mp4`: minuut 20 tot 60, één beeld per 10 s, ware grootte.
- 0 SCRIPT ERROR in 60 min.

**Blinde lezers (GEZIEN, elk een aparte lezer, 5 uitsneden van 300 x 120 op ware grootte door elkaar, sleutel in `blind-*/sleutel.txt`):**
- Nieuw: B, E, C, D, A = minuut 35, 25, 45, 55, 60. Alleen de eerste twee omgedraaid; "C heb ik op de grootte van de stapel geplaatst", zeker: middel.
- Oud (main): E, C, D, A, B = minuut 25, 45, 55, 60, 35. "De rij hoeden onderaan verandert nauwelijks", zeker: laag.
- Eerlijk: de "Klaar als" (vijf op volgorde goed) is net niet gehaald; minuut 25 en 35 liggen op 1x nog dicht bij elkaar (7 tegen ±9). Minuut 35 tot 60 leest hij wel goed op grootte.

**CPU (GEZIEN, binnen één run, Linux xvfb, `zaad=5 koper=1 hoeden_proef=84`, 12 min, twee runs tegelijk):** `wissel=berg` tekent de berg in oneven blokken van 20 s met hooguit 9 hoeden (zoals vroeger), `wissel=nep` is de placebo. Alle seconden: echt -3,2 procent, placebo -1,7 (fout van het gemiddelde ±3,9); met held in beeld: echt -3,7, placebo -2,9. Geen meetbare extra kost, ruim binnen +2. Of die run echt 21 plekjes kreeg hangt af van de linkergrens in dat hol (GOK: minstens 15). Script `platformen/steam/data/cpu-duur/cpu_stenen.py` (leest nu ook `wissel berg`), ruwe meting en startscript in `platformen/steam/data/cpu-duur/berg/`.

**Toetsen:** 11 x 0 FOUT (Linux). In `toets_held.gd` de getallen bij de nieuwe grenzen (44 -> 9, 70 -> 16, 99 -> 21; maat 5 bij 100, maat 6 bij 1000) en "niet hoger" telt nu de rij, niet de soort hoed.

**Code:** `systemen/slijm.gd` (`BERG_MAAT`, en `wissel=berg` alleen met het startargument), `kern/proef.gd` (`hoeden_proef=<n>`: Gloop begint met n hoeden, alleen meten). `slijm.gd` is 1626 regels; splitsen is issue #283.
