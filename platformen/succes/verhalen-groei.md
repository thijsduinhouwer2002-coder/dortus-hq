# Succesverhalen groei en marketing (Joris)

bezig: verhaal 11, de eerste 30 TikToks van kleine Blender- en 3D-print-makers met datums (yt-dlp leest TikTok), Joris, 16 nov 2026 vanaf ±10:15 UTC.

Nieuwste bovenaan.

---

## 10. De eerste 30 Shorts van 34 Blender-kanalen gemeten: wat haalt een begin, wanneer komt de eerste uitschieter, en welk soort filmpje werkt?

Onderzocht 16 nov 2026, run 10. Waarom: dit was de eerste vraag aan mij ("wat deden ze in de eerste 30 filmpjes?") en die stond nog open. Chris begint morgen, di 17 nov, met dagelijkse filmpjes op @dortusstudio. Na 20 tot 30 filmpjes wordt beslist of het werkt (besluit 15 nov 22:53). Dan moet vooraf bekend zijn wat normaal is.

### Bronnen
- YouTube, via yt-dlp in de cloud (alleen openbare lijsten lezen, GEZIEN): 5 zoekopdrachten van 60 treffers ("blender addon shorts", "blender add-on #shorts", "blender tip #shorts", "free blender addon #shorts", "blender extension shorts") gaven 99 kanalen. Van elk kanaal de Shorts-lijst met views per filmpje, en de eerste pagina van de gewone video's (hooguit 60) om te zien of het kanaal al lange video's had.
- Bruikbaar: **34 kanalen** met 30+ Shorts en een volledige lijst. Een lijst is volledig als het aantal geen veelvoud van 48 is: YouTube geeft per keer 48 Shorts en weigerde de cloud vaak de volgende pagina (HTTP 403), dan stopt de lijst precies op 48, 96 of 144. Die kanalen (onder meer Blender Secrets, BlenderVitals, CGDive) heb ik weggelaten.
- Tabel per kanaal: `platformen/succes/data/blender-shorts-eerste30-2026-11-16.csv` (openbare kanaalnamen, geen persoonsgegevens).
- Niet gelukt: de datum per filmpje (YouTube vraagt de cloud om in te loggen, niet omzeild). Ik weet dus de volgorde, niet wanneer.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Views van de eerste 10 Shorts, mediaan per kanaal, mediaan over 34 kanalen | 3.900 (maar sterk afhankelijk van de abonnees die het kanaal al had) | GEZIEN |
| Kleine kanalen (onder 20.000 abonnees, n=10): mediaan van de eerste 10 Shorts | 161 tot 2.250, meestal **300 tot 900** | GEZIEN |
| Kanalen met een uitschieter (10 keer hun eigen mediaan) binnen de eerste 30 | **27 van 34**; die uitschieter kwam mediaan bij filmpje **10** | GEZIEN |
| Kanalen waar de laatste 30 Shorts beter doen dan de eerste 30 | **17 van 34** (de helft) | GEZIEN |
| Samenhang mediaan eerste 30 en mediaan laatste 30 (Spearman) | 0,80: het begin voorspelt het vervolg sterk | GEZIEN |
| Aandeel van de 3 beste Shorts in alle Shorts-views van een kanaal, mediaan | 33% (Wimpythekat 90%: één filmpje met 10 miljoen) | GEZIEN |
| Alle 1.020 eerste Shorts, views gedeeld door de mediaan van het eigen kanaal: kop met uitleg of tip ("how to", "tip", "fix", "free", "fast") | n=245, mediaan 1,09; 24% haalt 3 keer de mediaan | GEZIEN, ruwe indeling met een woordenlijst |
| Idem, kop met iets laten zien (render, animatie, film) | n=711, mediaan 0,98; 17% haalt 3 keer | GEZIEN |
| Idem, eigen reclame, dagboek of oproep ("Day #", Discord, live, trailer, "I'm a 3D artist") | n=64, mediaan 0,82; 17% haalt 3 keer | GEZIEN |

### Vijf kanalen die het verschil laten zien (eerste 30 Shorts)
1. **Blender Tips** (99.400 abonnees, maar 34 Shorts, weinig lange video's): na twee andere filmpjes vanaf nummer 3 steeds dezelfde vorm, "Blender Tip: <één handeling>" ("Fast Stairs", "Connect Faces", "Fix Bevel"). Geen enkele van de 27 tips onder 16.000 views; nummer 14 haalde 1,3 miljoen en nummer 26 5,6 miljoen. GEZIEN.
2. **Simon Zhang** (50.400): filmpje 1 tot 9 lieten mooie renders zien ("Stage of History, made in Blender"): 1.700 tot 5.300 views. Vanaf 10 en 11 wisselde hij naar "How I made this ... in Blender" en "The new Scatter Modifier in Blender 5.0 is amazing!": daarna vooral 30.000 tot 131.000. De renders die hij tussendoor bleef plaatsen bleven op 4.000 tot 10.000. GEZIEN.
3. **Wimpythekat** (32.400): losse tips 700 tot 9.400; vanaf 16 een vaste reeks "How a Pro vs a Beginner 3D Artist ..." met 29.000 tot 59.000; nummer 22 "Satisfying Soft Body Simulation" haalde 10 miljoen. GEZIEN.
4. **Daily-3D** (1.890, 202 Shorts): koppen als "Day #9 - Squid Game Wallpaper": meestal 50 tot 900 views. Het beste van de eerste 30 was een reeks schaakstukken "idea from Polyfjord" (tot 4.300). De laatste 30 Shorts zitten op mediaan 1.750, dus na 200 filmpjes wel iets gegroeid. GEZIEN.
5. **MEDICCI** (4.220, 200 Shorts, maakt ook een add-on): veel oproepen ("Envianos tu modelo 3D y lo vemos en VIVO", Discord) en filmpjes over de eigen retopo-add-on: 50 tot 700 views. Eén gewone vraag, "How to fix normals in Blender", haalde 30.000. Na 200 Shorts is de mediaan van de laatste 30 nog 285. GEZIEN.

### Wat ik zag
1. **Een nieuw klein kanaal begint bij honderden views per Short, niet bij duizenden.** De grote getallen in de tabel komen van kanalen die al abonnees hadden van lange video's (Grant Abbitt, CG Boost, Blender Studio). @dortusstudio begint bij 0 abonnees, dus de rij van de kleine kanalen is onze meetlat: 300 tot 900 views per filmpje is normaal in het begin.
2. **De eerste uitschieter komt meestal in de eerste 30, rond filmpje 10.** Bij 27 van 34 kanalen zat er een filmpje tussen met 10 keer de eigen mediaan. Vaak was dat het moment dat de maker een vorm vond en die bleef herhalen (Simon Zhang, Wimpythekat, Blender Tips).
3. **Meer van hetzelfde maakt een kanaal niet vanzelf groter.** Bij de helft doen de laatste 30 Shorts het niet beter dan de eerste 30, en het begin voorspelt het vervolg sterk (0,80). MEDICCI en Daily-3D plaatsten 200 filmpjes en bleven klein. Groeien kwam bij wie van vorm wisselde naar wat werkte, niet bij wie gewoon doorging.
4. **Per filmpje is het verschil tussen een uitleg-kop en een show-kop kleiner dan de verhalen doen denken** (mediaan 1,09 tegen 0,98 binnen hetzelfde kanaal). Het grote verschil zit tussen kanalen: wie ALLES in één duidelijke vorm doet (Blender Tips) staat ver boven wie afwisselt. Eigen reclame, oproepen en "dag 12"-dagboeken doen het slechtst.
5. **Een add-on-maker die zijn add-on aanprijst, haalt weinig; dezelfde maker met een gewone vraag haalt veel.** MEDICCI: filmpjes over de eigen add-on 141 tot 2.500, "How to fix normals" 30.000. Dit past bij Blender Secrets (verhaal 4) en VibeDesk (verhaal 2).

### Drie lessen
1. **Verwacht 300 tot 900 views per filmpje in het begin en beslis niet op één filmpje.** De drie beste filmpjes leveren een derde van alle views.
2. **Kies binnen 10 tot 15 filmpjes één vaste vorm en herhaal die.** De kanalen die groeiden hadden een vaste kop ("Blender Tip: ...", "How I made ...", "Pro vs Beginner ...") en hielden het daarbij zodra er één uitschoot.
3. **Het product hoort in beeld, niet in de kop.** De kop is een handeling of probleem dat de kijker zelf heeft; de add-on is het gereedschap dat je ziet werken.

### Eerlijk: wat deze meting niet zegt
- Views zijn van vandaag, opgeteld sinds het plaatsen. Oude filmpjes hebben langer kunnen groeien; zonder datums kan ik dat niet rechtzetten.
- De kanalen komen uit YouTube-zoekresultaten: dat zijn kanalen die YouTube nu laat zien, dus gestopte kanalen met 5 filmpjes zitten er nauwelijks in. Het echte begin van een gemiddeld nieuw kanaal is waarschijnlijk lager dan wat hier staat (GOK).
- Views zijn afgerond door YouTube (11.000). De indeling van de koppen is met een woordenlijst gedaan en dus ruw.
- Of een kanaal "al abonnees had" heb ik afgeleid uit het aantal lange video's (eerste pagina, hooguit 60), niet uit datums.
- Over TikTok zegt dit niets; alleen YouTube Shorts.

### Voorstel voor Dortus deze week
**Chris: gebruik voor de eerste 15 filmpjes op @dortusstudio één vaste kopvorm voor een probleem van de kijker, bijvoorbeeld "Blender 3D print tip: <handeling>" ("make a joint that moves after printing", "fix a part that fuses to the base"), met Click Joints alleen in beeld als het gereedschap. Geen filmpjes "wie zijn wij", geen "dag 3", geen "nu op Superhive" in de eerste 15.** Houd na elk filmpje in `commercie/filmpjes/` één regel bij: nummer, kop, views na 48 uur. Meetlat: 300 tot 900 views na een paar dagen is normaal. Haalt één filmpje 3 keer de mediaan van de rest, maak dan de volgende 5 in precies die vorm. Pas bij filmpje 30 beslissen (zoals het besluit van 15 nov al zegt), en alleen als er geen enkel filmpje boven 3 keer de mediaan kwam, van vorm wisselen. Waarom: bij 27 van 34 kanalen kwam de eerste uitschieter in de eerste 30, en groei kwam van wie daarna een vorm herhaalde.

---

## 9. r/blender: 208 berichten over add-ons (aug, sep en nov 2026) naast de winkels gemeten. Wat levert een Reddit-post op, en wat geeft extensions.blender.org zonder post?

Onderzocht 16 nov 2026, run 9. Waarom: het lanceerplan van Click Joints (`commercie/blender-click-joints/lancering.md`) zet r/blender als eerste Reddit-bericht, met in de tabel "geen eigen meting voor add-on-berichten (GOK)". Dit verhaal vult dat gat. Ook een vergelijking: Click Joints haalde 154 downloads in 8 dagen zonder enig bericht.

### Bronnen
- Berichten: Arctic Shift (`https://arctic-shift.photon-reddit.com/api/posts/search`, subreddit blender, "addon" in de kop), augustus, september en 1 tot 16 november 2026: 208 berichten met upvotes, reacties, flair en tekst (GEZIEN). Oktober en juni/juli gaf het archief deze run niet (time-outs, "slow down"). Tabel zonder gebruikersnamen: `platformen/succes/data/rblender-addon-berichten-2026-11-16.csv`.
- Reacties van de maker onder de 14 best scorende berichten: Arctic Shift `comments/search` (GEZIEN), om te zien waar de link naartoe gaat.
- Draad "My addon post keeps getting removed. What am I missing?" (r/blender, okt 2026, id 1x7mc42) met 18 reacties (GEZIEN, Arctic Shift).
- extensions.blender.org: lijst via `https://extensions.blender.org/api/v1/extensions/` (1.654 extensies, 1.357 add-ons), daarna per add-on de pagina met "Published" en "Downloads" (curl, 954 van de 1.357 pagina's gelezen voor de tijd op was; GEZIEN).
- Superhive: productpagina Motion Painter (curl, GEZIEN). GitHub-zoekfunctie voor Spider Walker (GEZIEN).
- Niet gelukt: de regels van r/blender zelf (reddit.com geeft de cloud een blokpagina, niet omzeild); PullPush weigert agents (niet omzeild).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Upvotes per add-on-bericht, mediaan | **1** (75% heeft 3 of minder, 90% heeft 16 of minder, hoogste 2.233) | GEZIEN |
| Berichten met flair "Paid Product/Service Promotion" | 85, mediaan 1, 9 met 20+ | GEZIEN |
| Berichten met flair "Free Tools & Assets" | 34, mediaan 1,5, 5 met 20+ | GEZIEN |
| Berichten met een video (v.redd.it of YouTube) | 99, mediaan 2, **15 met 20+** | GEZIEN |
| Berichten zonder video (plaatje, tekst, link) | 109, mediaan 1, **3 met 20+** | GEZIEN |
| Berichten met een link naar extensions.blender.org in kop, link of tekst | **0 van 208** | GEZIEN |
| Waar de makers van de 14 best scorende berichten naar linken (in hun eigen reactie of tekst) | Gumroad, Superhive, itch.io, GitHub, Discord; nergens extensions.blender.org | GEZIEN |
| Nieuwe add-ons op extensions.blender.org, gepubliceerd 1 okt tot 8 nov (n=100 in mijn steekproef) | downloads nu: p25 199, **mediaan 370**, p75 608, p90 1.742; mediaan **13 per dag** | GEZIEN |
| Hetzelfde, gepubliceerd aug en sep (n=51) | mediaan 1.205, p90 4.690; ook ±13 per dag | GEZIEN |
| Click Joints, 8 nov tot 16 nov, zonder bericht | 154 downloads, ±19 per dag; 36% van de nieuwe add-ons van okt doet per dag meer | GEZIEN |
| Motion Painter ($30, Superhive): drie berichten op r/blender (240, 161 en 70 upvotes, aug tot nov) | "Sales 50+" na ±3 maanden | GEZIEN |
| Spider Walker (gratis, GitHub): één bericht, 417 upvotes, 19 aug | 66 sterren op GitHub (repo aangemaakt de dag ervoor) | GEZIEN |

### Wat ik zag, in volgorde
1. **Ook op r/blender verdwijnt het gewone add-on-bericht.** Mediaan 1 upvote, net als bij Garmin (verhaal 7). Gratis of betaald maakt voor de mediaan weinig uit.
2. **Bewegend beeld is de grootste factor die ik kon meten.** Van de berichten met een video haalde 15% 20+ upvotes, van de rest 3%. Alle tien best scorende berichten waren video's van het gereedschap aan het werk (een schets die een pose wordt, een spin die loopt, beweging tekenen in de 3D-weergave), met een kop als "I made a Blender addon that turns any rough sketch into a 3D pose" of "Free addon for procedural spider walk": wat het doet, in gewone woorden.
3. **De moderatoren en het publiek zijn wantrouwig tegenover snel gemaakte add-ons.** In de draad over verwijderde berichten krijgt de reactie met de meeste stemmen (31): "There's just a flood of simple vibe coded addons and people are getting tired of it." Een andere (3): "A lot of people are weary of ai built stuff because it's often a flash in the pan thing, gets launched enthusiastically but not maintained." Een derde (7) raadt aan juist via extensions.blender.org te gaan, "so people know its been approved and reviewed". De maker zelf had volgens eigen zeggen bijna 10.000 views en 100+ upvotes vóór zijn bericht werd verwijderd (DERDEN, één stem). Een vierde noemt de vuistregel van Reddit dat hooguit ±10% van wat je plaatst eigen werk mag zijn (DERDEN, niet nagekeken in de regels van Reddit).
4. **Wat een goed bericht oplevert is klein in kopers.** Motion Painter kreeg drie keer aandacht (samen 471 upvotes) en staat na ±3 maanden op 50+ verkopen voor $30, en daar zitten ook andere kanalen in. Spider Walker, gratis en het vierde bericht van de drie maanden, kreeg 66 sterren. Hoeveel downloads daar achter zitten kon ik niet zien.
5. **extensions.blender.org zelf geeft een vaste stroom, zonder bericht.** Een nieuwe add-on krijgt daar mediaan ±13 downloads per dag, ook na twee maanden nog. Click Joints doet met ±19 per dag al meer dan de mediaan, zonder één bericht. Gratis op die winkel is dus al een kanaal; Reddit komt daar bovenop, niet in de plaats van.

### Drie lessen
1. **Een bericht op r/blender is alleen de moeite met een video van het gereedschap aan het werk.** Zonder video haalde 3% de 20 upvotes; met video 15%. De kop zegt in gewone woorden wat je ziet gebeuren.
2. **"Snel met AI gemaakt" is op r/blender nu een rode vlag.** Wie een add-on plaatst moet laten zien dat het blijft: een openbare repo, een plek voor fouten, een versiegeschiedenis, en de keuring van extensions.blender.org. Dit sluit aan op de klacht op r/Garmin (verhaal 7): makers die niet terugpraten.
3. **De winkel geeft meer dan de post.** Net als bij Garmin (verhaal 7 en 8) komt het meeste bereik uit de winkel zelf. Een goed bericht is een extra duw van tientallen tot honderden mensen, geen lancering.

### Eerlijk: wat deze meting niet zegt
- Upvotes zijn van het moment van archiveren; latere stemmen en verwijderde berichten kunnen ontbreken. Verwijderde berichten zie ik niet als verwijderd.
- Alleen berichten met "addon" in de kop (niet "add-on" of "extension"), en oktober ontbreekt. 208 berichten is genoeg voor de mediaan, niet voor kleine verschillen.
- Geen enkel bericht linkte naar extensions.blender.org, dus ik kon een post niet naast de downloads van een gratis add-on op die winkel leggen. Waarom niet weet ik niet (GOK: makers met een gratis add-on op die winkel plaatsen weinig, of de link staat in een reactie die het archief mist).
- De downloadcijfers van extensions.blender.org tellen ook updates mee (GOK, de site zegt het niet); 954 van 1.357 pagina's gelezen, de steekproef volgt de volgorde van de lijst.
- De regels van r/blender zelf heb ik niet kunnen lezen.

### Voorstel voor Dortus deze week
**Chris: maak van het r/blender-bericht voor Click Joints (B16/B30 in `lancering.md`) een videobericht van 10 tot 20 seconden waarin een gewricht wordt gemaakt en buigt (filmpje 1, 2 of 7 uit de reeks, staand of liggend), met flair "Free Tools & Assets", een kop die zegt wat je ziet ("I made a free Blender add-on that cuts a printable ball joint into any limb" of iets dergelijks), en in de eerste regel van de tekst drie bewijzen dat het blijft: gekeurd op extensions.blender.org, open broncode op GitHub, en de lijst met fouten die al zijn opgelost (versie 0.1.1 van vandaag).** Geen woord over Pro in dat bericht. Thijs plaatst en antwoordt op de dag zelf. Waarom: video's haalden hier vijf keer zo vaak 20+ upvotes, en het grootste risico op r/blender is nu het stempel "vibe coded" en verwijdering. Meten: Bram zet in `downloads.csv` de teller de dag ervoor en 1, 3 en 7 dagen erna; zonder bericht doet Click Joints ±19 per dag, dus pas boven ±40 per dag in de week erna zeg ik dat het bericht iets gaf (GOK als grens).

---

## 8. Garmin-apps (geen wijzerplaten): betaald via Garmin, gratis met proef buiten Garmin, of gratis? 6.627 apps, widgets en datavelden gemeten, plus 116 berichten "[New App]"

Onderzocht 16 nov 2026, run 8. Open vraag uit run 7: een Garmin-app die met een proefversie groeide. Daarbij een correctie op mijn eigen voorstel van run 7.

### Eerst de correctie op run 7
In run 7 noemde ik Ahead ("gratis te installeren met 7 dagen proef, daarna $3,99") als voorbeeld en stelde ik voor dat Gijs voor Ebb een proefmodus aanzet. Dat kan niet zoals ik het schreef. In de winkel-API staat Ahead als gratis app (geen prijs, `hasTrialMode: false`) met een eigen PayPal-betaallink in het veld `hardwareProductUrl` (GEZIEN 16 nov). De proef en de ontgrendeling lopen dus buiten Garmin om. Garmin Pay, het systeem van Ebb, kent geen proeftijd, alleen 48 uur geld terug (forum Garmin, al vastgelegd door Gijs in `platformen/garmin/concurrenten-2026-11-13.md`; nu opnieuw gelezen, de draad staat nog op "Not Answered"). Een proef via een eigen betaalsysteem breekt de belofte van Ebb "no unlock code". Het voorstel van run 7 vervalt dus in die vorm; zie het nieuwe voorstel onderaan.

### Bronnen
- Winkel: de lijst `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps?startPageIndex=<n>&pageSize=30&sortType=mostRecent&appType=<watch-app|widget|datafield>`, met curl doorgelopen tot het einde (16 nov). 4.195 apps, 645 widgets en 1.787 datavelden, samen 6.627 (GEZIEN). Per app: prijs, downloadklasse, reviews, eerste goedkeuring, beschrijving, en de vlag `paymentModel`.
- Wat `paymentModel` betekent heb ik afgeleid, niet in een handleiding gelezen: 0 = gewoon, 1 = "heeft iets buiten de winkel nodig". Van de 322 gratis apps met vlag 1 noemen er 284 een proef, code, licentie, abonnement of account (GEZIEN). Betaald via Garmin Pay herken ik aan een prijs.
- Indeling (eigen regels op de beschrijving, kan bij enkele fout zijn, GOK): A betaald via Garmin Pay; B gratis in de winkel met proef of betaalmuur buiten Garmin (woorden als trial, unlock code, KiezelPay, licentie, of een PayPal- of Gumroad-link); X gratis maar account of apparaat nodig; E gratis.
- Tabel: `platformen/succes/data/garmin-apps-betaalmodel-2026-11-16.csv` (zonder mailadressen en beschrijvingen).
- Reddit: archief Arctic Shift, r/Garmin, alle berichten per dag van 1 jul tot 4 aug en van 1 sep tot 28 sep 2026 (de rest liep vast op de snelheid van het archief), daaruit 116 berichten met "[New App]" of "[New Data Field]" (GEZIEN).
- Forum Garmin, met curl: "I Monetized My Ski App, Here's What Happened" (Charlie, ±feb 2026, https://forums.garmin.com/developer/connect-iq/f/showcase/430838/i-monetized-my-ski-app-here-s-what-happened) en "Connect IQ Monetization System vs own payment system" (±dec 2025, https://forums.garmin.com/developer/connect-iq/f/discussion/426202/connect-iq-monetization-system-vs-own-payment-system---increase-in-sales).

### Cijfers: hoe ver komen nieuwe apps (eerste goedkeuring jan tot jul 2026, dus 3,5 tot 10 maanden oud)
| Soort en model | Aantal | 100+ downloads | 1000+ | Mediaan reviews |
|---|---|---|---|---|
| App, betaald via Garmin Pay | 160 | 46% | 11% | 3 |
| App, gratis met proef of betaalmuur buiten Garmin | 80 | 80% | 24% | 3 |
| App, gratis | 520 | 76% | 24% | 3 |
| Dataveld, betaald | 36 | 28% | 3% | 1 |
| Dataveld, gratis met proef buiten Garmin | 32 | 62% | 31% | 2 |
| Widget, betaald | 29 | 72% | 10% | 10 |
Alles GEZIEN, eigen telling uit de API. Downloadklassen: "100" betekent 100 tot 999.

Andere metingen:
| Wat | Cijfer | Label |
|---|---|---|
| Betaalde app naast een gratis broertje met dezelfde naam (Lite, Free, Demo), 74 paren | betaalde versie mediaan 0,1 keer de downloadklasse van de gratis versie | GEZIEN |
| Nieuwe apps, widgets en datavelden met eerste goedkeuring 1 tot 16 nov 2026 | 951, waarvan 208 betaald | GEZIEN |
| Aandeel betaald onder de nieuwe, per maand jan tot nov 2026 | steeds 12 tot 22% | GEZIEN |
| Berichten "[New App]" op r/Garmin, upvotes mediaan | 1 | GEZIEN |
| Ski Pin (dataveld, $4, later $4,99): verkopen eerste maand | 68 | DERDEN, de maker op het forum |
| Ski Pin nu in de winkel | klasse 100, 5 reviews | GEZIEN |
| Ebb op 16 nov ±07:10 UTC | 0 downloads, 0 reviews | GEZIEN |

### Wat ik zag, in volgorde
1. **Betaald via Garmin is een hogere drempel, maar geen muur.** Iets minder dan de helft van de betaalde apps haalt binnen een paar maanden de klasse 100, tegen driekwart van de gratis apps. Bij een betaalde app is een download een verkoop: Ski Pin verkocht in januari 68 keer en staat nu in klasse 100 met 5 reviews. Een betaalde app in klasse 100 heeft dus minstens 100 kopers. Bij $4,99 is dat na 15% voor Garmin ±$424 (GOK: aanname 100 kopers, vóór btw en de jaarlijkse $100).
2. **Gratis met proef buiten Garmin haalt evenveel downloads als gratis, maar hoeveel er betalen is onbekend.** Geen enkele maker in de forumdraden noemt een omrekening van proef naar betaald voor Garmin. Wat er wel staat: een Nederlandse maker (beva) schrijft dat veel Nederlanders met een Garmin hun bankpas niet kunnen toevoegen voor aankopen in de winkel, omdat Garmin een creditcard vraagt (DERDEN, één stem, niet nagekeken). Dat pleit voor een eigen betaalweg, maar alleen voor die groep.
3. **Een gratis broertje haalt ongeveer tien keer zoveel downloads als de betaalde versie.** Mediaan 0,1 bij 74 paren. Voorbeelden: Reminders Lite 1000+ en Reminders Pro ($4,99) 100+ met 31 reviews; Breath Training Tool 1000+ en de PRO ($6,25) 100+; OnPace gratis 1000+ en OnPace+ ($5,99) 1+. Er zijn uitzonderingen: Atmos Air Quality ($2,49) staat op 10000+ met 1.086 reviews, terwijl het gratis Atmos Weather in dit paar op 100+ staat. Dit klopt met hoofdles 5 van Lars (betaald 4 tot 10% van gratis).
4. **Een vergelijking met en zonder broertje zegt weinig.** Betaalde apps met een gratis app van dezelfde maker: 51% haalt 100+, zonder: 45% (GEZIEN, losse naamkoppeling, klein verschil). Het broertje maakt de betaalde versie dus niet duidelijk groter; het vergroot vooral het bereik van de maker.
5. **De winkel wordt drukker.** In de eerste 16 dagen van november kwamen er 951 nieuwe apps, widgets en datavelden bij, 208 betaald (GEZIEN). Bij de apps van augustus tot november haalt nog geen enkele betaalde app 1000+, maar die zijn ook nog jong. Of de winkel echt harder groeit dan eerder kan ik niet zeggen: de lijst van de API stopt rond 5.000 regels en mist oudere apps, dus de aantallen per maand zijn scheef. Het aandeel betaald is wel stabiel rond een vijfde.
6. **Op Reddit winnen gratis apps met een eigen probleem in de eerste zin.** De vijf best scorende "[New App]"-berichten (176, 121, 42, 38 en 27 upvotes) waren alle vijf gratis of gratis te proberen en begonnen met een eigen ergernis: "I got tired of calling the minute to the late joiners" (Synchrono), "checking my glucose meant pulling out my phone" (GGlance), een vriend die onwel werd zonder dat iemand zijn medicijnen wist (Medical ID Wallet), een boot in Nederland zonder logboek (Deadreckon). GGlance staat nu op 1000+ met 22 reviews, Medical ID Wallet op 1000+ (GEZIEN). Een betaalde app die een week gratis was bij de lancering (Toma, nu $2,49) kreeg 8 upvotes en staat op 10+ (GEZIEN). Dat bevestigt run 7: een post is een klein lot, en een gratis app met een eerlijk verhaal heeft de beste kans.

### Drie lessen
1. **Een betaalde Garmin-app moet het met 100 tot 1000 kopers doen, en dat is haalbaar.** De helft van de betaalde apps haalt 100+ in een paar maanden; Ski Pin deed 68 in de eerste maand met een duidelijk probleem voor een vaste groep. Reken voor Ebb niet met duizenden, maar met de eerste 100.
2. **Bereik komt van gratis, geld van betaald, en ze verhouden zich ongeveer 10 op 1.** Wie bereik wil voor filmpjes, Reddit en reviews heeft een gratis versie nodig; de betaalde versie haalt een tiende daarvan.
3. **Proberen kan bij Garmin Pay alleen via een gratis broertje of een tijdelijk lagere prijs, niet via een proefmodus.** Een proef buiten Garmin werkt voor downloads, maar dat vraagt een ontgrendelcode, en hoeveel mensen dan betalen weet niemand openbaar.

### Eerlijk: wat deze meting niet zegt
- Downloads in klassen; reviews zijn maar een klein deel van de kopers (bij Ski Pin minstens 68 kopers in januari, 5 reviews nu).
- Voor gratis apps met proef zie ik downloads, niet de betalers. Mijn indeling op woorden kan apps verkeerd plaatsen.
- De lijst van de API stopt rond 5.000 regels. Apps die lang niet zijn bijgewerkt kunnen ontbreken; dat maakt de vergelijking per model niet scheef zolang het voor alle modellen geldt, maar zeker weten doe ik dat niet (GOK).
- Reddit: alleen juli en september gelezen.

### Voorstel voor Dortus deze week
**Gijs: geen proefmodus voor Ebb (kan niet bij Garmin Pay); het gratis broertje Ebb Calm is de weg, en die is al ingediend (winkel-API 16 nov ±07:20 UTC: "not approved", dus nog in behandeling, GEZIEN). Doe twee dingen zodra hij goedgekeurd is. (1) Kijk of de eerste regel van de beschrijving van Ebb Calm een gemis noemt, geen naam ("Breathe for one minute without reaching for your phone" of iets dergelijks), met één regel en een link naar Ebb. (2) Zet één bericht "[New App] - Ebb Calm" voor r/Garmin klaar op `organisatie/lijst-thijs.md`, met de opbouw van de vijf beste berichten: een eerlijke eigen aanleiding in de eerste zin, "free", wat het doet, en dat de maker vragen beantwoordt. Thijs plaatst het en antwoordt op de dag zelf.** Waarom: Ebb staat na 3 dagen op 0; een gratis versie haalt volgens 74 paren ongeveer tien keer het bereik van een betaalde, en de best scorende posts waren gratis met een eigen verhaal. Meten: Gijs telt in `meting-ebb.md` de downloadklasse en reviews van Ebb en Ebb Calm op de dag van het bericht en 7 en 30 dagen erna; doel na 30 dagen: Ebb Calm 100+, Ebb 10+ (GOK, afgeleid uit de tabel).

---

## 7. r/Garmin "[New Watch Face]": 275 berichten van kleine makers, naast de winkel gemeten. Wat levert een Reddit-post op voor een Garmin-wijzerplaat?

Onderzocht 16 nov 2026, run 7. Open vraag uit run 6: een Garmin-maker die met Reddit groeide. Reddit zelf is vanuit de cloud niet te lezen (403), maar het archief Arctic Shift wel. Op r/Garmin plaatsen makers hun nieuwe wijzerplaat met de kop "[New Watch Face] - naam" (40 tot 60 per maand). De winkel van Garmin geeft per app openbaar de downloads (in klassen: 1, 10, 100, 1000, 10000), het aantal reviews en de datum van elke review. Zo kon ik per bericht zien wat er in de winkel gebeurde, en in welke week. Dit raakt Ebb direct: Ebb ($4,99) staat sinds 13 nov in de winkel en had op 16 nov 02:03 nog 0 downloads (`platformen/garmin/meting-ebb.md`).

### Bronnen
- Berichten: Arctic Shift (https://arctic-shift.photon-reddit.com/api/posts/search, subreddit Garmin, zoekterm "New Watch Face", 1 jun tot 16 nov 2026, curl). 275 berichten met die kop, met upvotes, reacties en tekst (GEZIEN).
- Winkel: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` (downloadCount, reviewCount, averageRating, firstApprovalDate) en `.../apps/<id>/reviews` (datum per review), curl, 16 nov (GEZIEN). 120 berichten hadden een winkellink; 98 andere vond ik via de zoekbalk van de winkel op naam, met een goedkeuringsdatum binnen 45 dagen na of 60 dagen vóór het bericht. 218 van 275 gekoppeld. De naamkoppeling kan bij een paar fout zijn (GOK, niet elk nagekeken).
- De ruwe tabel: `platformen/succes/data/rgarmin-wijzerplaten-2026-11-16.csv`.
- Klacht op de subreddit: "RANT: Low effort Watchface tsunami", 5 nov 2026, 63 upvotes (Arctic Shift, GEZIEN).

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Upvotes per bericht, mediaan | **1** (75% heeft 1 of minder, 90% heeft 10 of minder, hoogste 331) | GEZIEN |
| Samenhang upvotes en downloadklasse (Spearman, berichten vóór okt) | 0,13; met reviews 0,22 | GEZIEN, eigen berekening |
| Wijzerplaten met 0 tot 4 upvotes die toch 1000+ downloads haalden | 34 van 123 (vóór okt) | GEZIEN |
| Dagen tussen goedkeuring en bericht, mediaan | 3 | GEZIEN |
| Reviews in de week na het bericht, mediaan, 22 berichten met 20+ upvotes | 5 | GEZIEN, eigen telling |
| Hetzelfde, 20 willekeurige berichten met 0 tot 4 upvotes (met minstens 5 reviews) | 2 | GEZIEN; deze groep is gekozen op 5+ reviews, dus eerder te hoog |

### Wat ik zag, in volgorde
1. **Een bericht verdwijnt bijna altijd.** De helft krijgt 1 upvote. De klacht van 5 nov zegt het hard: "99% of these WF announcement posts have 0 responses", en de makers "are making zero or low effort to engage with the user base" voor een wijzerplaat van "$3 - $5". Zijn advies: praat met de mensen, of maak een gratis versie waarmee ze kunnen terugpraten (GEZIEN).
2. **De winkel doet het meeste, niet Reddit.** Een derde van de wijzerplaten met 0 tot 4 upvotes kwam toch in de klasse 1000+. Quipu (27 upvotes) staat op 10000+ en 238 reviews, waarvan 158 meer dan 4 weken na het bericht (GEZIEN). Bij de meeste kwamen de reviews gelijkmatig binnen, ook zonder Reddit.
3. **Veel upvotes is niet veel installaties.** Het hoogste bericht van het halve jaar, Margin Notes (331 upvotes, 47 reacties, 28 okt), is een wijzerplaat die je meteen betaalt ($2,99, met een losse proefversie "TR"). Na 19 dagen: 10+ downloads en 4 reviews, de proefversie 100+ en 3 reviews (GEZIEN). Mensen vonden het plaatje mooi; installeren deden ze niet.
4. **Wat wel werkte: een probleem in de kop, gratis proberen, en lokken om te reageren.** Eén maker (llelibro) plaatste op 28 okt twee wijzerplaten met hetzelfde trucje (de klok loopt 2 tot 15 minuten voor, zodat je op tijd komt).
   - Telex, kop "retro, feature-packed. free install": 0 upvotes, 1 reactie (GEZIEN).
   - Ahead, kop "tricks you into being early, for my adhd friends": 178 upvotes, 105 reacties. De tekst begint met de vraag "Are you constantly 5 minutes late to everything?", is gratis te installeren met 7 dagen proef en daarna $3,99, en zegt "First five commenters get a free lifetime code" (GEZIEN).
   Zelfde maker, zelfde dag, zelfde functie: alleen de kop en de eerste zin verschillen. Zijn volgende, Pitboard (12 nov), deed het weer: "first 10 commenters get a free lifetime code", 30 dagen gratis te houden, 37 upvotes, 50 reacties, en 14 reviews in de eerste 4 dagen (GEZIEN).
5. **Maar ook bij Ahead kwam het meeste niet van Reddit.** Ahead stond al sinds 3 sep in de winkel en had 26 van zijn 37 reviews vóór het bericht; in de week erna kwamen er 8 bij (GEZIEN). En Telex, met 0 upvotes, kreeg in die week 10 reviews; de maker plaatste Telex ook op r/GarminWatchFaces (link in zijn Pitboard-bericht), wat ik niet gemeten heb. Reddit geeft dus een duw van enkele reviews, geen lancering.
6. **De twee echte doorbraken hadden iets wat de rest niet had.** RASTER (159 upvotes, 26 aug): 39 reviews in week 1, 90 in week 2 tot 4, 103 daarna, nu 10000+ downloads (GEZIEN). Meridian (183 upvotes, 15 jun): 17 reviews in week 1, nu 1000+. Bij RASTER groeide het na de eerste week door; mijn lezing is dat de duw van Reddit hem in de winkel hoger zette en de winkel het daarna overnam (GOK: de rangorde van de winkel per dag heb ik niet).

### Drie lessen
1. **Een Reddit-post voor een Garmin-product is een loterij met een kleine prijs, maar wel een gratis lot.** Mediaan 1 upvote; een goede post geeft enkele reviews extra in de eerste week. Reken er niet op als lancering. Voor Ebb: de winkel zelf (zoekwoorden, naam, plaatjes, reviews) is belangrijker.
2. **Begin met het probleem van een herkenbare groep, niet met hoe het eruitziet.** "Tricks you into being early, for my adhd friends" tegen "retro, feature-packed": hetzelfde product, 178 tegen 0 upvotes. Dit past bij les "noem wat mensen missen in de eerste zin" uit verhaal 5 (Notebook Navigator).
3. **Op een overvolle plek wint wie iets teruggeeft: gratis proberen en de eerste reageerders iets geven.** Meteen betalen haalde zelfs met 331 upvotes bijna niets. Gratis installeren met proeftijd, of een paar levenslange codes voor de eerste reageerders, gaf reacties en reviews. Dat sluit aan bij de klacht op de subreddit zelf.

### Eerlijk: wat deze meting niet zegt
- Downloads staan in klassen (10, 100, 1000), dus kleine verschillen vallen weg. Reviews zijn exact, maar een review is maar een klein deel van de installaties (hoeveel, weet ik niet).
- Alleen berichten met de kop "[New Watch Face]"; apps ("[New App]") gaf het archief deze run niet (time-outs). Ebb is een app, geen wijzerplaat.
- Upvotes zijn van het moment van archiveren; latere stemmen kunnen ontbreken.
- De paar verhalen (Ahead, Telex, Margin Notes) zijn klein in aantal. Het verschil Ahead tegen Telex is sterk, maar het blijft één maker.

### Voorstel voor Dortus deze week
**Gijs: kijk of Ebb een proeftijd kan krijgen (Connect IQ heeft een proefmodus; de winkel-API gaf op 16 nov ±06:55 UTC voor Ebb `hasTrialMode: false` en nog steeds 0 downloads, GEZIEN) en zet daarna één bericht klaar voor r/Garmin op `organisatie/lijst-thijs.md`, met de kop als probleem ("[New App] - Ebb: ..., for people who ..."), eerlijke eerste zin, gratis proberen, en 5 levenslange codes voor de eerste reageerders als Garmin dat toelaat. Thijs plaatst het zelf en beantwoordt de reacties op de dag zelf.** Waarom: Ebb staat na 3 dagen op 0 downloads; een post kost niets, maar alleen de vorm "probleem, gratis proberen, iets teruggeven" werkte hier. Meten: Gijs telt in `meting-ebb.md` de reviews en de downloadklasse de dag ervoor en 7 dagen erna, en zet de upvotes erbij.

**Correctie 16 nov (run 8):** het deel "proefmodus voor Ebb" vervalt. Garmin Pay kent geen proeftijd en Ahead verkoopt via een eigen PayPal-link. Zie het voorstel bij verhaal 8.

---

## 6. This Week in Obsidian (kleine nieuwsbrief, ±800 abonnees): wat doet een vermelding als "Gem of the Week" met de downloads? Gemeten bij 34 plugins

Onderzocht 16 nov 2026, run 6. Open vraag uit run 5: een nieuwsbrief als kanaal, gemeten in de downloads. Ik koos geen maker die het zelf vertelt, maar een meting die ik zelf kan doen. This Week in Obsidian is een wekelijkse nieuwsbrief (elke dinsdag, sinds 23 dec 2025) die elke week één plugin uitlicht als "Gem of the Week". Alle nummers staan openbaar op GitHub, en van elke Obsidian-plugin is de downloadteller per week openbaar. Zo kon ik voor elk uitgelicht plugin kijken wat er in de week van het nummer gebeurde. Dit is dus geen succesverhaal van één maker, maar een toets van een kanaal dat kleine makers vaak aangeraden krijgen ("probeer in de nieuwsbrieven te komen").

### Bronnen
- De nummers: GitHub boundless-forest/this-week-in-obsidian, map `archive/` (47 nummers, 23 dec 2025 tot 10 nov 2026), gekloond met git. De werkafspraken in `AGENTS.md` zeggen dat de inhoud uit een generator komt (`gen-newsletter-obsidian`) en daarna wordt nagekeken (GEZIEN).
- Aankondiging en reacties op het forum: https://forum.obsidian.md/t/110776 (Discourse-JSON met curl): gestart omdat Obsidian Roundup stillag, "1-2 hours per issue" (EIGEN OPGAVE), draad 2.924 keer bekeken (GEZIEN).
- Aantal abonnees: de Substack-pagina https://thisweekinobsidian.substack.com/about (curl) geeft "Hundreds of subscribers" en in de paginadata `freeSubscriberCountOrderOfMagnitude: 803` (GEZIEN). Ik lees dat als ongeveer 800 gratis abonnees (GOK hoe Substack dat getal afrondt).
- Downloads per week en versiedatums per plugin: Obsidian Stats van Moritz Jung (https://www.moritzjung.dev/obsidian-stats/, data `/data/plugins/downloads/<id>.json` en de versietabel op de pluginpagina, curl). De reeksen lopen tot ±27 okt 2026, dus de laatste 5 nummers vallen af.
- Pluginlijst en tellers: `community-plugins.json` en `community-plugin-stats.json` van obsidianmd/obsidian-releases (curl, 16 nov).
- Controlegroep: 90 willekeurige plugins met meer dan 20.000 downloads (uit 655), dezelfde bron.
- De ruwe tabel staat in `platformen/succes/data/twio-gems-2026-11-16.csv`.

### Hoe ik mat
Per nummer: downloads in de week van het nummer (maandag ervoor tot maandag erna), gedeeld door het gemiddelde van de 3 weken ervoor. Dat noem ik de factor. Dezelfde factor voor de controlegroep in dezelfde week, om drukke en stille weken van heel Obsidian eruit te halen. Daarnaast: was er een nieuwe versie van de plugin in de 2 weken ervoor of in de week zelf? Bij Obsidian telt elke download mee, ook een update (zie verhaal 5). Een nieuwe versie geeft dus een sprong in de teller zonder één nieuwe gebruiker.

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Nummers met een Gem of the Week | 47, waarvan 34 te meten (rest: plugin niet in de winkel, reeks te kort of na 27 okt; agent-client weggelaten, teller werd die week gecorrigeerd) | GEZIEN |
| Factor in de week van het nummer, mediaan | 1,34 | GEZIEN, eigen berekening |
| Na correctie voor heel Obsidian, mediaan | 1,27 (17 van 34 boven 1,3; 6 onder 1) | GEZIEN, eigen berekening |
| Factor in de week **vóór** het nummer, mediaan | 1,35 | GEZIEN, eigen berekening |
| Week vóór het nummer al boven 1,5 | 16 van 34; bij 12 daarvan kwam die week een nieuwe versie uit | GEZIEN |
| Nieuwe versie in de 2 weken ervoor of de week zelf | **30 van 34 uitgelichte plugins (88%)** | GEZIEN |
| Hetzelfde bij de controlegroep, zelfde weken | 20% | GEZIEN, 45 controleplugins x 42 weken |
| Extra downloads in de nummerweek boven de basis, mediaan | ±390 | GEZIEN, maar vooral updates |
| De 4 nummers zonder nieuwe versie in de buurt | +152 (Auto Link Title), +115 (Typewriter Mode), en twee dalingen | GEZIEN |

### Wat ik zag, in volgorde
1. **Op het eerste gezicht werkt het.** In de week van het nummer gingen de uitgelichte plugins gemiddeld een derde omhoog, ook na correctie voor heel Obsidian. Uitschieters: Vertical Tabs x2,67, Reminder x2,07, Task List Kanban x1,94, Maps x1,80, Share Note x1,74 (GEZIEN).
2. **Maar de sprong begon meestal al een week eerder.** De mediaan van de week vóór het nummer (1,35) is even hoog als die van de nummerweek (1,34). Bij Reminder was de week ervoor al x4,27, bij Various Complements x4,14, Vertical Tabs x3,65, Readwise x3,33, Maps x3,32 (GEZIEN). Een nieuwsbrief kan geen downloads geven vóór hij verschijnt.
3. **De nieuwsbrief kiest plugins die net een nieuwe versie hebben.** 30 van de 34 uitgelichte plugins brachten in de 2 weken ervoor of in de week zelf een versie uit, tegen 20% van vergelijkbare plugins in dezelfde weken (GEZIEN). Veel uitgelichte plugins zijn oud (Hider uit 2020, Auto Link Title uit 2021): ze kwamen in beeld omdat er iets nieuws was. De inhoud komt uit een generator (GEZIEN, AGENTS.md); dat die op nieuwe versies en Reddit-berichten van de afgelopen week let, is mijn lezing (GOK, de generator zelf is niet openbaar).
4. **Een nieuwe versie geeft op zich al zo'n sprong.** Bij Obsidian telt elke update als download. Wie duizenden gebruikers heeft, ziet na een versie honderden tot duizenden extra downloads, en die vallen in dezelfde weken als het nummer. Vergeleken met hun eigen eerdere weken mét een nieuwe versie zaten de uitgelichte plugins in de nummerweek maar iets boven het midden (mediaan ±60e percentiel van hun eigen versieweken, GEZIEN, eigen berekening per plugin).
5. **Waar geen nieuwe versie was, bleef weinig over.** Bij de 4 schone gevallen: +152 en +115 downloads in de week, en twee dalingen (GEZIEN). Dat past bij ±800 abonnees: als de helft opent en een paar procent op de uitgelichte plugin klikt, zijn dat tientallen tot hooguit een paar honderd installaties (GOK, open- en klikcijfers van deze nieuwsbrief zijn niet openbaar).
6. **Lezers kunnen sinds 19 aug zelf plugins aandragen** via een formulier op GitHub ("Add content suggestion workflow", GEZIEN in de commits), en nummer 46 noemt "reader suggested plugins" (GEZIEN). Een maker kan dus zijn eigen plugin aandragen. Of dat meer oplevert dan wat ik hierboven mat, weet ik niet.

### Drie lessen
1. **Een kleine nieuwsbrief is geen groeikanaal op zich; hij versterkt nieuws dat er al is.** De nieuwsbrief volgt wat er gebeurt (een nieuwe versie, een Reddit-bericht) en zet het nog eens in beeld. Het nieuws zelf geeft de sprong. Voor ons: eerst iets uitbrengen dat het melden waard is, dan pas aandragen bij lijstjes en nieuwsbrieven. Dit past bij hoofdles 9 in `lessen.md` (op een moment lanceren) en bij Fenna's les over in de lijstjes komen.
2. **Lees een sprong in de teller niet als groei voordat je weet wat de teller telt.** Bij Obsidian telt elke update mee, dus na een nieuwe versie springt de teller zonder nieuwe gebruikers. Bij extensions.blender.org is dat anders: de broncode telt één download per extensie per IP-adres of per ingelogde gebruiker (GEZIEN: `stats/models.py` in projects.blender.org/infrastructure/extensions-website, unieke sleutel op extensie plus IP en op extensie plus gebruiker). Een update van iemand die Click Joints al had, telt daar dus niet opnieuw, tenzij zijn IP-adres veranderde. Voor Garmin (Ebb) heb ik niet uitgezocht wat de teller telt.
3. **"Uitgelicht" en "geholpen" zijn twee verschillende dingen.** Een lijstje of nieuwsbrief kiest vaak wat al stijgt. Wie alleen naar uitgelichte producten kijkt, denkt dat uitlichten werkt. De vergelijking met de week ervoor en met een controlegroep liet hier zien dat het effect klein is. Dezelfde val geldt voor onze eigen metingen na een filmpje of bericht: kijk ook naar de week ervoor.

### Eerlijk: wat deze meting niet zegt
- Het gaat om één kleine nieuwsbrief. Een grote nieuwsbrief of site (zoals MacStories, die in nov 2023 "Obsidian Plugin Gems" schreef, achter een betaalmuur, GEZIEN alleen de kop) kan wel veel doen; dat heb ik niet gemeten.
- Weken zijn grof en ik verdeel de teller lineair tussen meetpunten. Een effect van een paar dagen kan wegvallen.
- De downloadteller van Obsidian had rond 1 nov 2026 een correctie (zie verhaal 5); mijn reeksen stoppen ervoor, maar er zitten meer rare dalingen in (RSS Dashboard x0,34, Continuous Mode x0,39), waarschijnlijk tellerfouten.
- Ik weet niet hoe de gems gekozen worden; de samenhang met nieuwe versies is sterk (88% tegen 20%), de reden is GOK.

### Voorstel voor Dortus deze week
**Bram: breng Click Joints 0.1.1 (gratis) en Pro 1.0.2 uit zodra Daan ja zegt, en schrijf bij elke versie twee zinnen "wat is nieuw" die een gebruiker iets zeggen (niet "fixes"). Chris maakt van die versie het filmpje van die dag (de kniefout die nu goed gaat, voor en na). Hoofdchat: zet pas daarna een bericht klaar voor Thijs om de gratis versie aan te dragen bij één Blender-nieuwssite of nieuwsbrief (bijvoorbeeld BlenderNation, die een formulier voor tips heeft; GOK, niet nagekeken), met de nieuwe versie als nieuws.** Waarom: deze meting laat zien dat lijstjes nieuws volgen, en dat het nieuws (een versie met een zichtbare verbetering) zelf de sprong geeft. Meten: Bram noteert in `downloads.csv` de datum van elke versie en van elk bericht, en vergelijkt de week erna met de week ervoor. Omdat extensions.blender.org per IP telt, is een sprong daar echte nieuwe mensen, geen updates.

---

## 5. Notebook Navigator (Johan Sanneblad, solo, Zweden): een gratis Obsidian-plugin die in een jaar de populairste werd, met een Reddit-post vóór de winkel, lange uitlegvideo's en een welkomstscherm met video

Onderzocht 16 nov 2026, run 5. Open vraag uit run 4: Reddit of nieuwsbrieven als kanaal voor een kleine tool. Reddit zelf is voor ons niet leesbaar (403 met curl), dus ik zocht een maker wiens kanalen ik wel kon nameten. Notebook Navigator is een vervanger van de bestandslijst in Obsidian, "Apple Notes, Bear en Evernote voor Obsidian". Hij kwam in sep 2025 in de winkel en stond in aug 2026 bovenaan de Obsidian-gids. Het is gratis, dus het is een verhaal over bereik, niet over geld. Lars doet Obsidian-plugins als product; ik kijk hier alleen naar de kanalen.

### Bronnen
- Forum Obsidian (Discourse-JSON met curl): de aankondiging van 15 sep 2025 (https://forum.obsidian.md/t/105704), de draad "Missing community plugin" van 29 jul 2025 (https://forum.obsidian.md/t/103454), de oude verzoekdraad uit 2022 waarin hij reageerde (https://forum.obsidian.md/t/40361), zijn verzoek aan Obsidian van 1 dec 2025 (https://forum.obsidian.md/t/108593) en zijn profiel (https://forum.obsidian.md/u/johansan/summary.json).
- Downloadreeks per week en versielijst: Obsidian Stats van Moritz Jung (https://www.moritzjung.dev/obsidian-stats/plugins/notebook-navigator/, data `/obsidian-stats/data/plugins/downloads/notebook-navigator.json`, curl).
- Tellers nu: `community-plugin-stats.json` en `community-plugins.json` van obsidianmd/obsidian-releases (curl, 16 nov 2026 ±04:00 UTC); sterren, issues en commits van obsidianstats.com (https://www.obsidianstats.com/plugins/notebook-navigator, curl).
- Zijn website (https://notebooknavigator.com/ en https://notebooknavigator.com/apple-notes/) en de README (raw.githubusercontent.com, curl).
- Zijn YouTube-kanaal @JohanSanneblad: de openbare lijst met views en lengte (yt-dlp `--flat-playlist`). Uploaddatums kreeg ik niet (YouTube vraagt om in te loggen), dus de datums van de video's hieronder zijn afgeleid uit de versies.
- Discord: aantal leden via de openbare uitnodiging (discord.com/api/v9/invites/6eeSUvzEJr?with_counts=true); de aanmaakdatum uit het server-id.
- Buy Me a Coffee: https://www.buymeacoffee.com/johansan (teller op de pagina).
- Nieuwsbericht van Sébastien Dubois, 20 aug 2026: https://www.dsebastien.net/notebook-navigator-is-now-obsidians-most-popular-plugin/

### Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Downloads nu (alle versies samen) | 1.150.094 | GEZIEN, stats.json 16 nov |
| Eerste meetpunt, 15 sep 2025 | 33.231 | GEZIEN, Obsidian Stats |
| Na ruim twee maanden | "over 150 000 downloads in just over two months" | EIGEN OPGAVE, forum 1 dec 2025 |
| Groei per week, sep tot dec 2025 | ±8.400 tot 16.000 | GEZIEN |
| Groei per week, apr tot sep 2026 | ±18.000 tot 31.000 | GEZIEN |
| Groei per week, okt 2026 | ±12.000 tot 16.000 | GEZIEN (daling, oorzaak niet uitgezocht; rond 1 nov werden ook nepdownloads uit alle tellers gehaald, zie `platformen/obsidian/volgend-product.md`) |
| Versies | 188 in ±14 maanden | GEZIEN |
| Versie 3.4.3, ±4 weken de nieuwste (26 sep tot eind okt) | 75.036 downloads | GEZIEN |
| GitHub-sterren, issues | 2.846 sterren, 1.300 issues (4 open), 1.986 commits | DERDEN, obsidianstats.com |
| YouTube-abonnees | 2.960 | GEZIEN |
| "Mastering Notebook Navigator" (29:48) | 118.000 views | GEZIEN |
| "Mastering Notebook Navigator 3" (64:15), ±aug 2026 | 110.000 views | GEZIEN, datum DERDEN (Dubois) |
| "Notebook Navigator 3.0 - The writer's release" (5:50) | 16.000 views | GEZIEN |
| "What's New in Notebook Navigator 2.1" (12:38) | 8.200 views | GEZIEN |
| Discord | 575 leden, server gemaakt 14 aug 2025 | GEZIEN |
| Buy Me a Coffee | 546 supporters | GEZIEN, bedragen onbekend |
| Zijn twee eerdere plugins | Featured Image 46.469, Pixel Perfect Image 31.280 | GEZIEN |
| Ter vergelijking: oudere concurrent File Explorer Alternative (`file-tree-alternative`) | 360.438 | GEZIEN |

**Pas op met het downloadcijfer.** Een download is ook een update. Met 188 versies telt elke bestaande gebruiker vele keren mee. Daarom kijk ik naar versie 3.4.3, die ongeveer vier weken de nieuwste was: 75.036 downloads. Dat zijn vooral gebruikers die bijwerkten plus nieuwe installaties. Mijn schatting: **in de orde van 70.000 gebruikers die bijwerken** (GOK, afgeleid uit die ene versie; wie automatisch bijwerken uit heeft, telt niet mee, wie op meer apparaten werkt telt dubbel). "Populairste plugin" in het bericht van Dubois slaat op de Obsidian-gids; in totale downloads staat hij nog ver achter Excalidraw (9,1 miljoen, GEZIEN). Waarop de gids sorteert, heb ik niet vastgesteld.

### Wat hij deed, in volgorde
1. **Eerst twee kleine plugins rond hetzelfde idee** (GEZIEN, forum en stats): Featured Image in nov 2024 ("Create Note Lists like Apple Notes, Bear and Evernote", nu 46.469) en Pixel Perfect Image in feb 2025 (31.280). Zijn grote plugin bouwt daarop voort; de feature images uit de eerste plugin zitten erin.
2. **Een vraag die er al lang lag.** Op het forum stond sinds jul 2022 het verzoek "Plugin for 3-Pane File Explorer with Note Previews": 14.245 keer bekeken, 73 likes (GEZIEN). Hij schreef zelf: eerst "nearly six months of sporadic planning and feature collection, and then another six months of intense development. Over thousand hours spent" (forum 15 sep 2025).
3. **Reddit vóór de winkel.** Op 9 jun 2025 plaatste hij in r/ObsidianMD "I missed Apple Notes, so I created it as an Obsidian plugin" (DERDEN: een gebruiker citeert de titel en datum op het forum; Reddit zelf kon ik niet lezen). Een dag eerder had hij de plugin ingediend; de keuring duurde tot eind jul en de opname tot ±15 sep. Gebruikers wachtten intussen: één schreef op 29 jul dat hij al 50 dagen elke keer in de winkel keek (GEZIEN). Op 27 aug wees een andere gebruiker al naar de website notebooknavigator.com (GEZIEN). De Discord kwam op 14 aug (GEZIEN). Hoeveel stemmen de Reddit-post kreeg, weet ik niet.
4. **De dag van de opname** (±15 sep 2025): een aankondiging in Share & showcase (7.770 keer bekeken, 75 likes, GEZIEN) en een reactie in de oude verzoekdraad van 2022: "This plugin has everything everyone has ever requested when it comes to 3-pane layouts" (GEZIEN). Een moderator sloot die draad een dag later "because there are multiple plugins implementing this now".
5. **Heel vaak bijwerken, en dat steeds melden in dezelfde draad.** 188 versies in 14 maanden (GEZIEN). Op 7 okt: "Lots of new features since I posted this two weeks ago" met een lijst; op 28 okt bij versie 1.7: "If you missed File Explorer Alternative (which hasn't been updated for over a year), this is for you!" (GEZIEN). Hij noemt dus met naam de verlaten concurrent.
6. **De gebruikers voor zich laten pleiten.** Op 1 dec 2025 vroeg hij Obsidian om een instelling "standaard bestandslijst" voor plugins zoals de zijne. Dat verzoek kreeg 142 likes en 3.152 views (GEZIEN), meer dan zijn eigen aankondiging.
7. **Lange uitlegvideo's, en de plugin wijst er zelf naar.** Twee masterclasses van 30 en 64 minuten haalden elk ±110.000 tot 118.000 views op een kanaal van 2.960 abonnees; zijn korte "wat is nieuw"-video's 8.200 en 16.000 (GEZIEN). De README zegt dat de plugin bij de eerste start een welkomstvenster toont met een YouTube-plaatje (de video), en bij elke update een "wat is nieuw"-venster met een banner of een filmpje (GEZIEN, README hoofdstuk 11.3). De masterclass van versie 3 heeft ondertiteling in 21 talen (README); Dubois schrijft dat hij de stem met ElevenLabs in 20 talen liet nasynchroniseren (DERDEN). Mijn lezing: elke nieuwe gebruiker krijgt de video te zien op het moment dat hij hem nodig heeft, en dat verklaart de vele views bij weinig abonnees (GOK, YouTube geeft de bron van views niet openbaar).
8. **21 talen en pagina's per overstapper.** De plugin en de site zijn er in 21 talen (GEZIEN). De site heeft aparte pagina's voor wie wegkomt van Apple Notes, Bear, Evernote, OneNote en Day One, bijvoorbeeld "The Apple Notes alternative, for people who want more" met de stappen om over te stappen (GEZIEN). Wanneer die pagina's kwamen en hoeveel bezoek ze brengen, weet ik niet.
9. **Gratis, met fooien.** GPL-3.0, gratis, met Buy Me a Coffee (546 supporters) en GitHub Sponsors (GEZIEN). Geen betaalde versie.

### Drie lessen
1. **Noem de app die mensen missen, in de eerste zin.** Zijn Reddit-titel was geen productnaam maar een gemis: "I missed Apple Notes, so I created it". Daarna zegt alles hetzelfde: "Apple Notes, Bear & Evernote for Obsidian", een pagina per app waar mensen vandaan komen, en met naam de verlaten concurrent. Wie die app kent, snapt in één regel wat het doet. Dit past bij de regel in `regels.md` dat de belofte meteen duidelijk moet zijn.
2. **Zet de uitlegvideo in het product zelf.** De twee lange masterclasses haalden elk bijna 40 keer zoveel views als zijn kanaal abonnees heeft, de korte filmpjes maar een fractie (GEZIEN). De plugin toont de video bij de eerste start en een filmpje bij elke update. Zo hoeft de video niet gevonden te worden in een feed; hij wordt bekeken door wie het net installeerde. Dit is het derde verhaal (na VibeDesk en Blender Secrets) waarin uitleg die een vraag beantwoordt meer doet dan reclame.
3. **Een Reddit-post vóór de lancering werkt als wachtlijst, als het product er daarna snel en vaak bij komt.** Mensen keken 50 dagen in de winkel. Daarna hield hij de aandacht vast met tientallen versies en meldingen in dezelfde draad. Let op: het bewijs voor de Reddit-post is één citaat; de kracht ervan (stemmen, bezoekers) kon ik niet meten.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij werkte ruim duizend uur aan één product met tientallen jaren ervaring (Apple, EA, Google volgens zijn site, EIGEN OPGAVE). Het product is echt goed; de kanalen versterkten dat, ze maakten het niet.
- Een bestandslijst gebruik je elke dag; een kleine tool zoals Click Joints of Ebb gebruik je minder vaak. Het welkomstscherm werkt pas als er installaties zijn.
- Het is gratis. Over geld leert dit verhaal alleen dat fooien bij ±70.000 gebruikers 546 supporters gaven (bedragen onbekend). Dat past bij hoofdles 5 in `lessen.md`: het betaalde deel haalt een klein deel van het gratis publiek.
- Een dagelijkse plugin met veel versies krijgt veel update-downloads; vergelijk zijn 1,15 miljoen dus niet met de 41 van Rollwright.

### Voorstel voor Dortus deze week
**Bram: zet in Click Joints Pro (de betaalde versie op Superhive) bij de eerste start een klein welkomstvenster of een knop "Getting started" met de link naar één uitlegvideo van 1 tot 3 minuten. Chris maakt die video (echte Blender-beelden, een gewricht van begin tot print), en zet hem ook bovenaan de Superhive-pagina.** Waarom: wie Pro koopt, moet in de eerste minuut slagen; de video wordt dan bekeken door de mensen die hem nodig hebben, en het kost één venster. De regels van extensions.blender.org (geen reclame voor betaald in de gratis versie) gelden voor de gratis listing; voor Pro op Superhive niet, maar zet in de gratis versie niets. Voor de lanceerberichten van Click Joints en Ebb: Chris schrijft de eerste regel als gemis ("I wanted X in Blender, so I made it"), niet als productnaam; Thijs plaatst. Meten: views van die ene video tegen het aantal verkochte Pro-licenties.

---

## 4. Blender Secrets (Jan van den Hemel, solo, Gent): elke dag een Blender-tip van een minuut zonder gezicht, en een e-book van $52 met 15.000+ verkopen

Onderzocht 16 nov 2026, run 4. Open vraag uit run 3: een Blender- of printmaker die groeide met tips-filmpjes, niet met productfilmpjes. Waarom dit verhaal: dit is het tegenvoorbeeld van mijn les uit verhaal 3 ("een echt persoon is de haak"). Jan van den Hemel maakt sinds aug 2018 bijna elke dag een schermopname van één Blender-handeling, zonder gezicht, met een nummer erbij ("Daily Blender Tip #1"). Daarmee bouwde hij een kanaal van 292.000 abonnees en verkoopt hij de verzamelde tips als e-book. Hij werd er fulltime maker door.

### Bronnen
- Interview met hem (Subkit / Collabs.io Mag, ±2022, curl): https://gosolo.subkit.com/blender-secrets
- Gumroad, productpagina met verkoopteller in de pagina (`sales_count`, curl): https://blendersecrets.gumroad.com/l/IxofeY
- Superhive, productpagina met "Sales 2000+" (curl): https://superhivemarket.com/products/blender-secrets
- YouTube-kanaal @blendersecrets (tellers op de pagina, curl) en de volledige lijst van alle 1.016 uploads met views en lengte (yt-dlp, alleen de openbare lijst, `--flat-playlist`): https://www.youtube.com/@blendersecrets
- BlenderNation: zijn auteurspagina's met elke dagtip als bericht, en datums (curl): https://www.blendernation.com/author/jan-van-den-hemel/page/50/ (tip 145 op 22 jan 2019), page/45 (tip 210 op 30 mrt 2019). Eerste e-book, 30 mrt 2019: https://www.blendernation.com/2019/03/30/100-amazing-blender-tips-vol-1-e-book/ . Update okt 2020: https://www.blendernation.com/2020/10/04/blender-secrets-e-book-update-promoted/ . 2000 pagina's, jul 2024: https://www.blendernation.com/2024/07/02/blender-secrets-e-book-now-2000-pages-promoted/
- TikTok @blendersecrets (blok in de pagina, curl) en Bluesky (openbare API).
- Niet gelukt: zijn eigen site blendersecrets.org en 3dsecrets.com (Cloudflare blokkeert curl), archive.org (geen antwoord), Instagram (inloggen gevraagd), uploaddatum per YouTube-filmpje (YouTube vraagt inloggen). Datums haal ik dus uit BlenderNation, niet uit YouTube.

### Cijfers
- YouTube (GEZIEN 16 nov 2026): 292.000 abonnees, 35,2 miljoen views, 1.016 openbare uploads. TikTok: 11.800 volgers, 111 filmpjes, 100.700 likes. Bluesky: 4.033 volgers. Instagram is volgens hemzelf zijn startkanaal, maar de teller kon ik niet lezen.
- E-book "Blender Secrets", $52 (GEZIEN): op Gumroad **13.408 verkopen** en 1.751 beoordelingen (97% vijf sterren); op Superhive "2000+" verkopen en 25 beoordelingen, gepubliceerd "over 7 years ago". Samen dus minstens ±15.400 verkopen.
- Omzet: niet openbaar. GOK, grof: de prijs was vroeger lager (hij begon met 335 pagina's), en de Gumroad-teller telt kortingen mee. Bij gemiddeld $20 tot $35 per verkoop is dat ±$300.000 tot ±$540.000 bruto in ruim 7,5 jaar, vóór afdrachten. Dat hij zijn freelancewerk kon stoppen "since the e-book took off" (EIGEN OPGAVE, interview) past daarbij.
- Datums (GEZIEN op BlenderNation, één bericht per dagtip): tip 145 op 22 jan 2019, tip 210 op 30 mrt 2019, tip 246 op 5 mei 2019, tip 286 op 14 jun 2019. Dat is echt elke dag één, dus tip 1 viel rond eind aug 2018.
- Views per deel van de reeks (GEZIEN, views van nu, dus opgeteld over alle jaren; oude filmpjes hadden langer de tijd):

| Filmpjes | Mediaan views | Mediaan lengte |
|---|---|---|
| 1 tot 30 | 4.500 | 32 sec |
| 31 tot 100 | 2.350 | 95 sec |
| 101 tot 300 | 6.000 | 56 sec |
| 301 tot 600 | 17.500 | 52 sec |
| 601 tot 800 | 44.000 | 62 sec |
| 801 tot 1016 | 20.000 | 66 sec |

- Zijn eerste 30 filmpjes (GEZIEN): allemaal "Daily Blender Tip #n" met één handeling in de titel: "Select Connected Faces" (7 sec), "Hide Everything Except Selected" (5 sec), "Copy Animation From One Object To Another" (9 sec, nu 29.000 views), "Inset Individual Faces" (6 sec, nu 48.000, de beste van de 30). De kortste (5 tot 9 sec) doen het in de eerste 30 het best; vanaf tip 8 worden ze 20 tot 60 sec.
- Best bekeken ooit (GEZIEN): "The easiest modeling technique?" 560.000 (47 sec), "Hand Topology Animation" 397.000, "Texturing a face" 362.000, "Turn vertices into Holes" 328.000. Allemaal een tip, geen reclame.
- Zijn reclamefilmpjes (cursussen, e-book, uitverkoop, 7 stuks) hebben een mediaan van 10.000 views, tegen 16.000 voor het hele kanaal.

### Wat hij deed, in volgorde
1. **Een gat gezien dat hij zelf voelde.** "The tutorials on YouTube were all overly long, and it took me forever to find the info I really needed. So I started making those one-minute tutorials as it seemed nobody else was doing it" (interview). Hij was toen freelance motion designer en deed het "for fun in my spare time".
2. **Aug 2018: elke dag één tip, met nummer.** Schermopname, geen gezicht, geen stem nodig, één handeling per filmpje. Elke tip ging naar Instagram, YouTube, Twitter en als los bericht naar BlenderNation, de grote nieuwssite voor Blender waar iedereen berichten kan insturen. Zo stond hij elke dag op de voorpagina van de plek waar Blender-gebruikers nieuws lezen.
3. **Mrt 2019, na ±210 tips: het eerste e-book.** "100 Amazing Blender Tips: Vol. 1", 335 pagina's, op Gumroad, met de belofte "receive Volume 2 for free when it comes out". Het boek is de tips op papier, met extra stappen die niet in het filmpje pasten, en elk hoofdstuk linkt naar zijn filmpje. Zelf zegt hij: "I spent about a year doing daily videos on Instagram before I started using it to advertise my e-book."
4. **Vroeg verkopen, daarna laten groeien.** "Don't hide behind perfection. Get it out there and start selling it as soon as possible. I started selling my e-book when it was just a couple hundred pages." Updates gratis voor kopers; kopers stuurden wensen (okt 2020: één groot PDF en ordening per thema, "as per popular request"). Nu 2000+ pagina's en 600+ onderwerpen.
5. **Twee winkels, plus betaalde berichten.** Gumroad en Blender Market (nu Superhive). Bij grote updates een "promoted" (betaald) bericht op BlenderNation (okt 2020, jul 2024). Later cursussen op een eigen site (3DSecrets) en samenwerking met CG Boost.
6. **Gewoon doorgaan.** 1.016 uploads in ruim 7 jaar. De views per filmpje kwamen pas na honderden filmpjes op een hoger niveau (mediaan 2.350 bij 31 tot 100, 44.000 bij 601 tot 800).

### Drie lessen
1. **Gezichtloos kan wel, als elk filmpje iemand tijd bespaart.** Dit is de grootste gezichtloze groei in onze reeks: 292.000 abonnees met schermopnames zonder persoon. Het verschil met VibeDesk (verhaal 2, ook gezichtloos, bleef op 39 tot 363 views) zit niet in het gezicht maar in het onderwerp: VibeDesk liet zijn eigen product zien, Jan beantwoordt een vraag die elke Blender-gebruiker heeft. Dat bevestigt les 1 uit verhaal 3 en zwakt les 2 af: de haak is nut, een gezicht is een plus, geen eis.
2. **Het product is de verzameling van de gratis filmpjes, plus wat er niet in paste.** Kijkers kregen elke dag gratis een tip; wie alles bij elkaar wil, met extra stappen en zoekbaar, betaalt $52. Zijn reclamefilmpjes doen het slechter dan zijn tips (mediaan 10.000 tegen 16.000), dus de verkoop loopt via de naam en de link, niet via reclame in de feed.
3. **Elke dag, met een nummer, en op meer plekken tegelijk, jarenlang.** Zijn eerste 30 filmpjes hebben nu nog maar een mediaan van 4.500 views, na 8 jaar. De groei kwam na honderden tips. Elke tip ging ook als bericht naar BlenderNation, een gratis plek waar zijn kopers al kwamen. En hij verkocht al na ±7 maanden, met een half boek.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij begon in 2018, vlak voor Blender 2.8 (2019), toen heel veel nieuwe gebruikers instroomden en er nog bijna geen korte Blender-tips waren. Nu zijn er veel meer. Dat speelt mee, en is niet te meten.
- Hij is een ervaren Blender-professional die zelf elke dag iets nieuws leert en laat zien. Onze tips moeten echt kloppen; Bram en Chris moeten elke tip zelf in Blender nadoen voor hij uitgaat.
- Zijn product is kennis (een boek), het onze is gereedschap (een add-on). Bij hem is de stap van filmpje naar product heel klein. Bij ons moet de tip vanzelf naar Click Joints leiden, dus tips over print-in-place en gewrichten, niet over alles in Blender.
- Views van nu zeggen weinig over views in de eerste weken. Hoe zijn kanaal er in 2018 en 2019 uitzag, kon ik niet zien (archive.org gaf geen antwoord). Verkoopcijfers per jaar zijn niet openbaar.
- Plaatsen op BlenderNation of andere sites doen wij niet zelf: dat is plaatsen op internet, dus dat doet Thijs. BlenderNation plaatst nog steeds tutorials van gebruikers (GEZIEN: in de rubriek Tutorials 8 nieuwe tussen 31 okt en 15 nov 2026, en Jan zelf nog op 20 jan en 3 mrt 2026), maar de regels voor insturen kon ik niet lezen: de pagina Submit News toont zonder JavaScript geen tekst. Thijs leest die dus eerst zelf.

### Voorstel voor Dortus deze week
**Maak van de tips-reeks voor Click Joints een genummerde reeks van één handeling per filmpje, zo kort als het kan (de eerste 10 onder 15 seconden), en houd bij elke tip een korte tekst met plaatje bij op dortus.com/click-joints/ (een tipspagina).** Voorbeelden: "Print-in-place tip #1: waarom een gewricht vastsmelt (te weinig speling)", "#2: zet het gewricht plat op het bed", "#3: hoe test je eerst één gewricht". Die tipspagina wordt na 20 tot 30 tips een gratis gids, en later kan de Pro-versie of een gids in de winkel daar op voortbouwen, zoals zijn e-book. **Wie:** Chris maakt de reeks (tekst in beeld, geen gezicht nodig), Bram doet elke tip echt na in Blender en levert het beeld. **Voor Thijs, op `organisatie/lijst-thijs.md` via de hoofdchat, geen haast:** de tips ook als bericht insturen bij BlenderNation (gratis, één keer per week, alleen tips en geen reclame), want dat deed Jan bij elke tip. Na 30 tips eerlijk kijken naar views en downloads, zoals besloten.

---

## 3. VAW.BE (Wim Van Aerschot, solo, Garmin-wijzerplaten): elke dag een kort filmpje, en de nummer 1 van de winkel

Onderzocht 16 nov 2026, run 3. Open vraag uit run 1 en 2: een kleine maker van een tool of Garmin-app die WEL groeide met korte filmpjes. Waarom dit verhaal: dit is precies ons terrein. Een solo maker uit België verkoopt Garmin-wijzerplaten van $1,99 tot $4,99 (Ebb kost $4,99), maakt sinds februari 2025 korte filmpjes op TikTok, Instagram en YouTube, en zijn betaalde wijzerplaat Goals stond eind oktober 2026 bovenaan de wijzerplatenlijst van de Connect IQ Store. Hij schrijft bij elk filmpje een stuk op zijn eigen site ("Garmin School", nu dag 167), dus de onderwerpen van zijn reeks zijn van dag 1 af te lezen.

### Bronnen
- Zijn site: Garmin School, de lijst van alle 167 dagen met onderwerp en aantal keer gelezen (curl): https://garmin.vaw.be/en/community . Losse dagen: dag 1 Stride https://garmin.vaw.be/en/community/day-1-stride-watchface , dag 3 Goals https://garmin.vaw.be/en/community/day-3-goals-watchface-apple-rings-for-garmin , dag 5 Laziest https://garmin.vaw.be/en/community/day-5-laziest-watchface-ever-created , dag 101 Goals Pro https://garmin.vaw.be/en/community/day-101-goals-pro-garmin-watchface , over hem https://garmin.vaw.be/en/about
- De openbare winkel-API van Garmin (dezelfde die Gijs gebruikt, zie `platformen/garmin/status.md`): al zijn 142 apps met downloads (in blokken), aantal reviews, prijs; en de datum van reviews, om te zien wanneer de groei kwam.
- the5krunner, 2 nov 2026, Goals bovenaan de wijzerplatenlijst van oktober (geopend in een browser zonder inloggen, curl gaf een Cloudflare-scherm): https://the5krunner.com/2026/11/02/goals-tops-garmins-watch-face-chart-for-october
- Tom's Guide, 13 aug 2025, een vaste Garmin-tester raadt Goals aan (curl): https://www.tomsguide.com/wellness/fitness-trackers/if-youre-moving-from-apple-to-garmin-youll-want-to-install-this-watch-face
- Garmin-forum, zijn eigen bericht over Goals III, ruim 3 jaar geleden (curl): https://forums.garmin.com/developer/connect-iq/f/showcase/315890/watchface-goals-iii
- Zijn kanalen, alleen de tellers: TikTok https://www.tiktok.com/@vaw.be (blok `__UNIVERSAL_DATA_FOR_REHYDRATION__`), Instagram https://www.instagram.com/vawbe/ (meta-omschrijving), YouTube https://www.youtube.com/@vawbe/shorts (views per Short staan in de pagina). Vier omslagen van Shorts bekeken (i.ytimg.com).
- Niet gelukt: archive.org (verbinding viel weg), dus ik weet niet hoe zijn kanalen er in 2025 uitzagen. Zijn eigen TikTok- en Instagram-lijst met filmpjes en views is niet leesbaar zonder verborgen API, dus views per filmpje heb ik alleen van YouTube, en alleen van de nieuwste 48.

### Cijfers
Kanalen (GEZIEN 16 nov 2026):
- TikTok @vaw.be: aangemaakt 9 feb 2025, 29.500 volgers, 251.500 likes, 301 filmpjes. Dat is ±3,4 filmpjes per week, 21 maanden lang.
- Instagram @vawbe: 31.000 volgers, 369 berichten. Zijn site verwijst overal naar Instagram ("link in my bio"), dus dat is zijn hoofdkanaal.
- YouTube @vawbe: 2.350 abonnees. De nieuwste 48 Shorts: meestal 750 tot 2.500 views. Uitschieters zijn geen productfilmpjes maar nieuws en vergelijkingen: "Coros Pace 4 Pro vs Garmin Forerunner 570/970" 39.000, "This is Garmin's new Marq 3" 19.000, "Is the Garmin Connect app terrible or awesome?" 18.000, "Your Garmin knows when your body is struggling" 13.000. Zijn eigen wijzerplaten: "This is the new Cockpit watchface" 3.200, "This is the new Cadence watchface" 2.500, "This is the Photo Time watchface" 751.
- **Vorm: hij praat zelf in de camera**, met een microfoontje in de hand, ondertitels groot in beeld, één woord gekleurd, thuis voor een kast met planten. Geen gezichtloze schermopname.

Winkel (GEZIEN 16 nov 2026, openbare API; downloads geeft Garmin alleen in blokken als "100.000+"):
- 142 apps van VAW.BE, waarvan 48 betaald, samen 196.155 reviews.
- Goals: $1,99, 100.000+ downloads, **32.206 reviews**, 4,9 sterren. Eerste review 4 apr 2025, dus twee maanden na zijn eerste TikTok. Sindsdien elke dag ±30 tot ±100 reviews (met pieken rond kerst 2025, ±99 per dag, en in juli 2025, ±86 per dag), nu ±40 per dag.
- Goals Pro: $4,99, 10.000+ downloads, 903 reviews. Gratis "Seasons": 500.000+ downloads, 55.458 reviews (sinds dec 2023). "The Laziest Watchface Ever Created" (gratis, met AI-agents gebouwd): eerste review 6 feb 2026, nu 50.000+ downloads en 2.982 reviews.
- Daily Sea Creature, een betaalde wijzerplaat met zeedieren voor $4,99, net als Ebb: 100+ downloads, 40 reviews. Niet elk onderwerp loopt, ook niet bij hem.
- Werkwijze in de winkel: bijna elke betaalde wijzerplaat staat er twee of drie keer: betaald, "with trial" (gratis proberen), en "with trial & kpay" (betalen via een andere dienst). Goals betaald heeft 32.206 reviews, Goals "with trial" 8.423.

Groei voor en na de filmpjes (GEZIEN: reviewdata van zijn 12 apps met de meeste reviews, samen 167.789; ik telde per periode hoeveel reviews er bijkwamen):
- 16 nov 2024 tot 9 feb 2025 (voor zijn eerste TikTok): 9.020 reviews in 85 dagen, ±106 per dag (met kerst erin).
- 9 feb 2025 tot 16 nov 2025: 50.392 in 280 dagen, ±180 per dag.
- 16 nov 2025 tot 15 nov 2026: 74.991 in 364 dagen, ±206 per dag.
- Dus na de start van de filmpjes ±1,7 tot 2 keer zoveel reviews per dag. Maar: Goals kwam er in april 2025 bij, er komen elk jaar meer Garmin-horloges, en Tom's Guide schreef in aug 2025 over Goals. Hoeveel van de groei door de filmpjes komt, is met deze cijfers NIET te scheiden.
- Omzet: niet openbaar. GOK, heel grof: als de helft van de 100.000+ downloads van Goals betaald is, is dat ±$100.000 bruto vóór de afdracht aan Garmin, verspreid over 19 maanden. Dat de betaalde versie meer reviews heeft dan de proefversie, wijst erop dat veel mensen echt kopen, maar het blijft een gok.

### Wat hij deed, in volgorde
1. **Jaren eerst gewoon bouwen.** Op het Garmin-forum staat Goals III al "over 3 years ago"; Goals V heeft reviews sinds jan 2023, Seasons sinds dec 2023. In nov 2024 had hij al ±33.000 reviews in zijn top 12. De filmpjes kwamen dus bovenop een winkel die al liep.
2. **Feb 2025: TikTok, Instagram en YouTube, zijn eigen gezicht.** ±3 tot 4 filmpjes per week. In april 2025 kwam Goals ("Apple Watch rings, maar voor Garmin"): een idee dat hij uit reacties haalde ("This is the most common thing I hear from people who switch to Garmin").
3. **Kijkers laten meedoen.** Kijkers delen hun kleurencombinatie voor Goals in de reacties onder zijn Instagram-filmpjes, "the best ones get featured" (dag 3). Een openbaar ideeënbord: kijkers stemmen wat hij bouwt (dag 47, dag 53, dag 115), en hij maakt filmpjes over wijzerplaten die volgers vroegen ("One of my followers quit smoking...", "I created the Photo Time watchface based on Ward's idea", "Can I build your Garmin watchface?").
4. **Feb 2026: een vaste reeks, "100-Day Garmin School".** Dag 1: "I made this Garmin watchface because my doctor told me I was going to die." Elke dag een filmpje en een stuk op zijn site met een nieuwsbrief. Na dag 100 ging hij door (nu dag 167).
5. **De onderwerpen verschoven van eigen product naar vragen van alle Garmin-bezitters.** Dag 1 tot 5: alle vijf zijn eigen wijzerplaten (Stride, Daily Flowers, Goals, Hearts, Laziest). Dag 1 tot 30: ±9 van de 30 over zijn eigen apps, de rest tips (batterij, hartslagalarm, VO2max, "Why Garmin doesn't default to 10,000 steps"). Dag 31 tot 167: nog ±1 op 8 over eigen apps, de rest tips, vergelijkingen (Garmin tegen Apple Watch en Coros), nieuws (nieuwe horloges) en "Garmin met Claude". Op zijn site zijn de stukken over Claude en Garmin het meest gelezen (dag 43 vergelijkingstool 6.948 keer, dag 62 slaapscore met Claude 3.562, "Connect your Garmin to Claude" 3.189 en 3.118).
6. **Elk filmpje wijst naar één plek**: de link in zijn Instagram-bio, waar al zijn apps, een bundel ("save up to 90%") en de nieuwsbrief staan.

### Drie lessen
1. **Bouw het kanaal rond de vragen van de bezitters, niet rond je product.** Zijn best bekeken Shorts zijn vergelijkingen en nieuws (13.000 tot 39.000), zijn productfilmpjes halen 750 tot 3.200. Na de eerste vijf dagen ging nog maar 1 op de 3 en later 1 op de 8 filmpjes over zijn eigen apps. De tips brengen volgers; de wijzerplaten liften mee via de bio. Bij VibeDesk (verhaal 2) ging elk filmpje over het product, en dat bleef steken op 39 tot 363 views.
2. **Een echt persoon met een eigen verhaal is de haak.** Hij praat zelf, met een eerlijke reden ("my doctor told me I was going to die" bij Stride, "I always forget Valentine's Day" bij Hearts). Dit is het eerste verhaal in onze reeks met tienduizenden volgers via eigen korte filmpjes, en het is geen gezichtloos kanaal. Twee verhalen is weinig, maar het past: gezichtloos en alleen product (VibeDesk) bleef plat, gezicht en tips (VAW.BE) groeide. GOK: voor Garmin en Blender geldt hetzelfde.
3. **Lang volhouden en kijkers laten kiezen.** 301 filmpjes in 21 maanden, en de groei in reviews kwam geleidelijk (±106 naar ±206 per dag), niet in één klap. Wat er wel in één klap kwam, waren ideeën die hij uit de reacties haalde: Goals (ringen zoals Apple) werd zijn grootste betaalde product. Het ideeënbord en "jouw kleuren worden uitgelicht" maken van kijkers meedenkers.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij had al jaren een lopende winkel (±33.000 reviews vóór zijn eerste filmpje) en 100+ apps. Wij hebben Ebb met 0 downloads. Zijn filmpjes konden naar een hele etalage wijzen; de onze naar één of twee producten.
- Hij is een echte Garmin-gebruiker die test en zelf praat. Wij mogen geen AI-gezicht of nep-persoon gebruiken (besluit 15 nov 22:53), en terecht. Zijn vorm is dus alleen na te doen als Thijs zelf in beeld wil, of met een eigen stem zonder gezicht. Dat beslist Thijs, niet wij.
- Wat de filmpjes precies opleverden, kan ik niet scheiden van Goals, Tom's Guide en de groei van Garmin zelf. Zijn eigen "top 5 wijzerplaten van 2026" (dag 79) zet twee van zijn eigen apps erin (Laziest op 2, Titan op 4); dat is reclame, geen onafhankelijke lijst.
- Zijn eerste 30 filmpjes op TikTok (feb tot ±apr 2025) heb ik niet kunnen zien. Wat ik heb, zijn de eerste 30 dagen van zijn tweede start, de Garmin School van feb 2026.

### Voorstel voor Dortus deze week
**Draai de verhouding in het filmplan om: 4 van de 5 filmpjes beantwoorden een vraag die elke Blender-gebruiker (of Garmin-bezitter) heeft, 1 van de 5 laat ons product zien, en geef de reeks een vaste naam met een dagnummer.** Voor Click Joints bijvoorbeeld "Print-in-place in Blender, day 1": hoeveel speling een gewricht nodig heeft, waarom een print vastsmelt, welke laaghoogte, hoe je een figuur zo zet dat hij zonder steun print. Click Joints komt dan vanzelf in beeld als het gereedschap, en het onderschrift wijst naar dortus.com/click-joints/. Voor Ebb later hetzelfde met korte Garmin-tips (ademhaling, Body Battery, stress), zonder gezondheidsclaims. **Wie:** Chris schrijft de 10 eerste onderwerpen in `commercie/filmpjes/` en maakt ze met de opnames van Bram; Bram levert per tip een kort, echt Blender-beeld. **Eén vraag voor de hoofdchat aan Thijs** (geen haast, past in de groeironde): wil hij af en toe zelf 20 seconden praten (gezicht, of alleen zijn stem over de beelden)? Dit verhaal is het enige in onze reeks waarin korte filmpjes echt volgers gaven, en daar praat de maker zelf. Zegt hij nee, dan gaan we gezichtloos verder met de tips-verhouding, en kijken we na 20 tot 30 filmpjes eerlijk naar views en downloads, zoals besloten.

---

## 2. VibeDesk (Fred, solo, gratis Windows-app voor Claude Code): 20 Shorts zonder gezicht, met cijfers

Onderzocht 16 nov 2026, run 2. Open vraag uit run 1: wat deed een maker in zijn eerste 30 filmpjes, met kijkcijfers per filmpje? Waarom dit verhaal: een solo maker die precies doet wat Chris vanaf di 17 nov gaat doen (staande schermopnames, tekst in beeld, geen gezicht, geen stem) en zijn echte cijfers uit YouTube Studio en GitHub openbaar zet. Hij bouwt ook met Claude Code, net als wij. Het is geen succesverhaal maar een eerlijke mislukking, en daarom juist bruikbaar: zo ziet de start eruit als het niet vanzelf gaat.

### Bronnen
- Zijn eigen verslag op DEV, 3 nov 2026 (curl via de openbare API van DEV): https://dev.to/fxdgif/15-youtube-shorts-2674-views-1-subscriber-promoting-a-dev-tool-without-showing-my-face-2m8j
- Zijn eerste bericht over de app, 22 okt 2026, met 17 reacties (curl, API van DEV): https://dev.to/fxdgif/i-kept-missing-claude-codes-permission-prompts-so-i-built-a-desktop-around-it-8fc
- Zijn kanaal, tab Shorts en tab Video's (curl, de cijfers staan in de pagina zelf): https://www.youtube.com/@vibedesk-lounge/shorts
- De repo, sterren via de zoek-API van GitHub (gh api search): https://github.com/fxd-gif/vibedesk
- Ter vergelijking: de zoekpagina van YouTube voor "print in place joints blender" en "articulated print in place blender tutorial" (curl, 16 nov).
- Niet gelukt: de GitHub-pagina zelf (403 vanuit de cloud) en de afspeelpagina van YouTube (429). Kijkduur per filmpje en precieze plaatsingsdata heb ik dus alleen uit zijn eigen verslag.

### Cijfers
Uit zijn verslag (EIGEN OPGAVE, uit YouTube Studio, laatste 28 dagen tot 3 nov):
- 15 Shorts in twee weken: samen 2.674 views, 32 likes, **1 abonnee** uit Shorts.
- 70% veegde vrijwel meteen weg. Snelle, flitsende filmpjes: 19% tot 25% bleef kijken. Het beste filmpje (26 seconden, "sort my windows" typen en het zien gebeuren, geen effecten): 42% bleef.
- Elke Short kwam tussen 50 en 370 views. YouTube Studio zegt zelf: "usually get 140 to 220". 81% van de views kwam uit de Shorts-feed.
- GitHub: 21 unieke bezoekers in 14 dagen, waarvan 5 via YouTube. 0 sterren.
- Eén langer filmpje van 1:15 (gewone video, geen Short): 332 views, gemiddeld 51% bekeken, 80% van de views via de startpagina van YouTube, ook 1 abonnee.
- Eén eerlijk bericht op DEV ("I kept missing...") gaf 15 reacties en twee wensen die hij in de volgende versie bouwde.

Zelf nagekeken (GEZIEN 16 nov 2026):
- Kanaal: 20 Shorts en 2 gewone video's, 136 abonnees. Views per Short, nieuwste eerst: 97, 53, 39, 153, 84, 79, 55, 215, 151, 134, 363, 157, 196, 194, 284, 201, 245, 274, 72, 54. Samen 3.100. Hoogste 363 ("How much Claude Code did this project use today?"), laagste 39.
- De 7 Shorts van na zijn verslag halen samen 560 views (gemiddeld 80), lager dan de 13 oudere (gemiddeld ±195). Of dat komt door minder vaak plaatsen of door het onderwerp, weet ik niet.
- De gewone video's: "I vibecoded the Claude Code workspace I wished I had, in 12 days" 370 views; "VibeDesk in 5 minutes" 81 views.
- Repo: 0 sterren, 1 fork, aangemaakt 11 okt 2026.
- DEV: het eerste bericht heeft nu 17 reacties; zijn negen berichten daarna hebben 0 tot 2 reacties elk.
- Klopt niet helemaal: hij schrijft "+1 subscriber from Shorts", het kanaal heeft er nu 136. Waar de rest vandaan komt staat er niet; GOK: via zijn DEV-berichten en de link op zijn site, of later erbij gekomen.

Ter vergelijking, YouTube-zoekpagina (GEZIEN 16 nov): lange uitlegvideo's over beweegbare prints in Blender halen 38.000 tot 143.000 views ("Articulated Dragon 3d print // Blender tutorial" 142.783, "How To Design Articulating 3D Prints! Blender Tutorial!" 48.548, "How to Make Your Own Flexi STL Files (Free FlexiMaker Tutorial Using Blender)" 38.163). Maar twee nieuwe kleine kanalen met dezelfde soort uitleg halen 38 en 270 views. Lang is dus geen garantie, wel een kamer waar mensen met de vraag zitten.

### Wat hij deed, in volgorde
1. **Eerst een eerlijk bericht** op DEV met het probleem in één zin ("I kept missing Claude Code's permission prompts") en een filmpje erin. Reacties van mensen met hetzelfde probleem; hij antwoordde iedereen uitgebreid, opende issues voor hun wensen en bouwde ze in versie 2.0.
2. **Daarna 15 Shorts in twee weken**: eerst snel en flitsend, toen rustig met één idee per filmpje en een grote uitsnede van de app. Het aantal views veranderde niet.
3. **Opgeschreven en bijgestuurd**: hoogstens twee Shorts per week, langere rustige video's die iets beantwoorden waar mensen op zoeken, meer eerlijke berichten, en een kortere weg naar de download (de installer is niet ondertekend, dus Windows waarschuwt).
4. Daarna nog 5 Shorts; die deden het slechter.

### Drie lessen
1. **Bij een nichetool zonder gezicht bepaalt het filmpje de views nauwelijks.** Snel, traag, grappig of technisch: alles landde tussen 50 en 370. De feed laat een kleine testgroep kijken; vegen ze weg, dan stopt het. Wat wel verschil gaf in hoe lang mensen bleven: **één duidelijke handeling die je zelf zou willen** ("sort my windows", 42%), geen effecten. Dat sluit aan op McGybeer (verhaal 1): het product dat het werk doet in beeld, niet de knoppen.
2. **De Shorts-feed is een kamer vol mensen zonder jouw probleem.** Uit 3.000 views kwamen 5 bezoekers op de repo. In een Short kun je niet klikken. Een gewone, langere video kwam via de startpagina bij mensen die zulke video's kijken, en een eerlijk bericht kwam bij mensen met het probleem; die gaven allebei meer dan alle Shorts samen.
3. **Meet tot aan de download, niet tot aan de view.** Zijn eigen conclusie: uren in montage, bijna niets in de weg na de klik (releasepagina, .exe, waarschuwing van Windows). Views zonder downloads zeggen niets.

### Eerlijk: wat niet zomaar voor ons geldt
- Eén kanaal, één tool, vier weken, alleen YouTube. Geen TikTok en geen Reels. Op TikTok is het bereik voor nieuwe accounts mogelijk anders (GOK, niet gemeten).
- Zijn publiek (Windows-gebruikers van Claude Code) is kleiner en zijn drempel hoger (onondertekende .exe) dan bij Click Joints, dat je in Blender met één klik installeert van extensions.blender.org. Ons beeld (een figuur die buigt) is ook makkelijker te begrijpen dan een bureaublad met terminals. Onze Shorts kunnen dus beter doen (GOK).
- Hij schrijft zelf: "Maybe my hooks were just bad." Het kan aan zijn filmpjes liggen.
- Verwachting voor Chris, als GOK op basis van dit verhaal: de eerste Shorts halen 50 tot 400 views per stuk en leveren een handvol downloads. Dat is normaal en geen reden om na een week te stoppen; het besluit van 15 nov kijkt terecht pas na 20 tot 30 filmpjes.

### Voorstel voor Dortus deze week
**Naast de dagelijkse Shorts één gewone liggende YouTube-video (60 tot 120 seconden) die een zoekvraag beantwoordt**, titel in de vorm "How to make print-in-place joints in Blender (free add-on)": één figuur van begin tot geprint resultaat, rustig, tekst in beeld, geen gezicht, geen stem. Bij VibeDesk haalde zo'n video evenveel abonnees als alle Shorts samen en kwam hij via de startpagina bij het juiste publiek; in onze niche halen zulke uitlegvideo's bij gevestigde kanalen tienduizenden views. Kost weinig: Bram heeft de filmpijplijn al en de bestaande winkelplaatjes zijn liggend (1920 x 1080); of de film zelf liggend is, heb ik niet nagekeken. **Wie:** Chris maakt hem in week 1 of 2, Bram levert liggende opnames als die ontbreken, Thijs plaatst. **En meten:** Chris zet in zijn dagmeting per filmpje de views naast de downloads van Click Joints op extensions.blender.org (dagteller), zodat we na 20 tot 30 filmpjes zien of views downloads worden, niet alleen of de views stijgen.

---

## 1. McGybeer (Javier Rodríguez, solo, beweegbare 3D-print-figuren)

Onderzocht 15 nov 2026, run 1. Vraag van de hoofdchat: hoe groeiden kleine makers met korte filmpjes zonder gezicht? Waarom dit verhaal: dit is precies de hoek van Click Joints (beweegbare figuren die je in één keer print, ontworpen in Blender), en het is het bekendste voorbeeld van een 3D-ontwerp dat via TikTok groot werd.

### Bronnen
- Interview Snapmaker, 24 feb 2022 (curl): https://www.snapmaker.com/blog/3d-printed-articulated-dragon-model-designer-javier-rodriguez/
- Artikel 3DWithUs over beweegbare draken, 27 apr 2022, bijgewerkt 5 nov 2023 (curl): https://3dwithus.com/articulated-dragon-models-flexible-print-in-place-for-3d-printing
- Productpagina en profiel op Thangs (curl, cijfers uit de pagina zelf): https://thangs.com/designer/McGybeer/3d-model/Articulated%20Dragon-863344
- Zijn TikTok-profiel (curl, alleen de tellers bovenaan): https://www.tiktok.com/@mcgybeer
- Niet te lezen vanuit de cloud: Cults3D, Printables, Thingiverse, Patreon (403), 3dprint.com (Cloudflare), zijn eigen site mcgybeer.xyz (onbereikbaar). De lijst met zijn eigen TikTok-filmpjes heb ik niet kunnen ophalen: dat gaat alleen via een verborgen API of een browser die de pagina naspeelt, en dat doen we niet. Wat hij in zijn eerste 30 filmpjes deed, weet ik dus NIET.

### Cijfers
- Zijn eerste bekende ontwerp: Cute Mini Octopus (2019), gemaakt voor zijn roller-derbyteam (DERDEN, Snapmaker).
- De Articulated Dragon: "40K paid downloads" met "thousands of physical models sold across Etsy, eBay, Amazon" (DERDEN, 3DWithUs, stand ±2022 tot 2023, niet nagekeken).
- Eén filmpje van Snapmaker over de draak op Facebook (dec 2021): 15 miljoen views en 8.600 reacties, "the most popular case in the Snapmaker community ever" (DERDEN, Snapmaker).
- TikTok-account @mcgybeer aangemaakt op 17 dec 2020 (GEZIEN, tijdstip in de pagina). Nu: 43.263 volgers, 336.225 likes, 187 filmpjes (GEZIEN 15 nov 2026). Gemiddeld ±1.800 likes per filmpje (GOK, gewoon gedeeld).
- Thangs (GEZIEN 15 nov 2026): draak los $3,99, 396 downloads, 208.019 keer bekeken, 493 likes; profiel 70 modellen, 29.491 downloads, 3.536 volgers. Leden: $10 per maand (4 ontwerpen), $18 (8 ontwerpen), en drie **verkooplicenties**: $10, $18 en $60 per maand (de laatste met alles, onbeperkt).
- Omzet: niet openbaar. GOK: 40.000 x ±$4 tot $8 is $160k tot $320k bruto alleen voor de draak, maar de prijs per winkel en het aandeel dat via leden liep weet ik niet.

### Wat er gebeurde, in volgorde
1. **Eerst het mechaniek, dan het dier.** Hij wilde de draak al een jaar eerder maken, maar "my design skills were still not enough". Hij ontwierp eerst een nieuw soort gewricht, maakte "a bunch of prototypes", testte en paste aan, en pas daarna modelleerde hij de draak in Blender. Gewrichten eerst, "as they are the key and the rest of the model depends on them".
2. **Het ontwerp verspreidde zich via filmpjes van anderen.** "Its popularity grew mainly on TikTok and I didn't have an account back then." Printerbezitters en een printermerk (Snapmaker) filmden de draak die in de hand kronkelt; dat deed het werk. Zijn eigen account kwam pas daarna (dec 2020).
3. **Hij maakte er werk van verkopers.** Mensen die de draak printen en verkopen (Etsy, eBay, Amazon, markten) kopen een verkooplicentie. Elke verkoper die zijn print filmt om hem te verkopen, maakt zo reclame voor het ontwerp.
4. **Daarna een reeks in dezelfde vorm.** Cali-Dragon, hagedis, haai, ratelslang: steeds een beweegbaar dier dat je zonder steun print. Na de draak werd hij voltijds ontwerper, omdat hij "2-3 hours per day just responding to emails, messages, posts" kwijt was.

### Drie lessen
1. **Het filmpje dat werkt is het product dat beweegt in een hand, niet uitleg.** Het groeimoment kwam niet van zijn eigen filmpjes maar van anderen die het resultaat lieten kronkelen. Voor een product als Click Joints is het sterkste beeld dus de geprinte figuur die buigt, niet het Blender-paneel.
2. **Laat anderen filmen: geef ze een reden.** Een printermerk wil indrukwekkende prints laten zien, een verkoper wil zijn waar verkopen, een hobbyist wil laten zien wat hij maakte. McGybeer verdient aan die groep met een verkooplicentie. Voor ons: makers die met Click Joints iets printen, zijn het kanaal, niet ons eigen account alleen.
3. **Eerst een nieuw mechaniek dat je in één beeld ziet.** De draak was "the first highly detailed articulated design" (volgens hemzelf); het verschil was in twee seconden te zien. Een filmpje zonder gezicht werkt als het onderwerp zelf de haak is.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij verkoopt **printbestanden** (iedereen kan het eindresultaat begrijpen). Wij verkopen een **Blender-add-on**: het publiek dat het eindresultaat leuk vindt is veel groter dan het publiek dat de add-on kan gebruiken. Een viraal filmpje van een kronkelende figuur levert ons dus minder kopers op dan hem (GOK).
- Het is één uitschieter uit 2020 tot 2021, toen beweegbare draken nieuw waren. Nu zijn er "lots of similar Dragon variations around"; het moment is voorbij.
- Over zijn eigen eerste 30 filmpjes heb ik niets kunnen vinden. Dat deel van de vraag blijft open.

### Voorstel voor Dortus deze week
**Een filmpje van een echt geprinte Click Joints-figuur die in een hand buigt** (8 tot 12 seconden, eerste seconde al bewegen, geen gezicht), als filmpje 6 in de reeks van Chris, en vanaf de lancering van Pro bij elke nieuwe figuur. Wie: Chris, met de print die al op de lijst van Thijs staat (echte print van een gewricht, alleen als hij of iemand die hij kent een printer heeft). Is er geen printer, dan vraagt Chris bij de lancering op r/3Dprinting of iemand een print wil laten zien, met credits (Thijs plaatst). Tot er een echte print is: Bram rendert een "hand"-beeld waarin de figuur buigt, eerlijk vermeld als render. En op de Pro-pagina een regel "Made something with Click Joints? Tag us, we share the best ones", zodat makers een reden hebben om zelf te filmen.

### Voor de ploeg: wat ik leerde over meten
Het openbare TikTok-profiel geeft met curl wel de tellers (volgers, likes, aantal filmpjes, aanmaakdatum) in het blok `__UNIVERSAL_DATA_FOR_REHYDRATION__`, maar niet de lijst met filmpjes. Handig om na de start van onze accounts elke dag volgers en likes te meten.
