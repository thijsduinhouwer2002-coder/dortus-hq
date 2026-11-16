# Icoon Gloop-spel: voorstel (Mila, 16 nov)

## Keus na ronde 5 (±05:50 UTC): `icoon-500-keus.png` en `launcher-40/60/80-keus.png`
- Zelfde toren als 5d (puntmuts, hoge hoed op de punt, kroon scheef bovenop), maar **Gloop groter met heel gezicht** (moet van kijker 4) en een **lichter oranje spotlicht** (kijkers 2, 3 en 5 vonden het bruin dof). Vervangt het paarse icoon van ronde 2.
- Kijker 5 (A/B/C): 5d 6/5/4, Gloop groot 7/7/6, middenmaat 7/6/6. Kijker 6, keus tussen de toppers (`kijker-toppers-ronde5-keus.png`): **7/6/6, als tweede genoemd** na de Crossy-kip; noemt de drie hoeden goed en het spel ("stapelen zonder dat de toren omvalt"). Lichter of donkerder spotlicht maakte voor hem geen verschil.
- Wat nog zwak is (eerlijk): op 40 px valt de paarse puntmuts weg in de zwarte hoge hoed, dan tel je twee hoeden. Het oog, de kroon en het mint lezen wel. Kan later: een vierde hoed die nog valt (twee kijkers stelden het voor), alleen als het oog vrij blijft.
- `icoon-500-r5-kroon-boven.png` en `-kroon-onder.png` zijn opnieuw gemaakt met het lichtere spotlicht; de kijkers zagen de iets donkerdere versie.
- Volgende: Daan keurt op fouten en leesbaarheid, daarna gaat het naar Gijs (launcher schalen naar de SDK-maat per horloge).

## Ronde 5 (±05:40 tot 05:50 UTC): donker warm, kroon bovenop
Op Daans richting (16 nov 05:40): donker warm zoals de randen van het spelscherm, de schuine lichtbundel, geen paars als achtergrond, drie hoeden met een eigen omtrek en een donkere rand ertussen, bovenste hoed scheef binnen het vak.
- **Keus: `icoon-500-r5-kroon-boven.png`** (launcher `launcher-40/60/80-r5-kroon-boven.png`). Onder op Gloop de puntmuts, daarop balanceert de hoge hoed op de punt, bovenop scheef de kroon. Bijna zwarte grot met een oranje spotlicht achter de toren, Gloop geeft mint licht, lichte warme rand om de hele toren en een donkere rand om elke hoed.
- Waarom: vier blinde kijkers, elk nieuw, ons icoon telkens op een andere plek tussen dertien echte toppers uit de Connect IQ-winkel (`kijker-toppers-ronde5.png`):
  - zacht bruin, toren klein (ronde 5a): 5/4/4, niet in top 3; "hoeden lopen in elkaar over, zwarte hoed valt weg".
  - grotere hoeden met lichte rand (5b): 5/5/4, in A/B tegen 5a 6/5/5.
  - zwarte grot met fel oranje spotlicht (5c): 7/5/5, **voor het eerst in de top 3**; de kroon onderaan leest als "emmer met munten".
  - kroon bovenop (5d): **8/6/6 en als eerste genoemd** van alle veertien; A/B tegen 5c: 8/7/7 tegen 7/5/5. Hij noemt drie hoeden goed van onder naar boven en snapt het spel: "zo hoog mogelijk stapelen zonder dat de toren omvalt".
  - Ter vergelijking: paars van ronde 3 kreeg 6/7/5 en kwam nooit in de top 3.
- De grap: een hoge hoed die op de punt van een puntmuts balanceert, met de kroon er scheef op. Je ziet dat hij zo valt.
- Eerlijk: alle drie hoeden en Gloop zijn de renders uit het spel; alleen de kroon is iets feller gezet (helderheid 1,3) omdat hij klein als goudklomp las. De bundel en het warme donker zitten in het spel.
- Paars: de puntmuts is paars, maar dat is een hoed uit het spel, geen achtergrond.
- Open (moet van kijker 4): Gloop en zijn oog vallen klein net weg, op 40 px is het oog "net te zien". Volgende stap: Gloop groter of hoger, toren iets kleiner. Daarna aan Daan voor fouten en leesbaarheid, dan pas aan Gijs.
- Script: `ontwerp/garmin/bron/gloop_spel_icoon_r5.py bron-renders <uit>`.
- GEZIEN met Read: alle vijf versies op 500, de kijkers 5a tot 5d op ware grootte en de A/B-stroken op 110/40/60/80 px.


## Ronde 3 blind gekeurd (±05:15 UTC): nog niet goed genoeg
- Nieuwe kijker, ons icoon (vak 3) tussen dertien toppers: `kijker-toppers-ronde4.png`. Cijfers 6/7/5. Hij verwacht "een tamagotchi", niet een stapelspel; de drie die opvallen hebben allemaal een **donkere achtergrond** (raket, Fruit Spider, Simon).
- **Volgende ronde (Mila):** donkere grot (bijna zwart met warme gloed), Gloop groter en lichtgevend, één nette hoge toren van 3 hoeden die duidelijk wiebelt (of een vallende held erboven met "!", dan zie je de spelactie). Dit icoon nog niet aan Gijs geven.

## Ronde 2 (±05:10 UTC): tussen de toppers
- Elf echte iconen van de populairste spellen in de Connect IQ-winkel (Crossy Road 3D, Stack, Step Farmer, Flappy Bird, Floppy Bird, Simon, Fruit Spider, ZigZag, Dino, Timberman, AstroBlast; via de winkel-API) naast de onze op 110 px: `kijker-toppers-ronde1.png`, `kijker-toppers-ronde3.png`.
- Ronde 1 (Gloop klein, toren van zeven hoeden, bruine grot) viel weg: modderig oranje, Gloop klein. Daarna Gloop groter, felle achtergrond in twee kleuren.
- Blinde kijker: wint **rust op paars** 7/6/7 (oranje rust 6/6/7, slok-varianten 5 tot 6 met leesbaar klein 4). Hij noemt ons nog niet in zijn top 3 (Simon, Fruit Spider, Dino): "slijmpje met een hoed, geen toren". Daarom: **minder en grotere hoeden die steeds schever staan** (kroon, koksmuts, puntmuts, hoge hoed), toren loopt boven uit beeld.
- **Besluit voor nu: winkelicoon en launcher = rust op paars** (`icoon-500-rust.png`, `launcher-*-rust.png`). Waarom: paars is de tegenkleur van Gloops groen en geen enkele topper is paars; rust houdt oog en lach leesbaar op 40 px. De slok blijft voor de schermafbeeldingen.
- Open: nog een kijker op de laatste versie (ronde 3 nog niet blind gekeurd); paars is nieuw naast de warme grot van het spel (de lichtbundel blijft wel), past dat bij Het Hol? Daan mag zeggen als hij het niet vindt passen.

## Ronde 1 (±05:00 UTC)

Nog niet af en nog niet gekeurd. Het spel heeft nog geen icoon; dit is een begin, zodat Gijs niet met een leeg vak hoeft te bouwen.

- `icoon-500-slok.png` en `icoon-500-rust.png`: winkelicoon 500x500 (zelfde maat als bij Ebb). Gloop met de toren van hoeden die boven de rand uitloopt en een beetje naar rechts helt; bij "slok" steekt de held uit zijn mond (zelfde slok als in de kit).
- `launcher-40/60/80-*.png`: strakkere uitsnede (Gloop groter), want op 40 px is het oog het enige dat je herkent. De echte launchermaat per horloge staat in de SDK; Gijs schaalt naar die maat.
- `blad-icoon.png`: alles naast elkaar.
- Script: `ontwerp/garmin/bron/gloop_spel_icoon.py bron-renders icoon`.

Mijn keus voor nu: **launcher = rust** (op 40 en 60 px leest de slok als een vlek in de mond; rust laat oog, lach en hoeden zien), **winkelicoon = nog open** (rust is rustiger, slok is de grap). Eerlijk: alles wat je ziet zit in het spel (Gloop, held, de tien hoeden).
GEZIEN met Read: blad-icoon (twee versies van de opbouw: eerst te dicht op Gloop, toren viel weg; daarna kleiner Gloop, toren uit de rand).
Volgende: blinde kijker tussen de app-iconen van de toppers in de Connect IQ-winkel, dan pas aan Gijs.
