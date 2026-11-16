# Gratis tools van Product Hunt die ons helpen verspreiden (16 nov 2026)

Opdracht van Thijs: Product Hunt doorzoeken op gratis tools voor ons echte knelpunt, verspreiden. Streng gekeken: wat werkt zonder geld, zonder dat agents op accounts van Thijs inloggen, en past bij wat we nu doen (dagelijkse korte filmpjes vanaf 17 nov, Reddit via de hoofdchat, Steam-pagina en playtest voor Hats of the Fallen, dortus.com zonder analytics).

Eerlijke uitkomst: **vier echte JA's**. De andere vier in de top 8 zijn de beste MISSCHIEN's, zo aangegeven. Meer JA's zou opvulling zijn.

## Top 8

1. **HyperFrames (HeyGen), JA.** Open source (Apache 2.0) gereedschap dat van HTML, CSS, beelden en filmpjes een MP4 maakt, met een CLI en skills voor Claude Code. Draait op Linux met Node 22+, FFmpeg en headless Chrome, ook in Docker, dus in GitHub Actions. Geen account, geen sleutel, geen kosten per render (GEZIEN in de README). Waarom bovenaan: Chris begint di 17 nov met elke dag een kort filmpje. Hiermee maakt een agent in de cloud van onze echte opnames en schermen een verticaal filmpje met titels, tekst in beeld en ondertitels, zonder dat iemand een editor opent. Let op: de betaalde Studio Pro en de AI-video van HeyGen niet gebruiken (geen AI-beeld, regel voor Steam en eerlijke beelden).
2. **Forge (gratis Starter) met Playtester.gg, JA.** Gratis tot 5.000 spelers: aanmeldingen, e-mails, enquêtes op het web, Steam-sleutels uitdelen, spelerscijfers, Discord-koppeling, build vóór Steam verspreiden en een landingspagina (GEZIEN op forge.gg/pricing). Playtester.gg geeft volgens Forge gratis toegang tot een gemeenschap van 250.000+ speltesters. Waarom: Hats of the Fallen heeft speltesters en wishlists nodig ruim voor maart 2027; dit is gratis en precies daarvoor gemaakt. Vraagt: een account van Thijs (eenmalig) en de build. Pro is $29 per maand, niet nodig.
3. **Amami, JA.** Webanalytics zonder cookies voor dortus.com (GitHub Pages heeft nu niets: 0 treffers op analytics-scripts). Gratis: 100.000 gebeurtenissen per maand, 5 sites, 7 dagen bewaren, API om te lezen en 50 MCP-vragen per dag, geen creditcard (GEZIEN op amami.dev). Waarom: zonder meten weten we niet of een Reddit-post of filmpje bezoekers oplevert. Een agent kan met een leessleutel (als GitHub-geheim) zelf de cijfers ophalen. Vraagt: account van Thijs, één script-regel op de site. Bewaartermijn van 7 dagen is kort: agents moeten de cijfers dagelijks wegschrijven in de repo.
4. **FreeScan.app, JA (eenmalig).** Gratis controle van een openbare webpagina op SEO, vindbaarheid in AI-antwoorden, veiligheid, toegankelijkheid en ontwerp, zonder aanmelden (GEZIEN). Pro is $19 per maand, niet nodig. Waarom: snelle lijst met fouten op dortus.com en de productpagina's, die agents daarna zelf oplossen. Vraagt niets. Werkt in de browser, dus via de hoofdchat (Chrome) of Thijs.
5. **Rank Kiwi, MISSCHIEN.** Gratis Chrome-extensie zonder login die per maker laat zien welke Shorts en Reels veel beter liepen dan normaal, met transcript en download (GEZIEN: "Free forever, No login"). Helpt Chris uitzoeken welk soort filmpje werkt. Agents in de cloud kunnen het niet gebruiken; alleen de hoofdchat met Chrome of Thijs.
6. **Open Screenshot Generator, MISSCHIEN.** Gratis, open source (MIT), geen account, geen watermerk; met CLI (`npx open-screenshot-generator`, Node en Chrome) voor winkelbeelden en voorbeeldfilmpjes (GEZIEN in README). Sterk voor App Store en Google Play; onze winkels (Garmin, Blender, JetBrains, Obsidian, Steam) vragen andere beelden en Pillow werkt al. Proberen als de winkelbeelden van Gloop of Ebb beter moeten.
7. **Cut/Storm, MISSCHIEN.** Zelf te draaien video-editor in één Docker-container: Whisper-ondertitels lokaal, knippen, bijsnijden naar 9:16, stiltes eruit. Geen externe API, geen account (GEZIEN in README). Nuttig als filmpjes met stem komen; voor filmpjes met alleen beeld en tekst is HyperFrames genoeg.
8. **BugDrop, MISSCHIEN.** Gratis, open source (MIT) knop op een website waarmee bezoekers een fout of idee met schermafbeelding melden; het wordt een GitHub-issue (GEZIEN). Vraagt: Thijs installeert de GitHub-app op een repo. Risico: meldingen komen openbaar in een openbare repo en kunnen spam zijn. Pas zinvol als er echte gebruikers op een pagina komen.

**Buiten Product Hunt, wel gezien en waarschijnlijk een JA:** Steam Page Analyzer (steampageanalyzer.com) beoordeelt een Steam-winkelpagina (capsule, schermen, tekst, tags). Volgens hun eigen `agents.md`: REST-API en MCP "No API key. No account. No OAuth.", alleen lezen, 2 gratis controles per dag; het volledige rapport kost $29 per game. Niet gevonden op Product Hunt, dus niet in de lijst, maar een agent kan het voor Hats meteen gebruiken zodra de pagina live staat.

## Volledige tabel

Uitleg: Gratis = wat ik op de eigen site of in de README zag. "niet gezien" = stond niet op wat ik kon lezen. PH = productpagina op Product Hunt. Datum = lancering op Product Hunt.

### 1. Verspreiden (video, ondertitels, plannen, communities)

| Tool | Link | Wat het doet | Gratis en niet gratis | Knelpunt | Vraagt (risico) | Oordeel |
|---|---|---|---|---|---|---|
| HyperFrames | https://github.com/heygen-com/hyperframes , PH /products/heygen (4 okt 2026) | HTML en media worden een MP4, gemaakt voor agents | Kern en CLI gratis, Apache 2.0, geen kosten per render. Studio Pro $25 per maand (AI-modellen) | 1, 5 | Niets. Node 22+, FFmpeg, Chrome | JA |
| Framefields | https://github.com/gatewai-dev/framefields , PH 16 okt 2026 | Video uit TypeScript, rendert op de GPU via WebGPU | Apache 2.0 gratis. Optionele gateway met sleutel | 1, 5 | Niets, maar draait op GPU; of het op een runner zonder GPU werkt: niet gezien | MISSCHIEN |
| Remocn (Studio) | https://remocn.dev , PH 5 okt 2026 | 900+ MIT-blokken voor Remotion, plus Mac/Linux-app | Blokken MIT, app gratis. Remotion zelf heeft een eigen licentie | 1 | Niets | NEE (dubbel met HyperFrames) |
| Remotion Bits | PH /products/remotion-bits | Kant-en-klare animaties voor Remotion | Open source (repo av/remotion-bits) | 1 | Niets | NEE (dubbel) |
| VideoFlow | https://videoflow.dev , PH 11 mei 2026 | JSON wordt video, open source TypeScript | Open source; prijzen niet gezien | 1 | Niets | NEE (dubbel) |
| WeftCut | https://weftcut.com , PH 30 sep 2026 | Desktop-editor die een agent via MCP bestuurt | Gratis, MIT | 1 | Draait op een eigen computer, niet in de cloud | NEE |
| OpenVids | PH 8 okt 2026 | Desktop-editor die agents bedienen (Mac, Windows) | Open source volgens PH; prijs niet gezien | 1 | Desktop | NEE |
| EasyCut | PH 5 okt 2026 | Bewerkt filmpjes die Claude maakte op een tijdlijn | niet gezien | 1 | niet gezien | NEE |
| Clayzo | PH 23 okt 2026 | Animaties en motion design via een coding-agent | niet gezien | 1 | niet gezien | NEE |
| Cut/Storm | https://github.com/vorniches/cutstorm , PH 21 apr 2026 | Korte clips met lokale Whisper-ondertitels, Docker | Gratis, zelf hosten, geen externe API | 1 | Niets; zonder inlog, dus niet open op internet zetten | MISSCHIEN |
| SubForge | PH 23 mei 2026 | Whisper-ondertitels inbranden op eigen computer | niet gezien | 1 | Desktop | NEE |
| Captionly | PH 8 jul 2026 | Ondertitels met Whisper in de browser | "100% private", prijs niet gezien | 1 | Browser, geen agent | NEE |
| CapFlow Studio | PH 13 mei 2026 | Ondertitels in de browser via WebAssembly | "mostly free" volgens PH | 1 | Browser | NEE |
| FREE AI Auto Subtitle Generator | PH 10 jul 2026 | Windows-app voor ondertitels (Whisper of Groq) | Gratis, open source volgens PH | 1 | Windows-desktop | NEE |
| SubtitleGenerator | PH 15 aug 2026 | Ondertitels maken en stylen in de browser | Gratis 60 video's van 1 minuut per maand, zonder aanmelden (PH-tekst); site niet bereikt | 1 | Browser | NEE |
| SupoClip | https://github.com/FujiwaraChoki/supoclip , PH 11 okt 2026 | Lange video wordt verticale clips met ondertitels | AGPL, zelf hosten gratis; gehoste prijs niet gezien | 1 | AI-sleutels voor het kiezen (niet gezien welke) | NEE (we hebben geen lange video's) |
| OpusClip 4.0 | https://www.opus.pro , PH 2 nov 2026 | AI knipt ruwe beelden tot clips | niet gezien | 1 | Account | NEE |
| Riverside Agents | PH 26 okt 2026 | AI-agents die video maken, knippen en posten | niet gezien | 1 | Account | NEE |
| Instagram Edits for Desktop | PH 5 nov 2026 | Gratis video-editor van Instagram op Mac, met MCP | Gratis volgens PH | 1 | Mac en Instagram-account | NEE |
| OpenScreen | https://github.com/siddharthvaddem/openscreen | Schermopname voor demo's, open source | Gratis, geen watermerk (repo) | 1 | Desktop; onze opnames komen al uit Actions | NEE |
| OpenScreen 2 | PH 28 sep 2026 | Opname met automatische zoom, edit via MCP | Open source volgens PH | 1 | Desktop | NEE |
| Reelbird | https://github.com/btahir/reelbird , PH 13 okt 2026 | Gratis Mac-recorder met deellink en zoom | Gratis, open source | 1 | Mac, eigen S3-opslag | NEE |
| Screen Studio 4.0 | PH 30 okt 2026 | Mac-recorder met zoom en bewerken op tekst | Betaald (niet gezien) | 1 | Mac | NEE |
| Smooth Recorder | PH 3 okt 2026 | Mac-opnames die er bewerkt uitzien | niet gezien | 1 | Mac | NEE |
| Lumiko | PH 14 sep 2026 | Opname in de browser met automatische zoom | niet gezien | 1 | Browser | NEE |
| ScreenCursor | PH 10 sep 2026 | Opname met zoom op elke klik, lokaal | niet gezien | 1 | Browser | NEE |
| Flicka | PH 20 sep 2026 | Chrome-recorder voor productdemo's | niet gezien | 1 | Browser | NEE |
| Prequel | PH 29 aug 2026 | Mac-recorder met zoom en camera | niet gezien | 1 | Mac | NEE |
| CaptureFlow | https://captureflow.dev , PH 15 okt 2026 | Open source recorder met deellinks | Gratis tot 25 opnames van 5 min per persoon; daarna vanaf $5 | 1 | Account | NEE |
| isolate.video | https://isolate.video , PH 12 aug 2026 | Schermopname wordt productvideo met zoom en muziek | Gratis video maken; lifetime-deal betaald | 1 | Account | NEE |
| Slideshot | PH 20 mei 2026 | Agent neemt een demo van een web-app op via MCP | niet gezien | 1 | Werkt voor web-apps; onze producten zijn dat niet | NEE |
| Specreel | https://github.com/specreel/specreel , PH 13 okt 2026 | Playwright-traces worden demo's | Open source | 1 | Alleen web-apps | NEE |
| Takes for Mac | PH 11 okt 2026 | Teleprompter en opname, Claude Code knipt | Gratis, open source volgens PH | 1 | Mac en een gezicht voor de camera | NEE |
| Jupitrr Cut | https://github.com/Jupitrr-ai/JupitrrCut , PH 5 sep 2026 | Telefoon-app met teleprompter, stiltes eruit | Open source | 1 | Telefoon | NEE |
| Rank Kiwi | https://rankkiwi.com , PH 5 okt 2026 | Vindt uitschieters bij Shorts en Reels, transcript en download | Gratis, geen login (GEZIEN) | 1 | Chrome-extensie; niet voor cloud-agents | MISSCHIEN |
| Scrollsnacks | https://scrollsnacks.com , PH 4 nov 2026 | Lanceervideo's per seconde ontleed (hook, probleem, CTA), met MCP | Gratis: 20 MCP-vragen per dag en basis; Pro $13 tot $16 per maand | 1 | Account (Thijs) voor MCP | MISSCHIEN |
| Hookest | https://hookest.com , PH 7 sep 2026 | Bibliotheek met virale openingen van Shorts | Bekijken gratis; downloaden en editor alleen Pro | 1 | Account | NEE |
| How It Spread | https://howitspread.com , PH 19 okt 2026 | Hoe iets viraal ging, per tijdlijn | Gratis account om tijdlijnen te openen; prijzen niet gezien | 1 | Account | NEE |
| Searchtok | PH 19 okt 2026 | TikTok en Instagram doorzoekbaar voor een agent via MCP | niet gezien | 1 | niet gezien | MISSCHIEN |
| Any Video to Text | PH 3 nov 2026 | Transcript van een TikTok- of YouTube-link | niet gezien | 1 | Chrome-extensie | NEE |
| YouTube Transcript Tool | PH 25 mrt 2026 | YouTube-video naar tekst | niet gezien | 1 | niet gezien | NEE |
| Thumbmagic | PH 20 jun 2026 | AI-thumbnails | niet gezien | 1 | AI-beeld | NEE |
| AudienceCue | https://audiencecue.com , PH 13 jun 2026 | YouTube-reacties worden een rapport | niet gezien | 1 | Pas zinvol met een kanaal vol reacties | NEE |
| Postiz | https://github.com/gitroomhq/postiz-app , PH 26 apr 2026 | Plannen en plaatsen op 30+ netwerken, met CLI en API voor agents | Zelf hosten gratis (open source). Cloud: geen gratis plan, 7 dagen proef, vanaf $29 per maand | 1 | Server die altijd aan staat en koppeling met de sociale accounts van Thijs (groot risico) | MISSCHIEN |
| BrightBean Studio | https://github.com/brightbeanxyz/brightbean-studio , PH 8 okt 2026 | Open source Buffer-alternatief | Zelf hosten gratis | 1 | Server en accounts van Thijs | MISSCHIEN |
| PostSider | https://postsider.com , PH 17 sep 2026 | Plannen en plaatsen via MCP en API | 7 dagen proef, daarna vanaf $20 per maand | 1 | Accounts van Thijs | NEE |
| PostNitro for Agents | https://postnitro.ai , PH 7 okt 2026 | Agent ontwerpt en plaatst carrousels | niet gezien | 1 | Accounts | NEE |
| Beaquaro Studio | PH 2 nov 2026 | Schrijf één keer, plaats overal, link in bio | "Free to start" volgens PH | 1 | Accounts | NEE |
| LayerProof Matte 3.0 | PH 13 aug 2026 | 50 merkposts in één keer | niet gezien | 1 | AI-beeld | NEE |
| Agent Craft, Okara, Naise AI, SuperCMO AI | PH sep en okt 2026 | AI-marketingafdeling of "AI CMO" | niet gezien | 1 | Accounts, algemene AI | NEE (doen we zelf al) |
| lurk | PH 29 sep 2026 | Volgt Reddit en X op mensen die iets als ons product zoeken, stuurt naar e-mail, Discord of webhook | "Free, open-source" volgens PH; repo en site niet gevonden | 1 | niet gezien | MISSCHIEN |
| RedSignal | https://github.com/ivucicev/redsignal , PH 12 mei 2026 | Volgt subreddits op zoekwoorden, AI filtert | Gratis, MIT, zelf hosten | 1 | Reddit API-gegevens van een account van Thijs plus optioneel een AI-sleutel | MISSCHIEN |
| Ownfeed | PH 6 okt 2026 | Leest Reddit, X, Bluesky en HN en houdt posts over van mensen die jouw product nodig hebben | niet gezien | 1 | niet gezien | MISSCHIEN |
| Subreddit Finder | PH 28 jul 2026 | Plak je product-URL, krijg passende subreddits | Gratis, zonder aanmelden (PH-tekst); site niet gevonden | 1 | Niets | MISSCHIEN |
| Free Reddit Monitor | PH 18 apr 2026 | Live feed van tot 8 subreddits met zoekwoorden | Gratis volgens naam; site niet gevonden | 1 | niet gezien | MISSCHIEN |
| Sublookout | PH 1 apr 2026 | Reddit-meldingen bij treffers | niet gezien | 1 | niet gezien | NEE |
| Antibot | PH 26 jun 2026 | AI-communitymanager voor Discord | niet gezien | 4 | We hebben nog geen Discord | NEE |
| Volvox Bot, Kitcord | PH jun en mei 2026 | Discord-bots en bot-bouwer | niet gezien | 4 | Discord-server nodig | NEE |
| Guild Manager | PH 17 sep 2026 | Gilde beheren in Discord | Gratis voor gilden | 4 | Past niet | NEE |

### 2. Winkelpagina's en zichtbaarheid

| Tool | Link | Wat het doet | Gratis en niet gratis | Knelpunt | Vraagt (risico) | Oordeel |
|---|---|---|---|---|---|---|
| FreeScan.app | https://www.freescan.app , PH 1 sep 2026 | Gratis controle op SEO, AI-vindbaarheid, veiligheid, toegankelijkheid, ontwerp | Audit gratis zonder aanmelden; Pro $19 per maand | 2 | Niets; browser nodig | JA |
| Open Screenshot Generator | https://openscrgen.app , PH 20 jul 2026 | Winkelbeelden en voorbeeldfilmpjes, met CLI en MCP | Gratis, MIT, geen account, geen watermerk | 2, 5 | Niets. Node 20.12+ en Chrome | MISSCHIEN |
| Artboard Studio | PH 7 jul 2026 | Gratis winkelbeelden in de browser | Gratis, open source volgens PH | 2 | Browser | NEE |
| App Store Screenshots (skill) | PH 4 okt 2026 | Skill voor Claude Code die een lokale editor voor winkelbeelden bouwt | Gratis, open source volgens PH; repo niet gevonden | 2, 5 | Niets | MISSCHIEN |
| StoreLocale | PH 28 okt 2026 | Vertaalt tekst in winkelbeelden | niet gezien | 2 | niet gezien | NEE |
| Shotcandy | https://github.com/btahir/shotcandy , PH 27 sep 2026 | Schermafbeeldingen mooier maken in de browser | Gratis, open source | 2 | Browser; Pillow doet dit al | NEE |
| Portfolio Frame | PH 14 sep 2026 | Schermafbeeldingen kaderen en annoteren | niet gezien | 2 | Browser-extensie | NEE |
| Mokkit | PH 25 mrt 2026 | Schermafbeelding wordt geanimeerd beeld | niet gezien | 2 | niet gezien | NEE |
| Kitbitz | https://kitbitz.art , PH 12 aug 2026 | 2.000+ handgetekende illustraties, CC0 | Gratis (CC0 volgens site en PH) | 2 | Niets; nagaan of het echt handwerk is | MISSCHIEN |
| Waitlister | https://waitlister.me , PH 25 apr 2026 | Wachtlijst met landingspagina en verwijzingen | Gratis plan; betaald vanaf $19 per maand | 2 | Account | NEE (Steam-wishlist en GitHub Pages volstaan) |
| HTML Pub | https://htmlpub.com , PH 4 mrt 2026 | AI-HTML wordt een live pagina via MCP | Bouwen gratis, live vanaf $10 per maand | 2 | Account | NEE (we hebben GitHub Pages) |
| FeatDrop | https://www.featdrop.com , PH 7 apr 2026 | Openbare changelog-gemeenschap | niet gezien | 2 | Account | NEE |
| Shipnoted | https://shipnoted.com , PH 5 nov 2026 | Changelog, feedbackbord en roadmap vanuit git | Gratis plan (1 project, badge); Pro $90 per jaar | 2, 4 | Account, GitHub-koppeling | NEE |
| OpenSEO | PH 17 jul en 6 okt 2026 | Open source alternatief voor Semrush, data via MCP | niet gezien | 2 | niet gezien | MISSCHIEN |
| Free AI SEO Auditor | PH 11 mei 2026 | Open source scan voor AI-zoeken | Gratis volgens PH | 2 | Repo niet gevonden | NEE (FreeScan dekt het) |
| IndexedAI | PH 8 mei 2026 | Score hoe leesbaar je site is voor AI-agents | niet gezien | 2 | niet gezien | NEE |
| Rankfender, MentionBird, Dageno, Notra, Proofsource | PH sep tot nov 2026 | Zichtbaarheid in AI-antwoorden | niet gezien | 2 | Accounts | NEE |
| Google Search Profiles | PH 4 jun 2026 | Profiel voor makers in Google Zoeken | niet gezien | 2 | Google-account van Thijs | MISSCHIEN |
| Lovable Growth Tools | PH 14 okt 2026 | Groeiplan in Lovable | niet gezien | 2 | Lovable | NEE |

### 3. Meten

| Tool | Link | Wat het doet | Gratis en niet gratis | Knelpunt | Vraagt (risico) | Oordeel |
|---|---|---|---|---|---|---|
| Amami | https://amami.dev , PH 14 jul 2026 | Analytics zonder cookies, vragen via MCP | Gratis: 100K gebeurtenissen per maand, 5 sites, 7 dagen bewaren, API lezen, 50 MCP per dag; Starter vanaf $9 | 3, 5 | Account Thijs; leessleutel als GitHub-geheim | JA |
| Analytiics | https://www.analytiics.co , PH 7 sep 2026 | Analytics die je coding-agent instelt | Gratis: 25.000 gebeurtenissen per maand, 1 project; vanaf $8 | 3 | Account; aanmelden via Thijs | MISSCHIEN (reserve) |
| Known Agents | https://knownagents.com , PH 28 apr 2026 | Ziet welke AI-bots je site bezoeken en verkeer uit ChatGPT en co | Gratis: 1 project, 100K gebeurtenissen; Startup $29 | 3 | Account | MISSCHIEN |
| Pulse Analytics | https://pulse.ciphera.net , PH 13 okt 2026 | Analytics zonder cookies met uptime en Search Console | "Free Personal tier"; grenzen niet gezien | 3 | Account | MISSCHIEN |
| Statable Analytics | https://statable.com , PH 15 sep 2026 | Analytics voor mens en agent | 30 dagen proef, daarna vanaf $9 per maand | 3 | Account | NEE |
| YourTraffic | PH 6 jul 2026 | Open source analytics met MCP | Open source; eigen Postgres nodig | 3 | Database | NEE |
| Open Analytics | PH 18 sep 2026 | Analytics zonder cookies, koppelt aan Stripe of Polar | niet gezien | 3 | Account | NEE |
| Blipstat | PH 27 apr 2026 | Analytics met één script | niet gezien | 3 | GitHub-login | NEE |
| Raah.dev | PH 27 okt 2026 | Omzet, analytics en snelheid in één scherm | niet gezien | 3 | Account | NEE |
| Salience | PH 16 okt 2026 | Elk verzoek aan je site uit server- en CDN-data | niet gezien | 3 | Toegang tot serverlogs (GitHub Pages heeft die niet) | NEE |
| WebDecoy for Vercel | PH 21 sep 2026 | Herkent nep-crawlers | niet gezien | 3 | Alleen Vercel | NEE |
| Pulsetic RUM | PH 14 sep 2026 | Uptime gemeten bij echte bezoekers | niet gezien | 3 | Account | NEE |
| GAtrends | PH 12 nov 2026 | Meldingen bij pieken in zoekwoorden | Prijspagina met kortingscode, gratis niet gezien | 3 | Account | NEE |
| CrawlRaven | PH 22 jul 2026 | SEO-hub voor Search Console en GA4 | niet gezien | 3 | Google-accounts van Thijs | NEE |
| SteamPulse | PH 20 mei 2026 | Steam-markt: 166K+ games, trends | Site gaf fout 502 | 3, 4 | niet gezien | MISSCHIEN |
| Steam Wishlist Pulse | PH (via zoeken) | Volgt wishlists | niet gezien | 3, 4 | Waarschijnlijk Steamworks-toegang | MISSCHIEN |

### 4. Gamedev en feedback

| Tool | Link | Wat het doet | Gratis en niet gratis | Knelpunt | Vraagt (risico) | Oordeel |
|---|---|---|---|---|---|---|
| Forge Starter en Playtester.gg | https://www.forge.gg/pricing , PH 26 mrt 2026 | Playtest, aanmeldingen, enquêtes, Steam-sleutels, Discord, landingspagina; 250K+ speltesters | Starter gratis tot 5.000 spelers; Pro $29 per maand | 4 | Account Thijs, build van het spel | JA |
| Checkpoint Zero | PH 3 jul 2026 | Sociale plek voor indiegames: devlogs, schermen, wishlists, playtests | niet gezien | 4, 2 | Account | MISSCHIEN |
| LudumLanding | https://ludumlanding.com , PH 25 sep 2026 | Feedbackpagina voor het einde van je Steam-demo | $19,99 het eerste jaar, niet gratis | 4 | Account | NEE (Forge doet het gratis) |
| LaunchCrit | PH (via zoeken) | Feedback op Steam-pagina's | Site gaf bijna niets terug | 4 | niet gezien | NEE |
| Mentat AI (Forge) | PH | Marketingchatbot voor indiedevs | niet gezien | 4 | Chatbot | NEE (overslaan: chatbot) |
| BugDrop | https://bugdrop.dev , PH 9 mei 2026 | Feedbackknop op een site wordt een GitHub-issue | Gratis, MIT | 4 | GitHub-app op een repo; openbare issues | MISSCHIEN |
| Deskcord.chat | https://deskcord.chat , PH 17 jul 2026 | Chat op je site, antwoorden vanuit Discord | Gratis 30 gesprekken per maand; Pro $4,99 | 4 | Discord-server | NEE |
| Flockbay | PH 2 nov 2026 | Gratis AI-spelmaker in Godot die zelf speeltest | Gratis volgens PH | 4 | Desktop-editor; we bouwen al via Actions | NEE |
| Our Silly Games | PH 27 okt 2026 | Skills en gratis hosting voor browserspellen | Gratis | 4 | Past niet | NEE |
| Foleyfy | PH 17 sep 2026 | Geluidspakketten uit eigen opnames | In ontwikkeling | 4 | iPhone | NEE |
| Wombo | PH 17 sep 2026 | AI-spelplaatjes en geluid | niet gezien | 4 | AI-beeld (Steam-regel) | NEE |
| Gamosy | PH (via zoeken) | Contact met makers voor games | niet gezien | 4 | niet gezien | NEE |

### 5. Direct bruikbaar voor agents zonder in te loggen

Uit de tabellen hierboven: **HyperFrames** (JA), **Open Screenshot Generator** CLI (MISSCHIEN), **Cut/Storm** in Docker (MISSCHIEN), **Framefields** (MISSCHIEN, GPU onzeker). Buiten Product Hunt: **Steam Page Analyzer** API en MCP zonder sleutel. Alle analytics, Forge en planners vragen een eenmalig account van Thijs; daarna kan een agent vaak met een sleutel verder.

## Hoe ik zocht

- producthunt.com pagina's (topics, categorieën, productpagina's, sitemap, doorverwijzingen) geven met curl een Cloudflare-controle (403). De Atom-feed werkt wel, ook per onderwerp: `https://www.producthunt.com/feed?category=<slug>` geeft de 50 nieuwste van dat onderwerp. Een onbekende slug geeft de gewone voorpagina; die heb ik eruit gefilterd door te vergelijken met de gewone feed.
- 37 onderwerp-feeds gebruikt, onder meer video, marketing, social-media, youtube, analytics, seo, games, indie-games, gifs, community, design-tools, developer-tools, open-source, marketing-automation, customer-communication, user-experience, chrome-extensions, advertising, photography, github, bots, mac, android. Gefilterd op lancering na 16 nov 2025: **1.293 unieke producten**, alle titels en ondertitels doorgelezen.
- Aangevuld met zoekopdrachten `site:producthunt.com` op: Reddit-monitoring, subreddits vinden, speltesters, Steam-wishlist, analytics voor statische sites, winkelbeelden en mockups, Discord-bots, ondertitels, video uit code, devlog en presskit, feedbackknoppen, zoekwoorden, makers voor game-sleutels, GIF-makers, vermeldingen volgen.
- Voor ±130 kandidaten de beschrijving en lanceerdatum gelezen via hunted.space (een site die Product Hunt-lanceringen toont en wel met curl werkt).
- Van ±45 tools de eigen site of prijspagina met curl gelezen, en van 10 open source tools de README op GitHub (licentie, eisen, sleutels).
- Niet gelukt: de echte website van sommige tools vinden (Product Hunt verwijst via een geblokkeerde link). Daar staat "niet gezien". Geen enkele prijs of functie is verzonnen.
- Overgeslagen zoals gevraagd: algemene chatbots, takenlijsten, tools voor Claude-agents naast elkaar, en tools die AI-beeld maken (Steam-regel en de regel van Thijs over eerlijke beelden).
