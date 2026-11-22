# Voorstel: Garmin Connect IQ (apps, datavelden en wijzerplaten voor Garmin-horloges)

Onderzocht door Vera op 6 nov 2026 (run 18:31 UTC). Nagekeken door een controleur: akkoord met 9 correcties, alle verwerkt. Eigen meting via de openbare winkel-API van apps.garmin.com, zonder sleutel.

## Kort
- **Cijfer: 5 van 10.** Advies: **nog niet klaar.** Eerst 3 tot 4 weken de download-emmers van betaalde apps volgen (kost niets). Klopt het daarna dat een download een verkoop is, dan een kleine proef met één betaald dataveld of één betaalde app. Daarvoor één geldstap voor Thijs: $100 per jaar voor het verkopersaccount.
- Waarom interessant: de winkel laat zelf zien hoeveel betaalde apps van nieuwe makers gedownload worden, en betalen gaat volgens makers vóór het downloaden (DERDEN, niet zeker). Een kleine groep sportapps van nieuwe makers haalt 1.000+ als betaalde app.
- Waarom nog geen ja: een gewone nieuwe betaalde app (geen wijzerplaat) haalt weinig. Van 244 betaalde apps uit jan tot aug 2026 haalde 11% de 1.000+, en 56% bleef op 10+ of lager (GEZIEN, controleur). Dat is $25 tot $250 na afdracht, vaak niet genoeg voor de $100 per jaar. Er is maar één maker die zijn verkoopcijfer openbaar deelde.
- Stopregel voor een proef: haalt de proefapp na 3 maanden geen 100+ als betaalde app, dan stoppen we na het eerste jaar.

## Hoe gemeten
- De winkel heeft een open API (`apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps`) met per app: type, downloads, reviews, prijs, datum van eerste goedkeuring en maker. Script: `data/garmin-haal-script.py`, analyse: `data/garmin-analyse-script.py`, ruwe gegevens (27.935 apps sinds juni 2025): `data/garmin-nieuw-sinds-jun2025-2026-11-06.json`.
- Volledige lijst opgehaald, gesorteerd op "nieuwst": 50.150 rijen, **44.384 unieke apps** (GEZIEN). De sortering van Garmin schuift tijdens het ophalen, dus ±5.800 rijen waren dubbel en een vergelijkbaar aantal apps kan ontbreken. De steekproef is dus ±85 tot 90% van de winkel, niet geselecteerd op succes (GOK voor het percentage).
- **Downloads staan alleen in emmers:** 0, 1+, 10+, 100+, 1.000+, 10.000+, 50.000+, 100.000+ enzovoort (GEZIEN). Daarom geef ik de mediaan als emmer.
- Venster voor bereik: apps met eerste goedkeuring tussen 6 mei en 6 aug 2026 (3 tot 6 maanden oud).
- Reviews van 34 nieuwe betaalde apps met 1.000+ gelezen via dezelfde API, om te zien of ze gratis begonnen.

## Bereik (GEZIEN, apps van 6 mei tot 6 aug 2026)

| Groep | Aantal | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|
| Alles | 4.031 | 10+ | 31% | 7% |
| Wijzerplaten | 3.295 | 10+ | 24% | 5% |
| Apps | 538 | 100+ | 65% | 16% |
| Datavelden | 142 | 100+ | 58% | 17% |
| Widgets | 50 | 100+ | 54% | 14% |
| Kleine makers (5 of minder nieuwe apps in die maanden), alle typen | 1.122 | 100+ | 66% | 19% |
| Kleine makers, geen wijzerplaat | 517 | 100+ | 64% | 18% |
| Kleine makers, geen wijzerplaat, **betaald** | 55 | 10+ | 44% | 13% |

- Let op: de groep "kleine makers, geen wijzerplaat" bestaat voor 462 van de 517 uit gratis apps. Voor geld telt de betaalde rij: mediaan 10+, 44% haalt 100+.
- Alle betaalde apps zonder wijzerplaat met eerste goedkeuring 1 jan tot 6 aug 2026: 244 stuks, 11% haalt 1.000+, 56% blijft op 10+ of lager (GEZIEN, nagerekend door controleur).
- De grote massa zijn wijzerplaten van een paar fabrieken: de top 10 makers brachten er in drie maanden 1.519 uit (237, 201, 187 ...). Zonder die fabrieken ziet het er veel beter uit.
- Garmin Connect heeft volgens the5krunner ±45 miljoen actieve gebruikers (DERDEN, the5krunner.com/2026/05/01/garmin-connect-users-2026/, schatting van die site).

## Geld

- **Regeling:** $100 per jaar verkopersaccount en 15% afdracht per verkoop (DERDEN, maker Charlie op het Garmin-forum, bevestigd door een tweede maker in een andere draad). Uitbetaling via Adyen. Betaling gaat vóór het downloaden, er is geen kooprecht binnen de app (DERDEN, één forumbericht van flocsy, die zelf schrijft "as far as I understand"). Open punten: bij apps met proefperiode is een download geen verkoop, en het is onbekend of opnieuw installeren of een tweede horloge van dezelfde koper ook als download telt. Een proefperiode kan wel (34 van 8.147 betaalde apps gebruiken het, GEZIEN).
- **Betaalde apps in de winkel:** 8.147 (GEZIEN), allemaal in dollars, prijsmediaan $2,25. 340 hebben 1.000+ downloads, 54 hebben 10.000+ (GEZIEN).
- **Nieuwe betaalde apps per maand:** ±300 tot 440 in de eerste helft van 2026, ±900 in sep en okt 2026 (GEZIEN). Het meeste zijn wijzerplaten.
- **Eén maker met eigen cijfers:** Ski Pin (dataveld, $4, later $4,99, uitgebracht januari 2026) gebruikt een eigen server en verkocht 68 stuks in de eerste maand. Hij schatte zijn kosten in het slechtste geval op $340 per jaar (inclusief server, die in werkelijkheid $8,46 per maand kostte) en verwacht quitte te spelen (DERDEN, forums.garmin.com, draad "I Monetized My Ski App"). In de winkel staat Ski Pin nu op $4,99 en 100+ (GEZIEN), dat klopt met die cijfers.
- **Nieuwe kleine makers met betaalde apps op 1.000+ (GEZIEN, eerste goedkeuring 2026, geen wijzerplaat):**
  - Multipassionate: Hybrid Smash (Hyrox, jan 2026), Pickleball Smash (jan 2026) en Ping Pong Smash (mei 2026), alle drie $8,49 en 1.000+. Als alle downloads verkopen zijn, is dat minstens 3.000 x $8,49 x 0,85 = ±$21.600 voor de maker. Dat is een bovengrens (GOK): onzeker of elke download een verkoop is, en mogelijk gaat er btw af bij Europese kopers (niet nagekeken). In de reviews van Hybrid Smash, Pickleball Smash en Padel Smash geen aanwijzing dat ze gratis begonnen; Padel Smash had op 29 jan 2026 al een review "for the price of a drink". Geen klachten is wel zwak bewijs. Dezelfde maker heeft ook gratis varianten (Tennis Smash met 1.000+, Badminton Smash, Smash Coach), en Padel Smash ($8,49) staat pas op 100+. Niet alles van deze maker haalt dus 1.000+.
  - Meridian, RuckTrack ($2,99, april 2026, 1.000+; de maker heeft ook een gratis versie die via KiezelPay buiten Garmin om betaald wordt, 100+). ScannerApp, Flight Scanner Pro ($2,99, aug 2026, 1.000+, reviews als "happy to pay for the full version"). Rampo, Peak Finder Compass (widget, $3,49, mei 2026, 1.000+; zijn betaalde dataveld van $1,99 staat op 100+). LouisValli, RoxWatch ($4,25, dec 2025, 1.000+). Padelero, Padel & Tenis Score ($4,99, dec 2025, 1.000+, maker met één app).
  - Een eerlijke ondergrens voor zo'n app: 1.000 x $3 x 0,85 = ±$2.500 bruto in 3 tot 10 maanden (GOK, aangenomen dat alle downloads betaald waren).
- **Het nadeel: eerst gratis, dan betaald.** Bij spelletjes zie je in de reviews dat de app gratis begon en later geld ging kosten (Stack van MangoIQ: "2 days ago this game is for free", Crossy Road 3D, Google Dinosaur Game, Simon van garminland). Bij die apps zijn de downloads dus geen verkopen. Bij de sport- en meetapps hierboven vond ik zulke klachten niet. Dit is niet met zekerheid te meten; zie "Nog te meten".

## Drukte (GEZIEN)
- Nieuwe apps per maand (eerste goedkeuring): ±800 tot 1.000 in 2025, ±1.300 tot 1.700 in de eerste helft van 2026, en een sprong naar ±4.050 in sep en ±2.800 in okt 2026. Het grootste deel zijn wijzerplaten van fabrieken. Makers op het forum klagen al over "spam" van wijzerplaten (DERDEN, forumdraden 351765 en 375973).
- Apps en datavelden samen: ±230 per maand in mei tot aug 2026. Dat is rustig.

## Vindbaarheid
- In de winkel (op telefoon en web) zijn lijsten voor nieuw, populair, trending en "hot & fresh", plus categorieën en zoeken op trefwoord (GEZIEN in de code van de winkel).
- Zoeken op sport werkt: niche-apps voor Hyrox, padel, pickleball, rucking en skiën scoren hoog. Garmin-gebruikers zoeken naar een functie die hun horloge mist.
- Downloads worden alleen als emmer getoond, dus een nieuwe app ziet er snel net zo "populair" uit als een oude (100+).

## Past het bij ons
- De taal is Monkey C met de SDK van Garmin. Een kleine app of een dataveld is in 1 tot 2 weken te bouwen (GOK). Het lastige is testen op veel horlogemodellen; de simulator in de SDK helpt.
- Geen eigen server nodig voor een simpel dataveld.
- Nadelen: $100 per jaar vooraf (geld, dus Thijs beslist). Klachten op het forum over trage uitbetaling en Nederlandse betaalkaarten die niet in Garmin Pay passen (DERDEN, forum, maker beva). Betalen werkt alleen op nieuwere horloges (DERDEN, forum, zmullett).

## Eerste idee wat we zouden bouwen
Een betaald dataveld of app voor een sport of training waar Garmin zelf niets voor heeft, zoals Multipassionate deed met Hyrox en padel. Prijs $3 tot $8. Kandidaten om eerst te toetsen op aanbod in de winkel: wedstrijdvormen die snel groeien (Hyrox-achtige races, padel, pickleball, rucking), of een meetwaarde die mensen nu op hun telefoon zoeken. Eerst met de winkel-API kijken welke zoekwoorden weinig apps hebben.

## Voor en tegen
Voor:
- Winkel zelf meetbaar, betalen gaat via de winkel, 85% voor de maker.
- Gratis apps en datavelden van kleine makers: mediaan 100+, 64% haalt 100+ in 3 tot 6 maanden. Betaald: mediaan 10+, 44% haalt 100+.
- Een kleine groep sportapps van nieuwe makers ($3 tot $8,49) haalt 1.000+ als betaalde app in 2026 (gekozen op succes: 11% van de nieuwe betaalde apps).
- Weinig concurrentie buiten de wijzerplaten.

Tegen:
- Downloads alleen in emmers, en "eerst gratis, dan betaald" maakt het geld per app onzeker.
- Maar één maker met openbare verkoopcijfers (Ski Pin, 68 in de eerste maand).
- $100 per jaar en 15%.
- Lage prijzen (mediaan $2,25). Voor € 350 per maand zijn ±140 verkopen per maand van $3 nodig, of ±50 van $8,49 (GOK, rekensom met 15% afdracht).
- Veel horlogemodellen om op te testen.

## Nog te meten (voor de proef of erbij)
1. Elke week (3 tot 4 weken) per betaalde app het verloop van de download-emmer volgen (elke week de API lezen). Komt een app van 100+ naar 1.000+ terwijl hij betaald is, dan weten we dat het verkopen zijn. Dit kan de volgende verkennerrun doen.
2. Twee makers zoeken die hun maandbedrag delen (forum, Reddit r/Garmin, de CIQ-Dash-tool van Charlie).
3. Per zoekwoord tellen hoeveel apps er al zijn, om een gat te vinden.

## Bronnen
- Winkel-API: https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps
- Ski Pin: https://forums.garmin.com/developer/connect-iq/f/showcase/430838/i-monetized-my-ski-app-here-s-what-happened
- $100 en 15%, debitkaarten: https://forums.garmin.com/developer/connect-iq/f/discussion/426202/connect-iq-monetization-system-vs-own-payment-system---increase-in-sales
- Betalen vóór downloaden: https://forums.garmin.com/developer/connect-iq/f/discussion/397942/is-anybody-doing-well-from-the-new-merchant-system
- Gebruikers: https://the5krunner.com/2026/05/01/garmin-connect-users-2026/
