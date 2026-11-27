# Reuzen: na minuut 25 elke 10 tot 13 min iets wat je nog niet zag (Sanne, 27 nov 2026, issue #291 punt 2)

Gat (Iris #286, leuk 7): "minuut 50 is dezelfde scène als minuut 25 met een grotere berg". Na minuut 25 kwam er niets nieuws, alleen meer van hetzelfde. Iris noemde zelf "nieuwe held, baas, kamer die opengaat".

**Keuze:** een reus bij hol-niveau 9, 10, 11 en 12. Waarom dit en geen kamer: het hol-niveau komt na minuut 20 al om de 8 tot 14 min (GEZIEN in de logs hieronder) en ontgrendelde tot nu niets (`systemen/hol_niveau.gd` zegt dat zelf). Een reus kan zonder nieuwe kunst (de bladen van ridder, dief, magier en bard, groter getekend), dus Mila blijft op de etalage (#30). Een kamer had nieuwe kunst nodig.

**Wat de speler ziet:**
| hol-niveau | reus | soort | binnen (bord) | vangst (bord) |
|---|---|---|---|---|
| 9 | Sir Hulk | ridder | Sir Hulk ducks in. He does not fit. | Sir Hulk fell. The hole shook. |
| 10 | Big Pip | dief | Big Pip tiptoes in. Loudly. | Big Pip fell. Big hole, big loot. |
| 11 | Grand Mage Oom | magier | Grand Mage Oom floats in. Huge. | Oom fell. His crown stays here. |
| 12 | Bard Colossus | bard | Bard Colossus brings a giant lute. | The Colossus fell. Encore! |

- Anderhalf keer zo groot als een gewone held, met de kroon; zijn kop komt tot in de bovenste gang ("he does not fit"). Loopt langzamer (0,6).
- De eerste val springt hij altijd over (ook bij koopgeluk), zodat je hem niet maar 4 s ziet: in de eerste versie viel hij steeds 4,4 s na binnenkomst (GEZIEN). Nu staat hij 30 s tot een paar minuten in beeld, of ontsnapt en komt later even groot terug.
- Vangst: 2 keer het goud en 6 muntjes extra in de regen.
- Eén keer per niveau per spel (in de save). Niet in de demo-film. Spelerstekst is concept (Engels) tot Thijs hem schrijft.

**Tempo, 60 min met de koper (GEZIEN, Godot 4.3 Linux headless, `--fixed-fps 10`, `vers=1 zaad=<z> uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=3600`), reus binnen in s:**
| zaad | niveau 9 | 10 | 11 | 12 | langste gat na minuut 25 zonder nieuwe reus |
|---|---|---|---|---|---|
| 7 | 1318 | 1834 | 2334 | 2976 | 10,7 min (2334 tot 2976) |
| 3 | 1278 | 1781 | 2295 | 2850 | 12,5 min (2850 tot einde) |
| 11 | 1379 | 1911 | 2474 | 3245 | 12,9 min (2474 tot 3245) |

Main kent na minuut 25 geen nieuw ding (alleen de berg en de kopen). Een ontsnapte reus komt er nog als terugkomer bij. Logs: `reus-zaad<z>-kort.log`, main ter vergelijking `main-zaad<z>-kort.log`.
- Let op: headless met vaste beelden loopt het hol sneller dan de film op ware maat. In de film van Iris-instellingen onder xvfb (`bewijs-robijn/nieuw-60min-zaad7-kort.log`) kwam hol-niveau 9 tot 12 op 24, 34, 43 en 57 min; met reuzen dan gaten van 9, 9 en 14 min (GOK, daar niet opnieuw gefilmd). Iris filmt bij haar keuring zelf 60 min op ware maat.
- Kopen blijven doorlopen tot minuut 53 tot 58 (stap 9 van de put in 1 van 3 zaden binnen het uur), dus het goud van de reus haalt de laatste koop niet naar voren (main zaad 7: laatste koop 3411 s).
- Headless geeft op main en met reuzen evenveel SCRIPT ERROR (±13.000, iets van headless zonder scherm); de film onder xvfb hieronder heeft er 0.

**Beeld (GEZIEN, xvfb 1920 x 1080, strook onderaan 120 px, `vers=1 zaad=5 uitleg_klik=6 balk=0 reus_proef=9`):**
- `reus-binnen-6-beelden-2x.png`: de ingang op 131, 134, 137, 140, 145 en 150 s: gewone held, Sir Hulk komt binnen, loopt, springt over de put met zweetdruppel, rent terug.
- `reus-binnen-1x.png`: de hele strook op ware maat, bord "Sir Hulk ducks in. He does not fit."
- `reus-binnen-40s.mp4`: 40 s film van de strook.
- Deze beelden zijn van vóór twee kleine wijzigingen (naam intern "Hulk" zodat de regels geen "Sir Sir Hulk" zeggen, en de eerste val altijd overspringen); hoe hij eruitziet is gelijk.

**Toetsen:** 11 x 0 FOUT (Linux). Nieuw in `toets_systemen.gd`: één keer per niveau, niet op 8, niet in de demo, kroon en schaal 1,5, regels passen in 42 tekens.

**Code:** `kern/reus.gd` (nieuw), aansluitingen in `kern/afloop.gd` (niveau erbij, buit, vangstregel), `kern/binnenkomst.gd` (reus gaat voor, schaal), `kern/strook.gd` en `kern/opslag.gd` (in de save), `systemen/held_val.gd` (eerste val overspringen), `kern/proef.gd` (`reus_proef=<9..12>` om te filmen).
