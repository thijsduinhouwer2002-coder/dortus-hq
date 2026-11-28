# Keuring Iris: main e70eab3 (strook 200 px, #333), minuut 0 tot 20 als nieuwe speler (28 nov 2026 ±03:00 NL), issue #334

Bron: twee eigen films van main (spel gelijk aan e70eab3), 1200 s elk, 1920 x 200 ware grootte (schaal 5), 5 beelden per s. Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=200 vers=1 zaad=12 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=1200`, één keer `palet=vol` en één keer `palet=zacht`, lege map voor opslag en instellingen. Nieuw zaad 12. Wat ik zie is GEZIEN (film en log); de cijfers zijn mijn oordeel (GOK). Films (±780 MB elk) niet in de repo. Log zonder beestjes- en graafregels: `build-e70eab3-200-vol-zaad12.log`. 0 SCRIPT ERROR in beide.

Waarom: Olaf maakte de strook hoger (#333). Doel van #334: mooi minstens 8, leuk niet lager dan 8.

## Cijfers minuut 0 tot 20 (GOK)
| | cijfer | was (e0ed18c, 120 px) | waarom |
|---|---|---|---|
| leuk | **8** | 8 | Zelfde spel: val op 8 s (+9), Gloop eet Pim op 25 s (+9 x2), eerste koop op 75 s. Op 200 px zie je het lachen: Gloop met kroon, de held die wegvlucht, het zweetdruppeltje van Tibbe bij de schat lees je zonder te turen. |
| aandacht | **8** | 8 | Vol: 12 kopen, langste gat 136 s (75,0 tot 210,8 s). Zacht (andere loop door het toeval): 11 kopen, langste gat 139 s (889,8 tot 1028,8 s). Zwakste stuk blijft 27,8 tot 66 s: geen goud, "Next: Big Gloop, 2 gold to go" vanaf ±57 s. |
| mooi | **8** | 8 | Duidelijk beter dan 120: Gloop, troon, helden, luiken en bord zijn groot en scherp, het bord leest als hout van het hol. Maar door schaal 5 vallen de grove vlakken nu meer op (zie punt 1), en dat houdt het onder een 9. |

Doel #334 gehaald: mooi 8, leuk 8.

## Vol of zacht (voor de keuze van Sanne)
Op 1x zie ik weinig verschil (GEZIEN, `build-e70eab3-200-vol-later-1x.png` naast `...-zacht-later-1x.png`): zacht maakt aarde en gang iets grijzer, het fakkellicht links blijft even warm, Gloop en goud blijven fel. Op 2x (`build-e70eab3-200-2x-links-600s-vol-zacht.png`, boven vol, onder zacht) is zacht rustiger in de gang en de bovenkamer, maar de grove blokjes blijven. Mijn voorkeur: **zacht**, klein verschil, omdat de blinde test "cheap mobile game" en "softer" zei en zacht niets kost aan leesbaarheid. Blinde test op minuut 10 hieronder.

## Wat oogt nog goedkoop naast Rusty's Retirement (per punt)
1. **Grove vierkante vlekken in de gegraven kamers en de gangwand.** De lichtkaart en de stippen in de stenen zijn op 200 px blokken van 5 x 5 schermpixels, naast gladde 3D-figuren en zacht gras. Twee soorten beeld door elkaar: dat is wat "cheap" zegt. Rusty is één stijl, overal even scherp (GOK, uit hun winkelbeelden). Beeld: `build-e70eab3-200-2x-links-600s-vol-zacht.png` (bovenkamers met vlekken).
2. **Linker rand (x 0 tot 80) en rechts boven het bord (x 1440 tot 1920) zijn lege aarde** met een paar losse steentjes, ook na 20 min. Het hol groeit in het midden; de randen blijven onaf. Beeld: `build-e70eab3-200-vol-later-1x.png`, alle rijen.
3. **Het bord is een groot leeg plankenvlak met één regel.** Na het inklappen staat alleen "6" en "Next: Trick Lid" op ±450 x 50 px hout. Rusty's knoppen zijn kleine, afgewerkte iconen. Beeld: `build-e70eab3-200-2x-rechts-600s-vol-zacht.png`.
4. **Het nummerbordje linksboven (1, 2, 4, 6...) is een vlak oranje vierkant** in een andere stijl dan de rest, en zit half buiten de strook. Beeld: `build-e70eab3-200-vol-later-1x.png`.
5. **De eerste 40 s voor de eerste koop (27,8 tot 66 s) gebeurt niets wat goud brengt.** Zelfde punt als op e0ed18c; alleen tempo, geen beeld.

Punt 1 is wat ik als eerste zou doen voor een 9 (Olafs punt c en Mila).

## Beelden
- `build-e70eab3-200-min0-1-1x.png`: vol op 1, 9, 25, 60, 75 s
- `build-e70eab3-200-vol-later-1x.png` en `build-e70eab3-200-zacht-later-1x.png`: minuut 2, 4, 6, 10, 15, 20
- `build-e70eab3-200-2x-links-600s-vol-zacht.png` en `build-e70eab3-200-2x-rechts-600s-vol-zacht.png`: 2x op minuut 10

## Blinde test
Nieuwe set `hats-speelscherm-min10-200-e70eab3`: het beeld op minuut 10 (troon, hele strook gegraven) op het bureaublad, vol en zacht, tegen Rusty's Retirement, Spirit City en Desktop Defender (`scherm-zd-build-e70eab3-min10-200-vol-ware-maat.png`, `...-zacht-...`). Minuut 0 en 1 op 200 haalden al plek 2,0 bij Olaf; dit test of een vol hol hoger komt. De workflow draait bij de push.
