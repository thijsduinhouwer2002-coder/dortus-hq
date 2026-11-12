# Ebb: winkelbeelden v5 met de werelden (Mila, run 54, 12 nov)

Opdracht hoofdchat 06:00: poster en vijf kaarten opnieuw met de werelden erin, krab met zwemband voorop, één kaart met de werelden naast elkaar, één met dag en nacht. Ontwerp; Gijs vult ze later met echte simulatorschermen.
Script `bron/winkel_v5.py`, beelden `winkel5/` (poster 1000, kaarten 800, `rij-220.png` op winkelmaat, `overzicht-500.png`).
GEZIEN met Read: overzicht en rij op 220 na elke ronde.

## De zes beelden
| Nr | Bestand | Kop (geel woord) | Onderregel | Scherm (nu bladbeeld, straks simulator) |
|---|---|---|---|---|
| 0 | `0-poster.png` | Hold your breath. Make **sea friends.** | Each one in their own little world. | krab hold dag (zwemband), geel briefje "can't swim yet" met pijl naar de band, gele badge "One payment · no subscription" |
| 1 | `1-breathe.png` | Breathe in. The sea **rises.** | Breathe out, it sinks. | krab inademen dag |
| 2 | `2-worlds.png` | Every friend, their **own world.** | And their own silly thing. | drie vergrote stukken: krab "in a float", octopus "in a bath", haai "brushing" |
| 3 | `3-day-night.png` | The sea keeps **your time.** | Sun by day. Moon by night. | krab inademen dag (voor) en nacht (achter), "day" en "night" eronder |
| 4 | `4-beach.png` | Your day is a **beach walk.** | Every session leaves a shell. | Today met drie schelpen |
| 5 | `5-sea-log.png` | Fill your **sea log.** | Every friend you meet, saved. | sea log onder water |

## Besluiten
- **De grap staat op de poster: "can't swim yet".** Waarom: de frisse kijker stopt met scrollen op de krab in de zwemband met het briefje; zonder briefje is het een krab in een band, met briefje een grap. Eerlijk: het briefje is een onderschrift op de winkelplaat, niet iets in de app. De zwemband zit wel echt in de app.
- **Drie werelden groot in plaats van vijf hele schermen.** Waarom: frisse keuring 1 (6,5) zag op 220 px "vijf keer hetzelfde blauwe rondje"; de grap per dier leest pas als de held groot is. De vergroting is een uitsnede van het echte scherm (zoals de loep van v2), niets bijgetekend. Afwijking van de opdracht (vijf): bij een vergelijking gaat leesbaarheid op winkelmaat voor.
- **Dag en nacht als twee schermen, niet één gedeeld scherm.** Waarom: frisse keuring 2 vond de scheidslijn door de "12" en de krab een fout in het beeld.
- **Koopreden als gele badge op de poster.** Waarom: onderaan in kleine letters was hij op 220 px onzichtbaar (keuring 1). "no extra account" is eraf om de badge groot te houden; staat in de winkeltekst.
- **Onderregels kort en 56 px** (was 44): op 220 px leest nu elke kop en onderregel.
- **Kleine tekst in de schermen blijft.** Keuring 2 vroeg die weg te halen, maar het is het echte scherm: wat je ziet zit in het product.

## Frisse keuringen (losse agent, alleen beelden)
1. v5a: **6,5.** Moet: werelden groter (gedaan), onderregels groter en korter (gedaan), koopreden als badge (gedaan). Kan: strand zonder uuras (niet gedaan, het is het echte scherm), kleine tekst uit het scherm (niet, eerlijkheid).
2. v5b: **7.** Moet: dag en nacht niet door het cijfer snijden (gedaan, twee schermen). Kan: haai groter (gedaan, uitsnede strakker), opbouw meer variëren (nog open: zes keer een blauw rondje).

## Voor Gijs (later, als de werelden in de app staan)
Vervang elk scherm door de simulatoropname van de fenix 8 47 mm met dezelfde inhoud: poster = krab hold dag; 1 = krab inademen dag; 2 = krab, octopus en haai inademen dag (uitsnede: midden x 0,50 / 0,60 / 0,64 van de schermbreedte, y 0,49, vak 0,38 van de breedte); 3 = krab inademen dag en nacht; 4 = Today met drie schelpen; 5 = sea log. Dan in `winkel_v5.py` de neutrale ring vervangen door de echte kast (uitsnede zoals `winkel_v4.uitsnede`). Tot die tijd niet uploaden: deze beelden zijn het blad, niet de app.

## Nog open
- Opbouw varieert weinig (zes keer een rond scherm op blauw). Idee voor v5.1: kaart 2 op een lichte strandkleur, of één kaart met alleen een groot dier zonder kast.
