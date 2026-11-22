# Voorstel: Wix App Market (apps voor Wix-sites)

**Advies: nee voor nu. Cijfer: 3 van 10.** De voorwaarden zijn gunstig (het eerste jaar houdt de maker 100%, daarna 80%, betalen via Wix), maar Wix toont geen installs, nieuwe apps krijgen bijna geen reviews, en ik vond geen enkele kleine maker die aantoonbaar geld verdient met een Wix-app. Sinds augustus 2026 keurt een AI nieuwe apps binnen minuten goed, en er zijn tekenen dat er sindsdien veel meer nieuwe apps bijkomen. Geschreven op 7 nov 2026, run 13:31. Nagekeken door de controleur (akkoord, 8 correcties verwerkt).

## Wat ik zelf mat
- Met `data/wix-haal-script.py` alle 64 lijstpagina's gelezen (56 subcategorieën en 8 collecties zoals Newest, Staff picks en Popular this month) (openbare HTML, de data staat als base64 in de pagina). Per subcategorie toont de pagina de eerste 48 apps en het totaal. Samen **1.818 verschillende apps** gezien. Opgeteld totaal van de 56 subcategorieën 3.420 (1.773 uniek op 1.886 getoonde plaatsen); met die overlap schat ik de hele winkel op **±3.200 apps** (GOK op GEZIEN). Wix zegt zelf nog "meer dan 800": verouderd. Uitkomst in `data/wix-subcategorieen-2026-11-07.json`.
- Met `data/wix-reviewdata-script.py` van alle 418 apps met 1 tot 5 reviews de app-pagina gelezen. Een pagina toont de 5 nieuwste reviews met datum, dus bij deze apps is de oudste getoonde review de eerste. Uitkomst in `data/wix-apps-1tot5-reviews-2026-11-07.jsonl`, tellen met `data/wix-analyse-script.py`. GEZIEN
- **Meetgrenzen:** Wix toont geen installs en geen publicatiedatum, alleen reviews. De interne API van Wix mocht niet (geweigerd), de lijst "Newest apps" toont alleen de eerste 48. De 1.818 zijn de eerste 48 per subcategorie, dus scheef naar populaire apps. Eén app (rise-app) heeft 5 reviews maar toont er 4, daar klopt de eerste datum misschien niet (verwaarloosbaar); de ontbrekende ±1.400 hebben waarschijnlijk nog minder reviews.

## Cijfers

**Bereik (alleen reviews, installs niet te zien)**
- Gezien deel van de winkel (n=1.818): mediaan **2 reviews**, 37% heeft 0, 34% 10+, 11% 100+. GEZIEN, scheef naar populair. Alleen de 56 subcategorieën (zonder collecties, zo telt `data/wix-analyse-script.py` nu): n=1.773, mediaan 3, 36% heeft 0. GEZIEN
- Apps met een eerste review in mei tot aug 2026 (2 tot 6 maanden geleden) en nu hooguit 5 reviews: n=69, waarvan 31 met 1 review en 5 met 5. GEZIEN. Apps uit die maanden met 6+ reviews en nieuwe apps zonder enige review zitten hier niet in, dus dit is geen mediaan van alle nieuwe apps. Let op: 19 van de 69 komen van PURPLE en PurpleBear, en 5 van Certified Code, dus de groep is niet breed.
- De lijst "Newest apps" (306 apps): alle 48 getoonde hebben **0 reviews**. GEZIEN
- Hoeveel installs bij een review horen is op Wix niet bekend. Bij Shopify was het ±7 tot 13 (eigen meting 7 nov). Daarmee zou een nieuwe app met 1 tot 2 reviews ±10 tot 25 installs hebben. GOK
- Eén maker (V-Blog) meldde mei 2026 dat zijn beste apps van "100+ installs per maand" naar 0 tot 10 gingen toen Wix Harmony kwam, waar zijn Blocks-apps niet op werken. DERDEN, niet geverifieerd: [Wix forum](https://forum.wixstudio.com/t/whats-the-future-of-wix-cli-app-builders-with-ai-app-builder-in-pipeline/77981)
- Gebruikers: 304 miljoen geregistreerd, 6,11 miljoen premium-abonnementen eind 2025 (incl. Base44). DERDEN: [Wix jaarcijfers 2025, SEC](https://www.sec.gov/Archives/edgar/data/1576789/000162828026014406/fourthquarterandfullyear20.htm)

**Geld**
- Betalen gaat via Wix Billing (abonnement, gebruik, eenmalig, proefperiode). Wix houdt 20% in na 2,5% transactiekosten en btw; in het eerste jaar houdt de maker 100%. Uitbetaling maandelijks vanaf $200. DERDEN: [Wix FAQ](https://dev.wix.com/docs/build-apps/launch-your-app/pricing-and-billing/payments-and-billing-faqs), [aankondiging juli 2024](https://www.prnewswire.com/news-releases/wixs-devstudio-conference-reveals-new-features-that-empower-developers-to-build-applications-for-the-wix-app-market-302186388.html)
- Prijsvormen in de gezien 1.818: 901 gratis plan plus betaald, 358 proefperiode, 277 gratis, 185 gratis te installeren, 95 abonnement, 2 eenmalig. GEZIEN. Van de 69 nieuwe apps hierboven vragen er 14 meteen geld (proef of abonnement). GEZIEN
- **Geen enkele kleine maker gevonden met een bedrag.** TrustMRR heeft geen startup met een Wix-app als bron, Indie Hackers en Reddit gaven geen cijfers. DERDEN (zoektocht onderzoeker 7 nov)

**Drukte**
- ±3.200 apps (GOK op GEZIEN). Eerste reviews per maand bij apps met 1 tot 5 reviews: mei 14, juni 10, juli 15, aug 30, sep 28, okt 60, nov (half) 11. Let op: oudere apps die inmiddels 6+ reviews hebben vallen weg, dus de stijging is deels een meeteffect en een bovengrens. Ze past bij de AI-keuring sinds augustus 2026 ("uitslag binnen minuten"), maar bewijst die vloed niet. GEZIEN / DERDEN: [forum nieuws](https://forum.wixstudio.com/t/dev-partner-news-ai-app-market-review-verified-apps-ai-credits-api-and-more/79179)
- In de 48 nieuwste apps komt één bedrijf (Stable Growth LLC) 15 keer voor met kleine widgets (back-to-top, breadcrumbs, countdown). Dat lijkt massaproductie. GEZIEN
- Wix bouwt een AI App Builder; makers vrezen kopieën van hun apps. DERDEN: forumdraad hierboven

**Vindbaarheid**
- Zoeken, categorieën en collecties zoals Newest apps, Staff picks, Popular this month, Made by Wix en Apps on Sale. GEZIEN. Eigen promotie door de maker: e-mail, kortingsbonnen, eigen sales, reviews vragen. DERDEN: [Wix docs](https://dev.wix.com/docs/build-apps/launch-your-app/app-promotion/self-promotion/best-practices-for-app-promotion.md). Wix-apps staan prominent; de eerste 48 per categorie zijn vooral oude apps met veel reviews (GEZIEN).

**Past het bij ons**
- Bouwen met de Wix CLI (React, TypeScript, Node.js). DERDEN: aankondiging hierboven. In 1 tot 2 weken een app: GOK. Thijs moet een Wix-ontwikkelaarsaccount aanmaken.
- Risico: Wix verandert het platform plots; volgens één maker zakten zijn Blocks-apps in toen Harmony kwam. DERDEN, één bron

## Voor
- Eerste jaar 0% afdracht, daarna 20%, en betalen zit ingebouwd.
- Groot publiek van betalende sitebezitters (6 miljoen premium).
- Snelle AI-keuring.

## Tegen
- Bereik niet te meten: geen installs, alleen reviews, en nieuwe apps krijgen er bijna geen.
- Geen enkel geldbewijs van een kleine maker.
- Sinds aug 2026 waarschijnlijk veel meer nieuwe apps (306 in de lijst Newest), deels massaproductie.
- Wix bouwt zelf concurrentie (eigen apps, AI App Builder) en verandert het platform zonder waarschuwing.

## Eerste idee (als het ooit ja wordt)
Een kleine betaalde app die een verplichting oplost voor Wix-winkels (zoals de EU-herroepknop of het garantielabel, zie Shopify), met een gratis plan. Maar dat bestaat hier al: PurpleBear heeft een "EU withdrawal button" in de nieuwste apps.

## Wat het van nee naar ja zou brengen
- Een maker die echte installs of omzet van een nieuwe Wix-app deelt (boven $300 per maand).
- Wix die installs gaat tonen, dan kan het bereik gemeten worden. Herhaalmeting met de scripts in `data/` over 4 weken laat zien hoeveel reviews de nieuwe apps van nu halen.
