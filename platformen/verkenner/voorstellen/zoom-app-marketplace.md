# Zoom App Marketplace

Verkenner Vera, 9 nov 2026, run 17:31 (Amsterdam), tweede platform van de run. Voorwerk met eigen meting, kort.

## Advies: nee. Cijfer 2.

Betalen via Zoom kan alleen voor makers én kopers in de VS, dus niet voor Thijs. De winkel toont geen installaties en geen ratings, dus bereik is niet te meten. De apps zijn vrijwel allemaal van bedrijven, en bijna niemand vraagt geld via Zoom.

## Cijfers

### Eigen meting (GEZIEN)
- Open API achter de winkel: `marketplace.zoom.us/api/v1/marketplaceV2/homepage/search` (lijst, 4.037 apps, alle opgehaald) en `.../detailV2/<id>` (per app). marketplace.zoom.us heeft geen robots.txt. Scripts `data/zoom-lijst-script.py` en `data/zoom-detail-script.py`, data `data/zoom-lijst-2026-11-09.json` en `data/zoom-detail-steekproef-2026-11-09.jsonl`.
- Steekproef detailpagina's: 166 apps (elke 6e uit de standaardvolgorde van de winkel, het eerste kwart van de lijst; geen volledig willekeurige steekproef).
- **Geld:** 1 van de 166 apps heeft `monetized: true` (Nametags van Warmly). Van de 34 apps met aanmaakjaar 2025 of 2026: 0.
- **Drukte:** aanmaakjaar in de steekproef: 2025 17, 2026 17 (van 166). Grof doorgerekend naar 4.037 apps: GOK ±400 per jaar, ±35 per maand. Let op: `createdTime` is wanneer de app bij de ontwikkelaar is aangemaakt, niet per se de publicatiedatum.
- **Wie maakt ze:** de nieuwe apps van 2025 en 2026 in de steekproef zijn van bedrijven (Vanta, Composio, Front, Harness, Recruiterflow, Manus, Zoom zelf); veel AI-notulisten en MCP-koppelingen. Geen herkenbare kleine maker.
- **Bereik:** de API geeft geen installaties, geen ratings en geen reviews. Niet te meten.

### Bronnen (DERDEN)
- Monetisering van Zoom: "Monetization is available only to US-based customers and developers. The business or individual that receives payments and payouts must be in the geographic USA. Buyers must be in the geographic USA." Ook verplicht: een gratis versie naast de betaalde. https://developers.zoom.us/docs/distribute/monetization/
- Elke app gaat door een review op werking, gebruiksgemak en naleving: https://developers.zoom.us/docs/distribute/app-review-process/

## Langs de vier punten van een 8
1. Kleine makers verdienen: niet te zien; monetisering vrijwel ongebruikt. Zwak.
2. Bereik voor nieuwkomers: niet te meten, apps zijn vooral koppelingen die je meeneemt vanuit je eigen product. Zwak (GOK).
3. Bouwen en testen: web-apps met OAuth kunnen, Zoom Apps in de client zijn lastiger te testen in de cloud. Redelijk.
4. Thijs kan verkopen: niet via Zoom (alleen VS). Zelf afrekenen buiten Zoom kan, maar dan zonder etalage-voordeel. Zwak.

## Eerste idee
Geen. Een Zoom-app is hier een koppeling bij een eigen SaaS, geen product op zichzelf.

## Herhaalmeting
Alleen als Zoom monetisering opent voor makers buiten de VS (pagina hierboven).

## Nagekeken
Geen controleur (werktijd op). Wat niet te meten was: installaties en verkopen per app. De steekproef is het eerste kwart van de lijst; de rest van de 4.037 detailpagina's kan met `data/zoom-detail-script.py` (stap 1, ±70 minuten).
