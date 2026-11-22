# Voorstel: shadcn-registry's (Noor, 8 nov 2026)

**Cijfer: 4. Advies: nee voor de pionier, doorgeven aan Vera.** Het platform groeit harder dan alles wat ik tot nu toe zag (npm-pakket shadcn ×28 in een jaar) en betalen werkt (private registry's met inlog, verkopers met duizenden blocks), maar de lijst is al vol: 548 registry's, ±117 nieuwe per maand, en de grote categorieën (animatie, blocks, AI-chat, grafieken) hebben sterke spelers met duizenden onderdelen. Dat is Vera's soort: makers verdienen nu al, en de vraag is of een kleine nieuwkomer nog opvalt.

Bronnen: alles zelf gemeten (officiële lijst `ui.shadcn.com/r/registries.json`, npm-API, docs). Script `data/shadcn-registries-meet.py`, momentopname `data/shadcn-registries-2026-11-08.json`. Geen agent en geen controleur: het advies is geen ja en de kerncijfers zijn direct uit de bron gelezen. De GitHub-repo van shadcn kon ik niet via de API lezen (geen toegang in deze sessie), dus de geschiedenis van de lijst vóór aug 2026 ontbreekt; het Wayback-archief had geen bruikbare kopie.

## 1. Groeit het platform hard? Ja, extreem.
- npm-downloads van het pakket `shadcn` (de CLI): 1.862.177 in okt 2025 naar 52.517.578 in okt 2026, ×28, elke maand hoger (GEZIEN, https://api.npmjs.org/downloads/range/2025-10-01:2026-10-31/shadcn). Een groot deel komt van AI-bouwers en agents die `shadcn add` draaien (GOK), maar dat is juist de motor: v0, Lovable en codeer-agents gebruiken shadcn als standaard.
- GitHub-sterren 128k volgens de docs-pagina (GEZIEN, https://ui.shadcn.com/docs/registry/authentication). Docs hebben inmiddels een MCP-server, skills en "Open in v0" voor registry's (GEZIEN, zelfde pagina, menu).

## 2. Is de winkel jong? Jong, maar al vol.
- De officiële lijst telt 548 registry's (GEZIEN, 8 nov). Het meten van de gezondheid begon in aug 2026 (291 toen al), daarna 117 nieuwe in september, 117 in oktober en 23 in de eerste week van november (GEZIEN, veld health.firstObservedAt).
- Grootste registry's naar aantal onderdelen: @keyline 14.664 (iconen), @hugeicons-animated-vue 6.122, @catalogs 2.213, @000h-cojeev 1.876, @react-bits 1.274 (GEZIEN, veld ranking.itemCount).
- Er zijn geen installaties per registry openbaar. Dat maakt meten van wie wint lastig.

## 3. Kan er betaald worden? Ja, en het gebeurt al.
- shadcn ondersteunt private registry's met inlog, "private and personalized components" (GEZIEN, https://ui.shadcn.com/docs/registry/authentication). De kassa regelt de maker zelf.
- Shadcnblocks verkoopt levenslange toegang voor $149, $299 of $399, met 2.241+ pro-componenten en 2.697+ pro-blocks, alles via `npx shadcn add` en de shadcn-MCP (GEZIEN, https://www.shadcnblocks.com/pricing). 12 registry's noemen zich in hun beschrijving premium of pro (GEZIEN).

## 4. Is er vraag? Ja, groot.
- De groei van de CLI zelf is de vraag. Welke onderdelen mensen missen heb ik niet gemeten (GitHub-issues van shadcn niet bereikbaar).

## 5. Is de eerste plek te pakken? In de grote categorieën nee, in een paar kleine misschien.
- Telling op beschrijving (GEZIEN, grof): animatie 148, blocks en templates 139, AI en chat 86, grafieken en dashboards 84. Daar zitten spelers met honderden tot duizenden onderdelen.
- Dun: auth 8, billing 12, e-commerce 6, kalender en planning 6. Een registry met complete, werkende kalender- en planningsblokken (dag, week, resource-planning, boekingen) zou er nummer één kunnen worden (GOK). Maar zulke blokken hangen aan een backend, en grote spelers kunnen ze snel toevoegen.

## Risico
- Geen eigen winkel met installcijfers en geen kassa van shadcn: vindbaarheid hangt af van de lijst, zoekmachines en AI-agents die een registry kiezen. Een kleine nieuwkomer verdwijnt tussen 548.
- Vercel (eigenaar via v0) of shadcn zelf kunnen elk populair blok in de basis opnemen, zoals al gebeurde met AI Elements, charts en blocks.

## Wat het zou veranderen
- shadcn toont installaties per registry of opent een betaalde laag in de lijst: dan wordt meten mogelijk en opnieuw wegen.
- Vera kan meten of kleine premium-registry's nu verkopen (Gumroad, Lemon Squeezy, eigen sites).
- Herhaalmeting rond 8 jan 2027: `python3 -I data/shadcn-registries-meet.py data/shadcn-registries-2026-11-08.json` (let op: nieuwe registry's per maand en de dunne categorieën).

## Cijfer
Vraag 1: zeer sterk. Vraag 2: jong maar vol. Vraag 3: ja. Vraag 4: groot. Vraag 5: zwak voor een nieuwkomer. Samen 4 voor de pionier: dit is een groeiende oceaan, geen lege vijver.
