# Voorstel: Craft CMS Plugin Store (betaalde plugins)

Vera, verkenner, 7 nov 2026 run 17:32 (lokale tijd). Advies: **nee voor nu. Cijfer 4.**

## Wat is het
Craft CMS is een PHP-CMS voor websites van bureaus (Pixel & Tonic). De Plugin Store zit in het control panel van elke Craft-site en op plugins.craftcms.com. Craft verkoopt de licenties en betaalt de maker uit. Een licentie is eenmalig, met een vrijwillige verlenging per jaar voor updates.

## Zo gemeten (GEZIEN)
- De hele winkel in één keer via de open API `https://api.craftcms.com/v1/plugin-store` (robots.txt staat alles toe): 1.670 plugins, met per plugin actieve installs, goedkeuringsdatum, edities met prijs en verlengprijs, en maker. Ruwe data: `data/craft-plugin-store-2026-11-07.json`, script: `data/craft-meting-script.py`.
- De controleur heeft alles onafhankelijk herrekend en op 3 pagina's (Cookie Banner 108, LLMify 671, Translation Manager 93) gezien dat het getal gelijk is aan de API.
- Indeling: 1.075 gratis, 523 zuiver betaald, 72 freemium (gratis editie plus betaalde Pro).
- Leeftijd = goedkeuringsdatum. De controleur keek 41 van de 57 jonge betaalde plugins na op Packagist: 34 stonden er hooguit 90 dagen eerder op. Uitzondering: alle 6 betaalde plugins van LindemannRock stonden er 8 tot 11 maanden eerder, met eigen klanten.

## Bereik (GEZIEN)
Zonder de massamaker (zie Drukte). Maat: actieve installs, en daar tellen dev, staging en proefinstallaties waarschijnlijk mee (GOK, Craft geeft geen definitie; proberen in een dev-omgeving is gratis).

| Lichting | Soort | Aantal | Mediaan installs | 10+ | 100+ |
|---|---|---|---|---|---|
| mei t/m aug 2026 (3 tot 6 mnd oud) | betaald | 57 | 3 | 19% | 0% |
| mei t/m aug 2026 | gratis | 45 | 6 | 33% | 7% |
| mei t/m aug 2026 | freemium | 8 | 12 | 50% | 25% |
| jan t/m apr 2026 | betaald | 38 | 6,5 | 42% | 5% |
| jul t/m dec 2025 | betaald | 24 | 6 | 42% | 4% |
| jan t/m jun 2025 | betaald | 19 | 29 | 74% | 32% |

Grootste aantallen: SEOmatic 31.579 installs. De top 10 makers hebben 75% van alle installs (DERDEN: craftstats.bms.so).

## Geld
- Craft houdt 20% in (DERDEN: [docs](https://craftcms.com/docs/5.x/extend/plugin-store), Terms of Service §2.4.2). Verlengen is niet verplicht (ToS §2.4.1), Craft adviseert 20 tot 50% van de prijs.
- Mediaanprijs nieuwe betaalde plugins $59 eenmalig (GEZIEN).
- Bovengrens per maker = actieve installs × laagste betaalde prijs (GEZIEN als getal, GOK als omzet: dev, staging en proeven tellen mee). Nieuwe makers (eerste plugin 2025 of later) met zuiver betaalde plugins, n=67: **mediaan $195 bruto in totaal**.
- Beste nieuwe makers (bovengrens bruto):
  - samuelreichor (eerste plugin dec 2024, door mijn filter eerst gemist, gevonden door de controleur): LLMify (aug 2025, 671 × $59), CoPilot (mrt 2026, 512 × $59), Query API (apr 2025, 100 × $89), samen ±$78.700, ±$5.000 per maand over ±15 maanden. Na 20% en een korting voor dev-installs ±$1.500 tot 4.000 netto per maand (GOK). Alles in de AI-niche.
  - LindemannRock ±$20.600, maar met klanten van vóór de winkel, dus niet schoon.
  - anvildev ±$6.400 over 9 plugins, Digital Astronaut (Cookie Banner, 108 × $59) ±$6.400.
  - Freemium: Craft CMS MCP (jan 2026, 3.255 installs, Pro $99). Neemt 3 tot 5% Pro, dan ±$10.000 tot 16.000 in 10 maanden (GOK).
- Geen enkel openbaar bedrag van een maker die na 2023 begon (onderzoeker). Oude maker Ben Croker noemt de markt "capped" (DERDEN: craftentries.io, 2022).

## Drukte (GEZIEN)
- 2025: ±8 nieuwe plugins per maand. 2026: van 6 in jan naar 88 in okt.
- Eén maker, Justinholt.com Incorporated, heeft 145 plugins, waarvan 57 van de 167 uit mei t/m aug 2026. Zonder hem 32 tot 42 per maand in aug t/m okt.
- Craft keurt alleen naam, icoon, docs en licentie, niet de code (DERDEN: [goedkeuring](https://craftcms.com/knowledge-base/plugin-store-approval-process)). Geen AI-regel.

## Vindbaarheid (DERDEN)
Lijsten "Recently Added", "Recently Updated" en "Top Paid" en 17 categorieën (ook AI) in de winkel. De maandelijkse nieuwsbrief van Craft noemt elke nieuwe plugin. Met ±80 per maand duurt die zichtbaarheid kort (GOK).

## Markt (DERDEN)
±37.800 live Craft-sites (BuiltWith), 0,1% van alle sites (W3Techs), -14% tot dec 2025 (Joost.blog, DomainCrawler). Craft 6, gebouwd op Laravel, komt rond maart 2027; plugins moeten dan omgezet worden.

## Past het bij ons
- Bouwen kan in 1 tot 2 weken (PHP, Twig), keuring binnen een werkdag. Wel nodig: een bureaugebruiker die het test, en ondersteuning per mail.
- Verkoopt aan bureaus die betalen, en licenties zijn eenmalig, dus geen echte maandinkomsten.

## Voor en tegen
- Voor: open API met echte installs, 20% afdracht, betalen in de winkel, snelle keuring, geen AI-regel. Eén nieuwe maker in de AI-niche haalt aantoonbaar honderden installs met betaalde plugins.
- Tegen: kleine en krimpende markt (±38.000 sites), nieuwe betaalde plugins mediaan 3 installs en 0% 100+, mediaan nieuwe maker $195 in totaal, de instroom is in 2026 vertienvoudigd (deels massaproductie), en de AI-niche waar het wel lukt raakt snel vol (18 plugins met AI, LLM of MCP in de naam, 10 uit 2026).

## Eerste idee als het toch ooit zou gaan
Een AI-plugin voor Craft (bijvoorbeeld voor content of zoeken), freemium. Of: precies bij Craft 6 (±maart 2027) een plugin die op Craft 6 klaar is terwijl de oude makers nog omzetten. Dat tweede is de enige kans met een datum.

## Advies
**Nee voor nu, cijfer 4.** De mediaan is slecht en de markt klein, maar de AI-niche laat zien dat een nieuwe maker hier ±$1.500 tot 4.000 netto per maand kan halen (GOK op GEZIEN). Wat dit verandert: de lancering van Craft 6 met een lege winkel voor Craft 6-plugins. Herhaalmeting rond februari 2027 met `data/craft-meting-script.py`, dan ook kijken hoeveel plugins al op Craft 6 draaien.

## Niet zelf gemeten
- Wat "active installs" precies telt (Craft geeft geen definitie). Dat kan alleen een maker met een account zien, in zijn verkoopcijfers.
- Echte verkopen per plugin zijn niet openbaar.

Nagekeken door een controleur (7 nov): akkoord met nee, cijfer 3 werd 4. Correcties verwerkt: samuelreichor gevonden, omrekening LindemannRock (4 maanden in de winkel, eigen klanten van eerder), freemium niet op nul, commissie 20% nagekeken.
