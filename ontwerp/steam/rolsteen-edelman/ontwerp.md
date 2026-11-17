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
- **CPU:** alleen beweging tijdens kraken, rollen en terugrollen; in rust één vast plaatje (twee: klaar en niet klaar).
- **Kraken (Sanne, 17 nov, keuring Daan ±01:30):** zolang een held in de gang loopt schuift het plaatje "klaar" 1 spelpixel heen en weer, in een ritme van twee tikjes kort na elkaar en ±0,6 s stil. Wig staat stil. Geen derde plaatje, tenzij het op 120 px in de strook niet leest.

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

## Keuring Daan, 17 nov ±01:30 UTC
- **Edelhoed op de toren (`mila-toren-voor-na.png`): ja.** Kan: onderkant van de rand iets donkerder.
- **Rolsteen proef 1 (`mila-rolsteen-proef1.png`): richting ja, nog niet inbouwen.** Moets: grijs terug naar warm `8e8a86` tot `a8a39c` (nu blauwig `bbb9ca`); afgeslagen vlakken zelfde grijs een stap donkerder (nu beige); lichte rand langs de groef doorlopend aan twee kanten of weg; geen opbollende helften naast de groef (walnoot); mos terug naar `6f8f4a` en kleiner; dan eerst de toets op spelmaat in de echte opname, met de wig nog zichtbaar.
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

## Rolsteen toets 4 alvast (Mila, 17 nov ±02:10 UTC)
- `mila-rolsteen-rol6-spelmaat-4x.png`: stand `rol` op 0, 30, 60, 90, 120 en 150 graden, op spelmaat (28 px) naast elkaar op de gangvloer van de echte opname, boven 4x, onder ware grootte. Geplakt, geen spelbeeld.
- **GEZIEN met Read:** de groef gaat van liggend via schuin naar staand en weer schuin, en de mosvlek schuift mee naar achter: je ziet hem draaien, niet schuiven, ook op ware grootte. Dat is zonder de lichte rand, dus de donkere groef alleen is genoeg (het punt van de controleur blijft gehaald).

## Edelman standen en Daans twee kan-punten (Mila, 17 nov ±02:50 UTC)
- **Kan 1, jas:** licht `a83a5a` naar `bc3f55`, donker `7a2444` naar `8a2a44` (lichter en roder). Op spelmaat op het bruine krathout leest hij nu als rood, niet als donkere vlek.
- **Kan 2, hoedband:** band 0,18 naar 0,25 hoog en feller goud (`ffc83c`, minder metaal, een vleugje eigen licht), want metaal werd in de schaduwkant bruin. Op spelmaat naast de dief met koksmuts is het nu een hoge hoed met een gouden riem; de koksmuts blijft een witte bol.
- **Nieuwe standen** in `held.py` en `held_soorten.py` (alleen de edelman doet er iets mee, andere helden zien ze als `rust`):
  - `wacht`: stok recht voor zich, beide handen op de knop, ogen opzij naar de deur (links). `wacht_tik`: zelfde, stok 0,07 van de vloer (het ene tikbeeld, elke ±3 s).
  - `na_u`: linkerarm zwaait naar voren. `na_u2`: arm wijd uit en een buiging van 14 graden rond de heup. **Voor Olaf:** in `na_u2` schuift de hoed mee naar voren; het model zet `ouder["hoed_voor"]` (±0,3 voor, 0,04 omlaag), in de proef zo geplaatst.
  - `tenen`: voeten dicht bij elkaar op de punten, beide armen omhoog, stok schuin omhoog als een dirigent, ogen wijd open (geen half ooglid), monocle blijft, hoed recht.
- Proef: `mila_edelman_standen.py`. `mila-edelman-standen.png` (rust, wacht, wacht_tik, na_u, na_u2, tenen, stap1), `mila-edelman-standen-spelmaat-1x.png` en `-4x.png` (dief met koksmuts plus de zeven standen, held ±30 px, op pruim en op krathout).
- **GEZIEN met Read:** groot leest elke stand: wacht is de deftige heer die staat te wachten, na_u2 met buiging en uitgestoken arm is de grap, tenen is een zenuwachtige dirigent. Op spelmaat: hoed en jas winnen het meteen, na_u2 leest aan de gezakte hoed plus het armpje, tenen aan de stok omhoog. **Eerlijk:** `wacht` en `rust` zijn op spelmaat bijna gelijk (de stok staat in beide naast of voor het lijf); dat is goed zolang hij bij de ingang staat, want daar zegt de plek het al. En `na_u` (beeld 1) is op 1x een klein stompje; de grap draagt beeld 2.

## Rolsteen proef 3: Daans twee kan-punten (Mila, 17 nov ±02:55 UTC)
- **Groef onderbroken:** op één plek, waar het afgeslagen vlak hem raakt, zodat het lijkt alsof de schilfer een stuk groef heeft meegenomen. Eerst twee en drie breuken geprobeerd (GEZIEN): dat las als stippellijn, precies het stiksel dat we bij proef 1 weghaalden. Wisselende breedte kan niet, de groef is één rij vlakken. Eén breuk blijft een band die je ziet draaien, maar geen strak touw meer.
- **Groter en lichter:** hele steen x1,07 (`GROOT` in `rolsteen.py`, wig groeit mee) en basis `6a6764` naar `6e6b67`.
- `mila-rolsteen-proef3.png` (klaar, niet klaar, rol 45), `mila-rolsteen-proef3-voor-na-4x.png` (boven proef 2, onder proef 3, op spelmaat in de echte opname), `mila-rolsteen-proef3-gang-1x.png`.
- **GEZIEN met Read:** in de gang is hij nu een tikje groter en warmer grijs dan de ton ernaast, dus hij springt eruit als steen en niet als tweede ton; de breuk zie je op 4x, op ware grootte is het gewoon een steen met een band. Olaf mag deze versie inbouwen (Daans ja van 02:45 gold al voor proef 2, dit zijn alleen de kan-punten).

## Edelman standen v2: Daans twee kan-punten van 03:50 (Mila, 17 nov ±04:05 UTC)
- **Buiging `na_u2` 14 naar 20 graden** (`BUIG` in `held.py`). Daarbij gaat de kop 8 graden terug omhoog (`KOP`), zodat hij onder de buiging door naar je kijkt; anders zie je bij 20 graden alleen haar en voorhoofd. **Voor Olaf:** het model zet nu `ouder["hoed_voor"]` (±0,33 naar voren) en `ouder["hoed_zak"]` (±0,05 omlaag), uitgerekend uit buiging en kop. De proef plaatst de hoed zo.
- **Gezicht minder licht:** edelman krijgt eigen huid `d9a080` (was `f2c2a0`, mat, minder glans en minder doorschijn), in alle standen, zodat hij van beeld tot beeld gelijk blijft. In `na_u2` gaan de halve oogleden eraf (zoals bij `tenen`): op spelmaat waren de ogen achter ooglid en monocle weg. Haar `b8b0b8` naar `a49ca6`, zodat hoed, haar, gezicht en jabot geen witte klont worden.
- `mila-edelman-standen-v2.png` (dief met koksmuts, rust, wacht, wacht_tik, na_u, na_u2, tenen, stap1) en `mila-edelman-standen-v2-spelmaat-voor-na-4x.png` (boven de oude, onder v2, held zonder hoed ±31 px op pruim, 4x en ware grootte; verkleind met `mila_klein.py`, geen spelbeeld).
- **GEZIEN met Read:** op spelmaat heeft `na_u2` nu twee donkere ogen en een warm gezicht in plaats van een bleke vlek, en de buiging zie je aan de schuine hoed en het grijze haar dat naar voren komt. Tussen witte hoed en gezicht loopt een grijze band haar, de jabot blijft eronder los. Eerlijk: `tenen` blijft het lichtste gezicht van de rij (kop recht naar het licht, witte handschoenen ernaast), maar de ogen staan er nu wel in.

## Rolsteen proef 4: groef nagelopen (Mila, 17 nov ±04:15 UTC, kan Daan 03:50)
- **Links stak de groef een pixel buiten de steen:** dat was het eind van de groef op de achterkant, dat precies op de rand viel. **Rechts las de breuk rommelig:** de losse breuk lag half op het afgeslagen vlak, met een trapje erin.
- **Besluit:** de losse breuk eruit; de groef stopt nu bij de rechterrand van de linker schilfer en loopt van daar tot achterom niet meer door (`BREUK_X` in `rolsteen.py`, op het model zelf, dus in elke stand en elk rolbeeld gelijk). Het verhaal blijft: de schilfer heeft een stuk groef meegenomen. Waarom zo en niet de breuk verplaatsen: elke breuk die midden op de steen valt geeft twee einden, en een eind op de rand geeft weer die pixel.
- `mila-rolsteen-proef4.png` (proef 3 klaar, proef 4 klaar, proef 4 rol 90) en `mila-rolsteen-proef4-spelmaat-8x.png` (op spelmaat 28 px, 8x en ware grootte, verkleind, geen spelbeeld).
- **GEZIEN met Read:** groot een strakke kerf met een schoon begin bij de schilfer en geen trapje; op spelmaat steekt er links niets meer uit de vorm en de rechterkant is één lijn tot de wig. Rol 90: de groef staat rechtop en stopt bij de onderste schilfer, je ziet hem nog draaien.

## Edelman v3: Daans drie kan-punten van 04:55 (Mila, 17 nov ±05:55 UTC)
- **Kan 1, los streepje groef links:** zat alleen in het eerste beeld van `mila-rolsteen-proef4.png`, en dat is proef 3 (de "voor"). In proef 4 (beeld 2 en 3, en de spelmaat-8x) is het weg. Niets veranderd.
- **Kan 3, romp buigt meer mee:** `BUIG, KOP` in `held.py` van 20, 8 naar 24, 9. **Nieuw: de hoed kantelt mee.** Het model zet `ouder["hoed_voorover"]` (= BUIG min KOP, 15 graden) naast `hoed_voor` en `hoed_zak`; `hoeden.bouw` heeft daarvoor een nieuwe parameter `voorover` (standaard 0, dus voor alle andere hoeden verandert er niets). Waarom: met een rechtop blijvende hoed las de buiging als een knikkend hoofd; een hoed die meekantelt maakt er een echte buiging van, alsof hij zijn hoed tikt.
- **Kan 2, licht:** door het kantelen zie je in `na_u2` de felle bovenkant van de hoed niet meer, dus de hoed is niet meer het lichtste vlak. In `tenen` bloost hij van de zenuwen: eigen huid `f6bc94` (lichter en warmer dan `d9a080`), alleen in die stand. Zo valt het gezicht niet weg en is het meteen een grapje.
- **Voor Olaf:** de pijplijn moet bij `na_u2` de edelhoed met `voorover=hoed_voorover` renderen (of het hoedbeeld zo draaien), naast de verschuiving van `hoed_voor` en `hoed_zak`.
- `mila-edelman-standen-v3.png` en `mila-edelman-standen-v3-spelmaat-voor-na-4x.png` (boven v2, onder v3, met hoed, 4x en ware grootte; verkleind, geen spelbeeld).
- **GEZIEN met Read:** groot buigt nu de hele romp en tikt de hoed naar voren; op spelmaat leest `na_u2` als een buiging met hoed, niet meer als een knik. `tenen` heeft een warmer gezicht met de ogen erin. Eerlijk: de voorkant van de rand vangt nu het licht, de hoed blijft wit en fel, maar niet meer de grootste lichte vlek.

## Edelman stand `alleen`: zenuwachtig, hand aan de hoed (Mila, 17 nov ±06:05 UTC)
- Uit het plan hierboven: "Alleen en zenuwachtig: houdt met één hand de hoed vast, ogen opzij. Dit is ook het teken voor de speler: x 1,2."
- **Gebouwd:** linkerhand op de hoedrand (nieuw `hand_doel` in `held_soorten.py`: een hand naar een vast punt, arm in twee stukken met de elleboog opzij, in `held.py`), rechterhand houdt de stok gewoon, ogen opzij (zoals `wacht`), ogen wijd open (geen half ooglid) en een klein o-mondje. Alleen de edelman doet er iets mee; andere helden zien `alleen` als `rust`.
- **Voor Olaf:** de hoed zelf staat recht en op de gewone plek, er hoeft niets te schuiven. De hand ligt op z 1,66, net op de rand.
- **Besluit** arm lang en hoekig in plaats van een gewone armhoek. Waarom: met de vaste armhoeken komt de hand niet hoger dan het oor; een lange rode arm naar de hoed is op spelmaat de duidelijkste vorm van de hele rij.
- `mila-edelman-standen-v4.png` (dief, rust, wacht, wacht_tik, na_u, na_u2, tenen, alleen, stap1) en `mila-edelman-standen-v4-spelmaat-4x.png`.
- **GEZIEN met Read:** groot een nerveuze heer die zijn hoed vasthoudt en opzij loert, met "oh"-mondje. Op spelmaat leest de rode arm naar de witte hoed meteen, het verschil met `rust` en `wacht` zie je in één blik. Eerlijk: de arm is dun en lang (cartoon), en `tenen` is op spelmaat nu het lichtste gezicht van de rij, niet meer in de schaduw.

## Edelman v5: Daans vier kansen op `alleen` (Mila, 17 nov ±06:45 UTC)
- **(1) Arm dikker, korter ogend, knik:** dikte 0,055 naar 0,068, elleboog verder opzij en lager (`ell` in `held.py`), elleboogbol 0,072. De arm is nu een duidelijke V in plaats van een lange buis.
- **(2) Witte manchet:** kort wit stukje (straal 0,082) op de onderarm net voor de hand, zelfde wit als de handschoen. Zo houdt de rode arm op voordat de hand begint en loopt hij niet de romp in.
- **(3) Hand op de rand:** `hand_doel` naar (-0,4, -0,24, 1,67): op de voorkant van de rand (straal ±0,47, rand op z 1,62), de hand is plat (0,095 x 0,085 x 0,07) zodat hij op de rand ligt in plaats van ernaast te zweven.
- **(4) Licht op het gezicht:** **besluit** het verschil kwam vooral uit het brede proefblad. Waarom: daar staat de fakkel op x 2,8, dus de rechterste figuren (stap1, de "snor") krijgen hem van achteren en lijken donker, en de middelste te licht. Het spel rendert elke stand los in het midden. Nieuw script `mila_edelman_los.py` doet precies dat. Huid gemeten (mediaan lichtheid van de huidpixels, los gerenderd): rust 174, wacht 172, na_u 173, na_u2 174, alleen 176, stap1 174, tenen was 182. Alleen `tenen` was echt te licht: blos-huid van `f6bc94` naar `e4aa86`, nu 173. Niets anders aan het licht veranderd.
- `mila-edelman-standen-v5-los.png` (elke stand los gerenderd, naast elkaar), `-v5-los-spelmaat-4x.png` en `mila-edelman-alleen-v5-groot.png`.
- **GEZIEN met Read:** groot ligt de witte hand op de rand met de manchet eronder, de arm knikt; op spelmaat leest de arm als een rode haak naar de hoed met een witte punt, de gezichten zijn nu één toon. Voor Olaf: niets nieuws in de pijplijn, alleen andere maten in `held.py` en `held_soorten.py`.
