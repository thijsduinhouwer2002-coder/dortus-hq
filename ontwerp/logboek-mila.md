# Logboek Mila

## 9 nov 2026, run 1 (20:37 tot ±21:20 UTC)
- Gelezen: berichten, regels, besluiten, rol, overdracht van Daan, taken en status Steam, laatste build (main 4dcbda4, `schermen/steam-hol/main`).
- Oordeel build: netjes en leesbaar, maar geen eigen gezicht. Bruin overal, helden en Gloop verdwijnen in de muur, meldingenvlak groot en zwart. Haalt de lat "herkenbaar" en "haak" niet.
- **Besluit: aarde en holwand pruim in plaats van bruin.** Waarom: bruin is de kleur van de hele hoek; pruim is de tegenkleur van goud en van muntgroene Gloop, dus alles wat telt springt eruit, en geen topper gebruikt het. Blauwe nacht afgewezen: koud en de kleur van Ropuka. Daans maten en tekeningen blijven; alleen het palet in de bron is veranderd en alles is opnieuw getekend.
- **Besluit: de haak is Gloops hoedentoren** (hoeden van opgegeten helden op zijn hoofd, hooguit 4, daarna een hoedenberg). Waarom: een grap die je zonder lezen ziet, groeit vanzelf zonder straf, versterkt de wrok, en hoed-skins komen er later op. Bouwtaak naar Bram in `platformen/steam/taken.md`. Pas in winkelplaatjes als het in het spel zit.
- Vastgelegd in `ontwerp/steam/mila/stijl.md`.
- **Besluit: Gloop krijgt één oog, een scheve grijns en één tand** (alle slijmframes opnieuw getekend, zelfde bladen en maten). Waarom: twee oogjes met blosjes is de standaard slijm van elk spel; één groot oog is op 16 px direct herkenbaar en geeft karakter (een beetje eng, vooral grappig). Vier andere gezichten geprobeerd en afgewezen.
- Laars en trofee kregen een eigen leerkleur (`c`), want ze gebruikten de aardekleur 5 en zouden anders paars worden.
- Echte build bekeken (run 42696163192, commit 9efa3e1, `ontwerp/steam/mila/build-9efa3e1.png`): pruim en Gloop met één oog staan erin, plat-frame klopt, niets geschaald. Toets: (1) stopt scrollen: beter, de paarse strook valt op tussen blauwe en groene bureaubladen, maar nog niet genoeg; (2) herkenbaar: ja, voor het eerst; (3) haak: half, de hoedentoren moet nog gebouwd (Bram); (4) klein: ja, oog en held lezen op 120 px. Nog niet naar Thijs.
- Eerlijke vergelijking met Rusty's Retirement in `ontwerp/steam/mila/vergelijk-rusty-pruim.png`: Rusty laat ±330 px strook zien (GEZIEN), wij 120 px; wij winnen op karakter, niet op dichtheid. Meldingenvlak en gloed doorgezet naar Olaf in `platformen/steam/taken.md`.
- Garmin: Gijs heeft nog geen product (sterrenkaart is kandidaat). Niets voor mij tot hij kiest (regel 0c).
- Volgende run: build met hoedentoren keuren als Bram hem heeft; anders Gloop een eigen kijkrichting (oog naar de held) en de helden een slag groter en feller (13 tot 14 px), en een eerste opzet voor het winkelplaatje op 160 px.

## 9 nov 2026, run 2 (21:38 tot ±22:20 UTC)
- Gelezen: bericht van Sanne (toets 3: hoedentoren is de haak, 8+ hoedsoorten, boos teken leest als kruisje, spinrag als gewei, paneel bruin), taken, laatste besluiten.
- **Besluit: 10 hoedsoorten** (helm, puntmuts, kap, pet + kroon, koksmuts, emmer, hoge hoed, pan, veermuts). Waarom: op de toren moet elke hoed een eigen silhouet hebben, anders lees je geen stapel maar een vlek; koksmuts, pan en emmer zijn de grap (een held die met een pan op zijn hoofd een kerker in loopt). Alle tien op 3x bekeken (`ontwerp/steam/mila/hoeden-3x.png`): elk silhouet is los te herkennen. De emmer is de zwakste (leest bijna als helm), later misschien een hengsel.
- **Besluit: boos teken wordt een onweerswolkje met rode bliksem.** Waarom: het oude rode teken las als kruisje; een vuist las op 8 px als een gezicht en een stoomwolkje als een bot (alle drie naast elkaar bekeken). Een wolk met bliksem is in elk land "boos".
- **Besluit: paneel in pruim** (holwand-tinten, gouden spijkertjes blijven). Waarom: bruin hout was de enige bruine vlek in de strook en las als venster.
- **Besluit: spinrag opnieuw** als web met bogen en een spinnetje aan een draad. Waarom: het oude waren losse diagonalen, boven Gloop een gewei. Het spinnetje is meteen een klein grapje voor wie goed kijkt.
- Code (10 hoeden, `% 4` weg, tabellen) bij Bram, spinrag een kolom opzij bij Olaf (`platformen/steam/taken.md`, 21:55). De eerste 4 hoeden staan op dezelfde plek, dus de build breekt niet.

## 9 nov 2026, run 3 (22:39 tot ±23:05 UTC)
- Gelezen: nieuwe berichten (Thijs 23:37 en 23:45 NL: Steamworks staat, winkelpagina-pakket vóór 1 dec; Sanne toets 4; Gijs Garmin), besluiten, taken.
- **Winkelpagina begonnen** in `ontwerp/steam/winkelpagina/`. Maten met curl uit de Steamworks-docs (standard, libraryassets, rules), tabel in `plan.md`. Regel die telt: op capsules alleen beeld en naam, en de kleine capsule wordt door Steam verkleind tot 120 x 45.
- **Besluit (voorstel, definitief als niemand tegenspreekt vóór 11 nov): naam "Hats of the Fallen".** Waarom: de naam is de haak (Gloop draagt de hoeden van wie hij opat), een donkere grap op "Hall of the Fallen", en 0 treffers op Steam. Alles met Gloop afgewezen: vier bestaande spellen met Gloop in de naam (GEZIEN).
- **Logo v1:** eigen pixelletter, HATS in schatgoud, OF THE FALLEN in Gloopgroen, op elke letter van HATS een echte hoed uit het spel. Leest op 120 x 45 (GEZIEN).
- **Header v1 afgewezen, v2 gemaakt.** v1 (schaal 6, hele hol) toonde te veel kleine dingen; Gloop met toren verdween op 292 breed. v2 op schaal 10 met Gloop en vier hoeden als middelpunt, een held met een pan die naar hem kijkt, schat met gloed. Op 292 breed leest de toren nog (GEZIEN).
- **Helm hoger met een rode kam** (Sanne: pannendeksel). Alleen de hoedenbladen veranderden (git diff nagekeken). `HOED_TOP[0]` naar 0 gevraagd aan Bram.
- **Garmin:** naam en stijl in `ontwerp/garmin/tij-stijl.md`. Besluit: naam "Tide" en het ronde scherm als patrijspoort, inhouden is duiken, dieren als beloning. Waarom: elke concurrent is een timer of een cirkeltje; water dat het hele ronde scherm vult is op een paar centimeter rijk en meteen herkenbaar, en een duikprofiel is een mooiere lijn dan staafjes.
- Volgende run: main capsule 1232 x 706, staand 748 x 896, library 600 x 900, hero 3840 x 1240 (zonder tekst) en library-logo uit dezelfde maker; lijst met opnames voor schermen en trailer naar Olaf; header bovenrand (mos-rij) netter.
- Later in run 3: alle overige capsules v1 (main, staand, library, hero zonder tekst, los logo 1280) uit dezelfde maker. Header naast de vier toppers gezet (`vergelijk-header-toppers.png`): v2 verloor duidelijk (klein, donker). **Besluit: header v3 als close-up** (Gloop met toren op schaal 12, groot logo). Eerlijk: nog minder rijk dan de geschilderde toppers; v4 tekent Gloop en de hoeden opnieuw op 3x spelmaat. Logo v2 dikker met reliëf. Hero was 1248 hoog, nu precies 1240.

## 10 nov 2026, run 4 (±00:41 tot ±01:25 NL)
- Gelezen: berichten (Thijs 00:16 uniform met voorrang, 00:29 top van de top; Gijs naamcheck), keuring 1 van Daan op de winkelpagina, Abels `merk/maten.md` en `teksten.md`, het oude logo in de repo dortus.
- **Besluit: het uniform van Dortus is de D als deur op een kier, met warm licht erachter.** Waarom: (1) vertrouwd, de twee bolletjes van het oude logo worden scharnieren, dus het oude merk leeft voort; (2) goud licht in een donker vlak trekt het oog in elke lijst; (3) het past bij alles wat we maken (achter elke deur zit iets) zonder spelfiguur, zoals Abel eiste; (4) op 16 px blijft een lila D met een gouden hart over (GEZIEN).
- **Besluit: de grap op de grote beelden** is dat er spullen uit de deur rollen: kroontje (Het Hol), dobbelsteen (Rollwright), accolades (tools). Eerlijk, want het zijn onze producten.
- Gemaakt in `platformen/abel/merk/` met `bron/maak_uniform.py` (SVG, omgezet met rsvg-convert): avatars 1024, 512, 184 en een eigen kleine tekening voor 32 en 16, `merkteken.svg`, Steam-logo 1200 x 460, Steam-kop 1500 x 220, Steam-achtergrond 1920 x 1200, og 1200 x 630, social 1280 x 640, `toets-klein.png`. Alles bekeken met Read. Uitleg en kleuren in `uniform.md`.
- Afgewezen tijdens het werk: deurblad breed open op 32 px (de opening werd een donker gat, geen licht meer); lichtvlek op de vloer die buiten de D uitstak.
- **Garmin: naam Ebb** (Tide valt af door ±30 getijden-apps). Reden in `ontwerp/garmin/tij-stijl.md`, regel in Gijs' taken.
- Daans keuring 1 op de winkelpagina (A en S van HATS, één naam overal, twee dezelfde kisten, kleine capsule) ligt klaar voor de run na het uniform.
- Volgende run: uniform v2 (diepte in de D, betere spullen, social per repo met productbeeld in het licht), daarna Daans moet-punten winkelpagina.

## 10 nov 2026, run 5 (±01:40 tot ±02:30 NL)
- Gelezen: berichten (niets nieuws voor mij), Daans keuring 2 op het uniform, Abels `voor-mila.md` en proeven, Daans keuring 1 en 2 op de winkelpagina.
- **Uniform v2** (bestanden met `-v2`, uitleg onderaan `uniform.md`, proef op een echte Steam-pagina in `merk/proef/steam-pagina-v2-op-steam-*.png`). Besluit: **de Steam-kop krijgt geen tweede D**; het licht valt vanaf de avatar over de vloer en daarin rollen kroon, dobbelsteen en accolades. Waarom: de deur zit al in de avatar (Daan 6), en zo lijkt het licht uit de avatar te komen, op 1024, 1280 en 1920 breed (GEZIEN). Besluit: **de bundel begint smal onder de lichte opening** (Daan 2): nu lees je dat het licht door de kier valt. Abels achtergrond v1b overgenomen, spullen alle drie terug. Logo gemeten in het midden.
- Eerste kop-v2 afgewezen: de bundel was een harde gele baan (las als weg, niet als licht); nu zacht met een vervaging. Tweede afgewezen: spullen vielen onder de tabs (kop is op de pagina maar ±206 hoog).
- **Winkelpagina v4**, moet-punten 1, 4, 5, 6 en B van Daan; zie `ontwerp/steam/winkelpagina/plan.md` onderaan. Hero naar schaal 13: op 16 past de toren nooit in het veilige vlak.
- Volgende run: header v4 naast de toppers (Daan 9), goudhoop als munten (7), dan social per repo zodra Abel de volgorde geeft.
