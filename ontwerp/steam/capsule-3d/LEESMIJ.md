# Capsule in 3D (Mila, 14 nov 2026)

Eerste 3D-versie van de winkelafbeelding van Hats of the Fallen, voor het toetsmoment van Thijs (ma 16 nov) en de capsules van wo 25 nov (`platformen/steam/planning-fest-2027.md`).

## Het idee
De haak in één beeld, zonder uitleg: **Gloop zit grijnzend op zijn goud met een toren van gestolen hoeden** (helm, kroon, heksenhoed, rode muts). Links komt een ridder binnen en schrikt: onderaan de toren draagt Gloop precies dezelfde zilveren helm als hij. Je snapt wat er met de vorige ridder gebeurd is, en dat hij de volgende is. Dat is de naam: Hats of the Fallen.

Eerlijk: alles in beeld zit in het spel. Gloop en de ridder komen ongewijzigd uit Daans `gloop.py` (versie 2, 4 hoeden, stand rust) en `held.py` (ridder, stand schrik); de hoedentoren, de schat, de fakkels en de stenen boog van de schatkamer bestaan in het spel.

## Bestanden
- `capsule3d.py`: het model. Draai met Blender als Python-pakket (`bpy==5.2.4`):
  - header: `capsule3d.py header-920x430.png 920 430 64` (±1,5 min op 2 kernen)
  - klein: `capsule3d.py klein-462x174.png 462 174 96 klein`
- `LilitaOne-Regular.ttf`: letter van de titel (SIL Open Font License, Google Fonts; mag mee in een product en in winkelbeelden).
- `header-920x430.png`, `klein-462x174.png`: de renders.
- `klein-oud-nieuw.png`: de oude pixelcapsule klein naast de nieuwe.
- `vergelijk-header3d-toppers.png`: onze header naast Rusty's, Bongo Cat, Spirit City, Tiny Pasture en Deskrawl op dezelfde hoogte.

## Keuzes
- **Besluit: de capsule mag een lichte perspectief hebben (lens 42), anders dan de strook (orthografisch).** Waarom: een capsule is een poster; met diepte staan Gloop en de ridder in een kamer in plaats van op een plank. Kleuren en licht blijven die van `3d-stijl.md` (pruim, muntgroen, goud, warm fakkellicht).
- **Besluit: titel als 3D-letters in goud met een donkere pruimen rand, geen pixelletter meer.** Waarom: de pixelletter vloekte naast de 3D-figuren; Lilita One is rond en dik zoals Gloop, en leest op 174 px nog.
- Gloop zit op de berg (niet erin): eerst zakte hij in het goud en was zijn vorm weg.
- Gloop is groter dan de ridder: hij is de ster en de grap zit in zijn toren.

## Eigen toets (GEZIEN met Read)
- Naast de toppers op 231 px hoog: veel rijker dan de pixelheader van v5; titel leest, de toren leest als hoeden. Zwakker dan de toppers: hun figuren vullen het vak, bij ons is er nog veel muur. Rusty's en Tiny Pasture zijn feller en lichter.

## Ronde 2 (zelfde run, na de frisse kijker)
Frisse kijker (alleen de header en de rij met toppers), letterlijk: "Rechts zit een groen eenogig slijmmonster op een berg goud. Het draagt een stapel hoeden ... Het ridderventje draagt dezelfde soort helm, dus zijn helm komt straks waarschijnlijk op die stapel. Dat is een leuke donkere knipoog. Maar je moet het zelf in elkaar puzzelen." Klein: "Bij Hats zie je kerker met twee kleine dingetjes ... het paars is donker en vlak." Zijn tip: "maak het slijm met zijn hoedenstapel veel groter ... (liefst hoger en gekker) ... een lichtere, warmere achtergrond rond het slijm." Cijfer 5 (groot 6 tot 7).
- Gloop ±20% groter en dichterbij, de ridder kleiner en verder naar voren links (bang erbij, niet de ster).
- **Besluit: een hoedenberg rond Gloop (emmer, koksmuts, pan, pet, veermuts, kap, hoge hoed uit Daans `hoeden.py`), de toren op zijn hoofd blijft 4.** Waarom: in het spel draagt Gloop er hoogstens 4 en ligt de rest op de berg (`toets_held.gd`: "10 hoeden: 4 op zijn hoofd, 6 op de berg"). Zo wordt het "gekker" zonder te liegen, en zie je klein aan de pan en de emmer dat het om hoeden gaat.
- Warme gloed op de muur achter Gloop, koel licht alleen nog op de ridder.
- De hoge hoed stond eerst voor zijn mond; verplaatst naar achter op de berg, de grijns is weer vrij.
- `header-ronde1-920x430.png` is ronde 1 ter vergelijking.
- GEZIEN met Read: header, klein, rij met toppers. Eigen oordeel: voller en grappiger dan ronde 1, de hoeden lezen nu als thema. Nog steeds minder één helder idee dan Rusty's of Deskrawl: te veel kleine dingen tegelijk. Geen nieuwe frisse kijker meer deze run.

## Volgende ronde
1. Frisse kijker alleen op `header-920x430.png` en op ware grootte; letterlijk opschrijven wat hij ziet en of de helm-grap leest.
2. Eén helder idee: minder kleine dingen (fakkels of boog weg), Gloop met toren groot en midden, hoedenberg erachter in plaats van ervoor. Frisse kijker opnieuw, doel 7.
3. Hoofdbeeld 1232x706 en bibliotheek 600x900 (staand: toren past daar juist goed).
4. Idee uit de oude pixelcapsule terughalen: kleine hoeden op de letters van HATS (klein-oud-nieuw.png links). Dat maakt de titel zelf de grap.
5. Daan keurt op fouten en leesbaarheid.

## Ronde 4 (14 nov ±09:00 UTC, na Daans keuring van 06:35)
Alle vier moets van Daan gedaan in `capsule3d.py`:
1. **Helmgrap:** `"PLUIM_KNAK": True` naar `gloop.py`; Gloops helm draagt nu dezelfde rode pluim als de ridder.
2. **Titel vrij van de rand:** HATS kleiner en naar binnen. Gemeten op de header (GEZIEN): links ±50 px, boven ±45 px. Klein: links ±38 px, boven ±30 px.
3. **Niets afgesneden, alleen dingen die lezen:** stenen boog weg (las als confetti), kap, pan, emmer, pet en veermuts weg. Op de berg alleen nog de hoge hoed en de koksmuts, beide binnen het vak. De ridder groter (1,2) en dichterbij, voeten in beeld; de camera kijkt iets lager.
4. **Klein:** geen fakkels en geen losse hoeden, Gloop met toren groter, ondertitel groter (0,86), ridder tussen titel en Gloop.
- **Fout gevonden en omzeild:** `GS` (de grootte van Gloop) telde nooit mee: de lus zet locatie en schaal, maar daarna leest het anker `matrix_world` voordat Blender die bijwerkt. Gloop vergroten gaat nu via `anker.scale` (`GROOT`, header 1,1, klein 1,15). `GS` laat ik staan zodat de plek gelijk blijft.
- `header-ronde2-920x430.png`, `klein-ronde2-462x174.png`: ronde 2 ter vergelijking. `voor-na-ronde2-ronde4.png`: boven groot, onder klein, links ronde 2, rechts ronde 4.
- **Frisse kijker** (alleen header en klein), letterlijk: "het monster verzamelt de hoeden van gevallen avonturiers, en het jochie is de volgende ... De helm met rode pluim onderaan de stapel is precies dezelfde als die van het ridderjongetje", na 3 tot 5 seconden. Klein: "HATS lees je goed, OF THE FALLEN kun je nog net lezen ... de kroon en de helm lopen in elkaar over, en dat de helmen hetzelfde zijn zie je op dit formaat niet meer." Wat niet leest: de koksmuts ("slagroom of een wolkje?"), het mesje, de kroon lijkt "een hoopje munten". Cijfer groot 7 (was 7 bij Daans proef, 5 tot 6 bij ronde 2), klein 6 (was 5).
- GEZIEN met Read: header, klein, voor/na. Eigen oordeel: één helder beeld nu, rustiger en rijker. Nog niet genoeg: op klein valt de grap weg.

## Ronde 4b (zelfde run): klein met de grap
- Klein met 2 hoeden (helm met pluim en kroon), Gloop 1,3 en ridder 1,5: `proef-klein-2hoeden-462x174.png`. Frisse kijker: grap na 3 tot 5 s, "de kroon trekt de aandacht weg van de helm", cijfer 7.
- Klein met 1 hoed: alleen de helm, dan krijgt hij in `gloop.py` gewoon de rechte rode pluim, precies zoals de ridder. Nieuwe frisse kijker zag A (2 hoeden) en B (1 hoed) naast elkaar: B "het monster draagt de helm van een gevallen ridder, en de levende ridder kijkt naar zijn eigen toekomst. Ik snap het in 1 tot 2 seconden." A 6, B 8.
- **Besluit: klein krijgt 1 hoed (de helm), `KLEIN_HOEDEN` standaard 1.** Waarom: op 174 px is twee gelijke helmen naast elkaar de hele grap, sneller (1 tot 2 s tegen 3 tot 5) en hoger cijfer (8 tegen 6); de titel zegt al HATS, de header laat de toren zien. Eerlijk: in het spel draagt Gloop ook vaak maar één hoed.

## Ronde 4c (zelfde run): header, ridder dichterbij
- Proef: ridder van x -0,85 naar -0,1 (vlak bij de goudberg), toren 3 hoeden (helm, kroon, heksenhoed; de rode muts weg, die raakte bijna de bovenrand). Frisse kijker A (ronde 4) tegen B (proef): A "het ridderje staat ver van het monster, dus het verband zie je niet meteen", 3 tot 4 s, cijfer 6; B "dit ventje loopt het hol binnen en daar zit iemand met de hoeden van zijn voorgangers op", ±2 s, cijfer 7,5. Zijn punt bij B: de hoge hoed verdween half achter de ridder (rood randje leek een fout), de koksmuts bleef vaag.
- **Besluit: header met de ridder dichtbij en 3 hoeden op de toren; op de berg alleen nog de hoge hoed, rechts, goed zichtbaar; koksmuts weg.** Waarom: sneller begrepen (2 s tegen 3 tot 4) en hoger cijfer; wat niet leest gaat eruit. Instelbaar met `HEADER_RX` en `HEADER_HOEDEN`.
- GEZIEN met Read: de nieuwe header; titel en toren vrij van de rand, hoge hoed heel in beeld.

## Hoofdbeeld 1232x706, eerste versie (zelfde run)
- `hoofdbeeld-1232x706.png`: zelfde scène als de header, alleen het formaat anders (`capsule3d.py hoofdbeeld-1232x706.png 1232 706 48`, ±2 min). GEZIEN met Read: alles binnen het vak, titel en toren vrij van de rand; wel veel lege muur boven en vloer onder. Nog geen frisse kijker.
- Volgende stap voor het hoofdbeeld: camera dichterbij of Gloop en ridder groter, zodat ze het vak vullen.

## Volgende ronde
1. ~~Klein: de grap op 174 px~~ gedaan in ronde 4b. Nieuw: probeer ook in de header of de helm sneller leest als hij groter en vooraan op de toren staat (frisse kijker groot: grap na 3 tot 5 s).
2. Kroon: minder glans of strakkere punten, zodat hij niet als munten leest.
3. Koksmuts: duidelijker (hogere band, plooien) of vervangen door een hoed die meteen leest (de heksenhoed staat al op de toren; misschien de hoge hoed alleen).
4. Hoofdbeeld vullen (zie boven), frisse kijker erop; bibliotheek 600x900 (staand); hoedjes op de letters van HATS als proef.

## Ronde 5 (14 nov ±11:40 tot 12:05 UTC, Daans "kan"-punten van 09:35)
Alle vier gedaan in `capsule3d.py`; `gloop.py` en `held.py` van Daan zijn niet aangeraakt (alles via de capsule).
1. **Munt en schild uit elkaar:** Gloop zonder munt in de buik (`CAPSULE_GLOOP_V`, standaard 1). Het rode schild van de ridder zakt 0,42 en schuift opzij (`SCHILD_ZAK`), weg bij zijn gezicht; het leest nu als schild (rood met gouden rand) en niet als tweede gouden schijf.
2. **Pluim in de header recht:** geen knak meer (`PLUIM_KNAK=1` zet hem terug). Met een kroon erop past de pluim niet bovenop; hij steekt nu links onder de kroon uit en buigt omhoog, vrij van de rand van de heksenhoed (eerste poging botste ertegen, GEZIEN in zoom).
3. **Kroon minder munt:** punten smaller en ±15% hoger, bolletjes 30% kleiner, minder glans (ruwheid 0,38, geen gloed).
4. **Header:** ridder iets verder naar achter (`HEADER_RY` -2,2 werd -1,95), laarzen nu ±10 px van de onderrand (was ±5); linker fakkel 0,2 naar rechts.
- Hoofdbeeld 1232x706 opnieuw gerenderd met dezelfde wijzigingen.
- `header-ronde4-920x430.png`, `klein-ronde4-462x174.png`, `hoofdbeeld-ronde4-1232x706.png`: ronde 4 ter vergelijking. `voor-na-ronde4-ronde5.png`: boven groot, onder klein (2x), links ronde 4, rechts ronde 5.
- **Proef: tweede kleinere hoed (heksenhoed) achter de helm op klein** (Daans idee, `KLEIN_ACHTER=1`): `proef-klein-heksenhoed-achter-462x174.png`. Frisse kijker (Agent, zag eerst groot, dan klein A zonder en B met): A 4, B 5; bij B "het paarse ding is klein, valt weg in de paarse muur, lijkt een vlekje of een bloem". **Besluit: klein blijft 1 hoed.** Waarom: de proef wint maar één punt en het extra hoedje leest als een fout; de eerdere A/B gaf 1 hoed een 8. De grap klein zonder header blijft een open punt (zie onder).
- **Frisse kijker op groot**, letterlijk: "het monster eet avonturiers op en houdt hun hoeden als trofeeën. Het jongetje is de volgende, want hij draagt dezelfde helm als de onderste in de stapel", na 3 tot 4 s. Cijfer 6. Wat hij raar vond: (a) de ridder lijkt eroverheen geplakt (scherp, vlak belicht, lichte rand) en kijkt de kijker aan in plaats van het monster, dus geen spanning; (b) het geheel is wat zacht, alsof opgeschaald; (c) de hoge hoed staat los aan de rand; (d) OF THE FALLEN botst bijna met de helm van de ridder.

## Ronde 5b (zelfde run): ridder naar Gloop, scherper
- **Ridder kijkt naar Gloop** (draai 38 werd 50, `RIDDER_DRAAI`), minder randlicht (60 werd 25) en minder koel licht (500 werd 300). Waarom: de frisse kijker vond hem "eroverheen geplakt" en "hij kijkt de kijker aan, niet het monster, dus geen spanning". Nu kijkt hij naar de helm op Gloop; dat is de grap. Ik koos 50 en niet 58 (proef): bij 58 zag je zijn schrikgezicht bijna niet meer.
- **Scherper:** alle drie renderen op dubbele grootte en dan verkleinen (`maak_alles.sh`). GEZIEN met Read in een uitsnede van de ridder: munten en randen duidelijk scherper dan de 1x-render met ontruisen.
- Nog open voor een volgende ronde: de hoge hoed rechts staat los aan de rand; OF THE FALLEN zit dicht bij de helm van de ridder; klein snapt een frisse kijker zonder de header nog niet altijd (helm = helm leest als "maatjes").

## Ronde 6 (14 nov ±14:40 tot 15:00 UTC, Daan zelf, want Mila staat uit)
Daans twee moet-punten van 12:50 verwerkt in `capsule3d.py`, zodat de capsule klaar is voor het blad van Thijs (ma 16 nov):
- **Ridder kijkt naar Gloop:** `RIDDER_DRAAI` standaard -40 (was 50; hoger draaide hem juist weg). Zijn schild leest nu als rood schild met gouden rand, niet als tweede munt.
- **Zelfde pluim op beide helmen:** op Gloops helm nu precies de pluim van de ridder uit `held.py` (vier bollen die half overlappen en omkrullen), gespiegeld en x1,64 groter (helm 0,63 tegen 0,385). Hij komt links uit de helm, onder de kroon, en krult naar buiten en omhoog. Klein had al de pluim uit `gloop.py` (1 hoed) en is daarom alleen opnieuw gerenderd voor de draai.
- Alle drie opnieuw met `maak_alles.sh` (header en hoofdbeeld daarna nog eens na het vastzetten van de pluim aan de helm). Voor en na: `voor-na-ronde5-ronde6.png`.
- **Frisse kijker (Agent, met Read, wist niets):** header 7,5 en hoofdbeeld 7,5 (ronde 5: 6), grap na 3 tot 4 s: "het ridderje ziet dat zijn eigen soort helm al in de verzameling zit, hij is de volgende"; ridder kijkt naar het monster. Klein 6: daar leest één helm als "familie". Zijn punt "pluim oogt als losse bolletjes" was op de render waar de pluim nog los naast de helm stond; daarna vastgezet.
- **Nog open (kan, versie 2):** kroonpunten prikken door de rand van de heksenhoed; losse munt links van het schild; klein toont alleen de helm (de proef met een tweede hoed scoorde niet beter, zie ronde 5).

## Ronde 6b (14 nov ±14:40 tot 15:05 UTC, Mila, tegelijk met Daans ronde 6)
Ik werkte dezelfde twee moet-punten uit terwijl Daan dat ook deed (hij dacht dat ik uit stond). Draai -40 is gelijk aan Daan. Verschil zit in de pluim, en kan 3 erbij:
- **Pluim als één gladde krul.** Daans versie (vier bollen van de ridder x1,64) leest op groot nog als losse bolletjes. Nu dezelfde lijn als bij de ridder (eerst omhoog, dan om), als boog van negen bollen dicht op elkaar, gespiegeld naar de ridder toe, links onder de kroon uit.
- **Heksenhoed 0,2 hoger** (`HEKS_OP`, Daan kan 3): de kroonpunten prikken niet meer door de rand.
- `header-ronde6-920x430.png` is Daans ronde 6 ter vergelijking; `voor-na-ronde6-ronde6b.png`: links ronde 6, rechts 6b, onder klein (gelijk gebleven: klein heeft maar 1 hoed en daar staat al de pluim uit `gloop.py`).
- **Frisse kijker (Agent, met Read, A = ronde 6, B = 6b), letterlijk:** A "drie losse rode bolletjes in een kromme rij, een beetje als een rups, een rij ballonnetjes of een tros bessen"; B "één doorlopende gebogen pluim met ribbels ... lijkt veel meer op de pluim van het ridderje ... je snapt meteen dat dit de helm van een eerder ridderje is". A 7, B 8. Zijn punt over B: de krul is klein en zit deels achter de kroon. Over de kroonpunten: in beide ziet hij gouden puntjes net onder de rand, niet erdoorheen.
- **Besluit: 6b wordt de header en het hoofdbeeld.** Waarom: de pluim is de hele grap (zelfde helm), en die leest nu als pluim en niet als rups; frisse kijker 8 tegen 7. Klein blijft Daans render (beeld is gelijk).
- GEZIEN met Read: header 6b heel, uitsnede van de toren 2x, voor/na, hoofdbeeld 6b.

## Bibliotheek 600x900 en staand 748x896 in 3D (14 nov ±18:00 UTC, afspraak met Daan van 15:45)
Script: `staand3d.py` leest `capsule3d.py` (zelfde aanpak als Daans `winkel3d.py`), vervangt titel, camera, wand en een paar plekken. `capsule3d.py` zelf is niet veranderd, dus header, klein, hero en logo blijven gelijk.
- **Idee:** staand is het formaat van de toren. Gloop onderaan op het goud met de **volle toren van vier hoeden** (helm met pluim, kroon, heksenhoed, rode muts; zoveel draagt hij in het spel), de ridder linksonder met dezelfde helm, bovenaan de titel met **op elke letter een hoed uit het spel**, net als Daans 3D-logo (kroon, heksenhoed, koksmuts, veermuts). De toren wijst omhoog naar de titel.
- **Besluit: de hoeden op de letters ook hier.** Waarom: Daan vroeg het, en zo is de titel zelf al de grap (HATS met hoeden); het pixellogo deed dat ook, dus herkenbaar.
- **Besluit: camera staand, lens 52, vlak voor de groep.** Lens 40 (proef 1) liet een lege paarse muur tussen titel en Gloop; dichterbij vult Gloop de onderste helft.
- Ronde 1 (`bibliotheek-ronde1-600x900.png`, GEZIEN met Read) en `vergelijk-bibliotheek-toppers.png` (ronde 1 en de oude pixelversie naast Rusty's, Tiny Pasture en Ropuka op 200x300, zoals de bibliotheek).
- **Frisse kijker op ronde 1** (agent, alleen de rij en het beeld): valt als tweede op in de rij van vijf (na Tiny Pasture, vóór Rusty's en Ropuka). Letterlijk: "een slijmmonster met één oog draagt een torentje van gestolen hoeden op een berg goud. Een klein ridderje kijkt geschrokken toe, want zijn helm-pluim zit nu op de pan van het monster. Die grap snapte ik binnen 2 tot 3 seconden." De pixelversie kreeg 4 ("lijkt een fles met een hoedenstapel"), 3D een **7**. Moet: ondertitel groter, ridder groter. Kan: lucht tussen toren en titel, hoge hoed rechts weg (overbodig grijs blok), fakkel voegt weinig toe.
- **Ronde 2:** ondertitel 0,62 naar 0,78, ridder 1,2 naar 1,45, hoge hoed weg (de pan blijft rechts op de berg), titel iets hoger, Gloop 1,32 naar 1,28 voor lucht onder de titel. Proef GEZIEN met Read.
- Nog bekend (kan): de kroonpunten prikken net door de rand van de heksenhoed, net als op de header vóór ronde 6b; de heksenhoed staat in `staand3d.py` niet hoger dan in de header.
- **Ronde 2 op vol formaat** (render 2x, 32 samples, verkleind): `bibliotheek-600x900.png` en `staand-748x896.png` (staand: zelfde opstelling, lens 50, de bredere beeldhoek laat rechts de tweede fakkel zien). Beide GEZIEN met Read; de rij `vergelijk-bibliotheek-toppers.png` toont nu ronde 2, ronde 1, pixel, Rusty's, Tiny Pasture, Ropuka. Eigen oordeel: ridder en ondertitel lezen nu op 200x300, de helmgrap staat erin. Zwakker dan Tiny Pasture: die is lichter en voller.
- Nog te doen: in `ontwerp/steam/winkelpagina/` zetten na de ja van Thijs op het blad (de pixelversies blijven tot dan staan, net als Daans hero en logo).
- Ronde 3 geprobeerd (niet bewaard): heksenhoed hoger (`HEKS_OP` 0,34) en de achterste kroonbolletjes weg. 2x uitgesneden GEZIEN: de punten prikken nog steeds net door de schuine rand, en hoger geeft een gat tussen kroon en hoed. Teruggedraaid, zodat script en beelden gelijk blijven. Volgende keer: de kroonpunten in de toren korter (0,85) in plaats van de hoed hoger; alleen zichtbaar bij uitvergroten, dus geen moet.

## 14 nov ±20:58 UTC (Mila): ronde 3 warmere wand (kan Daan 18:28), niet gewonnen
- `staand3d.py` kan nu een warmere, lichtere wand met een fakkelgloed achter de titel (`ST_WARM=1`). Twee varianten gerenderd (bpy 4.2, 600x900, 16 samples): B roze-warm, C oranje-bruin. Op de plank naast Rusty's, Ropuka en Tiny Pasture op 200x300: `proef-ronde3-warme-wand-plank-200x300.png` (A is ronde 2). GEZIEN met Read.
- **Frisse kijker** (blind, alleen A/B/C): A 8, B 6, C 6. De koele paarse wand steekt juist af tegen de lichte, warme buren, en het gele HATS heeft daar het meeste contrast; op warm vloeit het geel weg.
- **Besluit: ronde 2 blijft**, `ST_WARM` staat standaard uit, zodat `bibliotheek-600x900.png` en `staand-748x896.png` niet veranderen. Waarom: Daan vroeg "houd alleen wat wint", en de warme wand won niet.
- Kan van de kijker: "OF THE FALLEN" is op tegelformaat net leesbaar; mogelijk later iets dikker.

## 15 nov ±15:40 tot 16:05 UTC (Mila): capsules in kleur H (punt 1 Thijs: minder paars en donker)
Het spel is sinds vandaag warm (kleur H op main). Een paarse capsule zou dus niet meer laten zien wat er in het spel zit. Daarom staat `capsule3d.py` nu standaard op kleur H (`CAPSULE_KLEUR=pruim` geeft de oude kleuren terug).
- **Wand** ruis 5e3a30 tot 7e5244 (warm bruin, iets donkerder dan de kamerwand van het spel, zodat goud, Gloop en de gele titel loskomen), vloer 4a2a20 tot 6e4033, voetrotsen en kiezels uit de aardekleuren van H, titelrand donkerbruin 2a120c in plaats van pruim, lucht warm donker. Warme lamp achter Gloop 500 werd 350: op de lichtere wand gaf 500 een feloranje vlek waarin het goud wegviel.
- Drie wanden geprobeerd op 920x430 (GEZIEN met Read): kamerwand 7a4a3a/9e6a56 met lamp 500 (te fel, goud valt weg), aarde 684033/8e5949 met lamp 280 (zalmroze), en 5e3a30/7e5244 met lamp 350 (gekozen: leest als warme grot, zoals de strook).
- **Blinde kijker** (Agent, rij met Rusty's, Tiny Pasture, Bongo Cat en Ropuka, oud paars A tegen warm B): A 19, B 20, kiest B ("de schat ziet er echt uit als goud, oogt rijker"). Zijn moet: OF THE FALLEN verdween half in het warme. Daarom die regel 0,70 werd 0,72, iets naar links (anders raakte de N de pluim van de ridder) en een dikkere donkere rand (0,07 werd 0,11 van de lettermaat). GEZIEN met Read.
- Eerlijk: paars viel in de rij iets meer op omdat geen buur paars is (kijker 7 tegen 6). Warm wint op rijkdom en is wat het spel nu is.
- Vol formaat met `maak_alles.sh` (2x gerenderd, verkleind): header, klein en hoofdbeeld GEZIEN met Read; voor en na: `voor-na-pruim-kleur-h.png` (links oud, rechts H, onder klein).
- Nog open (kan, volgende run): figuren groter in het vak (kijker: Gloop met toren 20 tot 30% groter; nu nog veel muur), en bibliotheek en staand (`staand3d.py`) in kleur H.

## 15 nov ±16:00 tot 16:25 UTC (Mila, extra run): bibliotheek 600x900 en staand 748x896 in kleur H
`staand3d.py` leest `capsule3d.py`, dus de warme wand, vloer en titelrand komen vanzelf mee. Eén wijziging in `staand3d.py`: de dikkere donkere rand om OF THE FALLEN (0,11 van de lettermaat) in kleur H, net als op de header.
- Proef op 1x, oud en nieuw naast elkaar, GEZIEN met Read. Opbouw gelijk aan ronde 2 (toren van vier hoeden, ridder linksonder, hoeden op de letters).
- **Blinde kijker** (Agent, plank met Rusty's, Tiny Pasture, Bongo Cat en Ropuka op 200x300): paars A 21, warm B 22, kiest B ("warmer, meer af, als een echt spel"). Paars valt op de plank iets meer op (7 tegen 6) omdat het de enige paarse tegel is; dat hangt af van de buren. Zijn moet: meer contrast achter de titel in het warme (donkerder vlak of zachte schaduw). Staat open voor de volgende run.
- Vol formaat gerenderd op 2x, 32 samples, verkleind met Lanczos: `bibliotheek-600x900.png` en `staand-748x896.png`, allebei GEZIEN met Read.
- Op 14 nov verloor een warme wand (`ST_WARM`, roze-oranje achter de titel) nog van paars (6 tegen 8). Het verschil nu: het hele beeld is warm zoals het spel, met een donkerdere bruine wand in plaats van een lichte gloed achter de titel.

## 15 nov ±17:35 tot 18:20 UTC (Mila, extra run): moet hoofdbeeld en kan bibliotheek (keuring Daan 16:40)
- **Hoofdbeeld 1232x706:** `capsule3d.py` kent nu de variant `hoofd` (`maak_alles.sh` gebruikt hem). Het hoofdbeeld is hoger dan de header, dus met dezelfde camera kwam er lege muur en vloer bij. Nu: Gloop dichter bij het midden (GX 2,35 werd 1,8), ridder dichter bij Gloop (RX -0,6), Gloop met toren 1,1 werd 1,2 en ridder 1,2 werd 1,3, camera lens 42 werd 47 en iets lager gericht, titel iets hoger zodat de pluim van de ridder de N niet raakt. Samen ±25% groter in beeld. Getallen staan als omgevingsgetallen `HF_*` in het script. Header en klein veranderen niet.
- Drie proeven op 616x353 GEZIEN met Read (`b`, `c`, `d`); `d` gekozen: pluim vrij van de titel, voeten met marge, heksenhoed niet afgesneden.
- **Blinde kijker** (Agent, oud en nieuw op 616x353): nieuw 7, oud 6, kiest nieuw ("titel, ridder en slijm groter en dichter op elkaar, de grap leest direct").
- **Bibliotheek en staand (`staand3d.py`):** zachte donkere vlek op de wand achter de titel (vlak dat naar de rand doorzichtig wordt, `ST_SCHADUW`, sterkte `ST_SV_A` 0,85), titel 0,25 lager (minder gat naar de toren), camera iets lager gericht zodat de figuren omhoog komen, ridder naar binnen (ST_RX 0,15 werd 0,4, schild weg van de rand). Sterkte 0,6 en 0,85 naast elkaar GEZIEN; 0,6 zag je bijna niet.
- **Blinde kijker** (200x300): oud 7, nieuw 7, kiest nieuw ("rustiger, titel en slijm lezen schoner"). Klein verschil, maar het lost Daans kan en de moet van 16:20 op zonder iets te verliezen.
- Les: een plat vlak heeft in Blender geen diepte in `Generated`; een bolvormig verloop moet de z dan op 0 zetten, anders is het overal 0.

## 15 nov ±20:40 tot 20:55 UTC (Mila): moet hoofdbeeld, pluim vrij van de N (keuring Daan 18:50)
- Titel 0,08 hoger (`HF_TZ` 0,32 werd 0,40) en ridder iets naar rechts (`HF_RX` -0,6 werd -0,25). Alleen titel hoger lukte niet: HATS staat al bijna tegen de bovenrand, en 12 px hoger raakte de pluim nog steeds. Ridder kleiner (`HF_RS` 1,2) gaf ook vrij, maar dan wordt de held weer klein; dat wilde ik niet.
- Vijf proeven (a tot e) GEZIEN met Read; `d` gekozen. Nu zit er ±15 px lucht tussen de punt van de pluim en de N, de ridder staat nog los van Gloop. Header, klein, bibliotheek en staand veranderen niet.
- Voor en na (links oud, rechts nieuw, uitsnede van de titel): `voor-na-pluim-15nov.png`, GEZIEN met Read.

## Volgende ronde (Mila 16 nov ±18:15 UTC, uit de beeldmap)
GEZIEN: `klein-462x174.png` op 231 x 87 tussen zeven toppers (`platformen/steam/kennisbank/beeldmap.md`). Drie dingen: (1) titel groter, "OF THE FALLEN" leest bijna niet, bij de toppers vult de titel 60 tot 80% van de breedte; (2) de helm op Gloop is daar ±14 pixels breed: hij moet het grootste ding op de capsule worden (Bongo Cat verkoopt ook hoeden en toont ze enorm); (3) minder goud op bruin, want dat ligt dicht bij Don't Rob My Dungeon; meer groen van Gloop.
- Proef 1 (zelfde run): alleen de titel groter in klein (`K_HATS` 2,25, `K_OTF` 1,12, standaard blijft 2,0 en 0,86). GEZIEN in `proef-klein-titel-groter.png` (links nu, rechts proef, onder op 231 x 87): OF THE FALLEN leest beter, maar de N loopt in de helm van de ridder. Niet gekozen. Volgende proef: ridder weg uit klein (Gloop met helm alleen is de grap al) of ridder achter Gloop, dan past de grote titel wel.

## Ronde 7 klein (Mila 16 nov ±18:40 tot 19:00 UTC, uit de beeldmap)
- **Nieuw `klein-462x174.png`** (oud bewaard als `klein-ronde6-462x174.png`). Titel ±22% groter (HATS 2,45, OF THE FALLEN 1,08), ridder van links naar rechts naast Gloop (kijkt naar zijn helm op Gloop, draai 55), zodat de grote titel links vrij staat; helm op Gloop 1,1x; wandlamp 350 naar 180, zodat de gele titel loskomt van de wand. Alles als standaard in `capsule3d.py` (K_* getallen), `maak_alles.sh` maakt hem zo.
- GEZIEN met Read: `voor-na-klein-ronde7.png` (op 462 en 231) en `vergelijk-klein-ronde7-toppers.png` (rij 2 oud, rij 3 nieuw, tussen de toppers).
- **Blinde kijkers** (drie Agents, 231 x 87): (1) ridder rechts klein met helm 1,7x: oud 6, nieuw 5 ("ridder is een vlek", grote platte helm leest als pan); (2) ridder kop eerst in de munten, kaal (de valhouding uit het spel): oud 6, nieuw 5 (op 231 onleesbaar, titel geel op oranje gloed); (3) deze versie: **nieuw 6, oud 5**, gekozen ("één duidelijk middelpunt, titel helemaal leesbaar").
- Lessen: de helm groter schalen maakt van de rand een bolhoed of pan; 1,1x is de grens. Een groene lamp maakt de wand bleker, niet groener. De valhouding is op 231 px te klein om te lezen.
- **Nog open (alle drie de kijkers):** de achtergrond is vlak bruin-oranje en verdwijnt naast Rusty's, Tiny Pasture en Don't Rob My Dungeon; en "fallen" zie je niet (de ridder leeft). Volgende proef: (a) een koelere of donkerdere achtergrond met een lichte rand om de figuren; (b) een tweede, kleinere hoed op de berg (een stapel hoeden zegt "verzameld van gevallen helden").
- **Ronde 7b, proeven die niet helpen (GEZIEN, niet gekozen):** twee hoeden op de berg (`K_BERG=1`): op 231 onzichtbaar, de hoge hoed verdwijnt achter de ridder. Donkerdere wand (`CAP_WAND1/2`) en minder wandgloed (`K_WANDGLOED` 350, wandlamp 60): het bruin blijft bijna gelijk. Het vlakke bruin zit dus niet in een lamp maar in het warme palet zelf (kleur H). Een echte oplossing is groter: bijvoorbeeld een tweede kleurvlak (het groen van Gloop of een koele nacht door een gat in de grot) achter de figuren. Dat raakt het kleurbesluit H, dus eerst een proef naast de toppers en dan Daan.

## Ronde 7c klein (Mila 16 nov ±19:45 UTC, kan-punt Daan 19:50 en controleur)
- Ridder stond met zijn voeten in de onderrand (op klein een bol met helm) en was in grijs op halve grootte een vlekje. Nu: ridder iets naar achter en rechts (`K_RY` -0,9 werd 0,0, `K_RX` 5,05 werd 5,35) en groter (`K_RS` 1,35 werd 1,6), zodat zijn laarzen op de grond staan en hij los van Gloop staat; plus een eigen lichtje `K_RLICHT` 700 (nieuw, alleen klein; in 7e weer uit). De titel is niet geraakt.
- Proeven a tot g (16 samples) GEZIEN met Read op 462 en in grijs op 231: alleen hoger (b) schoof hem half achter Gloop; met naar rechts (e, g) staat hij vrij; g met het meeste licht leest in grijs het best. Gekozen g.
- GEZIEN met Read: `voor-na-klein-ronde7c.png` (links ronde 7, rechts 7c, onder op 231 in kleur en grijs). Oud bewaard als `klein-ronde7-462x174.png`. Header, hoofdbeeld en bibliotheek veranderen niet (alle getallen zijn `K_*`).
- **Ronde 7d, proef tweede kleurvlak (GEZIEN, niet gekozen):** nieuwe optie `K_HALO` (standaard uit) zet een zachte gloed op de wand achter Gloop (`K_HALOKLEUR`, `K_HALOW`, `K_HALOZ`). Groen 2fbf5a en blauw 3a6cff geprobeerd. In de rij met de toppers (`proef-klein-halo-toppers.png`, links groen, rechts blauw, rij 2 is 7c) maakt de gloed het beeld melkig en vaag: Gloop verliest zijn eigen groen tegen een groene gloed, de ridder zijn blauw tegen een blauwe. 7c zonder gloed springt er juist meer uit, omdat warm oranje tussen de blauwe en groene toppers al anders is. Les: het "vlakke bruin" lossen we niet op met licht op de wand; als er iets moet, dan een echt ding met een harde rand (bijvoorbeeld de stenen boog uit het spel achter de figuren), niet een waas.
- **Ronde 7e, bijgesteld na een blinde kijker (Mila 16 nov ±19:55 UTC).** Blinde kijker (Agent, rij met toppers, `blind-ronde7.png` tegen `blind-ronde7c-licht.png`): ronde 7 een 7, 7c met het lichtje een 5: "lichtblauw/wit bolletje zonder duidelijke helm, leest als een geest". Het lichtje bleekte de ridder uit. Daarom: lichtje uit (`K_RLICHT` standaard 0) en ridder meer in profiel naar Gloop (`K_RDRAAI` 55 werd 75), plek en maat van 7c blijven (laarzen op de grond). Proeven m1 tot m3 GEZIEN met Read; m2 gekozen.
- Tweede blinde kijker (`blind-ronde7e.png` tegen ronde 7): 5 tegen 5, "geen verschil, figuurtje net herkenbaar als poppetje met helm en pluim". Dus 7e is niet slechter dan 7 en lost Daans kan op (laarzen op de grond, groter); het "vlekje in grijs" is maar een beetje beter. `klein-462x174.png` en `voor-na-klein-ronde7c.png` zijn nu 7e.
- Les: extra licht op een klein figuur maakt hem bleek, niet duidelijker; contrast komt uit zijn eigen kleuren (blauw lijf, rode pluim) en uit het profiel.
- **Proef kleurgrading (GEZIEN, niet gekozen):** `proef-klein-kleurgrading-toppers.png` (linksboven 7e, rechtsboven contrast 1,15 en kleur 1,2, linksonder dat plus donkere randen, rechtsonder alleen donkere randen). Zelf vond ik linksonder voller; een blinde kijker zag tussen 7e en linksonder geen verschil (6 en 6). Dus niet doen: het zou alleen de header en het spel uit de pas brengen.
- **Wat de kijkers wel steeds zeggen:** Tiny Pasture en Bongo Cat winnen met één grote schattige hoofdfiguur; bij ons is Gloop klein tussen veel oranje en goud. Volgende proef voor klein: Gloop veel groter (half tot tweederde van de hoogte, zoals de kat van Bongo Cat), minder munten in beeld, titel blijft.
- **Proef Gloop groter (GEZIEN, niet gekozen):** nieuwe optie `K_GROOT` (standaard 1,3). `proef-klein-gloop-groter.png`: links 7e, midden 1,55 met camera hoger (`K_CZ` 2,45), rechts 1,45. Gloops gezicht wordt groot en lief, maar de ridder komt weer met zijn voeten in de onderrand. Blinde kijker: 5 tegen 5, "geen verschil". Niet gekozen.
- **Belangrijkste les van deze run (twee van de vier kijkers zeggen het):** de helm op Gloop leest op 231 px als een **serveerkoepel of cloche**, niet als ridderhelm. Dan valt de grap weg ("slijm draagt een serveerhoed"). Grootte, licht en kleur veranderen weinig; dit is het echte werk. Volgende proef: de helm moet ridder zeggen, bijvoorbeeld een donkere vizierspleet of een neusstuk op de helm, en dezelfde rode pluim als de ridder (die heeft hij al). Eerst kijken of het vizier ook in het spel op de ridderhelm staat (`hoeden.py`); zo niet, dan in het spel en de capsule tegelijk, anders is het niet eerlijk.
- **Proef helm moet ridder zeggen (GEZIEN, niet gekozen, eerste poging):** opties `K_HELMRIDDER=1` (donkere band met gouden klinknagels op de rand, gouden kam over de bol) en `K_HELMRAND=0` (platte rand weg), standaard uit. `proef-klein-helm-ridder.png`: linksboven 7e, rechtsboven band en kam, linksonder zonder rand, rechtsonder beide. Band en kam maken er een **vliegende schotel** van (de ring met lichtjes rond de rand), slechter dan de cloche. Zonder rand is het een kale kom. Les: versiering op de rand maakt het niet ridderlijker; de vorm zelf moet anders. Volgende poging: diepere helm die over het voorhoofd zakt met een neusstuk naar beneden (tussen oog en helm), smallere rand, zelfde helm ook op de ridder in `hoeden.py`/`held.py`, anders klopt het niet met het spel. Na de speeltest van za 21 nov, want het raakt de pijplijn van Bram en Olaf.

