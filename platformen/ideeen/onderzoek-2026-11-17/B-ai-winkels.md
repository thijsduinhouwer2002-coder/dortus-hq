# Groep B: AI-agentwinkels en AI-platformen (onderzoek 17 nov 2026)

Alle pagina's gelezen met curl. Wat ik niet zelf zag staat als GOK of ONBEKEND.

### 1. Cowboy General Store
- Bestaat: JA. Eigen site https://cowboy.inc ("The App Store for AI", knop "Request an invite", gezien 17 nov 2026). Lancering 4 nov 2026 volgens Upstarts Media (https://upstartsmedia.com/p/cowboy-app-store-ai-agents, 4 nov 2026) en QUASA (https://quasa.io/stories/cowboy-launches-its-ai-agent-store-with-5m-and-100-agents, 14 nov 2026). $5M seed, 100 agents, 10.000 datafeeds, team van 10 in New York.
- Wat het echt is: een winkel waar je een draaiende agent ("actor" met eigen portemonnee, planning en bestanden) huurt op je eigen sleutels; de koper ziet de code niet, de maker ziet de sleutels niet. Gericht op handelaren, vooral crypto (Hyperliquid, Polymarket, prijswachters), met een eigen blockchain (Cowboy Chain) in testfase.
- Wet 1 (vroeg): deels. Twee weken oud, maar alleen op uitnodiging; of en wanneer Dortus erin komt is ONBEKEND, dus binnen 7 dagen staan is niet zeker.
- Wet 2 (brede basistaak): nee. De klanten zijn crypto-handelaren; de brede taken (spamfilter, contentmoderatie, PDF) doet Cowboy Labs zelf al.
- Wet 3 (kassa): ja op papier. Maandhuur, per gebruik, eenmalig; uitbetaling in dollars via Stripe. Commissie en rekenkosten worden ingehouden, percentage niet openbaar (QUASA).
- Wet 4 (platform doet het niet zelf): nee. Cowboy Labs vult de etalage met eigen agents (gezien op cowboy.inc).
- Vraag 5 (voert de winkel kopers aan): ONBEKEND en twijfelachtig. Upstarts en QUASA zeggen allebei dat betalende vraag nog niet bewezen is; geen cijfers over kopers.
- Mogelijk product voor Dortus: geen dat de wetten haalt. Hooguit later een algemene "prijs/voorwaarde-wachter met melding op Telegram", maar die staat er al als voorbeeld van Cowboy zelf.
- Cijfer: 3. Echt en met kassa, maar op uitnodiging, crypto-nis, geen bewezen kopers en het platform vult zelf de schappen.

### 2. Claude connectors, MCP Apps en Claude Marketplace
- Bestaat: JA.
  - Apps naast het gesprek openen: Claude-blog "Your apps can now open in Claude, and Claude can work in them", 10 nov 2026 (https://claude.com/blog/interactive-connectors-full-tool). Begint met "a small group of tools from our directory" (Asana, Canva, Carta, Dropbox, monday.com, Smartsheet, Vercel, Webflow).
  - Indienen: iedereen met een betaald plan (Pro, Max, Ultra, Team, Enterprise), geen partnerprogramma nodig (https://claude.com/docs/directory/publish.md en https://claude.com/docs/connectors/building/submission.md, gezien 17 nov 2026).
  - Claude Marketplace: blog 23 sep 2026 (https://claude.com/blog/claude-marketplace). Meer dan 2.000 connectors en plugins; "agents en producten kopen" kan alleen met vastgelegd Anthropic-tegoed van bedrijven, op aanvraag.
- Wat het echt is: een gekeurde directory van MCP-servers (connectors), optioneel met eigen scherm (MCP App). De directory heeft zoeken, bladeren, "Suggested Connectors" in het gesprek, en rangschikking op gebruik (https://claude.com/docs/connectors/directory.md).
- Wet 1 (vroeg): nee voor de directory zelf (open sinds 2025/begin 2026, al 2.000+ items). Het nieuwe van 10 nov (zijpaneel, volledig scherm, openen zonder prompt) is alleen voor een kleine groep partners; "entry points" werken alleen onder een Verified listing (https://claude.com/docs/connectors/building/directory-vs-custom.md). Een gewone maker krijgt dat dus niet binnen 7 dagen.
- Wet 2 (breed): mogelijk ja, maar de grote basistaken zijn bezet door merken (Google, Microsoft, Notion, Canva, Atlassian) en door Claude zelf (artifacts, bestanden, zoeken).
- Wet 3 (kassa): nee binnen Claude. Er is geen Anthropic-kassa voor makers; ik vond niets over afrekenen in de docs. De directory-regels verbieden advertenties en (meestal) crypto, maar NIET dat je eigen betaalde account achter OAuth zet (https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy). GOK: een eigen abonnement op je eigen site, ingelogd via OAuth, mag (Canva en Asana doen hetzelfde). De betaalcultuur van Claude-gebruikers is goed (betaalde plannen), maar voor losse connectors ONBEKEND.
- Wet 4 (platform doet het niet zelf): wisselend. Claude bouwt veel zelf (artifacts, Cowork, eigen documenten, Chrome). Elke brede tool loopt dat risico.
- Vraag 5 (etalage): JA, en dat is het sterke punt. Zoeken, lijsten, Suggested Connectors in het gesprek en rangschikking op gebruik. Sinds april 2026 haalt Claude ook zelf passende apps naar voren (https://elliotgarreffa.beehiiv.com/p/claude-organic-app-discovery-just-got-turned-on, 27 apr 2026).
- Mogelijk product voor Dortus: een remote MCP-server (met MCP App-scherm) voor een brede taak die Claude zelf niet doet en waar geen groot merk zit, gratis met een betaald eigen account voor zwaar gebruik. Betaler: Claude-gebruikers via Stripe of Polar op onze eigen site. Let op: we moeten zelf hosten (servers, OAuth, privacybeleid, support-adres), en de keuring duurt ONBEKEND lang.
- Cijfer: 5. Beste etalage van deze groep, maar geen kassa in de winkel, niet meer vroeg, en het nieuwe zijpaneel is alleen voor partners.

### 3. xAI Grok Build Plugin Marketplace en Grok Bot 1.0
- Bestaat: JA, maar niet van 2 nov 2026.
  - Plugin Marketplace: xAI-nieuws 11 jun 2026 (https://x.ai/news/grok-plugin-marketplace). Open catalogus; indienen via pull request op github.com/xai-org/plugin-marketplace. Nu 36 plugins, bijna allemaal van bedrijven (Vercel, Stripe, Supabase, Figma, Unity, Expo...), gezien in marketplace.json op 17 nov 2026.
  - Grok Bot: early beta rond 11 tot 13 aug 2026 (iphoneincanada.ca, propakistani.pk). Sjablonenwinkel voor Bots sinds 4 sep 2026 (basenor.com). "Grok Bot 1.0" bestaat volgens fourweekmba.com (stoel $30), maar de primaire x.ai-pagina kon ik niet lezen (Cloudflare blokkeert). Datum 2 nov: NIET GEVONDEN als primaire bron.
- Wat het echt is: een gratis lijst van plugins (skills, commando's, MCP-servers) voor de Grok Build terminal-coder, zelfde opbouw als Claude Code-plugins. Bot-sjablonen zijn gratis kopieën in je eigen account.
- Wet 1: nee. Vijf maanden oud.
- Wet 2: deels. Plugins zijn vooral koppelingen naar merkdiensten.
- Wet 3: nee. Geen kassa; alles is gratis open source of hoort bij een betaalde dienst van het merk.
- Wet 4: ONBEKEND.
- Vraag 5: deels. /marketplace in de terminal toont de catalogus, maar het is een kleine lijst met vooral merken; keuring via PR door xAI.
- Mogelijk product: geen.
- Cijfer: 2. Niet vroeg, geen kassa, klein publiek.

### 4. ChatGPT: apps (Prada), ChatGPT Sites, digitale verkoop
- Bestaat: JA, maar de data kloppen niet.
  - Prada-app in ChatGPT: Retail Gazette oktober 2026 (https://www.retailgazette.co.uk/blog/2026/10/prada-chatgpt-tool/), pilot in VK, VS en Italië, gebouwd met Accenture Song. Niet 17 nov.
  - ChatGPT Sites: publieke bèta sinds 9 jul 2026 (flaviocopes.com "A deep dive into ChatGPT Sites", 17 nov 2026, https://flaviocopes.com/chatgpt-sites/). Het artikel is van 17 nov, het product niet.
  - Digitale verkoop: NIET veranderd. https://developers.openai.com/plugins/build/monetization.md (gezien 17 nov 2026): "current approval is limited to plugins for physical goods purchases". De keuringsregels zeggen letterlijk: "Selling digital products or services, including subscriptions, digital content, tokens, or credits, is not allowed, whether offered directly or indirectly (for example, through freemium upsells)". Ook mag je geen abonnementen tonen of upgrades promoten.
- Wat het echt is: apps (nu "plugins") in ChatGPT zijn een etalage voor merken en fysieke winkels. Sites is hosting voor sites die ChatGPT zelf bouwt voor de gebruiker; er is geen winkel van Sites voor derden, alleen "Remix" binnen een werkruimte.
- Wet 1: nee. Apps sinds eind 2025, Sites sinds juli 2026.
- Wet 2: n.v.t.
- Wet 3: nee voor digitale producten in ChatGPT-apps (hard verboden, ook freemium-upsell). Een Site mag wel verkopen via een externe betaalverwerker, maar dat is gewoon een website zonder etalage.
- Wet 4: Sites is precies het platform dat het zelf doet: ChatGPT bouwt en host de kleine web-app voor de gebruiker. Dat maakt kleine webtools van makers minder waard.
- Vraag 5: apps-directory ja, Sites nee.
- Mogelijk product: geen. Wie een digitale tool in de ChatGPT-directory zet, mag er niets voor vragen.
- Cijfer: 1. Hard nee op wet 3 voor alles wat Dortus maakt.

### 5. Google Stitch Skills, Agent Skills open standaard, skills.sh
- Bestaat: JA. https://github.com/google-labs-code/stitch-skills (README gezien 17 nov 2026): skills en plugins voor Google Stitch volgens de Agent Skills-standaard (agentskills.io), te installeren in Codex, Claude Code, Cursor en andere. skills.sh is de open directory van Vercel ("npx skills add"), met een ranglijst op installaties: 1.471.015 skills totaal, gezien 17 nov 2026.
- Wat het echt is: Stitch Skills is Google's eigen pakket om met Stitch te ontwerpen; geen winkel. skills.sh is een gratis gids en installer met ranglijst.
- Wet 1: nee. De standaard bestaat sinds eind 2025; skills.sh heeft al bijna 1,5 miljoen skills.
- Wet 2: n.v.t., de brede taken zijn genomen (find-skills 4,4M installs, frontend-design van Anthropic 1,1M).
- Wet 3: nee. Geen kassa op skills.sh (geen prijs of betaalknop op de pagina). Losse betaalde skill-winkels bestaan (SkillHQ, Capafy, 402md), maar dat is het Gumroad-probleem: geen kopers.
- Wet 4: Google en Anthropic leveren zelf de belangrijkste skills.
- Vraag 5: skills.sh ja (ranglijst, trending), maar zonder geld.
- Mogelijk product: geen voor omzet. Hooguit gratis bereik, en dan alleen met iets echt nieuws.
- Cijfer: 2. Overvol en zonder kassa.

### 6a. Zoom AI Launchpad en Zoom Decisions APIs
- Bestaat: JA. Decisions APIs: Zoom-blog 19 okt 2026 (https://www.zoom.com/en/ai-research/introducing-zoom-decisions-apis-accurate-speech-reliable-action/). AI Launchpad: UC Today 10 nov 2026 (https://uctoday.com/in-brief/zoom-launches-ai-launchpad-for-eligible-startups-uMGEH8FUuS36LdqVbROvxmA).
- Wat het echt is: Launchpad is een programma met tot $150.000 API-tegoed voor "eligible AI-native startups", geen winkel. Decisions APIs zijn betaalde zakelijke API's (spraak naar beslissing) voor bedrijven die voice-agents bouwen.
- Wet 1: deels (een maand oud), maar het is geen winkel. Wet 2: nee, zakelijke spraakagents. Wet 3: geen nieuwe kassa voor makers (de Zoom App Marketplace bestaat al jaren). Wet 4: Zoom bouwt zelf ZoomMate en AI Companion. Vraag 5: Launchpad belooft "introducties bij enterprise-klanten", dat is verkoop door gesprekken, geen etalage.
- Mogelijk product: geen. Startupprogramma's vragen meestal een bedrijf (GOK: eis van een rechtspersoon, niet gecontroleerd).
- Cijfer: 1.

### 6b. ElevenLabs Marketplace
- Bestaat: JA. https://elevenlabs.io/marketplace (gezien 17 nov 2026): "Discover applications built with ElevenLabs, tailored to your industry", met knop "Register interest". Datum 11 nov 2026 kon ik niet bevestigen (de nieuwspagina van letsdatascience was geblokkeerd).
- Wat het echt is: een lijst van zakelijke partnerproducten per branche (Agentforce Voice, NiCE CXone, zorg, financiën). Geen kassa voor makers; je meldt interesse aan.
- Wet 1: ja qua leeftijd. Wet 2: nee, branche-oplossingen. Wet 3: nee, geen kassa. Wet 4: n.v.t. Vraag 5: ja voor bedrijven, maar het is een partnergids, geen open winkel.
- Mogelijk product: geen.
- Cijfer: 1.

### 6c. Google Cloud Agent Marketplace
- Bestaat: JA. Google Cloud docs "AI agents through Google Cloud Marketplace" (https://docs.cloud.google.com/marketplace/docs/partners/ai-agents) en IT Brief 8 jul 2026 (https://itbrief.co.uk/story/google-opens-marketplace-path-for-ai-agents-in-gemini).
- Wat het echt is: verkoop van "Agent-as-a-Service" aan bedrijven via Google Cloud Marketplace, met A2A Agent Card, eigen hosting, facturering via Google en registratie in Gemini Enterprise.
- Wet 1: nee (juli 2026, en inschrijven als Marketplace-partner met procurement-API's kost weken). Wet 2: nee, zakelijk. Wet 3: ja (Google factureert), maar alleen aan bedrijven met Google Cloud-account. Wet 4: Google bouwt zelf veel agents in Gemini Enterprise. Vraag 5: deels, zakelijke inkopers zoeken er wel.
- Mogelijk product: geen voor een eenmanszaak zonder bedrijfsstructuur. GOK: partnerinschrijving vraagt een rechtspersoon en belastinggegevens.
- Cijfer: 1.

## Top 2

Niets haalt een 7.

1. Claude connectors directory (5). Enige plek in deze groep met een echte etalage voor een kleine maker: open indienen met een betaald plan, zoeken, Suggested Connectors in het gesprek, rangschikking op gebruik. Zwak: geen kassa in Claude (eigen abonnement achter OAuth is een GOK dat het mag), niet meer vroeg (2.000+ items), en het nieuwe zijpaneel van 10 nov is alleen voor partners. Alleen interessant als we een brede taak vinden die Claude zelf niet doet en waar geen groot merk zit.
2. Cowboy General Store (3). Echt nieuw (4 nov) en met kassa (Stripe-uitbetaling, huur of per gebruik), maar alleen op uitnodiging, gericht op crypto-handelaren, zonder bewezen kopers, en Cowboy vult de schappen zelf. Hooguit een uitnodiging aanvragen en kijken, geen werk in steken.

Belangrijke correcties op de tips: Grok Plugin Marketplace is van 11 jun 2026 (niet 2 nov), ChatGPT Sites van 9 jul 2026 (niet 17 nov), de Prada-app van oktober 2026. OpenAI verbiedt nog steeds verkoop van digitale producten en abonnementen in ChatGPT-apps.
