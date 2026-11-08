# Voorstel: Payload CMS, plugins (Noor, 8 nov 2026)

**Cijfer: 4. Advies: nog niet klaar.** Het platform groeit het hardst van alle CMS'en en Payload 4 dwingt elke plugin met een eigen scherm tot een overstap, maar er is geen winkel, geen enkele betaalde plugin van derden en geen plan voor geld. De rijkste functies houdt de eigenaar zelf (Enterprise), en wat goed loopt verdwijnt in de kern.

Bronnen: eigen meting van npm (`data/payload-plugins-meet.py`, uitkomst `data/payload-plugins-2026-11-08.json`: 1.902 pakketten gevonden via vijf zoekopdrachten, 766 met payload als afhankelijkheid, waarvan 729 van derden en 37 officieel). Onderzoeker (agent) voor groei, Payload 4, geld, vraag en risico. GitHub zelf gaf in deze run een 403; sterren via ungh.cc en het Wayback-archief.

## 1. Groeit het platform hard en zichtbaar? Ja, heel hard.
- npm-downloads van `payload`: 818.564 in okt 2025, 1.500.140 in apr 2026, 4.556.254 in okt 2026, dus ±5,6 keer in een jaar (GEZIEN, https://api.npmjs.org/downloads/range/2025-10-01:2026-10-31/payload). Ter vergelijking: Strapi 701.555 naar 989.385, Directus vlak (GEZIEN, zelfde API). Let op: CI en AI-agents blazen npm-tellers op, maar die gelden voor Strapi ook.
- GitHub-sterren 38.746 (14 nov 2025) naar 45.722 nu, +18% (GEZIEN via https://web.archive.org/web/20251114083436/https://github.com/payloadcms/payload en https://ungh.cc/repos/payloadcms/payload). Discord 14.441 leden (GEZIEN, invite-API).
- Motor: Figma kocht Payload in juni 2025. Op 15 okt 2026 werd Payload de backend van Figma Make: wie in Make een site met data vraagt, krijgt database, opslag, inlog en adminpaneel van Payload, gehost door Figma, op alle plannen (DERDEN, https://www.figma.com/blog/websites-with-payload-in-figma/ en https://www.creativeainews.com/articles/figma-make-payload-cms-website-2026/). Figma noemt zelf "6x downloads in 12 maanden".

## 2. Is de app-winkel jong of gaat hij net open? Er is geen winkel.
- De docs verwijzen voor community-plugins alleen naar het GitHub-topic `payload-plugin` (GEZIEN, https://payloadcms.com/docs/v4/plugins/overview.md). Geen lijst op payloadcms.com (/plugins en /marketplace geven 404, GEZIEN). Geen roadmap-item voor een marketplace gevonden.
- Het aanbod zelf is jong en groeit snel: nieuwe plugin-pakketten van derden per maand (eerste publicatie op npm, GEZIEN eigen meting): 15 (nov 2025), 19 (jan), 31 (apr), 37 (jun), 57 (jul), 58 (aug), 50 (sep), 74 (okt). Dat is ±5 keer zo veel als een jaar geleden.
- Gedwongen overstap: Payload 4 beta sinds 9 okt 2026 (beta.7 op 4 nov), nieuw adminpaneel op het Figma-designsysteem, TanStack Start naast Next.js (DERDEN, https://payloadcms.com/posts/releases/payload-4-beta-redesigned-admin-tanstack-mcp). De migratiegids breekt vrijwel elke plugin met admin-UI: geen `next/navigation` of `next/link` meer in admincomponenten, subpaden van `@payloadcms/next` verhuisd, `definePlugin` vraagt een slug (GEZIEN, https://payloadcms.com/docs/beta/migration-guide/v4). Van de 729 pakketten van derden geven er ±44 al ondersteuning voor 4 aan (ruwe telling op de peer-versie, GEZIEN). Stabiel: geen datum; bij v3 duurde de beta ±7 maanden, dus Q1 of Q2 2027 (GOK).

## 3. Kan er betaald worden, of komt dat eraan? Nee, geen plan.
- Geen betaalde plugin van derden gevonden; 668 van de 729 pakketten zijn MIT, 3 "UNLICENSED" en 3 "SEE LICENSE" (GEZIEN). Zelfs een pakket met "pro" in de naam is MIT met 163 downloads per maand (GEZIEN, onderzoeker).
- De cultuur is gratis: FocusReactive geeft A/B-testen, commentaar, presets en AI-vertaling gratis weg en haalt daarmee 42.000+ downloads per maand per plugin (GEZIEN, eigen meting).
- Payload zelf verkoopt als Enterprise: SSO, AI auto-embedding, publicatieworkflows, visual editor, statische A/B-testen, Enterprise AI en straks multiplayer (GEZIEN, https://payloadcms.com/enterprise). Die hoek is dus van de eigenaar.
- Wat wel verkoopt: starters en templates (shadcnblocks-boilerplate $379, GEZIEN https://www.shadcnblocks.com/pricing). Verkopen via een eigen licentie en kassa kan technisch (npm is open), maar er is geen voorbeeld dat het werkt.

## 4. Is er al vraag te zien? Ja, maar klein per plugin.
- Terugkerende verzoeken (onderzoeker, zonder stemaantallen door de 403): rollen en rechten via een scherm in plaats van code (https://github.com/payloadcms/payload/discussions/2460), auditlog los van versies, talen naast elkaar bewerken (https://github.com/payloadcms/payload/discussions/4195), meer Lexical-functies.
- Bereik voor nieuwkomers (GEZIEN, downloads afgelopen maand): plugins van mei tot okt 2026 (303 stuks) mediaan 191 per maand, 41 boven 1.000 en 2 boven 10.000. Plugins van nov 2025 tot apr 2026 (127) mediaan 112, 25 boven 1.000, 3 boven 10.000. Veel kleiner dan bij Filament (mediaan duizenden).
- De grootste plugins gaan over inloggen (payload-oauth2 78.558, payload-auth 40.858) en API's (payload-oapi 70.489): technische bouwstenen, geen betaalde producten.

## 5. Is de eerste plek in een categorie nog te pakken? Deels, maar het blijft gratis.
- Rollen en rechten met een scherm: beste is payload-gatekeeper met 814 downloads per maand, alleen v3 (GEZIEN). Leeg veld, en straks moet iedereen naar v4.
- Auditlog: payload-auditor 6.564, @trieb.work/payload-audit 1.845 (GEZIEN). Maar Payload 4 zet `createdBy` en `updatedBy` al standaard in de kern, dus het eenvoudige deel verdwijnt (GEZIEN, migratiegids).
- Vertalen: drie plugins tussen 3.000 en 11.000, plus Enterprise AI-vertalen. Bezet.

## Risico en waaraan je ziet dat het stokt
- Figma haalt Payload uit Make of maakt nieuwe kernfuncties alleen voor de gehoste versie; de licentie gaat van MIT naar iets strengers.
- npm-groei vlakt af, de v4-beta blijft hangen, of 3.x-releases stoppen voor 4 stabiel is.
- Voor een pluginmaker het grootste risico: wat goed loopt slokt de kern op (nested docs, import-export, audit-velden) of Enterprise (A/B, workflows, SSO).

## Categorie en eerste productidee (als het ooit ja wordt)
Rechten en rollen met een scherm voor Payload 4 ("wie mag wat", per collectie en veld, met rollen die een redacteur zelf kan aanpassen), gratis kern en een Pro met eigen licentie. Past bij de groep die Figma Make nu binnenbrengt: ontwerpers en marketeers die geen code willen schrijven voor rechten.

## Wat zou het cijfer veranderen
- Naar 6: Payload of Figma kondigt een plugin-lijst aan (in Make of op payloadcms.com) met installs of betalen, of er verschijnt een betaalde plugin van derden die aantoonbaar verkoopt (bijvoorbeeld 100+ kopers).
- Naar 3: npm-downloads zakken twee maanden op rij, of Payload zet rollen met een scherm in Enterprise.

## Herhaalmeting
Rond 8 jan 2027 (na de v4-beta, misschien stabiel): `python3 data/payload-plugins-meet.py` en vergelijk met `data/payload-plugins-2026-11-08.json` (nieuwe pakketten per maand, mediaan downloads, aantal met v4-ondersteuning, licenties niet-MIT). Kijk ook of payloadcms.com of Figma Make een plugin-lijst heeft.

Geen controleur ingezet: advies is geen ja en de kerncijfers zijn zelf gemeten (zelfde werkwijze als eerdere runs).
