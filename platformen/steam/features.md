# Het Hol: features (Sanne, game-ontwerper)

Stand 9 nov 2026, ±19:10 UTC. Richting Het Hol (besluit Thijs 9 nov 19:20). Dit bestand zegt **wat** er in het spel zit en **waarom het leuk is**. Olaf beslist over de bouw en de volgorde, Daan over het uiterlijk.

## De toets (opdracht van Thijs, 18:50): elke feature moet hier langs
| | Eis | Wat het voor ons betekent |
|---|---|---|
| T1 | **Tussendoor** | een blik van 30 seconden levert al iets op: een nieuwe regel in de kroniek, een held die je herkent, iets om goud aan uit te geven. Het spel loopt door als je niet kijkt. |
| T2 | **Grappig om te onderhouden** | humor en karakter: helden met een naam en een wrok, bewoners met een eigen leven. Je wilt het verzorgen en uitbreiden. |
| T3 | **Niet tijdrovend, nooit straffen** | geen dagelijkse plicht, geen grindmuur, niets gaat kapot of dood als je weg bent, elke keuze is terug te draaien. |
| T4 | **Later skins en DLC, eerlijk** | het basisspel is af voor één prijs. Extra's zijn alleen uiterlijk en nieuwe inhoud, nooit sneller of sterker. |

## Wat de toppers ons leren (reviews geteld, 9 nov 2026)
**Bron (GEZIEN):** de meest nuttige Engelse reviews van de openbare communitypagina's van Steam, per spel ±80 negatieve en ±80 positieve, samen 316 negatieve en 305 positieve: Rusty's Retirement (2666510, 97% van 6.625 Engelse reviews positief), Ropuka's Idle Island (3416070, 95% van 2.405), Tiny Pasture (3167550, 93% van 1.209), Deskrawl (4623570, 69% van 472, laatste 30 dagen maar 36% van 1.256). Script en ruwe data: `platformen/steam/data/reviews-haal.py`, `reviews-tel.py`, `data/reviews-2026-11-09/` (telling.txt). Tellen gaat op trefwoorden, dus het zijn grove aantallen; de voorbeelden heb ik zelf gelezen. De API `appreviews` stuurt vanuit onze omgeving door naar de voorpagina (GEZIEN, 302), daarom de communitypagina's.

**Waarom ze stoppen** (316 negatieve reviews):
- **Op na een paar dagen, niets meer te doen**: 82 noemen weinig inhoud, kort of saai; 41 noemen dat het op of klaar is (trefwoorden als end game, nothing to do, ran out; "pretty much completely done after 3 days", "nothing to do with all your money", Rusty's Retirement). Belangrijk: negatieve schrijvers speelden toch lang (mediaan 26 uur bij Rusty's, 50 bij Ropuka's, 179 bij Deskrawl). Ze vonden het leuk tot het opraakte.
- **Grind en muur**: 58 (Deskrawl: zeldzame buit "is 0, just 0" na 230 uur; Ropuka's: "upgrade 1 thing every 6 minutes").
- **Geld en markt**: 58 over geld of DLC; bij Deskrawl noemen 26 van de 78 de ruilmarkt of betalen om te winnen ("takes hundreds of hours to get a single drop that you can buy for a buck on the marketplace").
- **Zwaar of in de weg**: 51 over pc, scherm of venster; 17 missen een fps-instelling; 7 zeggen dat je twee schermen nodig hebt ("it gets in the way unless you have 2 screens", Tiny Pasture).
- **Bugs en save kwijt**: 39 (Tiny Pasture 20: "wipes my save"; Ropuka's: een logbestand van 46 GB).
- **Te veel aandacht nodig, niet echt idle**: 26 ("ended up being a full distraction from my work", Tiny Pasture).
- **Straf als je weg bent**: 9, maar fel ("punishing you for being idle is a very strange choice. If you leave for too long, everyone gets sick", Tiny Pasture).
- **Onomkeerbare keuzes**: 4, alle bij Rusty's ("once you place animals, you can't remove them").
- **Te weinig leven**: "I was hoping for the little frog to do more stuff... instead he just cuts grass and sleeps" (Ropuka's).

**Wat ze prijzen** (305 positieve reviews): naast werk of studie 127, mooi en pixel art 110, voortgang en ontgrendelen 73, muziek 60, rustig 54, prijs 34, klein en licht 34. **Humor: 11 van de 305.** In deze hoek is bijna niemand grappig. Dat is ons gat (T2).

**Wat dat voor Het Hol betekent:** (1) de inhoud mag niet na 3 dagen op zijn: verhalen die zichzelf maken (helden met wrok, hun kinderen) en een verzamelboek dat lang meegaat; (2) geen ruilmarkt, geen zeldzame buit met kleine kans, geen betaalde kracht; (3) klein, zuinig en een fps-instelling; (4) een save die niet kwijt kan; (5) alles terug te draaien; (6) nooit straf; (7) humor als kern, want die mist bij de toppers.

## Het ritme
- **Elke paar minuten:** een held klimt je hol in (GOK: om de 2 tot 4 minuten, Bram rekent het door). Hij loopt naar je schat, loopt in vallen en bewoners, en valt of vlucht. Eén korte regel in de strook.
- **Elk bezoek (30 seconden tot een paar minuten):** je ziet wie er was ("Kees the Twice-Fled is back. Grudge: Gloop"), je geeft je goud uit aan een gang, een val of een bewoner, je hangt een nieuwe hoed aan de wand. Klaar. (T1)
- **Elke dag:** een of twee aartsvijanden die steeds terugkomen; de dag dat je hem eindelijk krijgt is een feestje. Geen dagelijkse beloning, geen plicht. (T3)
- **Elke week:** je hol is groter en voller, je heldenboek dikker, en de kinderen van je oude vijanden komen wraak nemen. (T2)
- **Weg geweest:** bij openen één regel "While you were away: 9 heroes came in, 6 stayed, 3 fled. Gloop is very full." Alleen winst, plafond 12 uur (Bram, `voortgang.gd`), dus een nacht weg levert hetzelfde als een week; niemand hoeft elke dag. (T3)

## Eerste speelbare versie: vijf features, echt goed
Volgorde = belangrijkheid. Grootte bouw is GOK.

### 1. Het hol in de strook, graven met één klik
**Wat:** een doorsnede onder het maaiveld in de breedte, 120 px hoog (96 tot 160 instelbaar). Klik op aarde naast een gang: daar wordt een gang. Een kamer is een stuk gang van 3 cellen breed met twee rijen hoog. De schat ligt achteraan. Graven kost een beetje goud, dus elke val van een held geeft je iets te doen.
**Waarom leuk:** het is jouw hol; je ziet het groeien in één blik (T1). Langer maken = langer pad = meer vallen = meer verhalen.
**Eerlijk:** dichtgooien kan altijd en geeft het goud terug (T3, geen onomkeerbare keuzes zoals bij Rusty's).
**Bouw:** staat al grotendeels (Olaf, `hol.gd`); nog: kosten en terugbetalen.
**Toets:** T1 ja, T2 middel, T3 ja, T4 ja (holthema's zijn later de grootste skin).

### 2. Helden met een naam, een hoed en een karakter
**Wat:** elke held heeft een naam, een hoed (lijf + hoed + wapen uit Daans bladen) en één karaktertrek die je ziet aan hoe hij loopt: **hebzuchtig** (rent recht op de schat af, ook door vallen), **schijterig** (keert om bij een val die hij gezien heeft), en voor versie 1 meer. Bij binnenkomst één regel: "Mara the Greedy climbs into your hole."
**Wat er gebeurt als hij de schat haalt:** hij probeert de stapel op te tillen, die is te zwaar, hij pakt niets en rent weg met een opschepperige bijnaam ("Odo the Hoard-Toucher"). Je verliest niets (T3), maar hij komt brutaler terug. Dat is de spanning, zonder straf.
**Waarom leuk:** helden zijn geen golven poppetjes maar figuren die je herkent. Je praat erover (T2).
**Bouw:** Bram (`held.gd`), staat in taken.
**Toets:** T1 ja, T2 sterk, T3 ja, T4 ja (hoeden en gilden zijn later DLC).

### 3. De wrok: helden die terugkomen (ons eigen stuk)
**Wat:** wie vlucht, komt terug met (a) een **litteken dat je op het poppetje ziet** (pleister, ooglap, verband, een hap uit de hoed), (b) een **wrok** tegen wat hem raakte, bij naam ("Grudge: Gloop the Slime"), en (c) een **bijnaam** (Once-Fled, Twice-Fled, Thrice-Fled). Een held met een wrok loopt eerst naar zijn vijand, niet naar de schat. Na de derde vlucht wordt hij je **aartsvijand**: gouden naamkaartje, en als hij binnenkomt hoor en zie je dat even (klein, binnen de strook). Krijg je hem eindelijk: "Grudge settled. Kees the Thrice-Fled will flee no more." Zijn hoed gaat op een ereplek aan de wand.
**Waarom leuk:** dit maakt de verhalen die mensen in reviews en op Reddit vertellen. Het is wat geen ander taakbalkspel heeft (zie `idee.md`). Spanning zonder straf: hij neemt alleen zijn wrok mee, niets van jou.
**Bouw:** `kroniek.gd` (Bram) heeft bijnaam, wrok en "Grudge settled" al; nog: litteken op het poppetje (Daan tekent 3 tot 4 littekens als losse laag, zoals de hoeden), aartsvijand-kaartje, wrok bepaalt het doel van het lopen.
**Toets:** T1 sterk (je ziet bij elk bezoek wie er terug is), T2 sterkst, T3 ja, T4 ja.

### 4. Bewoners met een eigen leven
**Wat:** om te beginnen één slijm (Gloop) en één val (stekelput). Bewoners hebben een naam, een teller ("Gloop has eaten 12 heroes") en verdienen zelf een bijnaam ("Gloop the Unbudged"). Als er niemand is doen ze iets kleins en grappigs, spaarzaam, want stilstand is zuinig (Olaf, logboek 17:31): slijm slaapt, spuugt na een held een laars uit, kruipt naar een gevallen munt. Een bewoner die verliest gaat **niet dood**: hij is even plat ("Gloop is flat. Back in a minute.") en staat daarna weer op (T3).
**Waarom leuk:** dit is wat je wilt verzorgen (T2) en waar Ropuka's mist dat de kikker "just cuts grass and sleeps". Een bewoner die je kent en die een held met een wrok heeft, is een duel waar je naar uitkijkt.
**Bouw:** Bram (systemen) en Daan (3 kleine leven-animaties per bewoner, meer niet).
**Toets:** T1 ja, T2 sterk, T3 ja, T4 ja (nieuwe bewoners zijn later DLC, hoedjes voor bewoners skins).

### 5. Buit, de trofeeënwand en de kroniek
**Wat:** een gevallen held laat goud achter en zijn **hoed**. Het goud ga je uitgeven (graven, val, bewoner). De hoed hangt in een kamer van je hol: de **trofeeënwand**. Elke soort hoed één keer, met de naam van wie hem droeg. Bij hover in de strook (niet erbuiten) zie je de kroniek: de laatste 20 regels, en per held zijn kaartje (bezoeken, littekens, wrok).
**Waarom leuk:** je ziet je verhaal letterlijk aan de muur hangen. Het geeft een verzameldoel dat niet op geluk draait: elke hoed komt een keer langs (geen kansen van 0,1% zoals bij Deskrawl).
**Bouw:** klein tot middel (Olaf hol, Bram kroniek, Daan de wand).
**Toets:** T1 ja, T2 ja, T3 ja, T4 ja.

**Altijd, in alle vijf (geen feature maar een eis):** strook klein en instelbaar, 15 fps en niet tekenen als er niets beweegt (staat al), een fps-instelling in het menu, save die niet kwijt kan (schrijven naar een tijdelijk bestand, dan hernoemen, plus één reserve), logbestand met een maximum. Dit zijn de klachten 4 en 5 uit de reviews.

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
- **Heldenboek:** elke soort held, trek en hoed één bladzijde; een verzamelboek dat lang meegaat (Birdwatching Notebook, de best verkopende betaalde app van 2026, leunt hier ook op; `idee.md`).
- **De kinderen van je aartsvijand:** een afgerekende aartsvijand heeft soms een kind dat later komt ("Kees II, son of Kees the Thrice-Fled, wants his father's hat back"). Dit is de verhaalmotor die nooit opraakt, zonder grind.
- **Faam:** hoe meer helden je hol overleefden of niet, hoe beroemder je hol en hoe gekkere helden er komen. Faam gaat nooit omlaag.
- **Instellingen:** hoogte, links of rechts, fps, geluid, "stil uur" (geen meldingen).

## Later: skins en DLC (alleen uiterlijk en inhoud, T4)
- **Holthema's** (de grootste skin): ijsgrot, vulkaan, spookslot, snoepgrot. Zelfde spel, ander hol. Tiny Pasture verkoopt al een thema-DLC voor $2,39 (Olaf, `idee.md`, GEZIEN).
- **Heldengilden** als inhoud-DLC: piraten, ridders van de ronde tafel, toeristen met camera's. Nieuwe trekken en hoeden, niet sterker.
- **Seizoenshelden:** kerstman die je hol in klimt, Halloween-helden. Gratis updates of klein pakket.
- **Hoedjes en kleuren voor bewoners.** Supporter Pack zoals alle toppers.
- Regel voor alles hierboven: wie het niet koopt mist geen kracht en geen voortgang.

## Balansdoelen voor Bram (`sim/`)
Alle getallen GOK tot de simulatie ze toetst:
- In de **eerste minuut** valt er minstens één held en zie je goud binnenkomen (de eerste GIF heeft 0 goud na een minuut; zie `spelgevoel.md`).
- In de eerste **10 uur open tijd** is er bij elk bezoek iets om goud aan uit te geven.
- Tijd tot het volgende nieuwe ding groeit langzaam en heeft een plafond (GOK: nooit meer dan 2 uur open tijd), dus geen muur.
- Ongeveer **1 op de 3 helden vlucht** (anders geen wrok en geen verhalen), en een aartsvijand komt gemiddeld één keer per dag langs bij een paar uur open per dag.
- Na 40 uur is het heldenboek ±80% vol (GOK), daarna blijven aartsvijanden en hun kinderen komen.

## Nagekeken
Controleur: zie onderaan, volgt.
