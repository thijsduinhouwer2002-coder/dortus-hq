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

## Ronde 5 (13 nov ±20:45 tot 21:05 UTC): tegels voor het spel kloppen (Bram 18:30, Daan moet 1 en 3)
Alleen in `hol.py`:
1. **Schatkamer 48 breed**, precies kolom 6 tot 9 (spelpixel 96 tot 144), zoals de schatkamer in het spel. Kist, berg, beker en fakkels mee naar binnen.
2. **Kamers boven de gang als één kamer** (voorstel Daan, `ontwerp/steam/kamer-3d/`): kolom 2 begin (fakkel laag), 3 midden a (stut met schoren), 4 midden b (houweel en ton), 5 eind (kistje), 11 los (twee lichtgevende zwammen). Ovaal 14 breed. Hout donkerder en minder oranje. Alles in één render.
3. **Eén licht over de hele aarde** (moet 1): de egale lamp van het rustige stuk loopt over de hele breedte met dezelfde sterkte per vlak. De aarde boven de kamers is nu even licht als de aardtegel; de linker gang is ook lichter.
4. Twee witte sikkels op de rechterwand van de kamers weg: de lamp van binnen stak in de aarde, en Gloops koele licht stond na het smaller maken naast de brede kamer (nu in de schatkamer).
- `ronde5-ware-grootte.png`, `ronde5-2x.png` (met Gloop en helden), `ronde5-tegellaag-960.png` (zonder, zoals de pijplijn), `ronde5-kamertegels-toets.png` (2, 3 en 6 cellen, los en aarde, uit de render geknipt zoals het spel ze legt).
- GEZIEN met Read: geen naad in de kamertoets, de aarde is overal één tint, geen sikkels meer.
- Eerlijk: de schatkamer is nu krap; Gloop staat voor de kist en de helft van de berg. In het spel tekent het spel Gloop zelf. Voor het blad voor Thijs wil ik Gloop een stukje naar links en de berg rechts hoger, zodat goud links en rechts van hem te zien is.

## Ronde 5b (13 nov ±20:55 UTC): concept van het blad voor Thijs
- Gloop 0,25 naar links, kist smaller en verder naar links: de berg is nu rechts van hem te zien.
- Eerst drie versies met meer of minder licht op de aarde (`HOL_TEGEL_LICHT` 200, 300, 420). Frisse kijker 1: "op ware grootte zie ik bijna geen verschil", alle drie een 5. Les: licht is hier niet de knop; drie lichtversies tonen heeft geen zin. Zijn punt: "de helden staan ver van het monster, er gebeurt niets".
- Daarom staat de ridder nu bij de kist en schrikt hij van Gloop (stand `schrik`, kijkt naar Gloop, schaal 0,85). Eerlijk: in het spel lopen helden naar de schat en eet Gloop ze op. `ronde5b-moment-ware-grootte.png`, `ronde5b-moment-2x.png`.
- Frisse kijker 2 (nieuw, alleen dit beeld): herkent slijm met kroon op goud, ridder voor de schatkamer, stekels, ladder; spel volgens hem "bewaak je schat tegen helden, Dungeon Keeper maar schattig" (klopt). Nog steeds 5 van 10: "een mooi stilleven, geen moment met spanning; figuurtjes piepklein; weinig contrast tussen gang en aarde". Het oranje figuurtje bij de put leest niet als vallen.
- Daarna Gloop in de stand `hap` (mond wijd open, Daans `gloop.py`; `HOL_GLOOP_STAND` kiest, standaard hap). GEZIEN: op 2x leest het als happen, op ware grootte is het verschil klein; de mond kijkt naar ons, niet naar de ridder. Beelden overschreven met deze versie.
- Concept: `ontwerp/steam/hol-3d-blad-voor-thijs.png` (Rusty's, versie 1 met het moment, versie 2 ridder in de gang). Nog niet op de lijst van Thijs.

## Ronde 6 (13 nov ±23:40 tot 23:50 UTC): moet 1 van Daan, de aarde overal één licht
Tak `claude/steam-hol-naad` (bovenop Daans `claude/steam-hol-fakkel`, dus met zijn nieuwe fakkels). Alleen in `hol.py`. Twee oorzaken gevonden door te meten (helderheid 0,21 R + 0,72 G + 0,07 B, mediaan van de aarde op spelpixel 10 tot 12 per kolom, 960 x 160 zonder Gloop en helden):
1. **De gedeelde lampen** van `gedeeld.licht()` (fakkel, koel, boven, vul) staan voor Gloop in het midden en vielen als een grote vlek op de voorkant van de aarde: kolom 0 tot 14 was 42, 42, 45, 52, 59, 66, 72, 79, 85, 83, 71, 58, 51, 51, 49. Nu schijnen die vier en de lampjes van de helden alleen op Gloop, helden en schat (light linking in Cycles, collectie `figuren`). De aarde krijgt alleen de egale tegellamp, die nu 40 breder is dan het beeld (aan de randen liep hij nog iets af).
2. **De ruis in de aarde ging niet rond per kolom.** De knoop gebruikte "Object", en dat is de geschaalde blokruimte (x van -0,5 tot 0,5 over het hele hol), dus de vlekken liepen als één trage golf van donker links naar licht in het midden. Dat zag ik pas toen er met alleen de tegellamp nog een helling van 42 naar 49 overbleef, ook met alle sprietjes, kiezels en fakkels verborgen. Nu komt x uit de wereldpositie en gaat het patroon echt rond met een periode van 16 spelpixels.
3. Kan (a) van Daan: de kamervloer begint 0,2 achter de voorkant, het donkere plankje onder de kamers is weg.
4. Het overhangende gras langs de rand ligt overal in het patroon van kolom 14 (4 per kolom). Dat bleek niet de oorzaak, maar het is wel eerlijker naar het spel, dat overal de grastegel van kolom 14 legt.
- Na: kolom 0 tot 14 is 48,0 / 43,8 (de schacht) / 48,0 / 48,0 / 48,0 / 48,0 / 48,7 / 48,9 / 49,9 / 49,0 / 49,0 / 48,0 / 48,7 / 48,0 / 48,7. Zonder de schacht: hoogstens 1,9 verschil.
- Kamertoets zoals het spel legt (aarde 14, begin 2, midden a 3, midden b 4, a, b, eind 5, aarde, los 11, aarde, aarde), naad in de bovenste strook: voor 4,4 / 0,3 / 0,1 / 15,4 / 0,1 / 0,5 / 19,6 / 12,1 / 4,5 / 0,6, na 1,4 / 1,8 / 1,7 / 1,9 / 1,7 / 1,5 / 1,4 / 1,3 / 1,3 / 1,4. Doel was onder 3.
- `ronde6-2x.png`, `ronde6-ware-grootte.png` (met Gloop, helden, Daans fakkels), `ronde6-kamertegels-toets.png`, `ronde6-naden-voor-na-versterkt.png` (boven voor, midden na, beide 4 keer versterkt rond 48; onder de toets gewoon).
- GEZIEN met Read: geen lichtere blokken meer rond de kamers, geen plankje, de aarde heeft nu zichtbare vlekken (pruim met lagen) in plaats van een glad verloop. Gloop, ridder en goud zijn even licht als in ronde 5b, het gras in het midden iets minder fel (de vlek van de gedeelde lampen viel er ook op).
- Eerlijk: het vlekpatroon herhaalt nu elke kolom; op 2x zie je het als je zoekt, op ware grootte niet. In het spel was dat al zo (overal de aardtegel van kolom 14).
- Nagemeten in het echte blad van de pijplijn (`godot/kunst/3d/hol_proef.png`, Action-commit 6349111 op deze tak, gerenderd van ronde 6), zelfde maat als Daan (aarde in de bovenste strook van elk vak): aarde 47,8, kamer_begin, midden_a, midden_b, eind en los allemaal 47,7. Was 60 / 60 / 64 / 70 / 77 / 71.
- Kan voor Bram en Daan: de vlam van de gangfakkel links (kolom 3) begint precies op spelpixel 24. In de laag `boven` zit hij dus op de onderrand van `kamer_midden_a`; met de doorgetrokken rand van 4 bladpixels kan daar een oranje stipje komen. Was voor de nieuwe fakkel ook al zo (gemeten, zelfde rij).

## Ronde 6b (13 nov ±23:55 UTC): gang een trede lichter dan de aarde (volgende ronde punt 2)
Frisse kijker 5b: "weinig contrast tussen gang en aarde". Gemeten: de achterwand van de gang lag in de schaduw van het plafond en was donkerder dan de aarde (37 tegen 48). Nu een lange warme lamp in de gang (`ganglicht`), naar achteren gericht, alleen op achterwand en vloer (light linking), even lang als de tegellamp, dus egaal in x. `HOL_GANG_LICHT` (standaard 60, 0 is uit).
- Drie sterktes naast elkaar: `ronde6b-gang-licht-0-60-120.png`. Gang op spelpixel 27 tot 33 in kolom 13 en 14: 37 / 56 / 70. Gekozen 60: de gang leest als een verlichte tunnel en de poelen van de fakkels blijven zichtbaar; bij 120 verdwijnen die en wordt het vlak.
- Naden in de kamertoets daarna nog hoogstens 2,4, gang tegen gang egaal (55 tot 57).
- `ronde6b-gang-2x.png`, `ronde6b-gang-ware-grootte.png`. GEZIEN met Read: de heks en de stekels staan nu tegen een lichtere gang, de aarde is een duidelijk donkerder vlak eromheen.

## Ronde 6c (14 nov ±00:00 UTC): de hoed van de heks blijft boven de put hangen (volgende ronde punt 3)
Daan (21:45, kan c): de hoed die los boven de put hangt vertelt de val beter dan de houding, en zo doet het spel het ook (`held_beeld.gd`). De heksenhoed op haar hoofd is weg; de puntmuts uit `hoeden.py` hangt scheef (28 graden) rechts naast haar, boven de put. Alles heet `held_...`, dus de tegels hebben hem niet: de laag zonder helden is gelijk aan 6b (grootste verschil 1 op 255). `HOL_HOED_LOS=0` zet hem terug op haar hoofd.
- `ronde6c-hoed-2x.png`, `ronde6c-hoed-ware-grootte.png`, `ronde6c-hoed-put-6x.png`.
- GEZIEN met Read: op 6x leest het als "de hoed vliegt eraf, zij valt kop eerst". Op ware grootte is het een paars vlekje naast een oranje figuurtje; beter dan een figuurtje alleen, nog geen schreeuw.

- Frisse kijker (nieuw, alleen `ronde6c-hoed-ware-grootte.png`): herkent ladder, kamer met stut, houweel, ton en kistje, heks boven de stekels, ridder met pluim, slijm met kroon en open mond op goud, beker, zwammennis, spinnenweb. Spel volgens hem: "slijmkoning beschermt zijn schat tegen helden, Dungeon Keeper maar lief" (klopt). Bij de stekels: "figuurtje staat in de stekels, geen schrik, geen beweging"; de losse hoed noemt hij niet als val. 6 van 10 (was 5): "de slijm met kroon en goud valt meteen op en is grappig, de rest te klein en er gebeurt niets duidelijks". Zijn ene tip: maak het stekelmoment groot en duidelijk (een au-houding, een sterretje) en dichter bij de slijm.
- Les: de hoed alleen is op 120 px te klein om de val te vertellen. Volgende stap voor punt 3: een held die op de rand van de put wankelt met armen omhoog (stand `schrik` bestaat), of de val laten zien met een klein stofwolkje of sterretjes, alleen als het spel dat ook tekent (navragen bij Bram of `held_beeld.gd` zoiets heeft).

## Ronde 7 (14 nov ±02:40 tot 03:05 UTC): put gelijk aan de gang, wand vlak per tegel, hoed weer op (Daan 00:40)
1. **Moet, put-cel:** de lichte roze vlek met harde linkerrand in de put-tegel was de poel van de gangfakkel links (x -7,2, kolom 3), die vlak naast kolom 4 brandt, waar de pijplijn de put uitknipt. In het spel ligt de put tussen gangtegels zonder poel, dus werd de rand een blok. De twee gangfakkels schijnen nu alleen op de figuren (light linking, zoals de gedeelde lampen); het spel tekent zijn eigen fakkels. `HOL_FAKKEL_POEL=1` geeft de poelen terug, alleen voor een sfeerplaatje, nooit voor de tegels.
   - GEMETEN in de laag `vol` (960 x 160, 24 samples, zoals de pijplijn), achterwand van de gang op spelpixel 27 tot 33, per 2 spelpixels: kolom 4 was 77 73 69 68 65 65 63 62, nu 60 60 59 60 59 60 59 59. Kolom 14: 59 overal.
2. **Kan, trede per gangtegel:** in kolom 14 liep de wand van 60 naar 62. De platen (aarde, achterwand, vloer, gras, gang rechts) hielden 0,5 voorbij het beeld op; door het open einde viel er licht binnen. Ze lopen nu 6 eenheden door (`XP0`, `XP1`). Kiezels en sprieten houden hun plek (zelfde reeks). Nu kolom 13 en 14 allebei 59 van rand tot rand.
3. **Heksenhoed terug op haar hoofd** (`HOL_HOED_LOS` staat standaard op 0; 1 hangt hem weer los). Daans reden klopt: zonder hoed geen heks, en het wegvliegen tekent het spel zelf.
- Aarde ongewijzigd (kolom 0, 1, 10, 12 tot 14: 48 tot 50).
- `ronde7-2x.png`, `ronde7-ware-grootte.png`, `ronde7-tegels-gang-put-gang-3x.png` (gang, gang, put, gang, gang, gang zoals het spel ze legt), `ronde7-heks-hoed-op-8x.png`.
- GEZIEN met Read: in de tegeltoets zie je geen rand meer tussen put en gang, alleen de stekels. De heks hangt kop omlaag met de paarse punthoed op haar hoofd; het rode haar en het gezicht lezen. Eerlijk: zonder de poelen is de gang rond de fakkels vlakker dan in ronde 6. Dat is hoe het spel hem tekent, dus het blad en de strook zijn nu eerlijker.
- Gezien maar niet van mij: de laarzen en rok van de vallende heks steken in het plafond van de gang (8x). Hangt af van de stand `vallen` in Daans `held.py` en haar hoogte; kan ik oplossen door haar plek 0,1 lager te zetten, maar dan zakt haar hoofd in de stekels. Gevraagd aan Daan.

## Volgende ronde (voor ma 16 nov)
1. Spanning in één stilstaand beeld: Gloop met open mond (hap) naar de ridder, of munten die van de berg vliegen; vraag Daan of `gloop.py` een hapstand heeft (in het spel bestaat hap al: `slijm.gd`).
2. (gedaan in ronde 6b) Contrast gang tegen aarde: gangvloer en achterwand een trede lichter en warmer, de aarde blijft. Geldt ook voor de tegels, dus samen met Bram.
3. (eerste stap in ronde 6c, hoed los) De heks moet lezen als vallen: kop naar beneden duidelijker, of een held die net op de rand wankelt.
4. Daarna opnieuw een frisse kijker; doel 7.

## Oudere lijst van ronde 4
- Het moment groter maken: Gloop die grijnst of kijkt naar de vallende heks (vraag Daan, zijn gloop.py), de heks en de put iets dichter bij de kamer zodat het oog van Gloop naar de val gaat. Titel of logo hoort op de capsule, niet in de strook.
- Ronde kamers boven de gang laten lezen als kamers (iets erin: een bed of een kist, alleen als het in het spel zit).

## Oude lijst
1. (gedaan in ronde 2) Gloop kan niet groter (ware maat in het spel), dus de kamer rond hem rustiger en lichter: geen kiezels binnen een halve kamer om de boog, warme gloed achter hem, achterwand van de kamer een trede lichter. Hij moet het lichtste vlak van de strook zijn.
2. (gedaan in ronde 2) Gloop op de rand van de berg in plaats van ernaast.
3. De gang breken: een bocht of trapje, en meer kleine dingen die over de dag veranderen (munten op de vloer).
4. Stekelput leesbaar: breder, stekels lichter, de helm groter en zichtbaar op de rand. Spinrag weg of groter.
5. Een held in de gang (vraag aan Daan: heeft hij al een 3D-held, anders een eenvoudige stand-in die eerlijk is).
6. Daarna drie versies op het blad voor Thijs (`ontwerp/steam/hol-3d-blad-voor-thijs.png`, ma 16 nov), opnieuw een frisse kijker.
