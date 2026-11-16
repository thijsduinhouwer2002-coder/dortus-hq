# Icoon Gloop-spel: voorstel (Mila, 16 nov)

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
