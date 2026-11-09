# Het Hol: features (Sanne, game-ontwerper)

Stand 9 nov 2026, ±19:00 UTC. Richting Het Hol (besluit Thijs 9 nov 19:20). Dit bestand zegt **wat** er in het spel zit en **waarom het leuk is**. Olaf beslist over de bouw en de volgorde, Daan over het uiterlijk.

## De toets (opdracht van Thijs, 18:50): elke feature moet hier langs
| | Eis | Wat het voor ons betekent |
|---|---|---|
| T1 | **Tussendoor** | een blik van 30 seconden levert al iets op: een nieuwe regel in de kroniek, een held die je herkent, iets om goud aan uit te geven. Het spel loopt door als je niet kijkt. |
| T2 | **Grappig om te onderhouden** | humor en karakter: helden met een naam en een wrok, bewoners met een eigen leven. Je wilt het verzorgen en uitbreiden. |
| T3 | **Niet tijdrovend, nooit straffen** | geen dagelijkse plicht, geen grindmuur, niets gaat kapot of dood als je weg bent, elke keuze is terug te draaien. |
| T4 | **Later skins en DLC, eerlijk** | het basisspel is af voor één prijs. Extra's zijn alleen uiterlijk en nieuwe inhoud, nooit sneller of sterker. |

## Wat de toppers ons leren (reviews geteld, 9 nov 2026)
**Bron (GEZIEN):** de meest nuttige Engelse reviews van de openbare communitypagina's van Steam, per spel ±80 negatieve en ±80 positieve, samen 316 negatieve en 305 positieve: Rusty's Retirement (2666510, 97% van 6.625 Engelse reviews positief), Ropuka's Idle Island (3416070, 95% van 2.405), Tiny Pasture (3167550, 93% van 1.209), Deskrawl (4623570, 69% van 472, laatste 30 dagen maar 36% van 1.256). Script en ruwe data: `platformen/steam/data/reviews-haal.py`, `reviews-tel.py`, `data/reviews-2026-11-09/` (telling.txt). Tellen gaat op trefwoorden met woordgrenzen (na de controleur aangescherpt), dus het zijn grove aantallen: een review telt mee als het woord erin staat, ook als het geen klacht is; de voorbeelden heb ik zelf gelezen. De API `appreviews` stuurt vanuit onze omgeving door naar de voorpagina (GEZIEN, 302), daarom de communitypagina's.

**Waarom ze stoppen** (316 negatieve reviews):
- **Op na een paar dagen, niets meer te doen**: 82 noemen weinig inhoud, kort of saai; 41 noemen dat het op of klaar is (trefwoorden als end game, nothing to do, ran out, ook in `reviews-tel.py`; "pretty much completely done after 3 days", "nothing to do with all your money", Rusty's Retirement). Belangrijk: negatieve schrijvers speelden toch lang (mediaan 26 uur bij Rusty's, 50 bij Ropuka's, 179 bij Deskrawl). Waarschijnlijk vonden ze het leuk tot het opraakte (uitleg, geen telling; het kan ook gewoonte of grind zijn).
- **Grind en muur**: 52 (Deskrawl: zeldzame buit "is 0, just 0" na 230 uur; Ropuka's: "upgrade 1 thing every 6 minutes").
- **Geld en markt**: 38 over DLC, betalen of markt; bij Deskrawl noemen 26 van de 78 de ruilmarkt, ruilen of betalen om te winnen ("It takes hundreds of hours to get a single drop. That you can buy for a buck on the marketplace.").
- **Zwaar of in de weg**: 22 over prestaties, geheugen of schermruimte; 2 noemen fps letterlijk ("No performance options to limit FPS", Tiny Pasture); 7 zeggen dat je twee schermen nodig hebt ("it gets in the way unless you have 2 screens", Tiny Pasture).
- **Bugs en save kwijt**: 39 (Tiny Pasture 20: "wipes my save"; Ropuka's: een logbestand van 46 GB).
- **Te veel aandacht nodig, niet echt idle**: 26 ("ended up being a full distraction from my work", Tiny Pasture).
- **Straf als je weg bent**: ongeveer 9 (hangt sterk af van de trefwoorden), maar fel ("punishing you for being idle is a very strange choice. If you leave for too long, everyone gets sick", Tiny Pasture).
- **Onomkeerbare keuzes**: 2 tot 4 (afhankelijk van de trefwoorden), bij Rusty's ("once you place animals, you can't remove them").
- **Te weinig leven**: "I was hoping for the little frog to do more stuff... Instead he just cut grass and sleeps" (Ropuka's).

**Wat ze prijzen** (305 positieve reviews): mooi en pixel art 91, naast werk of studie 80, voortgang en ontgrendelen 73, rustig 54, prijs 34, klein en licht 34, muziek 27. **Humor: 12 van de 305.** Niemand in de top zet op humor. Of kopers het willen, is een GOK die het prototype moet laten zien; het past wel bij de opdracht van Thijs ("grappig om te onderhouden").

**Wat dat voor Het Hol betekent:** (1) de inhoud mag niet na 3 dagen op zijn: verhalen die zichzelf maken (helden met wrok, hun kinderen) en een verzamelboek dat lang meegaat; (2) geen ruilmarkt, geen zeldzame buit met kleine kans, geen betaalde kracht; (3) klein, zuinig en een fps-instelling; (4) een save die niet kwijt kan; (5) alles terug te draaien; (6) nooit straf; (7) humor als kern: de opdracht van Thijs vraagt erom en de toppers doen het niet.

## Het ritme
- **Elke minuut of zo:** een held klimt je hol in (de bouw rekent nu met 25 tot 70 s in `strook.gd` en gemiddeld 47,5 s in `voortgang.gd`; Bram en Olaf kiezen samen één getal na de simulatie). Hij loopt naar je schat, loopt in vallen en bewoners, en valt of vlucht. Eén korte regel in de strook.
- **Elk bezoek (30 seconden tot een paar minuten):** je ziet wie er was ("Kees the Twice-Fled is back. Grudge: Gloop"), je geeft je goud uit aan een gang, een val of een bewoner, en soms hangt er een nieuwe aartsvijand aan de wand. Klaar. (T1)
- **Elke dag:** een of twee aartsvijanden die steeds terugkomen; de dag dat je hem eindelijk krijgt is een feestje. Geen dagelijkse beloning, geen plicht. (T3)
- **Elke week:** je hol is groter en voller, je heldenboek dikker, en de kinderen van je oude vijanden komen wraak nemen. (T2)
- **Weg geweest:** bij openen één regel met aantallen en goud ("While you were away: 612 heroes came in, 410 stayed, 202 fled. Gloop is very full."), plus **drie regels met namen** (wie er terug was, welke wrok er speelde, of een aartsvijand kwam). Nu geeft `voortgang.gd` alleen aantallen en goud; de regels met namen vraag ik aan Bram, anders is terugkomen alleen "+X gold". Alleen winst, plafond 12 uur (Bram, `voortgang.gd`), dus een nacht weg levert hetzelfde als een week; niemand hoeft elke dag. (T3)

## De eerste tien minuten van een nieuw spel (wat Thijs als eerste ziet)
Thijs keurt het prototype op wat hij in de eerste minuten ziet, en een koper schrijft zijn review op hetzelfde moment. Daarom sturen we de eerste tien minuten van een **nieuw** spel een beetje (zoals `moet_vallen` al doet), daarna is alles gewoon kans. Elk stuk gebruikt een systeem dat er al is of op de lijst staat; nieuw is alleen dat een paar uitkomsten eenmalig vastliggen (kolom rechts, met **vast** gemarkeerd), net als `moet_vallen` nu. Tijden in echte seconden, held elke 40 tot 60 s.

| Wanneer | Wat er gebeurt | Waarom | Wat het al gebruikt |
|---|---|---|---|
| 0 s | Strook verschijnt, Gloop slaapt, schat glinstert. Regel: "Your hole is open. Heroes will come." | rust, je ziet meteen wat van jou is | staat al |
| ±5 s | Eerste held, schijterig, struikelt in de put. Muntjes vliegen naar de schat. "+6" | binnen 10 s iets binnen (T1) | **vast:** `moet_vallen` (staat al); muntjes (feature 5) |
| ±1 min | Tweede held loopt tegen Gloop: hap, held stuitert terug en **vlucht**. Hij krijgt een pleister. | de wrok begint, je ziet het op het poppetje | **vast:** slaat de put over en vlucht na de hap van Gloop; held.gd, littekens (Daan) |
| ±2 min | Derde held valt (+6), nu 12 goud (alleen met 6 goud per val, voorstel in `balans.md`; met de huidige 3 is het 6 en wordt dit ±4 min): precies genoeg voor de eerste cel graven (12 in `balans.md`); de prijs staat bij hover. | je eerste keuze binnen 2 minuten (T1) | **vast:** derde held valt; graven, kosten uit `balans.md`; prijs bij hover is nieuw (Olaf) |
| ±3 min | **Die gevluchte held komt terug**: pleister, boos teken, bijnaam "the Once-Fled", loopt recht op Gloop af. | ons eigen stuk, in de eerste 5 minuten | **vast:** de volgende held is die terugkomer |
| ±4 min | Gloop wint of verliest; verliest hij, dan is hij plat met "Back in a minute." en staat op. | bewoner met karakter, nooit dood | slijm.gd |
| ±5 min | Gloop eet een held: zijn hoed komt op Gloops hoofd. "Gloop wears Odo's hat now." | de haak (hoedentoren) in de eerste 5 minuten | **vast:** de eerste held na de Hoard-Toucher (volgorde van Olaf: 1 valt, 2 vlucht, 3 terugkomer, 4 Hoard-Toucher, 5 opgegeten) haalt Gloop niet; ligt Gloop nog plat, dan de eerste held nadat hij op is; at Gloop de terugkomer al, dan vervalt deze rij. Hoedentoren (Bram) |
| ±6 min | Een hebzuchtige held haalt de schat, probeert de berg op te tillen, te zwaar, rent weg als **Hoard-Toucher**. | de grap die je aan iemand vertelt | **vast:** komt langs alles en haalt de schat; Hoard-Toucher (Bram) |
| 10 min | Daarna gewoon kans (Bram's sim). **Regel: geen aartsvijand in het eerste uur van een nieuw spel**, zodat het bijzonder blijft (daarna ongeveer één per dag, Bram's sim). | geen script dat je doorziet | sim |

**Regels:** alleen bij een vers spel (in de save onthouden, net als `moet_vallen`), nooit opnieuw na een herstart; de film van een minuut op Actions mag dit in een minuut proppen, maar het echte spel volgt de tabel. Olaf en Bram kiezen hoe; dit is wat er te zien moet zijn.

## Eerste speelbare versie: vijf features, echt goed
Volgorde = belangrijkheid. Grootte bouw is GOK.

### 1. Het hol in de strook, graven met één klik
**Wat:** een doorsnede onder het maaiveld in de breedte, 120 px hoog (96 tot 160 instelbaar). Klik op aarde naast een gang: daar wordt een gang. Het hol groeit in de breedte, niet dieper (120 px heeft daar geen ruimte voor, Olaf 18:40); dieper zien kan later bij hover. In de eerste versie is er één rij gangen plus **één schatkamer van twee rijen hoog** achteraan (dus rij 1 in `hol.gd` is nodig, maar alleen voor die kamer). Graven kost een beetje goud, dus elke val van een held geeft je iets te doen.
**Waarom leuk:** het is jouw hol; je ziet het groeien in één blik (T1). Langer maken = langer pad = meer vallen = meer verhalen.
**Eerlijk:** dichtgooien kan altijd en geeft het goud terug (T3, geen onomkeerbare keuzes zoals bij Rusty's).
**Bouw:** staat al grotendeels (Olaf, `hol.gd`); nog: kosten en terugbetalen.
**Toets:** T1 ja, T2 middel, T3 ja, T4 ja (holthema's zijn later de grootste skin).

### 2. Helden met een naam, een hoed en een karakter
**Wat:** elke held heeft een naam, een hoed (lijf + hoed + wapen uit Daans bladen) en één karaktertrek die je ziet aan hoe hij loopt: **hebzuchtig** (rent recht op de schat af, ook door vallen), **schijterig** (keert om bij een val die hij gezien heeft), en voor versie 1 meer. Bij binnenkomst één regel: "Mara the Greedy climbs into your hole."
**Wat er gebeurt als hij de schat haalt:** hij probeert de stapel op te tillen, die is te zwaar, hij pakt niets en rent weg met een opschepperige bijnaam ("Odo the Hoard-Toucher"). Je verliest niets (T3), maar hij komt brutaler terug. Brutaler betekent: hij loopt sneller of slimmer en vlucht vaker, zodat zijn verhaal langer duurt. Nooit dat je iets kwijtraakt of goud moet sparen om bij te blijven. Dat is de spanning, zonder straf.
**Waarom leuk:** helden zijn geen golven poppetjes maar figuren die je herkent. Je praat erover (T2).
**Bouw:** Bram (`held.gd`), staat in taken.
**Toets:** T1 ja, T2 sterk, T3 ja, T4 ja (hoeden en gilden zijn later DLC).

### 3. De wrok: helden die terugkomen (ons eigen stuk)
**Wat:** wie vlucht, komt terug met (a) een **litteken dat je op het poppetje ziet** (pleister, ooglap, verband, een hap uit de hoed), (b) een **wrok** tegen wat hem raakte, bij naam ("Grudge: Gloop the Slime"), en (c) een **bijnaam** zoals `kroniek.gd` ze al geeft (eerst Spooked of Lucky, dan Twice-Fled, Thrice-Fled). Een held met een wrok loopt eerst naar zijn vijand, niet naar de schat. Na de derde vlucht wordt hij je **aartsvijand**: gouden naamkaartje, en als hij binnenkomt zie je dat even (klein, binnen de strook; geluid staat standaard uit, want een geluidje naast je werk is precies de klacht "full distraction from my work"). Krijg je hem eindelijk, dan zegt de kroniek "Grudge settled" (tekst zoals in `kroniek.gd`) en gaat hij met naam en hoed op de **wand van aartsvijanden** (feature 5).
**Waarom leuk:** dit maakt de verhalen die mensen in reviews en op Reddit vertellen. Het is wat geen ander taakbalkspel heeft (zie `idee.md`). Spanning zonder straf: hij neemt alleen zijn wrok mee, niets van jou.
**Bouw:** `kroniek.gd` (Bram) heeft bijnaam, wrok en "Grudge settled" al; nog: litteken op het poppetje (Daan tekent 3 tot 4 littekens als losse laag, zoals de hoeden), aartsvijand-kaartje, wrok bepaalt het doel van het lopen.
**Toets:** T1 sterk (je ziet bij elk bezoek wie er terug is), T2 sterkst, T3 ja, T4 ja.

### 4. Bewoners met een eigen leven
**Wat:** om te beginnen één slijm (Gloop) en één val (stekelput). Bewoners hebben een naam, een teller ("Gloop has eaten 12 heroes") en verdienen zelf een bijnaam ("Gloop the Unbudged"). Als er niemand is doen ze iets kleins en grappigs, spaarzaam, want stilstand is zuinig (Olaf, logboek 17:31): slijm slaapt, spuugt na een held een laars uit, kruipt naar een gevallen munt. Een bewoner die verliest gaat **niet dood**: hij is even plat ("Gloop is flat. Back in a minute.") en staat daarna weer op (T3). Je kunt **meer van dezelfde** neerzetten (tweede slijm, tweede put, elke volgende iets duurder) en elke bewoner of val verplaatsen of weghalen voor het volle goud terug.
**Waarom leuk:** dit is wat je wilt verzorgen (T2) en waar Ropuka's mist dat de kikker "just cut grass and sleeps". Een bewoner die je kent en die een held met een wrok heeft, is een duel waar je naar uitkijkt.
**Bouw:** Bram (systemen) en Daan (3 kleine leven-animaties per bewoner, meer niet).
**Toets:** T1 ja, T2 sterk, T3 ja, T4 ja (nieuwe bewoners zijn later DLC, hoedjes voor bewoners skins).
**De hoedentoren (haak van Mila, getoetst 9 nov 21:00 UTC in `spelgevoel.md`):** Gloop draagt de hoeden van de helden die hij opat. Op zijn hoofd de laatste 4 (wiebelend), de rest op een **hoedenberg** naast hem die in zes maten groeit (5, 25, 100, 300, 1000, 3000 hoeden), zodat je ook na twee weken nog groei ziet (Brams sim, GEZIEN: ±27 hoeden per uur open tijd per slijm, 1000 na ±37 u, 3000 na ±110 u, dus met de strook een werkdag open rond dag 5 en dag 14); daarna telt de hover gewoon door en krijgt de berg in versie 1 een bladzijde in het heldenboek met stempels bij 1000, 3000 en 10.000; Gloop eet 13 tot 28 helden per uur (Brams sim), dus zijn hoofd is na een kwartier vol. Bij hover: "Gloop wears 4 hats. 212 more in the pile." Bijnaam bij 25 en 100. **Een hoed gaat er nooit meer af** (T3). Uitzondering: een afgerekende aartsvijand gaat met zijn hoed naar de **wand van aartsvijanden** (feature 5), ook als Gloop hem at; de wand gaat voor. Een naamgenoot van een held die **Gloop** at (niet de put; daarvoor moet strook.gd onthouden waardoor iemand viel) komt met een wrok tegen Gloop en wil de hoed van zijn vader terug; hij vindt hem nooit. Elke slijm heeft zijn eigen toren. De put geeft geen hoeden. Minstens 8 hoedsoorten in de eerste versie (Mila). **Toets:** T1 sterk, T2 sterk, T3 ja, T4 sterk (elke hoed-skin staat ook op de toren).

### 5. Buit, goud uitgeven, de wand van aartsvijanden en de kroniek
**Wat:** een gevallen held laat goud achter, en dat **zie je vliegen**: een paar muntjes springen van de val of bewoner naar de schatberg en de berg groeit zichtbaar mee (toets 2 in `spelgevoel.md`: nu staat het alleen als getal in de tekst). Het goud geef je uit: graven, een extra slijm of put, en per bewoner of val **drie upgrades** die je ziet (Gloop wordt groter, de put krijgt roestige stekels). Zo is er in de eerste uren bij elk bezoek iets te kopen. Een afgerekende aartsvijand hangt met naam en hoed aan de **wand van aartsvijanden** in de schatkamer (niet elke hoedsoort, want Daans blad heeft er 4 en dan is de wand in tien minuten vol). Bij hover in de strook (niet erbuiten) zie je de laatste 5 regels van de kroniek, scrollen kan binnen de strook, en bij een terugkerende held zijn kaartje (bezoeken, littekens, wrok).
**Waarom leuk:** je ziet je verhaal letterlijk aan de muur hangen, en elke naam aan de wand heeft een geschiedenis. Niets draait op geluk (geen kansen van 0,1% zoals bij Deskrawl).
**Bouw:** klein tot middel (Olaf hol, Bram kroniek, Daan de wand).
**Toets:** T1 ja, T2 ja, T3 ja, T4 ja.

**Altijd, in alle vijf (geen feature maar een eis):** strook klein en instelbaar, 15 fps en niet tekenen als er niets beweegt (staat al), een fps-instelling in het menu, geluid standaard uit en "stil uur", save die niet kwijt kan (schrijven naar een tijdelijk bestand, dan hernoemen, plus één reserve), logbestand met een maximum. Dit komt uit de klachten over zwaar, in de weg, afleiding en bugs.

## Waarom niet de andere twee (kort)
Kerkertocht (richting 1) is wat tientallen idle-RPG's al doen: helden lopen naar rechts en slaan, en in die soort klagen kopers juist over grind en eentonigheid; er is weinig om grappig te onderhouden. De Karavaan (richting 3) is mooi en klein om te bouwen, maar de humor moet uit geschreven briefkaarten komen, de vraag naar reizen is dunner bewezen en Silk Road Caravan (5495690) komt in Q1 2027 met bijna hetzelfde. Het Hol maakt zijn eigen verhalen (helden met een wrok), en dat is precies "grappig om te onderhouden". Zie `idee.md` voor het volledige bewijs.

## Bewust niet (ook niet later)
- **Geen ruilmarkt, geen Steam-ruilitems** (Deskrawl: 26 van 78 negatieve reviews). Hoeden en trofeeën zijn van jou, niet te koop.
- **Geen buit met kleine kans en geen eindgrind.** Alles is te halen; het verschil zit in het verhaal, niet in geluk.
- **Geen straf als je weg bent.** Niemand wordt ziek, niets gaat dood, niets raakt gestolen.
- **Geen dagelijkse beloning, geen energie, geen timers die je terugroepen.**
- **Geen onomkeerbare keuzes.** Alles verplaatsen of weghalen geeft het volle bedrag terug.
- **Geen betalen om sneller te gaan, nooit.**
- **Geen grote vensters of kaartjes buiten de strook.**

## Versie 1 (na het prototype, vóór de winkel)
Doel: genoeg inhoud dat het **niet na 3 dagen op is** (Rusty's-klacht). GOK: ±40 uur open tijd voor je alles een keer hebt gezien, en daarna blijven de verhalen komen.
- **4 heldensoorten:** ridder (sterk, traag), dief (ontwijkt vallen, pakt een munt van de grond, geen schat), magiër (ziet vallen), **bard** (zingt na zijn vlucht een lied over je hol, en dan komen er meer helden: het lied staat als regel in de kroniek).
- **6 karaktertrekken** in totaal: hebzuchtig, schijterig, wraakzuchtig, verdwaald (loopt de verkeerde gang in), opschepper, slaapkop (doet een dutje in je hol).
- **5 vallen** (stekelput, rolsteen, valluik naar de kelder, lijmplaat, nep-schat) en **4 bewoners** (slijm, skelet, mimic die een schatkist speelt, een chagrijnige trol die alleen wakker wordt voor aartsvijanden).
- **Kamers met een functie:** schatkamer, slaapkamer (bewoners staan sneller op), trofeeënzaal, keuken (slijm wordt groter van laarzen).
- **Heldenboek:** elke soort held, trek en hoed één bladzijde; **vol te krijgen met alleen het basisspel**, DLC krijgt eigen bladzijden; een verzamelboek dat lang meegaat (Birdwatching Notebook, de best verkopende betaalde app van 2026, leunt hier ook op; `idee.md`).
- **De kinderen van je aartsvijand:** een afgerekende aartsvijand heeft soms een kind dat later komt ("Kees II, son of Kees the Thrice-Fled, wants his father's hat back"). Dit is de verhaalmotor die nooit opraakt, zonder grind.
- **Faam:** hoe meer helden je hol overleefden of niet, hoe beroemder je hol en hoe gekkere helden er komen. Faam gaat nooit omlaag.
- **Instellingen:** links of rechts, kleurenblind, sneltoets om te verbergen (hoogte, fps, geluid en stil uur zitten al in de eerste versie).

## Later: skins en DLC (alleen uiterlijk en inhoud, T4)
- **Holthema's** (de grootste skin): ijsgrot, vulkaan, spookslot, snoepgrot. Zelfde spel, ander hol. Tiny Pasture verkoopt al een thema-DLC voor $2,39 (Olaf, `idee.md`, GEZIEN).
- **Heldengilden** als inhoud-DLC: piraten, ridders van de ronde tafel, toeristen met camera's. Nieuwe trekken en hoeden, niet sterker.
- **Seizoenshelden:** kerstman die je hol in klimt, Halloween-helden. Gratis updates of klein pakket. Ze komen vaker in hun seizoen, maar **zijn het hele jaar te halen**: geen tijdelijke hoed die nooit terugkomt, want dat is een verkapte plicht.
- **Hoedjes en kleuren voor bewoners.** Supporter Pack zoals alle toppers.
- Regel voor alles hierboven: wie het niet koopt mist geen kracht en geen voortgang; boek en wand zijn 100% vol te krijgen zonder DLC.

## Balansdoelen voor Bram (`sim/`)
Alle getallen GOK tot de simulatie ze toetst:
- In de **eerste minuut** valt er minstens één held en zie je goud binnenkomen (de eerste GIF heeft 0 goud na een minuut; zie `spelgevoel.md`).
- In de eerste **10 uur open tijd** is er bij elk bezoek iets om goud aan uit te geven.
- Tijd tot het volgende nieuwe ding groeit langzaam en heeft een plafond (GOK: nooit meer dan 2 uur open tijd), dus geen muur.
- Ongeveer **1 op de 3 helden vlucht** (anders geen wrok en geen verhalen), en een aartsvijand komt gemiddeld één keer per dag langs bij een paar uur open per dag.
- Na 40 uur is het heldenboek ±80% vol (GOK), daarna blijven aartsvijanden en hun kinderen komen.

## Nagekeken
Controleur 9 nov ±18:55 UTC: akkoord na verbeteren. 22 punten, verwerkt: cijfers opnieuw geteld met woordgrenzen (muziek 27 in plaats van 60, zwaar 22 in plaats van 51, geld 38 in plaats van 58; fps 2 in plaats van 17, dat was fout), alle extra tellingen nu in `reviews-tel.py`, twee citaten precies overgezet, humor als GOK in plaats van bewezen gat; seizoensinhoud altijd te halen, boek en wand vol zonder DLC, geluid standaard uit en stil uur in de eerste versie; "brutaler" zonder muur; meer om goud aan uit te geven (meer van dezelfde, drie upgrades); wand van aartsvijanden in plaats van elke hoed; kroniek 5 regels bij hover; ritme en bijnamen gelijk aan de code; regels met namen terwijl je weg bent gevraagd aan Bram; schatkamer van twee rijen; in de breedte, niet dieper; korte vergelijking met de andere twee richtingen.
