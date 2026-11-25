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
