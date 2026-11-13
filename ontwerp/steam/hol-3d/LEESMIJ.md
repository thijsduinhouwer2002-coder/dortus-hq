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

## Ronde 3 (13 nov ±17:45 tot 18:00 UTC): het hol als tegels voor Bram
Bram knipt het hol in stukken voor het spel (`"soort": "stukken"` in `pijplijn/sprites.json`). Drie dingen gedaan, alleen in `hol.py`:
1. Gloop heet `gloop_...` (alle onderdelen), zodat een laag zonder Gloop kan; het spel tekent hem zelf.
2. Het hol ligt op de rijen van `hol.gd`: gras 0 tot 8, bovenste rij 8 tot 24, gang 24 tot 40, vloer op 37. De camera staat vast (`CAM_MIDDEN`), zodat de rijen niet meer verschuiven als het maaiveld verandert. Het gras loopt ver naar achteren en vult rij 0 tot 8 (er zat een donkere band boven). Kamers boven de gang en de stekelput staan elk midden in één kolom van 16.
3. Kolom 13 en 14 (spelpixel 208 tot 240) zijn een rustig stuk dat herhaalt: de aarde-ruis gaat rond in x met een periode van één kolom, gras en kiezels liggen daar in elke kolom gelijk, en een lange egale lamp geeft er licht dat niet verloopt. De fakkel van de rechter gang schoof naar x 5,0, wortels en spinrag een stukje naar links.
- `ronde3-rijen-links.png`, `ronde3-rijen-rechts.png`: 960 x 160, 2x, met blauwe lijnen op 8 en 24, geel op 37, paars per kolom.
- `ronde3-tegel-kolom14-zesmaal.png`: zes keer kolom 14 naast elkaar.
- GEZIEN met Read: rijen kloppen (grasrand op 8, plafond op 24, vloer op 37), kamers en put binnen hun kolom, zonder-Gloop-laag zonder Gloop of hoed. GEMETEN: randverschil per kolom 1,8 tot 2,3 op 255 (eerst 4 tot 9, door het verloop van de fakkels; zonder egale lamp was het stuk ook veel te donker, helderheid 24 tegen ±55 nu).
- Eerlijk: het rustige stuk is vlak, met opzet; het spel tekent er zelf fakkels en gloed overheen. Op het blad voor Thijs laat ik het hele hol zien, niet de tegels.

## Ronde 4 (13 nov ±18:00 UTC): het verhaal in beeld
Punt 4 en 5 van hieronder. Daans `held.py` als module: een ridder (stap1) loopt van de ladder naar de put, een heks valt er kop eerst in (stand vallen). Alles heet `held_...`, dus `HOL_VERBERG ["held"]` geeft het hol zonder helden voor de tegels; `HOL_HELDEN=0` laat ze helemaal weg. De stekels steken nu boven de vloer uit (zoals hol.gd de put tekent, 8 spelpixels vanaf de vloer), lichter staal, put 1,55 breed in kolom 4.
- `ronde4-ware-grootte.png`, `ronde4-2x.png`, `ronde4-blad.png` (met Rusty's erboven).
- GEZIEN met Read: op ware grootte lezen de ridder (helm, blauw) en de witte stekels; de heks leest als een figuurtje dat valt of springt boven de put.
- Frisse kijker (alleen ware grootte), samengevat: "een ridder loopt naar rechts, een oranje figuurtje springt boven een rij witte pinnen (een val), een gekroond eenogig slijm op een berg goud". Spel volgens hem: "jij bent een gekroond slijmmonster dat zijn schat verdedigt tegen avonturiers, met vallen". Dat klopt met het spel (ronde 2: "ik zie niet wat het spel is"). Niet gelezen: de ronde kamers boven de gang, wat de helden precies doen (te klein). Stoppen met scrollen nog 6 van 10: "donker en klein, geen duidelijke actie of titel".
- Eerlijk: het rustige stuk rechts (egale lamp voor de tegels) is lichter en vlakker dan de rest; voor het blad voor Thijs wil ik daar nog wat sfeer terug zonder de naad te breken.

## Volgende ronde
- Het moment groter maken: Gloop die grijnst of kijkt naar de vallende heks (vraag Daan, zijn gloop.py), de heks en de put iets dichter bij de kamer zodat het oog van Gloop naar de val gaat. Titel of logo hoort op de capsule, niet in de strook.
- Ronde kamers boven de gang laten lezen als kamers (iets erin: een bed of een kist, alleen als het in het spel zit).

## Oude lijst
1. (gedaan in ronde 2) Gloop kan niet groter (ware maat in het spel), dus de kamer rond hem rustiger en lichter: geen kiezels binnen een halve kamer om de boog, warme gloed achter hem, achterwand van de kamer een trede lichter. Hij moet het lichtste vlak van de strook zijn.
2. (gedaan in ronde 2) Gloop op de rand van de berg in plaats van ernaast.
3. De gang breken: een bocht of trapje, en meer kleine dingen die over de dag veranderen (munten op de vloer).
4. Stekelput leesbaar: breder, stekels lichter, de helm groter en zichtbaar op de rand. Spinrag weg of groter.
5. Een held in de gang (vraag aan Daan: heeft hij al een 3D-held, anders een eenvoudige stand-in die eerlijk is).
6. Daarna drie versies op het blad voor Thijs (`ontwerp/steam/hol-3d-blad-voor-thijs.png`, ma 16 nov), opnieuw een frisse kijker.
