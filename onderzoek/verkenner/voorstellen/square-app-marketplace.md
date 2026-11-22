# Square App Marketplace (kassasysteem van Block)

Verkenner Vera, 9 nov 2026, run 17:31 (Amsterdam). Aanleiding: de les van Clover (kassasystemen hebben soms een open app-API).

## Advies: nee. Cijfer 1.

De winkel is dicht voor nieuwe makers. Square neemt sinds medio 2026 geen nieuwe app-partners aan voor een vermelding, en de documentatie over de marketplace is offline. Ook los daarvan is het een kleine, stille winkel van bekende bedrijven waar nieuwe apps vrijwel geen reviews krijgen. Nederland is geen Square-land, dus geld innen via Square kan Thijs niet.

## Cijfers

### Eigen meting (GEZIEN)
De open API achter de winkel (`/app-marketplace/api/partner_application_categories/<categorie>`, robots.txt staat dit pad toe) gelezen voor de VS: alle 17 categorieën, 396 apps, met publicatiedatum (`enabled_at`), aantal reviews, gemiddelde en prijs. Script `data/square-haal-script.py`, data `data/square-apps-us-2026-11-09.jsonl`. Installaties toont de API niet.

- **Drukte:** nieuwe apps per jaar in de VS: 2021 69, 2022 56, 2023 42, 2024 56, 2025 35, 2026 tot nu 12. Van nov 2025 t/m apr 2026 maar 6 nieuwe apps. Het aantal daalt.
- **Wie er nieuw bijkomt:** in 2026 onder meer Olo, Google Business Profile, Apple Business, Resy (Tock), Rise.ai, vivenu. Grote of bekende bedrijven, geen kleine makers.
- **Bereik nieuwe apps:** reviews per app naar startjaar, mediaan: 2021 2, 2022 1, 2023 0, 2024 0, 2025 0, 2026 0. Van de 24 apps sinds mei 2025 hebben er 3 vijf of meer reviews (QuickBooks Online 206, Stream 34, Gravity Forms 7). In 2026 heeft geen enkele nieuwe app er 5. Van de 12 apps uit 2026 hebben er 11 nul reviews.
- **Prijs:** bij 100 van de 396 apps staat een prijssoort, meest een maandabonnement (60).
- Een forumbericht van een Square-medewerker van 1 okt 2026 zelf nagelezen via het forum (zie onder): onboarding voor nieuwe vermeldingen is gepauzeerd.

### Bronnen (DERDEN, onderzoeker)
- Square neemt geen nieuwe partners aan: medewerker op 8 sep 2026, "Square is not accepting new formal App Partner partnerships at this time", https://developer.squareup.com/forums/t/app-partner-application-submitted-aug-20-no-confirmation-till-now/27517 ; 1 okt 2026 "we have currently paused onboarding new apps/partners for listing", https://developer.squareup.com/forums/t/listing-square-apps-marketplace/28043 (door mij nagelezen); juli 2026, https://developer.squareup.com/forums/t/app-submission-where-how/26982
- Volgorde nu: partneraanvraag, getekend contract, dan pas een vermelding indienen en QA: https://developer.squareup.com/forums/t/clarification-on-square-app-marketplace-submission-process-for-existing-integration/28402
- Een aanvrager met 10+ restaurants in productie kreeg maanden geen antwoord: https://developer.squareup.com/forums/t/submitted-app-partner-application-01-24-2026-and-no-reponse/26101
- De docs onder developer.squareup.com/docs/app-marketplace geven een 404 (onderzoeker met curl).
- Zonder vermelding live gaan mag wel, zonder plafond, maar dan geen etalage en geen startknop in Square: zelfde bron 28402 en https://developer.squareup.com/forums/t/can-a-private-square-appointments-pilot-have-a-launch-link/28036
- App Subscriptions (Square rekent af) was alleen voor ontwikkelaars uit de VS: https://developer.squareup.com/forums/t/app-subscription/19043 . Percentage voor Square nooit openbaar.
- Square werkt in 8 landen (VS, VK, Canada, Australië, Japan, Frankrijk, Spanje, Ierland), niet in Nederland: https://developer.squareup.com/docs/build-basics/international-development
- Ruim 4,5 miljoen verkopers in 2025 (Block 10-K): https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm
- Bouwen en testen kan zonder hardware in de gratis sandbox: https://developer.squareup.com/docs/devtools/sandbox/overview
- Geen verdiencijfers van kleine makers met een Square-app gevonden.

## Langs de vier punten van een 8
1. Nieuwe kleine makers verdienen: niet te zien en niet aannemelijk; nieuwe apps zijn van bedrijven en krijgen geen reviews. Zwak.
2. Bereik voor nieuwkomers: de etalage is dicht voor nieuwe partners. Zonder vermelding moet je alle klanten zelf vinden. Zwak.
3. Bouwen en testen: kan, web-app met OAuth en sandbox. Sterk.
4. Thijs kan binnen een week verkopen: nee. Geen vermelding mogelijk, geen Square-account in Nederland, dus afrekenen via Stripe of Polar en zelf klanten werven in de VS. Zwak.

## Voordelen
- Grote groep winkeliers (4,5 miljoen) die gewend is per maand voor apps te betalen.
- Open API's en een goede sandbox.

## Nadelen
- Winkel dicht voor nieuwe partners, zonder termijn.
- Weinig en dalende nieuwe aanvoer, vooral grote merken.
- Nieuwe apps vrijwel zonder reviews.
- Nederland is geen Square-land.

## Eerste idee (alleen als de winkel ooit opengaat)
Een kleine web-app voor Amerikaanse winkeliers bovenop de Square-API's (bijvoorbeeld rapporten of voorraadmeldingen), verkocht per maand. Nu niet zinvol.

## Herhaalmeting
Geen vaste datum. Alleen opnieuw kijken als Square meldt dat onboarding voor de marketplace weer open is (forum of developer.squareup.com/docs/app-marketplace weer bereikbaar). Dan `python3 -I data/square-haal-script.py US en uit.json`.

## Nagekeken
Geen aparte controleur-agent: de kern (winkel dicht) heb ik zelf in het forum nagelezen, en de telling komt rechtstreeks uit de API. Wat niet te meten was: installaties per app, de officiële eisen (docs offline), verdiensten.
