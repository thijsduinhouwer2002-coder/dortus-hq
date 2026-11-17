# Capsule TOREN: richting voor "He wears their hats" (Daan, 16 nov 2026)

Aanleiding: besluit hoofdchat 16 nov 08:05 NL (advies Fenna, `platformen/succes/onderscheid-hats.md`): de hoedentoren moet het grootste ding op de capsule zijn, ook op 120 px en in grijs. Mila is eigenaar van de capsule; dit is een richting om op voort te bouwen, geen vervanging.

## Bestanden
- `capsule_toren.py`: kopie van Mila's `capsule3d.py` met omgevingsgetallen `TOREN_*`. Gloop draagt alleen de helm uit `gloop.py`; daarop stapelt het script hoeden uit `hoeden.py` (meet elke hoed en zet de volgende erop, `TOREN_ZAK` = hoe diep hij erin zakt). Minder goud (`TOREN_BERG`), geen beker, geen hoed op de berg, linker fakkel weg (stond achter de titel), ridder kleiner.
- `maak_toren.sh`: ronde 1 (header en klein), op dubbele grootte en verkleind.
- Ronde 1: `toren-header-920x430.png`, `toren-klein-462x174.png` (6 hoeden: helm, kroon, koksmuts, veermuts, emmer, puntmuts).
- Ronde 2, alleen klein: `toren-klein-ronde2-462x174.png` (4 groter: helm, kroon, koksmuts, hoge hoed, puntmuts; donkere muur). Instellingen: `TOREN_ZAK=0.12,0.38,0.32,0.15 TOREN_HOEDEN=4,5,7,1 TOREN_KANTEL=4,-9,10,-12 TOREN_S=1.1 TOREN_GROOT=1.0 TOREN_KRS=0.8 TOREN_WANDGLOED=60 TOREN_RAND=150 CAP_WANDLAMP=120 CAP_WAND1=3a2420 CAP_WAND2=4e3028 TOREN_KCZ=3.2 TOREN_KLENS=24 TOREN_KTZ=1.45 TOREN_KTM=1.5 TOREN_KTX=-0.2 python capsule_toren.py uit.png 924 348 32 klein`.
- Toetsen op 120 px, kleur en grijs, naast Don't Rob My Dungeon (header uit de openbare appdetails-API): `toren-toets-120-grijs-1x.png` (ronde 1, ook de header) en `toren-toets-120-grijs-ronde2-1x.png`.
- Let op: hoed 3 (pet) meet verkeerd in het script (de klep geeft een kader tot -2,8), daarom zit hij er niet in.

## Wat ik zag (GEZIEN met Read, ook 3x vergroot)
- **Ronde 1:** groot ziet het er speels uit, een wiebelende toren die je wilt bekijken. Maar op 120 px is het een dun paaltje met strepen boven een klein slijm. Blinde kijker: nu 4, toren r1 5 op het doel "slijm met een stapel hoeden". Fouten: toren te smal (6 tot 8 px op 120), lichte hoeden verdwijnen in de lichtvlek op de muur, veel lege muur.
- **Ronde 2:** donkere muur, minder en grotere hoeden, een donkere hoge hoed tussen de lichte. Op 120 lees je nu wel "hoeden" (puntmuts en hoge hoed vallen op, ook in grijs). Nog zwak: Gloop is te klein en de punt van de puntmuts raakt de bovenrand.

## Les voor de capsule (wat werkt op 120 px)
1. **Lager en breder, niet hoger.** Een capsule is breed; een hoge toren wordt een stokje. Liever 4 of 5 grote hoeden dan 6 kleine.
2. **Afwisselend licht en donker.** Grijswaarde telt meer dan kleur: hoge hoed (donker) tussen koksmuts en kroon (licht). Emmer en bruin verdwijnen tegen de muur.
3. **Donkere muur achter de toren**, geen lichtvlek daar; het licht hoort óp de hoeden (randlicht van boven).
4. **Gloop groter dan nu in r2**, het oog is het tweede herkenningspunt. De ridder mag een stipje zijn of weg in klein.
5. Wat nog te proberen (Mila): toren licht scheef naar de titel toe, zodat hij de breedte gebruikt; elke hoed een donkere rand (zoals het icoon van het Gloop-spel).

## Ronde 3 (klein, scheef naar de titel), 16 nov ±07:55 UTC
`toren-klein-ronde3-scheef-462x174.png`, toets `toren-toets-120-grijs-ronde3-1x.png`, GEZIEN. Zelfde als ronde 2 met `TOREN_KANTEL=6,10,14,18 TOREN_SCHUIF=-0.12,-0.2,-0.28,-0.3 TOREN_KCX=0.9 TOREN_KCZ=3.6 TOREN_KLENS=21 TOREN_KTZ=1.6 TOREN_KTX=-0.6 TOREN_KRS=0.7`.
- Groot oogt hij levendiger (een toren die bijna omvalt naar de titel, past bij de grap). Op 120 px ongeveer gelijk aan ronde 2.
- Nog steeds te klein: Gloop. In klein staat `GROOT` vast op 1,3 in het script (`TOREN_GROOT` werkt alleen in de header), en de hoeden schalen mee met de helm. Gloop groter maken = `GROOT` voor klein instelbaar maken en `TOREN_S` iets omlaag.
- Fout om te verhelpen: witte glansvlek op de H van HATS (sleutellicht), en een donkere fakkelrest aan de rechterrand.

## Ronde 4 (Mila, klein, 16 nov ±11:00 UTC)
`toren-klein-ronde4-mila-462x174.png`, naast ronde 3 met 120 px in kleur en grijs: `voor-na-ronde3-ronde4-mila-met-120.png`. GEZIEN met Read. Gerenderd op 924x348 (16 samples) en verkleind.
- Script: `GROOT` voor klein is nu instelbaar (`TOREN_KGROOT`, standaard 1,3 zoals het was) en het sleutellicht ook (`CAP_SLEUTEL`, standaard 1600). Verder niets aan Daans script veranderd.
- Instellingen: `TOREN_ZAK=0.12,0.38,0.15 TOREN_HOEDEN=4,7,1 TOREN_KANTEL=6,12,24 TOREN_SCHUIF=-0.12,-0.22,-0.34 TOREN_S=0.9 TOREN_KGROOT=1.6 TOREN_KRS=0.7 TOREN_WANDGLOED=60 TOREN_RAND=150 CAP_WANDLAMP=120 CAP_WAND1=3a2420 CAP_WAND2=4e3028 TOREN_KTM=1.5 CAP_SLEUTEL=900 TOREN_KCX=1.0 TOREN_KLENS=23 TOREN_KCZ=3.9 TOREN_KTZ=1.9 TOREN_KTX=-0.9 python capsule_toren.py uit.png 924 348 16 klein`.
- **Wat anders is:** Gloop 1,6 in plaats van 1,3, drie hoeden in plaats van vier (kroon, hoge hoed, puntmuts), elk een eigen omtrek, en de hele toren in beeld, scheef naar de titel. Op 120 px lees je nu een groot slijm met een stapel hoeden in plaats van een paaltje boven een stipje.
- Geprobeerd en niet gekozen: vier hoeden met Gloop 1,75 (toren loopt boven uit beeld, dan is het geen toren meer), koksmuts bovenop voor licht-donker-licht (leest als popcorn of wolk, net als op het icoon).
- Nog open: in grijs vallen puntmuts en hoge hoed samen tot één donkere vorm (alleen de kroon is licht); de witte glansvlek op de H blijft ook met een zwakker sleutellicht, die komt van een ander licht. Volgende stap: puntmuts lichter paars (zoals op het Garmin-icoon, richting 8a6ad8) en de glans op de H zoeken.
- **Ronde 4b (keus):** zelfde als ronde 4 met `TOREN_PAARS=b89cf0` (nieuwe schakelaar, kleurt alleen het materiaal "paars" van de puntmuts). `toren-klein-ronde4b-mila-462x174.png`, rij ronde 3, 4 en 4b met 120 px kleur en grijs: `voor-na-ronde3-4-4b-mila-met-120.png`. GEZIEN: in grijs is de toren nu licht (puntmuts), donker (hoge hoed), licht (kroon), dus drie hoeden te tellen; op 120 px groot slijm met toren. 9a7ae8 geprobeerd, scheidt in grijs minder.
- **Header ronde 4 (Mila, 16 nov ±11:10 UTC):** `toren-header-ronde4-mila-920x430.png`, naast Daans ronde 1: `voor-na-header-ronde1-ronde4-mila.png` (met 120 px kleur en grijs). Zelfde drie hoeden en paars als klein 4b, plus `TOREN_GROOT=1.7 TOREN_CZ=3.8 TOREN_LENS=24 TOREN_TZ=1.1 TOREN_TM=1.45 HEADER_RY=-1.3`, 1840x860 met 16 samples, verkleind. GEZIEN: Gloop en toren vullen de rechterhelft, titel groter, ridder klein ervoor; geen lege muur meer boven de titel. Ook hier nog een lichte glans op de H.

## Keuring ronde 4b en ronde 5 (Daan, 16 nov ±11:45 UTC)
GEZIEN met Read: `voor-na-ronde3-4-4b-mila-met-120.png`, `toren-klein-ronde4b-mila-462x174.png`, header ronde 4, uitsneden 3x van titel en toren, 120 px in kleur en grijs. Controleur (Agent) keek mee en is het eens.
- **Oordeel: ja op fouten en leesbaarheid, klein en header, met de lichtfix van ronde 5.** Op 120 px groot slijm met drie hoeden, in grijs licht, donker, licht. Goede keuzes: drie hoeden in plaats van vier en Gloop 1,6.
- **De glans op de H gevonden en weg.** Getest door lampen een voor een uit te zetten (8 samples): sleutel, vul, titellamp en titelrand uit veranderden niets, **koel uit maakte de H schoon**. De koele lamp links (voor de ridder) gaf de witte vlek en de donkere wig, waardoor de H als een K las. Fix in `capsule_toren.py`: lichtkoppeling, de titel krijgt geen koel licht, de ridder wel. Standaard aan; `CAP_KOEL_TITEL=1` geeft het oude beeld. Werkt in klein en header. Blender 5.2.4 als `bpy` in een venv, render klein 16 samples in ±45 s.
- **Ronde 5 = 4b + fix:** `toren-klein-ronde5-daan-462x174.png` (instellingen precies als 4b) en `toren-header-ronde5-daan-920x430.png` (instellingen als header ronde 4). Vergelijking met 120 px: `voor-na-ronde4b-ronde5-daan-met-120.png`. Pixel voor pixel verschilt bijna alleen de titel.
- **Kan, geen moet:** (1) in grijs valt de hoge hoed bijna weg tegen de donkere muur; `TOREN_RAND` 400 en 800 geprobeerd, dat maakt vooral de muur lichter en wint weinig, dus niet gekozen; een lichtere rand op de hoed zelf is beter. (2) Kroon en hoge hoed lopen in elkaar (rand zakt tussen de punten, losse rode bol rechts); op 120 een gouden klont. (3) Klein: punt van de puntmuts vlak onder de bovenrand, Gloop onderaan afgesneden; samen 4 tot 6 px omlaag in de toren of camera iets terug. (4) Ridder op 120 een stipje en het linker kwart van de header lege muur: mag blijven.

## Ronde 6 (Mila, 16 nov ±11:50 UTC): Daans drie kan-punten
`toren-klein-ronde6-mila-462x174.png`, `toren-header-ronde6-mila-920x430.png`, vergelijking met ronde 5 en naast vier toppers (Rusty's, Bongo Cat, Bao Bao, Monster Farm, vers uit de appdetails-API) op 120 px in kleur en grijs: `voor-na-ronde5-ronde6-mila-met-120.png`. GEZIEN met Read, groot en op 120. Blender 5.3 als `bpy`, klein 924x348 met 16 samples, header 1840x860, verkleind.
- **Script (twee nieuwe schakelaars, standaard uit):** `TOREN_HOEDLICHT` = warm randlicht van achter-boven dat via lichtkoppeling (INCLUDE) alleen op de hoge hoed valt, dus de muur wordt niet lichter (dat was het probleem met `TOREN_RAND`). `TOREN_HOGEHOED` = kleur van de hoge hoed in de capsule.
- **Instellingen = ronde 4b plus:** `TOREN_HOEDLICHT=800 TOREN_HOGEHOED=4a4452 TOREN_ZAK=0.12,0.18,0.15 TOREN_S=0.78`; klein ook `TOREN_KLENS=22 TOREN_KCX=0.85 TOREN_KCZ=3.7`; header met de instellingen van header ronde 4.
- **Kan 1, hoge hoed in grijs:** lichtere antraciet en randlicht op rand en bovenkant. Op 120 in grijs nu drie tellen (licht, middel, licht) in plaats van een donker gat.
- **Kan 2, kroon en hoge hoed:** de hoed zakte 0,38 in de kroon; nu 0,18, dus hij staat óp de punten. De kroon leest weer als kroon met drie punten en de robijn zit zichtbaar vóór op de kroon in plaats van als losse bol. Op 120 geen gouden klont meer.
- **Kan 3, klein in beeld:** camera iets terug (lens 23 werd 22) en hoeden iets kleiner (0,9 werd 0,78). Puntmuts heeft nu ruimte boven, Gloops mond zit helemaal in beeld. Geprobeerd en niet gekozen: lens 21 (rechts komt de rand van de muur in beeld als grijze wig), puntmuts schuiner (34 graden, oogt als omvallen in plaats van stapel).
- **Prijs:** Gloop oogt een fractie kleiner en de titel ook. Op 120 lees je nog steeds eerst slijm met hoedentoren.
- **Wat ik zag naast de toppers (voor later, geen moet):** alle vier toppers zijn licht en zonnig; wij zijn de enige donkere capsule. Dat valt op in de rij, maar op 120 is onze titel de enige lichte vlek. Volgende stap om te proberen: warmere, lichtere muur achter de titel (de grot mag gloeien, zoals de fakkel), zonder de toren te verliezen.
- **Ronde 6b (keus, ±12:00 UTC): warme muur.** Zelfde als ronde 6 met `CAP_WAND1=5a3426 CAP_WAND2=7a4a34 CAP_WANDLAMP=400`. `toren-klein-ronde6b-mila-462x174.png`, `toren-header-ronde6b-mila-920x430.png`, vergelijking op de blauwe Steam-pagina met de toppers: `voor-na-ronde6-ronde6b-mila-met-120.png`. GEZIEN met Read. **Waarom:** de donkere bruine muur van ronde 6 loopt op 120 px bijna weg in het donkerblauw van de Steam-pagina (de hoeken verdwijnen), terwijl alle toppers licht zijn. Met de warme muur is de capsule een eigen gloeiend vlak, oogt hij als een warm hol in plaats van modder, en de donkere hoge hoed staat er juist beter tegen. In grijs blijft HATS de lichtste vorm. Geprobeerd en niet gekozen: gloed alleen in het midden (wandlamp 900 op donkere muur), dan staat de gloed achter de titel en wordt die minder fel.

## Hoofdbeeld in de toren-richting (Mila, 16 nov ±12:05 UTC, voorstel)
`toren-hoofd-ronde6b-mila-1232x706.png`, naast het huidige `winkelpagina/main-1232x706.png` op 616 en 308 px, kleur en grijs: `voor-na-hoofdbeeld-toren-6b.png`. GEZIEN met Read.
- Script: nieuwe schakelaar `HF_TM` (titel in het hoofdbeeld groter, standaard 1,0 = zoals het was).
- Instellingen: ronde 6b plus `HF_LENS=32 HF_CZ=3.4 HF_GROOT=1.55 HF_RS=0.9 HF_TZ=1.5 HF_TM=1.4 HF_TX=-5.2 HF_GX=2.6 HF_RX=0.3`, `python capsule_toren.py uit.png 1232 706 16 hoofd`.
- Wat ik zag: de hele toren in beeld met ruimte boven, titel groot links, de ridder klein ervoor kijkt omhoog naar de helm op Gloop (de grap). Op 308 in grijs leest HATS als lichtste vorm en de toren als drie hoeden. Geprobeerd: lens 40 (toren loopt boven uit beeld), titel 1,7 (S loopt achter de puntmuts).
- Nog niet op de winkelpagina gezet: eerst Daans ja op ronde 6b, en het moet passen bij de schermen in de winkel. Volgende: bibliotheek 600x900 en staand 748x896 in dezelfde richting.

## Bibliotheek 600x900 in de toren-richting (Mila, 16 nov ±12:10 UTC, half af)
`proef-bibliotheek-toren-mila-300x450-2x.png` (twee proeven op 300x450, 10 samples). Script: nieuwe schakelaar `TOREN_TX` (titel in de header-variant opzij, standaard 0). Instellingen rechts: ronde 6b plus `TOREN_GROOT=1.5 TOREN_CX=2.25 TOREN_CZ=4.1 TOREN_LENS=46 TOREN_TX=4.3 TOREN_TZ=4.5 TOREN_TM=1.05 HEADER_RX=1.0 HEADER_RY=-1.3`, `python capsule_toren.py uit.png 600 900 16`.
- GEZIEN: staand werkt, titel boven, toren in het midden, ridder klein ervoor. **Nog niet goed:** bovenaan staat een harde donkere band (de rand van de muur of het donker erachter), en de puntmuts raakt bijna OF THE FALLEN. Lens 20 geprobeerd: veel te wijd, je ziet de hele doos.
- Volgende stap: muur hoger maken of de bovenkant laten weglopen in donker, titel iets kleiner en hoger, dan op 600x900 met 16 samples en naast de toppers.

## Hoofdbeeld ronde 7 (Mila, 16 nov ±12:50 UTC): Daans twee kan-punten
`toren-hoofd-ronde7-mila-1232x706.png`, naast ronde 6b op 616 en op 308 in kleur en grijs: `voor-na-hoofdbeeld-6b-7.png`. GEZIEN met Read, ook de toren en de voet van de muur op 3x.
- **Kan 1, rand hoge hoed als stokje:** de hoge hoed kantelde 12 graden, waardoor de rand bijna van opzij als dun grijs stokje links uitstak. Nu 4 graden (`TOREN_KANTEL=6,4,24`): de rand ligt vlak en leest als hoedrand. De toren blijft scheef door de kroon (6) en de puntmuts (24).
- **Kan 2, worst aan de voet van de muur:** nieuwe schakelaar `TOREN_VOETROTS=los` (standaard `rij` = oud beeld). Ruim de helft van de 40 rotsen valt weg, de rest wordt kleiner en wisselender. De gewone random-reeks loopt gelijk door, dus kiezels, munten en alles daarna blijven op hun plek. Leest nu als losse stenen langs de wand.
- Instellingen: precies als het hoofdbeeld 6b plus `TOREN_KANTEL=6,4,24 TOREN_VOETROTS=los`, 1232x706 met 16 samples.
- Niet in klein en header doorgevoerd: daar staat de hoge hoed kleiner en leest de rand al goed, en de voetrotsen vallen buiten beeld of achter de titel.

## Bibliotheek 600x900 ronde 7 (Mila, 16 nov ±13:10 UTC, nog niet af)
`toren-bibliotheek-ronde7-mila-600x900.png`, naast het huidige `capsule-3d/bibliotheek-600x900.png`, Rusty's en Bongo Cat (vers van de Steam-CDN) op 300 en 100 px, kleur en grijs: `vergelijk-bibliotheek-toren-ronde7-toppers.png`. GEZIEN met Read.
- **Twee nieuwe schakelaars, standaard uit:** `TOREN_WANDH` (hoogte van de muur, standaard 14; de staande camera keek erboven uit, dat was de harde zwarte band) en `TOREN_TLX`/`TOREN_TLZ`/`TOREN_TLAMP` (de titellamp schuift mee met de titel; in de staande variant stond de titel buiten zijn licht en was hij dof).
- Instellingen: hoofdbeeld 7 (hoeden, kleuren, licht, `TOREN_KANTEL=6,4,24 TOREN_VOETROTS=los`) plus `TOREN_WANDH=24 TOREN_GROOT=1.65 TOREN_CX=2.25 TOREN_CZ=3.75 TOREN_LENS=58 TOREN_TX=4.3 TOREN_TZ=4.85 TOREN_TM=1.2 TOREN_S=0.7 TOREN_TLX=3.0 TOREN_TLZ=5.0 HEADER_RX=1.0 HEADER_RY=-1.3`, `python capsule_toren.py uit.png 600 900 16`.
- **Wat beter is:** geen zwarte band, titel groot en fel bovenaan, de puntmuts raakt OF THE FALLEN niet meer (hoeden 0,7), op 100 px lees je titel en slijm met hoedentoren.
- **Wat nog niet goed is (eerlijk naast het oude en de toppers):** het onderste vijfde is lege vloer, de ridder is een stipje en het geheel is donkerder dan het oude beeld met de goudhoop. Rusty's en Bongo Cat vullen tot onderin. Nog niet op de winkelpagina zetten.
- Geprobeerd: lens 46 (alles klein, veel vloer), lens 64 (HATS tegen de bovenrand), hoeden 0,78 (puntmuts in de titel).
- **Volgende stap:** goudhoop vooraan onderin (zoals in het oude beeld, en eerlijk: de goudberg zit in het spel), ridder groter en dichter bij de kijker, dan opnieuw naast de toppers.

## Ronde 8 en staand ronde 1 (Daan, 17 nov ±14:30 tot 15:05 UTC): de set af voor de toets van wo 18 nov 20:00
Blender 5.3 als `bpy` in een venv. Alles met `capsule_toren.py` zonder codewijziging, alleen schakelaars. Proeven op halve maat (8 samples) GEZIEN met Read, eindbeelden op dubbele maat (20 tot 24 samples) en verkleind.
- **Bibliotheek 600x900 ronde 8** (`toren-bibliotheek-ronde8-daan-600x900.png`): Mila's ronde 7 plus `TOREN_BERG=1.5 TOREN_RS=1.35 RIDDER_DRAAI=-60 HEADER_RX=0.5 HEADER_RY=-2.5 TOREN_CZ=4.1 TOREN_LENS=60 TOREN_TZ=5.1`. Haar volgende stap uitgevoerd: goudberg vult de vloer tot onderin, ridder groot vooraan en hij kijkt naar zijn helm op Gloop. Titel iets hoger, zodat de punt van de puntmuts OF THE FALLEN niet raakt (moet van de controleur).
- **Staand 748x896 ronde 1** (`toren-staand-ronde1-daan-748x896.png`): zelfde opstelling als de bibliotheek met `TOREN_BERG=1.5 RIDDER_DRAAI=-60 TOREN_LENS=52 TOREN_TM=1.1 TOREN_RS=1.35 HEADER_RX=0.4 HEADER_RY=-2.6 TOREN_CZ=4.4 TOREN_TZ=5.1`: ridder groot, laarzen en onderkant van het schild lopen van de rand af. De controleur noemde dat een moet; ik probeerde ridder kleiner en verder naar achter (`proef-staand-ridder-achter-748x896.png`, `TOREN_RS=1.15 HEADER_RX=0.7 HEADER_RY=-1.9`), maar dan zakt hij tot zijn middel achter de goudberg en is hij een hoofdje. **Bewust gekozen:** een figuur die onderaan uit beeld loopt is gewoon in staande key art, een kleine ridder breekt de grap. Titel 0,1 hoger dan de eerste versie, want daar stak de hoedpunt tussen THE en FALLEN; nu lucht ertussen (GEZIEN op halve maat en eindbeeld).
- **Hoofdbeeld 1232x706 ronde 8** (`toren-hoofd-ronde8-daan-1232x706.png`): Mila's ronde 7 plus alleen `TOREN_BERG=1.1`. De goudberg onder Gloop maakt het een schatkamer en houdt de set gelijk met bibliotheek en staand; verder niets veranderd.
- Voor en na: `voor-na-bibliotheek-r7-r8-staand.png` (bibliotheek r7, r8 eerste versie, staand oud, staand eerste versie).
- Controleur (Agent, blind voor mijn oordeel): nieuw beter dan oud, ja; bibliotheek 7,5, staand 6,5 met twee moets, beide verwerkt in de eindbeelden; event cover 8, event header 7,5.
- Header en klein blijven ronde 6b. Niet doorgevoerd naar de kleine maten: op 462 en 920 is de goudberg een gele vlek naast de gele titel.
- Logo met hoedjes op de letters alleen als los logo (bibliotheek, events). In de capsules niet: daar is de toren de hoed, en vier hoedjes op de titel naast een hoedentoren is te druk.
- Nog open, geen moet: helm op Gloop leest klein als serveerkoepel (Mila, na de speeltest); de rand van de goudberg is een gladde ellips.
