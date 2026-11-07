# Voorstel: Shopware Store (betaalde extensies voor Shopware 6)

Vera, 7 nov 2026, run 21:32. Nagekeken door een controleur (akkoord na 5 correcties, verwerkt).

**Advies: nee voor nu. Cijfer 3 van 10.**

## Wat is het
Shopware is Duitse webwinkelsoftware. In de Shopware Store huren winkels extensies. Shopware verkoopt, int en betaalt de maker uit. Sinds 28 dec 2023 kun je extensies alleen nog huren (per maand of per jaar), niet meer kopen, en elke betaalde extensie moet een gratis proefmaand hebben (DERDEN: [shopware.com/en/news/shopware-store-rental-licenses](https://www.shopware.com/en/news/shopware-store-rental-licenses), Extension Partner-voorwaarden art. 1.3.10).

## Meting (GEZIEN, eigen meting van alle pagina's)
- robots.txt staat alles toe. Sitemap: 10.957 URL's, 6.181 unieke extensies (varianten ...m en ...m12 samengevoegd; ...f zijn gratis). Elke pagina toont downloads (in emmers <10, <25, <50, <100, daarboven exact), publicatiedatum, prijs, reviews en partnerstatus.
- 77 pagina's zonder downloads en datum: 73 zijn "coming soon" (nog niet uit), 4 mislukte downloads. Niet meegeteld.
- **Drukte:** nog live en gepubliceerd in 2026: 920, in 2025: 299. Per maand in 2026 tussen 44 en 171 (okt). Let op: de sitemap toont alleen wat nog live is, dus het verschil 2025 tegen 2026 zegt niet zeker dat het groeit.
- **Bereik, lichting mei t/m aug 2026 (3 tot 6 maanden oud), zonder Shopware zelf:** 330 extensies, 282 (85%) onder 10 downloads, 6 (2%) met 100+. Betaald (huur): 276, waarvan 252 (91%) onder 10 en 6 met 100+. Mediaan maandprijs €9,90.
- **Lichting feb t/m apr 2026:** 230, 182 onder 10, 8 met 100+ (3%).
- **Ouder, betaalde Shopware 6-extensies uit 2024 (12+ maanden):** 235, 107 onder 10, 7 met 100+ (3%).
- Het getal downloads telt zeer waarschijnlijk de gratis proefmaand mee (niet bevestigd door Shopware). 100 downloads is dus geen 100 betalende winkels.
- **Alle 6 uitschieters uit mei t/m aug** zijn extensies voor nieuwe EU-wetten: de herroepingsknop (vanaf 19 juni 2026) en het GARAN-garantielabel. 4 van 6 komen van partners die sinds 2014 tot 2017 bestaan, 1 van een partner sinds 2021 (Fishnet, een Shopware 5-extensie). Uitzondering: Kommora, partner sinds 2026, 26 extensies, beste 144 downloads tegen €7,42 per maand. In feb t/m apr: J&G Agency (partner sinds 2025), herroepingsknop, 669 downloads tegen €7,99 per maand. Dat is het beste teken dat een nieuwe maker met een wetgolf geld kan halen; hoeveel van die 669 betalen is onbekend.
- Data: `data/shopware-alle-2026-11-07.jsonl`, `data/shopware-lichting-feb-aug-2026-2026-11-07.jsonl`, scripts `data/shopware-haal-script.py`, `shopware-prijs-script.py`, `shopware-analyse-script.py`. Het veld "maand" in het bestand met alle extensies is onbruikbaar (staat overal aan); gebruik het prijsblok uit de lichting.

## Geld en regels (DERDEN)
- Shopware houdt **25%** in (Extension Partner-voorwaarden versie 5.6, art. 2.1.2: [pdf](https://api.shopware.com/documents/producerContract/versions/5.6/en_GB.pdf)). Uitbetaling maandelijks, alleen naar een EU/EER-rekening. Geen instapkosten gevonden; certificering (Bronze, Silver, Gold) is optioneel en betaald.
- Support verplicht: reageren binnen 4 werkdagen, oplossen binnen 6, anders kan de extensie uit (art. 1.3.11).
- Keuring: automatisch plus een mens. Forum mei 2026: wachtrijen van 30 tot 40 dagen, een maker noemt 6 maanden van start tot live, QA overbelast ([forum](https://forum.shopware.com/t/shopware-pluginpruefung/109050)). Na drie mislukte tests tot 12 weken blokkade. Geen AI-regels gevonden.
- Geen enkele kleine maker gevonden die een bedrag noemt.
- **Markt krimpt licht:** 29.931 live winkels (StoreLeads, 30 okt 2026, -3% op jaarbasis, top 37.814 in 2023: [storeleads.app/reports/shopware](https://storeleads.app/reports/shopware)); BuiltWith 25.958 op Shopware 6 ([trends.builtwith.com](https://trends.builtwith.com/shop/Shopware-6)). Ter vergelijking: Shopify heeft miljoenen winkels.

## Voordelen
- Echte betaling via de winkel, terugkerende huur, 75% voor de maker.
- Alles is meetbaar, ook later opnieuw.
- Wetgolven werken: een nieuwe EU-regel geeft een korte periode waarin ook een nieuwe partner (J&G Agency) honderden downloads haalt.
- Duitstalige markt, weinig concurrentie van grote Amerikaanse makers.

## Nadelen
- Bereik zwak: 85 tot 91% van de nieuwe extensies blijft onder 10 downloads, ook na een jaar haalt maar 3% de 100.
- Kleine en krimpende markt (±30.000 winkels).
- Keuring traag (weken tot maanden), strenge supportplicht; een wetgolf is voorbij voor je live bent.
- Bouwen vraagt PHP/Symfony en een testwinkel; prima te doen, maar elke update gaat opnieuw door de keuring.

## Wat we zouden bouwen (als het ooit ja wordt)
Een extensie voor een aankomende EU-regel, minstens 3 maanden voor de datum live. Dezelfde wetgevingskalender als bij Shopify (zie taken.md: Franse e-factuur 1 sep 2027, EUDR 30 jun 2027) kan beide winkels bedienen.

## Wat dit oordeel verandert
Een aankomende wet met datum waarvoor nog geen sterke Shopware-extensie bestaat, minstens 4 maanden vooruit. Of bewijs dat kleine makers zonder wetgolf €300+ per maand halen.
