# Voorstel: Apple Vision Pro, betaalde visionOS-apps

Vera, verkenner, 8 nov 2026 run 07:33 UTC. Advies: **nee. Cijfer 2.** Nagekeken door een controleur: 6 van 6 punten live gelijk, kleine nuances verwerkt.

## Waarom bekeken
Jong platform, Apple rekent af (15% voor makers onder $1 miljoen), weinig concurrentie, en in 2024 was 52% van de apps die alleen voor de bril zijn vooraf betaald (DERDEN, TechCrunch 12 feb 2024). Paste bij de vraag van Thijs naar plekken waar Dortus groot kan worden.

## Hoe gemeten
- **Zelf (GEZIEN):** 120 uitlichtpagina's van de visionOS-winkel (apps.apple.com/us/vision, collecties, verhalen, Arcade; robots.txt staat dat toe) gelezen: 553 apps, via de iTunes lookup-API nagekeken welke alleen op de bril draaien. Script in deze run, data `data/visionpro-uitgelicht-2026-11-08.json`.
- **Zelf geprobeerd, mislukt (GEZIEN):** (1) Ratings: Apple toont voor visionOS-apps op het web en in de lookup-API geen ratings, ook niet voor bekende apps als Synth Riders en YouTube for visionOS (overal 0 en "hasn't received enough ratings"). De review-RSS is ook leeg. (2) De zoek-API vindt apps die alleen voor de bril zijn niet. (3) Alle 495 new-app-sitemaps van apps.apple.com gelezen (90.594 id's, 74.546 in de VS, bijna alles uit okt en nov 2026) met `data/visionpro-haal-script.py`: daar zit geen enkele app voor de bril of de Mac in, alleen iPhone en iPad. Bereik en drukte zijn dus niet zelf te meten. Wel meetbaar zou het zijn met een betaalde dienst als Appfigures of Sensor Tower, of met omzetcijfers van een maker zelf.
- **Bronnen van derden** via een onderzoeker (verslag samengevat hieronder).

## Cijfers
| Wat | Cijfer | Label |
|---|---|---|
| Brillen verkocht sinds feb 2024 | ±600.000 (2024: 390.000; kw4 2025 met M5: ±45.000) | DERDEN (IDC via MacRumors 2 jan en 29 apr 2026, 9to5Mac 2 jan 2026) |
| Goedkopere bril | Vision Air geschrapt (okt 2025); lichtere opvolger op zijn vroegst eind 2028, categorie "on ice" | DERDEN (MacRumors 1 okt 2025, 11 mei en 1 jun 2026) |
| Actieve visionOS-apps | minder dan 1.900 eind jan 2025 (Apple noemde 2.500 in aug 2024) | DERDEN (Appfigures via CNBC 21 feb 2025) |
| Nieuwe apps per maand | 20 tot 45 sinds medio 2024, 36 in mrt 2026 | DERDEN (Appfigures via birchtree.me 15 apr 2026) |
| Uitgelicht: apps alleen voor de bril | 131 van 553; daarvan 101 uit 2024, 17 uit 2025, 12 uit 2026; 57 betaald | GEZIEN |
| Kleine makers uitgelicht | ja: Philipp Stollenmayer (Cueva de las Manos, $2,99, aug 2026), Roxana-Monica Nagy (Kooboori, $9,99, aug 2026) | GEZIEN |
| Geld kleine maker | Adam Roszyk, 17 apps (o.a. Night Vision $4): ±$4.000 in 3 maanden, ±$1.300 per maand samen | DERDEN (CNBC 21 feb 2025) |
| Andere bedragen van makers 2025/2026 | niets gevonden | GEZIEN (afwezig) |

## Voordelen
- Weinig concurrentie: 20 tot 45 nieuwe apps per maand, dus een goede app maakt kans op uitlichting, ook van een solo-maker (GEZIEN).
- Kopers betalen vooraf zonder morren, prijzen van $3 tot $10 zijn gewoon.
- Bouwen kan zonder bril met de simulator in Xcode (Mac met M-chip nodig, of een macOS-runner op GitHub Actions).

## Nadelen
- Heel weinig brillen (±600.000, deels in de kast) en tot minstens 2028 geen groei. Apple richt zich op een slimme bril.
- Enige openbare maker verdient ±$1.300 per maand met 17 apps; dat is per app ±$75.
- Bereik is niet te meten: Apple toont geen ratings voor visionOS-apps.
- Wij hebben geen bril om te testen; ruimtelijke apps zonder echte test zijn riskant. Ontwikkelaarsaccount van Thijs nodig ($99 per jaar).

## Eerste idee als we het toch deden
Een klein betaald hulpmiddel ($4 tot $6), zoals Roszyk doet: één venster met een nuttige functie (timer, notitie, meetlat). Beter als bijproduct van een iPhone- of iPad-app dan als los platform.

## Cijfer en advies
**Cijfer 2. Nee.** Er is weinig concurrentie, maar ook bijna niemand om aan te verkopen, en dat aantal groeit tot 2028 niet. Het enige geldsignaal is ±$75 per app per maand. Wat dit verandert: een goedkope Apple-bril met een datum, of openbare cijfers van meerdere kleine makers boven $1.000 per maand per app.

## Bronnen
- https://www.macrumors.com/2026/01/02/vision-pro-still-failing-to-catch-on/
- https://9to5mac.com/2026/01/02/m5-vision-pro-launch-likely-made-minimal-sales-impact-report/
- https://www.macrumors.com/2026/04/29/apple-vision-pro-m5-flop/ (tegengeluid: https://sixcolors.com/post/2026/04/the-vision-pro-not-quite-dead-yet/)
- https://www.macrumors.com/2025/10/01/apple-ai-smart-glasses-focus/
- https://www.macrumors.com/2026/05/11/new-vision-pro-wont-arrive-at-least-two-years/
- https://www.macrumors.com/2026/06/01/slimmer-lighter-apple-vision-pro-late-2028/
- https://www.nbcnewyork.com/news/business/money-report/apples-vision-pro-has-a-problem-a-year-into-its-existence-not-enough-apps/6158727/
- https://birchtree.me/blog/no-vibe-coded-visionos-bump/
- https://techcrunch.com/2024/02/12/over-half-of-vision-pro-only-apps-are-paid-downloads-far-more-than-wider-app-store/
