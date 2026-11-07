# Voorstel: BigCommerce App Marketplace

Vera, verkenner, 7 nov 2026 run 17:32 (lokale tijd, derde platform van de run). Advies: **nee. Cijfer 2.**

## Wat is het
De app-winkel van BigCommerce (webwinkelsoftware, nu onder de naam Commerce). Makers verkopen apps aan winkels, vaak met een maandprijs. Betalen via BigCommerce (unified billing) kan, maar is niet verplicht; veel winkels rekenen direct bij de maker af.

## Zo gemeten (GEZIEN)
- Alle 1.469 app-pagina's uit de openbare sitemap `/apps/sitemap-marketplace-apps.xml` (robots.txt staat dat toe). Per pagina uit de ingebedde JSON: createdOn, reviewCount, rating, prijsvelden, unifiedBilling. Script: `data/bigcommerce-haal-script.py`, analyse: `data/bigcommerce-analyse-script.py`, data: `data/bigcommerce-apps-2026-11-07.jsonl`.
- Installs staan nergens, dus de maat is reviews. De controleur zag op 6 pagina's dat reviewCount klopt.
- createdOn is de aanmaak van het record in het app-register, niet de livegang. De echte lancering kan maanden later liggen (controleur: Gorgias record mei 2022, koppeling aangekondigd aug 2022). De jongste lichting is dus jonger dan ze lijkt.
- 713 betaald (maand- of startprijs boven 0). 46 apps sinds 2025 noemen een bedrag in de tekst maar hebben lege prijsvelden en tellen niet als betaald. Dat verandert de medianen niet.

## Bereik (GEZIEN, reviews)
| Lichting (createdOn) | Soort | Aantal | Mediaan reviews | 1+ | 5+ | 20+ |
|---|---|---|---|---|---|---|
| mei t/m aug 2026 | betaald | 40 | 0 | 15% | 2% | 0% |
| jan t/m apr 2026 | betaald | 39 | 0 | 28% | 0% | 0% |
| jul t/m dec 2025 | betaald | 37 | 0 | 24% | 3% | 0% |
| jan t/m jun 2025 | betaald | 31 | 0 | 48% | 6% | 0% |
| voor 2024 | alles | 1.032 | 1 | 53% | 26% | 10% |

- De 160 betaalde apps sinds 2025 hebben samen 90 reviews. Beste nieuwe app sinds 2025: Contact Form Builder, 11 reviews.
- Ter vergelijking: bij Shopify hoort bij een review ±7 tot 13 actieve installs (StoreCensus, zie `shopify.md`). Met die verhouding zit een gewone nieuwe BigCommerce-app op ±0 en de beste op ±100 (GOK). Reviews zijn hier een zwakke maat, want veel winkels rekenen buiten BigCommerce af.

## Geld
- 20% afdracht op publieke apps, unified billing is vrijwillig (DERDEN: [Commerce Partner Agreement](https://www.commerce.com/partner-agreement/change-summary/)). Maar 59 apps gebruiken unified billing, 38 daarvan sinds 2025 (GEZIEN).
- Mediaan maandprijs betaalde apps sinds 2025: $20 (GEZIEN).
- Geen bedrag van een kleine maker die alleen op BigCommerce zit. Dichtstbij: een bundel van 4 apps op Shopify en BigCommerce samen, ±$3.200 per maand, sinds 2020, zonder uitsplitsing (DERDEN: [Empire Flippers](https://empireflippers.com/listing/86627/)).

## Drukte (GEZIEN)
±5 tot 24 nieuwe apps per maand in 2025 en 2026. Weinig concurrentie, maar ook weinig kopers.

## Markt (DERDEN)
±41.200 live winkels in juli 2025, piek 48.231 eind 2019, ±6% minder per jaar, 67% in de VS ([Red Stag op basis van Store Leads](https://redstagfulfillment.com/how-many-bigcommerce-stores-are-there/)). Shopify heeft er miljoenen.

## Past het bij ons
Bouwen kan in 1 tot 2 weken (web-app met de BigCommerce-API). Maar het is een SaaS-app met eigen server en ondersteuning, voor een kleine, krimpende groep winkels.

## Voor en tegen
- Voor: hoge prijzen ($20 per maand), weinig nieuwe apps, 20% afdracht.
- Tegen: nieuwe betaalde apps mediaan 0 reviews en niemand 20+ sinds 2025, markt ±20 keer kleiner dan Shopify en krimpend, geen bedrag van een kleine maker.

## Advies
**Nee, cijfer 2** (de controleur vindt een 3 ook te verdedigen, het besluit blijft gelijk). Wat dit verandert: een app die we toch al voor Shopify bouwen, dan kan BigCommerce er als tweede winkel bij voor weinig extra werk. Alleen dan.

## Niet zelf gemeten
Installs en verkopen staan nergens. Echte livegang per app ook niet.

Nagekeken door een controleur (7 nov): akkoord, aanvullingen verwerkt (createdOn is registerdatum, 46 apps met bedrag in tekst, reviews zwakke maat, markt en afdracht met bron).
