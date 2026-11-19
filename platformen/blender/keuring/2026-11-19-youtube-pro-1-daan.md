# Keuring YouTube-video 1 Click Joints Pro (click hinge), 19 nov 2026, Daan
Wat ik keurde: release `youtube-pro-1` na run 44493861163 (groen, klaar ±09:55 UTC): `click-joints-pro-uitleg-1-geluid.mp4` (122,5 s, 1920 x 1080, h264 en aac), `metingen.json`, `hoofdstukken.txt`, en de tekst in `commercie/wachtrij/youtube-pro-1.md`. Elke 2 s een beeld bekeken (61 beelden) en de momenten rond rood en "terug" op volle grootte.
Akkoord: nee (3 moet-punten, alle drie in het script of de tekst; geen nieuwe opname in Blender nodig voor 1 en 2)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Onderschrift "Push past the stop: the faces that would collide turn red" (0:54 tot 1:01) klopt niet met het beeld: alleen de boog krijgt een rode lijn, een rood vlakje en "+9° past limit". Geen enkel vlak van het model is rood te zien. `metingen.json` meldt wel `rood_vlakken: 7`, dus ze bestaan, maar ze zitten uit beeld (binnenkant of achterkant). Zelfde zin staat in de beschrijving. | feit (GEZIEN 0:56, 0:58, 1:00) | hoog | een beeld waarin het model zelf rood is |
| 2 | "Back inside the range, the red is gone" staat al in beeld bij 1:02 en 1:03, terwijl "+6° past limit" en de rode lijn nog te zien zijn. Pas vanaf ±1:04 is het rood weg. Precies de plek waar een kijker het verschil ziet. | feit (GEZIEN 1:03 volle grootte) | hoog | |
| 3 | Stop bij 90 en 135 klopt: de boog loopt tot 90 (1:12 tot 1:20) en tot 135 (1:26 tot 1:32), voorbij de stop komt "+9°" en "+10° past limit". `metingen.json`: 89,96, 114,96 en 135,04. | feit (GEZIEN) | hoog | |
| 4 | Begin is traag: 0:00 tot 0:08 een stilstaande titelkaart, daarna 0:10 tot 0:14 een hoofdstukkaart en 0:14 tot 0:22 een stilstaand been. Het eerste bewegende scharnier komt pas rond 0:40. Op YouTube beslist de kijker in de eerste seconden; zo haakt een groot deel af voor de hinge te zien is. | eerste deel feit (GEZIEN), afhaken is vermoeden | midden | kijkcijfers in YouTube Studio na een week |
| 5 | Vijf hoofdstukkaarten van 4 s (0:10, 0:36, 0:50, 1:08, 1:38): ±20 s zwart scherm met een nummer. Samen met titel en stilstaand been is ±36 van 122 s zonder beweging. | feit | hoog | |
| 6 | 1:22 en 1:24: onderschrift "it stops at 90°" terwijl het beeld "+9° past limit" toont. Niet fout (het rood laat juist de stop zien), wel verwarrend. | feit (GEZIEN) | hoog | |
| 7 | In het paneel staat bij "3 Fit and export" steeds "No joint yet", ook als er een scharnier staat (0:47, 0:58). Een oplettende kijker ziet het. Dit is de add-on, niet de video. | feit (GEZIEN) | hoog | `passing.py` of het paneel, voor Bram |
| 8 | Hoofdstukken kloppen met de kaarten en zijn elk minstens 10 s (laatste 1:48 tot 2:02). Eindkaart 14 s stil is goed voor YouTube-eindschermen. | feit | hoog | |
| 9 | Geluid: geen stiltes, -18,6 LUFS, piek -1,8 dBFS. YouTube zet op -14; deze is iets zachter dan de rest. | feit (gemeten met ffmpeg ebur128) | hoog | |
| 10 | Links in de beschrijving geven 200 (dortus.com/click-joints/?ref=yt en de Gumroad-pagina, GEZIEN 19 nov ±10:00 UTC). | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Echte beelden uit Blender 5.3.0, "Measured in Blender, not printed yet." in beeld en tekst: eerlijk. | feit | hoog | regel 5 |
| 2 | Geen stem, geen muziek van een ander, geen AI-beeld. | feit (opname-log niet gelezen, wel workflow-uitleg) | midden | |
| 3 | Plaatsen gebeurt door de hoofdchat na deze keuring, niet door Chris. | feit | hoog | regel 4 |

## Moet (blokkeert akkoord)
1. Onderschrift bij 0:54 tot 1:01 en de zin in de beschrijving aanpassen aan wat je ziet, bijvoorbeeld "Push past the stop: the arc turns red and shows how far you went." Of de camera zo zetten dat de rode vlakken op het model echt in beeld zijn; dan mag de zin blijven.
2. "Back inside the range, the red is gone" pas laten beginnen als het rood echt weg is (±1:04, het beeld waarin Bend weer onder 115 staat), niet bij 1:02.
3. Begin sneller: geen 8 s stilstaande titel. Open met de buig naar de stop (de beelden van ±0:40 tot 0:48) met titel en "90° · 115° · 135°" eroverheen, hooguit 2 s stilstand. Het stilstaande been (0:14 tot 0:22) inkorten tot ±3 s.

## Kan (mag later)
1. Hoofdstukkaarten van 4 naar ±1,5 s, en het hoofdstuk vullen met beeld (de 10 s-eis van YouTube haal je dan met beweging in plaats van zwart).
2. 1:22: onderschrift "Push past 90° and it turns red" bij het rode stuk.
3. Geluid naar ±-14 LUFS.
4. "No joint yet" bij een scharnier: aan Bram als kleine fout in de add-on (doet niets aan deze video).

## Omslag
Beeld op **0:47,5** (`ffmpeg -ss 47.5`): de knie staat op de stop, boog van 0° tot 115° helder wit, groene naad, Bend 114.90 in het paneel. Snij het paneel rechts eraf (x 0 tot ±1520), schuif het model naar het midden, en zet "STOPS AT 115°" groot linksboven in wit met het groen van ons palet op "115°". Niet het rode beeld: zonder uitleg leest rood als "kapot".

---
# Herkeuring versie 2, 19 nov 2026 ±12:35 UTC, Daan
Wat ik keurde: release `youtube-pro-1`, `click-joints-pro-uitleg-2-geluid.mp4` uit run 44519478563 (groen, commit eb3f1ff, bevat ac0dbb7). 127,0 s, 1920 x 1080, h264 en aac. Elke 2 s een beeld, 0:12 tot 0:24 en 1:00 tot 1:08 elke halve seconde. Tekst in `marketing/wachtrij/2026-11-20-yt-lang-pro-hinge.md`.
Akkoord: ja YouTube Pro 1 versie 2 (click-joints-pro-uitleg-2-geluid.mp4)

## Mijn drie moet-punten
| # | Moet | Nu | Bewijs |
|---|---|---|---|
| 1 | Zin over rood klopt met beeld | "Push past the stop: the arc turns red and shows how far you went." Rode boog en "+9° past limit" in beeld. Zelfde zin in de beschrijving. | GEZIEN 0:54 tot 1:02 |
| 2 | "Back inside the range" pas als rood weg is | Bij 1:03 staat nog "+2° past limit" zonder onderschrift; vanaf 1:04 geen rood meer en dan pas de zin. `metingen.json`: `rood_na_terug: 0`. | GEZIEN 1:03 en 1:04 per halve seconde |
| 3 | Geen stilstaande titel, been korter | Video opent met de buig naar de stop, titel en "90° · 115° · 135°" erover (0:00 tot 0:07). Stilstaand been ±3 s (0:14,5 tot 0:17). | GEZIEN |

Ook gezien: geluid -14,3 LUFS (ffmpeg ebur128), stap 3 in het paneel zegt nu "Good fit" (de fout uit versie 1 is weg), dortus.com/yt/ geeft 200 (12:35 UTC).

## Kan (mag later, blokkeert niet)
1. 0:17 tot 0:22: onderschrift "Start with one solid part, like this leg." staat er nog terwijl het been al een scharnier en boog heeft en buigt, nog voor "Pick the end stop... Click Place hinge." Wie oplet ziet de volgorde omgedraaid. Beter: dat stukje weglaten of daar al "Pick the end stop" tonen.
2. Hoofdstukkaarten zijn nog 4 s zwart (5 keer). Mijn oude kan 1 blijft staan.

## Omslag
Blijft 0:47,5 uit versie 1 met "STOPS AT 115°". In versie 2 is dat beeld ongeveer op 0:40 (knie op de stop, boog wit, Bend ±115). Kies het beeld waarop de boog helemaal wit is en Bend het dichtst bij 115 staat.

---
# Herkeuring versie 3, 19 nov 2026 ±21:35 UTC, Daan
Wat ik keurde: release `youtube-pro-1`, `click-joints-pro-uitleg-3-geluid.mp4` (geüpload 21:14 UTC, run 44614093759). 127,0 s, 1920 x 1080, h264 en aac (ffprobe). Elke 2 s een beeld bekeken, plus 0:04 groot.
Akkoord: ja YouTube Pro 1 versie 3 (click-joints-pro-uitleg-3-geluid.mp4)

## Wat Chris vroeg
| Vraag | Nu | Bewijs |
|---|---|---|
| De zin in het eerste deel | "Click Joints Pro: a hinge with a real end stop." Geen "print-ready" meer. | GEZIEN 0:08 |
| Blik op het geheel | Zelfde opbouw als versie 2 die ik goedkeurde: titel met buig, plaatsen, buigen tot 115°, rood voorbij de stop en weer weg, 90° en 135°, kogels met groene band, eindkaart dortus.com/click-joints. Mijn drie moets van versie 1 staan nog goed. | GEZIEN; `metingen.json`: buig_stop 114,96, rood_na_terug 0 |

Ook gezien: geluid -14,3 LUFS (ffmpeg ebur128); dortus.com/click-joints geeft 200 (21:35 UTC).

## Moet vóór plaatsing (geen werk aan de video)
1. `marketing/wachtrij/2026-11-20-yt-lang-pro-hinge.md` wijst bij `bestand:` nog naar `uitleg-2`. Wie de post in Metricool zet (Maker van Roep), moet daar `uitleg-3` van maken en in Metricool het bestand vervangen. Anders gaat versie 2 met "print-ready" uit.

## Kan (blokkeert niet)
1. Oude kan blijft: 0:18 tot 0:22 staat "Start with one solid part, like this leg." terwijl het been al een scharnier heeft en buigt.
2. Eindkaart staat 25 s stil (1:42 tot 2:07). Kan naar ±8 s; dan is de video ook korter en de kijkduur per kijker hoger.
3. Hoofdstukkaarten nog 4 s zwart (5 keer).
4. 0:00 tot 0:08: "Bends 0° to 115°" plakt rechts tegen het titelvak. Een paar px lucht of lager zetten.
