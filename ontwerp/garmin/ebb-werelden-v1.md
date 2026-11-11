# Ebb blad werelden v1 (Mila, run 39, 11 nov nacht): elk dier zijn eigen stukje zee

Opdracht: besluit Thijs 11 nov 23:13 (geen zwart meer, per dier een eigen wereld, ademschermen vol water). Eerst drie werelden helemaal af (schildpad, krab, clownvis) zodat Gijs de techniek kan bewijzen. Nog niet bouwen: eerst frisse keuring (8 of hoger).

Beelden in `werelden1/`: `werelden-260-rij-2x.png` (dubbel), `werelden-454-rij.png`, losse schermen `<scherm>-<dier>-<maat>.png`. Script `bron/werelden_v1.py <uitmap>`. Data `werelden1/ebb-werelden-v1-data.json`. Contrast `werelden1/contrast.txt`, punten `werelden1/punten.txt`.

## De drie werelden
| dier | plek | haak | punten |
|---|---|---|---|
| Turtle (4) | zeegrasweide op licht zand, sprieten hoog aan beide randen | één spriet heeft een hap eruit: de schildpad eet zeegras (groene zeeschildpad doet dat echt) | 68 |
| Crab (5) | grijze en paarse keien aan de randen, bleek zand | een verloren roze slipper op het zand, plus schelp en zeepok | 66 |
| Clownfish (8) | anemoon links (roze vingers, lichte toppen), paarse waaier en geel takje rechts, donkerpaars rif | één arm van de anemoon staat hoger en buigt naar het midden: hij zwaait naar zijn vis | 67 |

Familie later: zand + zeegras (schildpad, zeekoe-achtigen, rog), rotsen (krab, kreeft, zeester, octopus), rif (clownvis, kogelvis, zeepaardje), ijs (zeehond, orka, narwal), open zee met lichtstralen (walvis, dolfijn, haai). Elk dier krijgt binnen zijn familie een eigen ding (zoals de hap en de slipper).

## Regels (gelden voor alle 25)
- **Alleen vlakken en cirkelranden**, alleen de 64 MIP-kleuren (elk kanaal 00, 55, AA of FF; het script toetst dat), geen verlopen. Hoogstens 120 punten per wereld; deze drie zitten op 66 tot 68, dus ruim onder de grens van de krab-watchdog.
- **Eenheid:** 1/260 D, y van boven. Op elk horloge x·D/260, afkappen zoals bij de dieren. Vlakken mogen buiten de cirkel lopen (het horloge knipt).
- **Eén keer tekenen:** de wereld is per sessie gelijk, dus Gijs tekent hem één keer in een plaatje (BufferedBitmap) en zet dat elke beurt neer; de zee en het dier gaan eroverheen of eronder zoals op de beelden: eerst lucht en zee, dan wereld, dan dier en tekst.
- **Waar de wereld mag:** in het midden (x 70 tot 190) niet hoger dan y 219, aan de randen tot y 150. Zo blijft hij uit alle tekst op deze schermen; gemeten op de inkt van elke letter, 1 px verdikt.
- **Kleuren van de zee:** lucht NACHT 000055 (geen zwart meer), water 0055AA met schuimkam 00FFFF, diepe band 0000AA vanaf 55 procent onder de kam.

## Schermen (maten in 1/260 D, y = bovenkant tekst)
- **Ademschermen vol water:** bij "breathe in" staat de kam op 92 (ruim boven het midden van 130), bij "breathe out" op 186. Tussendoor schuift hij mee met de adem (lineair over de in- en uitademtijd). Kop op 34, regel "round 2 · 18 left" op 62, cijfer op 104 (in) en 92 (uit), maat 70. Het cijfer staat bij inademen in het water, bij uitademen erboven op nachtblauw. Het dier dobbert in de kam, midden op x 130+74, maat 21 (454: 37).
- **Inhoudscherm (hold):** kam op 30, "hold" op 36, "press START to breathe" op 64, timer op 78 maat 88, dier midden op 187 maat 20 (454: 35), "61 bpm · round 2" op 202.
- **Eindscherm:** indeling van blad v13 ongewijzigd, wereld eronder.
- **Menu:** kam op 184 (was ±170), dier in de kam midden op 186; pillen en menuregel blijven.
- **Sea log, dierscherm:** naam op 26, "friend 4 of 24" op 52, kam op 70, dier groot in vak 96 x 74 rond y 120, "START: swims with you" op 164.
- **Today, 8 weeks, instellingen:** achtergrond NACHT 000055 in plaats van zwart, verder gelijk. **Veiligheidsschermen blijven zwart met wit.**

## Contrast (gemeten, alle 36 schermen, laagste per tekst in `contrast.txt`)
Laagste overal **5,8:1** ("hold" in schuim op water 0055AA). Wit op water 0055AA is 7,3:1, wit op 0000AA 13:1, wit op nachtblauw 18:1, geel FFFFAA op water 6,8:1. Geen enkele letter raakt een stuk wereld of dier (de meting keek naar elke pixel onder de inkt; in v0 vond hij zo nog de krab onder "1:45", een belletje onder "Clownfish" en twee sprieten onder de bpm-regel, alle drie weg).

## GEZIEN met Read
Beide rijen bekeken (260 dubbel, 454). Wat werkt: het zwart is weg, elk scherm ziet eruit als een eigen plek, schildpad, krab en clownvis lezen meteen bij hun wereld. Eerlijk wat nog zwak is: (1) de werelden zijn dun in het midden onderin, omdat de tekst daar vóór gaat; aan de randen zit de rijkdom. (2) De slipper leest op 260 als roze vlek met wit bandje; op 454 is hij een slipper. (3) De zwaaiende arm is subtiel. Dit gaat naar de frisse keuring.

## Frisse keuring v1: 5 van 10 (Opus, 11 nov nacht)
Harde eisen gehaald, maar "op 260 vooral een plat blauw vlak met een dun bodemrandje", grappen onzichtbaar, rechte kam en rechte diepe band maken een vlag in plaats van een plek, dier hangt in de lucht, rif leest niet. Tien punten, waarvan ik 1 tot 9 in v1.1 heb gedaan.

# v1.1 (zelfde run): na de keuring
Beelden `werelden11/werelden-260-rij-2x.png`, `werelden11/werelden-454-rij.png`, ware grootte `werelden11/ware-grootte-1x.png`. Script `bron/werelden_v11.py`, data `werelden11/ebb-werelden-v11-data.json`, metingen `werelden11/contrast.txt` en `werelden11/punten.txt`.
1. **Maan en sterren** (punt 2): maansikkel FFFFAA r 8 op (214, 40) min nachtblauw r 7 op (218, 37), vijf sterren van 1 px (454: 2 px). Ebb is eb: de maan trekt het water omhoog als jij inademt. Hoort bij elke wereld, staat achter de zee (de zee dekt hem als het water hoog staat).
2. **Golvende kam** (punt 3): 2,5 golf over de breedte, 4/260 hoog, schuim 00FFFF 2/260, daaronder band 00AAFF tot 5/260. **Geen rechte diepe band meer** (punt 4): één water 0055AA, de wereld geeft de diepte.
3. **Elk dier een thuis en gedrag** (punt 1), allemaal echt gedrag van het dier: schildpad komt bij inademen met zijn kop boven de kam (lucht happen) en graast verder bij zijn zeegras (thuis 84, 214); krab blijft altijd op de bodem naast zijn slipper (thuis 178, 214) en blaast 2 belletjes; clownvis zwemt bij inademen uit (200, 150) en zit verder in zijn anemoon (thuis 36, 196), de voorste vingers liggen over hem heen (lijst `voor_het_dier` in de data: na het dier tekenen). Op eindscherm en sea log staat het dier groot in zijn vak zoals in v13.
4. **Randen tot y 120** (punt 5): sprieten tot 118, keien tot 120, anemoon tot 130, waaier tot 128. Boven y 175 blijft alles buiten x 36 tot 224.
5. **Grappen groter** (punt 6): slipper 52 x 16 met rand AA0055 en wit V-bandje (leest op 260 nu als slipper, GEZIEN); arm van de anemoon dikker met gele top; hap uit een brede spriet.
6. **Rif lichter** (punt 7): bodem AA5555 met FFAA55 brokjes.
7. **Sea log** (punt 8): kam op 80, dier in vak 96 x 70 rond 124, regel op 166.
8. **Eerlijke beelden** (punt 9): het script toetst nu elke pixel van elk scherm zonder letters: **0 pixels buiten de 64 MIP-kleuren** (vlakken hebben harde randen; alleen de letters zijn zacht, zoals de horlogefont ook). Plus een toets of teksten elkaar raken (minder dan 3 px): 0.
9. **Hold:** timer maat 80 op 76, bpm-regel op 162, zodat het dier thuis onderin kan zitten.

Punten: schildpad 65, krab 72, clownvis 76, plus maan en sterren 7 (gedeeld). Laagste contrast nog steeds 5,8:1.

**Bouwbaarheid (punt 10), voor Gijs:** teken niet het hele scherm als plaatje. Zee en lucht blijven zoals nu (een paar lijnen per beurt), de wereld komt in een BufferedBitmap van alleen de onderste strook plus de randen: op 260 een bitmap van 260 x 140 (y 120 tot 260) met een palet van de kleuren van die wereld (hoogstens 16, dus 4 bit, ±18 kB), op 454 454 x 245 (±56 kB bij 4 bit). Het dier en de `voor`-laag teken je er elke beurt overheen. Meet het geheugen op FR255 en fenix 7 en zet het in status.md.

GEZIEN met Read (260 dubbel, 454, en ware grootte 1x): het scherm is nu een plek met een eigen nacht, eigen bodem en een dier dat daar woont. Zwak nog: de hap in de spriet leest op 260 als een groen wantje; de anemoonarm komt dicht bij de bpm-regel (contrast wel goed).
