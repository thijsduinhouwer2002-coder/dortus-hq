# Attio App Store (apps voor de CRM Attio, App SDK)

Noor, run 9 nov 2026 08:39 UTC. Zelf gevonden: gezocht naar jonge, hard groeiende zakelijke software met een app-winkel waar betalen nu al werkt. Claim-commit 027f4b3. Nagekeken door een controleur (hulpagent, alles zelf opnieuw gelezen met curl).

## Advies: ja, met kleine inzet. Cijfer 6

Attio is de CRM die op dit moment het hardst groeit onder start-ups (Lovable, Granola, Modal en Replicate gebruiken het). De App SDK is pas sinds 11 augustus 2026 stabiel (versie 1.0), de winkel heeft 294 apps waarvan 166 van derden, en er komen er ±20 per maand bij. Betalen werkt nu al: kleine studio's verkopen apps die alleen voor Attio bestaan met hun eigen kassa voor $29 tot $199 per maand, en Attio vraagt geen afdracht. Dat past precies bij de koers van 8 nov: zakelijke klanten die al voor zulke hulpmiddelen betalen.

Waarom geen 7: (1) vraag kon ik niet direct meten, het forum (community.attio.com) en het feedbackbord staan dicht voor onze proxy en Reddit ook; (2) er is geen verkoopcijfer van een app, alleen prijzen en installs; (3) apps die na mei 2026 kwamen halen tot nu toe mediaan 3 tot 6 installs, dus de winkel geeft een nieuwkomer weinig vanzelf; (4) de ontwikkelaarsvoorwaarden geven Attio een eeuwige licentie op de broncode van SDK-apps (zie risico). Eén verkoopcijfer van een betaalde utility-app, of zichtbare vraag naar de gekozen categorie, maakt dit een 7.

## De vijf vragen

### 1. Groeit het platform hard en zichtbaar? Ja
- Aug 2025: "5,000 paying customers" en "on track to 4x ARR growth this year", Series B van $52 mln geleid door GV (GEZIEN, https://attio.com/blog/attio-raises-52m-series-b, nagekeken).
- Nu op de homepage: "Trusted by 30,000+ customers", 2,6 mld API-aanvragen per maand, 30 mln MCP-aanroepen per maand, 76.000 actieve agents van klanten (GEZIEN, https://attio.com, nagekeken). Let op: 30.000 "customers" is niet hetzelfde als 5.000 betalende klanten; de groei is dus niet zuiver ×6, maar wel duidelijk.
- Bouwers groeien het hardst: het npm-pakket `attio` (de App SDK) had 7.230 downloads in jan 2026, 7.039 in feb, 15.878 in mei, 59.482 in jun, 27.074 in sep en 52.608 in okt (GEZIEN, https://api.npmjs.org/downloads/range/2025-04-01:2026-11-08/attio, nagekeken). Ruwweg ×7 in een jaar.
- Motor: veel risicogeld (totaal ±$116 mln, DERDEN, https://geo.sig.ai/brands/attio.md), een trend die meetrekt (AI-agents en "vibe coden" van apps in de CRM), en klanten die zelf snelgroeiende start-ups zijn.

### 2. Is de winkel jong? Ja
- Developer Platform aangekondigd in 2025, App SDK eerst als `0.0.1-experimental`, **stabiel 1.0 op 11 aug 2026**, daarna 1.0.1 tot 1.1.0 (GEZIEN, https://docs.attio.com/changelog/app-sdk.md, nagekeken).
- 294 apps in de openbare winkel, 128 officieel (van het bedrijf achter de dienst, of van Attio zelf: 32 apps), 166 van derden; 238 verschillende makers (GEZIEN, ingebedde JSON op https://attio.com/apps, op app_id geteld, nagekeken; bestand `data/attio-apps-2026-11-09.json`).
- Nieuwe apps per maand (aanmaakdatum van de app, niet de publicatiedatum, dus een benadering): 2025 apr 32 (start), mei 9, jun 6, jul 4, aug 10, sep 7, okt 5, nov 10, dec 20; 2026 jan 13, feb 21, mrt 17, apr 14, mei 26, jun 24, jul 8, aug 20, sep 24, okt 18 (GEZIEN). Gestaag ±20 per maand, geen golf die al wegzakt.
- Per categorie (een app kan in meer zitten): data en verrijking 75, automatisering 72, bellen 35, analyse 26, communicatie 24, productbeheer 14, facturatie 12, klantenservice 10, e-mailreeksen 8, formulieren 8, opslag 5 (GEZIEN).

### 3. Kan er betaald worden? Ja, nu al, met eigen kassa
- Attio heeft geen eigen kassa voor apps. De docs (alle 9 pagina's onder /share/ en llms.txt) zeggen niets over prijzen, afdracht of een verbod op betaalde apps (GEZIEN, nagekeken). De ontwikkelaarsvoorwaarden (laatst bijgewerkt feb 2026) noemen ook geen afdracht (GEZIEN, https://attio.com/legal/attio-developer-terms).
- In de praktijk verkopen makers wel, met hun eigen abonnement (GEZIEN, prijspagina's, nagekeken):
  - Forms van dialed technologies (attioforms.com): gratis, $49, $99 en $199 per maand. 467 installs.
  - Dedupe van dialed (usededupe.com): $145 eenmalig of vanaf $35 per maand. 45 installs.
  - Deduptio van Craftt (deduptio.com): gratis, $39 per maand of $390 per jaar, $500 eenmalige opschoning. 46 installs.
  - AttiBooks van Craftt (attibooks.com, QuickBooks-facturen): gratis tot 10 facturen, daarna $29 per maand of $290 per jaar. 63 installs.
  - Kolaai (attio.kolaai.com: Cal.com Sync 1.534 installs, Round Robin Pro, Jira Sync) en Neon Deer Data Labs (één abonnement voor al hun Attio-apps, naar grootte van de werkruimte) hebben ook prijspagina's.
- Wie betaalt: start-ups en hun sales- en ops-mensen, per werkruimte, maandelijks of jaarlijks. Prijzen zijn veel hoger dan bij onze andere platformen ($29 tot $199 per maand tegen $6 eenmalig bij Rollwright).
- Kosten vooraf: geen bekend. Een ontwikkelaarsaccount is gratis; Thijs moet het aanmaken en de voorwaarden accepteren. Een eigen server (of serverfuncties in de SDK) en Stripe voor het abonnement zijn nodig.

### 4. Is er al vraag te zien? Deels, indirect
- Niet direct te meten: community.attio.com en feedback.attio.com geven een fout via de proxy, Reddit 403; Hacker News levert niets bruikbaars (GEZIEN door controleur).
- Indirect wel: twee studio's (dialed technologies met 10 apps, Craftt met 3) bouwen de ene betaalde Attio-app na de andere; dat doe je alleen als het verkoopt (GOK, logisch maar geen bewijs). Kleine makers halen 1.000+ installs met een simpele koppeling: Calendly-sync van Neon Deer 1.554, Cal.com Sync van Kolaai 1.534, Apollo Enrichment van Neon Deer 1.221 (GEZIEN).
- Xero: er is geen Attio-app voor Xero, terwijl er kant-en-klare Zapier-, Pipedream- en Albato-recepten "Attio + Xero" bestaan (DERDEN, https://zapier.com/apps/attio/integrations/xero/255644650/update-or-create-records-in-attio-whenever-sales-invoices-are-updated-in-xero). Mensen plakken het dus nu met losse automatisering aan elkaar. Attio komt uit Londen, veel klanten zitten in het VK en Europa, waar Xero groot is (GOK).

### 5. Is de eerste plek in een categorie nog te pakken? Ja, in een paar hoeken
- **Duplicaten: vol.** Neon Deer (548), Origami (264), Deduptio (46), Dedupe (45).
- **Formulieren: vol.** Typeform (2.102), Fillout (1.674), Forms van dialed (467).
- **Boekhouding: open.** Alleen QuickBooks (AttiBooks, 63) en Stripe Invoicing (333). Geen Xero, geen Moneybird, Exact, Pennylane of FreeAgent (GEZIEN, zoeken op titel en omschrijving in alle 294 apps).
- **Rapportages en dashboards: open.** Geen enkele app met "report" of "dashboard" in titel of omschrijving (GEZIEN door controleur). Attio heeft wel eigen rapporten, dus eerst kijken wat ontbreekt.
- **Offertes en documenten: half.** PandaDoc (900, officieel), DocuPotion (29), Docusign via Fluidlabs (5). Geen eenvoudige "offerte als PDF uit een deal" van een kleine maker.
- Beste kans: **Xero-facturen en betaalstatus in Attio** (zoals AttiBooks voor QuickBooks, maar dan Xero, en later de Europese pakketten). Dat sluit aan op het voorstel van Tess (boekhoudkoppeling voor TikTok Shop met Moneybird, Exact, Pennylane): dezelfde kennis, twee platformen.

## Eerste productidee
"Xero voor Attio": vanuit elke deal of company een Xero-factuur maken (knop en workflow-blok), betaalstatus en openstaand bedrag terug als attribuut op het record, en een widget met de facturen van de klant. Gratis tot 10 facturen per maand, daarna $29 per maand of $290 per jaar (zelfde prijs als AttiBooks, waar mensen al voor betalen). De betaalde logica draait op onze eigen server; de SDK-app is alleen de schil (zie risico).

Daarna dezelfde app voor Moneybird, Exact en Pennylane, of een rapportage-app als de vraag daar groter blijkt.

## Risico
- **Attio bouwt het zelf.** Attio maakte al 32 eigen apps (Stripe, Notion, Apollo, lemlist, PandaDoc). Een eigen Xero-koppeling zou ons product wegvagen. Teken: "Xero" in de changelog van Attio.
- **Broncode.** De ontwikkelaarsvoorwaarden (2.4) geven Attio een eeuwige, onherroepelijke licentie op de broncode van SDK-apps, en een SDK-app kan niet worden verwijderd. Daarom de waardevolle logica op onze eigen server houden en alleen de schil in de SDK.
- **Weinig vanzelf.** Nieuwe apps sinds mei 2026 halen mediaan 3 tot 6 installs, apps van voor 2026 mediaan 17 tot 49 (GEZIEN). Gevonden worden moet dus ook via zoekwoorden ("Attio Xero integration" geeft nu alleen Zapier-achtige pagina's) en via Attio-bureaus.
- **Zakelijk werk.** Review door Attio (doel binnen een week), een video, Engelse teksten, en klanten die support verwachten. Geld van klanten raakt hun boekhouding: fouten zijn duur.
- **Platform stokt.** Teken: npm-downloads van `attio` twee maanden op rij lager dan 25.000, of minder dan 10 nieuwe apps per maand.

## Wat nog gemeten moet worden
- Herhaalmeting rond 9 dec 2026: `python3 -I data/attio-apps-meet.py data/attio-apps-<datum>.json data/attio-apps-2026-11-09.json` geeft nieuwe apps en groei van installs per app (vooral AttiBooks, Deduptio, Forms: groeien betaalde utility-apps?).
- Vraag naar Xero: als het forum ooit leesbaar is via de proxy, zoeken op "Xero" en "accounting".
- Een verkoopcijfer: makers als Craftt of dialed delen soms klantaantallen op hun blog of LinkedIn.
