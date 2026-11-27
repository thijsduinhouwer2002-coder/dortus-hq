# Robijnkoop zie je ook een minuut later (Olaf, 27 nov 2026, issue #298)

Gat (Iris #286 punt 1, build 43879de): stap 7 tot 9 maakten één gouden ruitje van ±5 px rood; troon, Gloop en luik bleven gelijk. Wie niet keek bij de koop, zag het daarna niet.

**Wat er veranderde voor de speler:** elke koop vanaf stap 7 zet grote geslepen robijnen neer, zo groot als Gloops kroon, met een zachte rode gloed.

| stap | Gloop (op de gouden troonrand) | put (op het dichte luik) |
|---|---|---|
| 7 | 2 robijnen op de hoekbollen boven | 1 grote robijn, luik roder |
| 8 | ook 2 op de armleuningen (4) | 2 robijnen, luik nog roder |
| 9 | ook 2 bij de voeten (6) | 3 robijnen, luik het roodst |

- Midden boven op de troon geprobeerd, maar daar staat de hoedentoren ervoor (in de eerste film van deze run zag je de robijn van stap 7 niet). Daarom links en rechts.
- De kleine rij stenen van stap 4 tot 9 (Sanne #280) blijft zoals hij was.
- Vormen in code (`systemen/robijn.gd`), geen nieuwe getekende kunst, geen AI. Eén keer per maat gebakken, daarna één plaatje per robijn. Geen beweging.
- Beelden (GEZIEN, xvfb 1920 x 120, `slijm_proef=<n> put_proef=<n> vers=1`): `stap6-tot-9-1x.png` (hele strook, stap 6 tot 9 onder elkaar) en `stap6-tot-9-put-en-gloop-2x.png` (put en Gloop 2x).

**Film van 60 min (GEZIEN, Godot 4.3 Linux onder xvfb, `--fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=3600`, eigen lege map):** 0 SCRIPT ERROR. Kopen na minuut 20 op 1190 (put 6), 1628 (Gloop 7), 1926 (put 7), 2270 (Gloop 8), 2619 (put 8), 3130 s (Gloop 9); put 9 op 3598 s valt buiten de film (`film-60min-zaad7-koper-kopen.log`). Tijdsprong putten en Gloop elke 10 s van minuut 19 tot 60: `putten-en-gloop-min19-tot-60-elke-10s-2x.mp4`. De volle film (2 GB) staat niet in de repo; pushen naar de tak `schermen` liep vast op de grootte van die tak.

**Blinde lezer (GEZIEN, een aparte agent zonder uitleg over robijnen):** per koop twee volle stroken op 1x, 60 s voor en 60 s na de koop, A en B door elkaar (`blind-sleutel.json`). Vraag: welk beeld is later, en wat kwam erbij en waar. Beelden: `robijnkopen-voor-na-1min-1x.png` (per robijnkoop voor boven, na onder).

| paar | koop | later goed? | ding goed genoemd? | zijn woorden |
|---|---|---|---|---|
| 1 | put 6 (gouden steen, oud) | ja | nee | "geen duidelijk blijvend verschil", laag |
| 2 | Gloop 7 | ja | ja | "twee grote rode robijnen bovenaan naast de troon", hoog |
| 3 | put 7 | ja | ja | "op beide putluiken een rode robijn", hoog |
| 4 | Gloop 8 | ja | ja | "een tweede paar robijnen bij de troon, lager", hoog |
| 5 | put 8 | ja | nee | noemde de robijnen bij de troon (die waren er al) |
| 6 | Gloop 9 | ja | ja | "robijnen onderaan links en rechts van het monster", middel |

Robijnkopen: 5 van 5 voor en na goed, 4 van 5 het gekochte ding goed aangewezen. Zwak: de tweede robijn op het luik (put 8). De gouden steen van put stap 6 (#162, niet van dit issue) ziet een lezer op 1x ook niet.

**CPU (GEZIEN, binnen één run, `wissel=stenen` tegen `wissel=nep`, stap 9, 600 s, `platformen/steam/data/cpu-duur/robijn/`, `cpu_stenen.py`):** stenen en robijnen aan tegen uit -4,6 procent (aan goedkoper), placebo -2,0 procent: niet meetbaar, binnen de ruis. Gemeten op de eerste indeling (1, 3, 5 robijnen op de troon); de verplaatsing naar 2, 4, 6 is één robijn meer bij stap 9. Een tweede meting op de nieuwe indeling ging mis (verkeerd proces gemeten, uitkomst onzin) en telt niet.

**Toetsen:** 11 x 0 FOUT (Linux, Godot 4.3). Nieuw in `toets_systemen.gd`: aantal robijnen per stap op troon (0, 2, 4, 6) en luik (0, 1, 2, 3), drie passen binnen het luik, luik roder per stap, plaatje rood met lege hoek.

**Code:** `systemen/robijn.gd` (nieuw), drie regels in `systemen/slijm.gd`, `hol/hol.gd` (luikkleur en plekken), `systemen/stap_stenen.gd` (tekent de robijnen op het luik in dezelfde laag).
