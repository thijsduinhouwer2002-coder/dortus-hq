# Ebb blad v9: de vier punten "Voor Mila" uit keuring bouw 4 (run 33, 11 nov)

Blad `ebb-blad-v9.png`, losse schermen `blad9/` (260 en 454), bron `bron/blad_v9.py` (tekent met `horloge_sim.py`, dus zoals `DierenData.mc` het doet, en met Barlow Condensed Medium en SemiBold uit `bron/fonts/`, OFL). Meting `blad9/meting-v9.txt`. Dieren: v8.3, niets veranderd aan de vormen.

Besluit Thijs 11 nov 07:13 gaat voor: Ebb gaat door tot elk keuringscijfer minstens 8. Dit blad is mijn deel voor "Bouw visueel" en "Dieren in de app".

## 1. Sea log op 260: groter, 2 rijen van 3
- **Raster:** 6 dieren per blad in 2 rijen van 3, **maat 23 op 260** (was 15) en **40 op 454**. Dat is ruim 1,5 keer zo groot: op 260 is een dier gemiddeld ±48 px breed in plaats van ±30.
- **Plek (in 1/260 van de diameter, keer D/260 voor andere horloges):** kolommen op midden −62, 0, +62; rijen op y 103 en 150. Kop "sea log" op y 28 (SemiBold 26), "8 of 24" op y 58 (Medium 17), naam op y 184 (SemiBold 26), regel eronder op y 210 (Medium 15), bladstippen op y 236 (straal 2, stap 9). y is de bovenkant van de tekst.
- **Bladen:** 4 bladen van 6 = de 24 gewone dieren op volgorde (blad 1: nr 1 tot 6, blad 2: 7 tot 12, enzovoort). **Blad 5 is het bonusblad:** alleen de zeekomkommer, groot (maat 37 op 260), met "bonus" in geel erboven. Dus 5 stippen.
- **De regel onder de naam blijft** (antwoord op je vraag van 05:35): met 2 rijen is er ruimte, en die regel ("4 more weeks in a row", "START: swims with you") is de haak die je terug laat komen.
- Keuzestip: 2 px onder het gekozen dier zoals nu, in schuim.
- Gemeten: alles binnen 0,85 R; kader x binnen 2 px van het midden, behalve blad 4 (+6,5 px op 260) omdat orka en walvis rechts breed zijn; de dieren zelf staan op hun zwaartepunt op de kolom.

## 2. Gladde silhouetten (orka, haai, zwaardvis, en alle andere)
Oorzaak van het rafelige: het silhouet krijgt nu de rand door het dier 4 keer schuin 2 px te verschuiven, en daarna gaan rol 7, 8 en 10 er in 00AAFF overheen. Bij dunne vinnen en het zwaard geeft dat dubbele, getande lijnen (`blad9/silhouet-oud-boven-v9-onder-4x.png`, boven oud, onder nieuw).
- **Nieuw:** rand **1 px in 8 richtingen** (recht en schuin) in 00AAFF, dan de vorm in 000055 erover, **geen binnenlijnen** meer in het silhouet. Op 454 (maat 40 en hoger) 2 px in 8 richtingen.
- Gevonden dieren veranderen niet (stickerrand blijft zoals nu).
- Gezien met Read 4x: orka, haai, zwaardvis, manta en rog worden één schone lijn. Het silhouet zegt nog steeds wat het is (vin, zwaard, hoorns), en het is een raadsel, dus details hoeven er niet in.

## 3. "Sea complete": een eigen feest
Geen gewoon eindscherm meer. Eén keer in je leven, dus het mag knallen:
- De zee staat hoog (kamlijn op y 77), de **walvis groot in het midden** (maat 38 op 260, 66 op 454, op y 108) met drie belletjes als fontein.
- **De 23 andere vrienden zwemmen in een glimlach onder hem**, in twee bogen rond (130, 98): buitenboog straal 90 met 14 dieren van hoek 30° tot 150°, binnenboog straal 64 met 9 dieren van 42° tot 138° (90° is recht onder), maat 11 op 260 en 19 op 454, volgorde nr 1 tot 23. Dat is de grap: je hele zee lacht naar je.
- Tekst: "sea complete" in geel (SemiBold 23, y 26), "24 of 24 friends" in schuim (y 51), "12 weeks in a row" onderin (y 206).
- **Geen tijden op dit scherm**: die staan één knop verder in het duikprofiel. Eerlijk: wat je ziet zijn je eigen 24 dieren.
- Gemeten: 0 pixels buiten 0,85 R, kader op het midden.
- **Let op voor de watchdog:** 24 dieren tekenen is zwaar. Teken ze één keer in een BufferedBitmap (of via EbbDierPlaatje, doorzichtig, zie keuring punt 1) en zet daarna alleen dat plaatje neer. Lukt het niet binnen de tijd: binnenboog weg (14 dieren), dat leest nog steeds als glimlach.

## 4. Volgend dier: een schaduw in het water
Donkerblauw op donkerblauw viel weg. Nieuw: het volgende dier is een **zwarte schaduw met een schuimrand** (00FFFF, 1 px in 8 richtingen op 260, 2 px op 454), zonder binnenlijnen. Zwart haalt op elke zeetint (0055AA, 0000AA, 000055, en het AMOLED-verloop) genoeg verschil, en schuim op zwart is de sterkste rand die we hebben. Het leest als "wie zwemt daar?": nieuwsgierig, niet verklappen.
- Op het eindscherm op y 112 (260), maat 26 op 260 en 45 op 454. Tekst eronder: "1 more session:" (wit) en "a new friend" (geel), dan de reeks.
- Alleen in het water. In de sea log (op zwart) blijft het silhouet 000055 met 00AAFF-rand (punt 2).

## Antwoord op de vraag van Gijs (11 nov 05:35)
- **Eindschermen 6b, 6c en 6d: "in het water" is goed**, de zee blijft daar op ±0,33 D. Het dier dat boven komt en de regels in het water zijn het verhaal van Ebb. Wel: tekst minstens 0,03 D onder de kamlijn of erboven, nooit erop.
- **Sea complete** krijgt het nieuwe scherm hierboven (zee op y 77 van 260 = 0,30 D).
- **Sea log op 260:** geen 3 rijen meer, dus geen kleinere dieren; de regel onder de naam blijft.

## Toets aan de lat
1. Stopt iemand met scrollen? Sea complete wel: een grote walvis met een glimlach van 23 gekleurde dieren eronder is het winkelbeeld voor "verzamel je hele zee". Sea log op 260 nu leesbaar op ware grootte.
2. Herkenbaar? Ja: dezelfde stickerdieren, één zee met kamlijn, Barlow.
3. Grap of haak? De glimlach van vrienden, en de schaduw "wie zwemt daar?".
4. Klein? Bekeken op 260 ware grootte en 2x: alle 6 dieren per blad herkenbaar. Zwakste: in de glimlach op 260 zijn de dieren klein (±22 px) en raken ze elkaar in het midden; dat is bedoeld als een school, niet om elk dier te lezen.
