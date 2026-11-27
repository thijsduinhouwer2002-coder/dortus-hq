# Robijnen v2: gezet in het goud, put past (Olaf, 27 nov 2026, #298 na Daan #307)

Daan #307 (nee 7): op de troon lazen de robijnen als stickers (in de lucht naast de troon, groter dan Gloops oog, harde vorm, geen schaduw); op de put raakten ze elkaar en zag je het rodere luik bijna niet.

**Wat er veranderde voor de speler:**
- **Troon (M1):** elke robijn is nu een ronde, heldere robijn in een gouden kastje met een klein schaduwtje eronder, óp het goud van de troon en binnen zijn omtrek. Stap 7 op de gouden hoekbollen, stap 8 op de gouden knoppen onder de kussens, stap 9 op de troonpoten (niet meer in de lucht naast de voeten). Kastje ±15 schermpixels op 120; Gloops kroon (ring met steen) is ±13 tot 16 (GEZIEN, ingezoomd op het beeld). Was ±25.
- **Put (M2):** robijnen 3,9 in plaats van 5 spelpixels breed, met 1,6 ertussen: drie naast elkaar raken elkaar niet en steken niet meer boven het luik uit. Het luik wordt per stap duidelijk roder: honing (6), oranjerood (7), rood (8), diep robijn (9).
- **Kan K1:** donkere rand zachter (wijnrood in plaats van bijna zwart). K2 (glinstering) niet gedaan.
- Een rode gloed op de aarde rond het luik geprobeerd; weggelaten omdat het luik zelf al genoeg verschilt en een grote gloed op deze xvfb (softwarematig tekenen) vlak kost.

**Beelden (GEZIEN, xvfb 1920 x 120, `slijm_proef=<n> put_proef=<n> vers=1`):** `stap6-tot-9-put-en-gloop-2x.png` (dezelfde strook als v1, put links, Gloop rechts, stap 6 tot 9 onder elkaar) en `stap6-tot-9-1x.png` (hele strook).

**Blinde lezers (GEZIEN, aparte agents, volle strook op 1x, voor en na door elkaar, niet ingezoomd):**
| proef | put | Gloop |
|---|---|---|
| put en Gloop samen veranderd (stap 6/7, 7/8, 8/9), 3 rondes met elk een nieuwe lezer | 3 van 3 goed in elke ronde (1 keer stap 6/7 met twijfel door een wisselende hoed) | niet genoemd: de lezer zag alleen de put |
| alleen Gloop veranderd (`blind-gloop-paar*-1x.png`, sleutel `blind-sleutel-gloop.json`) | | 3 van 3 goed op volgorde en het ding goed genoemd ("rode edelstenen op de hoeken van de troon", "steentjes langs de zijkanten"); stap 7 middel tot hoog zeker, stap 8 en 9 laag |

Eerlijk: kleiner en in het goud leest de troon minder snel dan v1 (toen ±25 px, los naast de troon). Stap 7 valt op; 8 en 9 zie je pas als je goed kijkt. Een dieper robijnrood kussen per stap (alleen de rode pixels van het troonbeeld) heb ik ook geprobeerd: een lezer zag dat niet, dus eruit. Gloop-proef gemaakt met de gloed rond de troonrobijn op 1,25 keer de maat; daarna terug naar 1,05 (CPU), het kastje is gelijk.

**CPU (GEZIEN, binnen één run, `wissel=stenen` tegen `wissel=nep`, stap 9, 640 s, xvfb, `platformen/steam/data/cpu-duur/robijn-v2/`, `cpu_stenen.py`):** stenen en robijnen aan tegen uit +0,5 procent, placebo -0,8 procent: binnen de ruis. Een eerdere meting mét de rode gloed rond het luik gaf +11 procent tegen placebo -5,6 (weinig blokken, afgebroken); daarom is die gloed eruit.

**Toetsen (GEZIEN):** 11 x 0 FOUT (Linux, Godot 4.3). Nieuw in `toets_systemen.gd`: robijnen op het luik raken elkaar niet, luik per stap duidelijk roder, troonrobijn rond in een gouden kastje en niet groter dan 5 (maat in de troontabel).
