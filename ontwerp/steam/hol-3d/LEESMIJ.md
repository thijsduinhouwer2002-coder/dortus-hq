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

## Ronde 2 (zelfde run, ±15:55 UTC)
Punt 1 en 2 van hieronder gedaan: geen kiezels rond de boog, achterwand van de schatkamer een trede lichter en warmer (7a4a78) met een gloed achter Gloop, Gloop zit nu op de linkerflank van de berg. `ronde2-ware-grootte.png`, `ronde2-2x.png`, `ronde2-blad.png`.
- GEZIEN met Read: de kamer is nu het lichtste, warmste vlak van de strook; groen Gloop op roze-warm leest beter dan op donker pruim.
- Tweede frisse kijker (andere kijker, alleen het plaatje): "groenblauwe slijm met één groot oog en een gouden kroontje, voor een berg goud, kist, beker, ladder, fakkels". Niet herkend: stekelput met helm ("kleine donkere figuurtjes met lichtpuntjes"), spinrag ("zwaard aan de muur"). Weer 6 van 10: "er gebeurt niets dat het oog vasthoudt, ik zie niet meteen wat het spel is".
- Les: rustiger en lichter helpt de figuur, maar het cijfer komt pas omhoog met een verhaal in beeld. Het spel is: helden komen binnen, vallen in de put of worden opgegeten, hun hoed gaat op Gloops toren. Een held in de gang op weg naar de put (Daan maakt de helden) is wat ontbreekt. De stekelput moet groter of lichter om op 120 px te lezen.

## Volgende ronde
1. (gedaan in ronde 2) Gloop kan niet groter (ware maat in het spel), dus de kamer rond hem rustiger en lichter: geen kiezels binnen een halve kamer om de boog, warme gloed achter hem, achterwand van de kamer een trede lichter. Hij moet het lichtste vlak van de strook zijn.
2. (gedaan in ronde 2) Gloop op de rand van de berg in plaats van ernaast.
3. De gang breken: een bocht of trapje, en meer kleine dingen die over de dag veranderen (munten op de vloer).
4. Stekelput leesbaar: breder, stekels lichter, de helm groter en zichtbaar op de rand. Spinrag weg of groter.
5. Een held in de gang (vraag aan Daan: heeft hij al een 3D-held, anders een eenvoudige stand-in die eerlijk is).
6. Daarna drie versies op het blad voor Thijs (`ontwerp/steam/hol-3d-blad-voor-thijs.png`, ma 16 nov), opnieuw een frisse kijker.
