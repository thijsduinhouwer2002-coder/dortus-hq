# FlutterFlow Marketplace (betaalde app-sjablonen, UI-kits en libraries)

Vera, 15 nov 2026 (run 11:31 Amsterdam). Controleur: een aparte agent, deels akkoord, correcties verwerkt.

## Wat het is
FlutterFlow is een visuele app-bouwer (Flutter). In de winkel marketplace.flutterflow.io verkopen makers sjablonen (volledige apps en UI-kits), libraries en losse pagina's. Kopers voegen een item met één klik toe aan hun FlutterFlow-project. FlutterFlow rekent af via Stripe.

## Hoe gemeten
- De winkel is een Flutter-webapp. In Playwright gekeken welke verzoeken hij doet: hij leest de openbare Firestore-collectie `marketplace_items` (project flutterflow-io-6f20), zonder inlog. Alle 3.228 items daaruit opgehaald, alleen de velden die de winkel ook toont (naam, soort, status, prijs, aantal keer toegevoegd, datums, ratings). Rustig, 11 verzoeken. Geen andere collecties gelezen.
- Data: `data/flutterflow-marketplace-items-2026-11-15.json`. Scripts: `data/flutterflow-haal-script.py` (ophalen) en `data/flutterflow-tel-script.py` (tellen). Let op: het telscript telt bij de ratings ook `total_count` mee, dus de ratings daarin zijn dubbel; de getallen in dit voorstel zijn gecorrigeerd.

## Cijfers
- 3.228 items, waarvan 1.934 gepubliceerd: 1.640 sjablonen, 228 libraries, 66 losse pagina's. 1.405 betaald, 529 gratis (GEZIEN).
- Drukte: ±20 tot 120 nieuw gepubliceerd per maand, in 2026 meestal 50 tot 120 (GEZIEN).
- Prijs: minimum $50 voor UI-kits en libraries, $400 voor volledige apps (DERDEN, docs.flutterflow.io/marketplace/creators-hub/submitting-an-item-for-review, bijgewerkt 26 okt 2026). 1.041 betaalde items staan op precies $50 (GEZIEN). Mediaan $50.
- Afdracht aan FlutterFlow: niet openbaar. De voorwaarden verwijzen naar "Pricing and Payment Terms" (flutterflow.io/tos-marketplace) en makers vragen op het forum vergeefs naar het percentage (DERDEN, community.flutterflow.io, "FlutterFlow Marketplace Financial Aspects").

### Valkuil in de teller
Het veld "keer toegevoegd" telt ook toevoegingen uit een tijd waarin een item gratis of anders geprijsd was. 685 betaalde items kregen hun prijs meer dan 7 dagen na aanmaak, 424 daarvan staan nu op $50; de prijswijzigingen komen in golven (okt 2025, jun, aug en okt 2026), dus waarschijnlijk regels van het platform (GEZIEN). Wie alle betaalde items gewoon vermenigvuldigt (toegevoegd keer prijs) komt op $2,8 miljoen bruto; dat is dus te hoog. Het eerlijke beeld ligt tussen een strenge en een ruime telling.

### Bereik en geld van nieuwe betaalde items (aangemaakt nov 2025 t/m mei 2026, dus 6 tot 12 maanden oud)
| Telling | Items | Mediaan keer toegevoegd | Haalt 10+ | Samen bruto |
|---|---|---|---|---|
| Streng (prijs binnen 7 dagen na aanmaak gezet) | 195 | 0 | 2% | $11.479 |
| Drempel 30 dagen | 222 | 0 | 6% | $29.629 |
| Drempel 90 dagen | 239 | 0 | 10% | $38.819 |
| Alle betaalde (te hoog, zie boven) | 326 | 1 | 21% | $168.447 |
(GEZIEN; drempelvarianten van de controleur.)

Dus: **2 tot 10% van de nieuwe betaalde items haalt 10 verkopen** (bij $50 is dat ±$500 bruto in 6 tot 12 maanden), de middelste nieuwe maker verkoopt niets. Eén oudere lichting (jan t/m okt 2025, streng): mediaan 1, 9% haalt 10+.
- Makers in de strenge set: 84, mediaan $200 bruto in totaal, 7 boven $5.000 (GEZIEN). Eén maker zette op 13 en 14 nov 2026 104 items online die elk precies evenveel 5-sterrenratings als toevoegingen hebben; dat ruikt naar eigen of nep-aankopen en telt niet mee.
- num_times_added is niet zeker gelijk aan kopen: eigen tests en terugbetalingen zijn niet te zien (GOK dat het dicht bij kopen ligt, want toevoegen vraagt bij betaalde items afrekenen).

## Vindbaarheid
Winkel in FlutterFlow zelf en op de website, sorteren op populariteit, rating, prijs en datum. Geen teken van uitlichting voor nieuwkomers. Het publiek is beperkt tot FlutterFlow-gebruikers; FlutterFlow duwt zelf steeds meer naar bouwen met AI ("Building by describing your app?" in de docs), wat de vraag naar kant-en-klare sjablonen eerder kleiner dan groter maakt (GOK).

## Past het bij ons
Slecht. Bouwen gebeurt in de visuele editor van FlutterFlow, met een account (en voor publiceren een betaald plan) van Thijs; onze Claudes kunnen daar niet zelf in werken of testen. Onderscheiden met 3D of simulators past niet bij UI-kits.

## Voor en tegen
- Voor: echte kassa, prijzen vanaf $50, een handvol makers verdient duizenden dollars.
- Tegen: nieuwe betaalde items verkopen meestal niets (2 tot 10% haalt 10), afdracht geheim, golven van prijsverlagingen door het platform, nep-reviews zichtbaar, en we kunnen er niet zelf bouwen.

## Cijfer en advies
**Cijfer 2. Nee.** Geld bestaat, maar bij een paar oude makers; bereik voor nieuwkomers is bijna nul en het werk past niet bij hoe wij bouwen. Opnieuw kijken alleen als FlutterFlow een open API voor het bewerken van projecten zonder inlog van Thijs biedt en nieuwe items aantoonbaar beter verkopen.
