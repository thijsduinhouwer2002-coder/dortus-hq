# Rolsteen en edelman: hoe ze eruitzien (Daan, 17 nov 2026 ±00:30 UTC)

Wat ze doen staat bij Sanne in `platformen/steam/features.md`, blok "De rolsteen en de edelman". Hier staat alleen het uiterlijk. Bouw pas na de speeltest van za 21 nov (Olaf beslist de volgorde). Mila maakt de modellen in de vaste 3D-stijl (`ontwerp/steam/3d-stijl.md`: één camera, één licht, rond speelgoed), keuring Daan op ware grootte in een echte opname van 1920.

## De edelman: herken hem aan één ding, de witte hoge hoed

**Waarom zo:** er bestaat al een hoge hoed (`hoeden.py` nr 7, antraciet met rode band) die elke held kan dragen. Is de hoed van de edelman ook donker, dan ziet niemand op de toren dat dit de zeldzaamste hoed is. Een **ivoren zijden hoge hoed** is het enige lichte, hóge silhouet in het spel (de koksmuts nr 5 is ook licht, maar laag en bol; de brede gouden band maakt het verschil af): op het pruimen hol en bovenop de toren zie je hem in één oogopslag, en hij verschilt van nr 7 als dag en nacht.

**De hoed (nieuw nummer in `hoeden.py`, naam `edelhoed`, alleen voor de edelman):**
- Ivoor `f3ead6`, zacht glanzend (rough 0,3, spec 0,6), zodat het fakkellicht er een lange streep op legt: zijde, geen vilt.
- 30 procent hoger dan nr 7 (koker 0,86 in plaats van 0,66) en iets getailleerd (onder 0,31, midden 0,29, boven 0,34). Brede rand 0,55 die aan de zijkanten licht omhoog krult.
- **Brede** band van goud (`goud`, metaal, hoogte 0,18, bijna een kwart van de koker), zodat hij op de toren nooit voor de koksmuts doorgaat, met vooraan één klein wijnrood rozetje (`8e2a4a`). Geen veer: de hoogte is het pronkstuk, een veer maakt hem druk.
- Op de toren: altijd bovenop (Sanne), 5 graden scheef, nooit gedeukt of met een hap. Eén keer per ±20 s loopt er één glinster over de band (één beeld, 0,4 s). Dat is de enige beweging; de toren staat verder stil, dus CPU blijft laag.

**Het lijf (`held_soorten.py`, soort `edelman`):**
- Lange slipjas in **wijnrood fluweel** (licht `a83a5a`, donker `7a2444`) met een **gouden bies** langs de voorkant en de slippen. Geen van de andere heldkleuren: de rode held is helder oranjerood (`ee6a4f`), dit is roze-wijnrood. Eerst stond hier donker `5a1630`: de controleur zag terecht dat die op het pruimen hol wegvalt en dan zweven hoed en hoofd los. Twee slippen achter die bij elke stap meezwaaien (het tweede silhouet naast de hoed).
- Wit kanten jabot onder de kin (`f6efe2`, drie bolletjes onder elkaar) en witte handschoenen: licht naast licht maakt het hoofd met hoed één heldere vorm op ooghoogte.
- Gouden knopen (3), een wandelstok met een gouden knop in de rechterhand.
- Gezicht: zelfde grote ogen als alle helden, **ooglid half dicht** (verveeld, neus omhoog) en een gouden monocle om het rechteroog. De monocle zie je pas op 3x; op 1x doen hoed, jas en stok het werk.
- Haar: grijs kortgeknipt met een keurige scheiding (`b8b0b8`), zodat hij zonder hoed (na Gloop) nog deftig is.
- Lengte: lijf even groot als de andere helden; alleen de hoed steekt erboven uit. Totaal hooguit 1,25 maal de ridder met helm, zodat hij in de gang past. **Toets:** past hij op 120 px niet onder het plafond van de gang, dan zakt de hoed naar 1,15 en niet het lijf.

**Standen (zelfde reeks als de andere helden, plus twee):**
- `wacht`: staat bij de ingang, stok voor zich, beide handen op de knop, kijkt opzij naar de deur. Elke ±3 s tikt de stok één keer (één beeld).
- `na_u` (als de voorloper komt): linkerarm maakt een zwaai naar voren, kleine buiging. Twee beelden, één keer. Dit is de grap; die moet zonder tekst lezen.
- Lopen: rechtop, kin omhoog, korte stappen, stok tikt mee.
- Om de val heen: in plaats van een rare sprong loopt hij op zijn tenen een bocht, armen omhoog (één beeld `tenen`), hoed blijft recht.
- Alleen en zenuwachtig: houdt met één hand de hoed vast, ogen opzij. Dit is ook het teken voor de speler: "x 1,2".
- Schrik en vallen: zoals de andere helden, en de hoed vliegt los en blijft even hangen.

## De rolsteen: een steen die je aan ziet dat hij gaat rollen

**Waarom zo:** de steen moet in rust al zeggen "ik ga rollen" en de speler moet zonder klok zien of hij klaar ligt (Sanne). Dat doen we met waar hij ligt, niet met een balkje.

- **Vorm:** bijna bol, iets platgedrukt (1 : 0,92), twee schilfers eraf en een **ingekerfde donkere band rondom** (een groef, `6e6860`, met een lichte rand `d8d0c0` erlangs). De band is de truc: als hij rolt zie je de band draaien, zonder band ziet een rollende bol eruit als een schuivende bol.
- **Kleur:** koel lichtgrijs `a8a39c` met warme bovenkant van de fakkel, groef `6e6860` met lichte rand `d8d0c0` (alleen licht op grijs zag je op 40 px niet draaien, punt controleur), een vlek mos `6f8f4a` op de bovenkant. Lichter en grijzer dan de roze-bruine aarde en de steentjes in de wand, zodat hij er niet in wegvalt. Geen gezicht (het is een val, geen figuurtje).
- **Maat:** doorsnee 0,9 maal de hoogte van een held zonder hoed. Groter dan een held is net de grap (de held kijkt op), maar hij moet in de gang passen.
- **Klaar:** ligt boven aan het eind van de gang op een **houten wig met een touwtje** ervoor (Mila's helling-randje). Steen op de wig = klaar. Het belangrijkste teken is aan welk eind hij ligt; de wig maakt het af.
- **Rollen (±2 s):** de band draait (12 beelden per omwenteling is genoeg), een stofwolkje per cel achter hem, bij elke geraakte held een korte schok (1 beeld, de steen wipt 1 spelpixel). Tegen de ridder: één witte vonk en de steen kaatst een halve cel terug ("Clang.").
- **Na het rollen:** ligt aan het andere eind **zonder wig, tegen de wand, iets gekanteld** zodat de mosvlek opzij ligt. Zo zie je in één blik: niet klaar. Rolt hij terug (een held springt eroverheen), dan rustig, zonder stof, en de mosvlek komt weer boven.
- **CPU:** alleen beweging tijdens rollen en terugrollen; in rust één vast plaatje (twee: klaar en niet klaar).

## Toets voor de keuring (Daan, ware grootte 1920)
1. Een frisse kijker krijgt alleen de strook met de edelman tussen drie andere helden en zegt uit zichzelf iets als "die met de hoge hoed is rijk / deftig".
2. Op de toren is de witte hoed op 1x het eerste wat je ziet.
3. Een frisse kijker ziet het verschil tussen steen klaar en steen niet klaar zonder uitleg (twee plaatjes naast elkaar).
4. In een reeks van 6 beelden tijdens het rollen zie je dat hij rolt (de band draait), niet schuift.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## Schets in 3D (Daan, 17 nov ±00:34 UTC)
`proef.py` hiernaast (bpy 5.3, draait in ±12 s), uit: `schets-hoeden-steen.png` (koksmuts nr 5, hoge hoed nr 7, edelhoed, steen klaar, steen niet klaar, op het pruimen hol) en `schets-spelmaat-4x.png` (spelmaat, 4x vergroot).
- **Edelhoed: GEZIEN, werkt.** Naast nr 7 als dag en nacht, en door hoogte en brede gouden band nooit te verwarren met de koksmuts, ook op spelmaat. Opgekrulde flapjes aan de rand geprobeerd: lazen als handvatten, weg. Mila mag deze maten zo overnemen in `hoeden.py`.
- **Rolsteen: nog niet goed, dat is werk voor het echte model.** Drie rondes: een gladde bol leest als ei of bal, bultjes als schilfers lezen als wratten, een torus als band steekt uit als een touw of een ring om een planeet. Wat het model nodig heeft: een bultige vorm (bol met ruis verplaatst, geen perfecte bol), de band als echte groef erin gesneden (boolean), schilfers als platte afgeslagen vlakken. Kleur `8e8a86` (koeler dan `a8a39c`) is beter onder de fakkel. Wig: leest als oranje driehoekje, mag donkerder hout.

## Schets edelman tussen andere helden (Daan, 17 nov ±00:36 UTC)
`schets_edelman.py` (lijf van de gewone held, jas wijnrood `a83a5a`/`7a2444`, jabot, drie gouden knopen, stok, edelhoed), uit: `schets-edelman.png` en `schets-edelman-spelmaat-4x.png` (ridder, dief met koksmuts, edelman, held met hoge hoed nr 7).
- **GEZIEN op spelmaat: werkt.** De edelman is in één blik "de rijke": witte hoge hoed met goud, jabot, stok. De wijnrode jas valt niet weg op het hol en is te onderscheiden van de oranjerode held. Hij heeft iets van een circusdirecteur; dat is goed, het is een grappig figuur.
- **Voor het echte model (Mila):** hoed op het lijf op 0,9 van de maat in `proef.py` (in de schets steekt hij boven het kader uit; regel blijft totaal hooguit 1,25 maal de ridder); gouden bies echt op de jasrand (een losse ring zweefde als hoepel, weggehaald); slippen achter en ooglid half dicht ontbreken nog in de schets en maken hem pas deftig in plaats van vrolijk; geen lantaarn en tas (in de schets verborgen).

## Edelhoed in het echte model (Mila, 17 nov ±01:05 UTC)
- Op tak `claude/steam-edelman` (niet op main: bouwen pas na de speeltest van 21 nov, Olaf beslist): **nr 10 `edelhoed` in `hoeden.py`** met Daans maten (koker 0,86, getailleerd 0,31/0,29/0,34, rand 0,55, brede gouden band 0,18, wijnrood rozetje), plus een iets lichtere bovenkant en een dun donker biesje onder de band, zodat het goud niet in het ivoor overloopt. Gewone helden krijgen nog steeds 0 tot 9 (`hoedenwand.py` rekent al met % 10). In `pijplijn/sprites.json` een beeld `edelhoed` in blad `hoeden`, **niet** in `hoeden_hap` (nooit een hap). Het blad is daardoor 3 bladpixels hoger (cel 63 x 49); `kruin` en `nul_y` staan per beeld in `kunst/3d/sprites.json`, dus de toren hoort gewoon te blijven staan. Toets dat in de echte run.
- Proef op de toren, in de echte opname van 1920 (`strook-10min.png`, spel op 3x): `mila-toren-voor-na.png` (links de toren zoals nu: kroon, nr 7, koksmuts; rechts kroon, nr 7, edelhoed 5 graden scheef; boven 3x, onder ware grootte) en `mila-toren-edelhoed-1x.png`. Script `mila_toren_proef.py`. Eerlijk: de rechthoek wand achter de toren is geplakt om de oude toren weg te halen, dat is de proef, niet het spel.
- **GEZIEN met Read op 1x en 3x:** de edelhoed is op ware grootte het eerste wat je op de toren ziet (het enige lichte hoge ding, het goud vangt licht), en hij is nooit de koksmuts: die is laag en bol, de edelhoed hoog met een gouden band. Toets 2 van Daan: ja voor mij.
- Alle 11 naast elkaar: `mila-hoeden-11.png`.
- Nog te doen: lijf `edelman` in `held_soorten.py` (slippen, ooglid half dicht, bies op de jasrand) en de rolsteen als echt model (bultige bol, groef als boolean, schilfers als platte vlakken, wig donkerder hout).

## Rolsteen proef 1 als echt model (Mila, 17 nov ±01:18 UTC)
- `producten/steam-hol/modellen/rolsteen.py` op tak `claude/steam-edelman` (nog niet in de pijplijn). Bultige bol (ruis op de vorm, 1 : 0,92), de groef als echte inkeping met donker `5e5850` en een lichte rand, twee platte afgeslagen vlakken, mos bovenop, wig donker hout `5e3b22` met touwtje. Standen `klaar`, `niet_klaar`, `rol` (met draai in graden).
- Eerst met een icosfeer: GEZIEN, de groef werd een zaagtand. Nu een bol met zijn polen op de groefas, dan loopt de band strak.
- `mila-rolsteen-proef1.png` (klaar, niet klaar, rollend 45 graden). **GEZIEN met Read:** leest nu als steen, niet als bal of ei, en de groef is een scherpe kerf die je ziet staan. Eerlijk nog niet goed: de afgeslagen vlakken lezen als lichte lappen, de lichte rand zie je maar aan één kant, en niet klaar (rechtop gekanteld) heeft iets van een walnoot. Volgende run: vlakken kleiner en donkerder, rand aan beide kanten, de 6 rolbeelden op spelmaat in de echte opname (toets 3 en 4).

## Rolsteen proef 2 en de toets op spelmaat (Mila, 17 nov ±01:50 UTC)
Daans moets van 01:30, op volgorde (tak `claude/steam-edelman`, `modellen/rolsteen.py`):
- (a) Basis `6a6764` (neutraal) in plaats van `8e8a86`: het gedeelde licht (warme fakkel, koel tegenlicht) tilde 8e8a86 op naar blauwig `bbb9ca`. **Nagemeten in de render:** lichte kant `928783` en `938a8b`, schaduwkant `645d5d`. Dat valt in Daans `8e8a86` tot `a8a39c`. De fakkelkant van de rollende steen is warmer (`ad937c`), dat is het licht en hoort zo.
- (b) Afgeslagen vlakken: zelfde grijs een stap donkerder (`5a5754`), nagemeten `807062` en `6f6d79`, geen beige meer. De kleur zit nu per hoekpunt met een zacht verloop (een kleurlaag), niet per vlak: per vlak gaf kartelranden rond vlakken en mos. Vlakken ook iets kleiner.
- (c) Lichte rand langs de groef helemaal weg. De groef zelf donkerder (`2e2a26`), zodat hij op 28 px nog leest.
- (d) Groef ondiep (0,016 in plaats van 0,045) en smaller: geen twee opbollende helften meer, één bultige vorm met een kerf erin.
- (e) Mos donkerder (basis `3c5228`, nagemeten `638457`) en kleiner.
- (f) Toets op spelmaat in de echte opname (`strook-10min.png` van de koper-duurtest, spel op 3x; held zonder hoed is daar 31 px, steen 0,9 daarvan = 28 px): `mila-rolsteen-spelmaat-4x.png` (klaar en niet klaar op dezelfde plek bij de spijkers, boven 4x, onder ware grootte) en `mila-rolsteen-gang-1x.png` (hele gang op ware grootte: niet klaar links tegen de wand, klaar rechts bij de val). Script `mila_rolsteen_spelmaat.py`. Eerlijk: de steen is geplakt op de opname, dat is de proef, niet het spel.
- Bij de toets twee dingen bijgesteld, GEZIEN: **niet klaar** stond rechtop (75 graden) en las op spelmaat weer als ei of walnoot; nu 32 graden gekanteld, groef schuin, breed op de vloer. **Wig** `5e3b22` viel weg in de bruine gangwand; nu `7a4a26` en 30 procent groter. Touwtje donkerder (`6a4e2c`); op spelmaat zie je het niet, dat mag.
- **GEZIEN met Read, op 4x en ware grootte:** het is een grijze steen, geen bal of ei, en hij valt niet weg in de roze-bruine aarde. Klaar en niet klaar zijn naast elkaar te onderscheiden aan drie dingen: wig ja of nee, groef recht of schuin, mos boven of opzij. Eerlijk: op ware grootte is de wig een klein bruin driehoekje en het mos een paar pixels, het grootste teken blijft aan welk eind van de gang hij ligt (zoals Daans ontwerp zegt). Toets 4 (6 rolbeelden) doe ik na Daans ja op deze stand.
- `mila-rolsteen-proef2.png`: klaar, niet klaar, rollend 45 graden op groot formaat.

## Edelhoed: rand onder donkerder (Mila, 17 nov ±01:50 UTC)
Daans kan-punt: de onderste helft van de rand is nu een eigen schijf `7a6e60`, vlak gearceerd (glad mengde hem weg). Op groot formaat een duidelijke schaduwlijn onder de ivoren rand. Het blad `hoeden` rendert de pijplijn opnieuw na deze commit.

## Edelman proef 1 als echt model (Mila, 17 nov ±02:05 UTC)
- `held_soorten.py` soort `edelman` (tak `claude/steam-edelman`, nog niet in de pijplijn): jas wijnrood `a83a5a`/`7a2444` (fluweel, iets meer glans dan de tuniek), grijs haar `b8b0b8`, witte handschoenen, kanten jabot (drie bolletjes), drie gouden knopen, gouden bies op de jasrand (geen losse ring), twee slippen achter die bij `stap1`/`stap2` meezwaaien en bij vallen opwaaien, wandelstok tot op de vloer met gouden knop (vliegt weg bij schrik en vallen). Nieuw haakje `gezicht()`: ooglid half dicht met donker randje en een gouden monocle met kettinkje om het rechteroog. In `held.py` alleen twee kleine haakjes (gezicht en witte handschoenen); de andere helden veranderen niet.
- `mila_edelman.py`: strook ridder, dief met koksmuts, edelman met edelhoed op 0,9, held met nr 7 (Daans opstelling). `mila-edelman-proef1.png` (rust), `-stap1.png`, `mila-edelman-spelmaat-4x.png` (spelmaat: held zonder hoed 31 px zoals in de echte opname, op de gangvloer geplakt, boven 4x, onder ware grootte).
- **GEZIEN met Read:** groot leest hij in één blik als de deftige rijke: witte hoge hoed met goud, monocle, jabot, knopen, stok, en het grijze haar maakt hem ouder dan de rest. Op spelmaat: hoed, wijnrode jas en het witte jabot doen het werk, de monocle is een goudpuntje, en hij is niet te verwarren met de oranjerode held ernaast. Eerlijk: de slippen zie je alleen in de stap (in rust staan ze achter het lijf), de bies eerst te lang (stak onder de jas uit als een stokje), ingekort. Nog niet gedaan: de standen `wacht`, `na_u`, `tenen` en de hand op de hoed; eerst Daans ja op het lijf.
