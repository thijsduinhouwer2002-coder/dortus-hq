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
