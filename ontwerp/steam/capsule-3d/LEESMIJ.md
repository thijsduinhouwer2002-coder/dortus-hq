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
