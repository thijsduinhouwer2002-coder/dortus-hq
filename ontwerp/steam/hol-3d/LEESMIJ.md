# Het hol in 3D (Mila)

Model: `producten/steam-hol/modellen/hol.py`. Draai: `<venv>/bin/python hol.py uit.png 720 120 32 2 2` (breedte, hoogte, samples, Gloop-versie, hoeden). ±25 s op 2 kernen voor 1440 x 240. Gebruikt `gedeeld.py` (camera, licht, kleuren) en zet Daans `gloop.py` ongewijzigd in de kamer.

## Ronde 1 (13 nov, ±15:40 tot 16:05 UTC)
Een doorsnede van de grond zoals een mierenbak: gras met sprietjes en bloemetjes, pruim aarde met ruis en kiezels, de ingang met een ladder, een stenen boogje en een fakkel op een paal, een gang met een stekelput (helm en munten van een gevallen held aan de rand), de schatkamer met een open kist, een gouden berg met beker en twee edelstenen, Gloop met helm en kroon, twee kleine ronde kamers boven de gang, wortels, spinrag. Alles zit in het spel (gangen, kamers boven de gang, stekelput, schat, ingang met fakkel; `godot/hol/hol.gd`).

- `ronde1-ware-grootte.png` (720 x 120), `ronde1-2x.png`, `ronde1-blad.png` (met Rusty's Retirement op dezelfde stroookhoogte erboven).
- Aanpassing aan het gedeelde licht, alleen in `hol.py`: "koel" stond in de achterwand van de kamer en "boven" gaf een witte vlek op het gras. Zelfde richting en kleur, verplaatst; Gloop krijgt evenveel licht. `gedeeld.py` zelf is niet veranderd.

Eigen oordeel (GEZIEN met Read, ware grootte naast Rusty's):
- Goed: Gloop, kroon en goud lezen meteen; de warme fakkels op pruim geven sfeer; de ronde kamers geven ritme; het is duidelijk "een hol onder het gras", niet nog een boerderij.
- Niet goed: Rusty's is vijf keer zo vol. Grote vlakken pruim zonder iets, de gang leest als één lange band. De helm onder de kroon zie je op ware grootte niet.

Frisse kijker (alleen het plaatje, ware grootte), letterlijk samengevat: "groene slijm met één groot oog en een gouden kroon, open schatkist, beker, grote hoop goud, ladder, lampen, putje op de vloer". Niet herkend: de helm aan de rand van de put, het spinrag, de wortels, of Gloop op of naast de berg staat. Stoppen met scrollen: 6 van 10, "de figuur is klein ten opzichte van de strook, de achtergrond is donker en druk". (De blauwe band die hij noemde was mijn bureaublad onder de strook, geen fout in het hol.)

## Volgende ronde
1. Gloop kan niet groter (ware maat in het spel), dus de kamer rond hem rustiger en lichter: geen kiezels binnen een halve kamer om de boog, warme gloed achter hem, achterwand van de kamer een trede lichter. Hij moet het lichtste vlak van de strook zijn.
2. Gloop op de rand van de berg in plaats van ernaast.
3. De gang breken: een bocht of trapje, en meer kleine dingen die over de dag veranderen (munten op de vloer).
4. Daarna drie versies op het blad voor Thijs (`ontwerp/steam/hol-3d-blad-voor-thijs.png`, ma 16 nov), opnieuw een frisse kijker.
