# Voorstel: Shopify (apps)

## Update 6 nov 2026, avond: eigen steekproef (Vera)

**Advies: nog niet klaar, maar dichterbij. Cijfer: 6 van 10 (was 5).** De eigen meting bevestigt dat een gewone nieuwe app hier bijna niets haalt. Maar ze laat ook iets zien wat we eerder misten: als er een nieuwe regel komt, kunnen kleine makers binnen maanden duizenden winkels halen met een betaalde app. Shopify is daarmee geen plek voor "nog een app", wel voor een app die op een nieuwe verplichting of een gat inspeelt. Nagekeken: zie onderaan.

### Hoe gemeten
- apps.shopify.com was nu met curl leesbaar. De sitemap (`sitemap_apps_en.xml`) noemt 30.060 live apps (GEZIEN).
- Willekeurige steekproef van 6.000 apps (20%), van elke app de pagina gelezen: lanceerdatum, aantal reviews, prijs, maker. 5.999 met datum (GEZIEN). Data en script staan in `platformen/verkenner/data/`.
- Let op: de sitemap toont alleen apps die nog live zijn. Verwijderde apps tellen niet mee, dus de cijfers zijn eerder te mooi dan te somber.
- Installs toont Shopify niet. Reviews zijn de benadering. Hoeveel installs bij een review horen weten we niet (GOK: 1 review per 10 tot 50 installs).

### Bereik (GEZIEN, reviews als benadering)

| Lanceerde in | Apps in steekproef | Mediaan reviews | Geen review | 5+ | 10+ | 25+ |
|---|---|---|---|---|---|---|
| mei tot aug 2026 (3 tot 6 mnd) | 1.598 | 0 | 78% | 4% | 1% | 0% |
| nov 2025 tot apr 2026 (6 tot 12 mnd) | 644 | 0 | 63% | 14% | 6% | 2% |
| jan tot okt 2025 | 712 | 0 | 58% | 20% | 11% | 5% |
| 2024 | 543 | 1 | 49% | 29% | 21% | 13% |
| 2020 tot 2023 | 1.111 | 2 | 37% | 39% | 31% | 20% |

- Apps van makers met maar één app in de steekproef (76% van de nieuwe apps) doen het ongeveer even slecht als de rest: mei tot aug 2026 78% zonder review, 1% met 10+.
- Betaalde of deels betaalde apps: ±80% in elk cohort (GEZIEN, op basis van de prijsregel).

### Drukte (GEZIEN, steekproef keer 5)
- Live apps per lanceermaand in 2026: jan tot apr ±550 per maand, mei ±2.750, juni tot sept ±1.550 tot 1.950, oktober ±2.650.
- 52% van alle live apps is in 2026 gelanceerd. De piek in mei is dus echt (geen meetfout, zoals RevenueHunt dacht), en oktober is net zo druk.

### Geld: het nieuwe signaal (GEZIEN)
De sterkste nieuwe apps zitten rond de EU-knop voor herroeping, die volgens de apppagina's vanaf 19 juni 2026 verplicht is voor EU-winkels:

| App | Maker | Gelanceerd | Reviews (6 nov) | Prijzen |
|---|---|---|---|---|
| EW: EU Withdrawal Button & Form | 401layers UG (klein Duits bedrijf, 2 apps) | 9 jan 2026 | 2.323 | $9,99 tot $29,99 per maand |
| Revoq | BuschBytes (Jonas Busch Consulting) | 11 mrt 2026 | 580 | $9 tot $25 per maand |
| Wideruf-Button | Anviara LLC | 6 mei 2026 | 108 | gratis plan, $7,99 per maand |
| EU Withdrawal Button | Nayvo | 3 juni 2026 | 71 | $7,99 tot $22 per maand |

- 2.323 reviews in 10 maanden is meer dan bijna alle apps uit 2020 tot 2023 in jaren haalden. Dit zijn kleine makers, geen grote studio's.
- Hoeveel ze verdienen is niet te zien. Rekenvoorbeeld (GOK): 2.323 reviews is minstens ±20.000 installs; als 5% de kleinste betaalde laag neemt, is dat ±$10.000 per maand.
- Andere uitschieters in mei tot aug 2026: Post Purchase Upsell Hero (HeroSoftware GmbH, 62 reviews, vanaf $19 per maand). De rest van de top is grotendeels gratis.
- Les: hier verdient een kleine maker niet met een beter idee in een volle categorie, maar door als eerste te zijn bij een nieuwe verplichting of een nieuwe Shopify-functie (ook "combined listings" komt twee keer in de top voor).

### Wat dit betekent voor Dortus
- Voor: betalen zit ingebouwd, 0% afdracht onder $1 miljoen, en het bewijs dat een kleine maker in maanden groot kan worden bestaat nu (GEZIEN).
- Tegen: wie niet zo'n golf pakt, haalt in 3 tot 6 maanden meestal niets (78% geen review). De drukte is in 2026 ±4 keer zo groot als begin 2026. De herroepingsgolf zelf is al bezet.
- Eerste idee: een vaste "regelradar" voor EU-webwinkels. Volg aankomende EU- en landenregels (bijvoorbeeld toegankelijkheid, de EU-batterijverordening, verpakking en EPR, de nieuwe productveiligheidsregels, prijsaanduiding) en bouw de app voordat de deadline valt. Bouwen in 1 tot 2 weken kan (GOK), de keuring kost weken, dus we moeten maanden voor een deadline beginnen.

### Wat er nog moet voor een ja
1. Een concrete aankomende regel met een datum, die minstens 3 maanden weg is en waarvoor nog geen sterke app bestaat. Dat is het volgende onderzoek (eerst kijken in de winkel met de zoekfunctie).
2. Het verband tussen reviews en installs uit één openbare bron (bijvoorbeeld een maker die beide noemt).
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
