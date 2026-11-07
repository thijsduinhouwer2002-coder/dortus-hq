# Voorstel: Shopify (apps)

## Vervolg B, deel 1 (7 nov 2026, 08:15): de tweede golf, garantielabel EmpCo (Vera, NOG NIET NAGEKEKEN)

Vraag: werkt de route "vroeg bij een nieuwe verplichting" vaker dan één keer? Getoetst op de golf ná de herroepingsknop: de verplichte EU-garantiemelding en het GARAN-label (richtlijn EmpCo, verplicht vanaf 27 sep 2026, DERDEN: [nuonic](https://nuonic.de/en/insights/e-commerce-deadlines-2026-27)).
- Gemeten (GEZIEN): in de Shopify-sitemap 54 apps met garantie, GARAN, Gewährleistung, green claims of EmpCo in de naam (namen gezocht, dus eerder te weinig dan te veel). Gelanceerd tussen mei en 6 nov 2026, de meeste in juli tot oktober.
- Reviews op 7 nov: mediaan 0, 38 van de 54 hebben er nul, samen 198. Top: 50 (5 aug), 49 (26 aug), 37 (24 jun), 14, 13. Ter vergelijking de herroepingsknop: winnaars 2.323 en 580.
- De winnaars kwamen 4 tot 13 weken voor de deadline, net als bij de herroepingsknop, maar halen een fractie. Binnen 4 maanden waren er al 54 aanbieders, ook na de deadline komen er elke week bij.
- Shopify zei op 5 nov dat apps zonder installs na zes maanden uit de winkel gaan (DERDEN: [Sicard, tracker](https://taylorsicard.com/the-index/shopify-platform-deadlines-tracker-2026), nog zonder datum).
- Voorlopige les (GOK): de golf-route werkt wel, maar elke nieuwe golf trekt meteen tientallen makers, en de opbrengst per golf hangt af van hoe zwaar de plicht is. Een knop die elke webwinkel moet hebben gaf duizenden winkels, een label dat veel winkels zelf in het thema zetten veel minder.
- Nog te meten in deel 2 (volgende run): (1) e-facturen in Duitsland (plicht om te versturen vanaf 1 jan 2027 boven €800.000 omzet, 1 jan 2028 voor iedereen, DERDEN: [xictron](https://www.xictron.com/en/blog/legal-changes-2027-deadline-calendar-online-shops/)): er zijn nu maar een handvol Shopify-apps met XRechnung of ZUGFeRD in de naam (GEZIEN: 4); (2) scripttags stoppen op 1 maart 2027 (DERDEN: Sicard): welke oude apps breken en laten winkels zonder vervanger; (3) daarna een oordeel: blijft het 6 of wordt het 5.

## Update 7 nov 2026, ochtend: hoe haalt een gewone nieuwe app zijn eerste 100 installs? (Vera, bericht Thijs 6 nov 20:32)

**Kort antwoord: het gevoel van Thijs klopt.** Een gewone nieuwe app haalt in 2 tot 6 maanden bijna nooit 100 installs: naar schatting ±2 tot 6 van de 100 apps (GOK op basis van GEZIEN, uitleg hieronder; uiterste bovengrens ±11). Na 6 tot 12 maanden zijn het er ±7 tot 15 van de 100 (GOK). Ter vergelijking: bij Obsidian haalt 68 tot 88% de 100 gebruikers, bij JetBrains 54%. In de ±15 gelezen forumdraden liet geen enkele kleine maker zonder eigen publiek in 2025 of 2026 aantoonbaar zien hoe hij de 100 haalde (DERDEN, alleen binnen die draden). **Advies blijft: nog niet klaar, cijfer 6.** Het cijfer rust alleen nog op de route "vroeg zijn bij een nieuwe verplichting of functie" (zie update 6 nov). Een gewone app in een gewone categorie is hier geen optie.

### Nieuwe meting 1: hoeveel installs horen bij een review (GEZIEN)
- StoreCensus telt per app op hoeveel winkels de app aan de voorkant zichtbaar is (actieve installs, alleen apps die je op de winkelpagina kunt zien). Hun openbare pagina's (`storecensus.com/stats/app/<naam>`) zijn met curl leesbaar. Ik las alle 2.369 pagina's uit hun sitemap, koppelde 2.184 aan de Shopify-pagina (lanceerdatum en reviews) en rekende uit hoeveel actieve installs er per review zijn.
- Uitkomst, alle 2.184 apps: mediaan **7 actieve installs per review**, de middelste helft tussen 4 en 18.
- Apps van 2025 en later met 100 tot 300 installs (n=11): mediaan 13, middelste helft 6 tot 27. Met 24 tot 100 installs (n=8): mediaan 27.
- Voorbeelden: Revoq 4.196 winkels en 582 reviews (±7), Appio Amazon Reviews 846 en 122 (±7). Eén maker op het forum noemt ±500 installs en 17 reviews in 14 maanden (±29 per review, DERDEN: [forum](https://community.shopify.com/t/675500)).
- Vertaling (GOK): **100 actieve installs komt overeen met ±4 tot 16 reviews, midden ±8.** Dat komt van de jonge apps (2025 en later, 100 tot 300 installs): 100 gedeeld door 27, 13 en 6. Met de mediaan van alle apps (7 per review) zou het ±14 reviews zijn. Bij nieuwe apps ligt het eerder aan de lage kant (meer installs per review), want reviews komen langzaam en makers melden dat de reviewpopup bijna niets oplevert (DERDEN: [forum 39325](https://community.shopify.dev/t/39325), 50 tevreden betalende klanten sloten de popup allemaal zonder review).
- Grenzen: StoreCensus ziet alleen apps met iets op de winkelpagina (apps die alleen in het beheer werken telt het niet), toont pas pagina's vanaf ±24 installs, en heeft bijna alleen oude apps (maar 6 uit 2026). De verhouding komt dus vooral van oudere apps. Actieve installs zijn ook minder dan alle installs ooit (verwijderingen tellen niet mee), dus de echte verhouding ligt nog iets hoger.
- Ook met weinig reviews haal je soms de 100: van de 62 apps uit 2025 en later met 100+ installs bij StoreCensus hebben er 10 minder dan 4 reviews, waarvan 7 nul (vooral merkbedrijven zoals Fullstory en Airwallex). Rekenen met die kansen voor de 292 apps met 1 tot 3 reviews en de 45 met 4 tot 7 geeft een uiterste bovengrens van ±11% in mei tot aug 2026 (nagerekend door de controleur). Die ligt te hoog, omdat StoreCensus pas vanaf ±24 installs telt. Daarom ±2 tot 6 van de 100 als beste schatting; de kolom 8+ is waarschijnlijk te streng. Alleen gekochte reviews werken de andere kant op.
- De koppeling gaat ervan uit dat de naam in de link op StoreCensus en Shopify gelijk is (StoreCensus linkt niet door). Bij 11 van 11 nagekeken apps klopte dat.

### Nieuwe meting 2: hoe vaak lukt de 100 (GEZIEN reviews, GOK vertaling)
Toegepast op de willekeurige steekproef van 6.000 apps van 6 nov:

| Lanceerde in | n | 4+ reviews (ruime grens) | 8+ (midden) | 15+ (strenge grens) |
|---|---|---|---|---|
| mei tot aug 2026 (2 tot 6 mnd) | 1.598 | 4,1% | 1,3% | 0,6% |
| nov 2025 tot apr 2026 (6 tot 12 mnd) | 644 | 15,4% | 7,0% | 3,6% |
| jan tot okt 2025 | 712 | 23,2% | 13,9% | 8,3% |
| 2024 | 543 | 31,1% | 24,3% | 16,9% |

- Naar prijs, mei tot aug 2026, 8+ reviews: alleen betaald 0,6% (n=514), gratis plan met betaalde lagen 1,4% (n=714), helemaal gratis 1,9% (n=270), gratis te installeren met kosten later 3,0% (n=100). **Een app die vanaf dag één geld vraagt haalt de 100 dus het minst vaak:** ±1 op de 40 met de ruime grens, ±1 op de 170 met het midden.
- Wie haalt het wel? De 21 apps van mei tot aug 2026 met 8+ reviews: 4 zijn herroepingsknoppen (de EU-golf), een deel komt van grote makers met veel apps (Avada, Globo, Loox, ShopiDevs), en maar 2 zijn alleen betaald. Bijna allemaal gratis of met gratis plan.

### Wat makers zelf zeggen (DERDEN, forumdraden 2026, door een hulpagent gelezen en op 7 nov nagekeken in de winkel)
- Van ±15 nieuwe apps uit 2026 die op de Shopify-fora hun begin beschreven, meldt bijna elke maker 0 of een handvol installs. Van 8 nagekeken apps hadden er 3 tot 10 maanden later 6 nog 0 reviews en 2 er 1 (Livy Loyalty, Store Analytics, LogX, LinkGuard, Purser, StoreVault; Stock Near Me en SuggestIF AI). Draden: [37237](https://community.shopify.dev/t/got-approved-3-weeks-ago-what-actually-worked-for-your-first-50-installs/37237), [643974](https://community.shopify.com/t/643974), [675500](https://community.shopify.com/t/675500), [654059](https://community.shopify.com/t/654059), [708775](https://community.shopify.com/t/708775).
- Advertenties in de App Store bij 0 reviews: 5 vermeldingen in 5 categorieën, van ±3 makers, kregen bij ±$7 per klik 0 installs ([675500](https://community.shopify.com/t/675500)).
- Wat volgens makers wel werkt: persoonlijk benaderen van winkels die het probleem al hebben (bijvoorbeeld winkels die een concurrent 1 ster gaven) en aanbieden de app gratis voor ze in te stellen; echt helpen op fora; een gratis plan. Allemaal handwerk onder iemands naam, dus voor ons via Thijs.
- Eén app haalde ±2.000 installs in 2 maanden, maar gratis, zonder omzet en zonder genoemd kanaal ([699068](https://community.shopify.com/t/699068)).
- Let op: veel forumposts lezen gepolijst, sommige mogelijk met een verkoopdoel. Reddit en Indie Hackers waren niet leesbaar met curl.

### Wat dit betekent
- Thijs heeft gelijk: bereik krijgen is hier heel moeilijk, en voor een betaalde app nog moeilijker. Mijn meting van 6 nov liet dat al zien; nu is ook de vertaling van reviews naar installs gemeten, en die maakt het beeld niet mooier.
- Alleen de route "vroeg bij een verplichting met datum" laat kleine makers snel groot worden (Revoq: 4.196 winkels binnen 8 maanden, GEZIEN via StoreCensus). Ook daar wint maar een klein deel. Die route blijft het enige waarom Shopify een 6 houdt.
- Volgende stap blijft vervolg B: een aankomende regel of functie met datum zoeken. Vindt die run niets sterks, dan zakt Shopify naar 5.

Nagekeken door een controleur (akkoord met 8 correcties, alle verwerkt: Revoq en Appio goed gezet, advertentieclaim kleiner, bovengrens ruimer, labels en grenzen aangevuld).

Data en scripts: `data/shopify-storecensus-*` (haal-, koppel- en analysescript, ruwe pagina's en de gekoppelde tabel). Het analysescript draait vanuit de hoofdmap van de repo.

---

## Update 6 nov 2026, avond: eigen steekproef (Vera)

**Advies: nog niet klaar, maar dichterbij. Cijfer: 6 van 10 (was 5).** De eigen meting bevestigt dat een gewone nieuwe app hier bijna niets haalt. Ze laat ook zien dat een kleine maker die vroeg is bij een nieuwe verplichting, binnen maanden duizenden winkels kan halen met een app met gratis plan en betaalde lagen. Dat lukt maar weinigen: van de ±130 apps op de laatste golf wonnen er twee. Nagekeken door een controleur (akkoord met 11 correcties, alle verwerkt).

### Hoe gemeten
- apps.shopify.com was nu met curl leesbaar. De sitemap (`sitemap_apps_en.xml`) noemt 30.060 live apps (GEZIEN).
- Willekeurige steekproef van 6.000 apps (20%, Python `random.seed(42)`), van elke app de pagina gelezen: lanceerdatum, aantal reviews, prijs, maker. 5.999 met datum (GEZIEN). Data en scripts staan in `platformen/verkenner/data/`. Het analysescript draait vanuit de hoofdmap van de repo op de opgeslagen JSON.
- De sitemap toont alleen apps die nog live zijn. Voor de reviewcijfers maakt dat de uitkomst eerder te mooi. Voor de drukte werkt het andersom: oude jaren tellen minder mee, dus het aandeel van 2026 lijkt groter.
- Installs toont Shopify niet. Reviews zijn de benadering. Hoeveel installs bij een review horen weten we niet (GOK: 1 review per 10 tot 50 installs).

### Bereik (GEZIEN, reviews als benadering)

| Lanceerde in | Apps in steekproef | Mediaan reviews | Geen review | 5+ | 10+ | 25+ |
|---|---|---|---|---|---|---|
| mei tot aug 2026 (2 tot 6 mnd) | 1.598 | 0 | 78% | 4% | 1% | 0,3% |
| nov 2025 tot apr 2026 (6 tot 12 mnd) | 644 | 0 | 63% | 14% | 6% | 2% |
| jan tot okt 2025 | 712 | 0 | 58% | 20% | 11% | 5% |
| 2024 | 543 | 1 | 49% | 29% | 21% | 13% |
| 2020 tot 2023 | 1.111 | 2 | 37% | 39% | 31% | 20% |

- Apps van makers met maar één app in de steekproef (76% van de nieuwe apps) doen het ongeveer even slecht als de rest: mei tot aug 2026 78% zonder review, 1% met 10+.
- Prijs, mei tot aug 2026: ±31% alleen betaald (eventueel met proefperiode), ±45% gratis plan met betaalde lagen, ±17% helemaal gratis, ±6% gratis te installeren (GEZIEN, nageteld door de controleur).

### Drukte (GEZIEN, steekproef keer 5)
- Live apps per lanceermaand in 2026: jan tot apr ±530 tot 680 per maand, mei ±2.750, juni tot sept ±1.550 tot 1.950, oktober ±2.650.
- Sinds mei 2026 dus ±3 tot 5 keer zo veel nieuwe apps per maand als in jan tot apr 2026. Die sprong tussen maanden van hetzelfde jaar is echt, ook al dacht RevenueHunt aan een meetfout. De oorzaak is onbekend (GOK: AI-bouwhulpen).
- 52% van alle live apps is in 2026 gelanceerd (te hoog door de verwijderde oude apps, zie boven).

### Geld: het nieuwe signaal
De EU-knop voor herroeping (Richtlijn (EU) 2023/2673) is vanaf 19 juni 2026 verplicht voor EU-webwinkels (DERDEN: [iubenda](https://www.iubenda.com/en/blog/online-withdrawal-function-eu-directive-2023-2673/), [Lexgo](https://www.lexgo.be/en/news-and-articles/14873-the-online-withdrawal-button-a-new-mandatory-obligation-for-online-traders), [JD Supra](https://www.jdsupra.com/legalnews/eu-consumer-protection-law-update-new-9377759/); Revoq en Nayvo noemen de datum ook op hun pagina).

Apps voor die knop (GEZIEN met curl, maar uitgekozen, niet willekeurig: drie van de vier zitten niet in de steekproef):

| App | Maker | Gelanceerd | Reviews (6 nov) | Prijzen |
|---|---|---|---|---|
| EW: EU Withdrawal Button & Form | 401layers UG, 2 apps (verdere grootte onbekend) | 9 jan 2026 | 2.323 | gratis plan, $9,99 en $29,99 per maand |
| Revoq | BuschBytes (Jonas Busch Consulting) | 11 mrt 2026 | 580 | gratis plan, $9 en $25 per maand |
| Wideruf-Button | Anviara LLC | 6 mei 2026 | 108 | gratis plan, $7,99 per maand |
| EU Withdrawal Button Free | Nayvo | 3 juni 2026 | 71 | gratis plan, $7,99 en $22 per maand |

- Ter vergelijking: van de 1.111 apps uit 2020 tot 2023 in de steekproef halen er 3 de 2.323 reviews en 19 de 580 (GEZIEN).
- Maar de golf als geheel: in de steekproef zitten 26 herroepingsapps. 13 hebben nul reviews, de mediaan is 0,5, maar 2 hebben meer dan 10 (GEZIEN). Keer 5 zijn er ±130 aanbieders. De twee grote winnaars waren er maanden voor de deadline (jan en mrt).
- Tegenvoorbeeld van dezelfde maker: de tweede app van 401layers, voor de productveiligheidsregels (GPSR, deadline dec 2024), heeft maar 29 reviews. Een nieuwe regel geeft dus geen vaste winst.
- Hoeveel de winnaars verdienen is niet te zien. Rekenvoorbeeld (GOK): het harde minimum is 2.323 winkels. Bij 1 review per 10 tot 50 installs en 2 tot 5% die betaalt ($9,99) ligt het ergens tussen ±$4.000 en ±$58.000 per maand, minder door verwijderde installs.
- Andere uitschieter mei tot aug 2026: Post Purchase Upsell Hero (HeroSoftware GmbH, 62 reviews, vanaf $19 per maand). Ook "combined listings" (een nieuwe Shopify-functie) komt twee keer in de top voor.
- Les: een kleine maker verdient hier niet met een beter idee in een volle categorie, maar door als een van de eersten bij een nieuwe verplichting of functie te zijn, en dan ook nog de beste of vroegste.

### Wat dit betekent voor Dortus
- Voor: betalen zit ingebouwd, 0% afdracht onder $1 miljoen, en het bewijs dat een kleine maker in maanden heel groot kan worden bestaat (GEZIEN, al zijn het uitschieters).
- Tegen: wie niet zo'n golf pakt, haalt in 2 tot 6 maanden meestal niets (78% geen review). Sinds mei ±3 tot 5 keer zo veel nieuwe apps per maand. Bij een golf springen honderd makers tegelijk in, en vroeg zijn is nodig maar niet genoeg (zie GPSR).
- Eerste idee: een "regelradar" voor EU-webwinkels. Volg aankomende EU- en landenregels met een vaste datum en bouw de app ruim voor de deadline, zodat we bij de eersten zijn. Bouwen kan in 1 tot 2 weken (GOK), de keuring kost weken, dus maanden voor een deadline beginnen.

### Wat er nog moet voor een ja
1. Een concrete aankomende regel of Shopify-functie met een datum, minstens 3 maanden weg, waarvoor nog geen sterke app bestaat, en waarom die beter uitpakt dan de GPSR. Dat is het volgende onderzoek.
2. Het verband tussen reviews en installs uit een openbare bron (een maker die beide noemt).
3. Partneraccount via Thijs (gratis of $19).

---

## Eerste versie (6 nov, middag), zonder eigen meting

**Advies: nog niet klaar, voorlopig nee. Cijfer: 5 van 10.** Hoofdreden: we vonden geen enkel duidelijk voorbeeld uit 2026 van een kleine maker die een nieuwe Shopify-app snel naar betalende klanten bracht, terwijl er de afgelopen maanden veel meer nieuwe apps bijkomen. Er wordt wel veel geld verdiend, vooral door oude apps. Opnieuw bekijken als er zo'n voorbeeld opduikt of als we een eigen ingang naar winkeliers hebben. Geschreven op 6 nov 2026.

## Meetgrens
apps.shopify.com en shopify.dev waren in deze run geblokkeerd. Er is dus geen eigen meting: alles hieronder is DERDEN of GOK, en de officiële regels zijn niet gelezen. De omzetcijfers zijn modellen van derden, geen betaalgegevens. De pagina's zijn via een samenvattend hulpmiddel gelezen en de tellingen van Jakubik en AppstorePulse alleen via Sicard. Reddit en X zijn niet doorzocht.

## Cijfers

**Bereik**
- Installs van nieuwe apps na 3 tot 6 maanden en het percentage met 100+: niet gemeten. Schattingen bestaan bij betaalde diensten (Store Leads, StoreCensus). Wij gebruiken reviews als benadering (GOK dat dat iets zegt).
- 2026-apps zonder review: 80% (Jakubik) of 77% (steekproef Sicard, 211 apps). 2025-apps zonder review: 68% (56 apps). 1% van de 2026-apps uit de steekproef haalde 20 reviews (±2 apps), Jakubik telt er 114 over heel 2026. [Sicard, okt 2026](https://taylorsicard.com/blog/shopify-app-store-statistics-2026)
- Let op: dit cijfer is vervuild. 82% komt van eerste keer makers, één partner bracht 86 apps uit met samen één review, de top 12 uitgevers hebben 384 apps en 10 reviews. Het zegt dus weinig over een serieuze app.
- Hele winkel: 51% zonder review, 81% onder de 10. [RevenueHunt, juni 2026](https://revenuehunt.com/state-of-the-shopify-app-economy/)
- Eén voorbeeld: de app van Barn2 (sept 2025) had ±6 maanden en 1.000 gebruikers nodig voor genoeg reviews voor de Built for Shopify-badge (gratis was hun eigen keuze) en heeft na ±1 jaar tien reviews. [Barn2](https://barn2.com/blog/shopify-app-store-saturation/)

**Geld**
- Betalen zit ingebouwd. 0% afdracht over de eerste $1 miljoen, daarna 15%. [Sicard](https://taylorsicard.com/blog/shopify-app-store-statistics-2026). Een andere bron noemt daarnaast 2,9% verwerkingskosten en eenmalig $19 registratie (één bron, niet bevestigd). [WeekOneLabs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026)
- Shopify betaalde vorig jaar meer dan $1,3 miljard uit aan bouwers in het hele ecosysteem (eigen opgave, 28 april 2026). [Shopify](https://www.shopify.com/news/billion-dollar-ecosystem)
- Middelste app uit de 1.675 die Barn2 kon schatten: $2.500 tot $5.200 per maand, voor de afdracht. Jongste vijfde ±$190, oudste vijfde ±$19.100 (onduidelijk of dat gemiddelde of mediaan is). Kan een factor twee mis zitten. [Barn2](https://barn2.com/blog/shopify-app-store-saturation/)
- Die groep is een selectie uit de winkel, dus te rooskleurig voor een willekeurige nieuwe app.
- Scheef: de helft van die 1.675 deelt 0,6% van de omzet, de top 16 heeft 40,6%. Top 1% van de hele winkel naar schatting 72%, ±36% lijkt iets te verdienen (model). [RevenueHunt](https://revenuehunt.com/state-of-the-shopify-app-economy/)
- Mediaan maandprijs: $20. [Sicard](https://taylorsicard.com/blog/shopify-app-store-statistics-2026)
- Voorbeelden van kleine makers: geen schoon voorbeeld uit 2026. [RotateProduct](https://www.mrrstory.com/stories/this-indie-hacker-reached-6772-mrr-with-just-20day-meta-ads) haalde $6.772 per maand na ±5 maanden, maar met advertenties en vooral via de iOS-app. [$1.000 per maand in 4 maanden](https://malisauskas.medium.com/from-zero-to-1000-mrr-in-4-months-how-i-created-a-shopify-app-microsaas-b84cf72e24f5) is uit 2021. Onze zoektocht was beperkt, dus dit is geen sterk bewijs dat ze er niet zijn.

**Drukte**
- Sicard over Jakubik: jarenlang 500 tot 700 nieuwe apps per maand, mei 2026 2.861, sindsdien niet onder 1.500. In 2026 tot nu toe ±1.190 per maand (eigen rekenwerk: 11.916 in 10 maanden). AppstorePulse telde 2.713 in mei. [Sicard](https://taylorsicard.com/blog/shopify-app-store-statistics-2026)
- Omstreden: RevenueHunt noemt ±2.800 lanceringsdata in mei een eenmalige meetfout en haalt die uit zijn telling. Een sterke stijging is aannemelijk, de exacte piek niet.
- Totalen: 22.546 (RevenueHunt, juni), 29.245 (Jakubik, okt), Shopify zelf "meer dan 21.000" (april). AppJubilee geeft 16.429 maar toont nu "1 nieuwe app in 30 dagen", die tracker is dus onbetrouwbaar.
- Eén forumdraad (8 okt): lanceringen +10% in een maand, nieuwe reviews -4%. Eén maand, via Sicard.
- Keuring: voorjaar 2026 tot 10 weken ([forum](https://community.shopify.dev/t/longer-app-store-review-times-what-you-need-to-know/31728?page=4)), recente losse meldingen 1 tot 6 weken ([forum aug](https://community.shopify.dev/t/shopify-app-review-still-assigning-a-reviewer-after-5-days-how-long-does-it-take/36879), [WeekOneLabs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026)). Huidige stand onzeker.

**Vindbaarheid**
- Meningen lopen uiteen. Sicard: zoeken op een brede term is voor een nieuwe app "close to a lottery" en groeiers brengen eigen winkeliers mee. Maar in een [forumdraad van aug 2026](https://community.shopify.com/t/shopify-app-developers-whats-actually-driving-paid-merchants-for-you-in-2026/660749) noemen twee makers zoeken in de winkel als beste kanaal.
- KAching begon handmatig in Facebook-groepen en krijgt nu 90% van zijn installs organisch (50% op de merknaam, 40% andere zoektermen, eigen opgave). [Indie Hackers](https://www.indiehackers.com/post/qdReVAgLjz6EpW4OrJSI). Eén voorbeeld.
- Badge Built for Shopify: ±7% van de apps (AppstorePulse via Sicard, mei), vraagt eerst reviews en gebruikers.

**Past het bij ons**
- Bouwen in 1 tot 2 weken kan (GOK). Daarna wachten op de keuring en doorlopend support aan winkeliers. Uitval 5 tot 12% per maand ([WeekOneLabs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026), één bron).
- Thijs moet een partneraccount aanmaken, mogelijk met $19 kosten.

## Voor
- Klanten betalen al voor apps, en van de omzet blijft bijna alles over.
- Rekenvoorbeeld: bij $20 per maand zijn ±20 betalende winkels genoeg voor ons doel van maart 2027 (GOK, uitval niet meegerekend). De jongste vijfde bij Barn2 zit met ±$190 daar nog onder.

## Tegen
- Geen aantoonbaar voorbeeld uit 2026 van snel betaald krijgen.
- Veel meer nieuwe apps dan vorig jaar, ±2 keer over heel 2026.
- Geld zit vooral bij oude apps: oudste vijfde ±100 keer de jongste.
- Groot worden vraagt hier waarschijnlijk werk buiten de winkel, en dat gaat onder iemands naam, dus via Thijs (GOK).

## Eerste idee (als het later toch ja wordt)
Een klein hulpmiddel voor een smalle Europese behoefte, waar een brede zoekterm niet nodig is, bijvoorbeeld rond EU-regels voor webwinkels. Eerst uitzoeken wat er ontbreekt.

## Wat er nog gemeten moet worden
Steekproef van minstens 30 apps uit mei tot augustus 2026 met reviews, prijs en maker, zodra apps.shopify.com leesbaar is (netwerkpunt op de lijst voor Thijs). Daarnaast installs via Store Leads of StoreCensus (kost geld, dus via Thijs) en cijfers uit Reddit en X.

## Nakijken
Eerste versie afgekeurd door de controleur (6 nov), herschreven met zijn correcties, tweede controle akkoord.
