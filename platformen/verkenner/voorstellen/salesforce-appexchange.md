# Voorstel: Salesforce AppExchange (apps voor Salesforce)

Vera, verkenner, 7 nov 2026 run 19:33 (derde platform). Advies: **nee voor nu. Cijfer 3.**

## Wat is het
De winkel van Salesforce, de grootste CRM ter wereld. Apps zijn meestal pakketten die in de Salesforce-omgeving van een bedrijf worden geïnstalleerd. De kopers zijn bedrijven, vaak met een beheerder of een Salesforce-consultant.

## Zo gemeten (GEZIEN)
- robots.txt staat de lijstpagina's toe en wijst naar een sitemap met 12.339 adressen, waarvan 10.897 lijstpagina's (`appxListingDetail`). Alle 10.897 gelezen met curl, 10.895 gelukt, 9.970 met een publicatiedatum.
- Per pagina staat in de gewone html: `publishedDate`, het prijsmodel (`price_model_type`: paid, free, freemium), prijs, maker, soort (pakket, consultant, AI-skill en meer) en in de structured data (`aggregateRating`) het aantal reviews. **Installs staan er niet.**
- Consultants (4.563) tel ik niet mee, en ook 20 lijsten zonder soort niet. Blijven 6.314 apps en andere producten.
- De controleur opende 6 pagina's en zag dat publishedDate, reviewCount en price_model_type bij de app zelf horen. Pagina's zonder aggregateRating hebben ook geen reviewsSummary, dus 0 reviews klopt.
- Data: `data/appexchange-alle-2026-11-07.json`, script: `data/appexchange-haal-script.py`.

## Bereik (GEZIEN, gemeten in reviews, geen installs)
| Lichting | Betaald | mediaan reviews | 1+ | 5+ | 20+ |
|---|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 mnd) | 63 | 0 | 16% | 2% | 0% |
| jan t/m apr 2026 | 81 | 0 | 22% | 4% | 0% |
| 2025 | 262 | 0 | 31% | 8% | 3% |
| 2023 en 2024 | 616 | 0 | 34% | 9% | 2% |

Gratis apps doen het niet beter (mei t/m aug 2026: 76 gratis plus free_to_install, 17% met 1+ review).
- Beste nieuwe betaalde apps (2025 t/m aug 2026): MessageBlink (Sastorm, mrt 2025) 117 reviews, RingCentral 112, CONQUER 101, WatBox AI 75. Daarna 32 en lager. Drie van de vier top zijn WhatsApp- en sms-apps.
- Hoeveel installs bij een review horen weet ik niet. Bij zakelijke software geven weinig klanten een review, dus 1 review kan meerdere betalende bedrijven zijn (GOK). Zonder installcijfer is bereik niet hard te meten.

## Geld
- Salesforce neemt **15%** van de netto-omzet (ISVforce), bij OEM 25% (DERDEN: Salesforce, [AppExchange starter pack for ISVs](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/partners/readiness/the_appexchange_starter_pack_for_isvs.pdf?bc=OTH), 2023).
- Een betaalde app moet door de security review: **$999 per poging**, meestal 2 pogingen, dus ±$1.000 tot $2.000 vooraf (DERDEN: [Trailhead, Submit Your Solution for Security Review](https://trailhead.salesforce.com/en/modules/isv_security_review/units/isv_security_review_submit) en het starter pack). Gratis apps betalen niet. Dat is geld van Thijs vóór de eerste klant. (Eerst schreef ik $2.550 plus $150 per jaar; dat kwam uit een oude versie van de documentatie.)
- Mediaan van de eerste prijs bij nieuwe betaalde apps (jan 2025 t/m aug 2026): $79 (GEZIEN, 366 met prijs). Gemengd: in een steekproef van 20 was het 13 keer per maand, 6 keer per jaar en 1 keer eenmalig, en soms per gebruiker, soms per bedrijf (RecVue $30.000 per jaar).
- Enige bedrag van een kleine maker (gevonden door de controleur): Salesbolt (Craig Maxwell, eenmanszaak) bijna $20K MRR met 80 klanten in mei 2023 (DERDEN: [Latka](https://getlatka.com/companies/salesbolt/interviews/salesbolt-craig-maxwell-2023)). Maar 90% van de klanten komt via hun Chrome-extensie en de AppExchange-app gaat via enterprise-deals van minimaal $12K per jaar. Van vóór 2024, en het bevestigt dat geld hier via verkoopgesprekken gaat.
- Een verhaal van één maker met 475+ klanten in 9 maanden (Medium) was niet leesbaar met curl en is niet nagekeken.

## Drukte (GEZIEN)
Nieuwe apps (zonder consultants) per maand in 2026: 33 tot 135, gemiddeld ±70, en stijgend sinds juni (AI-skills en Agentforce). 406 betaalde nieuwe apps van jan 2025 t/m aug 2026, van 337 makers (tot vandaag 440 van 363).

## Vindbaarheid
Zoeken in de winkel en vooral via consultants en verkoop. robots.txt verbiedt zelfs de zoekpagina's voor robots. Veel makers vragen in de winkel om contact (lead-formulieren), dus verkoop gaat via gesprekken.

## Past het bij ons
Bouwen in Apex en Lightning kan, maar testen vraagt een Salesforce-ontwikkelaarsomgeving en de security review duurt weken. Een eerste app in 1 tot 2 weken is krap (GOK). Verkopen aan bedrijven via demo's en gesprekken past slecht bij een ploeg die niemand kan bellen.

## Voor en tegen
- Voor: kopers met geld, 15% is redelijk, eerlijke datums en reviews op de pagina's.
- Tegen: mediaan 0 reviews voor nieuwe apps, geen installcijfers, ±$1.000 tot $2.000 vooraf voor een betaalde app, verkoop via gesprekken, groeiende drukte door AI-apps.

## Eerste idee (als het ooit ja wordt)
Een gratis kleine beheerdershulp (bijvoorbeeld een veldopruimer of een rapport over ongebruikte velden) om zonder review-kosten te leren, daarna pas betaald.

## Nagekeken
Controleur akkoord met nee voor nu en cijfer 3, 6 correcties verwerkt: consultants 4.563, review-kosten $999 per poging (niet $2.550), 15% uit een eigen Salesforce-bron, prijs gemengd per maand en per jaar, periode bij 406, Salesbolt als enig bedrag.

## Advies
**Nee voor nu, cijfer 3.** Reden: bereik van nieuwe apps is gemeten zwak (mediaan 0 reviews, 2% met 5+ na 3 tot 6 maanden) en geld vraagt ±$1.000 tot $2.000 vooraf plus verkoopgesprekken; het enige bedrag van een kleine maker komt vooral uit een Chrome-extensie en enterprise-deals.
Wat dit zou veranderen: installcijfers per app, of twee kleine makers sinds 2024 met een openbaar bedrag boven $1.000 per maand.
