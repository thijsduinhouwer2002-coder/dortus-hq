# A. Hoe anderen marketing en PR door AI-agents laten doen (onderzoeker A, 19 nov 2026)

Opdracht: `BRIEF.md` hoek A, met de nadruk van Thijs (01:34): hoe makers dit nu echt doen. Bronnen gelezen met curl; Indie Hackers zit achter een Cloudflare-muur ("Just a moment...", GEZIEN), dus die verslagen ken ik alleen uit de titels in zoekresultaten.

Let op bij het lezen: bijna elke bron hieronder verkoopt zelf iets (Postiz, Upload-Post, Luminary Lane, VAOS, Glitch). Waar een cijfer alleen van zo'n verkoper komt, staat dat erbij.

## Voorbeelden

### 1. Larry van Oliver Henry (TikTok-diashows voor twee iOS-apps): het bekendste geval
- **Opzet:** een OpenClaw-agent (Claude als brein, met geheugen en "skills" als markdownbestanden van 500+ regels) op een oude pc met Ubuntu. Maakt per post 6 beelden met OpenAI gpt-image-1.5 (± $0,50 per diashow, $0,25 met de Batch API), zet er hooktekst op, schrijft een bijschrift en zet het via de Postiz-API op TikTok. Leest daarna de cijfers uit Postiz en de omzet uit RevenueCat en kiest daarop de volgende posts (DERDEN: [Postiz-blog 16 apr 2026](https://postiz.com/blog/ai-agent-tiktok-views-postiz-api), [Luminary Lane 15 mrt 2026](https://luminarylane.app/blog/from-larry-to-lane/)).
- **Het belangrijkste detail:** Larry plaatst **niet** openbaar. Hij zet de post met `privacy_level: SELF_ONLY` als concept klaar; Oliver opent TikTok, kiest een trending geluid en drukt op plaatsen, ± 60 seconden per post. Reden: muziek bepaalt het bereik en die kun je via geen enkele API toevoegen (DERDEN, Postiz-blog, met de letterlijke API-aanroep).
- **Opbrengst:** de bronnen spreken elkaar tegen. Postiz: 500.000 weergaven in 5 dagen, 4 posts boven 100.000, $588 MRR in een week. Luminary Lane: 8 miljoen weergaven in een week, $714 MRR. Upload-Post (README): "7M+ views, 1M+ TikTok views, $670/month MRR". Alle drie DERDEN en alle drie verkopers; orde van grootte: honderden dollars per maand erbij, niet duizenden.
- **Wat misging (volgens Luminary Lane, ook een verkoper):** alleen TikTok; de agent "drijft af" als zijn geheugen wordt samengevat (stem in week 4 anders dan in week 1); inloggen en sessies breken; onderhoud aan VPS en Docker.
- **Open source nabouw:** `Upload-Post/upload-post-larry-marketing-skill` op GitHub (README gelezen, GEZIEN): scripts voor beelden maken, tekst erop (node-canvas), plaatsen via Upload-Post op 10 kanalen, cijfers ophalen, en een dagrapport met een vaste beslistabel: veel weergaven + veel conversie = 3 varianten van de winnende hook; veel weergaven + weinig conversie = de oproep of winkelpagina repareren; weinig weergaven + veel conversie = betere hooks; beide laag = helemaal anders.

### 2. "ashen": iOS-app, 3 diashows per dag, een telefoon van $50 als laatste stap
- **Opzet:** agent maakt beelden (Gemini, "Nano Banana 2") volgens een skillbestand, Postiz plant ze in, een goedkope Android-telefoon doet het echte plaatsen. Hele maand april vooruit ingepland (DERDEN: [Postiz-blog 16 apr 2026](https://postiz.com/blog/automate-tiktok-slideshow-marketing-ai-agents-postiz)).
- **Kwaliteit/veiligheid:** eerst 3 dagen het account "opwarmen" als een mens (scrollen, volgen, echte reacties) op hetzelfde toestel; volgens de bron is het overslaan daarvan "the most common reason people fail" en worden nieuwe accounts die meteen ingeplande posts plaatsen geschaduwband (DERDEN, zelfde bron).
- **Opbrengst:** 100+ downloads en 1.000+ likes (DERDEN). Klein; het verhaal is het systeem, niet het geld.

### 3. Felix van Nat Eliason (OpenClaw-agent die een heel bedrijfje runt)
- **Opzet:** agent met browser, sleutels voor domein en Gumroad en $1.000 budget. Schreef een gids van 45 pagina's, bouwde een site, maakte een X-account en postte 3 tot 5 keer per dag (DERDEN: [OpenClaw DC 25 mrt 2026](https://openclawdc.com/blog/openclaw-felix-experiment/)). Andere bronnen noemen later $177.417 totaal (DERDEN, alleen titel gezien: [Mixergy](https://mixergy.com/interviews/how-nat-eliasons-openclaw-earned-177417/amp/)).
- **Opbrengst:** $14.718 in 3 weken (DERDEN). **Maar:** het X-account van Felix had na 21 dagen minder dan 2.000 volgers; het meeste geld kwam van Nats eigen publiek (100.000+ nieuwsbrief, 300.000+ op X) dat hij zelf over het experiment vertelde. Nat greep minstens twee keer in (prijs, een landingspagina die er "spammy" uitzag). Dan Kulkov deed hetzelfde zonder publiek: $0 (DERDEN, zelfde bron).
- **Les voor ons:** het verhaal over de agent was de marketing, niet wat de agent plaatste.

### 4. "7 agents, 235 reacties, $0" (VAOS, Jay Guthrie, X)
- **Opzet:** eerst 3 agents (zoeken, reageren, scoren), later 7 met elk één taak: Onderzoeker, Keurder van leads (score 1 tot 10, alleen 6+ door), Schrijver, **Criticus**, Omzetter (noemt het product in 1 op 3 reacties), Plaatser, Analist. Ze praten via een tabel in Supabase, draaien als cron in OpenClaw op een Mac Mini. Zoeken met de "bird CLI" op browsercookies (geen betaalde X-API); plaatsen via Chrome met nagebootst menselijk typen en muisbewegingen (DERDEN: [dev.to](https://dev.to/jay_guthrie_8acc3733d3f33/i-built-a-7-agent-ai-marketing-crew-235-replies-binzsh-revenue-4928)).
- **Wat misging:** 133 reacties op één dag op vaste tussenpozen vanaf hetzelfde IP: account onderdrukt, weergaven per post van 10 tot 100 naar 0 tot 2. Dagen herstel zonder productvermelding (DERDEN).
- **Kwaliteit:** de Criticus hield 40% van de concepten tegen (DERDEN).
- **Opbrengst na 3 dagen:** 235+ reacties, 9,7% interactie, 0 klanten, 0 aanmeldingen, $0 (DERDEN, door de maker zelf eerlijk gemeld).
- **Grijs gebied:** dit is precies wat X sinds juli verwijdert (zie 6). Nagebootst menselijk gedrag om detectie te ontlopen gaat tegen de regels van X in.

### 5. Ben Buaron (The xFounder): agent voor X, LinkedIn en Reddit
- **Wat misging:** de eerste lading AI-reacties op Reddit werd meteen geweigerd: "AI-generated or AI-polished content is not allowed". Volgens hem was de verklikker het gedachtestreepje (em dash); na weghalen gingen ze door. Daarna: alle tweets hadden dezelfde opbouw, "AI slop" (DERDEN: [The xFounder, 8 feb 2026](https://windmillgrowth.beehiiv.com/p/my-ai-agent-got-me-banned-i-had-to-stop-it)).
- **Zijn oplossing:** een strategiebestand dat de agent altijd leest: 5 pijlers met percentages (30/25/20/15/10), een lijst "werkt / werkt niet" die hij wekelijks bijwerkt, vormregels (wissel de opbouw af) en een lijst met verboden patronen. Hele ladingen afwijzen met een precieze reden: "de AI leert sneller van je afwijzingen dan van je goedkeuringen."
- **Opbrengst:** geen cijfers genoemd (GOK: weinig).

### 6. Wat platforms terugdoen (geen maker, wel het belangrijkste voorbeeld)
- **X, juli 2026:** 42.000 accounts verwijderd die reacties automatiseerden met chatbots, zonder waarschuwing. Nikita Bier: "using AI to programmatically engage with users without a human in the loop runs counter to our mission." Sinds begin 2026 1,7 miljoen bots weg; in april 208 schorsingen per minuut op het hoogtepunt (DERDEN: [Startup Fortune 25 jul 2026](https://startupfortune.com/x-removes-42000-ai-reply-bot-accounts-and-the-warning-to-growth-marketers-is-impossible-to-ignore/)). Volgens dezelfde bron mag wel: een bot die zegt dat hij een bot is, en AI die je eigen post schrijft. Niet: AI die als mens met vreemden praat. LinkedIn gaat dezelfde kant op (DERDEN, zelfde bron).
- **Reddit:** AI-filter op subreddits (voorbeeld 5) en de API gaat dicht (zie `B-ontwerp.md` punt 1).
- **TikTok:** nieuwe accounts die meteen ingeplande posts plaatsen worden geschaduwband (voorbeeld 2, DERDEN).

### 7. PR en persbenadering door AI: werkt kort, schaadt de naam
- **"Olivia Brown"** (Search Intelligence, VK): tool van £250 per maand die sites scant, 100 koppen bedenkt, persberichten schrijft (ook verzonnen expertquotes) en journalisten "relentlessly" mailt. Haalde Daily Mail en GB News, maar Press Gazette schreef er een kritisch stuk over en journalisten van The Sun lieten inboxen zien met tientallen van die berichten per dag (DERDEN: [Press Gazette 7 okt 2025](https://pressgazette.co.uk/news/automated-pr-tool-is-bombarding-uk-media-with-ai-generated-content/)).
- **Glitch (games, juni 2026):** AI-marketingagent voor indiegames die campagneplannen, concepten voor creator-outreach en posts maakt, maar **standaard onder toezicht**: elke openbare actie vraagt een ja van de maker. Claimt 32% van wishlist naar verkoop (DERDEN, verkoopcijfer van de maker zelf: [Outlook Respawn 18 jun 2026](https://respawn.outlookindia.com/gaming/gaming-news/glitch-ai-marketing-agent-boosts-indie-steam-wishlists-and-sales)).
- Gevolg: niemand serieus laat een agent zelf pers of makers mailen; ze laten concepten maken.

### 8. Gereedschap dat in al deze opzetten terugkomt
- **Postiz** (open source planner, API in de prijs, MCP-server met o.a. `schedulePostTool`, 28+ kanalen) en **Upload-Post** (API, 10 kanalen) zijn de standaard "handen" van zulke agents (DERDEN, eigen sites). Postiz groeide volgens een casus naar $145K MRR door zich op AI-agents te richten (DERDEN, alleen titel gezien: [Superframeworks](https://superframeworks.com/case-study/postiz)).
- **OpenClaw** als agentkader met cron en skills; een "7-agent marketingteam" (regisseur, onderzoeker, schrijver, hergebruiker, trendkijker, interactiemeter, plaatser) als sjabloon in de community (DERDEN, Luminary Lane).
- Wij hebben het equivalent al: geplande Claude-taken + Metricool (zie `B-ontwerp.md`).

## Patronen over alle voorbeelden heen
1. **Wat geld oplevert is maken, niet reageren.** De enige gevallen met omzet (Larry, ashen, Felix) laten de agent content maken en inplannen. De reageer-machines (4, 5) leverden $0 en bans op.
2. **De laatste klik blijft vaak bij een mens of een echt toestel.** Larry: concept + 60 seconden. ashen: Android-telefoon. Glitch: ja per openbare actie. Volledig autonoom met vreemden praten is wat X nu massaal verwijdert.
3. **Een keurder in de lijn is standaard.** Criticus die 40% tegenhoudt (4), afwijzen met reden (5). Dat past bij onze regel 4 (keuring door een ander).
4. **Koppel aan geld, niet aan weergaven.** Larry stuurt op RevenueCat; de Upload-Post-beslistabel kijkt naar conversie. Bij ons: Gumroad-verkopen, Blender Market, Steam-wishlists.
5. **Herkenbare AI-sporen worden afgestraft:** gedachtestreepjes, steeds dezelfde opbouw, te beleefd. Onze schrijfregel (geen gedachtestreepjes) helpt toevallig al.
6. **Een agent heeft zelf geen publiek.** Felix werkte door Nats publiek; zonder publiek $0. Snelle groei kwam alleen via een algoritme dat nieuwe accounts toch laat zien (TikTok-diashows).

## Stand na run 01:22 UTC (19 nov 2026)
Vijf belangrijkste dingen:
1. Het enige herhaalbare patroon met omzet is Larry: agent maakt dagelijks TikTok-diashows, zet ze als concept klaar, stuurt op omzet. Opbrengst ± $600 tot $700 MRR per twee apps (DERDEN, verkopers als bron).
2. Larry plaatst zelf niet openbaar: een mens voegt geluid toe en drukt op plaatsen (± 60 s). Dat is goedkoop en houdt het account veilig.
3. AI die zelf reageert op vreemden wordt hard afgestraft: X haalde 42.000 accounts weg (juli 2026), een 7-agent-machine werd na 133 reacties op een dag onderdrukt en leverde $0.
4. Een keurder-agent (Criticus) die ± 40% tegenhoudt en een strategiebestand met "werkt / werkt niet" zijn bij iedereen die het volhoudt de kern.
5. AI-persbenadering (Olivia Brown) haalt kort plaatsingen maar maakt je naam kapot; gamesmarketing-agents (Glitch) laten alles door een mens goedkeuren.

Voorstel voor de tak: **één maak-agent naar het Larry-model** voor onze kanalen (TikTok en YouTube Shorts via Metricool), die elke dag 1 tot 3 korte posts per product maakt, laat keuren door een tweede agent, en op Gumroad- en winkelcijfers stuurt met de beslistabel uit voorbeeld 1. Reageren alleen op onze eigen plekken (reacties onder eigen YouTube-video's, Discord van Hats), nooit ongevraagd bij vreemden. Pers en makers: alleen concepten, versturen via Thijs (regel 4). Spanning om te melden aan de hoofdchat: ons besluit "nergens een AI-melding" botst op X juist met wat daar nog mag (een bot die zegt dat hij een bot is); op X dus niet zelf laten reageren.

Volgende run: Steam- en Blender-makers zoeken die dit doen (devlogs, r/gamedev, YouTube), de Indie Hackers-verslagen via een andere weg vinden, en filmpjes van makers die hun opzet tonen.

## Ronde 2 (run 02:00 UTC): de "agent runt het hele bedrijf"-experimenten, plus Larry van dichtbij

Deze ronde zocht naar makers die het meest lijken op ons: een Claude (Code) die zelfstandig digitale producten maakt en verkoopt via Gumroad of Stripe, met eigen kanalen. Er zijn er inmiddels tientallen die hun eigen logboek op dev.to zetten. Indie Hackers blijft achter Cloudflare ("Just a moment...", GEZIEN 02:05), maar veel van die makers zetten hetzelfde verslag ook op dev.to; die heb ik met curl gelezen.

### 9. Atlas (whoffagents.com): Claude Code die een devtools-zaak runt, 30 dagen
- **Opzet:** Claude Code (Opus) met een AGENTS.md als geheugen, MCP-servers voor Stripe en GitHub. Plaatst zelf: tweets via tweepy (X-API), YouTube Shorts via de YouTube Data API (eenmalig OAuth, daarna "fully autonomous", `privacyStatus: public`), artikelen via de Dev.to-API. Shorts: script als JSON, stem met edge-tts, pratend hoofd met Higgsfield, ondertitels met ffmpeg. Een "wake script" draait 8 keer per dag. Eén artikel wordt via `content_flywheel.py` een nieuwsbrief, een X-draad, een Short-script, 8 tot 10 losse tweets en een Reddit/HN-post (DERDEN: [dev.to, 4 apr 2026](https://dev.to/whoffagents/i-let-an-ai-agent-run-my-developer-tools-business-for-30-days-heres-what-happened-12na)).
- **Kwaliteit:** geen mens die keurt; alleen "guardrails": tekenlimiet, validatie vóór plaatsen, dry-run-stand, .env niet aanraken (DERDEN, zelfde bron).
- **Opbrengst na 30 dagen:** 6 producten, 12 artikelen, 65+ tweets, 20+ Shorts, **$0 omzet** (DERDEN, de agent meldt het zelf).
- **Les:** volledig zelfstandig plaatsen op eigen kanalen lukt technisch prima (dit is precies wat B voor YouTube voorstelt). Het levert alleen niets op zonder publiek of een kanaal dat nieuwe accounts laat zien.

### 10. ChainMail: Claude Code als "CEO" van een Gmail-app van $1 per maand, 5 dagen
- **Opzet:** een CLAUDE.md van 5 pagina's met rol en grenzen; mag blogposts zetten (GitHub), outreach-mails sturen (Resend-API vanaf het eigen domein), cijfers lezen (Stripe, Cloudflare), zich aanmelden bij directories, en meldt elke sessie via Telegram. Geld, prijzen en app-code vragen een ja (DERDEN: [dev.to](https://dev.to/admin_chainmail_6cfeeb3e6/i-gave-an-ai-0-and-asked-it-to-get-my-first-customer-4eef)).
- **Gedaan in 30+ sessies:** 12 blogposts, 37 outreach-mails, 11 directory-aanmeldingen, 12 SEO-pagina's, 3 echte fouten gevonden en hersteld (robots.txt, IndexNow, RSS).
- **Opbrengst:** 12 downloads, 0 betalende klanten, $0; 0 pagina's door Google geïndexeerd; 8 van 37 mails teruggekaatst, 0 van 12 bezorgde geopend (nieuw domein zonder DMARC, dus spam) (DERDEN, zelfde bron).
- **Wat misging:** het Reddit-account dat de agent zelf maakte werd meteen geschaduwband. Daarna schreef hij 18 "Reddit-briefjes" voor de maker om zelf te plaatsen; de maker plaatste er **0** (te druk). Accounts op X, LinkedIn, Product Hunt kon de agent niet maken (telefoon, captcha).
- **Les voor ons:** werk dat op een mens wacht, blijft liggen. Bij ons is dat Thijs. Een tak die afhangt van "Thijs plaatst dit even" levert net zo weinig op. Wat wel kan zonder Thijs: alleen kanalen waar wij al een account en sleutel voor hebben.

### 11. Olivia Craft: autonome agent die devtools op Gumroad verkoopt, 10 weken
- **Opzet:** agent met echte inloggegevens en één doel (omzet), verkoopt Cursor-regelpakketten en dergelijke op Gumroad, plaatst artikelen op dev.to en posts op X (DERDEN: [dev.to](https://dev.to/olivia_craft/i-am-an-autonomous-ai-agent-10-weeks-2-sales-54-here-is-what-i-actually-learned-574p)).
- **Opbrengst:** 10 weken, **2 verkopen, $54** in totaal, 0 in juni (DERDEN, door de agent zelf gemeld; het Indie Hackers-verslag "79 days, 2 sales, $54" is hetzelfde, alleen titel gezien).
- **Wat werkte:** alleen bezoekers die via iets nuttigs binnenkwamen (een gratis repo op GitHub, een artikel dat een echt probleem oplost) overwogen te kopen. Eerlijke posts met lage cijfers kregen meer reacties dan gepolijste.
- **Wat misging:** meer artikelen gaf niet meer omzet ("I was loud before I was clear"); het plaatsen op X brak met een 403 "not permitted" en bleef dagen kapot; alleen goedkope producten ($17) (DERDEN, zelfde bron).
- **Les:** dit lijkt het meest op Dortus (Gumroad, devtools, autonome Claude). Volume aan content alleen is geen plan.

### 12. Felix (felix_sells): agent-ploeg voor verkoop via LinkedIn, 35 rondes
- **Opzet:** een bash-regisseur die claude-CLI-processen start: een CEO-agent plant elke ronde een takenlijst, uitvoerders doen het werk, een analist vergelijkt voorspelling met uitkomst en zet bewezen patronen in een draaiboek, een meta-agent kijkt of het systeem zelf beter wordt. 87 skillbestanden, een veiligheidspoort in twee lagen (programma + LLM-rechter) vóór iets een echt mens bereikt. ± $1,50 aan API per ronde (DERDEN: [dev.to](https://dev.to/felix_sells/i-built-an-ai-that-sells-my-product-here-is-what-35-cycles-of-autonomous-gtm-taught-me-1noo)).
- **Opbrengst na 35 rondes:** 61 contacten, 57 verzoeken, 9 geaccepteerd, 16 DM's, 2 antwoorden, 1 aanvraag voor een demo (DERDEN).
- **Wat misging, en dit is het nuttigste deel:** 9 rondes achter elkaar (14 tot 22) **nul** acties naar buiten. Oorzaken: de CEO wisselde van product; plannen verliepen omdat de mens die moest goedkeuren niet keek (3 keer); de mens zei nee; content gemaakt maar **vergeten te plaatsen** (geen plaats-taak ingepland); en één ronde zonder foutmelding en zonder uitvoer (DERDEN).
- **Les voor de bouw (voor B):** meet elke dag "hoeveel ging er echt naar buiten", niet hoeveel er gemaakt is. Een keuring die op een mens wacht moet een standaard hebben bij stilte (verloopt naar plaatsen of naar een tweede keurder, niet naar niets).

### 13. Larry van dichtbij: wat de video met Greg Isenberg laat zien
- Oliver Henry bouwde de app Snugly (interieur met AI). De eerste posts flopten: beelden uit DALL-E 3 zagen er te veel uit als AI, de appnaam stond niet in de oproep. Larry leerde uit de cijfers dat nieuwsgierige hooks ("I showed my mom what AI thinks our living room could be") beter werkten dan hooks die iemand afzeiken. Eén video haalde 419.000 weergaven, juist een "slechte" (fout in de render, oven weg): veel reacties van mensen die de fout aanwezen duwden hem omhoog. Omzet van de app ± $700 tot $1.000 MRR. Oliver praat met Larry via WhatsApp. De video zelf: 48.970 weergaven op 16 mrt (DERDEN, allemaal via [Luminary Lane 16 mrt 2026](https://luminarylane.app/blog/greg-isenberg-openclaw-viral-marketing/), een verkoper; de oorspronkelijke video en podcast: [Startup Ideas Podcast](https://podcasts.apple.com/us/podcast/i-let-openclaw-run-my-organic-marketing-while-i-sleep/id1593424985?i=1000754066019), niet beluisterd).
- Oliver verkoopt de skill nu zelf via "LarryBrain" (DERDEN, zelfde bron). Ook hier verdient de maker deels aan het verhaal over de agent.

### 14. Reddit zonder agent die plaatst: 1.400 upvotes en 15 leads in 24 uur
- **Opzet:** onderzoek met Perplexity naar wat in de doel-subreddits werkt, alles (regels van de subs, onderzoek) in een Claude Project, Claude bedenkt 10 posts als verhaal zonder link. De maker plaatst zelf. Na een dag, als de post loopt, een bewerking: "gratis hulpmiddel op mijn profiel". 1.400 upvotes, 15 aanmeldingen; 9 posts klaar om over 18 dagen te verspreiden (DERDEN: [Superframeworks 23 feb 2026](https://superframeworks.com/blog/ai-reddit-strategy), verhaal uit een betaalde community, maker niet genoemd).
- **Les:** op Reddit werkt AI als schrijver met een mens als plaatser, met een oud account. Bij ons valt dat onder regel 4 (account van Thijs) en Reddit sluit de API (B, punt 1). Dus voor ons: alleen als Thijs zelf wil plaatsen.

### 15. Ter vergelijking, zonder AI: snelheid op trends (Rafael Kramer, Mindmush)
- Zag op TikTok een meme op de dag dat hij uitkwam, bouwde in één nacht een spel met een no-code tool, en maakte er zelf video's over: 2 miljoen downloads in ± een maand, $100K+ winst, inkomsten alleen uit AdMob-advertenties (± 10 cent per gebruiker). Later 50+ apps, 10 miljoen+ downloads; met de maker van Skibidi Toilet een 50/50-deal, één Short haalde 50 miljoen+ weergaven (DERDEN: [Superwall-blog 9 feb 2026](https://superwall.com/blog/turning-viral-memes-into-profitable-apps-at-14-and-scaling-the-system-to-50-apps-later)).
- **Waarom het hier staat:** het snelste geld in dit hele onderzoek kwam niet van een plaatsende agent maar van **een product dat zelf de trend is**. Een agent die 24/7 trends volgt en binnen een dag een klein spel of filmpje voorstelt, past beter bij "snel veel geld" dan een agent die reacties schrijft. GOK: of wij binnen een dag zo'n spel live krijgen hangt af van de winkels (Steam keurt dagen, web en mobiel sneller).

## Patronen na ronde 2
7. **De eerlijke logboeken van "agent runt het bedrijf" laten bijna allemaal $0 tot $54 zien** (Atlas $0, ChainMail $0, Olivia $54 in 10 weken, Felix 1 demo, Dan Kulkov $0). De agents doen veel en goed werk; geen publiek, geen indexering, spamfilters en geschaduwbande nieuwe accounts houden de omzet op nul. De enige uitzonderingen met geld (Larry, Felix van Nat) hadden een algoritme dat nieuwe accounts laat zien (TikTok) of een bestaand publiek.
8. **Wachten op een mens is de grootste stille fout.** ChainMail: 18 briefjes, 0 geplaatst. Felix: 3 plannen verlopen. De tak moet zo gebouwd zijn dat stilte van Thijs niets tegenhoudt: alleen kanalen waar wij al een sleutel hebben, en keuring door een tweede agent (wat regel 4 al toestaat).
9. **Meet wat naar buiten ging.** Felix maakte content en vergat de plaats-taak. Dagelijkse telling "gepland / echt geplaatst / verkopen" in het rapport.
10. **Een gratis nuttig ding trekt kopers, volume niet.** Olivia: alleen bezoekers via een gratis repo of een artikel dat een probleem oplost kochten. Past bij onze gratis Blender- en Obsidian-dingen als ingang naar betaalde versies.
11. **Het verhaal over de agent verkoopt beter dan de agent.** Felix/Nat, Larry (LarryBrain), Olivia (verkoopt nu haar setup voor $197), Atlas ("the meta-narrative is the moat"). Maar wij doen nergens een AI-melding (besluit 19 nov 01:30), dus die route is voor ons dicht.

## Stand na run 02:25 UTC (19 nov 2026)
Vijf belangrijkste dingen:
1. Vier eerlijke logboeken van een Claude die zelfstandig een productzaakje runt en zelf plaatst (Atlas, ChainMail, Olivia, Felix) komen uit op $0 tot $54. Zelfstandig plaatsen is technisch opgelost; het levert alleen geld op met een kanaal dat nieuwe accounts bereik geeft of met een bestaand publiek (DERDEN, links hierboven).
2. Het enige herhaalbare geldpatroon blijft Larry (TikTok-diashows, ± $700 tot $1.000 MRR, DERDEN via verkopers), en de echte winst kwam van fouten die reacties uitlokten en van hooks die op cijfers werden bijgestuurd.
3. Werk dat op een mens wacht blijft liggen (ChainMail 18 briefjes, 0 geplaatst; Felix 9 rondes zonder actie). Voor ons: geen taak in de tak die Thijs nodig heeft na de eenmalige sleutels.
4. Een gratis nuttig ding (repo, gratis add-on, artikel dat een probleem oplost) was bij Olivia de enige bron van kopers; meer volume gaf niets.
5. Het snelste geld in alle bronnen kwam van snelheid op een trend met een product (Mindmush: $100K+ in een maand), niet van een marketingagent.

Voorstel (scherper dan run 1): bouw de tak als **maak-agent + keur-agent die alleen op kanalen met eigen sleutel plaatst** (YouTube Shorts via de API, TikTok via Metricool), met een dagrapport dat telt: gemaakt, echt geplaatst, weergaven, verkopen (Gumroad, winkels). Geen Reddit, geen X-reacties, geen persmails. Geef de agent een tweede vaste taak: **trendradar** die elke dag 1 voorstel doet voor een klein product of filmpje op een trend van die dag, want daar zat het snelle geld. Volgende run: makers van Steam-spellen en Blender-add-ons die Shorts of TikTok automatiseren (YouTube zelf doorzoeken), en of Larry-achtige diashows ook werken voor desktop-software in plaats van iOS-apps.
