# Gloop in 3D (Daan)

Model: `producten/steam-hol/modellen/gloop.py` (versie 1 Speelgoed, 2 Muntje, 3 Schatbuik; 0 tot 4 hoeden). Camera, licht en kleuren: `producten/steam-hol/modellen/gedeeld.py` (voor iedereen, regel 1 van `ontwerp/steam/3d-stijl.md`).
Renderen: `python3 -m venv venv && venv/bin/pip install bpy==5.2.4`, dan `venv/bin/python gloop.py uit.png 2 4 320 320 20` (±10 s op 2 kernen, doorzichtige achtergrond met contactschaduw).

## Ronde 1 (13 nov, ±15:40 UTC)
- `ronde1-raster.png`: rijen versie 1, 2, 3; kolommen 0, 2 en 4 hoeden (320 px, op pruim).
- `ronde1-strook-ware-grootte.png` en `-2x.png`: dezelfde negen in de echte strook (run 43440335055, commit c9c3e60), lijf ±42 px hoog, naast de pixelhelden.

Eigen oordeel ronde 1:
- **Goed:** op ware grootte lees je meteen "slijmpje met één oog dat lacht": groot oogwit, ronde pupil met glimstip, open lach met tong, blosjes. Schattiger dan elke pixelversie van vandaag. De munt van versie 2 is op 42 px nog te zien.
- **Moet beter:** (1) de kroon is een kluwen goud, geen kroon: minder en grotere punten, recht op de band. (2) De helm leest als pannendeksel: hoger, met een neusstuk of klep. (3) Versie 3 (doorschijnend) zie je niet: glas leest niet op een donkere achtergrond, munten verdwijnen. Kiezen tussen weggooien of het lijf veel lichter en melkiger maken. (4) De tand staat los boven de lach en leest als druppel: aan de bovenlip hangen. (5) Het lijf is pastel tegen de pixelwereld; dat lost zich op als het hol ook 3D is (Mila), maar nog een tikje dieper groen proberen.
- **Nog niet gedaan:** frisse kijker (regel 4 van de 3D-stijl) en Rusty's en Ropuka op dezelfde maat ernaast. Eerst in ronde 2.

## Begin ronde 2 (zelfde run, ±15:48 UTC)
`ronde2-begin-muntje-4-hoeden.png`: tand hangt nu aan de bovenlip (leest als tand), helm hoger als koepel met punt (minder pannendeksel), kroon met vijf grote punten aan de voorkant. Volgende run: kroon los bekijken met 2 hoeden, versie 3 lichter en melkiger of weg, frisse kijker, Rusty's en Ropuka ernaast, dan het blad.

## Ronde 2a: standen (13 nov, ±16:30 UTC)
`gloop.py` kent nu een 7e woord `stand`: **rust** (standaard, verandert niets), **knipper** (oog dicht als platte streep), **blij** (oog als boogje omhoog, grotere lach) en **hap** (mond wijd open met tong). Zonder 7e woord is alles als voorheen, ook voor `hol.py` (getest: Mila's hol rendert nog). `ronde2-standen.png`: de vier op 320 px en linksonder op ware grootte (42 px, 2x). Op ware grootte lees je alle vier: oog open, streep, boogje, grote mond.
Voor Bram: in `sprites.json` per stand een eigen beeld, bijvoorbeeld args `["{uit}", "1", "0", "{w}", "{h}", "{samples}", "knipper"]`. Voorstel voor het spel: elke 4 tot 7 s één knipper (2 beelden), blij als er een hoed op de toren komt, hap bij opeten.
Nog in ronde 2: kroon los bekijken met 2 hoeden, versie 3 lichter of weg, frisse kijker, Rusty's en Ropuka ernaast, dan het blad (ma 16 nov).
