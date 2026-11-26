# Dichte put = luik van hout met een donkere rand (Mila, 26 nov ±19:40 NL, issue #209)

**Waarom:** Iris (keuring bb298d3 punt 1): van 800 tot 1200 s was een dichte put onzichtbaar, alleen een donker streepje en de gouden ruit. Je zag niet waar je val stond en wat je kocht. Bij Rusty's Retirement zie je alles wat je neerzette op 1x.

**Wat er voor de speler veranderde:**
- Op elke dichte put ligt een luik: honinghout (lichter dan de gangvloer), vier planken met staande voegen, een zwarte rand eromheen (de put eronder) en een ring vooraan. Op 120 px ±48 x 15 px (GEZIEN).
- Per stap van de put een eigen luik, zodat je ook ziet wat je kocht: gewoon (ijzeren banden), Rusty Spikes (roestige banden, drie roestige punten steken achter het luik uit), Deep Pit (dikkere zwarte rand, vier lange stalen punten), Trick Lid en hoger (aarde en een plukje gras erop, koperen scharnieren). De gouden ruiten van stap 4 tot 6 (#162) liggen op het luik.
- Klapt de put, dan is het luik weg en zie je de stekels zoals altijd; na 2 s ligt het luik er weer.
- Ook in het korte hol van de eerste minuut (`strook-0030s-...`).
- Het luik krijgt het licht van de gang op die plek, iets lichter, zodat het hout ook ver van de fakkel opvalt.

**Bron:** `modellen/luik.py` (Blender uit code, 4 beelden van 18 x 10 spelpixels op 4 px, blad `godot/kunst/luik.png`), tekenen in `godot/hol/luik.gd`, aangeroepen in `hol/hol.gd` (lus van de vallen); `hol/hol_3d.gd` zet in het vaste beeld de gewone gang onder een dichte put. Tekenvolgorde in `licht.gd` niet veranderd. Startargument `luik=0` geeft de oude put (voor de meting).

**Beelden (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200`; voor = zelfde build met `luik=0`):**
- `film-20min-elke-10s-1x.mp4`: de hele 20 min echt spel met koper, elke 10 s een beeld, ware grootte.
- `na-800-tot-1190s-elke-10s-1x.png`: 40 beelden rond de twee putten (x 880 tot 1180), ware grootte. In 37 zie je twee luiken; in 3 is één put net open na een klap (stekels), de andere een luik.
- `putten-30-300-600-900-1195s-voor-links-na-rechts-1x.png` en `-2x.png`: links voor, rechts na.
- `strook-0030s-...` en `strook-1195s-...`: hele strook, boven voor, onder na.
- `blad-luik-4-stappen.png`: het blad zelf.

**CPU (GEZIEN):** 9 paren runs om en om met en zonder luik (600 s spel, `--fixed-fps 5` zonder film, zelfde zaad, CPU-tijd van het proces): met luik gemiddeld 29,45 s, zonder 29,66 s (-0,7 procent; per run spreiding ±3 procent, dus het verschil is ruis; gemeten vóór de laatste kleurstap `OPLICHT`, één kleurmenging per put). Tekenbeurten: het luik zet geen eigen opnieuw-tekenen aan; het is één plaatje per put in een beeld dat hol.gd toch al tekent, en voor stap 1 en 2 komt het in de plaats van de putstekels.

**Toetsen:** alle 9 toetsen 0 FOUT op Linux; nieuw in `toets_systemen.gd`: luik staat aan, vaste beeld toont gang onder een dichte put, maat van het blad, elk beeld minstens 14 spelpixels breed.

## Nakeuring Daan #213 M1: Deep Pit zwaarder dan Rusty Spikes (Mila, 26 nov ±21:15 NL)

**Wat er voor de speler veranderde:** Deep Pit (de duurdere stap) leest nu meteen als de zwaarste put. Vier dikke stalen punten achter het luik, links licht staal en rechts een donkere kant, op 1x ±5 px breed onderaan en 6 tot 7 px hoog (GEZIEN, geteld in het blad op 1x; was 4 grijze stipjes van ±2 px). De zwarte rand is rondom ±2 spelpx dikker en hoger, met zwart ijzerbeslag en een lichte nagel op de hoeken, en de twee banden zijn licht staal in plaats van donker ijzer. Gewoon, Rusty en Trick Lid zijn niet veranderd.

**Bron:** `modellen/luik.py` (cel nu 18 x 12 spelpixels, onderkant op dezelfde plek, zodat de punten er niet meer boven afgesneden worden), `godot/hol/luik.gd` (CEL_H 12, MIDDEN_Y 34,5), toets in `toets_systemen.gd` meet de breedte op de rij van het luik.

**Beelden (GEZIEN, Godot 4.3 Linux onder xvfb, `--fixed-fps 1`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 balk=0 duur=40 put_proef=0..3`, beeld op 38 s):**
- `vier-stappen-in-spel-gewoon-rusty-deep-trick-1x.png` en `-3x.png`: dezelfde plek in het spel op 1x, van links naar rechts gewoon, Rusty Spikes, Deep Pit, Trick Lid.
- `blad-voor-daan213-4x.png` en `blad-na-daan213-4x.png`: het blad op 1x (3 px per spelpixel) en 4x uitvergroot, voor en na.

**CPU:** niets aan het tekenen veranderd: nog steeds één plaatje per dichte put, het blad is 288 x 48 in plaats van 288 x 40 (GEZIEN). **Toetsen:** alle 9 toetsen 0 FOUT op Linux (GEZIEN).

## #222: luik van Trick Lid blijft zichtbaar, geen rood blokje (Mila, 26 nov ±23:15 NL; Iris 5ecaf64 punt 3 en 4)

**Wat er voor de speler veranderde:**
- De gouden ruiten van stap 4 tot 6 liggen op de put nu kleiner (0,7 van de maat, ±8 schermpixels breed op 120) en onderaan op het luik, niet meer midden erop. Het hele hout met de aarde en het plukje gras van Trick Lid zie je weer; de ruiten bedekken alleen de onderste rand (GEZIEN, `222-stap3-tot-6-voor-boven-na-onder-1x.png` en `-2x.png`: stap 3, 4, 5, 6 van links naar rechts, boven voor, onder na). Bij Gloop blijven de ruiten op volle maat.
- Het rode blokje onder het rek met de kroon was het **vaandel** uit het deco-blad: in een vol hol (vanaf 20 gangtegels, hier vanaf ±200 s) hangt soms een vaandel aan het gangplafond. Om binnen de regel "hooguit 6 spelpixels onder het plafond" (Daan 16 nov) te passen kromp het tot 0,47, en half achter de plafondrand bleef op 1x alleen een rood vlakje van ±4 x 3 spelpixels over. Op die plek hangen nu wortels door het plafond (zelfde stuk als de wortels onder het gras): dun en licht, dus ook verkleind lees je wortels (GEZIEN, `222-1195s-voor-boven-na-onder-1x.png` en `-4x.png`, x 860 tot 1160, boven voor, onder na). In de schatkamer hangt het vaandel nog.

**Blinde lezer (GEZIEN, één lezer):** `222-blind-volgorde-abcd-2x.png`, de twee putten op stap 5, 3, 6, 4 (A, B, C, D). Een aparte agent die niets van dit werk wist, kreeg alleen dit beeld en "zet van minst naar meest verbeterd": **B, D, A, C, goed**, "de gele ruitjes nemen toe; het gras en de planken zijn bij alle vier gelijk".

**Beelden:** Godot 4.3 Linux onder xvfb. 1195 s: `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200` (zelfde args als Iris; de runs lopen niet precies gelijk, op 1195 s staan beide putten op stap 5). Stap 3 tot 6: `--fixed-fps 1`, zelfde args zonder koper, `duur=40 put_proef=3..6`, beeld op 38 s.

**CPU (GEZIEN):** 4 paren runs om en om, 1200 s spel, `--fixed-fps 5` zonder film, `put_proef=6` (drie ruiten op elke put), CPU-tijd user plus sys: voor 49,27 s, na 49,72 s gemiddeld, **+0,9 procent** (per paar +0,1, +0,8, +2,7, +0,1). De runs lopen uiteen (ander goud), dus dat is ruis; aan het tekenen veranderde niets: nog steeds één gebakken plaatje per rij ruiten (nu smaller) en één deco-stuk per plek.

**Code:** `godot/systemen/stap_teken.gd` (PUT_MAAT 0,7, maat in plek en plaatje), `godot/systemen/stap_stenen.gd` (maat per laag), `godot/hol/hol.gd` (PUT_STEEN_Y 38), `godot/hol/hol_vast.gd` (GANG_VAANDEL = wortels_a in het volle gangstuk; regels van vol_rij gelijk). **Toetsen:** alle 9 op Linux 0 FOUT, 3 nieuwe regels in `toets_systemen.gd`.
