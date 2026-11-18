# A: gevonden worden in de winkel zelf (agent A, 18 nov 2026)

Opdracht: hoe bepalen extensions.blender.org, Superhive, Gumroad Discover, de JetBrains Marketplace, de Garmin-winkel en Steam wat bovenaan staat, waar staan wij nu, en wat verbetert onze plek het meest (en wat kan vanzelf).

Alle metingen 18 nov 2026 tussen ±18:45 en 19:40 UTC, met curl op openbare API's en pagina's, niet ingelogd. Labels: **GEZIEN** (zelf gemeten of in broncode of officiële uitleg gelezen), **DERDEN** (iemand anders zegt het, met link), **GOK**.

**Al bekend (niet overgedaan):** hoofdles 18 in `platformen/succes/lessen.md` (in Blender zoekt Get Extensions alleen in naam en tagline, volgorde mediaan sterren; Garmin geeft 14 dagen "nieuw"; Steam zet in een themafest spellen met korting bovenaan); verhaal 25 (een Garmin-update geeft geen sprong); `platformen/garmin/gebruikers-krijgen-2026-11-13.md` (Garmin-lijsten, 20 tot 25 reviews voor Trending en Hot & Fresh); de Steam-tags in `platformen/steam/marketing/winkeltekst.md`; de IDE-aanraadlijst per bestandssoort in `platformen/jetbrains/marktmeting-2026-11-06.md`. Hieronder alleen wat nieuw is of nu nagemeten.

---

## Kort: de 3 dingen per winkel

| Winkel | 1 | 2 | 3 | Wat vanzelf kan |
|---|---|---|---|---|
| Blender (Click Joints Free) | tagline met "3D printing" erin (dekt print, printing, 3d print) | één eerlijke review van 5 sterren | lange omschrijving met de zoekwoorden die de site gebruikt | niets via updates: Blender sorteert niet op bijgewerkt |
| Superhive (Pro) | titel met de zoekwoorden (Superhive weegt de titel zwaar) | coupon en sitebrede actie: eigen rijen op de voorpagina | "Upgrade Variant": Free als Lite op Superhive, Pro als upgrade | elke nieuwe versie komt in "For You" bij kopers en verlanglijsten |
| Gumroad | eerst $100 echte verkoop (anders sta je nergens in Discover) | categorie, tags en ratings aan (tags staan al goed) | naam met "Blender add-on" en het werkwoord, zoals CatPin en Cleave | niets tot de $100 |
| JetBrains (Bison & Flex) | in de aanraadlijst voor `*.y` en `*.l` komen (nu niet!) | omschrijving uitbreiden (kan zonder nieuwe versie) | eerste reviews | elke update: ±1 uur in "New and Updated" in de IDE |
| Garmin | eerste 10 tot 25 echte reviews in de 14 dagen "nieuw" | korte naam met het zoekwoord vooraan | meer horloges vóór dag 14 | update zet ons op 1 bij "Most Recent", maar dat geeft geen downloads |
| Steam (Hats) | verlanglijsten vóór de lancering (Popular Upcoming) | korting in het fest (plek, niet percentage) | talen en tags | "Major Update"-event: alleen voor bezitters en verlanglijsten |

---

## 1. extensions.blender.org (Click Joints Free)

### Hoe de winkel rangschikt (GEZIEN, broncode `infrastructure/extensions-website`, bestanden `extensions/views/public.py`, `extensions/models.py`, `ratings/utils.py`, gelezen 18 nov)
- **In Blender (Get Extensions):** de lijst komt uit de API in de standaardvolgorde van het model: `['-average_score', '-date_created', 'name']`. Dus eerst de **mediaan** van de sterren, dan **wanneer de add-on is aangemaakt** (niet bijgewerkt), dan de naam. Zoeken filtert op naam en tagline (Joris, verhaal 18).
- **Op de website, zoeken:** Postgres full-text op **naam plus de lange omschrijving**, gerangschikt op `ts_rank`, hooguit 32 treffers (2 pagina's van 16). Geen tags, geen downloads in de zoekrang.
- **Op de website, lijsten:** sorteren kan op Rating (standaard), Downloads, Newest First (datum goedgekeurd), Oldest, Naam. **Er is geen sortering op "bijgewerkt".**
- **Rating op de website** is niet het gemiddelde maar een ondergrens (methode Evan Miller, `compute_rating_sortkey`, z = 1,65). Eigen berekening: 1 review van 5 sterren geeft 2,40; 10 reviews van 5 geven 3,82. Veel reviews winnen dus van één perfecte.
- **Voorpagina:** 8 willekeurige uit de **top 24 op rating**. Die top 24 heeft 47 tot 176 reviews (GEZIEN, lijst `?sort_by=-rating_sortkey`). Voor ons onhaalbaar.

### Meting: waar staan wij (GEZIEN, API 1.688 extensies, 18 nov)
Click Joints staat in de API nog als naam "Click Joints", tagline "Ball joints for 3D printed figures that show their bend range", tags Mesh en Modeling, plek 1.147 van 1.688 in de standaardlijst (0 reviews).

| Zoekwoord | In Blender: treffers, onze plek | Website: onze plek (pagina 1) | Bovenaan op de website |
|---|---|---|---|
| joint | 2, **1** | **1** | click-joints, linkforge, better-ragdoll |
| ball joint | 1, **1** | **1** | |
| 3d print | 8, 4 | niet op pagina 1 | snapsplit, bake-shape-keys, easy-print |
| print | 25, 15 | niet op pagina 1 | polyshell-builder, papercraft-pro, easy-print |
| printing | 6, **geen treffer** | niet op pagina 1 | |
| figure | 2, **1** | 11 | |
| poseable | 0 | **1** | |
| hinge | 0 | niet op pagina 1 | easy-pivot, papercraft-pro |
| connector | 4, geen treffer | niet op pagina 1 | snapsplit, easy-print |
| print in place | 0 | 7 | |
| stl | 3, geen treffer | 13 | |
| articulated, action figure, flexi | 0 | niet | |

Lezing: op het eigen woord ("joint") staan we al op 1. We verliezen op de brede printwoorden. In Blender komt dat door 0 reviews (wie reviews heeft staat boven ons), en "printing" vinden we helemaal niet omdat "3D printed" en "3D print" geen "printing" bevatten.

De geplande tagline van Free 0.1.2, `Ball joints for poseable 3D print figures, with bend range` (58 tekens), mist "printing", "stl" en "connector".

### De 3 dingen
1. **Tagline (64 tekens max):** `Poseable figures for 3D printing: ball joints with bend range` (61 tekens). Die dekt poseable, figure, 3d print, print, **printing**, ball joint, joint. Waarom: in Blender is de tagline met de naam het enige waar gezocht wordt; elk woord erbij is een zoekvraag erbij (GEZIEN). Eigenaar: Ruben en Joris, vóór 0.1.2 de deur uit gaat.
2. **Eén eerlijke review van 5 sterren.** Met mediaan 5 springen we in Blender van plek 1.147 naar de groep bovenaan, en binnen die groep staat de nieuwst aangemaakte eerst (GEZIEN in de broncode; Joris rekende plek 757 naar bovenin na). Hoe: één vriendelijke zin in de README en de changelog ("Does it work for you? An honest rating on extensions.blender.org helps others find it"), en Thijs of Daan vraagt de eerste echte gebruikers erom. Nooit zelf of nep.
3. **Lange omschrijving op de site** (telt mee bij zoeken op de website, niet in Blender): de woorden hinge (Pro), connector, STL, 3MF, articulated, action figure, print in place, flexi in gewone zinnen. Geen lijst van losse woorden; de full-text-rang telt hoe vaak en hoe dicht, dus echte zinnen werken.

### Automatisch
- **Een update tilt ons nergens omhoog in Blender** (geen sortering op bijgewerkt, standaardvolgorde op aanmaakdatum). Dat is een GEZIEN feit uit de code; dus geen updates uitbrengen voor de plek.
- Wel te automatiseren: een wekelijkse meting van onze plek per zoekwoord (het script hierboven, ±20 regels Python, gratis, draait in de CI). Thijs hoeft niets te doen.

---

## 2. Superhive (Click Joints Pro)

Click Joints Pro staat nog niet open: `superhivemarket.com/products/click-joints-pro` geeft 403 (GEZIEN 19:05 UTC). Een plek meten kan dus nog niet; wel wat de top doet.

### Hoe de winkel rangschikt (GEZIEN)
- **Zoeken:** standaard "Most Relevant"; verder Price, Most Sales, Most Reviewed, Newest, Oldest. **Geen sortering op bijgewerkt.**
- **Relevant weegt de titel zwaar, daarna tags:** Cleave heeft de titel "Cleave - Smart Model Split & Cut for 3D Printing with Connectors (Pegs, Dowel, Rod channel, Magnets, Ball Joints)" en staat op 1 bij "joint", "ball joint", "connector" en "joints 3d print". Cut Flex (titel zonder het woord) wint "poseable" via de tag `3d-printed-poseable`. Tags zijn vrij, de meeste producten hebben er 12.
- **Rijen op de voorpagina en de pagina Addons** (GEZIEN 18 nov): Staff Picks ("hand-picked by our staff who have personally reviewed them"), New and Rising, Top Selling this Week, Top Sellers, Popular Under $20, Brand New Arrivals, New from Top Creators, Top Rated, Hidden Gems, Popular Free Addons this week, **Popular Coupons This Week**, **Brand New Coupons**, Biggest Coupon Savings, Popular Items On Sale.
- **Nieuw sinds 16 nov 2026: de "For You"-pagina** (GEZIEN, blog Superhive 16 nov): toont bij ingelogde kopers producten van hun verlanglijst die in de aanbieding gaan, coupons die ze kunnen gebruiken, **nieuwe versies van wat ze bezitten of op hun verlanglijst hebben**, en "Upgrade Variant: Pro" voor wie de Lite-versie bezit.
- **Sinds 26 mei 2026** installeren en updaten kopers een gekochte add-on vanuit Blender zelf, als het product "Blender Extension Compatible" is (GEZIEN, blog Superhive).
- **Elke vrijdag "Fresh Finds"** in de nieuwsbrief: een redactie kiest nieuwe producten (GEZIEN, blog 3 mrt 2026).
- **Sitebrede acties** ongeveer per kwartaal, 25% korting, makers kiezen zelf mee te doen; deelnemers verdienden in de Winter Sale 72,5% meer per dag dan gewoon (DERDEN, Superhive-blog maart 2025). Datum van de volgende actie niet gevonden (GOK: eind november, zoals de Cyber Sale van 2024).

### Meting: de buren in onze hoek (GEZIEN, productpagina's 18 nov)
| Product | Prijs | Verkocht | Online | Reviews |
|---|---|---|---|---|
| Cleave (splitsen, ook kogelgewricht) | $23 | 200+ | 2 mnd | 3, gem. 5, coupon actief |
| CatPin | $24 | 400+ | 3 mnd | 4, coupon actief |
| Dovetail Key | $18 | 800+ | 5 mnd | 13, coupon actief |
| ARTICULATOR, figure joint generator | $1 | 30+ | 3 mnd | 2 |
| JointLab, articulated joints | $65 | 20+ | 4 mnd | 3 |
| Cut Flex (action figure, joints) | $34,99 | 10+ | 28 dagen | 0 |
| **Pose to Print: rigged characters to print-ready figures** | $24 | <10 | 16 dagen | 0 |
| FigureCut (pins en sockets) | $10 | <10 | 17 dagen | 0 |

Nieuw feit: **Pose to Print** (16 dagen oud) doet bijna wat Pro 1.1 "Rig to Figure" belooft. De hoek met figuurgewrichten op Superhive heeft nu minstens 5 kleine spelers; de drie verkopers (Cleave, CatPin, Dovetail) hebben allemaal een coupon lopen.

### De 3 dingen
1. **Titel met de zoekwoorden.** Nu heet hij "Click Joints Pro"; bij "Most Relevant" verliest hij dan van iedereen met het woord in de titel. Voorstel: `Click Joints Pro: Ball and Hinge Joints for Poseable 3D Printed Figures`. En de 12 tags vol (nu 9): ball-joint, hinge, poseable, action-figure, articulated, 3d-printing, figurine, stl, 3mf, print-in-place, rig, joints. Kost niets; de hoofdchat past het aan zodra de keuring rond is.
2. **Coupon en sitebrede actie.** Een nieuwe coupon komt in de rij "Brand New Coupons" op de voorpagina en de pagina Addons (GEZIEN: daar staan coupons van kleine makers, ook "10% off Cleave for one week"). Meedoen aan de volgende sitebrede actie geeft de rij "On Sale" en de For You-pagina van iedereen met ons op de verlanglijst. Dit is korting, geen uitgave, maar het raakt de prijs: **voorstel aan Thijs** (bijvoorbeeld 25% één week bij de lancering op Superhive). Verwachte opbrengst: GOK.
3. **Free als "Lite" op Superhive met Pro als upgrade.** For You toont "Upgrade Variant: Pro" aan wie de Lite bezit, en "Popular Free Addons this week" is een eigen rij (GEZIEN). Tegenwicht: verhaal 19 zag ±1 verkoop per 550 gratis downloads bij gratis in Blender naast betaald op Superhive. Dit is een keuze voor de hoofdchat, geen zekerheid (GOK of het meer brengt dan alleen de Blender-winkel).

### Automatisch
- **Elke nieuwe versie van Pro komt vanzelf in "For You" (sectie New) bij kopers en wie hem op de verlanglijst heeft**, en kopers krijgen de update in Blender als het product "extension compatible" staat (GEZIEN). Dat is de enige winkel waar een update iets laat zien aan mensen die nog niet kochten (de verlanglijst). Zorg dus dat het vinkje "Blender Extension Compatible" aan staat.
- De uitgave-workflow maakt de zip al; het uploaden blijft handwerk van de hoofdchat (geen openbare upload-API gevonden, GOK).

---

## 3. Gumroad Discover (Click Joints Pro)

### Hoe het werkt (GEZIEN, Gumroad Help "Gumroad Discover", 18 nov)
- Pas in Discover na **$100 aan echte verkopen** op het account, uitbetaling ingesteld, en een risicokeuring van gemiddeld 3 weken. Daarna per product: minstens 1 verkoop, een categorie, ratings aan. Producten in Discover doen automatisch mee aan het partnerprogramma van Gumroad.
- Zoeken (`gumroad.com/products/search`): sorteringen featured (standaard), newest, hot_and_new, best_sellers, highest_rated, most_reviewed. **Featured gaf bij "blender joints" dezelfde top als best_sellers** (CatPin, Auto-Rig Pro), dus verkoop telt het zwaarst (GEZIEN, één zoekterm).

### Meting (GEZIEN)
- Onze pagina "Click Joints Pro for Blender": 0 ratings, 8 tags (3d printing, action figure, articulated, ball joints, blender, blender addon, hinge joint, poseable). Goede tags.
- Bij "click joints", "blender joints", "ball joints 3d print", "articulated figure 3d print" staan wij **nergens** (logisch: nog niet in Discover). Bovenaan: CatPin (84 ratings, gem. 4,8, $21) en Cleave. Beide hebben "Blender Add-on" en het werkwoord in de naam.

### De 3 dingen
1. **De eerste $100 komt van buiten** (Superhive-kopers tellen niet; wel elke link naar onze Gumroad-pagina vanaf dortus.com, YouTube, het veld Website in Blender). Zonder dat staat Gumroad voor vindbaarheid op 0.
2. **Ratings aan laten en kopers één keer om een rating vragen** in de bedankmail (Gumroad stuurt die; de tekst kan de hoofdchat aanpassen).
3. **Naam:** `Click Joints Pro: Blender Add-on for Poseable 3D Printed Figures`. CatPin en Cleave doen het zo.

### Automatisch
Niets tot de $100 gehaald is. Daarna: niets extra; bijwerken telt niet zichtbaar mee (GOK, niet gemeten).

---

## 4. JetBrains Marketplace (Bison & Flex)

### Hoe de winkel rangschikt (GEZIEN)
- **In de IDE** (bron: `MarketplacePluginsTab.kt` in intellij-community, gelezen 18 nov) toont het tabblad Marketplace vier groepen van elk **9 plugins**: Staff Picks (`is_featured_search=true`), **New and Updated** (`orderBy=update date`), Top Downloads, Top Rated.
- **New and Updated beweegt snel:** de 100 laatst bijgewerkte plugins zijn in ±11 uur bijgewerkt (nummer 1 om 19:26, nummer 100 om 08:38 UTC op 18 nov). Dus ±9 updates per uur; een update staat ±1 uur bij de eerste 9 (GOK op GEZIEN; de IDE filtert ook nog op de eigen versie).
- **Staff Picks** zijn reuzen (.env files 33 miljoen, Rainbow Brackets 25 miljoen). Onhaalbaar.
- **Zoeken** standaard op relevantie, waarin downloads zwaar wegen; andere sorteringen: downloads, rating, update date, publish date, name.
- **Aanraadlijst bij het openen van een bestand** (Feature Extractor): een plugin die een bestandssoort declareert wordt in de IDE aangeraden als iemand dat bestand opent. Dit is volgens de marktmeting van 6 nov de grote weg naar installs. De regels: "Features implemented by the Plugin are subject to review and approval by JetBrains", en "The Plugin's ratings, reviews, and download numbers are taken into consideration. We may decline to approve newly submitted plugins that do not yet have any history" (GEZIEN, Approval Guidelines 1.3).
- **Elke update wordt met de hand gekeurd** (1 tot 4 werkdagen). Naamregel: 1 tot 4 woorden, max 20 tekens aanbevolen, geen zoekwoorden of "Support" erbij. De omschrijving kan op de site worden aangepast **zonder nieuwe versie** (GEZIEN, "Best practices for listing").

### Meting (GEZIEN, API `searchPlugins`, 18 nov ±19:10 UTC)
Bison & Flex: 6 downloads, geen rating, maker "Dortus" geverifieerd, laatste versie 2026.1.1 (8 nov).

| Zoekwoord | Treffers | Standaard (relevant) | Op update date | Bovenaan standaard |
|---|---|---|---|---|
| bison | 2 | 2 | 1 | Bison Language Support (13.060, 3,41 sterren) |
| yacc | 3 | 2 | 1 | GoYacc Support (21.187) |
| lex | 13 | 9 | 1 | thema's die "lex" in de tekst hebben |
| flex | 46 | 29 | 18 | Flash/Flex, Flexible Freemarker |
| lexer | 41 | 35 | 9 | Grammar-Kit |
| grammar | 113 | niet in top 40 | 21 | Grammar-Kit, Context Free Grammar |
| parser | 189 | niet in top 40 | 40 | PlantUML Parser |
| bison flex, flex bison, lex yacc, yacc lex | 1 | **1** | 1 | wij |

**Aanraadlijst, nu (GEZIEN, `feature/getImplementations`, 19:20 UTC):**
- `*.y`: GoYacc Support en Bison Language Support. **Wij niet.**
- `*.l`: **niemand.** `*.yy`: alleen GameMaker Tools. `*.ll`: LLVM en NPCoding (dat is LLVM-IR, niet Flex).

Bison & Flex declareert `extensions="y;yy"` en `extensions="l;ll"` in `plugin.xml`, staat sinds 17 nov openbaar, en staat er nog niet in. Jet had al als taak: "Staat hij er na 2 dagen niet in: uitzoeken waarom" (`platformen/jetbrains/taken.md`).

### De 3 dingen
1. **In de aanraadlijst komen.** Bij `*.l` zijn we dan de enige; bij `*.y` één van drie, naast een plugin met 3,41 sterren. Dit is veruit de grootste knop. Wat te doen: vr 20 nov opnieuw meten (2 dagen na openbaar). Staat hij er dan niet: de hoofdchat stuurt (na ja van Thijs op de tekst, het gaat onder zijn naam) een korte mail naar marketplace@jetbrains.com met de vraag of de bestandssoorten van 35901 voor de aanraadlijst zijn goedgekeurd. Mogelijk moet eerst een nieuwe versie (2026.1.2 ligt klaar) door de Feature Extractor (GOK).
2. **Omschrijving zonder nieuwe versie uitbreiden** met de woorden die mensen zoeken in gewone zinnen: "parser generator", "lexer", "grammar files", "GNU Bison", "Flex scanner", ".ypp". Geen lijst losse woorden (dat verbieden de regels). Effect op de brede woorden is klein zolang we 6 downloads hebben (downloads wegen zwaar), dus dit is nummer 2.
3. **Eerste reviews:** ze tellen voor Top Rated, en JetBrains noemt reviews en downloads bij het goedkeuren van de aanraadfuncties. Vragen in de bestaande Pro-melding (één keer, na een week gebruik, met "not now").

### Automatisch
- Elke goedgekeurde update staat ±1 uur in "New and Updated" in de IDE en bovenaan bij sorteren op "updated". Klein maar gratis: als er een echte verbetering is, uitbrengen via de bestaande workflow (Gradle `publishPlugin` met de sleutel die al gebruikt is). Niet voor de plek alleen uitbrengen: elke versie kost een handkeuring.
- Te automatiseren meting: dagelijks `getImplementations` voor `*.y`, `*.yy`, `*.l`, `*.ll` en de zoektabel hierboven; bij verandering een bericht in `berichten/jet.md`. Gratis, CI.

---

## 5. Garmin Connect IQ (Ebb, Ebb Calm, Gloop's Hat Tower)

Rangschikking: zie `platformen/garmin/gebruikers-krijgen-2026-11-13.md` (lijsten Trending, Hot & Fresh, New and Updated, Most Popular; Garmin publiceert de regels niet). Nieuw nagemeten: de sorteringen die de zoek-API aanneemt zijn `mostRelevant`, `mostRecent`, `highestRated`, `mostPopular`, `trending`, `hotFresh` (GEZIEN, foutmelding van de API). Bij een zoekwoord geven `mostRelevant`, `hotFresh` en `trending` vrijwel dezelfde volgorde (GEZIEN bij breathe, breath, calm, tower, stack, hat).

### Meting (GEZIEN, API 18 nov ±19:15 UTC, alleen horloge-apps)
Stand: Ebb 1 download, Ebb Calm 10, **Hat Tower 10 en sinds 17 nov 11:59 UTC live** (status APPROVED, "nieuw" tot ±1 dec), alle drie 0 reviews.

| Zoekwoord | Treffers | Relevant | Most Recent | Most Popular |
|---|---|---|---|---|
| calm | 66 | Calm 1, Ebb 4 | Calm 2, Ebb 4 | Ebb 3, Calm 7 |
| relax | 60 | Calm 10 | Calm 3 | Calm 14 |
| breath | 249 | Ebb 11, Calm 55 | | |
| breathe | 201 | Ebb 15, Calm 16 | Calm 6 | |
| breathing | 313 | Ebb 18, Calm 25 | Calm 13 | |
| stress, meditation | 61, 107 | niet in top 300 | | |
| hat | 164 | **Hat Tower 1** | 2 | 4 |
| stacking | 282 | Hat Tower 4 | 3 | 38 |
| tower | 77 | Hat Tower 13 | **1** | 19 |
| stack | 143 | Hat Tower 21 | **1** | 26 |
| game | 753 | Hat Tower **212** | 3 | |

Bovenaan bij "game", "stack" en "tower": korte namen met het woord vooraan (Snake Game, Maze Game, Stack, Stack Tower) met 100 tot 300 horloges. Hat Tower heeft 69 horloges en een lange naam.

### De 3 dingen (Hat Tower is nu het enige Garmin-product dat telt: reclame voor Hats)
1. **Eerste 10 tot 25 echte reviews binnen de 14 dagen "nieuw"** (tot ±1 dec). Apps met zoveel reviews staan in Trending en Hot & Fresh (GEZIEN 12 nov). Vragen: één zin op het eindscherm of in de omschrijving, en Thijs vraagt een paar bekenden met een Garmin. Geen nep.
2. **Meer horloges vóór dag 14**: binnen de 14 dagen ging 24% van de apps met extra horloges een klasse omhoog tegen 15% zonder; na dag 30 0 van 80 (verhaal 25, GEZIEN). Hat Tower draait op 69 van ±170.
3. **Naam**: het zoekwoord vooraan bij "stack" en "game" kost ons nu plek 21 en 212. Maar de naam is net goedgekeurd en hoort bij Hats; alleen doen als 1 en 2 niets geven (GOK of een naamwissel helpt; Garmin zoekt vaag in titel en omschrijving).

### Automatisch
- **Een update zet de app op 1 bij "Most Recent" en terug in "New and Updated"** (GEZIEN: Hat Tower staat nu op 1 bij tower en stack, omdat hij net goedgekeurd is). Maar dat geeft geen downloads (verhaal 25: klasse omhoog 0,9% met update tegen 1,0% zonder). **Dus niet doen voor de plek;** alleen updaten voor horloges erbij (vóór dag 14) of klachten.
- Meting automatiseren: het script hierboven dagelijks, gratis.

---

## 6. Steam (Hats of the Fallen, pagina nog niet live)

### Hoe Steam rangschikt (DERDEN, Valve: https://partner.steamgames.com/doc/marketing/visibility, gelezen 18 nov)
- "Players and Purchases Matter": kopen en spelen is het sterkste signaal. "Language Matters": Steam toont je vaker aan wie je taal spreekt. "Tags Matter".
- "With a few exceptions like the **Popular Upcoming** tab, wishlists are not a factor in your game's algorithmic visibility." Verlanglijsten krijgen wel een mail bij de lancering en bij 20%+ korting.
- "Store Page Traffic Doesn't Matter", "Conversion Rate Doesn't Matter", review score telt niet zolang het 40% of hoger is.
- Na de lancering: New Releases Queue (iedereen een keer), "New and Trending" als het goed loopt, Top Sellers per tag als je verkooprang haalt.
- **Update Visibility Rounds**: een plek "Recently Updated" op de voorpagina, maar alleen voor wie het spel bezit of op de verlanglijst heeft.

### Meting (GEZIEN, Steam-zoek-API, 18 nov)
- Tag Desktop Companion heeft **530 aangekondigde spellen** (filter popularcomingsoon). Bovenaan Popular Upcoming: BEAR THE BURN, Orion Blue, My Galaxy Buddy, Notched, Desktop Divinity Demo, Cornerwitch.
- Uitgebracht bovenaan de tag: Drawquarium, Spirit City, Cast n Chill, Bongo Cat, Desktop Mate, Deskrawl, TBH.

### De 3 dingen (staan al in de plannen van Sem en Sanne; hier alleen de winkelkant)
1. **Verlanglijsten vóór de lancering**: de enige plek waar ze de rang bepalen is Popular Upcoming, en daar staan 530 concurrenten in onze tag. De pagina zo vroeg mogelijk live (±8 dec) en het fest (14 tot 18 jan) met demo.
2. **Korting in het fest**: Valve zet spellen met korting bovenaan in een themafest (hoofdles 18). De eerste korting van 20%+ mailt ook alle verlanglijsten.
3. **Tags en taal**: Desktop Companion, Idler, Casual vooraan (besluit ligt er), en Chinees erbij (Steam toont vaker aan wie de taal spreekt).

### Automatisch
- Na de lancering: elke grote update als "Major Update"-event (komt in "Recently Updated" bij bezitters en verlanglijsten). De tekst schrijft een agent als concept, de hoofdchat plaatst na ja van Thijs.
- Steam laat geen onbewaakte update de plek verbeteren; ook hier niet voor de plek alleen uitbrengen.

---

## Per product: de 3 acties met de meeste kans

**Hats (Steam):** zie Steam hierboven: verlanglijsten vóór 8 dec tot het fest, festkorting, tags en Chinees. Niets extra's vanuit de winkel zelf.

**Click Joints Free (Blender):**
1. Tagline `Poseable figures for 3D printing: ball joints with bend range` in 0.1.2.
2. Eén eerlijke review vragen (README, changelog, eerste gebruikers).
3. Lange omschrijving met hinge, connector, STL, 3MF, articulated, action figure in zinnen.

**Click Joints Pro (Superhive en Gumroad):**
1. Titel op Superhive met de zoekwoorden en 12 tags, zodra de keuring rond is.
2. Coupon bij de lancering op Superhive en meedoen aan de volgende sitebrede actie (voorstel aan Thijs, raakt de prijs).
3. "Blender Extension Compatible" aan, zodat elke versie in For You en in Blender bij kopers komt. Gumroad pas na $100 van buiten.

**Bison & Flex (JetBrains):**
1. Vr 20 nov de aanraadlijst `*.y` en `*.l` meten; staat hij er niet, mail aan JetBrains (tekst via Thijs).
2. Omschrijving uitbreiden op de site (geen nieuwe versie nodig).
3. Eerste reviews vragen in de bestaande melding.

**Garmin (Hat Tower):** reviews in de 14 dagen, horloges erbij vóór ±1 dec, naam pas daarna.

---

## Wat te automatiseren, hoe, kosten, wat Thijs doet

| Wat | Hoe | Kost | Thijs |
|---|---|---|---|
| Wekelijkse plekmeting alle winkels | Eén Python-script in de CI met de zoek-API's hierboven (Blender-API, Superhive-zoekpagina, Gumroad `products/search`, JetBrains `searchPlugins` en `feature/getImplementations`, Garmin `asw/apps/keywords`, Steam `search/results`), uitkomst als csv plus een regel in het berichtenbestand van de eigenaar bij een verandering | gratis | niets |
| Aanraadlijst JetBrains dagelijks | dezelfde CI, alleen `getImplementations` | gratis | niets |
| Updates die kopers bereiken | Superhive: vinkje "extension compatible" (For You plus update in Blender); Steam: Major Update-event als concept | gratis | ja op de tekst bij Steam |
| Review vragen | één zin in README, changelog, eindscherm Hat Tower, Pro-melding Bison & Flex | gratis | niets (eigen winkelpagina en product) |

## Wat niet werkt of te duur is (niet proberen)
- **Updaten om hoger te komen** in Blender (geen sortering op bijgewerkt, GEZIEN in code), Garmin (geen sprong, verhaal 25) en JetBrains (±1 uur zichtbaar, handkeuring per versie). Alleen op Superhive (verlanglijsten) en Steam (verlanglijsten) bereikt een update iemand die nog niet kocht.
- **De voorpagina van extensions.blender.org**: top 24 op rating heeft 47+ reviews.
- **Staff Picks bij JetBrains** (reuzen van miljoenen downloads) en **Staff Picks op Superhive** (redactie, niet aan te vragen; niet gevonden hoe).
- **Gumroad Discover vóór $100** echte verkoop: je staat er niet in, wat je ook doet.
- **Zoekwoorden opstapelen in een naam of omschrijving** bij JetBrains: verboden ("adding irrelevant keywords") en de naam mag 1 tot 4 woorden zijn. Bij Superhive en Gumroad mag een lange titel wel (Cleave doet het).
- **Store-verkeer kopen voor Steam**: "Store Page Traffic Doesn't Matter" en "Conversion Rate Doesn't Matter" (DERDEN, Valve). Advertenties alleen als ze verlanglijsten of kopers geven.

## Wat ik niet kon nagaan
- Onze plek op Superhive (pagina nog niet openbaar) en op Gumroad Discover (niet toegelaten).
- Waarom Bison & Flex niet in de aanraadlijst staat (wachttijd, keuring of nieuwe versie nodig).
- Hoe "New and Rising" op Superhive en Trending bij Garmin precies rekenen (niet gepubliceerd).
- De meetscripts staan alleen in mijn sessie (`/tmp/scripts`), niet in de repo; de brief stond alleen dit bestand toe. De aanroepen staan hierboven, zodat een ander ze in een paar regels kan herbouwen.

Bronnen (allemaal met curl gelezen): broncode extensions-website op projects.blender.org (`extensions/views/public.py`, `extensions/models.py`, `ratings/utils.py`, `ratings/signals.py`); `MarketplacePluginsTab.kt` in github.com/JetBrains/intellij-community; https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html; https://plugins.jetbrains.com/docs/marketplace/best-practices-for-listing.html; https://gumroad.com/help/article/79-gumroad-discover; https://superhivemarket.com/posts/meet-your-new-for-you-page-deals-upgrades-and-new-releases-picked-just-for-you; https://superhivemarket.com/posts/blender-extension-support-launched-on-superhive; https://superhivemarket.com/posts/four-ways-to-discover-more-on-superhive; https://superhivemarket.com/posts/winter-sale-2025-recap; https://partner.steamgames.com/doc/marketing/visibility.
