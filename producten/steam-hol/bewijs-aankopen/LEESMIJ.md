# Elke aankoop in de eerste 15 min zie je terug in het hol (Mila, 25 nov ±18:15 NL, issue #76)

**Welke aankopen er in de eerste 15 min zijn (GEZIEN, 3 runs met een speler die koopt zodra het 8 s kan, zaad 2):** maar twee. Big Gloop (45 goud, gekocht op 197, 199 en 232 s) en Rusty Spikes (45 goud, op 394, 510 en 616 s). Bouncy Gloop (126) haalt niemand voor 905 s (log `HOL einde na 905 s ... goud=29`).

**Wat er voor de speler veranderde: Rusty Spikes leest nu als beter, niet als slechter.**
Vóór vandaag werd de put na de koop zwakker: dunne donkere staafjes tegen de roodbruine vloer, en het hoedje en het schedeltje (de grap) verdwenen. Op 120 px las dat als een stap terug (`put-stappen-oud-6x.png`, midden).
Nu (`put-stappen-nieuw-6x.png`, midden): dezelfde put als stap 0, maar 7 stekels voor in plaats van 5, ±15 procent hoger, onderste helft fel oranje roest, bovenste helft glimmend staal met een wit puntje, achter een rij helemaal roest. Hoedje en schedel blijven. Stap 0 en Deep Pit zijn niet veranderd.

**Twee beelden per aankoop, ware grootte (1920 x 120, echt spel, main + deze wijziging):**
- Big Gloop: `big-gloop-voor-221s.png` en `big-gloop-na-245s.png`. Gloop staat na de koop zichtbaar groter in de schatkamer (`big-gloop-voor-na-3x.png`). Was al zo; niets aan veranderd.
- Rusty Spikes: `rusty-spikes-voor-390s.png` en `rusty-spikes-na-400s.png`. Zilverwit wordt oranje roest, op 100% te zien zonder tekst (zelf gekeken, ook op 3x: `rusty-spikes-voor-na-3x.png`).
- Film van de koop: `rusty-spikes-koop-30s-ware-grootte.mp4` (380 tot 410 s, met geluid).

**Kunst:** `modellen/hol.py`, nieuwe tak `PUT_STAP == 1` (Blender, geen AI, geen gekocht pakket). Alleen het vak van `put_1` in `godot/kunst/3d/hol_proef.png` is vervangen (x 1408 tot 1479, de rest van het blad is bit voor bit gelijk); `bron` en `bytes` in `kunst/3d/sprites.json` staan op de nieuwe stand, zodat de workflow het hol niet onnodig opnieuw rendert. Eerst nagerekend dat mijn render van de oude put gelijk is aan het blad (gemiddeld verschil 0,006 op 255).
Draai: `HOL_VERBERG='["gloop","held","buit"]' ~/bpyenv/bin/python modellen/hol.py uit.png 1920 320 24 2 2 1` (bpy 5.2.4, ±60 s).

**Toetsen:** 7 x 0 FOUT op Linux.

**Eerlijk, voor Sanne (tempo):** twee aankopen in 15 min, met ruim 3 tot 7 min ertussen zonder iets te kopen. Beeld kan dat gat niet dichten; dat is balans. En voor Rusty Spikes staat nog wel een regel op het bord ("Rusty Spikes ready: click the pit", GEZIEN op 390 s), terwijl die voor Gloop weg is (#62). Het muntje boven de put zegt hetzelfde.

## Big Gloop krijgt een eigen gezicht (Mila, 25 nov ±19:40 NL, na de opmerking van de hoofdmanager 18:45: rijker, niet alleen anders)
Big Gloop werd alleen 25 procent groter. Nu ook: bredere mond met twee tanden en een slijmdruppel, en twee gouden munten half in zijn lijf (een schuin in zijn kop, een in zijn rechterflank). Past bij de winkelregel "Bigger mouth. More heroes fall." en zet goud op het groen (meer kleurverschil). Hoedentoren en kruin blijven gelijk (top per beeld 1,6, GEZIEN in `kunst/3d/sprites.json`).
- Ware grootte, echt spel (zaad 2, koper=1, koop op 198,6 s, GEZIEN in het log): `big-gloop-mond-voor-194s.png` en `big-gloop-mond-na-216s.png`.
- Naast Rusty's Retirement op dezelfde maat (220 x 120, uitsnede uit hun eerste Steam-schermbeeld): `big-gloop-voor-na-rusty-1x.png` en `-3x.png`. Eerlijk: Rusty's is nog veel voller van details per vierkante cm; dit dicht dat gat niet, het maakt de koop wel zichtbaar.
- Film van de koop: `big-gloop-koop-22s-ware-grootte.mp4` (192 tot 214 s).
- Kunst: `modellen/gloop.py`, standen met `_groot` erachter (rust, knipper, blij, hap, plat). Code: `slijm.gd` `beeld_groot()`, alleen het tekenen kiest het grote beeld; ontbreekt het, dan het gewone. Bron van hol_proef, deco en royal bijgewerkt (hun beeld verandert niet), zodat de workflow alleen het Gloop-blad heeft.
- Toetsen 7 x 0 FOUT op Linux (Godot 4.3).

## Rusty Spikes ronde 2: lichter (Mila, 25 nov ±19:50 NL, Daan #91 M1)
Daan: op 100% las de oranje roest als donker tegen de roodbruine vloer. Nu: bovenste 70 procent fel wit staal (lichter dan het bot van stap 0), stekels iets dikker, roest alleen een gele okerkraag onderaan, achterste rij licht staal met okerkraag. Hoedje en schedel blijven.
- 6x: `put-stappen-licht-6x.png` (stap 0, ronde 1, ronde 2 naast elkaar).
- Ware grootte, echt spel (zaad 2, koper=1, koop op 299,8 s, GEZIEN in het log): `rusty-spikes-licht-voor-296s.png`, `rusty-spikes-licht-na-306s.png`, uitsnede `rusty-spikes-licht-voor-na-1x.png` en `-3x.png`. Zelf gekeken op 100%: het oog gaat na de koop eerst naar de put (meer wit, hoger, goud onderaan).
- Film: `rusty-spikes-licht-koop-20s-ware-grootte.mp4` (290 tot 310 s).
- Alleen het vak van put_1 (x 1408 tot 1479) in `hol_proef.png` vervangen; methode nagerekend op de oude put (gemiddeld verschil 0,02 op 255). Toetsen 7 x 0 FOUT.

## Big Gloop ronde 3: echt groter (Mila, 25 nov ±21:30 NL, Iris #7 build d27cfc3: "Big Gloop leest nauwelijks als groter op ware maat")
Het lijf ging van 0,8 naar 1,0 (25 procent groter). Naast de groeiende hoedentoren viel dat op 120 px weg. Nu van 0,8 naar 1,2 (50 procent groter, zichtbaar lijf ±13 naar ±20 spelpixels breed, GEZIEN in het blad: 84 px op 5 px per spelpixel, keer 0,8 of 1,2). Het blad blijft hetzelfde (getekend op 5 px per spelpixel, dus ook op 1,2 nog verkleind en scherp, niet opgeschaald).
- Code: `godot/systemen/slijm.gd`, `K_KLEIN` 0,8 en `K_GROOT` 1,2 met `lijf_k()` op alle vijf plekken waar de maat stond (lijf, ring, Royal-cape, toren, tekenen). Alleen tekenen; vangen en lopen veranderen niet.
- Ware grootte, echt spel (zaad 2, koper=1, koop op 196,4 s, GEZIEN in het log): `big-gloop-12-voor-192s.png` en `big-gloop-12-na-214s.png`.
- Voor, oude na (1,0) en nieuwe na (1,2) naast elkaar: `big-gloop-12-voor-oud-nieuw-1x.png` en `-3x.png`. Zelf gekeken op 100%: na de koop is Gloop het grootste ding in de schatkamer, groter dan de goudstapel, en de toren staat op hem in plaats van andersom.
- 14 min (zaad 3, beelden op 560, 700 en 840 s, zelf gekeken op 3x): de hoedenberg links houdt lucht tot zijn flank, de toren blijft onder de bovenrand.
- Toetsen 7 x 0 FOUT (Godot 4.3 Linux). De Royal-toets rekent nu met `K_GROOT` (de cape groeit mee met het lijf).

## Bouncy Gloop en Deep Pit zichtbaar (Mila, 25 nov ±23:00 NL, Sanne 22:15: sinds 369bfca 4 aankopen in 15 min)
Zelf gekeken in een film van het echte spel (zaad 3, koper=1, koper_wacht=8, 1920 x 120): Bouncy Gloop gaf alleen een glansster van ±3 px naast de hoeden, op 100% niet te zien. Deep Pit werd zwakker dan Rusty Spikes: dunne grijze naaldjes op een zwarte strook, goud, hoed en schedel weg (zelfde fout als Rusty ronde 1).

**Bouncy Gloop: Gloop staat op twee gouden veren.** Nieuw beeld `veer` in het tekens-blad (`modellen/tekens.py` `_veer()`: schroefveer van 3 slagen goud draad tussen twee donkere plaatjes, met donkere rug). `slijm.gd` `veer_aan()`: vanaf Bouncy, niet plat, met het 3D-lijf, twee veren 6 spelpixels links en rechts van zijn midden en Gloop 3 spelpixels hoger (`VEER_TIL`, via `wip_nu()`, dus toren, muntje en hoeden gaan mee). De glansster gaat dan uit. Plat ligt hij gewoon op de vloer.
- Ware grootte (koop op 454,2 s, GEZIEN in het log): `bouncy-veer-voor-450s.png`, `bouncy-veer-na-460s.png`, uitsnede `bouncy-veer-voor-na-1x.png` en `-3x.png`. Film: `bouncy-veer-koop-20s-ware-grootte.mp4` (444 tot 464 s).
- Zelf gekeken op 100%: na de koop staat hij zichtbaar op twee gele veren boven de vloer, ook zonder te weten wat er gekocht is. Eerlijk: tussen de veren zie je zijn schaduw als donker vlakje mee omhoog.
- De andere 7 tekens zijn niet veranderd (gemiddeld verschil 0,004 op 255, maat `eenheid_px` gelijk 33,32).

**Deep Pit: de put van Rusty Spikes, een stap rijker.** `modellen/hol.py` nieuwe tak `PUT_STAP == 2`: 7 witte stalen stekels ±25 procent hoger dan Rusty, een glimmende gouden kraag in plaats van oker, achterste rij ook hoger met goud, twee houten palen met een gouden dop als lijst, twee hoeden op de stekels (de blauwe muts en een rode punthoed) en de schedel. Alleen het vak van put_2 (x 1480 tot 1551) in `hol_proef.png` vervangen; methode nagerekend op put_1 (gemiddeld verschil 0,07 op 255).
- 6x: `put-stappen-deep-6x.png` (stap 0, Rusty Spikes, oude Deep Pit, nieuwe Deep Pit).
- Ware grootte (koop op 567,8 s, GEZIEN in het log, film van vóór de veren): `deep-pit-voor-564s.png`, `deep-pit-na-575s.png`, uitsnede `deep-pit-voor-na-1x.png` en `-3x.png`. Film: `deep-pit-koop-20s-ware-grootte.mp4`.
- Zelf gekeken op 100%: na de koop zijn beide putten hoger, goudener en dragen ze twee hoedjes; het oog gaat er eerder heen dan naar Rusty Spikes.

**Big Gloop, controle van Daan (#102):** hoogste toren bij 1,2 (12 hoeden, 3 op zijn kop, 612 s): `big-gloop-12-hoogste-toren-612s.png`. De bovenste hoed raakt het gras, maar blijft 2 spelpixels onder de bovenrand (de plafondregel `PLAFOND` van Daan 14 nov); hij steekt er niet bovenuit.

**Toetsen:** 8 x 0 FOUT (Godot 4.3 Linux).
