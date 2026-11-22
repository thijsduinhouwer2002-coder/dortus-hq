# Voorstel: Freshworks Marketplace (apps voor Freshdesk, Freshservice, Freshsales en Freshchat)

Vera, 16 nov 2026, run 11:31 (Amsterdam). Eigen meting van alle 1.749 pagina's uit de sitemap, nagekeken door een controleur (agent): 15 van 15 pagina's opnieuw gelijk, alle getallen klopten.

**Cijfer: 2. Advies: nee.**

## Wat het is
De appwinkel van Freshworks, de tweede grote helpdesk na Zendesk (zelfde soort kopers: supportteams en IT-afdelingen). Betaalde apps lopen via het Freshworks paid apps program. robots.txt staat alles toe (GEZIEN, 16 nov). Elke apppagina geeft in zijn paginadata install_count, ratings_count, published_at en extension_id; er is ook een open API `https://www.freshworks.com/apps/api/app/<naam>` (gevonden door de controleur).

## Hoe gemeten
- 1.749 pagina's gelezen, 1.598 apps. Daarvan 1.093 echte apps in de winkel (source platform of mcp_server); 452 zijn alleen een verwijzing naar een andere site (external) en 53 zijn eigen koppelingen van Freshworks (native) (GEZIEN).
- Er is nergens een aanmaakdatum, alleen de datum van de laatste versie. Leeftijd daarom gemeten met extension_id, een oplopend nummer: bij de 430 apps die nog op versie 1 staan loopt de publicatiedatum keurig mee met het nummer (4,5% van de paren in de verkeerde volgorde) (GEZIEN). 405.000 tot 460.000 is ongeveer mei t/m aug 2026, 340.000 tot 390.000 ongeveer jun t/m nov 2025. Een nieuwe vermelding van een oude app telt daardoor als nieuw (GOK: weinig).

## Cijfers
- **Bereik, lichting ±mei t/m aug 2026** (n=65): mediaan 1 installatie, 18% met 10+, 2% met 100+ (dat ene is een eigen app van Freshworks). Betaald (n=27): mediaan 1, 4% met 10+ (GEZIEN).
- **Bereik, lichting ±jun t/m nov 2025** (n=140, een jaar oud): mediaan 4, 32% met 10+, 7% met 100+. Betaald (n=27): mediaan 1, geen enkele 100+ (GEZIEN).
- **Wie wint:** de top 5 van alle apps sinds jun 2025 is van Freshworks zelf (Freshservice for AI Agents 1.037, Freshdesk for AI Agents 962, SharePoint Search Connector 513, Confluence 309, Google Drive 241); in de top 20 zijn er 12 van Freshworks. Grootste externe: SquawkVoice 193, PDQ 162, Synthflow 113 (GEZIEN, maker uit het veld account).
- **Drukte:** ±65 nieuwe apps in vier maanden, ±63 sinds september (GEZIEN, via extension_id). Rustiger dan Zendesk, maar elke nieuwe app haalt toch bijna niets.
- **Geld:** 280 betaalde apps (235 betaald, 45 met aankopen in de app). De grootste betaalde zijn connectors (Azure DevOps 764, Jira 667, Power BI 324) van gevestigde makers (GEZIEN). Prijzen en omzet niet openbaar; geen bron van derden gevonden over wat kleine makers verdienen. In beide recente lichtingen samen haalt geen van de 54 betaalde apps 100 installaties.

## Voor en nadelen
- Voor: open data per app, betalen via de winkel, kopers met budget.
- Tegen: nieuwe apps van derden halen mediaan 1 installatie, Freshworks vult de top zelf (AI-agents en zoekconnectors), kopers zijn bedrijven (les van Atlassian), geen enkel bewijs dat een kleine nieuwe maker hier geld verdient.

## Wat het cijfer kan veranderen
Een lichting met 20%+ op 100 installaties, of een openbaar bedrag van een kleine nieuwe maker. Herhalen: `python3 -I data/freshworks-marketplace-haal-script.py uit.jsonl` (±3 minuten, 4 tegelijk); meting van vandaag in `data/freshworks-marketplace-2026-11-16.jsonl`.

## Les
Samen met Zendesk (16 nov, cijfer 2): helpdeskwinkels geven nieuwe apps nauwelijks bereik en het platform bouwt de AI-koppelingen zelf. Niet verder zoeken in helpdesk- en CRM-winkels.
