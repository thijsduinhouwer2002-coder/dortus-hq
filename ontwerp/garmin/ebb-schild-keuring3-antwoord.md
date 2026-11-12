# Schildpad na frisse keuring 3, nachtregel v1.3 en nachtwater MIP (Mila, run 55, 12 nov)

Opdracht hoofdchat 12 nov 07:35, punten 1 tot 3 (`ebb-krab-echt-keuring-3.md`). Script `bron/schild_keuring3.py` (bouwt op `krab_keuring2.py` en `werelden_v32.py`, verandert daar niets). Beelden `keuring3/` (alle zes schermen, dag en nacht, 454 en 260; `overzicht-schild-260-2x.png`).
GEZIEN met Read: overzicht 260 2x na elke ronde, kop van dichtbij (hold dag, menu nacht, eind dag) op 4x.

## 1. Schildpad
- **Kop met donkere omtrek** van 1 px in 000055 (zoals de krab) en een **groot oog**: wit rondje met donkere rand, zwarte pupil en een wit lichtpuntje (straal 3 px op 260). Het gezicht leest nu ook op ware grootte.
- **Geen blad meer in de bek.** Geprobeerd: (a) een los, licht slablad (bleekgeel FFFFAA, groene nerven, gekrulde rand) vlak voor de bek: frisse kijker 3b zag het niet als eten, kop en blad werden een groene vlek (6); (b) hetzelfde blad aan een steeltje, los van het gezicht: frisse kijker 3c "lijkt los voor zijn kop te zweven", nog steeds dezelfde kleurfamilie als de kop (6). Dat is de derde keer dat het eten niet leest.
- **Besluit: de schildpad eet niet meer onder water; zijn grap is de meeuw die meeliftet op zijn schild (boven water).** Waarom: drie keurders herkenden het eten niet en het maakte zijn gezicht onleesbaar; een held met een helder gezicht gaat voor een grap die niet overkomt. De functie `slablad()` blijft in het script voor een latere poging met een ander voorwerp.
- **Open plek rond de held** in de weide (inhouden en menu): van 1,45 x maat links tot 1,2 x maat rechts van zijn midden staan geen sprieten of plukken. Op het **eindscherm** staat de schildpad voor open water: links (x 20 tot 132 op 260) geen sprieten en geen plukken meer.
- **Regel voor alle werelden** (in de json): achter de held staat nooit iets in dezelfde kleurfamilie als de held.

## 2. Nachtregel v1.3 (in `ebb-nachtregel-v1.json`, sleutel `held_nacht`)
- Groene en bruine kleuren van de held houden bij nacht hun dagkleur op MIP (21 kleuren uit het palet staan in de lijst), op AMOLED 80 procent van de dagkleur: een tint lichter dan de gewone regel.
- De donkere omtrek wordt bij nacht een smalle lichte rand: 5555AA (MIP), (85, 85, 170) AMOLED.
- Rood, oranje, roze en wit van de held volgen de gewone regel (de krab bleef daarmee goed zichtbaar).
- GEZIEN: de schildpad springt bij nacht nu juist uit beeld (frisse kijker 3c: "bij nacht springt hij er juist beter uit").

## 3. Nachtwater MIP (in de json, sleutel `mip_nachtwater`)
Eén gedempt diep blauw 000055 in plaats van de felle vlakken (0000AA, 0000FF), met dunne golflijnen van 1 px in 0000AA om de 18 px (op 260), niet door tekst en niet door de held. Lucht blijft 000000.

## Frisse keuringen (losse agent, alleen beelden)
- 3b (slablad voor de bek): 6. Kop en blad een vlek, oog te klein; nachtwater rustig maar "blokkerige stroken" (dat waren de oude vlakken onder de held: nu weg).
- 3c (blad aan steeltje, oog groter): 6. Blad zweeft los en is dezelfde kleur; held bij nacht goed; kop op de lichte golfband overdag zwak (nu met donkere omtrek).
- Na het weghalen van het blad niet opnieuw fris gekeurd in deze run. Volgende run: frisse keuring op de echte schermen van Gijs.

## Voor Gijs
Zie bovenaan `berichten/gijs.md`.
