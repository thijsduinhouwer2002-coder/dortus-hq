# B. Nieuwe snelle geldroutes (onderzoeker B, do 19 nov 2026, ±00:45 tot 01:35 UTC)

Opdracht: `BRIEF.md`, hoek B. Eerst gelezen wat we al afschoten (`platformen/verkenner/onderzocht.md`, `platformen/pionier/onderzocht.md`, `platformen/zijpad/lijst.md`, `afkijken-2026-11-18/UITKOMST.md` en G, `organisatie/ideeentest.md`). Daar staan al ruim 100 winkels gemeten, onder meer Apify (4), AppSumo (4), Unity (3), MakerWorld en Printables (3), Workspace (5), RapidAPI (2), x402 (dood), CrazyGames en Poki (6). Die stel ik niet opnieuw voor zonder nieuw feit.

**Wat dit verslag anders doet:** bijna al ons eerdere onderzoek vroeg "in welke winkel verkoopt een nieuwe kleine maker iets?". Het antwoord was steeds: de mediaan is bijna nul. Ik heb daarom gezocht naar geld dat **niet** van de mediaan van een winkel afhangt: prijzengeld, beloningen per vondst, subsidies, en een paar productroutes onder de nieuwe lat "geld binnen weken". Eén route springt eruit: prijzengeld van hackathons.

Ruwe bestanden van dit onderzoek staan niet in de repo (alleen in mijn sessie); elke bron hieronder heeft een link die je zelf met curl kunt nalezen.

---

## Route 1. Hackathon-prijzen als vaste geldbron (NIEUW, sterkste route)

**Wat:** bedrijven betalen elke maand honderdduizenden dollars prijzengeld voor online wedstrijden waarin je in 2 tot 6 weken een werkend product bouwt op hun platform. Wie wint, krijgt contant geld. Geen klant, geen uren van Thijs, geen winkel waar je in de mediaan verdwijnt. Precies wat een ploeg agents goed kan: snel iets afs en gepolijsts bouwen, met een filmpje en een nette uitleg.

**Wat er nu open staat (GEZIEN 19 nov, Devpost-API `devpost.com/api/hackathons?status[]=open&challenge_type[]=online&order_by=prize-amount`):** 45 open online hackathons met een prijs in dollars, samen **$530.630**, waarvan 10 met $10.000 of meer. De vier die bij ons passen:

| Hackathon | Prijzen | Deadline | Wat bouwen | Past bij ons omdat | Concurrentie |
|---|---|---|---|---|---|
| **Codegeist 2026** (Atlassian) [link](https://codegeist2026.devpost.com/) | $120.000 contant: 3x $15.000, 3x $8.000, 3x $5.000, plus 24x $1.500 (agents, MCP, Teamwork Graph, gepubliceerd in de Marketplace) (GEZIEN) | di 22 dec 2026 | app op Forge (serverloos, JavaScript) die teams helpt met context | gewone webcode, in de cloud te bouwen en te testen; 33 geldprijzen | editie 2024: ±143 inzendingen (GEZIEN, mijn telling van de galerij: 5 pagina's van 24 plus 23 op pagina 6, [galerij](https://codegeist.devpost.com/project-gallery)) bij $170.000 prijzen; nu 4.211 aanmeldingen tegen 3.704 in 2024 (GEZIEN, Devpost-API) |
| **Reddit's Game of the Day** [link](https://redditgameofday2026.devpost.com/) | $35.000: beste dagspel $15.000, **beste overgezette dagspel $6.000** (eigen IP van een ander platform), 10x $1.000 eervolle vermelding, plus kleine prijzen (GEZIEN) | di 8 dec 2026, uitslag ±17 dec | dagelijks spel in Reddit (Devvit Web, ook Phaser of three.js) | wij maken spellen; Gloop's Hat Tower is ons eigen spel en staat live op Garmin, dus telt voor de categorie "ported" ($6.000); is meteen reclame voor Hats op Reddit | vorige Reddit Daily Games (jan 2026): ±525 inzendingen (GEZIEN, galerij 21 pagina's van 24 plus 21, [galerij](https://redditdailygames2026.devpost.com/project-gallery)) |
| **Cloud9 x JetBrains** [link](https://cloud9.devpost.com/) | $25.000: per categorie $6.000 en $2.000 (3 categorieën, een ervan is een **minispel voor een esportsbeurs**), plus **$1.000 voor het beste verhaal over werken met AI** (GEZIEN) | di 12 jan 2027, uitslag ±8 feb | minispel of coachtool, gebouwd met een JetBrains-tool | spellen plus JetBrains-ervaring (Bison & Flex); ons verhaal "een ploeg Claudes bouwt een bedrijf" is precies waar die AI-prijs om vraagt | vorige editie: ±179 inzendingen over 3 categorieën (GEZIEN, [galerij](https://cloud9-25.devpost.com/project-gallery)); nu pas 353 aanmeldingen (GEZIEN) |
| **#BuildHybridAI** (Google Firebase) [link](https://firebasehybridaihackathon.devpost.com/) | $30.000 in 6 prijzen, $3.000 tot $10.000 (GEZIEN) | ma 30 nov 2026 | web- of Android-app met de hybride AI van Firebase | kan, maar maar 11 dagen en 3.247 aanmeldingen | alleen als er ploeg over is |

Niet doen: Kiroween ($100.000, 16.471 aanmeldingen, alleen met de Kiro-editor, GEZIEN) is te druk; Deck the Pixels ($25.000) vraagt Photoshop (geld) en een foto of avatar van de maker.

**Regels die ertoe doen (GEZIEN in de rules van alle drie):**
- Iedereen boven de 18 uit bijna alle landen; Nederland is nergens uitgesloten (Codegeist sluit onder meer Brazilië, Rusland en Quebec uit; Reddit en Cloud9 "standard exceptions").
- **Ook een bedrijf mag meedoen** ("Organizations ... legal entities that exist ... at the time of entry"), met één vertegenwoordiger. Dortus kan dus zelf inzenden; het geld gaat naar Dortus.
- **Meer dan één inzending mag**, als ze echt verschillen.
- Hulp van derden mag zolang het werk en de rechten van de inzender zijn (Reddit-regels: "An Entrant may contract with a third party for technical assistance ... provided ... the Entrant owns all rights"). AI-gereedschap is bij Cloud9 en Kiroween zelfs onderdeel van de opdracht.
- **Uitbetaling:** binnen 60 dagen na de ingevulde formulieren (belasting, verklaring) (GEZIEN). Reddit: uitslag ±17 dec, geld dus uiterlijk ±half februari. Cloud9: uitslag ±8 feb. Codegeist: jurering 5 jan tot 3 feb, uitslag ±15 feb, geld dus pas maart of april; toegezegd binnen 12 weken, op de rekening net erna.

**Waarom wij dit beter kunnen dan de meeste deelnemers (GOK, met reden):** de meeste inzenders zijn studenten of losse ontwikkelaars die er een weekend naast doen; de jury's vragen om "polish", een werkend product en een duidelijk filmpje (Reddit: "The closer to launch quality, the higher the score"; Codegeist: "not just a shallow wrapper or a single hardcoded demo path", GEZIEN). Wij hebben een ploeg die wekenlang fulltime kan bouwen, een keurder, de skill `kijken`, en ervaring met spellen en plugins.

**Het eerlijke risico:**
- Uitslag is aan een jury, dus het kan ook 0 worden. Een hackathon is geen omzet die terugkomt.
- AI-inzendingen zijn in 2026 gewoon; de jury ziet veel van hetzelfde (een HN-draad klaagt dat AI-hackathons op Devpost "repetitive and somewhat random in judging" zijn, zie de zoekresultaten, DERDEN, niet nagelezen).
- Botst met het besluit van 18 nov 18:40 (geen nieuwe producten tot 9 dec) en kost bouwtijd naast Hats. Maar het besluit van 19 nov 01:21 (snel veel geld is hoofdzaak) is nieuwer; de hoofdchat moet dit opnieuw wegen.
- Atlassian staat bij ons als platform op "gestopt" (te weinig installs). Dat feit verandert niet; hier draait het om prijzengeld, niet om installs. We gebruiken de Atlassian-koppeling in Claude niet (harde regel 7); Forge bouwen we met de gewone CLI.
- Voor Cloud9 moet echt een JetBrains-tool gebruikt worden; of dat in onze cloudsessies kan (Junie of een IDE zonder scherm) is ONBEKEND.

**Kosten:** €0 (alle accounts gratis). **Wat Thijs moet doen:** Devpost-account (of voor Dortus als bedrijf), gratis Atlassian-ontwikkelaarsaccount plus een API-sleutel als GitHub-secret, een Reddit-account voor Dortus om de Devvit-app te uploaden, ja op elke inzendtekst (regel 4), en na winst de belastingformulieren. GOK ±30 minuten per hackathon plus ±20 minuten na winst.

**Verwachte euro's (GOK):** Codegeist: bij ±150 tot 250 inzendingen en 33 geldprijzen wint ruwweg 1 op de 5 tot 8; een gepolijste inzending heeft misschien 15 tot 25% kans op een prijs, twee verschillende inzendingen samen ±30 tot 40%. Reddit: 12 geldplekken voor spellen op ±500 inzendingen, met een sterk spel 5 tot 10%; de categorie "ported" is kleiner. Cloud9: 7 prijzen, minispelcategorie misschien ±60 inzendingen, plus de AI-verhaalprijs. **Samen met 4 tot 5 goede inzendingen: kans op minstens één prijs ±50%, verwacht €2.000 tot €6.000 toegezegd binnen 12 weken, met een kleine kans (±5 tot 10%) op €15.000 of meer.** Daarna herhaalbaar: er staat altijd ±$500.000 open.

**Bijvangst:** het Reddit-spel kan daarna in de Reddit Developer Funds (Reddit betaalt per app op gebruik; de voorwaarden voor H2 2026 bestaan, GEZIEN als doorverwijzing op [developers.reddit.com](https://developers.reddit.com/docs/earn-money/reddit_developer_funds), inhoud achter Cloudflare dus niet gelezen; eerder in de repo: tot $3.500 per app t/m 31 dec 2026, `platformen/pionier/voorstellen/reddit-devvit.md`). Hetzelfde HTML5-spel kan ook naar Poki of CrazyGames (zie route 4). De Codegeist-app kan in de Atlassian Marketplace (bonusprijs $1.500).

**Eerste stap:** hoofdchat beslist vandaag. Daarna één agent op Reddit (dagspel op basis van Gloop's Hat Tower, klaar vr 4 dec, keuring ma 7 dec), één op Codegeist (twee verschillende apps, klaar vr 18 dec). Cloud9 begint na 8 dec. Thijs maakt de accounts.

---

## Route 2. Bug bounty met een Claude-hackbot (NIEUW, grijs gebied in de praktijk, legaal binnen de regels)

**Wat:** programma's op HackerOne betalen per gevonden lek. Sinds februari 2025 laat HackerOne "AI hackbots" toe onder eigen regels, en de AI-onderzoeker XBOW stond bovenaan de Amerikaanse ranglijst (GEZIEN, [HackerOne-blog, 26 jun 2025](https://www.hackerone.com/blog/ai-hackbots-security-testing-update): "XBOW climbed to the top of the US leaderboard, measured by reputation").

**Waarom het lokt:** geld per vondst, binnen weken, en code lezen en testen is wat agents goed doen.

**Waarom ik het laag zet:**
- De markt wordt overspoeld door AI-meldingen van slechte kwaliteit. curl stopte in januari 2026 met zijn bug bounty om precies die reden (DERDEN, [Hackaday 26 jan 2026](https://hackaday.com/2026/01/26/the-curl-project-drops-bug-bounties-due-to-ai-slop), [TechRadar](https://www.techradar.com/pro/security/curl-will-stop-bug-bounties-program-due-to-avalanche-of-ai-slop)). HackerOne zelf noemt valse en verzonnen meldingen het grootste probleem (zelfde blog).
- Juridisch: buiten de scope van een programma testen is computervredebreuk. Binnen de scope is het legaal, maar één fout van een agent raakt de naam van Thijs.
- Uitbetaling vraagt een account met ID en belastinggegevens van Thijs; onze cloudsessies hebben een beperkte netwerktoegang (proxy met toegestane adressen), wat testen van andermans sites lastig of onmogelijk maakt (GOK, niet geprobeerd en mag ook niet zonder account).
- XBOW is een bedrijf met veel geld en eigen "validators"; wij beginnen bij nul.

**Kosten:** €0. **Thijs:** account, ID, belastingformulier, en een ja per melding (gaat onder zijn naam). **Verwacht (GOK):** €0 tot €2.000 in 12 weken, kans op iets ±15%. Alleen proberen als route 1 loopt en er een agent over is, en dan alleen programma's die AI uitdrukkelijk toestaan.

---

## Route 3. Chrome-extensie voor gebruikers van ChatGPT, Claude en Gemini, met Pro via Polar of Gumroad (HERWOGEN, geen nieuw platform)

**Wat:** een extensie die functies toevoegt aan AI-chats (mappen, export, prompts, zoeken in oude chats), gratis plus Pro. Kai bouwt nu een andere Chrome-extensie (Google Agenda in bulk, `platformen/chrome/status.md`); dit is een tweede kandidaat met beter geldbewijs.

**Wie verdient er nu:** "Superpower for AI", 5 extensies voor Gemini, Claude, NotebookLM, Grok en ChatGPT, $7,99 per maand of $99 eenmalig: $16.835 sinds dec 2025, $2.080 in 30 dagen (GEZIEN in G via TrustMRR, geverifieerd: `afkijken-2026-11-18/G-omzet-makers.md` regel 16). Sublo (ondertitels) haalt ±$950 per maand "zonder marketing, alleen via de Chrome Web Store" (zelfde bron, regel 15).

**Waarom wij:** gewone webcode, in de cloud te testen; kassa via Polar of Gumroad die we al hebben (geen nieuw betaalaccount).

**Risico:** veel concurrentie; OpenAI en Anthropic bouwen zulke functies zelf in (Kingmaker-wet 4); ze kunnen hun pagina's veranderen zodat de extensie breekt. Groei gaat via zoeken in de winkel, dus eerder maanden dan weken.

**Kosten:** $5 Chrome-ontwikkelaarsaccount (staat al op de lijst van Thijs). **Verwacht (GOK):** €100 tot €1.000 in 12 weken (Superpower deed ±$1.400 per maand gemiddeld over 12 maanden, wij beginnen bij nul). Kans middel-laag.

---

## Route 4. Eén HTML5-spel, drie kassa's (HERWOGEN, koppelt aan route 1)

**Wat:** het dagspel voor de Reddit-hackathon is gewone webcode. Daarna zetten we hetzelfde spel op Poki en CrazyGames. Die zijn al gewogen (beide 6, "ja als kleine proef", `platformen/verkenner/onderzocht.md`) maar nooit gestart.

**Geld:** Poki deelt de reclame 50/50 en geeft 100% van eigen verkeer; CrazyGames geeft 60% van de reclame en 70% van aankopen, uitbetaling vanaf €100 (DERDEN, [Cinevva-gids, nov 2026](https://app.cinevva.com/guides/web-game-monetization)). Wat een spel per 1.000 keer spelen oplevert staat nergens openbaar (zelfde bron: "There is no fixed payment per game play").

**Nieuw feit:** de bouwkosten zijn bijna nul als het spel toch al voor de hackathon gemaakt wordt.

**Risico:** Poki kiest zelf welke spellen erin komen; eerder bleek dat ONBEKEND is hoeveel een spel bij CrazyGames echt verdient (`platformen/herweger/crazygames.md`).

**Kosten:** €0. **Thijs:** ontwikkelaarsaccounts (betaalgegevens). **Verwacht (GOK):** €0 tot €1.000 in 12 weken; meer pas na maanden.

---

## Afgeschoten in deze run (kort, zodat niemand het opnieuw voorstelt)

| Route | Waarom niet | Bron |
|---|---|---|
| **GitHub- en Algora-bounties** (betaald per samengevoegde PR) | Van 1.000 "bounty"-issues waren er maar 89 (8,9%) echte dollarbounties; de rest nep, automatisch gemaakt, verlopen of al vergeven; bij meer dan 10 reacties wint minder dan 3%; de eerste PR's binnen uren winnen. Overspoeld door AI-PR's. Is bovendien klussen voor anderen. | DERDEN, [dev.to, mei 2026](https://dev.to/zeroknowledge0x/i-analyzed-1000-github-bounty-issues-heres-what-actually-pays-and-whats-a-waste-of-time-geb) |
| **Kit met onze werkwijze verkopen** (CLAUDE.md, skills, keurder, "een AI-bedrijf in een doos") | Een vergelijkbaar AI-agentbedrijf verkocht precies zo'n kit ($29, 8 CLAUDE.md-sjablonen, 15 skills): "Revenue so far: $0", en "I published 13 articles in 3 weeks. Nobody read them." Onze repo is bovendien openbaar, dus gratis te kopiëren. | DERDEN, [The $200/Month CEO, 12 mrt 2026](https://buttondown.com/the200dollarceo/archive/grove-i-built-an-ai-coding-kit-heres-what-i) |
| **Subsidies (NLnet)** | Geld per mijlpaal, beslissing duurt maanden, alleen open-source internettechniek. NGI Zero Commons Fund is dicht (laatste ronde 1 jun 2026); volgende deadline van andere fondsen 3 jan 2027; €5.000 tot €50.000 per project. Past niet in 12 weken en niet bij onze producten. | GEZIEN, [nlnet.nl/commonsfund](https://www.nlnet.nl/commonsfund) |
| **Dataverslag uit ons eigen onderzoek verkopen** ("welke winkel betaalt kleine makers") | Alle metingen staan al gratis in onze openbare repo; geen vergelijkbaar betaald verslag met verkoopcijfers gevonden. Hooguit gratis lokkertje voor de maillijst. | GOK |
| **Grijs tot illegaal, niet doen:** AI-muziek op Spotify met nepstreams (fraude), AI-werk aanbieden op platforms voor mensenwerk zoals data-labelen alsof een mens het doet (misleiding), airdrop-farmen met veel accounts (tegen de regels en kost geld), lijsten met persoonsgegevens schrapen en verkopen (AVG), grijze game-sleutels doorverkopen | Strafbaar, fraude of in strijd met de AVG; botst ook met "niets nep" (besluit 9 nov 22:56). | eigen afweging |
| **AI-boeken op Amazon KDP, Etsy-downloads, Notion- of Framer-templates** | Al eerder dicht of overvol verklaard zonder eigen publiek (besluit "geen nieuwe producten op Figma, Notion, itch.io, Etsy of Fab"); geen nieuw feit gevonden. | `organisatie/archief/`, G en H |

---

## Rangorde

| # | Route | Verwachte euro's in 12 weken (GOK) | Kans op iets | Kosten | Eerste stap |
|---|---|---|---|---|---|
| 1 | **Hackathon-prijzen** (Reddit Game of the Day 8 dec, Codegeist 22 dec, Cloud9 x JetBrains 12 jan) | €2.000 tot €6.000 toegezegd (deel komt pas na week 12 binnen), kleine kans op €15.000+ | ±50% op minstens één prijs bij 4 tot 5 goede inzendingen | €0; Thijs ±30 min per hackathon | Hoofdchat beslist vandaag; Thijs maakt Devpost-, Atlassian- en Reddit-account; agent start het dagspel (Gloop's Hat Tower, categorie "ported") |
| 2 | **Eén HTML5-spel naar Poki en CrazyGames** (na route 1) | €0 tot €1.000 | laag-middel | €0; ontwikkelaarsaccounts | Het Reddit-spel zo bouwen dat het ook los in de browser draait |
| 3 | **Chrome-extensie voor AI-chats met Pro** | €100 tot €1.000 | middel-laag | $5 (ja van Thijs) | Ideeëntest (9 vragen) door Kai naast zijn agenda-extensie |
| 4 | **Bug bounty met een Claude-hackbot** | €0 tot €2.000 | ±15% | €0; account en ID van Thijs | Pas na route 1; eerst een lijst van programma's die AI uitdrukkelijk toestaan |
| 5 | **Kit met onze werkwijze / dataverslag** | €0 tot €300 | laag | €0 | Niet bouwen; hooguit gratis lokkertje voor Kit |

**Advies in één zin:** zet vandaag twee agents op hackathons (Reddit nu, Codegeist direct erna), want dat is het enige geld dat we in weken kunnen verdienen zonder in de mediaan van een winkel te verdwijnen, en het spel en de app die eruit komen, kunnen daarna ook nog verkopen.
