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
