# Voorstel: Webflow Marketplace, betaalde templates

Vera, verkenner, 7 nov 2026 run 21:31. Advies: **nee voor nu. Cijfer 4.**

## Wat is het
Webflow is een websitebouwer. In de Marketplace verkopen makers kant-en-klare websites (templates) voor meestal $59 tot $129. Webflow rekent af en geeft de maker sinds 21 okt 2025 **95%** van de prijs, Webflow houdt 5% (DERDEN: [Webflow blog](https://webflow.com/blog/template-creator-enhancements), ook zo in de [creator agreement](https://webflow.com/legal/creator-agreement), alleen voor aankopen via de Marketplace). Eerder (5 en 6 nov) stond Webflow bij "zwak of te klein", toen alleen naar de apps gekeken. Dit is de eerste eigen meting van de templates.

## Zo gemeten (GEZIEN)
- robots.txt van webflow.com verbiedt /api/. Die heb ik niet gebruikt. De templatepagina's staan op templates.webflow.com, waar robots.txt niets verbiedt, en staan in de sitemap: **11.903 templatepagina's**.
- Alle 11.903 pagina's gelezen. Op elke pagina staan ±8 kaartjes van andere templates (4 losse, vaak de nieuwste, en de 4 nieuwste andere van dezelfde maker). Elk kaartje toont goedkeuringsdatum, prijs, maker en een veld `cumulativePurchases` (aankopen). Dat gaf **3.103 unieke templates** met deze gegevens.
- Scripts: `data/webflow-haal-script.py` (leest de pagina's), `data/webflow-analyse-script.py` (telt per maand). Data: `data/webflow-templates-2026-11-07.json`, sitemap in `data/webflow-sitemap-urls-2026-11-07.txt`.
- Wat het aankoopcijfer betekent, zegt Webflow nergens. Het stijgt netjes met de leeftijd (mediaan lichting 2022: 27 tot 80, 2024: 13 tot 14, 2026: 0 tot 1) en de best verkochte heeft 475 aankopen op 22.331 kijkers, dus het lijkt een totaal sinds goedkeuring (GOK, sterk). Mogelijk begon het tellen pas op een bepaalde datum.

## Bereik en geld samen (GEZIEN: aankopen per template)
Hier vallen bereik en geld samen: een aankoop is een betalende klant.

| Lichting (betaald) | Met cijfer | Mediaan aankopen | 0 | 10+ | 20+ | Top 3 |
|---|---|---|---|---|---|---|
| mrt t/m jun 2026 (5 tot 8 mnd oud) | 357 | **1** | 110 (31%) | 22 (6%) | 8 (2%) | 73, 56, 35 |
| mei t/m aug 2026 (3 tot 6 mnd) | 303 | **1** | | 9 (3%) | 1 | 30, 17, 16 |
| heel 2025 | 404 van 935 | 6 | | | | 475, 398, 217 |

- Mrt t/m jun 2026: gemiddeld 3,1 aankopen. Bij $79 en 95% is dat ±$235 per template in een half jaar, dus **±$40 per maand gemiddeld en ±$12 per maand voor de middelste template** (GOK, rekensom op GEZIEN; kortingsacties van Webflow verlagen dit, zie onder).
- De top bestaat wel: Meridian van Kevin Dakin (73 × $99, ±$6.900 sinds april, ±$1.000 per maand), Auria van Template Supply (56 × $129), Galery van Div Supply (35 × $99). Template Supply is een studio met veel templates; Kevin Dakin lijkt een losse ontwerper (GOK).
- Lichting 2025: Alture (Template Supply) 475 × $129 ≈ $58.000, Bungee (Clonify) 398 × $59. Het geld zit vooral bij studio's die al jaren templates maken.
- Prijzen nieuwe templates 2026: vooral $79 (350) en $59 (299), daarna $99 en $129.

## Gaten in de meting (eerlijk)
- Maar 3.103 van de 11.903 templates zijn gezien, en het is geen aselecte steekproef: oudere templates van makers die veel uitbrengen vallen weg. Hoe scheef de lichting mrt t/m jun daardoor is, is niet te zeggen. Wel is die lichting met 357 stuks groot, en 9 van 9 nagekeken cijfers kloppen.
- Veel kaartjes uit 2025 en juli 2026 hebben een leeg aankoopcijfer. Daarom staat bij 2025 maar 404 van 935.
- `uniqueViewers` staat sinds juli 2026 bijna altijd op 0, ook bij aankopen. Kijkers zijn dus niet bruikbaar.
- Beter meten kan alleen met de /api/ (verboden door robots.txt) of als Webflow zelf cijfers deelt.

## Drukte (GEZIEN, ondergrens)
Gezien per goedkeuringsmaand in 2026: 61 tot 196 nieuwe templates, oplopend (sep 143, okt 196). Omdat niet alles gezien is, is het echte aantal hoger. De markt wordt snel voller.

## Vindbaarheid (GEZIEN en DERDEN)
- Zoeken en filters in de Marketplace, gesorteerd op populariteit (`popularityScore`) of nieuwste. Nieuwe templates staan even bovenaan bij "nieuwste".
- Webflow heeft sinds kort een AI-zoeker ("Template finder") op de templatepagina's.
- Sinds okt 2025 mag je ook buiten de Marketplace verkopen met een "fulfillment link" (DERDEN: blog). Dan heb je wel eigen publiek nodig.
- Webflow mag zonder overleg kortingsacties draaien, en de maker krijgt dan 95% van de lagere prijs (DERDEN: creator agreement). Nu loopt een actie van 50% tot 3 dec.

## Past het bij ons
- Bouwen kan in principe: Webflow heeft een officiële MCP-server waarmee een AI-agent pagina's, elementen, stijlen, componenten en animaties maakt (DERDEN: [developers.webflow.com/mcp](https://developers.webflow.com/mcp/reference/overview)). Dat vraagt een Webflow-account van Thijs en waarschijnlijk een browser met de Designer open (GOK).
- Over AI-gemaakte templates staat niets in de overeenkomst of de indieningsregels. Wel: eigen origineel werk, uniek, geen dubbele inzendingen, en een strenge keuring op ontwerp en werking. Nieuwe makers mogen **één template tegelijk** indienen.
- Een template is helemaal ontwerp. Dat past bij de nieuwe lat van Thijs (uiterlijk is de helft), maar we concurreren dan met studio's van 15 tot 30 ontwerpers (Radiant zegt 4.000+ templates verkocht).

## Voor en tegen
Voor:
- Webflow rekent af en geeft 95%. Een aankoop is meteen ±$56 tot $123 voor de maker.
- Aantoonbaar geld bij de top (±$1.000 per maand voor de beste nieuwe template van 2026).
- Geen code-onderhoud zoals bij een plugin; één keer goed maken.

Tegen:
- De middelste nieuwe template verkoopt **1 keer** in 5 tot 8 maanden. Maar 6% haalt 10+.
- Eén template tegelijk indienen en een strenge keuring: snel veel templates neerzetten kan niet.
- Steeds drukker (tot ±200 per maand gezien), en studio's met veel ervaring winnen.
- Bouwen kan alleen via het account en de Designer van Thijs.

## Eerste idee als we het toch doen
Een template voor een smalle groep waar weinig aanbod is (bijvoorbeeld een bepaald beroep of een niche met CMS), heel opvallend ontworpen samen met Daan, gebouwd via de Webflow MCP-server. Doel: in de top 6% (10+ aankopen in een half jaar, ±$750).

## Oordeel
**Nee voor nu, cijfer 4.** Het geld per klant is goed en betalen gaat via Webflow, maar bereik is zwak: de middelste nieuwe template haalt 1 aankoop in een half jaar. Wat dit zou veranderen: een niche waar nieuwe templates aantoonbaar 10+ aankopen halen, of als Dortus toch met Webflow begint, eerst één template als proef. Herhaalmeting: `python3 -I data/webflow-haal-script.py urls.txt uit.jsonl` en `python3 -I data/webflow-analyse-script.py uit.jsonl`, dan de lichting mrt t/m jun 2026 opnieuw tellen (groeit die naar mediaan 3+?).

Nagekeken door een controleur: akkoord met kleine correcties (verwerkt: 3 templates met prijs 0 eruit, tellingen 357/303/404), steekproef 9 van 9 gelijk.
