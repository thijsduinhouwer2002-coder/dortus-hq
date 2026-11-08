# Vercel Marketplace (native integraties)

Noor, pionier, 8 nov 2026, run 22:39 UTC. Cijfer **4**, advies **nee voor de pionier**.

## Wat het is
Op de Vercel Marketplace installeert een klant een dienst van een derde (database, AI-dienst, testen, code-review) zonder apart account, en betaalt hij via zijn Vercel-rekening. De aanbieder stuurt facturen via de Partner API en Vercel int het geld (GEZIEN, https://vercel.com/docs/integrations/create-integration/billing.md). Gestart op 28 aug 2024 met Supabase, Redis en EdgeDB (GEZIEN, https://vercel.com/blog/introducing-the-vercel-marketplace). Sinds 23 okt 2025 een aparte hoek "AI Agents & Services" (GEZIEN, https://vercel.com/changelog/introducing-ai-agents-and-services-on-the-vercel-marketplace).

Waarom gekozen: betalen werkt al (zoals Thijs op 8 nov vroeg), de winkel is ruim twee jaar jong en Vercel groeit van alle platforms die ik vandaag zag het hardst.

## De vijf vragen

**1. Groeit het platform hard? Ja, heel hard (9 van 10).**
- npm per maand, okt 2025 tegen okt 2026: `vercel` (CLI) 4,54 mln naar 18,90 mln (x4,2), `@vercel/sdk` 0,39 mln naar 2,29 mln (x5,9), `ai` (AI SDK) 17,2 mln naar 132,7 mln (x7,7) (GEZIEN door hulpagent, https://api.npmjs.org/downloads/range/2025-10-01:2026-10-31/vercel). Elke maand hoger. CI en AI-agents blazen dit op, maar de richting is duidelijk.
- Omzet: Sacra schat $600M per jaar in sept 2026, +111% (DERDEN, https://sacra.com/c/vercel/). Ander nieuws noemt $200M ARR in april 2026 (DERDEN, https://www.descubre.vc/noticia/vercel-alcanza-los-200m-de-arr-y-guillermo-rauch-prepara-el-camino-al-ipo-2026-04-13). Die twee botsen; niet na te gaan welke klopt.
- Motor: Series F van $300M bij $9,3 mld (sept 2025) (DERDEN, https://www.thestar.com.my/tech/tech-news/2025/10/01/ai-coding-startup-vercel-raises-300-million-valued-at-93-billion); v0 meer dan 4 mln gebruikers (DERDEN, Sacra).

**2. Is de winkel jong? Redelijk jong, maar gecureerd en langzaam (5 van 10).**
- Zelf geteld op https://vercel.com/marketplace (paginadata, veld approvedAt): 76 producten (GEZIEN, `data/vercel-marketplace-meet.py`, uitkomst in `data/vercel-marketplace-2026-11-08.json`). Per jaar goedgekeurd: 2024: 10, 2025: 34, 2026 tot nu: 22. Per maand in 2026: 1 tot 6. De piek was okt 2025 (11, de start van de AI-hoek).
- In 2026 kwamen er ongeveer 12 nieuwe aanbieders bij (AssistLoop, cubic, Parallel, PostHog, Browserbase, Firecrawl, Shopify, AgentMail, Endform, Algolia, Exa, Mem0); de rest zijn extra producten van bestaande namen zoals AWS (S3, DynamoDB, Aurora) (GEZIEN).
- Hoeken (tags, GEZIEN): databases 29, agents 17, observability 16, cms 11, zoeken 9, dev tools 9, auth 8, analytics 8, ai 8. Testen 3, code-review 3, security 3, betalingen 1.
- Installs staan nergens in de pagina (GEZIEN, geen tellerveld). Groei per integratie is dus niet te meten.

**3. Kan er betaald worden? Ja, ingebouwd (7 van 10), maar met onbekende afdracht.**
- Billing plans per product, Vercel int het geld (GEZIEN, docs hierboven).
- Het deel dat Vercel houdt is niet openbaar: het openbare Integrations Marketplace Agreement geldt voor gratis koppelingen ("currently no fees"), de voorwaarden voor native billing staan pas in de console (GEZIEN, https://vercel.com/legal/integrations-marketplace-agreement en https://vercel.com/docs/integrations/create-integration/submit-integration.md). Die voorwaarden accepteren is iets voor Thijs.
- Kosten vooraf: een Vercel-team op Pro ($20 per maand per lid, GOK op de huidige prijs) en een eigen server voor de integratie (GEZIEN, https://vercel.com/docs/integrations/create-integration/marketplace-product.md).

**4. Is er vraag te zien? Weinig (3 van 10).**
- Community-forum: vooral fouten met Neon en Supabase, een paar losse verzoeken (Typesense, Vercel zegt "no immediate plans") (GEZIEN door hulpagent, https://community.vercel.com/t/42852). Op Hacker News bijna niets (GEZIEN, hn.algolia.com). Geen terugkerend verzoek dat niemand bouwt.

**5. Is de eerste plek in een hoek te pakken? Nee, niet voor Dortus (2 van 10).**
- Wie erin mag: een formulier (bedrijfsnaam, contact, website) op https://vercel.com/marketplace/program, daarna een checklist en een beoordeling per mail (GEZIEN door hulpagent). Geen harde eis voor omzet of SOC2 gevonden, maar het blijft handmatige selectie, en een aanvraag kan blijven liggen (GEZIEN, https://community.vercel.com/t/22001).
- De aanbieders zijn bijna allemaal gefinancierde bedrijven met een eigen dienst: AWS, Stripe, Shopify, Sentry, Supabase, PostHog, YC-startups (cubic, team van 6). Dit is hetzelfde beeld als bij Claude en ChatGPT (les 8 nov 03:10 en 09:00): de winkel vult met merk-koppelingen.
- Een native integratie is een **gehoste dienst** (database, AI-API, test- of review-dienst) met support op Vercel-niveau. Dat is geen klein product dat Dortus bouwt en laat staan; het vraagt servers, kosten per klant en altijd bereikbaar zijn. De kleinste hoeken (testen 3, code-review 3) worden al bezet door YC-bedrijven met geld en een team.
- Gewone koppelingen (zonder billing) komen pas na 500 actieve installaties in de openbare lijst (GEZIEN, https://vercel.com/docs/integrations/create-integration.md). Dus ook daar geen snelle vindbaarheid.

## Risico
Het platform haalt het vrijwel zeker; het risico is andersom: Vercel bouwt zelf de hoeken die lopen (AI Gateway, Blob, Edge Config, Workflow) en kiest zelf wie erin komt. Een kleine aanbieder kan zo uit beeld raken.

## Categorie en productidee (als het toch ooit zou moeten)
Geen hoek waar wij nummer één kunnen worden. Het dichtstbij: een kleine, goedkope dienst die bij AI-apps op Vercel ontbreekt (bijvoorbeeld zoeken met Typesense of Meilisearch als native integratie). Maar dat is een hostingbedrijf beginnen, niet een app bouwen.

## Cijfer en advies
**4, nee voor de pionier.** Groei is top en betalen werkt, maar de winkel is gecureerd, gevuld met merken en vraagt een gehoste dienst met support. Niet doorgeven aan Vera: makers zonder eigen dienst verdienen hier niets en verkopen zijn niet te zien.

Opnieuw wegen als: Vercel installs per integratie toont, een lichte soort integratie met billing opent (bijvoorbeeld betaalde templates of agents-skills zonder eigen server), of de afdracht openbaar wordt. Herhaalmeting hooguit rond 8 feb 2027: `python3 -I data/vercel-marketplace-meet.py`.

Wat ik niet kon meten: installs, het percentage dat Vercel houdt, hoe lang de goedkeuring duurt, en welk omzetcijfer van Vercel klopt.

Controle: geen aparte controleur. De winkeltelling is mijn eigen volledige meting van de pagina (twee keer gedraaid, 77 en 76 producten door één dubbele naam); de groeicijfers zijn npm-tellingen met link, de rest DERDEN met link.
