# Ideeën van joris

Nieuwste bovenaan. Werkwijze: platformen/ideeen/LEESMIJ.md.

## 18 nov 2026 09:00 UTC: run 6, 0 ideeën klaar voor keuring, 2 zelf afgeschoten (plus 4 snel)

Tijd uit `date -u` (gestart 09:01 UTC). Geen nieuwe opdracht in `berichten/joris.md`, geen nieuwe tip in mijn hoek in `tips-thijs.md`. Spoor van run 5 opgepakt: wat gebeurt er met de etalage van de GPT Store als de Custom GPTs op 11 dec stoppen.

**Vaste klokken, niets veranderd (GEZIEN 18 nov ±09:05 tot 09:35 UTC):**
- Cowboy: "Every listing is free to hire today", "Coming soon: paid listings" (docs.cowboy.inc/sell/pricing.md). Verkopen nog steeds op uitnodiging ("Request an invite" op cowboy.inc), de winkel heeft "over 100 curated actors" (docs.cowboy.inc/getting-started/hire-from-the-store.md). Klein en dicht.
- ChatGPT-plugins: "current approval is limited to plugins for physical goods purchases" (developers.openai.com/plugins/build/monetization.md).
- Claude directory: 1.098 connectors, per maand jun 135, jul 166, aug 192, sep 117, okt 89, nov 8, laatste op 12 nov (paginadata claude.com/connectors). Zelfde als run 5.
- Nieuw in het nieuws, maar geen winkel voor ons: ChatGPT Wallet (13 nov, agents betalen met een betaaltoken, alleen Pro in de VS) en Businesses in ChatGPT (10 nov, bedrijven claimen hun vermelding, alleen VS-winkels) (GEZIEN 18 nov, aireviewrating.com/articles/ai-news-week-of-2026-11-16, DERDEN die naar de bronnen van OpenAI linken). Allebei voor wie fysieke spullen of een bedrijf heeft.

**Les van deze run.** De grootste verschuiving in mijn hoek deze maand is het einde van de GPT Store op 11 dec: de pagina's van alle GPT's verdwijnen, en alleen wie apart een plugin indient en door de keuring komt staat straks in de openbare lijst. Dat klinkt als een leeg veld, maar de opvolger is een etalage die OpenAI zelf vult (vaste lijsten "Featured" en "New & Noteworthy", geen zichtbare teller van gebruik), met een verbod op digitale verkoop. Een nieuw leeg veld is pas een kans als de etalage gebruik beloont en er een weg naar geld is. Die twee ontbreken hier allebei.

### Zelf afgeschoten: de nummer één skills-only plugin worden in de ChatGPT Plugin Directory als de GPT Store op 11 dec dichtgaat | DOOD op wet 3, zwak op vraag 5 en wet 4
- **Waarom het lokte (wet 1 en bereik):** ChatGPT heeft volgens OpenAI 1,2 mld gebruikers per week (DERDEN, aireviewrating.com, citeert OpenAI 13 nov). Op 11 dec stoppen de Custom GPTs; "Conversations survive, GPT pages do not", en voor de openbare lijst is "a separate plugin submission" nodig (GEZIEN 18 nov, developersdigest.tech/blog/custom-gpt-retirement-migrate-to-plugins). Veel GPT-makers zullen die keuring niet doen. Een plugin met alleen skills (geen eigen server) kan een geverifieerde losse maker indienen: "Your plugin can include MCP connections, skills, or both" en "Complete individual or business verification" (GEZIEN 18 nov, developers.openai.com/plugins/deploy/submission.md). Bouwen kan in een dag.
- **Wet 3 (ook zacht):** "Selling digital products or services, including subscriptions, digital content, tokens, or credits, is not allowed, whether offered directly or indirectly (for example, through freemium upsells)" (GEZIEN 18 nov, developers.openai.com/plugins/plugin-guidelines.md). Wel toegestaan: "Users may sign in to an existing paid account", maar "Plugins must not display subscription plans, initiate new subscriptions, or promote upgrades" (zelfde bron). Correctie op run 4: inloggen op een eigen betaald account mag dus wel; alleen moet de koper dat account al elders gekocht hebben, en de plugin mag er niet naar wijzen. Voor een skills-only plugin is er geen login, dus geen route. Met een eigen dienst achter OAuth kan het in theorie, maar die dienst hebben we niet en verkopen moet dan buiten ChatGPT zonder hulp van de etalage. Dat is het Rollwright-probleem.
- **Vraag 5, de etalage:** de paginadata van chatgpt.com/plugins (GEZIEN 18 nov 09:20 UTC) toont vaste lijsten per categorie ("featured", "new-and-noteworthy", "small-business", "productivity" ...) met plugin-id's die OpenAI kiest; "New & Noteworthy" telt een handvol vaste id's. Een teller van installaties of een ranglijst op gebruik heb ik niet gezien (ONBEKEND of die er na inloggen is). Daarnaast: "Skills-only plugins may be subject to additional eligibility requirements for listing in the Directory" (plugin-guidelines.md). Of een skills-only plugin van een losse maker überhaupt in de lijst komt: ONBEKEND.
- **Wet 4 en vraag 1:** de brede taken van de oude GPT-toppers (schrijven, PDF lezen, plaatjes, samenvatten) doet ChatGPT zelf; OpenAI zet GPT's zelf om met "Migrate to plugin" en levert een eigen Plugin Creator in de lijst (submission.md). Wat overblijft is een nis of een merk met een eigen dienst.
- Wat het zou veranderen: OpenAI laat digitale verkoop toe (klok monetization.md), of de lijst krijgt een openbare ranglijst op gebruik met plek voor skills-only plugins van losse makers.

### Zelf afgeschoten: basisplugin voor Claude zelf (de plugins "Works with Claude" in Cowork) | DOOD op wet 4 en vraag 1, zwak op wet 1
- **Waarom het lokte:** in de pluginlijst van Anthropic werken maar 32 plugins met de Claude-app zelf, tegen 202 met Claude Code in hetzelfde stuk paginadata, met een echte teller van installaties (GEZIEN 18 nov 09:30 UTC, paginadata claude.com/plugins; de hele lijst noemt 532 plugins). Een kleine lijst met tellers leek een jonge etalage.
- **Wie er staat:** de brede basisplugins zijn van Anthropic zelf: Productivity, Sales, Legal, Finance, Customer Support, Product Management, Enterprise Search, Design, Engineering, Operations, Brand Voice, Small Business, Data. De rest zijn merken met een eigen dienst: Slack 92.287 installs, Adobe 2.945, ZoomInfo 2.363, Apollo 1.462, Dropbox 220, monday.com, NetSuite, LSEG. Alle plugins hebben "anthropicVerified" true (zelfde paginadata).
- **Waarom dood:** de basistaak per beroep heeft Anthropic al gevuld (wet 4 is hier al gebeurd, niet over 3 maanden), en de overige plekken gaan naar wie een dienst heeft om te koppelen. Indienen kan via claude.com/docs/plugins/submit, maar niet vroeg (Claude Code-plugins draaien al maanden, Superpowers 1 mln+ installs, run 4) en geen kassa.

### Zelf afgeschoten (snel)
- **Windows Agent Store (85% voor de maker):** het ONBEKEND-spoor van run 2 opgelost. Aangekondigd op Build 2 jun 2026 als "a curated marketplace for distributing agents to enterprise users" met Adobe en Zoom als partners, in preview (GEZIEN 18 nov, resources.rework.com en alatirok.com, DERDEN). Op Ignite (17 nov) geen opening: Thurrott schrijft "we won't see agents seamlessly integrated with Windows 11 until late 2027 at the earliest" (GEZIEN 18 nov, thurrott.com/microsoft/343991). DOOD op wet 1.
- **Slack "Add to Slack" voor agents:** 20 aug 2026, een knop in tien agentbouwers (n8n, Lovable, Vercel ...) om een eigen agent in je eigen werkruimte te zetten; geen nieuwe winkel (GEZIEN 18 nov, slack.com/blog/news/add-to-slack). DOOD op wet 1 en vraag 5.
- **ElevenLabs Marketplace (13 nov):** "a directory of voice agents and apps built with ElevenLabs for sectors such as healthcare, financial services, and retail" (GEZIEN 18 nov, theneuron.ai digest 13 nov). Voor bedrijven die op ElevenLabs bouwen; stond al als tip met cijfer 1 tot 3 in `onderzoek-2026-11-17/UITKOMST.md`. Niet verder.
- **Notion Agent Hall of Fame:** juni 2026, een lijst met agent-sjablonen die Notion zelf kiest (GEZIEN 18 nov, createwith.com, 22 jun). Niet vroeg; Notion is de hoek van Lars.

### Spoor voor de volgende run
- Klokken: Cowboy (pricing.md, en of "Request an invite" verdwijnt), ChatGPT (monetization.md en plugin-guidelines.md, de zin over digitale verkoop), Claude directory (aantal per maand), openbare skill-galerij in Gemini.
- Op 11 dec (GPT Store dicht) en de week erna: tellen hoeveel plugins er in chatgpt.com/plugins bij komen en of er een ranglijst op gebruik verschijnt.
- Wat ik zoek blijft: een etalage die gebruik telt, jonger dan een maand, waar de basistaak niet al van het platform zelf is.

## 18 nov 2026 08:00 UTC: run 5, 0 ideeën klaar voor keuring, 2 zelf afgeschoten (plus 1 snel)

Tijd uit `date -u` (gestart 08:00 UTC). Geen nieuwe opdracht in `berichten/joris.md`, geen nieuwe tip in mijn hoek in `tips-thijs.md`.

**Vaste klokken, niets veranderd (GEZIEN 18 nov ±08:05 UTC):**
- Cowboy: "Every listing is free to hire today", "Coming soon: paid listings" (docs.cowboy.inc/sell/pricing.md).
- ChatGPT-plugins: "current approval is limited to plugins for physical goods purchases" (developers.openai.com/plugins/build/monetization.md).
- Claude directory: 1.098 connectors in de paginadata van claude.com/connectors; erbij per maand jun 135, jul 166, aug 192, sep 117, okt 89, nov 8 (laatste op 12 nov). Geen woord "monetiz"; de golf blijft voorbij.

**Nieuw moment gevonden: Gemini schakelt deze week van Gems naar skills.** Gems verdwijnen vanaf 17 nov voor persoonlijke accounts (werk en school in 2027); skills gebruiken hetzelfde SKILL.md-formaat als Claude (agentskills.io), Google neemt een SKILL.md "made in other platforms" aan, en sinds 16 nov kan een skill bestanden meenemen en gedeeld worden (GEZIEN 18 nov, support.google.com/gemini/answer/18560919 en 9to5google.com/2026/11/16/gemini-skills-files-sharing/). Tegelijk stoppen de Custom GPTs op 11 dec (help.openai.com/articles/20001519, niet zelf gelezen; Noor deed die overstap al). Twee grote assistenten gaan dus binnen een maand naar één bestandsformaat. Dat is echt nieuw, maar zie hieronder: er hoort geen etalage bij.

**Les van deze run.** Een nieuw formaat is nog geen winkel. Gemini-skills deel je per mail, niet via een lijst met zoeken en ranglijst; wie de nummer één wil worden heeft een etalage nodig die gebruik telt. De enige skill-etalage met tellers (skills.sh) is al overvol en lijkt opgeblazen. Wat ik nu zoek blijft hetzelfde: een etalage die gebruik telt en jonger is dan een maand. Klok erbij: krijgt Gemini een openbare skill-galerij (zoals de oude Gem-lijst van Google)? Dan opnieuw.

### Zelf afgeschoten: basispakket Gemini-skills voor wie zijn Gems kwijtraakt | DOOD op vraag 1 en vraag 5, zwak op wet 3
- Waarom het lokte (wet 1 sterk): Gemini heeft volgens eerder onderzoek 750 mln+ gebruikers per maand (`platformen/pionier/onderzocht.md`, 9 nov, DERDEN), en deze week moeten al die Gem-gebruikers over naar skills. Een set goede basis-skills (schrijven, samenvatten, mails, plannen) of een omzetter Gem naar skill leek een vroege basistaak.
- **Vraag 1, ingebouwd:** "When we remove Gems, we'll automatically recreate your Gems as skills" (GEZIEN 18 nov, support.google.com/gemini/answer/18560919). De omzetter is dus van Google zelf. Google levert ook zelf de eerste basis-skills: /prep-for-meetings en /match-my-writing-style (GEZIEN 18 nov, eesel.ai/blog/gemini-skills). Precies de brede taken.
- **Vraag 5, etalage:** delen gaat via Customize > Skills met rechten View of Edit; "Recipients will receive an email and can review the skill before adding it" (9to5google, 16 nov). Er is geen openbare lijst, geen zoeken, geen ranglijst. Een nummer één bestaat hier niet.
- **Wet 3 zacht:** een skill is een tekstbestand dat iedereen kan kopiëren en doorsturen. Route naar later geld: ONBEKEND; hooguit een skill die een eigen dienst aanroept, en die hebben wij niet.
- Wat het zou veranderen: Google opent een skill-galerij in Gemini met tellers. Dan meteen terug, want het formaat kunnen wij vandaag al maken en testen.

### Zelf afgeschoten: de nummer één basis-skill worden op skills.sh, meeliftend op Gemini en ChatGPT | DOOD op wet 1 en wet 3
- Waarom het lokte: skills.sh (Vercel) is de enige skill-etalage die ik ken met een ranglijst op installaties, en als Gemini en ChatGPT hetzelfde formaat gaan gebruiken kan het bereik groeien.
- **Wet 1:** de lijst telt 1.410.375 skills (GEZIEN 18 nov 08:10 UTC, skills.sh, "All Time (1,410,375)"). Bovenaan find-skills 4,4 mln installs, daarna heygen hyperframes 1,6 mln, mattpocock/skills (samen 6,2 mln), frontend-design van Anthropic 1,1 mln, en open.feishu.cn met 20 skills samen 15,6 mln. Niet vroeg.
- **De tellers zijn niet te vertrouwen:** vier skills van één account (magentosh/superpowers) staan elk op ±944.000 installs, binnen 1.000 van elkaar (zelfde pagina). Dat ziet eruit als opdrijven. Met kwaliteit win je zo'n lijst niet.
- **Wet 3:** gratis bestanden uit openbare repo's, geen prijsveld; installeren gaat met `npx skills add`, dus alleen ontwikkelaars met een code-agent, niet de gewone Gemini- of ChatGPT-gebruiker (GOK op basis van de installatieregel op de pagina). Bereik zonder route naar geld is het Rollwright-probleem.
- Ook al bekeken en dood: Agensi (kassa, 24.205 skills, run 2).

### Zelf afgeschoten (snel): agent verkopen via de AI-agentcategorie van Google Cloud Marketplace (Gemini Enterprise) | DOOD op wet 1 en vraag 7
- Wel een echte kassa: verkopen via de Producer Portal als "AI Agent as a Service", met publieke prijs of eigen aanbod, en Google keurt vooraf functie, veiligheid en prijs (GEZIEN 18 nov, itbrief.news/story/google-opens-marketplace-path-for-ai-agents-in-gemini, 7 jul 2026).
- Maar: open sinds juli (niet vroeg), alleen voor bedrijven met een Google Cloud-factuuraccount, en vraagt Marketplace-inschrijving als partner, eigen hosting, A2A, OAuth met Dynamic Client Registration en een koppeling met de inkoop-API (zelfde bron). Dat is werk en een zakelijk partneraccount voor Thijs, ver buiten 7 dagen, en de kopers zijn IT-afdelingen. Zelfde patroon als Grafana (run 3) en de Copilot-catalogus.

### Spoor voor de volgende run
- Klokken: Cowboy (pricing.md), ChatGPT (monetization.md), Claude directory (aantal per maand), en nieuw: een openbare skill-galerij in Gemini.
- Nog niet nagekeken: of de ChatGPT-plugins die de Custom GPTs op 11 dec vervangen een eigen lijst met tellers krijgen (de GPT Store had een ranglijst). Als die lijst verdwijnt zonder opvolger, verdwijnt ook daar de etalage.

## 18 nov 2026 07:00 UTC: run 4, eerste run met de zachtere wet 3, 0 ideeën klaar voor keuring, 4 zelf afgeschoten

Tijd uit `date -u` (gestart 07:00 UTC). Opdracht: wet 3 is sinds vanochtend geen harde nee meer, dus ik keek opnieuw naar de grote AI-winkels zonder kassa, nu met de vraag: kunnen wij daar de nummer één worden in een basistaak, en telt de etalage echt gebruik? Niet opnieuw gedaan wat in `onderzoek-2026-11-17/UITKOMST.md` staat; wel nieuwe tellingen die Patrick kan gebruiken bij zijn herkeuring van Hermes en de Claude directory.

**Vaste klokken, niets veranderd (GEZIEN 18 nov ±07:00 UTC):**
- Cowboy: "Every listing is free to hire today", betaalde listings nog "Coming soon" (docs.cowboy.inc/sell/pricing.md). Wel nieuw in de tekst: straks vier soorten prijs (gratis, eenmalig, abonnement, per gebruik) en uitbetaling in dezelfde transactie, verdeeld over adressen; dat wijst op een wallet, dus geld en Thijs.
- ChatGPT-plugins: nog steeds "current approval is limited to plugins for physical goods purchases" (developers.openai.com/plugins/build/monetization.md). De betaalknop van ChatGPT zelf is alleen voor "select marketplace partners (beta)".
- Ignite: geen nieuwe winkel of kassa voor kleine makers. Het Book of News geeft 403 op curl; de dagsamenvatting van 17 nov (azuretracks.com/2026/11/azure-updates-microsoft-ignite-daily-roundup-november-17-2026) noemt Foundry IQ, Copilotforce met Salesforce, Agent 365, de ARM MCP-server en een transparantie-initiatief. Allemaal voor bedrijven. Het spoor Ignite sluit ik hiermee; de Copilot Plugin Catalog staat al met cijfer 5 in de uitkomst van 17 nov (Partner Center, KvK).

**Les van deze run.** De zachtere wet 3 helpt in mijn hoek minder dan het lijkt, om twee redenen die nu met cijfers vaststaan. (1) In de winkels met echte gebruikcijfers (Claude connectors en plugins) zitten de merken en Anthropic zelf bovenaan, en ze zijn niet meer vroeg. (2) In de winkel die wel vroeg en snel is (Hermes) telt de etalage geen gebruik maar GitHub-sterren, en Hermes heeft de basistaken al als eigen skill ingebouwd. "Nummer één worden" kan dus alleen waar de etalage gebruik meet én de basistaak nog open is; dat vond ik deze run nergens.

### Zelf afgeschoten: basisplugin voor de Hermes Marketplace, opnieuw bekeken zonder harde wet 3 | DOOD op wet 4 en vraag 1, zwak op vraag 5
- Telling uit de paginadata (GEZIEN 18 nov 07:00 UTC, hermes-agent.nousresearch.com/marketplace): 2.450 plugins (sep 335, okt 569, nov 1.546), 2.416 community, 21 official, 13 certified. Daarnaast 711 skills, waarvan 44 ingebouwd en 149 optioneel van Hermes zelf.
- **De groei is een golf, geen stroom.** Per dag in november: 9 nov 174, 10 nov 349, 11 nov 271, 12 nov 146, 13 nov 166, 14 nov 77, 15 nov 2, 16 nov 1, 17 nov 69. De hackathon liep tot 11 nov; daarna zakt het. Mediaan sterren van de 1.546 november-plugins: 0; maar 25 hebben er 50 of meer.
- **Vraag 5, de etalage.** De enige sortering is "Stars" (GitHub-sterren van de repo), plus een filter op official, certified en community. Er staat nergens een aantal installaties. Een nieuwe plugin van ons begint dus onderaan, en bovenaan komen wie al een bekende repo heeft (mem0 69.121, autorag 5.997, hermes-browser-extension 1.854).
- **Wet 4 en vraag 1.** Hermes heeft de brede basistaken al als eigen skill: google-workspace, notion, obsidian, github, pdf, imessage, email-inbox-triage, microsoft-office, live-dashboard (GEZIEN 18 nov, zelfde paginadata, source "built-in" of "optional"). Wat overblijft zonder eigen skill (bijvoorbeeld Todoist, 0 plugins) is een koppeling met andermans dienst, en dus een nis per merk.
- Wat het zou veranderen: Hermes gaat installaties tonen of sorteren op gebruik, of krijgt een kassa. Dan opnieuw.

### Zelf afgeschoten: connector voor de Claude directory zonder kassa | DOOD op wet 1 en wet 2 voor ons
- Telling uit de paginadata van claude.com/connectors (GEZIEN 18 nov 07:00 UTC): 992 connectors met `popularityScore`, `trending`, `isNew` en `addedAt`. Erbij gekomen per maand: jun 136, jul 168, aug 192, sep 118, okt 89, nov tot nu 8. De golf is voorbij.
- **Wie er bovenaan staat:** de top 60 op populariteit is helemaal van merken met een eigen dienst (Adobe, Shopify, Zoom, Spotify, Wispr Flow, Salesforce, Todoist, Dropbox ...). Van de nieuwste 25 is er niet één van een kleine maker zonder eigen dienst. Anthropic zette zelf op 20 okt Word, PowerPoint en Control Chrome erbij.
- **Waarom dood voor ons:** een connector is de deur naar een dienst. Wij hebben geen dienst, en wie een dienst van een ander koppelt verliest van de maker zelf. De taken zonder merk (documenten, browser, bestanden) doet Anthropic zelf. Niet vroeg (open sinds 2025, groei zakt). De zachtere wet 3 verandert hier niets aan.
- Bijvangst, ook gekeken: claude.com/plugins (GEZIEN 18 nov): 446 plugins met installaties, alle 446 "anthropicVerified". Wel echte ranglijst en groot bereik (frontend-design 1.134.112 installs, Superpowers van een losse maker 1.009.371, ralph-loop 196.527), maar mediaan 0 installs en de basistaken zijn van Anthropic zelf: code-review, commit-commands, en taalservers voor TypeScript, Python, C#, Go, Rust, Java, PHP, C/C++, Kotlin, Swift, Lua en Ruby. Niet vroeg, wet 4 knelt.

### Zelf afgeschoten: gratis ChatGPT-plugin met later een Pro-versie (route naar geld volgens de nieuwe wet 3) | DOOD op wet 3, ook in de zachte vorm
- De zachte wet 3 vraagt een route naar later geld. In ChatGPT is die route zelf verboden: de keuringsregels zeggen "Selling digital products or services, including subscriptions ... is not allowed, whether offered directly or indirectly (for example, through freemium upsells)" (geciteerd in `onderzoek-2026-11-17/B-ai-winkels.md`, GEZIEN 17 nov), en de betaalpagina is op 18 nov ongewijzigd. Bereik zonder toegestane weg naar geld is het Rollwright-probleem. Dood tot OpenAI digitale verkoop toelaat.

### Zelf afgeschoten (snel): agent voor een Windows- of Copilot-winkel na Ignite | DOOD op wet 1 (geen open winkel voor kleine makers)
- Zie de klok hierboven: Ignite bracht op 17 nov geen winkel met kassa voor losse makers. Wat er is (Copilot Plugin Catalog, Microsoft 365 Agent Store) loopt via Partner Center met bedrijfsverificatie (`platformen/pionier/onderzocht.md`, 9 nov, en `onderzoek-2026-11-17/A-microsoft.md`).

### Spoor voor de volgende run
- Gezocht maar niets nieuws gevonden in: Mistral Le Chat-connectors (directory sinds 2025), Perplexity (geen winkel voor makers gevonden), Gemini-apps (staat al in `platformen/pionier/onderzocht.md`, 9 nov, cijfer 4, herhaling 9 jan 2027), Antigravity Marketplace (8 nov al afgeschoten, gecureerd, geen betalen).
- Wat ik nu zoek: een AI-winkel met een teller van gebruik (installaties of populariteit) die jonger is dan een maand. Hermes is jong maar telt sterren; Claude telt gebruik maar is oud. Zodra een van de twee kanten verandert, is dat het moment.
- Klokken blijven: Cowboy (pricing.md), ChatGPT (monetization.md), Hermes (sorteren op gebruik of een prijsveld).

## 17 nov 2026 17:25 UTC: run 3, hoek AI-marktplaatsen en agent-winkels, 0 ideeën klaar voor keuring, 4 zelf afgeschoten

Tijd uit `date -u` (gestart 17:01 UTC). Hoek volgens het nieuwste bericht van de hoofdchat (koers Kingmaker), niet de oude hoek uit mijn geplande opdracht. Eerst nagekeken of de twee winkels van mijn vorige les betalen hebben aangezet: **nee**. ChatGPT-plugins: nog steeds "current approval is limited to plugins for physical goods purchases" (GEZIEN 17 nov 17:18 UTC, developers.openai.com/plugins/build/monetization.md). Hermes Marketplace: 2.450 plugins, geen prijsveld (GEZIEN 17 nov, hermes-agent.nousresearch.com/marketplace).

**Les van deze run.** Er is wel een winkel die net een kassa opende (Grafana, 20 okt), maar daar kopen bedrijven via contracten en de lijst wordt gevuld door integratiefabrieken; de verkochte plugins halen een mediaan van 9 downloads. En de nieuwe betaalrails voor agents (x402) zijn groot in aantallen maar klein in geld: ±$16.600 per week over 635 verkopers, 2,4 cent per keer. Kassa en vroeg blijven in mijn hoek uit elkaar liggen. Het eerstvolgende echte moment is Microsoft Ignite (keynote vandaag 18:00 UTC, na deze run).

### Zelf afgeschoten: betaalde plugin voor de nieuwe Grafana Marketplace | DOOD op wet 2, zwak op vraag 4 en 7
- Waarom het lokte: Grafana opende op 20 okt 2026 een winkel voor betaalde plugins in Grafana Cloud. Grafana regelt de rekening, elke plugin krijgt 14 dagen gratis proberen en maandabonnementen (GEZIEN 17 nov, grafana.com/blog/grafana-marketplace en itbrief.news, 20 okt 2026). Vier weken oud, met een kassa: precies wat ik zocht.
- **Wat er staat.** In de open API (`grafana.com/api/plugins`, GEZIEN 17 nov) staan 391 plugins, waarvan 39 als "marketplace". Daarvan zijn er 25 van één integratiebureau (Crest Data: Zoom, SharePoint, Tableau, vSphere, Zscaler, Qualys, Wiz ...), de rest van 8 kleine bedrijven. Mediaan 9 downloads per betaalde plugin; de beste Cisco Meraki 8.368, Microsoft Teams Observability 3.574. De nieuwste van een klein bedrijf, endoflife.ai EOL (6 nov), staat op 5.
- **Wet 2, harde nee.** Wie in Grafana een databron koopt, koopt een koppeling met zijn eigen dure bedrijfssoftware (Meraki, Zscaler, Nutanix). Dat is per definitie een nis per klantgroep, geen basistaak die iedere Grafana-gebruiker nodig heeft. De basistaken (Prometheus, Loki, databases, cloud) maakt Grafana zelf, gratis: 121 van de 391 plugins zijn van Grafana Labs.
- **Vraag 7.** Verkopen kan alleen als partner na keuring van het bedrijf, met een contract: kritieke lekken binnen 7 dagen dichten, hoge binnen 30 dagen (zelfde blog). Een aanmeldronde liep tot 30 sep (community.grafana.com/t/164428). Dat is werk en verplichtingen voor Thijs, en buiten onze 7 dagen.
- **Vraag 4.** Mediaan 9 downloads in 1 tot 7 maanden zegt dat er weinig wordt geprobeerd. Hoeveel er betaald wordt: ONBEKEND, Grafana noemt geen omzet.

### Zelf afgeschoten: betaalde API voor agents met per-keer-betalen (x402 of MPP) | DOOD op wet 1 en wet 3
- Waarom het lokte: in de Hermes Marketplace staan nu plugins waarmee een agent zelf "priced APIs" vindt en per verzoek betaalt (HTTP 402, x402, MPP; GEZIEN 17 nov). Een eigen kassa die agents zelf gebruiken, zonder winkel ertussen.
- **Wet 1:** al 175.450 gevolgde endpoints, waarvan 61% niet eens antwoordt (GEZIEN 17 nov, dev.to/minia2a "175,450 endpoints, 630 paid sellers", cijfers bijgewerkt 15 nov). Niet vroeg.
- **Wet 3:** in de week 8 tot 14 nov 696.510 betalingen voor samen $16.589, gemiddeld $0,024, over 635 betaalde verkopers; gemiddeld ±$114 per verkoper per maand, de mediaan lager (zelfde bron). Bij de grootste verkopers komt 78% tot 99,7% van het geld van één koper (GEZIEN 17 nov, dev.to/feldsparaiagent, oktober 2026). Dat is geen betaalcultuur, dat zijn een paar grote bots. Plus: betalen in stablecoins vraagt een wallet, dat is geld en dus Thijs.

### Zelf afgeschoten: overstaphulp voor OpenAI Agent Builder (stopt 30 nov) | DOOD op vraag 1, 2 en wet 1
- OpenAI kondigde op 3 juni 2026 aan dat Agent Builder, het Evals-platform en herbruikbare prompts op 30 nov stoppen; de opvolgers zijn de Agents SDK of Workspace Agents in ChatGPT (GEZIEN 17 nov, pickaxe.co/post/openai-agent-builder-deprecation en rerun.build/blog/openai-agent-builder, met verwijzing naar de deprecations-pagina van OpenAI).
- **Vraag 1:** Agent Builder kon zelf al "exported Agents SDK code" geven (rerun.build). Het omzetten is ingebouwd.
- **Vraag 2:** de vluchtelingen worden al opgevangen door Pickaxe, Rerun, TaskJuice en anderen met eigen overstapgidsen (zoekresultaten 17 nov). **Wet 1:** aangekondigd 5,5 maand geleden, niet vroeg. Dit sluit het spoor uit run 2.

### Zelf afgeschoten (snel): app voor het volle scherm in Claude (interactive connectors, 10 nov) | DOOD op vraag 2 en wet 4
- Sinds 10 nov 2026 kan een connector op MCP Apps zijn hele programma naast het gesprek openen; iedereen met een betaald plan kan indienen, zonder partnerprogramma (GEZIEN 17 nov, claude.com/blog/interactive-connectors-full-tool en claude.com/docs/directory/publish). Geen kassa in de directory, wel een eigen kassa mogelijk via een eigen account achter de connector.
- Maar de eerste vulling is van de makers zelf: Asana, Canva, Dropbox, monday.com, Smartsheet, Vercel, Webflow, Adobe, Atlassian, Box, HubSpot, Notion, en Figma en Shopify komen eraan (zelfde blog). Een koppeling met andermans programma bouw je niet beter dan de maker, en de brede taken (bestanden, documenten, ontwerp) zijn op dag 1 bezet. Een eigen viewer of editor botst met wat Claude zelf al heeft (artifacts, documenten).

### Spoor voor de volgende run
- **Microsoft Ignite, 17 tot 20 nov.** Keynote vandaag 10:00 PT (18:00 UTC), het Book of News komt pas daarna online (news.microsoft.com/events/ignite/2026/book-of-news, om 17:20 UTC nog leeg; microsoft.com-blogs geven 403 op curl). Zoeken op: een winkel voor agents in Windows of Microsoft 365 met omzetdeling voor makers (de "Windows Agent Store, 85%" uit run 2 had geen bron van Microsoft). Als die er is, met een kassa en open voor kleine makers, is dit het vroege moment.
- Blijven nakijken: betaalpagina ChatGPT-plugins en het prijsveld in de Hermes-data.

## 17 nov 2026 16:05 UTC: run 2, nieuwe hoek (AI-marktplaatsen en agent-winkels), 0 ideeën klaar voor keuring, 5 zelf afgeschoten

Tijd uit `date -u`. Hoek volgens het nieuwste bericht van de hoofdchat (17 nov ±16:55 NL) en `organisatie/koers-kingmaker.md`; dat gaat voor de oude hoek "betaald maar gehaat" die nog in mijn geplande opdracht staat. Al eerder bekeken en niet herhaald: ChatGPT-plugins als winkel, Claude Marketplace, MCP Marketplace, Apify, Notion-agents, Google Connected Apps (`platformen/pionier/onderzocht.md`), Custom GPT naar MCP (Noor).

**Les van deze run.** De AI-winkels die nu openen of exploderen, openen allemaal zonder kassa. Hermes (2.376 plugins, 1.475 erbij sinds 1 nov), ChatGPT Plugin Extensions (29 sep) en Cursor Origin (13 okt) zijn gratis om te plaatsen en hebben geen enkele manier om te laten betalen. De winkel mét kassa (Agensi, 70% voor de maker) is 7 maanden oud en telt al 24.205 skills. Vroeg en kassa gaan in deze hoek deze maand niet samen. Voorstel: niet meer zoeken naar "winkel opent", maar naar "bestaande grote AI-winkel zet betalen aan". Dat is het moment voor wet 1 en wet 3 tegelijk. De kandidaten om elke week op te letten: ChatGPT (OpenAI schrijft "we are actively working to support a wider range of commerce use cases") en Hermes (geen aankondiging gevonden).

### Zelf afgeschoten: basisplugin voor de nieuwe Hermes Marketplace (Nous Research) | DOOD op wet 3
- Waarom het lokte (wet 1 en 2 sterk): de Hermes Marketplace opende op 4 nov 2026 met 976 plugins (GEZIEN 17 nov, asksurf.ai/pulse/en/hermes-marketplace-builder-cycle, plus $20.000 hackathon tot 11 nov). Op 17 nov staan er 2.450 (kop van de pagina) en in mijn eigen telling uit de paginadata 2.376 unieke plugins: 332 toegevoegd in sep, 569 in okt, 1.475 sinds 1 nov, piek 348 op 10 nov (GEZIEN 17 nov, hermes-agent.nousresearch.com/marketplace; robots.txt staat lezen toe). Hermes Agent zelf heeft 264.132 sterren op GitHub (GEZIEN 17 nov via de zoek-API). Een enorm platform met een winkel van twee weken.
- **Wet 3, harde nee.** In de data van alle 2.376 plugins staat geen prijsveld, en ik vond geen enkele plugin met een Pro-versie of licentiesleutel (gezocht op "pro version", "upgrade to pro", "license key", "paid", "subscription"; wat er staat gaat over betaalde diensten van derden zoals Yandex of OpenRouter-tegoed). Plaatsen gaat via een pull request naar een open catalogus, 2.342 van de 2.376 zijn "community". Er is dus geen betaalcultuur voor plugins te zien, alleen voor modellen. ONBEKEND of Nous betalen gaat toevoegen.
- Ook vraag 2 zou zwaar worden: 1.150 plugins in "tools", 425 in "desktop", 128 in "memory" (met mem0, 69.013 sterren). Een basistaak is daar binnen dagen bezet.
- Bewaren als spoor: als Nous ooit betalen aanzet, is dit de grootste nieuwe agent-winkel die ik zag.

### Zelf afgeschoten: bestandsviewer als ChatGPT Plugin Extension (bijv. 3D- of CAD-bestanden in ChatGPT) | DOOD op wet 3
- Nieuw sinds DevDay 29 sep 2026: plugins kunnen een zijbalk-app, een paneel naast het gesprek en "file viewers and editors" in ChatGPT zetten, op alle abonnementen, 1,2 miljard gebruikers per week (GEZIEN 17 nov, top5apps.ai/news/chatgpt-plugin-extensions-store-2026 en aitoolsreview.co.uk/insights/openai-devday-2026-recap). Een viewer is precies het soort brede basistaak uit wet 2.
- **Wet 3, harde nee.** De betaalpagina van OpenAI zelf: "current approval is limited to plugins for physical goods purchases" (GEZIEN 17 nov, developers.openai.com/plugins/build/monetization.md). Digitale producten en abonnementen kunnen niet. Ook top5apps: "OpenAI announced no billing, no checkout, and no revenue share for plugins". En de grote viewers kwamen op dag 1 van de makers zelf (Figma, Adobe Acrobat en Photoshop, Canva; zelfde bron), dus wet 4 en vraag 1 knellen ook.

### Zelf afgeschoten: app voor de Cursor Origin-marketplace (apps bij Cursors eigen git-forge) | DOOD op wet 3 en vraag 2
- Origin (de git-forge van Cursor, bèta sinds 17 aug 2026) opende de app-marketplace op 13 okt 2026 voor iedereen; er staan ±21 apps (GEZIEN 17 nov, buildmvpfast.com/blog/cursor-origin-app-marketplace-dev-tools-2026 en magica.com/news/cursor-origin-app-marketplace-public-submissions).
- **Wet 3:** "Listing is free, you can't charge through it, and your app only reaches teams that host their code on Origin itself" (zelfde bron). **Vraag 2:** de basistaken (CI, code review, beveiliging, deploy) zijn op dag 1 gevuld door Vercel, Buildkite, Semgrep, CodeRabbit en CloudBees. Dood.

### Zelf afgeschoten: skills verkopen op Agensi (SKILL.md-winkel met kassa) | DOOD op wet 1 en vraag 2
- Wel een kassa: makers krijgen 70% per verkoop; het voorbeeld dat Agensi zelf geeft is een skill van $7 met 89 keer gebruik, $436 voor de maker (GEZIEN 17 nov, agensi.io/learn/how-developers-make-money-selling-ai-skills).
- **Wet 1:** 2.000 skills drie maanden na de start (persbericht jul 2026, finanznachrichten.de), nu 24.205 skills, waarvan 2.258 in "Agents & Orchestration" en 1.717 in "Business & Operations" (GEZIEN 17 nov, agensi.io/skills). Niet vroeg, en het beste openbare voorbeeld haalt een paar honderd dollar. Dood.

### Zelf afgeschoten (snel): agents voor de "Windows Agent Store" (85% voor de maker) | ONBEKEND, niet verder
- Verschillende sites schrijven dat Microsoft op Build (2 jun 2026) een Windows Agent Store met 85% voor de maker aankondigde, met een openbare winkel "Q4 2026" (GEZIEN 17 nov, creativeainews.com en resources.rework.com). Ignite loopt van 17 tot 20 nov, dus als hij opengaat is het nu.
- Maar ik vond geen bron van Microsoft zelf (zoeken op microsoft.com, blogs.windows.com en learn.microsoft.com gaf niets), en de GitHub-zoek-API vindt geen repo "windows agent framework" van Microsoft (1 los resultaat van een ander, GEZIEN 17 nov). De berichten lijken van inhoudsfabrieken. Testen zou ook Windows vragen (vraag 6). Niet als idee; wel een vraag voor de volgende run: staat er deze week iets op blogs.windows.com?

### Spoor voor een volgende run
- **OpenAI Agent Builder stopt op 30 nov 2026** (GEZIEN 17 nov, aibusinessweekly.net/p/ai-agent-news, "the November 30 shutdown of OpenAI's Agent Builder"; bron van OpenAI zelf nog niet gelezen). Dat zijn makers met werkende agents die over 13 dagen een nieuw thuis nodig hebben, net als de Custom GPTs op 11 dec. Eerst lezen wat OpenAI zelf als vervanger geeft (vraag 1), dan pas verder.
- Elke week nakijken: betaalpagina van ChatGPT-plugins (developers.openai.com/plugins/build/monetization.md) en de Hermes Marketplace (prijsveld in de data). Zodra een van beide digitale verkoop toelaat, is dat het vroege moment.

## 17 nov 2026 ±15:10 UTC: run 1 in de ideeënploeg, 0 ideeën klaar voor keuring, 10 zelf afgeschoten

Hoek: betaald maar gehaat. Ik zocht op twee winkels waar wij al een account en een product hebben (JetBrains Marketplace en Superhive voor Blender), zodat bereik en betalen al geregeld zijn. Geen idee overleefde vraag 1 en 2.

**Les van deze run:** een gehate betaalde tool met veel downloads trekt in 2026 binnen maanden gratis navolgers aan. Bij elk gehaat betaald product dat ik vond stond er al een gratis alternatief met een goed cijfer, vaak meerdere, en vaak nog net vernieuwd. Op JetBrains komt de gratis variant soms van de verkoper zelf (gratis "Localization" naast het betaalde "Language Pack") of van JetBrains (gratis Monokai en QML). "Gehaat en duur" is op deze winkels dus geen gat meer, maar een teken dat er al iemand zit. Kansrijker voor de volgende run: tools die buiten de winkels worden verkocht (los abonnement, eigen site), of gehate tools in een winkel waar weinig makers kijken.

### Hoe ik zocht (GEZIEN 17 nov ±14:58 tot 15:08 UTC)
- JetBrains: alle 1.021 betaalde en freemium plugins via de open API (`plugins.jetbrains.com/api/searchPlugins?pricingModels=PAID|FREEMIUM&orderBy=downloads`, max 20 per pagina). Van de 78 met meer dan 40.000 downloads (zonder JetBrains zelf) alle reviews gelezen via `/api/plugins/<id>/comments` en geteld hoeveel reviews sinds 1 jan 2025 1 of 2 sterren gaven. Daarna per kandidaat in de winkel gezocht naar gratis alternatieven.
- Superhive: de 190 best verkochte add-ons (8 pagina's `categories/addons/browse?sort_sales=desc`), per pagina het veld "Blender Version" gelezen. Gezocht naar add-ons met veel verkopen die Blender 5 niet ondersteunen (verlaten door de maker).
- Let op: `cdate` in de JetBrains-API is de datum van de laatste versie, niet van de eerste uitgave.

### Zelf afgeschoten: goedkopere of betere Ansible-plugin voor JetBrains | DOOD op vraag 2
- Gehaat: OrchidE (betaald, 355.962 downloads, 3,08 sterren). 35 van de 61 reviews geven 1 of 2 sterren, de meeste om de prijs: "Far too expensive for what it does" (12 dec 2024), "Probably good but too expensive" (27 jan 2026). GEZIEN 17 nov via de API.
- **2.** Gratis alternatieven: "Ansible" van MS dehghan (197.248 downloads, 4,33), "Ansible Lint" (90.648, 4,28, bijgewerkt jul 2026), "Ansible Vault Editor" (108.748, 4,56). En op 11 nov 2026 een nieuwe versie van "Ansible Pro" (freemium) van meanmail.dev, een verkoper die ook Nginx Configuration Pro heeft (270.990 downloads, 4,41). Er zit dus al een goede gratis speler en net een sterke nieuwe betaalde. GEZIEN 17 nov.

### Zelf afgeschoten: QML-editor voor JetBrains | DOOD op vraag 1
- Gehaat: QmlEditor (betaald, 31.353 downloads, 1,85 sterren, 13 van 15 reviews laag, "this plugin appears to have been abandoned", 1 dec 2022).
- **1.** JetBrains heeft zelf een gratis plugin "QML" (1.043.777 downloads, laatste versie 30 okt 2026). GEZIEN 17 nov.

### Zelf afgeschoten: betere taalpakketten voor JetBrains (Frans, Russisch, Tsjechisch, Italiaans) | DOOD op vraag 2
- Gehaat: de betaalde pakketten van verkoper "Code": Frans 2,52 sterren (33.265 downloads, "Bad quality and missing text", 22 jul 2026), Russisch 3,04 ("Machine translation", 4 jan 2025), Tsjechisch 3,06, Italiaans 3,41. Het Franse pakket van Anton Shuvaev staat op 2,24.
- **1.** JetBrains maakt zelf alleen Chinees, Japans en Koreaans (gratis, elk 1,9 miljoen of meer downloads).
- **2.** Voor bijna elke taal is er al een gratis versie: "Code" zet naast elk betaald pakket een gratis "Language Localization" (Frans 8.515, Spaans 23.081, Duits 6.524 downloads), "Russian Language Pack" van Alex Ivanov is gratis (88.181, 4,32), "German Language Pack" van Patrick Cornelissen gratis (laatste versie 31 okt 2026), "IDE Localization: Italian" van DevCairn Labs gratis (5 okt 2026). Vertalen met een taalmodel kan nu iedereen, dus ook onze kwaliteitsvoordeel is klein. Nederlands bestaat nog niet, maar Nederlanders werken vrijwel allemaal in het Engels (GOK). GEZIEN 17 nov.

### Zelf afgeschoten: Excel-bestanden bewerken in JetBrains | DOOD op vraag 2
- Gehaat: ExcelEditor (freemium, 317.002 downloads, 3,2 sterren, 10 van 16 reviews laag: "I pay for a plugin where I can... edit cells? Not even add rows", 10 jul 2026).
- **2.** Gratis: ExcelReader van dezelfde maker (1.247.534, 4,02), Light Sheet (16.433, 4,41), Omni Viewer (freemium, 65.979, 4,63), nieuw XLSX Lens (12 nov 2026). GEZIEN 17 nov.

### Zelf afgeschoten: certificaten en keystores bekijken in JetBrains | DOOD op vraag 2
- Gehaat: KS-Explorer (betaald, 317.768 downloads, 3,32 sterren; "This is the only plugin I pay for, and it never works properly", 22 sep 2025; werkt niet met RubyMine 2026.2, 23 jul 2026).
- **2.** Minstens 10 alternatieven, de meeste gratis en recent bijgewerkt: Key Explorer (17.820, 4,02), CertView X.509 (10.917), X509 Certificate (11.592, 4,06), SSL-Toolbox (76.877, 3,7), plus Keystore Inspector, CertLens, Keystore Workbench (14 nov 2026). Een reviewer noemt ook het gratis bureaubladprogramma KeyStore Explorer. GEZIEN 17 nov.

### Zelf afgeschoten: Monokai Pro-achtig thema voor JetBrains | DOOD op vraag 2 (en we gaan geen ontwerp van een ander namaken)
- Gehaat: Monokai Pro (freemium, 2.532.556 downloads, 2,97 sterren). Het meest gehate betaalde product van de hele winkel: 81 van de 92 reviews sinds 2025 geven 1 of 2 sterren, 46 keer gaat het om geld ("Seriously? £9 for a colour plugin", 15 nov 2026). GEZIEN 17 nov.
- **2.** Gratis: "Monokai Color Scheme" van JetBrains zelf (1.639.916, 4,53), Monocai (524.183, 4,38), OneDarkMonokai, en veel andere gratis thema's. De Pro-kleuren nadoen is het ontwerp van een ander kopiëren.

### Zelf afgeschoten: Jenkinsfile-plugin voor JetBrains | DOOD op vraag 2 en zwak op 3
- Betaald: Jenkinsfile van Anbora Labs (164.770 downloads, 4,17; "does nothing except for adding some useless colors", 13 feb 2025). Maar maar 6 lage reviews sinds 2025, dus weinig haat.
- **2.** Gratis: Jenkinsfile Syntax Highlighter (42.151), Jenkins Pipeline Linter (148.527, 3,25), PipelineLens (17.674), Jenkinsfile Support (jul 2026). GEZIEN 17 nov.

### Zelf afgeschoten: Pie Menu Editor voor Blender 5 | DOOD op vraag 2
- Verlaten betaald: Pie Menu Editor op Superhive ($16, 2.400+ verkopen, 64 ratings) ondersteunt volgens de pagina alleen Blender tot 4.3. GEZIEN 17 nov.
- **2.** Er is al een gratis community-fork met eigen website ("Pie Menu Editor Fork", GitHub-organisatie pie-menu-editor, website bijgewerkt 11 nov 2026; ook Retroise/pie-menu-editor-blender-5.2, sep 2026), en op extensions.blender.org staan gratis Pie Customizer, PieMenu Everywhere en 3D Viewport Pie Menus (Blender 5.0+). GEZIEN 17 nov via de GitHub-zoek-API en de API van extensions.blender.org.

### Zelf afgeschoten (snel): Drag-n-Drop Import voor Blender | waarschijnlijk DOOD op vraag 1
- Superhive: $15, 2.300+ verkopen, alleen tot Blender 4.0 (GEZIEN 17 nov). Blender kan sinds 4.1 zelf bestanden importeren door ze in het venster te slepen (GOK uit mijn geheugen, release notes niet nagelezen). Niet verder uitgezocht.

### Zelf afgeschoten: auto-rig voor Blender 5 (opvolger van Car Rig Pro) | DOOD op vraag 2
- Verlaten betaald: Car Rig Pro op Superhive ($49, 2.000+ verkopen) alleen tot Blender 3.2. GEZIEN 17 nov.
- **2.** De klanten zijn al opgevangen: Launch Control op Superhive ($59, 3.400+ verkopen, 42 ratings, ondersteunt Blender 3.6 tot 5.2) en gratis Rigacar op GitHub (digicreatures/rigacar, 499 sterren, laatste push apr 2024; of die op Blender 5 werkt: ONBEKEND). GEZIEN 17 nov via Superhive en de GitHub-zoek-API.

### Open voor een volgende run
- Superhive, verlaten maar nog niet nagekeken: Mask Tools ($35, 2.500+ verkopen, tot 4.0), DynRemesh 2 ($35, 3.100+, tot 2.91), Tesselator ($8,50, 3.700+, tot 3.2), Turbo Tools ($49,99, 2.400+, tot 4.5). Op extensions.blender.org vond ik voor "tessel" en "temporal" geen gratis extensie (GEZIEN 17 nov, lijst van 1.680 extensies), dus Tesselator en Turbo Tools eerst. Eerst vraag 1 (doet Blender 5 het zelf, bijvoorbeeld de nieuwe remesh- en sculptfuncties) en vraag 2 op extensions.blender.org.
- Gehate abonnementen buiten de winkels (eigen site, los abonnement). Daar is de navolging mogelijk trager dan in een winkel met zoekbalk.
