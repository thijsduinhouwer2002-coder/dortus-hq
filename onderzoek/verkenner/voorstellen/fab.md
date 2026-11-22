# Voorstel: Fab (winkel van Epic, tools en plugins voor Unreal)

**Advies: nee voor nu. Cijfer: 3 van 10.** Geschreven op 6 nov 2026 (run 22:31), met eigen meting van 4.108 tools en plugins. Het geldmodel is goed (makers houden 88%), maar een nieuwe betaalde tool krijgt na 3 tot 6 maanden bijna nooit een beoordeling: 85% heeft er nul. Hetzelfde beeld als bij Unity. Het aanbod groeit hard (893 nieuwe tools in oktober 2026).

## Eigen meting (6 nov 2026)
Hoe: de open zoek-API van Fab (`/i/listings/search?listing_types=tool-and-plugin&sort_by=-createdAt`) gaf 4.128 tools, nieuwste eerst, tot ±nov 2025. Per product de open JSON (`/i/listings/<uid>`) met firstPublishedAt, beoordelingen per ster en prijs. 20 gaven een 403, dus 4.108 geanalyseerd. Scripts: `data/fab-zoek-script.py`, `data/fab-haal-script.py`, `data/fab-analyse-script.py`; data in `data/fab-tools-2026-11-06.json`. Verkopen toont Fab niet. Een beoordeling vraagt een geverifieerde aankoop (DERDEN, verkopersblog), dus elke beoordeling is minstens één verkoop.

**Bereik (GEZIEN)**
- Betaalde tools van 3 tot 6 maanden oud (mei tot aug 2026): n=1.181. Mediaan 0 beoordelingen. 15% heeft er 1 of meer, 2% 5 of meer, minder dan 0,5% 10 of meer.
- Makers met 1 tot 3 tools: 19% 1+, 2% 5+.
- Ouder (mrt tot apr 2026, 6 tot 8 maanden): 26% 1+, 5% 5+, 1% 10+.
- De best scorende nieuwe tool (mei tot aug) heeft 71 beoordelingen (Mesh Painting, $38,99, maker met 2 tools). Daarna vooral gratis tools of tools van Epic zelf.
- Producten van de oude Unreal Marketplace hebben hun beoordelingen meegenomen (bijvoorbeeld Electronic Nodes 464, Blueprint Assist 186). Die staan bovenaan; nieuwe makers beginnen op nul.

**Geld**
- Makers houden 88% (DERDEN, [Game Developer](https://www.gamedeveloper.com/marketing/epic-to-unify-content-marketplaces-and-offer-creators-88-percent-revenue-cut)). Netto iets minder volgens een verkoper ([StraySpark](https://www.strayspark.studio/blog/fab-marketplace-12-month-retrospective-seller-2026)).
- Prijsmediaan nieuwe betaalde tools $19,99, ±85% betaald (GEZIEN).
- Volgens het jaaroverzicht 2025 verdienden makers samen ruim $24 miljoen over ruim 20.000 verkopers, gemiddeld ±$1.200 per verkoper per jaar, alle soorten producten samen (DERDEN, via StraySpark, niet op de pagina van Epic zelf gelezen: [Fab 2025](https://www.unrealengine.com/en-US/news/fab-2025-year-in-review)). Dat gemiddelde ligt ver onder ons doel, en de meeste geld gaat naar de top.
- Geen gemeten cijfer van een kleine nieuwe maker gevonden. Op het forum klagen verkopers over maanden zonder verkoop ([forum](https://forums.unrealengine.com/t/no-fab-sales-in-january-2025-any-one-else-experiencing-this/2279155/7)).

**Drukte (GEZIEN)**
- Nieuwe tools per maand: ±170 tot 210 dec 2025 tot feb 2026, 272 tot 418 in mei tot aug (gemiddeld 348), 518 in sep, 893 in okt 2026.

**Meetgrenzen**
- De zoek-API geeft geen totaal. De controleur bladerde andere sorteringen door en vond geen ontbrekend product van mei tot aug 2026.
- Alleen het type tool-and-plugin gemeten. Een losse steekproef van 2.500 producten over alle types (vooral 3D-modellen) was nog zwakker: 3% van de nieuwe heeft een beoordeling.

## Waarom nee
Goed geldmodel, grote kopersgroep, maar het bereik voor een nieuwe maker is bijna nul en het aanbod verdubbelt. Het gemiddelde per verkoper ($1.200 per jaar) maakt het niet beter.

## Wat het oordeel kan veranderen
Cijfers van een kleine maker die met een nieuwe tool in de eerste maanden echt verkocht, of een verandering in hoe Fab nieuwe producten toont.

## Nakijken
Controleur (6 nov, run 22:31): zes producten zelf nagelezen, alles klopt, lijst mei tot aug compleet, rekenwerk zonder fouten. Zes kleine correcties, alle verwerkt (n=4.108, 10+ is minder dan 0,5%, spreiding per maand, nov 2025 weggelaten, overgenomen beoordelingen, gemiddelde per verkoper).
