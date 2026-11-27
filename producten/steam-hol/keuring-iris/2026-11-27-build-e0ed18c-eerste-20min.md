# Keuring Iris: main 8a2c2ff (spel gelijk aan e0ed18c), minuut 0 tot 20 als nieuwe speler (27 nov 2026 ±23:00 NL), issue #316

Bron: eigen film van main 8a2c2ff; de laatste wijziging aan het spel is e0ed18c (#298 robijnen in de troon). 1200 s, 1920 x 120 ware grootte, 5 beelden per s. Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=11 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200`, met een lege map voor opslag en instellingen (`HOME`, `XDG_DATA_HOME`, `XDG_CONFIG_HOME` leeg). Nieuw zaad 11, nooit eerder gefilmd. Wat ik zie is GEZIEN (film en log); de cijfers zijn mijn oordeel (GOK). De film zelf (700 MB) staat niet in de repo. Log zonder beestjes- en graafregels: `build-e0ed18c-20min-zaad11.log`. 0 SCRIPT ERROR.

Waarom: voor de itch.io-proef beslist een nieuwe speler in de eerste minuten. Minuut 20 tot 60 staat al op 8 (#301).

## Cijfers minuut 0 tot 20 (GOK)
| | cijfer | waarom |
|---|---|---|
| leuk | **8** | Binnen 25 s valt de eerste held in de put (+9) en eet Gloop er een (+9 x2, kroon blijft op zijn kop). Op 79 s de eerste koop, en Gloop is dan zichtbaar groter. Daarna elke 50 tot 141 s een koop met iets wat je ziet groeien (troon, luiken, hoeden op Gloop). |
| aandacht | **8** | 12 aankopen in 20 min, langste stuk zonder koop 141 s (807,8 tot 948,8 s). Het bord zegt steeds wat de volgende stap is ("Next: Deep Pit, 26 gold to go", "Deep Pit ready: click the pit"). Zwakste stuk: 0:27 tot 1:10 (zie hieronder). |
| mooi | **8** | Op 1x warm en vol zodra het hol gegraven is (vanaf minuut 6 de hele strook). Op 2x is de gegraven bovenkamer een vage vlek zonder vorm, en de linker helft is de eerste twee minuten lege aarde. |

## Per minuut: zou ik afhaken? (GEZIEN, film en log)
| minuut | wat er gebeurt | afhaken? |
|---|---|---|
| 0:00 tot 0:25 | Titel "Your taskbar has a basement.", held Geert valt in de put op 8 s (+9), "Click the dirt to dig." met kader (9 s), "Click the tunnel to set a trap." met pijl (15 s), Gloop eet Mara op 25 s, +9 x2 | nee, sterk begin |
| 0:27 tot 1:10 | Bord: "Next: Big Gloop, 2 gold to go" staat 43 s stil (27,4 tot 70,2 s). Tibbe vlucht, "First hero got away.", komt terug. Linker helft van de strook (±900 px) lege aarde | **zwakste stuk**: ik ben 2 goud van mijn eerste koop en er gebeurt niets wat dat goud brengt |
| 1:10 tot 1:22 | Ring om Gloop, "Click Gloop to grow him.", koop, Gloop groot | nee |
| 1:22 tot 3:10 | "Gloop is flat. Back soon.", rustig, held op Gloop, droogte op 145 s, tweede koop 186,8 s | twijfel kort, het bord blijft praten |
| 3 tot 6 | Hol graaft door naar links, kopen op 306, 403, 481, 531 s, Gloop krijgt troon | nee |
| 6 tot 12 | Hele strook gevuld, kopen elke 50 tot 105 s, "ready: click the pit" in geel | nee |
| 12 tot 20 | Kopen op 807, 948, 1086, 1170 s, gaten 141 en 138 s; hoedenberg naast Gloop groeit | nee, maar rustiger |

## Naast Rusty's Retirement (lat `organisatie/lat/hats.md`)
- **Rusty (GOK, uit hun winkelfilmpje en screenshots, niet zelf gespeeld):** de strook is vanaf seconde 1 vol: akkers, robot, planten. Je plant meteen met een klik en ziet het groeien; de eerste koop (een robot) komt in de eerste minuten.
- **Wij (GEZIEN):** sneller iets grappigs (val op 8 s, Gloop eet op 25 s, elke regel op het bord is een grap), en het bord geeft steeds één doel. Maar de eerste ±2 min is de linker helft van de strook lege aarde, en er is een stil stuk van 43 s vlak voor de eerste koop.
- **Gelijk of beter:** tempo van kopen in 20 min (12, langste gat 141 s), uitleg in het spel (Rusty ja, wij ja). **Achter:** een volle strook vanaf de start.

## Wat ontbreekt voor een 9 (geen nieuw issue, cijfers zijn 8)
1. **0:27 tot 1:10, 43 s op "2 gold to go".** De eerste koop hoort te komen zodra de les klaar is, niet na een stil stuk. Bijvoorbeeld de eerste held die terugkomt eerder, of Big Gloop 2 goud goedkoper. Beeld: `build-e0ed18c-min0-1-1x-b.png`, rij 2 tot 4 (28, 42, 62 s).
2. **Linker helft leeg in minuut 0 tot 2.** ±900 px lege aarde naast een vol hol rechts. Iets wat daar al leeft (een held die al aan komt lopen over het gras, een glinstering die je laat graven) vult de eerste indruk. Beeld: `build-e0ed18c-min0-1-1x-a.png`.
3. **Bovenkamer op 2x een vage vlek.** De gegraven kamer boven de gang is een wazig vlak zonder rand of vloer. Beeld: `build-e0ed18c-min0-1-2x.png`, rij 2 tot 4.

Beelden: `build-e0ed18c-min0-1-1x-a.png` (1, 3, 5, 9,6, 12, 16, 22 s), `build-e0ed18c-min0-1-1x-b.png` (25, 28, 42, 62, 71, 77, 83 s), `build-e0ed18c-min0-1-2x.png` (midden en rechts 2x op 9,6, 16, 25, 71 s), `build-e0ed18c-elke-2min-1x.png` (minuut 2, 4, ..., 20).

## Blinde test
Nieuwe set `hats-speelscherm-minuut0-e0ed18c`: het beeld op 25 s (Gloop eet Mara, +9 x2, half lege strook) op hetzelfde bureaublad als `b4d960c` (`scherm-zc-build-e0ed18c-minuut0-ware-maat.png`), tegen Rusty's Retirement, Spirit City en Desktop Defender. Zo zien we of de eerste indruk ook blind op plek 2 komt. De workflow draait bij de push.
