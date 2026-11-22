# Notion Marketplace: Custom Agents, AI Skills, Workers en koppelingen

Onderzocht door Noor op 9 nov 2026, run 11:40 UTC. Cijfer **3**, advies **nee voor nu**.

Notion bouwt sinds 2026 een ontwikkelaarsplatform rond AI: Custom Agents (agent-templates in de Marketplace sinds feb 2026), AI Skills, Workers (eigen code die Notion host, sinds mei 2026) en de oude lijst met koppelingen. Ik keek of hier een jonge winkel is waar wij vroeg kunnen zijn en kunnen verkopen.

## De vijf vragen

**1. Groeit het platform hard? Ja.**
- Sacra schat $865 mln ARR in juli 2026, +82% op jaarbasis, waardering $11 mld (DERDEN, https://sacra.com/research/notion-at-865m-year-growing-82-yoy/). Notion zet volledig in op agents (Notion Agent sept 2025, Custom Agents, Notion-credits van $10 per 1.000 sinds 4 mei 2026; DERDEN, https://matthiasfrank.de/en/notion-custom-agents/).
- Maar Notion is geen jong platform: het is een oceaan van tientallen miljoenen gebruikers en een templatewinkel met duizenden makers.

**2. Is de winkel jong? Het agent-deel wel, maar de instroom is al stilgevallen.**
- 393 agent-templates in de Marketplace (GEZIEN, `__NEXT_DATA__` op https://www.notion.com/custom-agent-templates?page=1 tot 33; door controleur nageteld).
- Aanmaakdatum van de agent: alle steekproeven (controleur, 13 stuks) tussen feb en juni 2026; feb 104, mrt 89, apr 63, jun 61 volgens mijn telling; sinds juli bijna niets nieuws (GEZIEN, `created_time` op de detailpagina's, data in `data/notion-agents-2026-11-09.json`). Het was een lanceergolf.
- AI Skills: 2.305 listings, wel hard groeiend: in mijn steekproef van 703 aug 110, sep 199, okt 209 nieuw (GEZIEN, https://www.notion.com/skills-templates).
- Koppelingen: 528 in de lijst, 38 van Notion zelf, lijst bestaat al jaren (GEZIEN, https://www.notion.com/connections).
- Workers kunnen alleen binnen de eigen workspace gedeeld worden; geen route naar andere workspaces of de Marketplace (GEZIEN, https://developers.notion.com/workers/guides/sharing-workers.md). Voor makers is dat dus geen winkel.

**3. Kan er betaald worden? Voor templates ja, voor agents en koppelingen nog niet.**
- Templates verkopen via Notion: Notion is merchant of record, 8% plus $0,40 per verkoop, wachtlijst en goedkeuring ("a few months"), Nederland toegelaten (GEZIEN, https://www.notion.com/help/selling-on-marketplace).
- In de webhook-velden staat al `productType` "Custom Agent" en "Integration Listing" (GEZIEN, zelfde pagina). Betaalde agents en koppelingen lijken dus voorbereid, maar zonder datum of aankondiging.
- Vandaag: alle 393 agents price 0, alle 528 koppelingen price 0 (GEZIEN, nageteld). Bij AI Skills ±30 betaalde van 703 ($0,99 tot $199,99), die halen 0 tot 3 installs (GEZIEN).
- Buiten Notion verkopen makers agent-instructies los ($15 tot $89, DERDEN, https://www.bettercreating.com/notionagents), maar zonder verkoopcijfers.
- Custom Agents werken alleen op Business en Enterprise (GEZIEN, https://www.notion.com/help/custom-agents).

**4. Is er vraag? Ja, maar Notion vult die zelf.**
- Installs zijn zichtbaar: de top is van Notion zelf (Email assistant 25.673, Calendar optimizer 22.446, Morning brief 19.545, Task triager 18.182; GEZIEN). Notion maakte 80 van de 393 agents en heeft 59% van alle 238.931 installs.
- Agents van na juli: mediaan 1 install, geen enkele 100+ (GEZIEN, eigen telling). Een nieuwkomer krijgt geen bereik meer.
- Notion zelf duwt "copy and remix" met de Agent Hall of Fame (DERDEN, https://www.createwith.com/tool/notion/updates/notion-launches-agent-hall-of-fame-to-showcase-custom-agent-templates). Een agent-template is tekst en is in een minuut na te maken.

**5. Is de eerste plek te pakken? Nee.**
- De grote categorieën (mail, agenda, ochtendoverzicht, taken) zijn van Notion zelf. Kleine categorieën zijn er genoeg, maar zonder bereik en zonder betalen levert dat niets op.

## Risico en wat het verandert
- Wordt dit hoger: Notion opent betaalde Custom Agents of betaalde koppelingen in de eigen kassa (het veld in de webhook wijst daarop), of Workers worden deelbaar met andere workspaces via de Marketplace. Dan opnieuw wegen: een Worker met een betaalde sync of tool is iets wat niet in een minuut te kopiëren is (dan mogelijk 6).
- Herhaalmeting rond 9 jan 2027: `python3 -I data/notion-marketplace-meet.py custom-agent-templates` en `integrations/all`, kijk naar price > 0.

## Cijfer
3: platform groeit hard, maar de agent-winkel was een lanceergolf die stilviel, Notion pakt zelf de top, en betalen voor agents en koppelingen bestaat nog niet. Templates verkopen kan wel, maar dat is de oceaan.
