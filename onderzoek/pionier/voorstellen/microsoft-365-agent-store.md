# Voorstel: Microsoft 365 Agent Store (agents in Copilot en Teams)

Noor, 9 nov 2026. Cijfer **5**, advies **nog niet klaar** (opnieuw zodra Thijs een KvK heeft; herhaalmeting 9 dec 2026 met `data/m365-agents-meet.py`).

## In het kort
De winkel zelf is jong en loopt nu snel vol met agents, op een platform dat hard groeit. Betalen werkt (eigen kassa mag, of via Microsoft voor 3%). Maar Thijs kan er nu niet in (bedrijfsverificatie vraagt een geregistreerd bedrijf), en van de 340 nieuwe agents sinds mei 2026 krijgt bijna niemand zichtbaar gebruikers. De winkel is vooral een plek voor bekende SaaS-merken die hun eigen dienst in Copilot hangen.

## Hoe gemeten
- Alle 11.609 Microsoft 365-apps (Office, Teams, Copilot) uit de sitemap van marketplace.microsoft.com, daarna per 30 id's opgehaald uit de openbare catalogus-API (api-version 2018-08-01-beta, geen sleutel nodig). 11.350 kwamen terug (GEZIEN, `data/m365-apps-2026-11-09.jsonl`, script `data/m365-agents-meet.py`).
- Een agent herken je aan de badge `CopilotExtension`. De id's (WA2000xxxxx) lopen op in de tijd, dus per blok van 500 id's zie je de instroom. De datum per blok is de vroegste `releaseDate` in dat blok; die schuift mee bij updates, dus de datums zijn bij benadering (GOK op de precieze dag).
- Een hulpagent zocht de groeicijfers, betaalregels en publicatie-eisen op; een controleur rekende alle tellingen met eigen code na en las de Learn-pagina's: alles klopt (één correctie: de nieuwe reeks begint ±mei, niet april).

## De vijf vragen

**1. Groeit het platform hard?** Ja.
- Betaalde Microsoft 365 Copilot-plaatsen: 15 mln (jan 2026), 20 mln (apr 2026), ruim 30 mln (jul 2026). DERDEN: https://www.directionsonmicrosoft.com/blog/microsoft-claims-15-million-paid-m365-copilot-seats, https://nojitter.com/ai-automation/microsoft-365-copilot-hits-20-million-paid-seats, https://www.uctoday.com/unified-communications/microsoft-365-copilot-passes-30-million-paid-seats-as-cloud-and-ai-growth-power-record-quarter
- Okt 2026 (FY27 Q1): dagelijkse Copilot-gebruikers 5 keer zo veel als een jaar eerder, 50 mln+ agents in het register (meest eigen agents van bedrijven). DERDEN: https://www.datastudios.org/post/microsoft-q1-fy27-results-azure-48-percent-33-2-billion-capex-45-2-billion
- Ook de hele Microsoft 365-winkel versnelt: 500 nieuwe app-id's duurden in 2023 tot 2024 ±4 maanden, nu ±3 tot 4 weken (GEZIEN, id-blokken; datums GOK).

**2. Is de winkel jong?** Ja, het agent-deel wel.
- Agent Store open sinds mei 2025 (DERDEN, https://devblogs.microsoft.com/microsoft365dev/introducing-the-agent-store-build-publish-and-discover-agents-in-microsoft-365-copilot/).
- 519 agents in totaal (GEZIEN). Per 500 id's: in 2025 ±10 tot 13 agents, begin 2026 30, daarna 34, 50, 55, 64 en in het blok van ±eind sep tot begin okt 2026 **100** (GEZIEN). De instroom is in een jaar ±8 keer zo hoog.
- Sinds ±mei 2026: 340 nieuwe agents, waarvan 47 van Microsoft zelf en 25 testapps; ±268 van ±220 andere makers (GEZIEN).

**3. Kan er betaald worden?** Ja, nu al, maar niet voor Thijs zonder KvK.
- Via Microsoft: een SaaS-aanbod koppelen aan de agent of Teams-app, Microsoft houdt 3% (GEZIEN, https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-commercial-transaction-capabilities-and-considerations).
- Eigen kassa mag: een link naar een externe betaalpagina; niet binnen Teams afrekenen en op iOS en Android geen prijzen tonen (GEZIEN, https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/teams-store-validation-guidelines). In de catalogus heeft 284 van de 519 agents `ExternalPurchase` (eigen account bij de maker nodig), 230 gratis, 5 met proefperiode, geen enkele met een prijs via Microsoft (GEZIEN).
- Publiceren vraagt een Partner Center-account met bedrijfsverificatie: "legally registered" bedrijf, wettelijke naam en adres, eigen domein, meestal 3 tot 5 werkdagen (GEZIEN, https://learn.microsoft.com/en-us/partner-center/enroll/understand-the-verification-process). Publisher Verification en Publisher Attestation zijn verplicht (GEZIEN, submission-checklist op Learn). Inschrijfkosten: geen gevonden (GOK).
- Testen in de echte Copilot vraagt een Microsoft 365-tenant met een Copilot-licentie (±$30 per maand, GOK) en is lastig in GitHub Actions.

**4. Is er vraag te zien?** Zwak.
- Van de 340 nieuwe agents hebben er 33 minstens één beoordeling in Teams/Copilot, 2 er tien of meer, het maximum is 19 (Draup for Sales); AppSource-beoordelingen: 0 (GEZIEN). Beoordelingen zijn in zakelijke winkels zeldzaam, dus dit zegt weinig over installs, maar er is geen enkel teken van een nieuwkomer die opvalt.
- Forums: vooral technische vragen; wel verzoeken om één tool voor doelen, feedback en 1-op-1's in Teams (DERDEN, https://techcommunity.microsoft.com/discussions/microsoftteams/anything-inside-teams-for-people-management-you-use-and-can-recommend/4518744) en klachten dat goede agents moeilijk te vinden zijn.
- Tegensignaal: beheerders zetten agents van derden juist uit (DERDEN, https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/how-to-remove-third-party-external-agents-from-the-copilot-agent/ba-p/4450518). Agents van externe partners staan standaard aan, maar in strakke organisaties beslist de IT-beheerder.

**5. Is de eerste plek in een categorie te pakken?** Misschien, maar niet bewezen.
- De meeste nieuwe agents zijn koppelingen van bestaande merken (Gamma, LegalZoom, Smartsheet, Databricks, Blue Yonder) naar hun eigen dienst. Losse agents zonder eigen SaaS zijn er weinig; wie ze maakt zijn kleine fabriekjes (Apps 365 & HR365 met 9 agents, ATM Bilgisayar met 3, Saifs AI 5) en die hebben nauwelijks beoordelingen.
- Grootste categorieën bij nieuwe agents: productiviteit 196, data-analyse 142, financiën 58, verkoop 54, juridisch en HR 48 (GEZIEN). Een categorie zonder nummer één zou "Europese regels in Word en Outlook" kunnen zijn (bijvoorbeeld AI Act- en AVG-controle van documenten, e-facturen volgens EU-norm), maar of iemand die koopt, konden we niet meten.

## Risico
Het platform haalt het wel (Microsoft, 30 mln+ betaalde plaatsen). Het risico zit in de winkel: Microsoft vult zelf gaten (47 eigen agents sinds mei), beheerders blokkeren derden, en een kleine maker zonder verkoopteam wordt niet gevonden. Teken dat het stokt voor ons: over een maand nog steeds geen nieuwe agent van een kleine maker met 10+ beoordelingen.

## Eerste productidee (als het ooit ja wordt)
Een agent "EU-check" voor Word en Outlook: controleert een document of e-mail op AVG-punten en AI Act-meldplichten, met eigen abonnement (bijvoorbeeld €9 per gebruiker per maand) via een externe betaalpagina. Geen eigen SaaS nodig behalve een kleine server voor licenties.

## Cijfer en advies
**5, nog niet klaar.** Groei (1) en jonge winkel (2) zijn sterk, betalen (3) werkt nu al met lage afdracht. Wat het tegenhoudt: Thijs kan zonder KvK niet publiceren, er is geen enkel bewijs dat een nieuwe agent van een kleine maker gebruikers of verkopen krijgt (4), en de winkel is vooral voor merken met een eigen dienst (5). Testen in de echte app kost een Copilot-licentie.
Opnieuw bekijken: zodra de KvK er is, en bij de herhaalmeting op 9 dec 2026 (instroom per id-blok en beoordelingen van nieuwe agents van kleine makers). Een 6 of 7 als er een kleine maker met een losse betaalde agent zichtbaar gebruikers krijgt. Misschien later iets voor Kees: een steekproef van losse agents met een prijs op de eigen site.
