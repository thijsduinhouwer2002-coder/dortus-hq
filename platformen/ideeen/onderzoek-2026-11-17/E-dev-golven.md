# Groep E: ontwikkelaarsgolven en migraties (17 nov 2026)

Alle pagina's gelezen met curl. Vraag 5 (voert een winkel kopers aan?) per tip apart bekeken.

### 1. .NET 11 en C# 15, einde support .NET 8 en 9
- Bestaat: JA. "Announcing .NET 11", Microsoft .NET Blog, 10 nov 2026: https://devblogs.microsoft.com/dotnet/?p=61205 . .NET 11 is een STS-release met twee jaar support; C# 15 brengt union types en closed hierarchies. Dat .NET 8 en 9 nu uit support gaan staat in nieuws (InfoWorld, pbxscience 13 nov 2026), niet zelf in de officiele supportpagina nagelezen: GOK dat de datum 10 nov 2026 klopt, wel heel waarschijnlijk.
- Migratietool van Microsoft zelf: JA, en gratis te gebruiken. De oude Upgrade Assistant is vervangen door "GitHub Copilot upgrade" (eerder "app modernization"). Werkt in Visual Studio, VS Code, Copilot CLI en GitHub.com, en werkt volgens de FAQ ook met **Copilot Free** (vanaf VS 2026 18.1): https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/faq . In de .NET 11-aankondiging noemt Microsoft daarnaast een ".NET Upgrade canvas" en ".NET Skills" voor agents. Ontwikkelaars klaagden eind 2025 dat de nieuwe tool slechter is dan de oude (devclass 20 nov 2025, techzine), maar het gat is er niet.
- Wat het echt is: een gewone jaarlijkse .NET-release plus het vaste einde van twee oudere versies. Microsoft levert de upgradetool zelf, ingebouwd in Copilot.
- Wet 1: nee. .NET-upgrades zijn elk jaar; geen nieuw platform of nieuwe winkel.
- Wet 2: deels. Elke .NET 8/9-ploeg moet migreren, maar het is een eenmalige klus.
- Wet 3: zwak. VS Code Marketplace heeft geen kassa; Visual Studio Marketplace laat betaalde extensies alleen via eigen licentie toe. Bedrijven betalen wel voor migratie, maar als dienst, niet als kleine tool.
- Wet 4: nee. Microsoft doet het zelf, gratis, in VS en VS Code (GEZIEN in de FAQ).
- Vraag 5: VS Code Marketplace voert wel kopers aan, maar daar staat Microsofts eigen "GitHub Copilot modernization" al met ±1,9 miljoen installs (GEZIEN via de Marketplace-API, 17 nov 2026).
- Mogelijk product: geen.
- Cijfer: 2. Microsoft bezit deze migratie zelf en geeft hem gratis weg.

### 2. Linear Agent API en open webhooks (12 nov 2026)
- Bestaat: DEELS. De Linear Agent API (Agent Interaction, agent-sessies, webhooks) bestaat al sinds 2025: https://linear.app/developers/agent-interaction.md en https://linear.app/developers/webhooks . Wat Linear op **12 nov 2026** uitbracht is iets anders: "Bring your own key" voor Linears eigen cloud-codeeragent: https://linear.app/changelog/2026-11-12-bring-your-own-key . Een nieuwe "Agent API en open webhooks" op 12 nov 2026: NIET GEVONDEN.
- Integratiedirectory: JA, https://linear.app/developers/integration-directory , met meer dan 250 integraties van derden. Maar letterlijk: "We'll accept integrations that we think are useful to the community and are built by formal companies. We generally do not accept scripts, low-effort/vibe coded or apps built by hobbyists". Aanmelden gaat via een formulier en mail, geen kassa; geld vragen kan alleen buiten Linear om (eigen abonnement).
- Wat het echt is: een bestaande API waarmee je een agent als "teamlid" in Linear zet, en een redactioneel beheerde lijst van integraties, geen winkel.
- Wet 1: nee. De API is ruim een jaar oud; het nieuws van 12 nov gaat over Linears eigen agent.
- Wet 2: nee. Een Linear-agent is een nis per gebruik (triage, standups).
- Wet 3: nee binnen Linear, alleen eigen kassa. Betaalcultuur onder Linear-teams is er wel.
- Wet 4: nee. Linear bouwt zelf een agent (Linear Agent, coding sessions, BYOK) en doet de brede basistaken dus zelf.
- Vraag 5: deels. De directory toont integraties, maar Dortus komt er als eenpersoons-hobbymaker waarschijnlijk niet in (GEZIEN in de regels).
- Mogelijk product: geen.
- Cijfer: 1. Toegang tot de etalage is voor ons vrijwel dicht en Linear doet het zelf.

### 3. Render Sandboxes en Cloudflare Sandboxes/Projects
- Bestaat: DEELS.
  - Render Sandboxes: JA, maar gelanceerd op **4 nov 2026** (public beta), niet 13 nov: https://render.com/blog/introducing-render-sandboxes . Firecracker-microVM per agent, SDK in TypeScript en Python.
  - Cloudflare Sandboxes: JA, maar al **algemeen beschikbaar sinds april 2026** (Agents Week): https://blog.cloudflare.com/agents-week-in-review . Een "Developer Week nov 2026" en een product "Cloudflare Projects": NIET GEVONDEN. Op de Cloudflare-blog (gelezen 17 nov) staan in november o.a. Spend Management (13 nov) en Kitesurf open source (13 nov), geen Developer Week.
- Wat het echt is: geisoleerde Linux-machines die je agent per taak opstart. Infrastructuur voor bedrijven die zelf agents bouwen.
- Wet 1: deels voor Render (2 weken oud), nee voor Cloudflare (7 maanden oud).
- Wet 2: nee. Alleen voor ontwikkelaars die agent-producten bouwen.
- Wet 3: nee. Geen winkel, geen kassa voor derden.
- Wet 4: nee. Render en Cloudflare leveren SDK, CLI en voorbeelden zelf; er zijn ook al tussenlagen (ComputeSDK met Render-provider, skills op skills.sh).
- Vraag 5: nee. Geen marktplaats bij Render; Cloudflare heeft geen winkel voor sandbox-tools.
- Mogelijk product: geen.
- Cijfer: 1. Infrastructuur zonder etalage en zonder kassa voor kleine makers.

### 4. Shopify Fall '26 Edition en nieuwe App Store-regels
- Bestaat: JA.
  - Fall '26 Edition voor ontwikkelaars, 28 okt 2026: https://www.shopify.com/news/fall-26-edition-developer . Shop.dev geeft elke agent of app een koppeling met Shopify Catalog, Shop-inlog, winkelwagen, checkout en Shop Pay, "with no key required". Plus Universal Checkout voor partners en **WebMCP-tools op elke Liquid- en Hydrogen-winkel en checkout**: "Every Shopify store is agent-ready by default."
  - Nieuwe regels, 10 nov 2026: https://shopify.dev/changelog/shopify-app-store-submission-requirements-build-grow-then-expand . Vier dingen: elke bestaande app moet 10 installs op volbetaalde winkels hebben voor je een volgende app mag aanmelden; oplopende wachttijd na elke afwijzing; verplichte ID-controle voor nieuwe apps; apps met 0 installs na zes maanden worden automatisch verwijderd.
- Wat het echt is: Shopify maakt zelf elke winkel klaar voor AI-agents en opent zijn catalogus en checkout voor elke agent. Tegelijk maakt Shopify de App Store strenger voor nieuwe makers.
- Wet 1: nee voor de App Store (bestaat jaren). Shop.dev is 3 weken oud, maar dat is een gratis koppeling, geen winkel.
- Wet 2: nee. "Agent-klaar maken van een winkel" was de brede basistaak, en die doet Shopify nu standaard zelf.
- Wet 3: ja. Shopify Billing API, sterke betaalcultuur onder winkeliers.
- Wet 4: nee. WebMCP en agent-checkout zitten standaard in elke winkel (GEZIEN). Een "maak je winkel AI-klaar"-app verkoopt lucht.
- Vraag 5: ja in theorie (zoeken, categorieen, uitgelicht), maar in de praktijk zwak voor nieuwkomers: onze eerdere meting was 2 tot 6 van de 100 nieuwe apps die 100 installs halen. De nieuwe regels maken het zwaarder: ID-controle (onbekend of dat voor een Nederlandse particulier zonder KvK soepel gaat, GOK: waarschijnlijk wel met paspoort), en we mogen pas een tweede app aanmelden als de eerste 10 betalende installs heeft.
- Mogelijk product: alleen een nisje rond "wat zien agents van mijn winkel" (controle van productdata voor de Catalog), maar Shopify heeft net de Catalog-filters en AI Toolkit zelf uitgebreid. Haalt de wetten niet.
- Cijfer: 2. Shopify doet het agent-stuk zelf en zet de deur voor nieuwe makers juist op een kier.

### 5a. Google Opal stopt op 17 nov 2026
- Bestaat: JA. Google zet Opal (no-code mini-app-bouwer van Google Labs) uit op 17 nov 2026 en vervangt het door Gemini Skills; Gems worden op dezelfde dag omgezet naar Skills voor persoonlijke accounts. Bron: AlphaSignal, 30 sep 2026, met link naar Googles aankondiging https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/ : https://alphasignal.ai/news/google-kills-opal-and-turns-gems-into-gemini-skills-for-free-users . Op killedbyai.net kon ik Opal NIET terugvinden in de tekst van de voorpagina (gelezen 17 nov).
- Wat het echt is: een gratis Google-experiment dat stopt. Volgens AlphaSignal is er geen automatische migratie voor Opal-projecten.
- Wet 1: ja qua timing (vandaag), maar er opent niets; het sluit.
- Wet 2: nee. Opal was een experiment met een kleine gebruikersgroep.
- Wet 3: nee. Opal-gebruikers betaalden niets; geen winkel om een exportdienst te verkopen.
- Wet 4: nee. Google wijst zelf Gemini Skills aan als opvolger.
- Vraag 5: nee. Geen winkel.
- Mogelijk product: geen. Een "Opal naar X"-exporttool heeft vanaf vandaag geen bron meer.
- Cijfer: 1. Te laat en zonder kopers.

### 5b. Claude Data standaard aan voor Enterprise op 20 nov 2026
- Bestaat: JA. "Introducing Claude Whiteboards, Claude Sheets, and Claude Data", claude.com, 10 nov 2026: https://claude.com/blog/sheets-whiteboards-data . Letterlijk: "On Enterprise plans, Claude Whiteboards and Sheets are off by default, and Claude Data turns on by default on November 20, 2026."
- Wat het echt is: Claude Dashboards wordt algemeen beschikbaar als Claude Data, met gecertificeerde queries, live delen en datastories. Partners zijn Amplitude, Mixpanel, Omni, PostHog, Sigma en ThoughtSpot.
- Wet 1: ja qua timing.
- Wet 2: nee voor ons. Het vraagt een datawarehouse-connector; dat is grote-bedrijvenwerk.
- Wet 3: nee. Geen kassa voor kleine makers in Claude Data; connectors en plugins zijn gratis te installeren.
- Wet 4: nee. Anthropic doet het zelf, met grote partners.
- Vraag 5: deels. Claude heeft een connector- en pluginmap, maar zonder betaalmodel voor derden (ONBEKEND of dat verandert).
- Mogelijk product: geen.
- Cijfer: 1. Het platform doet het zelf en er is geen kassa.

### 5c. AG-UI-protocol
- Bestaat: JA. Open protocol voor de verbinding tussen een agent en een gebruikersscherm (ag-ui-protocol/ag-ui op GitHub; de GitHub-pagina kon ik niet uitlezen, sterren en releases dus ONBEKEND). Primaire bevestiging dat het leeft: Microsoft noemt in de .NET 11-aankondiging (10 nov 2026) "Experimental Blazor AI components integrate with the Agent User Interaction Protocol (AG-UI)".
- Wat het echt is: een open standaard die frameworks (CopilotKit, Microsoft, LangGraph e.d.) zelf inbouwen.
- Wet 1: nee. Bestaat sinds 2025.
- Wet 2: nee. Alleen voor bouwers van agent-apps.
- Wet 3: nee. Open source, geen winkel.
- Wet 4: nee. De grote frameworks bouwen het zelf in.
- Vraag 5: nee. Geen winkel.
- Mogelijk product: geen.
- Cijfer: 1. Een protocol, geen markt.

### 5d. Token-limiet-tools zoals Burnstate
- Bestaat: JA. Burnstate staat op Product Hunt (https://www.producthunt.com/products/burnstate , datum 13 nov niet zelf kunnen zien, pagina zit achter een Cloudflare-check). Volgens huntscreens: een **macOS**-menubalk-app die gebruik en limieten van Claude, Codex, Cursor en Vercel bijhoudt: https://huntscreens.com/products/burnstate
- Winkel erbij? Gezocht naar de juiste etalage:
  - VS Code Marketplace (werkt op Windows, voert wel gebruikers aan): de categorie is al vol. Zoekterm "claude usage limit" (Marketplace-API, 17 nov 2026): Claude Usage Bar ±13.600 installs, Codex Rate Limit Monitor ±8.700, Claude Status Bar ±5.700, Claude Stats ±4.900, Claudemeter ±4.300, en nog minstens 10 andere met 1.400 tot 3.000. Allemaal gratis; de Marketplace heeft geen kassa.
  - Raycast Store: alleen gratis extensies (GOK op basis van wat ik weet, niet nagekeken), en Burnstate-achtige tools zijn vooral Mac.
  - Mac App Store: geen Mac bij Dortus.
- Wet 1: nee. De golf is al een jaar oud.
- Wet 2: ja. Iedere zware Claude Code- of Codex-gebruiker wil dit zien.
- Wet 3: nee. In de winkel die werkt (VS Code) kun je geen geld vragen; Burnstate zelf verkoopt via eigen site, dus Gumroad-probleem.
- Wet 4: nee. Claude Code toont gebruik en limieten zelf (statusregel, /usage), net als Codex.
- Vraag 5: ja voor VS Code Marketplace, maar wij zouden nummer 16 zijn.
- Mogelijk product: geen. Hooguit als gratis bereikproduct, maar zonder voorsprong.
- Cijfer: 2. Brede behoefte, maar te laat, gratis en deels al door het platform zelf opgelost.

### 6. HubSpot Marketplace en Vertex AI (kort)
- HubSpot: een specifieke Marketplace-wijziging in **nov 2026**: NIET GEVONDEN. De HubSpot-changelog (gelezen 17 nov) toont o.a. "fall-2026-spotlight", "october-2026-rollup", het einde van legacy private apps en legacy API's en het einde van oudere Node-versies. Eerdere wijzigingen aan listing- en certificeringseisen waren in mei 2026: https://developers.hubspot.com/changelog/app-listing-and-app-certification-requirement-updates-for-may-2026 . De Marketplace heeft etalage en betaalcultuur, maar geen eigen kassa (je rekent zelf af) en is al jaren oud. Wet 1: nee. Cijfer 2.
- Vertex AI: Vertex AI is op Cloud Next 2026 (april) opgegaan in "Gemini Enterprise Agent Platform"; de officiele release notes noemen een stopdatum van **26 nov 2026** voor een onderdeel met het advies "migrating to Agent Platform": https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes . Welk onderdeel precies stond buiten mijn uitsnede: ONBEKEND. Google levert eigen migratiegidsen, er is geen winkel en het is bedrijfswerk. Alle wetten nee. Cijfer 1.

## Top 2
Niets haalt een 7. Dit was een groep van migraties en infrastructuur, en bij bijna elke tip doet het platform het zelf (Microsoft Copilot upgrade, Shopify WebMCP, Linear Agent, Anthropic Claude Data) of is er geen winkel met kassa.

Als ik toch moet kiezen, de twee minst slechte:
1. **Shopify (cijfer 2)**: de enige tip met echte etalage en echte kassa (Billing API, betalende winkeliers). Maar het agent-stuk doet Shopify zelf en de nieuwe regels (ID-controle, 10 betalende installs voor een tweede app, verwijdering bij 0 installs) maken het voor een nieuwkomer zwaarder. Alleen zinvol als Dortus al een sterk, breed Shopify-idee heeft dat los staat van agents.
2. **Token-limiet-tool op VS Code Marketplace (cijfer 2)**: brede behoefte en een winkel die zelf gebruikers aanvoert, maar al 15+ gratis concurrenten en geen kassa. Hooguit een gratis bereikproduct, geen geldmaker.

Advies: groep E levert geen kandidaat op. Niet aan beginnen.
