# Groep A: Microsoft en GitHub (onderzoek 17 nov 2026)

Alles hieronder is met curl gelezen, tenzij er GOK of ONBEKEND staat. Tijdstip van lezen: 17 nov 2026, rond 17:30 tot 18:00 UTC (de Ignite-keynote begon om 18:00 UTC, dus nieuws van de keynote zelf zit er nog niet in).

### 1. Microsoft Copilot Plugin Catalog
- Bestaat: JA. GEZIEN in "Plugins at Microsoft Ignite 2026", Tech Community, 12 nov 2026: https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/plugins-at-microsoft-ignite-2026/4569951 ("The new Plugin Catalog will launch on Nov 17th at Ignite at this link: aka.ms/plugins"). aka.ms/plugins wijst nu naar https://www.microsoft.com/en-us/copilot/features/plugins/explore (pagina "Copilot Plugin Catalog", live). Let op: aka.ms/CopilotPluginCatalog uit de tip wijst naar de prijspagina van Copilot Business, niet naar de catalogus. De plugin registry (de beheerkant voor IT) bestaat sinds september 2026.
- Wat het echt is: een openbare etalage op microsoft.com voor plugins van Microsoft 365 Copilot (en Copilot Cowork). Een plugin is een pakket van skills (herbruikbare instructies), tools/connectors/MCP-servers en agents; de knop "Get in Copilot" stuurt naar m365.cloud.microsoft, dus het is voor werkaccounts, niet voor gewone consumenten.
- Harde cijfers (GEZIEN, uit de openbare inventaris die de catalogus laadt: res.cdn.office.net/taos-platsvcs-controlplane/public-metadata/public-catalog.json, stand 29 okt 2026): 653 plugins, 501 van derden, 152 van Microsoft zelf, 327 uitgevers. Bijna alles toegevoegd in sept/okt 2026. Bron van alles: "Omex", dat is de Office/Microsoft 365-winkel via Partner Center. 82 plugins bevatten skills, waarvan 72 van derden. De catalogus heeft zoeken, categorieën, uitgelichte plugins ("Featured"/editor's pick) en een link "publish your own plugins" (aka.ms/publishplugin naar https://learn.microsoft.com/en-us/plugins/).
- Hoe kom je erin: openbaar publiceren gaat alleen via Microsoft Partner Center, programma "Microsoft 365 and Copilot" (GEZIEN: https://learn.microsoft.com/en-us/plugins/publish en de WIQD-gids https://microsoft.github.io/wiqd/getting-started/publish-to-partner-center/). Eisen daar: een Microsoft Entra-werkaccount, "Authority to sign legal agreements on your company's behalf", "Your company's legal business name, address, and primary contact. Microsoft verifies these", verificatie "can take several business days". Daarna nog certificering per plugin. Losse skill- of connector-plugins mogen ook (via het portaal).
- Geld vragen: de catalogus zelf heeft geen kassa. In de WIQD-gids moet je bij indienen aangeven of de plugin "a separate service purchase or has in-app purchases" heeft. Dus: eigen abonnement buiten de winkel is toegestaan, of een gekoppelde SaaS-aanbieding in Microsoft Marketplace (zie tip 2). In de beschrijvingen van derden staat "subscription" 158 keer: vrijwel alle derden zijn bestaande SaaS-bedrijven (Box, Canva, Miro, Atlassian, Harvey, monday.com) die hun eigen abonnement verkopen.
- Wet 1 (vroeg): JA voor de catalogus (vandaag live, ±650 items), maar NEE voor binnen 7 dagen: bedrijfsverificatie plus certificering kost GOK 1 tot 3 weken, en zonder KvK-bedrijf kom je er niet door.
- Wet 2 (brede basistaak): DEELS. Brede taken (documenten, mail, vergaderingen) doet Microsoft zelf in Copilot. Wat over is, is vooral koppeling met andermans SaaS of vakkennis (juridisch, financieel): nis.
- Wet 3 (kassa): DEELS. Zakelijke betaalcultuur is er, maar alleen via eigen abonnement of Marketplace-SaaS, en de koper is een bedrijf waarvan de beheerder de plugin moet toestaan.
- Wet 4 (platform doet het niet zelf): NEE. Microsoft maakt zelf 152 van de 653 plugins, waaronder brede skill-pakketten "Finance for Cowork", "Legal for Cowork", "Sales for Cowork", "Service for Cowork", "Education for Cowork". Precies het soort brede basistool dat wij zouden willen maken.
- Vraag 5 (etalage): JA, er is zoeken, categorieën en uitgelicht. Maar de klant is IT: "Each customer's administrator still installs the plugin, allows its publisher category, and sets availability" (learn.microsoft.com/en-us/plugins/publish). Een gebruiker kan dus niet zomaar zelf installeren zoals bij Blender Extensions.
- Mogelijk product: alleen als Thijs een eenmanszaak inschrijft bij de KvK. Dan GOK: een gratis skill-pakket zonder server (alleen instructies), om bereik te testen. Geld komt dan pas later via een eigen abonnement. Niemand betaalt voor losse skills zolang Microsoft zelf gratis skill-pakketten levert.
- Cijfer: 5. Echte nieuwe etalage die vandaag opengaat, maar bedrijfsverificatie, IT-poortwachters en Microsoft die zelf de brede skill-pakketten maakt, maken het voor ons zwaar.

### 2. Microsoft Marketplace (zakelijke winkel), incentives, private offers, Agent 365
- Bestaat: JA, maar de tip klopt maar half.
  - "220 nieuwe AI apps & agents": GEZIEN als "New in Microsoft Marketplace: Offers published September 29-30, 2026", Marketplace blog, 10 nov 2026 ("Learn about 220 new offers that went live..."), lijst op https://techcommunity.microsoft.com/category/marketplace/blog/marketplace-blog. Dat zijn 220 aanbiedingen in twee dagen: het is een overvolle, gevestigde winkel, geen nieuwe.
  - FY27 "AI Build & Publish" tot $80.000: DEELS GEZIEN, alleen via een derde partij (WeTransact, bijgewerkt 17 nov 2026): https://docs.wetransact.io/guide-to-submitting-the-claim-for-ai-build-and-publish-marketplace-incentives-fy27. De $80.000 geldt alleen bij meer dan $750K geplande Marketplace-omzet in jaar 1; toegangsdrempel "More than $100K in Marketplace Billed Sales" of een Azure-verbruiksafspraak van meer dan $1M; je moet uitgenodigd zijn; looptijd 1 okt 2026 tot 30 jun 2027. De officiële pagina op partner.microsoft.com kon ik niet lezen (TLS-fout via de proxy). Datum 6 nov uit de tip: NIET GEVONDEN.
  - Vereenvoudigde private offers: GEZIEN, Partner Center-aankondigingen november 2026, datum 5 nov 2026: https://learn.microsoft.com/en-us/partner-center/announcements/2026-november ("eligible private offers can be accepted and purchased in a single step").
  - Agent 365 in Partner Center op 13 nov: NIET GEVONDEN op die datum. Wel GEZIEN (12 nov 2026, zelfde pagina): een Agent 365-module voor beveiligingspartners (SSP's en systeemintegratoren). Niets voor kleine makers.
- Wat het echt is: de zakelijke winkel van Microsoft (vroeger Azure Marketplace en AppSource) voor SaaS, Azure-apps en agents, waar bedrijven via hun Azure-rekening kopen. Microsoft rekent 3% bij transactable SaaS (GOK uit eerdere kennis, niet opnieuw gecontroleerd).
- Wat een eenmanszaak in NL moet doen: Partner Center-account met Entra-werkaccount, inschrijven in het AI Cloud Partner Program en het Marketplace-programma, juridisch profiel met bedrijfsnaam en adres dat Microsoft controleert (WeTransact noemt 24 uur voor het juridisch profiel en 48 uur voor uitbetaal- en belastingprofiel), daarna per aanbieding certificering. Voor een SaaS-aanbieding moet je zelf een landingspagina en de SaaS Fulfillment API bouwen. Zonder geregistreerd bedrijf (KvK-uittreksel) lukt de verificatie niet (GOK, maar de docs vragen overal "your company's legal business name").
- Wet 1: NEE. De winkel bestaat al jaren en krijgt honderden aanbiedingen per week.
- Wet 2: NEE. Zakelijke SaaS per sector, geen basistaak voor "iedere gebruiker".
- Wet 3: JA. Er is een echte kassa (transactable SaaS) en zakelijke betaalcultuur.
- Wet 4: onbekend per product, maar Microsoft concurreert hier met alles wat het zelf in Copilot stopt.
- Vraag 5: NEE in de praktijk. Er is zoeken en een categorieënlijst, maar kopers komen via verkoop, co-sell en private offers; een nieuwe kleine aanbieding verdwijnt tussen duizenden.
- Mogelijk product: geen.
- Cijfer: 2. Gevestigde enterprise-winkel, incentives pas vanaf $100K omzet, zware verificatie en geen etalage voor een nieuwkomer.

### 3. Microsoft Ignite 2026 Book of News (17 nov)
- Bestaat: ONBEKEND op het moment van lezen. https://news.microsoft.com/ignite-2026-book-of-news/ gaf een 404 om 17:47 UTC, 13 minuten voor de keynote. Varianten (ignite-2026, ignite2026-book-of-news, /source/...) ook 404. Het Book of News van Build 2026 staat achter een inlog. Lukte dus niet: opnieuw proberen na 18:00 UTC.
- "Windows Agent Store": NIET GEVONDEN als officieel product. Het officiële Build 2026-bericht van Windows (https://blogs.windows.com/windowsdeveloper/?p=57809, "Build 2026: Furthering Windows as the trusted platform for development", juni 2026) noemt alleen verbeteringen aan de gewone Microsoft Store: "free and faster company onboarding with Entra ID support, accelerated app certification times, and new near real-time analytics and subscription insights". Het woord "Agent Store" en een omzetdeling staan er niet in. Een blog van fourweekmba ("App Store for AI Agents, 85% Revenue Share") kon ik niet lezen (403) en is geen primaire bron. Wat wel bestaat is de "Agent Store" binnen Microsoft 365 Copilot (de WIQD-gids zegt: "Find it in the Agent Store once it's certified and Live"); dat is dezelfde route als tip 1.
- Wat wel uit voorberichten bekend is (GEZIEN, borncity.com 12 nov 2026): Copilot-harness in Foundry Agent Service als openbare preview met meer dan 20 modellen, betaald vanaf 1 dec 2026; Microsoft Execution Containers voor agents op Windows 11. Geen nieuwe winkel of kassa voor kleine makers.
- Wet 1 tot 4 en vraag 5: onbekend, er is (nog) geen winkel om te toetsen.
- Cijfer: 1 (voorlopig). Niets gevonden; herkansing na de keynote.

### 4. GitHub Copilot Skills / Agentic Hooks / Copilot Automations en GitHub Marketplace
- Bestaat: DEELS.
  - Copilot automations: GEZIEN als aangekondigd op GitHub Universe (28 okt 2026), volgens de samenvatting op https://capitalandcompute.net/md/github-universe-2026-announcements.md: werkstromen in de cloud per repo (op schema of bij een gebeurtenis), betaald in AI-credits. Het officiële keynote-bericht (https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/, 28 okt 2026) noemt Copilot app, Copilot Fusion, Copilot projects en sessie-continuïteit; de woorden marketplace, plugin, extension en skill-winkel komen er niet in voor.
  - Copilot Skills: Agent Skills bestaan al sinds dec 2025 (github.blog changelog 2025-12-18) en voor code review sinds juli 2026. Het zijn gratis bestanden in een repo; geen winkel met kassa.
  - "Agentic Hooks" als nieuw Universe-product: NIET GEVONDEN.
  - GitHub Marketplace betaalde route: GEZIEN (https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app): betaalde plannen alleen voor GitHub Apps van een organisatie die "verified publisher" is, met "a minimum of 100 installations", maandelijks en jaarlijks abonnement verplicht. De oude Copilot Extensions (als GitHub App) zijn op 10 nov 2025 stopgezet ten gunste van MCP (https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/).
- Wat het echt is: GitHub bouwt de agent-functies zelf (automations, skills, hooks) en betaalt ze via AI-credits; extern uitbreiden gaat via MCP en skill-bestanden, die gratis rondgaan.
- Wet 1: NEE. Skills bestaan bijna een jaar, de Marketplace al jaren.
- Wet 2: DEELS. Ontwikkelaars hebben brede taken, maar die bouwt GitHub zelf.
- Wet 3: NEE voor skills (geen kassa). Voor GitHub Apps pas na 100 installaties en publisher-verificatie van een organisatie.
- Wet 4: NEE. GitHub doet automations, code review, security-scans zelf.
- Vraag 5: DEELS. GitHub Marketplace heeft zoeken en categorieën, maar skills staan er niet in.
- Mogelijk product: geen.
- Cijfer: 2. Geen betaalde route voor skills, en GitHub bouwt alles wat breed is zelf.

### 5. Copilot Cowork Skills / Work IQ Dev Tools
- Bestaat: JA. Work IQ Dev Tools (wiqd) v1.0.0 met eigen docs: https://microsoft.github.io/wiqd/ (gids "Publish to Partner Center"). Ignite-sessies GEZIEN in het Tech Community-bericht van 12 nov 2026: LTG1220 "WIQD in 15 minutes: Build, validate, and publish plugins", LAB652 "Hands-on with Copilot Cowork", THR851 "Skills in Microsoft Copilot". Cowork accepteert een plugin-ZIP die je deelt met "Only you" of "Specific users"; organisatiebreed vraagt beheerdersgoedkeuring (https://learn.microsoft.com/en-us/plugins/publish).
- Wat het echt is: het gereedschap (CLI en VS Code-extensie) om Copilot- en Cowork-plugins te bouwen, te testen en via `wiqd publish pc` naar Partner Center te sturen. Het is geen aparte winkel: openbaar komt het in dezelfde catalogus en Agent Store als tip 1. Cowork zelf is betaald per verbruik (Copilot Credits) door de klant.
- Wet 1: JA voor het gereedschap (net 1.0), maar de publicatie loopt via dezelfde bedrijfsverificatie als tip 1.
- Wet 2: DEELS, zie tip 1.
- Wet 3: NEE binnen de winkel; alleen eigen abonnement of Marketplace-SaaS.
- Wet 4: NEE, Microsoft levert zelf de "for Cowork"-skillpakketten per beroep.
- Vraag 5: zelfde etalage als tip 1.
- Mogelijk product: geen los product; het is het bouwgereedschap voor tip 1.
- Cijfer: 4. Handig gereedschap en een echte nieuwe route, maar geen eigen kassa en geen eigen etalage.

## Top 2
Niets haalt een 7.

1. Copilot Plugin Catalog (cijfer 5): de enige echte nieuwe etalage (live sinds vandaag, ±650 plugins, zoeken en uitgelicht). Valt af op wet 1 (bedrijfsverificatie via Partner Center, KvK nodig, binnen 7 dagen niet haalbaar), wet 3 (geen kassa in de winkel) en wet 4 (Microsoft maakt zelf de brede skill-pakketten). Alleen interessant als Thijs toch een eenmanszaak inschrijft en we gratis bereik willen testen met een skill-pakket zonder server.
2. Copilot Cowork / Work IQ Dev Tools (cijfer 4): het bouwgereedschap voor dezelfde route; nuttig als we toch voor de catalogus gaan.

Advies: Microsoft en GitHub nu niet kiezen. Wel na 18:00 UTC het Ignite 2026 Book of News opnieuw proberen op news.microsoft.com/ignite-2026-book-of-news/ voor een eventuele nieuwe winkel of kassa.
