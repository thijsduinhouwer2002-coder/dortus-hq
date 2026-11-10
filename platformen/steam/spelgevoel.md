# Het Hol: spelgevoel en toetsen van het prototype (Sanne)

Hier toets ik elke GIF en elke schermafbeelding van het prototype: is het leuk, is het duidelijk, is het grappig. Nieuwste bovenaan. Wat er in het spel hoort staat in `features.md`.

## Toets 7: de film van main met de afloop van de wrok, 10 nov 2026 (run 42728963292, commit 4be7165, main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/main/`, commit d64caf8, 1024 x 120, 298 beelden, 60 s), twee bladen met een beeld per 3 s, ingezoomd op 39 tot 46 s en 46 tot 60 s, `film/film.log`, `cpu.txt` (1,13 CPU-s per 10 s, 115 MB).

**Wat nu goed is:**
- **De wrok heeft een afloop, en die leest.** Bram vlucht (26,1 s, "Grudge: the Spike Pit."), komt terug met het grijze boze wolkje boven zijn helm (33,7 s), loopt door het hol naar de put, valt erin (42,5 s, stekels omhoog), de muntjes vliegen naar de schat en de teller springt van 12 naar 21 met "Bram came back. The Spike Pit won. +9" (43,2 s). Dit is de beste grap van de minuut en het verhaal van onze winkelpagina in negen seconden. Punt 1 van toets 6 is opgelost.
- **Elke held een eigen hoed:** Kees koksmuts, Bram helm met rode kam, Odo kroon, Tibbe bruine hoed, Mara grijze pet, Lotte hoge hoed. Je ziet in één minuut dat er veel hoeden zijn. Punt 2 opgelost.
- **De drukke stap loopt gelijk:** Tibbe raakt de schat terwijl Gloop plat ligt (36 tot 37 s) en de regel staat er in hetzelfde beeld (37,3 s). Punt 3 opgelost.
- **CPU** 1,13 CPU-s per 10 s op Actions (toets 6: 1,49; Olafs vorige run 0,81). Het verschil tussen twee runs van bijna dezelfde code is ruis van de Actions-computer; ruim zuinig. Punt 4 klaar.

**Wat niet goed is (in volgorde van belang):**
1. **De laatste 13 seconden hebben geen afloop.** Mara komt binnen rond 46 s, haar eigen regel vervalt ("kroniek vervallen 48.0: Mara read about you in a tavern."), en ze loopt 13 s naar Gloop terwijl er verder weinig gebeurt (Tibbe keert om, Lotte klopt aan). De hap valt in het laatste beeld (59,8 s, alleen in de film te zien, niet in de log); de kijker ziet hem niet en er komt geen regel. Een minuut die eindigt met iemand die loopt, voelt als afgeknipt. **Eis voor de demo:** Mara wordt opgegeten rond 52 tot 55 s, met de regel en de hoed die op de toren komt (dan zie je de toren groeien, punt 6 van toets 4). Bijvoorbeeld `snelheid` 1.4 voor haar, of haar 5 s eerder laten binnenkomen nu de Hoard-Toucher eerder klaar is. Haar binnenkomst-regel mag dan vervallen. **Voor Olaf.**
2. **De val zelf duurt één beeld.** Bram is op 42,5 s half doorzichtig in de stekels en een beeld later weg. Het moment waar de hele wrok naartoe werkt, verdient ongeveer een seconde: stekels omhoog, Bram zakt zichtbaar weg, het boze wolkje knapt als een poef (of wordt een klein wit vlaggetje). Dan lacht een kijker op het goede moment in plaats van te denken dat hij iets miste. **Voor Mila** (poef of vlaggetje, een paar beelden) **en Olaf** (stekels en wegzakken langer).
3. **Tibbe keert meteen om.** "Tibbe ran off, giggling." op 47,9 s en "Tibbe is back for Gloop." op 50,7 s; in beeld klimt hij de ladder op en direct weer af. Dat leest als een fout, niet als een terugkomer. In het echte spel is het goed (daar zit er tijd tussen), maar in de demo liever geen tweede terugkomer, of minstens 8 s ertussen. En als hij terugkomt, met zijn bijnaam: "Tibbe the Hoard-Toucher is back for Gloop." (`_held_naam()` in strook.gd geeft dat al). **Voor Olaf, klein.**
4. **Paneel:** nog altijd ±320 van de 1024 px. Blijft bij Mila en Olaf (geen nieuwe eis).

**Winkeltekst:** hoogte en klikken zijn nu waar in de build (rechtsklik wisselt 96, 120, 160; klikken gaan door lucht en gras, `kern/strook.gd`). De zin in `ontwerp/steam/winkelpagina/teksten.md` volgt nu precies de build.

**Oordeel:** de minuut heeft nu een begin, een midden en een clou. Met punt 1 en 2 is dit de demo-minuut die ik ook in de trailer zou willen zien.

## Toets 6: de film van main na de kroniek-wachtrij, 10 nov 2026 (run 42723851206, commit 4c7bd5d, main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/main/`, commit 8c9397e, 1024 x 120, 298 beelden, 60 s), twee bladen met een beeld per 3 s, `film/film.log`, `cpu.txt` (1,49 CPU-s per 10 s, 114 MB).

**Wat nu goed is:**
- **Tekst en beeld lopen samen.** Kees valt en in hetzelfde beeld (12 s) vliegen de muntjes naar de schat, gaat de teller van 0 naar 6 en staat er "Kees fell to the Spike Pit. +6". Punt 1 van toets 5 is opgelost; het was verdringen, zoals Olaf vond.
- **Geen grap twee keer:** "read about you in a tavern" staat er nog maar één keer in (Joost, 44 s). Punt 3 opgelost.
- De kroon blijft de haak: Gloop met kroon vanaf 27 s, plat met de kroon naast zich (33 tot 40 s), "Gloop is up again. Wobbly." Het hol groeit zichtbaar naar links (ingang schuift van ±150 naar ±50 px).
- De Hoard-Toucher eindigt nu binnen de minuut: "Ties the Hoard-Toucher ran." (50,6 s).

**Wat niet goed is (in volgorde van belang):**
1. **De wrok heeft geen afloop.** Bram komt terug ("Bram is back for the Spike Pit.", 33,7 s, met het boze teken boven zijn helm) en daarna staat er "Bram escaped with a limp." (53,1 s). De kijker ziet hem dus nooit krijgen wat hij zocht. Dit is ons eigen stuk en de beste grap van de minuut ligt open: hij komt terug voor de put en valt erin. **Eis voor de demo:** de terugkomer valt in precies de val waar hij een wrok tegen heeft, met een eigen regel, bijvoorbeeld "Bram came back for the Spike Pit. The Spike Pit won. +6". In het echte spel mag hij soms weer ontsnappen (dan groeit de wrok naar aartsvijand), maar in de demo-minuut moet de grap af zijn. **Voor Olaf** (demo in `strook.gd`) en **Bram** (de regel in `kroniek_regels.gd`).
2. **Bijna iedereen draagt de paarse puntmuts.** Rond 45 s lopen drie van de vier helden met dezelfde paarse muts; Ties, Bram (bij binnenkomst) en Joost lijken op elkaar. De hoeden zijn de haak van de winkelpagina en de trailer. **Eis voor de demo:** elke vaste held in de demo-minuut een andere hoed uit Mila's tien (kroon blijft bij Odo; daarnaast bijvoorbeeld koksmuts, emmer, koekenpan, helm), zodat de minuut zelf laat zien dat er veel hoeden zijn. **Voor Olaf** (demo) en **Mila** (welke vijf het best lezen op 120 px).
3. **Nog 3 tot 4 s achter in de drukke stap.** Ties staat rond 30 tot 33 s met een uitroepteken bij de schat, maar "Ties is now the Hoard-Toucher." komt pas op 36,3 s (wacht 1,1 s na twee andere regels). Olafs verklaring (de demo laat vier dingen binnen 2 s gebeuren) klopt; met punt 1 erbij wordt het drukker. Voorstel: de Hoard-Toucher 4 s later laten binnenkomen, net als de terugkomer.
4. **CPU van 1,16 naar 1,49 CPU-s per 10 s** (toets 5 naar nu, zelfde hoogte). Nog ruim zuinig, maar 28% meer in één dag; Olaf, kijk of iets elk beeld tekent wat stil staat.
5. **Paneel:** nog altijd ±320 van de 1024 px. Blijft bij Mila en Olaf.

**Oordeel:** de minuut klopt nu als film: wat je ziet, lees je. Wat nog ontbreekt is de clou van onze eigen grap (punt 1) en dat de minuut de hoeden laat zien (punt 2). Met die twee is dit de film waar de trailer uit gesneden kan worden.

## Toets 5: de film van main met kroon en muntje, 9 nov 2026 (run 42714582677, commit 4b51856, main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/main/`, commit 9499a26, 1024 x 120, 298 beelden, 60 s), een strook van het rechterdeel per 2 s met de tijd erbij, drie uitsneden van Gloop drie keer vergroot (28 s, 34 s, 60 s), `film/film.log` en `cpu.txt` (1,16 CPU-s per 10 s, 115 MB; iets meer dan 1,09 bij toets 4, nog ruim zuinig).

**Wat nu goed is:**
- **De kroon is de haak die we zochten.** Vanaf 28 s staat Gloop met een gouden kroon met rode steen; op ware grootte lees je meteen "dit slijm heeft een koning opgegeten". Als hij plat gaat (32 tot 40 s) ligt de kroon naast hem en staat hij er weer mee op. Punt 2 van toets 4 is opgelost.
- **De Hoard-Toucher komt nu op tijd bij de schat:** Ties (paarse puntmuts) staat rond 34 tot 36 s bij de berg met een uitroepteken boven zijn hoofd. Punt 4 van toets 4 is in het beeld opgelost.
- **De terugkomer zegt waarom:** "Bram is back for the Spike Pit." (26 s). Punt 3 opgelost. De wand-regel is weg (punt 1).
- **Muntje plus getal** in het paneel leest beter dan "Hoard: 21 gold". Een tweede opgegeten held (Joost) zit er aan het eind in.

**Wat niet goed is (in volgorde van belang):**
1. **De kroniek loopt tot 18 s achter op het beeld.** Ties raakt de schat aan rond 35 s, maar "Ties tried to lift it. Too heavy." staat er pas van 52 tot 57 s; op het moment zelf staat er "Gloop is flat. Back soon." Kees valt rond 10 s (goud van 0 naar 6), maar "Kees fell to the Spike Pit. +6" zie je in geen enkel beeld per 2 s; "Bram fled. Grudge: the Spike Pit." ook niet. Intussen staan de binnenkom-regels lang: "Odo is here for your gold." 12 tot 18 s, "Ties read about you in a tavern." 20 tot 24 s, "Joost has a map. It is wrong." 44 tot 48 s. De grappen over wat er **gebeurt** missen dus, die over wie er **binnenkomt** staan er lang. **Besluit (spelgevoel, mijn deel):** een regel over wat er gebeurt (gevallen, opgegeten, gevlucht, terug, schat, hoed) gaat altijd voor en verschijnt binnen 1 s na het beeld; een binnenkom-regel mag alleen als er niets wacht, en vervalt als hij niet binnen 3 s aan de beurt is. Een regel staat minstens 2,5 s (leesbaar) en hooguit 6 s. **Voor Olaf** (`kern/strook.gd`, de rij van de kroniek): jij kiest hoe.
2. **De tweede hoed zweeft.** Aan het eind (60 s) hangt Joosts rode hoofdband als een los rood streepje een paar spelpixels boven de kroon, niet erop. Dat leest als een fout, en juist de groeiende toren moet kloppen. **Voor Bram** (`slijm.gd`, stapelen) en **Mila** (`HOED_TOP` en `HOED_ONDER` van de platte hoeden): de onderkant van hoed 2 moet in de bovenkant van hoed 1 vallen, ook als hoed 1 een kroon is.
3. **Dezelfde grap twee keer in een minuut:** "read about you in a tavern" bij Ties (20 s) en Lotte (50 s). In de demo-minuut geen binnenkom-regel twee keer; in het spel niet binnen de laatste 10 regels. **Voor Bram** (`kroniek_regels.gd`, of wie de regel kiest).
4. **De Hoard-Toucher eindigt nog niet:** door punt 1 valt "Ties the Hoard-Toucher ran." buiten de minuut. Lost zichzelf op met punt 1.
5. **Paneel:** nog ±320 van de 1024 px (bijna een derde), met veel lege ruimte achter de tekst. Staat bij Mila (20:55) en Olaf.

**Oordeel:** het beeld is nu goed genoeg voor de winkel: kroon op Gloop, Hoard-Toucher, terugkomer, alles in een minuut. Wat ontbreekt is dat de tekst gelijk loopt met het beeld, en dat is het verschil tussen "leuke poppetjes" en "ik moest lachen". Na punt 1 en 2 kan Olaf hier de beelden voor de winkelpagina uit halen.

## Toets 4: de eerste tien minuten en de eerste hoed, 9 nov 2026 (run 42701685818, commit 6db37a1, tak `claude/steam-hol-begin`, nog niet op main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/claude-steam-hol-begin/`, 1024 x 120, 298 beelden, 60 s; eerste beeld 0,6 s), een blad met een beeld per 5 s, uitsneden drie keer vergroot (Gloop met hoed, Gloop plat, het boze teken), `film/film.log`, `cpu.txt` (1,09 CPU-s per 10 s, 114 MB) en `strook-96.png`, `strook-160.png`.

**Wat nu goed is (punt 1, 3 en 6 van toets 3 opgelost):**
- **Ons eigen stuk zit in elke film.** In 60 s: Kees valt in de put (+6), Bram vlucht met een wrok, Odo wordt door Gloop opgegeten ("Gloop ate Odo. Burp. +6", "Gloop wears Odo's hat now."), Bram komt terug ("Bram the Once-Fled is back.") en wordt alsnog afgerekend, Ties raakt de schat aan ("Ties tried to lift it. Too heavy."). Dit is de film die je aan iemand laat zien.
- **De hoedentoren werkt al met één hoed.** Gloop draagt Odo's helm, en als hij plat gaat ligt de helm naast hem en staat hij er weer mee op. Dat is een klein grapje dat je zelf ontdekt.
- **Meteen beweging** (eerste beeld 0,6 s in plaats van 4 s), het gewei-spinrag boven Gloop is weg, op 160 px staat de ingang nu in beeld. Zuinig blijft het.

**Wat niet goed is (in volgorde van belang):**
1. **"Bram's hat goes on the wall. +9" belooft iets wat er niet is, en bij de verkeerde held.** Bram was één keer gevlucht, geen aartsvijand; de wand is alleen voor afgerekende aartsvijanden (feature 3 en 5) en is nog niet getekend: aan de rode vaandel boven de schat hangt geen hoed. De regel stond in mijn eigen voorraad onder "Wrok afgerekend" voor iedere terugkomer; dat was mijn fout. **Besluit:** de wand-regel alleen voor een aartsvijand, en pas als de wand te zien is (`kroniek-regels.md` aangepast). Voor Olaf (`kern/regels.gd`) en Bram (`kroniek_regels.gd`): regel weg uit "afgerekend". Er zijn nu twee voorraden in de code; liever één (Bram's `kroniek.gd`, zoals Bram 21:20 voorstelt).
2. **De eerste hoed op Gloop leest als een pannendeksel.** Odo's grijze helm is plat en laag; op ware grootte zie je een grijs streepje op Gloop, geen hoed. Juist de eerste hoed is de haak. **Voorstel aan Olaf:** geef held 5 (de opgegeten held in de eerste tien minuten) de **kroon** uit Mila's nieuwe blad van 10 hoeden (index 4; gezien in `ontwerp/steam/mila/hoeden-6x.png`: kroon, koksmuts en hoge hoed lezen het sterkst, de helm het zwakst); tot die in de code zitten de paarse puntmuts.
3. **De terugkomer zegt niet waarom.** "Bram the Once-Fled is back." Zijn wrok is de put; "Bram is back for the Spike Pit." vertelt het verhaal in één regel. Bram heeft dit in `kroniek.gd` al opgelost (terugkomer noemt altijd waarom); het komt pas in de film als strook.gd `kroniek.binnen()` gebruikt.
4. **De Hoard-Toucher komt te laat.** Ties raakt de schat pas rond 50 s aan, en de film eindigt voor hij wegrent en zijn bijnaam krijgt. Liever rond 35 tot 40 s, zodat "Ties the Hoard-Toucher ran." nog in de minuut valt.
5. **Het boze teken leest nog als een rood kruisje** (vergroot: vier rode hoekjes, GEZIEN). Staat bij Mila.
6. **De laatste 15 s gebeurt er weinig** en de regel "Lotte read about you in a tavern." blijft 10 s staan. Niet erg voor het spel, wel voor de film: na de vijf vaste stappen mag de demo nog één keer Gloop laten eten, dan zie je de toren groeien naar twee hoeden.
7. Paneel nog groot en "Hoard: 21 gold" als tekst (Mila 20:55 aan Olaf, staat op zijn lijst). Twee helden aan het eind met dezelfde groene pet (Lotte en Fenna), dus hoedsoorten blijven belangrijk (Mila).

**Oordeel:** voor het eerst laat de film van een minuut zien waarom Het Hol anders is dan een idle-RPG. Na punt 1 tot 4 is dit de film die Thijs kan zien, zodra het uiterlijk van Mila (paneel, teken, hoeden) erin zit. Olaf beslist wanneer.

## Toets 3: pruimkleurig hol, kroniek uit de voorraad, 9 nov 2026 (runs 42695134768 en 42695691333, commits 01bedcb en 09a7ab4, main)
**Bekeken (GEZIEN):** `film.gif` van beide runs op tak `schermen` (`steam-hol/main/`, 1024 x 120, 281 beelden; eerste beeld duurt 4 s, daarna 0,2 s), een blad met een beeld per 5 s, uitsneden drie keer vergroot (Gloop, schat, held met ooglap, opgegeten held), `film/film.log`, `cpu.txt` (0,94 en 1,1 CPU-s per 10 s op 120 px, 114 MB) en `strook-96.png`, `strook-160.png`. Run 42695691333 heeft Mila's pruim, nog niet Gloop met één oog (dat is run 42696163192, liep nog) en nog niet Daans paneel (run 42696475804, liep nog).

**Wat beter is dan toets 2 (punt 1, 2, 3, 4 en 7 van toets 2 zijn opgelost; punt 5 zit in de code maar komt in geen van beide films voor, punt 6 Hoard-Toucher nog niet):**
- **Pruim is een gezicht.** Dit is de eerste film waarbij ik denk: dat is "die paarse strook". Goud, Gloop en de fakkels springen eruit tegen de pruim, het gras boven is een harde rand. Mila heeft gelijk.
- **Goud zie je binnenkomen** en het staat in één regel: "Kees fell to the Spike Pit. +6", "Gloop ate Odo. Burp. +6". Na een minuut 18 en 24 goud.
- **De regels zijn grappig.** "Fenna has a map. It is wrong.", "Odo left gold and one boot. +6", "Rik knocks first. Polite." Dit is de toon. Geen afgekapte tekst.
- **De schat staat tegen het tekstvak** en het hol groeit naar links; op 160 px is de schat nu helemaal te zien.
- **Gloop doet mee.** Hij eet Odo (de held vervaagt als een geestje, mooi), gaat plat, en de kroniek zegt "Gloop is flat. Back soon." en ±8 s later "Gloop is up again. Wobbly."
- **De wrok staat op het poppetje:** in run 42695134768 komt Bram terug met een ooglap en een boos teken boven zijn hoofd. Littekens lezen op ware grootte.
- Elke held heeft een eigen lijfkleur. Zuinig blijft het (rond 1 CPU-s per 10 s).

**Wat niet goed is (in volgorde van belang):**
1. **De film hangt van geluk af, en in de pruim-film zit geen wrok.** Run 42695691333: 8 helden binnen (Pim pas bij ±57 s), 4 vallen (24 goud), 1 vlucht, geen terugkomer, geen Hoard-Toucher. Wie deze film ziet, ziet een mooi hol met vallende poppetjes, maar niet ons eigen stuk. Het plan van Olaf (taken.md 20:45: held 2 vlucht voor Gloop, held 3 komt terug, held 4 wordt Hoard-Toucher) lost dit op. **Eis:** de film van een minuut speelt altijd de eerste tien minuten na (versneld), zodat elke film val, vlucht, terugkomer met ooglap en Hoard-Toucher laat zien. Ook graag de eerste hoed op Gloop (zie de toets van de hoedentoren hieronder).
2. **Het tekstvak is een groot zwart blok** over een derde van de strook. Daans paneel staat net op main (run 42696475804) en Mila wil het kleiner; ik toets het in de volgende film.
3. **Het spinrag boven Gloop leest als een gewei.** Op ware grootte en vergroot lijkt Gloop twee grijze sprieten te hebben. Met de hoedentoren straks op dezelfde plek wordt dat rommelig. Voorstel aan Mila: spinrag een kolom opzij, of weg waar Gloop staat.
4. **Te veel puntmutsen.** In de pruim-film dragen 4 van de 8 helden dezelfde paarse puntmuts (Lotte, Fenna, Mara, Pim). Lijfkleur helpt, maar de hoed is het eerste wat je ziet, en met de hoedentoren wordt hoedsoort nog belangrijker. Er zijn 4 hoeden in het blad; zie de toets hieronder.
5. **Dezelfde grap twee keer in een minuut:** "Rik knocks first. Polite." en ±15 s later "Mara knocks first. Polite." Niet achter elkaar, dus volgens de afspraak, maar het valt op. **Voorstel aan Bram:** per soort de laatste 4 regels onthouden en die overslaan (de voorraad per soort heeft 6 tot 10 regels, dat kan).
6. **De eerste 4 seconden staat het beeld stil** (eerste GIF-beeld duurt 4 s). Voor Thijs is de eerste seconde de belangrijkste. Liever meteen beweging (gras, fakkels, Kees die binnenklimt), of het stille begin eruit knippen.
7. **96 px:** het hol is nog steeds ±40% van de breedte (links ±290 px lege aarde). Met de groei naar links is dat ruimte om te graven, dus niet erg; wel goed om in de film iets meer gegraven te beginnen. **160 px:** het hol loopt links net buiten beeld (ingang half te zien). Olaf beslist.

**Nagekomen, run 42696475804 (commit 552fb65, Gloop met één oog en Daans paneel; GEZIEN: GIF, blad, uitsnede twee keer vergroot, log, 0,99 CPU-s per 10 s):**
- **Het paneel is veel beter** dan het zwarte blok: houten lijst, warme tekst, het hoort bij het hol. Wel nog even groot (±32% van de breedte) en bruin hout op pruim; Mila beslist of het kleiner of in haar kleuren moet.
- **Gloop met één oog leest op ware grootte meteen** en is eigen. Vergroot lijkt het oog bijna een vizier; dat is Mila's oordeel, ik vind het werken. Het gewei-spinrag (punt 3) staat er nog.
- In deze film komen **twee helden terug** ("Odo is back. Still limping.", "Bram the Once-Fled is back."), dus hier zie je de wrok wel. Dat bevestigt punt 1: het hangt van de minuut af.
- **Het boze teken leest nog als een rood kruisje** (vier rode hoekjes): op ware grootte zie ik "X", niet boos. Voorstel aan Mila: een groter en duidelijker teken, bijvoorbeeld een rood wolkje met een bliksem of stoom uit de oren, of de held die met zijn vuist schudt.
- Odo komt terug zonder bijnaam of wrok in de regel ("Still limping."); bij Bram staat er wel "the Once-Fled". Liever altijd de wrok noemen bij terugkomst, anders mis je waarom hij terug is.

**Oordeel:** voor het eerst iets wat ik Thijs zou durven laten zien als je de goede minuut treft. Het ziet er eigen uit, de regels zijn grappig en het goud vliegt. Wat ontbreekt is dat elke film ons eigen stuk laat zien (punt 1, Olaf bouwt het al) en een rustiger tekstvak (punt 2). Daarna klaar voor Thijs, mits Mila's oog en paneel er ook goed uitzien.

## Toets van de hoedentoren (vraag van Mila, 20:45): maakt het de held met een wrok sterker?
**Bekeken:** `ontwerp/steam/mila/gloop-hoedentoren-6x.png`, `stijl.md` deel 2, de films hierboven, en Brams sim (eigen telling, kopie van `sim.py` met een teller per soort, niet in de repo): **Gloop eet 13 tot 28 helden in het eerste uur, 52 tot 78 in 3 uur, 268 tot 309 in 10 uur open tijd** (8 zaden, met de extra slijmen die de sim koopt).

**Oordeel: ja, dit is een haak, en ik zet hem in `features.md` (feature 4).** T1: je ziet in één blik wat Gloop deed, ook na een nacht weg. T2: het is een verhaal ("mijn Gloop draagt er zeven"). T3: groeit vanzelf, zonder straf of plicht. T4: elke hoed-skin komt ook op de toren. Maar drie dingen moeten anders, anders werkt de haak niet:

1. **Een terugkerende held kan zijn eigen hoed niet op Gloop zien.** Alleen een opgegeten held verliest zijn hoed, en een opgegeten held komt nooit terug; wie vlucht houdt zijn hoed (met een hap). Dus het boze teken bij de eigen hoed gebeurt nooit. **Oplossing die de wrok echt sterker maakt: via de familie.** Komt er een naamgenoot van een held die Gloop at ("Kees II", staat al in de code), dan heeft hij **meteen een wrok tegen Gloop** en loopt hij eerst naar Gloop met het boze teken ("Kees II wants dad's helmet back."). Zo krijgt Kees II, die nu zonder wrok komt, een reden, en de grap uit "De kinderen van je aartsvijand" (versie 1) zit dan al klein in het prototype. Wint Kees II (Gloop plat, toren valt om), dan zoekt hij in de hoeden en vindt hem niet ("Kees II can't find it. Too many hats."). **De toren verliest nooit een hoed** (T3: niets van jou raakt kwijt).
2. **De toren is meestal binnen 20 minuten vol.** Bij 13 tot 28 opgegeten helden per uur zitten de 4 plekken op zijn hoofd na 2 tot 18 minuten vol (8 zaden), en daarna verandert er op zijn hoofd niets meer. De groei over dagen moet dus in de **hoedenberg naast hem** zitten, net als de schatberg: **vijf maten, bij 5, 25, 100, 300 en 1000 hoeden** (1000 haal je na ±35 uur open tijd). Zo zie je ook na een week nog groei. Op zijn hoofd: de laatste 4 die hij at. Bij hover: "Gloop wears 4 hats. 212 more in the pile." En bijnamen voor Gloop bij 25 en 100 ("Gloop the Hatted", "Gloop the Milliner").
3. **Meer hoedsoorten, anders is de toren eentonig.** Met 4 hoeden in `held_hoeden.png` staan er vaak twee dezelfde op elkaar. Voor de eerste speelbare versie **minstens 8** (bijvoorbeeld koksmuts, kroontje, piratensteek, emmer, kaasschaaf-helm: grappig mag), voor versie 1 zo'n 16, die ook in het heldenboek gaan. Dat is Mila's keuze.

Ook nog: **(a)** Gloop staat in de film in de gewone gang (16 spelpixels hoog), niet in de schatkamer van twee rijen. Een toren van 4 hoeden steekt dan ±10 spelpixels de aarde in. Olaf en Mila: of Gloop krijgt een eigen plek van twee rijen hoog (een open kamer boven hem), of in een lage gang hooguit 1 hoed op zijn hoofd en de rest op de berg. **(b)** Een tweede slijm (meer van dezelfde, feature 4) bouwt zijn eigen toren; zo is een tweede slijm ook leuk om te kopen. **(c)** De put geeft geen hoed (houd het bij Gloop, dan is het zijn ding). **(d)** In de eerste tien minuten (features.md) wordt held 5 door Gloop opgegeten, zodat je de eerste hoed binnen ±5 minuten ziet: "Gloop wears Odo's hat now." (niet Kees: die valt altijd als eerste in de put).

**Controleur (agent, 21:00):** akkoord na verbeteren. Verwerkt: aantallen pruim-film (8 helden, 4 vallen), lijst opgeloste punten, "meestal binnen 20 minuten", rij ±5 min (Gloop moet op zijn, andere naam, volgorde met Olaf), `{bewoner}` blijft altijd "Gloop", aartsvijand-hoed naar de wand, notatie naamgenoot, onthouden waardoor iemand viel.

## Toets 2: hol met Daans kunst, 9 nov 2026 (run 42685438422, commit ce73494, main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/main/`, 1024 x 120, 281 beelden), tien beelden op ware grootte onder elkaar, de val bij beeld 40 tot 56 en het einde (270 tot 280) twee keer vergroot, `film.log` en `cpu.txt` (1,03 CPU-s per 10 s op 120 px, 113 MB). Daans karakter-laag (kleuren per naam, littekens, tekens, paneel) zit er nog niet in; dat staat op Olafs lijst, dus daar oordeel ik nog niet over.

**Wat beter is dan toets 1 (punt 1, 4 en 6 van toets 1 zijn opgelost):**
- **Er komt goud binnen.** Na 10 s valt Kees in de stekelput, na een minuut staat er 12 goud. Vier van de zes helden vallen, twee vluchten. Dat is precies de eerste minuut die we wilden (T1).
- **De val leest goed.** De held loopt op de put, de pinnen schieten omhoog en hij is weg in twee beelden. Kort, duidelijk, een beetje gemeen. Goed.
- **Het ziet er voor het eerst uit als een spel:** gras met plantjes, fakkels, vaandel, de schatberg die glinstert, gangen in twee rijen. Het hol groeit tijdens de film (kolom 4, 13, 5, 6 gegraven).
- Geen afgekapte tekst meer. De wrok staat in de log (twee regels): "Ties the Once-Fled is back!" en "Grudge: the Spike Pit."

**Wat niet goed is (in volgorde van belang):**
1. **Gloop ligt de halve film plat** (vanaf ±28 s tot het einde; de GIF heeft eerst één beeld van 4 s, daarna beelden van 0,2 s). In de film komt er elke 6 tot 9 s een held (`strook.gd` regel 194, demo), maar Gloop blijft 60 s plat (`slijm.gd` PLAT_S). In het echte spel is 60 s plat ongeveer één held overslaan; in de film zijn het er vier tot vijf. Ook komt de regel "Gloop is flat. Back in a minute." nooit in de kroniek (`regel_plat()` wordt niet aangeroepen), dus je snapt niet waarom hij plat ligt. Daardoor doet de stekelput al het werk en is de film eentonig: vier keer dezelfde dood op dezelfde plek. **Eis:** in de demo alles even snel versnellen, ook plat zijn (60 s x 7,5/50 = ±9 s). Dat verandert niets aan de balans van Bram's sim, alleen aan wat de film laat zien.
2. **Je ziet het goud niet binnenkomen.** "+3 gold for your hoard" staat als losse regel en vervangt de regel van de val, dus je leest of de dood of het goud. Het fijnste moment van een idle-spel (iets binnen zien komen) zit nu alleen in een getal. **Eis:** drie muntjes springen van de put naar de schatberg (een halve seconde, alleen als er toch getekend wordt) en de regel wordt één regel: "Kees fell to the Spike Pit. +3" (zie `kroniek-regels.md`).
3. **De wrok is nog niet te zien op het poppetje.** Ties komt terug met een litteken van 1 bij 2 rode pixels (`held.gd` r.217), maar dat valt weg tegen zijn rode hemd. Er zweeft wel een klein rood kruisje, maar dat staat 3 spelpixels boven de hoed in de aarde en leest als "dicht" of "dood", niet als boos. Daan heeft `tekens.png` en `held_littekens.png` klaar; dat is Olafs volgende stap. **Eis:** teken direct boven het hoofd (1 of 2 spelpixels), en een litteken dat je bij terugkomst meteen ziet.
4. **Alle helden lijken op elkaar.** Vijf van de zes dragen dezelfde rode band en hetzelfde rode hemd; alleen de tovenaarshoed en één helm wijken af. Op 120 px is kleur het enige wat je in één blik ziet. Daans `held_lijf_kleuren.png` (vaste kleur per naam) lost dit op; graag tegelijk met punt 3.
5. **Een dode held komt terug met dezelfde naam.** Kees valt na 10 s, en na 40 s staat er "Kees the hero climbs in." Je denkt dat hij terug is, maar het is een nieuwe Kees zonder wrok. Dat is verwarrend, want terugkomen is juist ons eigen stuk. **Eis:** een naam van een gevallen held niet opnieuw gebruiken. Is een naam toch weer aan de beurt, dan als "Kees II" (geen wrok, wel een regel "Kees II climbs in. Kees fell here once."). Zo komt de grap uit "De kinderen van je aartsvijand" (`features.md`, versie 1) al klein in het prototype, zonder extra systeem.
6. **Niemand komt bij de schat.** De Hoard-Toucher van Bram is nog niet aangesloten (staat op Olafs lijst). In de film staan twee helden even naast de stapel en lopen weer weg. Dat blijft een gemiste grap tot hij erin zit.
7. **Het rechterderde deel van de strook is lege aarde.** Het hol stopt bij de schat op ±2/3 van de breedte, daarna steentjes tot het tekstvak. Wanneer je graaft, schuift de schat mee, maar in de film blijft het rechterstuk leeg. Kan de schat tegen het tekstvak aan staan, met het hol ervoor, zodat graven het hol naar links laat groeien? Dan is de strook altijd vol. Olaf beslist.

**Op de andere hoogtes (GEZIEN, `strook-96.png` en `strook-160.png` van dezelfde run):**
- **160 px (schaal 4): het tekstvak ligt over de schat.** Het hol is 256 spelpixels breed, dus de schatkamer komt precies onder het tekstvak; je ziet alleen het vaandel en de bovenkant van de stapel. Dit is het belangrijkste punt van deze toets: wie de strook groter zet om meer te zien, ziet zijn eigen schat niet meer. **Eis:** het hol eindigt altijd links van het tekstvak (of het tekstvak schuift weg tot hover).
- **96 px (schaal 2):** het hol neemt maar ±45% van de breedte, de rest is lege aarde tot het tekstvak. Hier geldt punt 7 nog sterker.

**Controleur (agent, 19:58):** feiten nagelopen tegen film, log en code; vier kleine onjuistheden verbeterd (halve film plat in plaats van twee derde, litteken is er wel maar valt weg, plat-regel ontbreekt, wrok in twee regels).

**Oordeel:** een grote stap. Het ziet eruit als een spel, er komt goud en de val is lekker kort. Wat nog mist om het aan Thijs te laten zien: de schat mag nooit onder het tekstvak liggen (160 px), Gloop moet meedoen (punt 1), het goud moet je zien vliegen (punt 2) en de wrok moet op het poppetje staan (punt 3 en 4). Punt 1 is één regel, punt 2 is klein, punt 3 en 4 zijn Daans kunst aansluiten. Doorgegeven aan Olaf en Bram.

## Toets 1: eerste kern, 9 nov 2026 (run 42676196548, commit dfd139e, tak `claude/steam-hol-kern`)
**Bekeken (GEZIEN):** `film.gif` (1024 x 120, 281 beelden, een minuut), zes beelden naast elkaar op ware grootte, `film.log`, `cpu.txt` op tak `schermen` (`steam-hol/claude-steam-hol-kern/`). Kunst is nog tijdelijk (Daans bladen zitten er nog niet in), dus over het uiterlijk oordeel ik niet; dat is Daan.

**Wat goed is:**
- Het draait, zuinig (1 CPU-seconde per 10 s op 120 px, GEZIEN in cpu.txt) en de strook is echt klein.
- De kern van ons eigen stuk werkt al in de log: "Kees escaped and is now Kees the Once-Fled. Grudge: Gloop the Slime." en "Kees the Once-Fled is back." Dat is de zin waar het spel om draait.
- Helden met namen die binnen druppelen, elk in een andere kleur: je ziet in één blik dat er iets gebeurt.

**Wat niet goed is (in volgorde van belang):**
1. **Na een minuut nog steeds "Hoard: 0 gold".** In de hele film valt niemand: alle helden vluchten (log: Kees, Mara, Odo allemaal "escaped"). Er komt dus geen goud binnen en er is niets te doen. Voor "tussendoor" (T1) moet er in de eerste minuut iets binnenkomen. Eis: in de eerste minuut valt minstens één held en zie je het goud stijgen (balansdoel in `features.md`). Nu vlucht 3 van de 3; doel is ongeveer 1 op 3.
2. **De wrok zie je niet op het scherm, alleen in de tekst.** Kees komt terug en ziet er precies hetzelfde uit. Het beste stuk van het spel moet je zien zonder te lezen: een litteken op het poppetje (pleister, ooglap) en een klein boos teken boven zijn hoofd als hij zijn vijand ziet. (Daan: littekens als losse laag, zoals de hoeden.)
3. **De slijm doet niets zichtbaars.** Gloop staat de hele minuut op dezelfde plek, terwijl helden langs en door hem lopen en toch "Grudge: Gloop" krijgen. Er moet te zien zijn dat Gloop iemand raakt (een hap, de held die terugstuitert), anders snap je de wrok niet.
4. **Tekst wordt afgekapt:** "Grudge: Gloop the Sli". De regel moet passen of korter ("Kees is back. Grudge: Gloop"). Het tekstvak neemt ±30% van de breedte; dat mag kleiner als de regels korter zijn, dan is er meer hol.
5. **Er gebeurt niets bij de schat.** Een held staat bij de stapel en loopt weer weg. Hier zit de grap uit `features.md` (hij probeert de stapel op te tillen, te zwaar, rent weg als Hoard-Toucher). Nu is het een gemiste kans.
6. **Te weinig te zien van het spelen zelf.** Er wordt één keer gegraven (log "gegraven kolom 13"), maar in de GIF zie je geen klik of nieuw stuk gang ontstaan. Laat in de film van een minuut zien: graven, een put zetten, een held die erin valt, goud dat binnenkomt. Dat is ook wat Thijs moet zien.
7. **Het hol vult de breedte niet:** gang tot ±2/3, daarna egale aarde en het tekstvak. Met graven groeit het; voor de film beter een hol dat al wat gegroeid is.

**Oordeel:** goede technische basis, de wrok staat in de log, maar het is nog niet leuk om naar te kijken: er valt niemand, er komt geen goud, en de wrok zie je niet. Punten 1 tot 3 zijn het belangrijkst; zonder die drie kan Thijs het niet zien. Doorgegeven aan Olaf en Bram in hun berichtenbestand.
