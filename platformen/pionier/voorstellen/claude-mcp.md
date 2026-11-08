# Voorstel: Claude-koppelingen en MCP-servers (pionier)

Noor, 8 nov 2026. Onderzoeker en controleur waren agents; het officiële MCP-register en de officiële plugin-marketplace heb ik zelf geteld (`data/mcp-register-meet.py`, uitkomst in `data/mcp-register-2026-11-08.json`).

**Cijfer: 4. Advies: nee voor nu, wachtlijst.** Het platform groeit harder dan alles wat ik tot nu toe zag, maar de winkel is al vol, de grote categorieën zijn van de eigenaren van de diensten zelf, en in de winkel kan niemand betalen. Wat overblijft is een gratis koppeling als etalage voor een eigen abonnement. Dat is een gewoon SaaS-bedrijf met een extra ingang, geen pionierskans.

## 1. Groeit het platform hard en zichtbaar? Ja, heel hard
- npm-downloads van `@modelcontextprotocol/sdk` per maand: nov 2025 35,0 mln, jan 2026 50,2 mln, mrt 141,9 mln, jun 171,2 mln, aug 225,9 mln, sep 241,8 mln, okt 281,1 mln. Acht keer zoveel in een jaar, en sep naar okt nog +16% (GEZIEN, https://api.npmjs.org/downloads/range/2025-11-01:2026-11-07/@modelcontextprotocol/sdk). Een groot deel is automatische builds (GOK), dus alleen als richting.
- Python-pakket `mcp`: 196 mln (apr) naar 320 mln (jul), daarna 230 tot 330 mln per maand, vlakker (GEZIEN, https://pypistats.org/api/packages/mcp/overall).
- Anthropic: omzet-run-rate ruim $47 mld in mei 2026 tegen $9 mld eind 2025; wekelijkse gebruikers van Claude Code verdubbeld sinds januari (DERDEN, https://officechai.com/ai/anthropic-says-its-revenue-run-rate-has-now-touched-47-billion/). Dagelijkse gebruikers van de app ±2 mln naar 11 mln tussen okt 2025 en feb 2026 (DERDEN, SimilarWeb via https://officechai.com/ai/claudes-app-daus-are-up-5x-in-the-last-5-months). MCP wordt ook gebruikt door OpenAI, Google en Microsoft.
- Motor: geloofwaardig, de grootste trend in software van dit moment.

## 2. Is de winkel jong? Jong in jaren, maar al vol
- Connectors Directory sinds juli 2025; Claude Marketplace in maart 2026 met 6 partners, op 23 sep 2026 opengezet met 2.000+ koppelingen en plugins (DERDEN, https://www.it-connect.tech/claude-marketplace-grows-fast-anthropic-brings-2000-connectors-and-plugins-together/). claude.ai/directory zelf geeft een 403, niet zelf geteld.
- Aanmelden is open: iedereen met een betaald Claude-plan, externe server via HTTPS met OAuth, privacybeleid en testaccount. Je komt erin als "Community"; "Verified" kiest Anthropic zelf (DERDEN, nagekeken door controleur, https://claude.com/docs/connectors/building/submission.md, https://claude.com/docs/directory/publish.md).
- Officiële Claude Code plugin-marketplace: 317 plugins, 40 van Anthropic, de rest bijna alleen bedrijven (Google 14, SAP 9, AWS 7, Stripe, Datadog, Notion) (GEZIEN, https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/.claude-plugin/marketplace.json).
- Aantal MCP-servers in het algemeen: Glama 117.389 (GEZIEN, https://glama.ai/mcp/servers), Smithery 20.759 waarvan 193 geverifieerd (GEZIEN, https://registry.smithery.ai/servers?pageSize=1). Officieel MCP-register: zie de telling onderaan.
- Conclusie: een winkel van 2.000+ met daarachter 100.000+ servers is geen lege winkel. Dit hoort qua drukte bij Vera.

## 3. Kan er betaald worden? Niet in de winkel
- De documentatie van Anthropic noemt nergens een prijs, betaling of omzetdeling voor koppelingen of plugins (GEZIEN door onderzoeker en controleur, https://claude.com/docs/llms.txt). De directory-regels verbieden advertenties en betaalde plaatsing (DERDEN, https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).
- Wel toegestaan: een koppeling die via OAuth toegang geeft tot een eigen betaald abonnement. Bij aanmelden vul je in welk account of plan de gebruiker nodig heeft (DERDEN, submission-pagina hierboven). Geld loopt dan buiten Claude, bijvoorbeeld via Polar.
- De betaalde categorie "Agents and products" (betalen uit het Anthropic-budget van een bedrijf) is alleen via een wachtlijst voor producten voor grote bedrijven (DERDEN, https://claude.com/marketplace-partners). Niets voor ons.
- Elders: Apify betaalt makers van Actors en MCP-servers, 20% commissie, "$1.7M paid out last month" (GEZIEN, https://apify.com/mcp/developers, https://docs.apify.com/actors/publishing/monetize.md); vooral scrapers, MCP-deel onbekend. Eén kleine maker met bewijs: Ref (ref.tools), $9 per maand, "hundreds of subscribers" na 3 maanden (DERDEN, PulseMCP-blog). Tegenvoorbeeld: maker 5 maanden $2.885 per maand kosten voor de eerste klant (DERDEN, Reddit-kopie).
- Geen aankondiging van betaalde koppelingen of een makersfonds gevonden sinds juli 2026.

## 4. Is er vraag te zien? Ja, maar naar de grote koppelingen van Anthropic zelf
- Meest gevraagd op anthropics/claude-code: meerdere accounts per koppeling (647 reacties, https://github.com/anthropics/claude-code/issues/27302), meerdere Slack-werkplekken (130, #44243), Microsoft 365 voor persoonlijke accounts (105, #20469), Gmail met labels en verzenden (41, #36547), Telegram en WhatsApp (#36814) (GEZIEN door onderzoeker).
- Dat zijn gaten in koppelingen van Anthropic of van de dienst zelf. Die kunnen morgen dicht, en dan is ons product weg.

## 5. Is de eerste plek in een categorie te pakken? Bijna nergens
- Bezet door de eigenaar zelf: code en devops (GitHub, GitLab, Linear, Atlassian, Datadog, Grafana), cloud en databases, design (Figma, Canva), betalen en boekhouden (Stripe, QuickBooks), zoeken en scrapen (Exa, Firecrawl, Context7).
- Nog open (GOK): diensten zonder eigen koppeling, zoals Nederlandse boekhoudpakketten en overheidsdata, of vakgerichte Skills. Klein per stuk, en de eigenaar kan altijd zelf instappen. Een derde partij is hier per definitie te gast in andermans categorie.

## Risico dat het platform het niet haalt
Klein: MCP is een standaard van alle grote AI-bedrijven. Het risico zit niet in het platform maar in onze plek erop: de eigenaar van elke dienst en Anthropic zelf zijn de natuurlijke makers van koppelingen. Teken dat het voor ons beter wordt: Anthropic opent betaalde koppelingen of een omzetdeling voor kleine makers, of zet installs per koppeling openbaar.

## Categorie en eerste productidee (alleen voor de wachtlijst)
Nederlandse bedrijfsdata als koppeling (KvK, BAG, CBS, rechtspraak): gratis basis in de directory, betaald abonnement via Polar voor meer verzoeken. Geen eigenaar die dit zelf bouwt, wel klein (GOK: honderden gebruikers, niet duizenden). Pas zinvol als er meer bewijs is dat directory-gebruikers doorklikken naar een betaald plan.

## Wat ik niet kon meten
Aantal koppelingen in claude.ai/directory (403), installs per koppeling (niet openbaar), mcp.so en PulseMCP (geblokkeerd), groei van de Glama-telling door de tijd. Herhaalmeting rond 8 dec met `python3 data/mcp-register-meet.py`: groei van het officiële register per maand en van de officiële plugin-marketplace.

## Officieel MCP-register, eigen telling
Gemeten 8 nov 03:19 UTC over de hele API (alle versies, per servernaam de eerste publicatie), GEZIEN, https://registry.modelcontextprotocol.io/v0/servers:
- 58.585 servers onder 36.599 namen van makers, waarvan 39.661 met een server op afstand (zoals de directory eist).
- Nieuw per maand: sep 2025 456, dec 276, feb 2026 1.154, apr 2.547, jun 3.848, aug 6.519, sep 11.849, okt 16.283, en in de eerste 7 dagen van nov al 4.763.
- Dit bevestigt het oordeel: het aanbod verdubbelt ongeveer elke twee maanden en loopt nu op ±500 nieuwe servers per dag. Een nieuwe koppeling van ons verdrinkt hier, tenzij hij in een categorie zit die niemand anders kan bedienen.
