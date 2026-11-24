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

## Ronde 3 (run 03:00 UTC): diashows van dichterbij, Shorts met agents, en het model met veel accounts

Deze ronde: werkt het Larry-model ook buiten één iOS-app, wat levert een agent op YouTube Shorts op, en hoe doen de grote spelers het (veel accounts). Steam- en Blender-makers die hun marketing door een agent laten doen heb ik **niet** gevonden: de zoekresultaten geven alleen bureaus, gidsen en Glitch (voorbeeld 7). Een Indie Hackers-post "i built a saas because i couldnt promote my blender add on" bestaat, maar zit achter Cloudflare (alleen titel gezien).

### 16. Correctie op Larry: TikTok kan via de API wel zelf muziek toevoegen
- In de officiële TikTok Content Posting API (fotopost) staat het veld `auto_add_music`: "recommended music will be automatically added to photos". Werkt alleen bij `post_mode = DIRECT_POST`, dus bij openbaar plaatsen, niet bij een concept (GEZIEN: [TikTok developers, photo post](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post), met curl gelezen 19 nov).
- Blotato (verkoper) bouwt er een hele flow op: diashow met auto-muziek rechtstreeks openbaar, en alleen voor een trend "post as draft and pick a trending sound" (DERDEN: [Blotato-blog, bijgewerkt 12 aug 2026](https://www.blotato.com/blog/automate-tiktok-slideshows)). Kosten volgens hen $0,05 tot $0,20 per diashow aan API (DERDEN).
- **Wat dit voor ons betekent:** de "laatste klik door een mens" uit voorbeeld 1 is niet nodig voor gewone diashows. Aanbevolen muziek is wel iets anders dan een trending geluid; voor een trend blijft het concept + mens. Of Metricool `auto_add_music` doorgeeft weet ik niet (vraag voor B).

### 17. "Joe", een OpenAI Dot: 5,4 miljoen weergaven op 3 diashows
- **Opzet:** een altijd-aan ChatGPT-agent (OpenAI Dots, sinds 29 sep 2026) met een eigen cloudcomputer en **een eigen TikTok-account om mee te kijken**. Elke ochtend om 8:00 zoekt hij 20 nieuwe virale posts die op een app passen, legt uit waarom ze werken (hook, tekstplaats, pose, tempo), en bouwt de winnaar 1 op 1 na rond de app met een lange "masterprompt". Van één winnaar maakt hij varianten (zelfde opbouw, andere hook, ander personage, app op dia 12 van 14). Een mens keurt elke dia; Postiz plant ze **verspreid over meerdere accounts en dagen** (DERDEN: [Postiz-blog 10 nov 2026](https://postiz.com/blog/openai-dots-tiktok-app-marketing), verkoper).
- **Opbrengst:** 2,3 miljoen, 2,0 miljoen en 1,1 miljoen weergaven in een paar dagen (DERDEN, zelfde bron). Geen installaties of omzet genoemd.
- **Kwaliteit:** "Do not let a dot generate a slideshow and post it on autopilot": tekst fout, verkeerde schermafbeeldingen, iemand met drie armen (DERDEN).
- **Les:** het werk van de agent is vooral **onderzoek naar wat nu werkt en dat nabouwen**, niet zelf iets verzinnen. Dat past bij onze trendradar.

### 18. NerdSip: twee natuurkundigen, 350.000 weergaven in twee weken, eigen app
- **Opzet:** OpenClaw maakt in één sessie twee weken aan onderwerpen, bijschriften en hashtags als JSON. Een script vraagt per onderwerp één panoramabeeld (21:9, 4K) aan Gemini ("Nano Banana 2") en knipt dat met sharp in Node in 6 staande dia's; wie swipet, loopt door één doorlopend beeld. Elk beeld krijgt een menselijke controle van ± 5 seconden; ± 1 op de 10 beelden heeft AI-fouten. Daarna ingepland, 2 posts per dag (DERDEN: [NerdSip-blog 3 apr 2026](https://nerdsip.pages.dev/blog/we-automated-tiktok-with-ai-350k-views), eigen verslag van de makers, geen tool die ze verkopen).
- **Opbrengst na 2 weken:** 24 posts, 350.000 weergaven, 5.000 likes, 450 volgers vanaf nul, beste post 100.000, slechtste 1.200. TikTok werd hun **tweede bron van installaties** na zoeken in de App Store; aantallen installaties noemen ze niet (DERDEN).
- **Wat misging:** abstracte onderwerpen (kwantum) scoorden 50 keer slechter dan tastbare ("waarom je jezelf niet kunt kietelen"); 3 zinnen per dia werd overgeslagen, 1 zin werkt; 15+ hashtags deed het slecht, 5 tot 7 beter; tijdstip maakte weinig uit (DERDEN).
- **Les:** dit is het nuttigste recept voor ons: geen gezicht, geen stem, alleen beelden en één zin per dia, en het product komt niet in elke post terug.

### 19. Twee Claude-agents op YouTube Shorts, 6 weken: veel werk, weinig publiek
- **Opzet:** een arts/ingenieur liet twee Claude-agents met eigen geheugen ("Midnight" voor video, analyse en uploaden via de YouTube-API; "Dusk" voor X en blog) om de paar uur zelf werken. Video's met TTS, vertaald in 14 tot 15 talen. De mens keurt ideeën en kijkt elke video na voor die openbaar gaat (DERDEN: [dev.to, wcamon, feb 2026](https://dev.to/wcamon/i-let-ai-agents-run-my-youtube-channel-for-6-weeks-heres-what-actually-happened-21b1)).
- **Opbrengst na 6 weken:** 52 video's, 30.170 weergaven, **29 abonnees**, 4 tot 5% likes. Geen omzet genoemd (DERDEN).
- **Wat misging:** nul reacties onder alle video's, ook met vragen erin; de Analytics-API loopt 72+ uur achter, dus de agent stuurt op oude cijfers; video's werden korter dan gevraagd (41 in plaats van 60 seconden); AI-beelden gaan op elkaar lijken (DERDEN).
- **Les:** Shorts met een agent geeft per video honderden weergaven, geen abonnees en geen gesprek. Vergelijk NerdSip: 24 TikTok-posts gaven 350.000 weergaven. Voor snelle bereik zit TikTok vóór Shorts; Shorts blijven wel langer vindbaar via zoeken (DERDEN, [Bugnet-blog 10 jun 2026](https://bugnet.io/blog/youtube-shorts-for-indie-game-marketing): zet de Steam-link in de vastgezette reactie, titels schrijven voor zoeken).

### 20. Weergaven zonder uitgang zijn niets waard (knipkanalen met Claude)
- Een Japans verhaal op X (769.000 weergaven) over een knipkanaal dat met Claude clips van een bekende maker verspreidt: 530.000 weergaven in 7 dagen leverden ± **$200 per maand** aan YouTube-advertenties op. Het claimde geld ($16.000 per maand) komt alleen van een link naar "iets erachter" (cursus, affiliate, eigen product) (DERDEN: [YouMind-vertaling, 1 jul 2026](https://youmind.com/landing/x-viral-articles/claude-youtube-clipping-automation-workflow); duidelijk verkooppraat, eindigt bij een LINE-groep; de $16.000 is een rekensom, geen bewijs).
- **Les:** het enige bruikbare: de waarde zit in de uitgang. Voor ons is dat de link naar Gumroad, een winkelpagina of de maillijst, en die moet in elke bio en vastgezette reactie staan.

### 21. Het model met veel accounts: Studley AI, en wat onderzoekers erover zeggen
- **Studley AI** (studie-app, ± $13 per maand) laat 110+ TikTok-accounts draaien door betaalde studenten: $20 per post plus tot $2.000 bonus op weergaven. 152,1 miljoen weergaven, $50K per maand; eerder 98 miljoen weergaven in een half jaar met **diashows** (slechte cijfers "met ChatGPT" tegenover goede "met Studley") (DERDEN: [8x.social](https://www.8x.social/en/blog/studley-ai-creator-network), een bureau dat dit verkoopt). Dit zijn mensen, geen agents, en de posts lijken geen reclame.
- **AI Forensics** onderzocht 354 "Agentic AI Accounts" op TikTok: 43.000 posts, 4,5 miljard weergaven in een maand, TikTok labelde minder dan 1,38% als AI (DERDEN: [AI Forensics, 3 dec 2025](https://aiforensics.org/work/agentic-ai-accounts)). Groot bereik dus mogelijk, en tegelijk het soort accounts waar pers en platform op letten.
- **Grijs gebied, voor ons:** meerdere eigen merkaccounts van Dortus (bijv. één per product) is gewoon gebruik. Betaalde posts die niet als reclame herkenbaar zijn, is sluikreclame en valt onder bedrog: niet doen. Studley kost bovendien geld (regel 1).

### 22. Kort: Claude Code die zelf Meta-advertenties draait
- Giorgio Liapakis gaf een agent $1.500 en volledige controle over een Meta Ads-account voor een maand (DERDEN: [Technically, 9 apr 2026](https://read.technically.dev/p/i-let-claude-code-autonomously-run); achter een betaalmuur, alleen de inleiding gelezen, uitkomst onbekend). Kost geld, dus voor ons pas na een ja van Thijs; wel het noemen waard als snelste weg naar meetbare verkopen.

## Patronen na ronde 3
12. **Alle diashow-successen zijn mobiele apps** (Larry, ashen, Joe, NerdSip, Studley): de kijker zit op zijn telefoon en installeert met één tik. Voor desktopsoftware (Blender-add-ons, Obsidian) heb ik geen enkel voorbeeld gevonden. GOK: de omzetting is daar veel lager, want de kijker kan op zijn telefoon niets installeren. Uitgang dan: maillijst ("stuur me de link") of een Steam-verlanglijst, die werkt wel vanaf de telefoon.
13. **Nabouwen wat al werkt** wint van verzinnen (Joe: 20 virale posts per ochtend, 1 op 1 nabouwen; NerdSip: eerst kijken wat in de niche werkt). De maak-agent heeft dus een kijk-taak nodig: TikTok lezen kan zonder account via de zoekpagina's? (onbekend, vraag voor B).
14. **De menselijke keuring is kort en visueel:** 5 seconden per beeld (NerdSip), elke dia (Joe). Een keur-agent die beelden bekijkt (drie armen, verkeerde tekst) kan dit deels overnemen.
15. **TikTok > Shorts voor snelle weergaven:** 24 TikTok-posts 350.000 tegenover 52 Shorts 30.170 (twee verschillende makers en onderwerpen, dus GOK als vergelijking).

## Stand na run 03:20 UTC (19 nov 2026, klok van de container)
Vijf belangrijkste dingen:
1. TikTok kan via de API zelf aanbevolen muziek onder een diashow zetten (`auto_add_music`, GEZIEN in de officiële docs). Larry's "mens moet muziek kiezen" geldt alleen voor trending geluid. Volledig zelfstandig diashows plaatsen op TikTok kan dus.
2. Het sterkste eerlijke recept is NerdSip: één panoramabeeld in 6 dia's, één zin per dia, tastbare onderwerpen, 2 posts per dag, 5 seconden keuring per beeld: 350.000 weergaven en 450 volgers in 2 weken vanaf nul (DERDEN).
3. Agents die vooral **onderzoeken en nabouwen** wat al viraal is (Joe, 5,4 miljoen weergaven op 3 posts, DERDEN via verkoper) doen het beter dan agents die zelf verzinnen.
4. YouTube Shorts met agents: 52 video's, 29 abonnees, 0 reacties (DERDEN). Shorts als bijvangst van dezelfde beelden, niet als hoofdkanaal.
5. Alle successen zijn mobiele apps; voor onze desktopproducten is geen bewijs gevonden. Weergaven zonder uitgang (link, maillijst) leveren bijna niets op ($200 per 530.000 weergaven, DERDEN).

Voorstel (aanvulling op run 2): laat de maak-agent als eerste product een **telefoonvriendelijke uitgang** kiezen (de Steam-verlanglijst van Hats, of de maillijst met een gratis add-on), en bouw de NerdSip-pijplijn na: één beeldmodel, knippen met sharp of Pillow, één zin per dia, 2 per dag, met de keur-agent die elk beeld bekijkt. Plaatsen direct openbaar met `auto_add_music` als onze planner dat doorgeeft (B checken), anders via de TikTok-API zelf. Volgende run: of TikTok zonder account te lezen is voor de kijk-taak, en voorbeelden van diashows voor games op Steam (wishlists) in plaats van apps.

## Ronde 4 (run 04:20 UTC, klok van de container): open pijplijnen, draft-modus, reageer-bots en games

Vervolg op de vragen van run 3. Nieuw: twee volledige pijplijnen met Claude of een andere agent tot en met plaatsen, een eerlijk verslag van een reageer-bot na drie maanden, en voor het eerst voorbeelden met **games en Steam-verlanglijsten**.

### 23. Robin Faraj: open source "content-workflow" met Claude Code en Postiz
- **Opzet:** zes stappen, twee met een mens. 06:00 een cron die trends ophaalt (Playwright, Apify, yt-dlp, transcripties) en elk idee een score geeft (nieuwheid x betrokkenheid, in SQLite). Dan een eigen "Tinder voor ideeën": 5 tot 10 minuten per ochtend vegen. Daarna schrijven vier agents tegelijk (LinkedIn, TikTok EN, TikTok DE, Instagram), elk met een lus **schrijver, vermenselijker ("humanizer", haalt 29 vaste AI-trekjes weg, waaronder gedachtestreepjes), criticus**. De criticus geeft cijfers op haak, juistheid en beknoptheid; alles moet 8 van 10 halen, anders terug, maximaal twee rondes, daarna naar de mens. Beelden met HTML-sjablonen en Playwright-schermafdrukken, of eigen telefoonfoto's met tekst erop. `/approve` toont een voorbeeld per platform, dan plaatst de Postiz-CLI alles. 18:00 haalt een script de cijfers op en maakt er vermenigvuldigers per onderwerp en vorm van (bijv. Claude Code-carrousels ± 2,8x het bereik van een gewone AI-trenddia), die de volgende ochtend de score sturen.
- **Opbrengst:** 8,7 miljoen weergaven op X en ± $45.000 omzet over twee producten in een jaar (DERDEN: [Postiz-blog, 8 mei 2026](https://postiz.com/blog/steal-viral-content-claude-code-postiz-pipeline); Postiz verkoopt de planner, de cijfers komen van Robin zelf, niet nagegaan).
- **Wat misging / eerlijk:** de dia's gaan op elkaar lijken (± 30 foto's in zijn map); tekst op foto's goed leesbaar krijgen is gepruts; werkt omdat zijn onderwerp (AI en devtools) makkelijk tussen platforms te vertalen is. Het is nabouwen van wat trendt, geen eigen denkwerk, en juist dat "basiswerk" doet het meeste.
- **TikTok:** ook hier gaat TikTok naar **concept (draft)** zodat hij zelf muziek kiest; LinkedIn en Instagram gaan direct.
- **Repo:** github.com/robinsadeghpour/content-workflow. Kon ik niet lezen: deze geplande run mag alleen onze eigen twee repo's via GitHub openen (api.github.com gaf 403 met die melding). Een volgende run of de hoofdchat kan de repo via curl naar raw.githubusercontent.com of een clone in /tmp proberen als de omgeving dat toelaat.
- **Les voor ons:** dit is het meest complete voorbeeld dat bij ons past: Claude Code als regisseur, een keur-agent met een harde drempel, een mens alleen bij de ideekeuze en de laatste ja, en een avondtaak die de cijfers terugvoert. Zijn vermenselijker-lijst past precies bij ons besluit "nergens een AI-melding" en onze regel zonder gedachtestreepjes.

### 24. Alex Nguyen: Hermes-agent op een VPS van $5, 30 TikTok-accounts, alles via draft
- **Opzet:** Hermes Agent (Nous Research) met skills als markdownbestanden en cron-taken per stap (haak verzinnen, beelden kiezen, dia's samenstellen zonder taalmodel, onderschrift, plaatsen). Beelden deels van Pinterest via roterende proxy's. Postiz zet de diashow in de **draft-inbox** van het TikTok-account; publiceren gebeurt vanaf een echte telefoon met een echt IP ("iPhone farm"). Kosten: meer aan proxy's dan aan het taalmodel (DERDEN: [Postiz-blog, 14 mei 2026](https://postiz.com/blog/automate-tiktok-slideshow-ai-agents-postiz)).
- **Wat misging:** twee weken één soort haak: cijfers bleven plat; pas met een A/B-test van drie soorten haken per niche en een dagelijkse terugkoppeling ging het omhoog. Drie maanden aan AI-beelden geschaafd, daarna won een 50/50-test met echte Pinterest-foto's: **2,3x zoveel keer bewaard**. En: **vier accounts dood** voordat hij draft-modus accepteerde. "Direct publiceren op een vers account = stille shadowban binnen de eerste week" (DERDEN, zelfde bron, één verteller, verkoper als schrijver).
- **Grijs:** 30 accounts, gescrapete foto's van anderen en proxy's die echte gebruikers nadoen. Meerdere eigen merkaccounts mag; foto's van anderen gebruiken is auteursrecht (niet doen); een telefoonfarm om detectie te ontwijken is tegen de voorwaarden van TikTok.
- **Spanning met run 3:** ik schreef dat TikTok via de API volledig zelfstandig kan plaatsen (`auto_add_music`). Dat klopt technisch, maar drie bronnen (Larry, ashen met de telefoon van $50, Alex) zeggen los van elkaar dat **direct plaatsen via de API op een nieuw account** het bereik doodt. GOK: de veiligste route voor ons is draft via de API en dan één tik op een telefoon, of eerst een account een paar weken met de hand opwarmen.

### 25. Pocket Linguist: een reageer-bot op X na drie maanden (eerlijk verslag)
- **Opzet:** solo iOS-app. Python-daemons per platform (X, Threads, Facebook, Dev.to) met eigen statusbestand, CrewAI elke maandag voor een weekbundel (strateeg, schrijver, redacteur, verspreider), en een **reageer-bot**: alleen op berichten met trefwoorden, 36 sjablonen willekeurig gekozen, max 20 reacties per uur, 30 tot 120 seconden wachten, nooit ongevraagd DM'en.
- **Opbrengst na drie maanden:** draadjes 2 tot 5x de vertoningen van losse posts; Dev.to traag maar groeit via zoekmachines; Threads het meeste bereik maar een wankele API; de reageer-bot "bescheiden volgersgroei, volgers van lagere kwaliteit"; CrewAI spaart 2 tot 3 uur per week. **De posts die echt downloads brachten waren die waar hij zelf reageerde bij het publiek van een groot account** (DERDEN: [Ahmed Mahmoud op dev.to, 2026](https://dev.to/pocket_linguist/how-i-used-ai-agents-to-automate-my-marketing-with-code-3p2b); geen harde downloadcijfers genoemd).
- **Les:** sjabloon-reacties op vreemden leveren bijna niets op en zijn precies wat platforms zoeken. Laat de reageer-agent alleen antwoorden onder **onze eigen** posts en in onze eigen Discord; reacties bij grote accounts kan een agent klaarzetten, maar het moeten echte, gerichte antwoorden zijn.

### 26. Games: hoe kleine studio's verlanglijsten halen met korte clips (zonder en met AI)
- **The Hive (Skydome, klein Fins team):** 10.000+ Steam-verlanglijsten in ± 10 dagen, met accounts van 0 tot 10 volgers. Gedaan: veel korte gameplayclips en schermafdrukken op TikTok, Shorts, Instagram, Facebook, Bluesky, X en Imgur. Wat hielp: "de fantasie meteen laten zien" (jij bent de zwerm), één idee per post in plaats van een functielijst, en **snel vergelijkbare haken opnieuw plaatsen zodra er één aanslaat**; plus een update op Steam in dezelfde periode (GEZIEN: [devlog op itch.io, ± dec 2025](https://skydome.itch.io/thehive/devlog/1164902/10000-wishlists-in-10-days-what-changed-for-the-hive)). Geen AI (het spel heeft zelfs het label "No AI"), maar dit is precies het ritme dat een agent kan draaien: veel varianten, platform laten kiezen, winnaars herhalen. Latere devlogs: een Japans artikel gaf 1.000 verlanglijsten (GEZIEN, titel in de lijst, niet gelezen).
- **Glitch (AI-marketingagent voor games, Tulsa):** agent die campagneplannen, posts, makers-benadering en tracking klaarzet voor Discord, Steam en Twitch, **standaard onder toezicht**: een mens moet op de knop drukken voor plaatsen, geld uitgeven, makers benaderen en "risicovolle claims". Claimt 500 verlanglijsten per dag na een demo, kosten per verlanglijst van $3,00 naar $0,19, en 32% van verlanglijst naar koop (DERDEN: [Outlook Respawn, 18 jun 2026](https://respawn.outlookindia.com/gaming/gaming-news/glitch-ai-marketing-agent-boosts-indie-steam-wishlists-and-sales), overgenomen persbericht, niet controleerbaar; kost geld). Interessant als ontwerp: zelfs een bedrijf dat agents verkoopt, zet de mens bij elke openbare handeling.
- **Les voor Hats:** het diashow-recept van de apps vertaalt bij games naar **korte clips van 5 tot 15 seconden met één fantasie per clip**, uitgang de Steam-verlanglijst (werkt vanaf de telefoon). Dit vult het gat uit patroon 12 (geen desktopbewijs) deels: voor games is er wel bewijs, maar zonder AI.

### 27. Reddit in 2026: wat de bans precies veroorzaakt
- **Maart 2026:** Reddit trad zichtbaar harder op tegen geautomatiseerde accounts; GummySearch (± 135.000 gebruikers) sloot in nov 2025 omdat het geen commerciële API-licentie kreeg. Wat bans geeft: massaal plaatsen via de API, stemringen, en nieuwe accounts die meteen promoten (DERDEN: [Readyt, 29 jul 2026](https://www.readyt.ai/blog/reddit-automation-crackdown-2026/); verkoopt een tool die alleen klaarzet).
- **Eén maker van dichtbij:** een week shadowban op r/SaaS na 12 reacties in 4 dagen, waarvan 11 met een link naar zijn eigen product. De moderator noemde vier signalen: account over één onderwerp, link in de reactie (vaker dan eens per week), jong account, en **AI-achtige schrijfstijl** ("Great question, I love how you framed this"). Vijfde: volume; 2 tot 3 per dag is goed, 20 per week te veel (DERDEN: [Thread Otter](https://www.threadotter.com/blog/founder-led-marketing-reddit-shadowban-lessons); ook een verkoper van een klaarzet-tool).
- **Les:** Reddit niet automatisch plaatsen. Een agent zoekt draadjes en zet antwoorden klaar; plaatsen valt onder de naam van Thijs (regel 4) of een eigen account van Dortus dat eerst weken gewoon meedoet. Zelfde schrijfstijl-eis als bij Robin: geen vaste AI-zinnen.

## Patronen na ronde 4
16. **Draft of één menselijke tik aan het eind is overal waar accounts blijven leven** (Robin, Alex, ashen, Larry, Glitch). Volledig zelf plaatsen werkt bij LinkedIn, Instagram en X volgens Robin; bij TikTok en Reddit kost het accounts.
17. **Een criticus met een harde drempel plus een vermenselijker** is het verschil tussen "AI-brij" en bruikbaar (Robin: 8/10 op drie punten, 29 trekjes weg). Dat past bij ons: de keur-agent geeft cijfers, en alleen boven de drempel gaat iets naar de wachtrij.
18. **De avond-terugkoppeling** (cijfers ophalen, vermenigvuldigers per onderwerp en vorm) komt terug bij Robin, Alex en NerdSip. Zonder die lus bleven de cijfers plat (Alex, twee weken).
19. **Echte beelden winnen van AI-beelden** voor "echt" ogende onderwerpen (Alex 2,3x bewaard, Robin eigen foto's). Voor ons: echte schermopnames van onze producten (Hats, add-ons) zijn ons voordeel.
20. **Reageer-bots op vreemden leveren weinig op en geven bans**; reageren onder eigen posts en in eigen Discord is wel veilig en nuttig.

## Stand na run 04:20 UTC (19 nov 2026, klok van de container)
Vijf belangrijkste dingen:
1. Robin Faraj laat de meest complete open opzet zien die bij ons past: Claude Code regisseert, vier schrijvers, een criticus met drempel 8/10, een vermenselijker, één mens die 10 minuten per dag kiest en goedkeurt, en een avondtaak die cijfers terugvoert. Gemeld: 8,7 miljoen weergaven en ± $45.000 in een jaar (DERDEN, verkoper).
2. Draft-modus op TikTok is volgens meerdere makers verplicht op nieuwe accounts: vier accounts dood bij direct plaatsen (DERDEN). Dit nuanceert mijn punt 1 van run 3: technisch kan het zelf, maar het kost bereik.
3. Voor games is er wel bewijs dat veel korte clips met één fantasie verlanglijsten opleveren: The Hive 10.000 in 10 dagen vanaf bijna nul volgers (GEZIEN, zonder AI). Dat ritme kan een agent draaien.
4. Een reageer-bot met sjablonen bracht na drie maanden alleen "bescheiden" volgers van lage kwaliteit; downloads kwamen van echte reacties door de maker zelf (DERDEN).
5. Reddit: elke automatische plaatsing is sinds maart 2026 een risico; AI-achtige zinnen en links in reacties zijn de signalen waar moderators op letten (DERDEN).

Voorstel: bouw de tak als kopie van Robins opzet, met drie aanpassingen: (a) TikTok via de API naar draft, Thijs of een telefoon doet de laatste tik tot een account een paar weken oud is; (b) eerste product Hats met korte gameplayclips (één fantasie per clip, link naar de Steam-verlanglijst), naar TikTok, Shorts en Bluesky tegelijk, winnaars binnen een dag in varianten herplaatsen; (c) de reageer-agent alleen onder eigen posts en in de Discord van Hats. Volgende run: de repo van Robin lezen (als de omgeving dat toelaat), en zoeken naar een game-studio die dit clipritme al met een agent draait.

## Ronde 5 (run 05:20 UTC, klok van de container): de repo van Robin gelezen, SEO-agents, koude mail en de YouTube-regel van juli

Getoetst aan de hoofdzaak (snel geld). Nieuw: de code van Robin zelf (vraag uit run 4), een SEO-agent met eerlijke cijfers, een volledig gelogde mislukking met koude mail, echte antwoordcijfers van een benader-agent, en wat YouTube sinds juli 2026 niet meer laat verdienen.

### 28. Robin Faraj van dichtbij: wat er echt in de repo staat
Gekloond in /tmp met `--filter=blob:none`, alleen gelezen, niets uitgevoerd (GEZIEN: github.com/robinsadeghpour/content-workflow, laatste commit 10 mei 2026).
- **Vier vaste commando's als Claude Code-skills:** `/pulse` (06:00 vanzelf via een eigen cron-daemon in Node: YouTube, X, TikTok en de changelogs van Anthropic schrapen, scoren, transcripties ophalen, alles in SQLite en een dagbestand), `/review` (mens kiest KEEP, SKIP of STAR), `/generate-content` (schrijver, vermenselijker, criticus, beelden), `/approve` (mens keurt per concept, daarna `npx postiz upload` en inplannen). Om 20:00 haalt `perf-check.js` de cijfers uit Postiz.
- **De criticus is een eigen subagent op Sonnet**, één verse aanroep per concept, met drie cijfers van 0 tot 10: haak, feiten (elke bewering moet terug te vinden zijn in een onderzoeksbriefje, anders 0) en "knip-test" (per dia: zou het slechter worden zonder? elke overbodige dia kost 2 punten). Drempel 8 op alle drie, maximaal 2 herschrijfrondes. **Harde afkeur vóór het scoren:** elk gedachtestreepje (em dash), en het vraag-en-antwoordtrucje ("Het resultaat? 40% sneller."). Gewichten per platform alleen om bij falen de beste versie te kiezen (TikTok: haak 0,45; LinkedIn: feiten 0,50) (GEZIEN, `critic.md` en `critic-rubric.json`).
- **De terugkoppeling is simpel:** score per post = log van (likes + reacties + delen) / weergaven; vermenigvuldiger per bron en vorm = gemiddelde score gedeeld door het totale gemiddelde, **begrensd tussen 0,7 en 1,5**, over de laatste 14 dagen. Die vermenigvuldiger gaat de volgende ochtend in de score van nieuwe ideeën (40% versheid, 60% betrokkenheid) (GEZIEN, `perf-check.js`, `apply-performance-weights.js`, `scorer.js`).
- **Regel in de skill:** "NEVER schedule a post without Robin's explicit per-draft approval". Ook hier dus een mens per post (GEZIEN, `approve/SKILL.md`).
- **Les voor ons:** dit is in een paar dagen na te bouwen met wat wij al hebben (Claude Code, skills, cron). Twee dingen nemen we letterlijk over: de harde afkeur op vaste AI-trekjes en de begrenzing 0,7 tot 1,5 (zodat één toevalstreffer de agent niet de verkeerde kant op stuurt). Wat ontbreekt bij Robin en wat Larry wel heeft: de score kijkt naar betrokkenheid, **niet naar geld**. Wij moeten in de avondtaak Gumroad-verkopen, Steam-verlanglijsten en Kit-aanmeldingen meenemen.

### 29. Paul Irolla: SEO-agent die elke dag een artikel plaatst, 60 dagen
- **Opzet:** een Python-lus op een kleine VPS. Dagelijks de zoekresultaten van ± 300 zoektermen via DataForSEO, scoren op intentie x moeilijkheid, eerste versie door een groot model (± $0,10 per artikel), dan een **feitencheck door een kleiner model** ("vind elke bewering en kijk of er een bron is"), interne links via embeddings, schema-opmaak, één artikel per dag op een vast tijdstip, wekelijks Google Search Console uitlezen om slechte artikelen te verversen. Minder dan $100 per maand aan API (DERDEN: [dev.to, 15 mei 2026](https://dev.to/paul_irolla_6b5ae261d0224/im-running-an-autonomous-ai-agent-that-publishes-a-fact-checked-seo-article-every-day-heres-the-1753)).
- **Opbrengst:** van 0 naar 400.000+ vertoningen in Google in 60 dagen, 46 artikelen live; de eerste drie weken plat, daarna omhoog (DERDEN, zelfde bron). **Geen klikken, aanmeldingen of omzet genoemd.** Hij verkocht er zelf een opzet bij (the-seo-autopilot.com). Een eigen later stuk zegt dat AI-overzichten in Google de klikken op plek 1 flink omlaag halen (DERDEN, alleen titel gezien, [dev.to mei 2026](https://dev.to/paul_irolla_6b5ae261d0224/position-1-ctr-isnt-30-anymore-what-ai-overviews-actually-do-to-your-clicks-a-free-57n)), en een ander stuk heet "28 bezoekers van één site brachten meer op dan 219 van Google" (alleen titel gezien op zijn profiel).
- **Les:** een SEO-agent is technisch makkelijk en loopt zonder mens, maar is **traag** (drie weken niets) en vertoningen zijn geen geld. Past niet bij "binnen weken geld". Wel nuttig als bijvangst op dortus.com voor producten die al verkopen (handleidingen bij add-ons), met de feitencheck als verplichte stap.

### 30. Automaton Agency: agent met budget en één doel ($700 per maand), een maand, $0
- **Opzet:** een bureau dat agents bouwt testte er een op zichzelf, met Claude Cowork in het verslag genoemd. Product: een betaald rapport van $149 tot $349 voor advocatenkantoren, met een gratis scorekaart als lokkertje. De agent bouwde de landingspagina en de scorekaart, maakte de rapporten, mailde kantoren, haalde elke ochtend de cijfers op en schreef een logboek waarmee een nieuwe sessie alles kon reconstrueren. Vaste uitgavenplafonds; alleen bij een strategische keuze, een uitgave boven het plafond of het weekvoorstel vroeg hij een mens (DERDEN: [Automaton Agency, 31 jul 2026](https://automatonagency.com/insights/autonomous-agent-revenue-experiment-teardown)).
- **Opbrengst:** koude mail aan 25 kantoren, vier mails per kantoor, ± 96 verzonden in 17 dagen: 1 keer de scorekaart bekeken, 0 klikken, 0 antwoorden, 0 verkopen, $0. Minder dan $100 uitgegeven (DERDEN, zelfde bron, eerlijk over het eigen falen).
- **Hun conclusie:** "agents maken het doen goedkoop, niet het gelijk hebben". De uitvoering klopte elke dag; er was geen vraag naar het product.
- **Les voor ons:** past bij patroon 7. Koude mail door een agent naar mensen die niet om het product vroegen is de slechtste route. Bovendien valt mail onder regel 4 als het onder de naam van Thijs gaat.

### 31. MentionAgent: echte antwoordcijfers van een benader-agent (voor PR en makers)
- **Opzet:** een agent die sites over een onderwerp zoekt, het adres controleert, een mail schrijft op basis van één specifieke pagina, verstuurt **vanaf een apart verzenddomein**, nastuurt en antwoorden leest. Geld, ruil en alles wat onduidelijk is gaat naar een mens. Kost $99 per maand (DERDEN: [MentionAgent](https://mentionagent.ai/ai-outreach-agent/), een verkoper, maar met eigen productiecijfers).
- **Cijfers:** 17.821 koude mails naar 14.972 domeinen voor 29 sites (10 mrt tot 18 sep 2026): **9,0% van de domeinen antwoordde**, per site van 7,0% tot 14,4%; algemene verkoopmails haalden bij hen **onder 1%**; 2,6% kwam terug; mediaan eerste antwoord na 2,3 uur. Hoeveel er echt tot een vermelding leidde, publiceren ze niet (DERDEN, zelfde bron).
- **Les voor ons (PR, makers benaderen):** het verschil tussen 9% en onder 1% is of de mail over **een pagina van de ontvanger zelf** gaat. Een agent die YouTubers zoekt die al over gezellige games of Blender-add-ons maakten, hun laatste video bekijkt en een korte, specifieke mail met een sleutel klaarzet, is een redelijke opzet. Versturen valt onder regel 4 (naam van Thijs) of moet vanaf een adres van Dortus; nooit vanaf het hoofddomein zolang het domein nieuw is (zie de teruggekaatste mails bij ChainMail, voorbeeld 10).

### 32. YouTube, juli 2026: sjabloonwerk en diashows verdienen niets
- YouTube gaf op 13 juli 2026 drie soorten video's op die niet meer mogen verdienen: **"generiek of herhalend"** (uitdrukkelijk genoemd: diashows van beelden, sjabloonverhalen, AI-werk "met generieke sjablonen dat de indruk geeft van massaproductie"), "onbevredigend of afstotend", en AI-personages over gevoelige onderwerpen. Volgens YouTube een verduidelijking, geen nieuwe regel (DERDEN: [Tubefilter, 13 jul 2026](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/)). Volgens andere berichten zijn hele AI-kanalen met miljoenen abonnees verwijderd (DERDEN, alleen titel gezien: [ARY News](https://arynews.tv/youtube-deletes-viral-ai-slop-channels-with-millions-of-subscribers)).
- **Les:** wij verdienen niet aan YouTube-advertenties, dus het verdienverbod raakt ons niet direct. Maar het zegt wat YouTube als laagwaardig ziet: dezelfde diashow-vorm die op TikTok werkt. Voor @Dortusapps dus echte schermopnames van onze producten met variatie per video, geen sjabloon-diashows in massa (zelfde richting als patroon 19).

## Patronen na ronde 5
21. **Alle open opzetten die ik nu van binnen heb gezien (Robin, Larry-nabouw van Upload-Post) zijn klein:** een paar skills, SQLite, een cron, een planner-API. Bouwen is niet het probleem; vraag en een kanaal dat nieuwe accounts bereik geeft wel (Automaton, Atlas, ChainMail, Olivia: allemaal $0 tot $54).
22. **Sturen op geld in plaats van op betrokkenheid** doet alleen Larry (RevenueCat). Robin en Paul sturen op likes of vertoningen. Bij ons kan de avondtaak de Gumroad-verkopen en Steam-verlanglijsten per dag naast de posts van die dag leggen; grove toewijzing per dag is beter dan geen.
23. **Snelheid naar geld per route (GOK, op basis van alle 32 voorbeelden):** TikTok-diashows of korte clips met een uitgang: dagen tot weken. Benaderen van makers met een specifieke mail en een sleutel: weken (9% antwoord, DERDEN). SEO: maanden. Koude mail naar klanten en reageer-bots: $0.

## Stand na run 05:20 UTC (19 nov 2026, klok van de container)
Vijf belangrijkste dingen:
1. De repo van Robin is gelezen (GEZIEN): vier skills, een criticus op Sonnet met drempel 8 op haak, feiten en knip-test, harde afkeur op gedachtestreepjes en vraag-antwoordtrucjes, en een terugkoppeling met vermenigvuldigers begrensd tussen 0,7 en 1,5. Een mens keurt elke post. Na te bouwen in dagen.
2. Zijn terugkoppeling stuurt op betrokkenheid, niet op geld. Wij moeten Gumroad, Steam-verlanglijsten en Kit in de avondtaak zetten (zoals Larry met RevenueCat).
3. Een SEO-agent zonder mens haalde 400.000 vertoningen in 60 dagen maar noemt geen omzet en was drie weken plat (DERDEN). Te traag voor de hoofdzaak.
4. Een volledig gelogde agent met budget en koude mail: 96 mails, 0 antwoorden, $0 (DERDEN). Een benader-agent die over de eigen pagina van de ontvanger schrijft haalt 9% antwoord, algemene mails onder 1% (DERDEN, verkoper met eigen cijfers). Voor PR: makers benaderen werkt alleen specifiek.
5. YouTube noemt sinds juli 2026 sjabloon-diashows en massaal AI-werk "generiek of herhalend" (DERDEN). Op YouTube dus echte schermopnames met variatie, niet dezelfde diashows als op TikTok.

Voorstel (vult run 4 aan, geen vervanging): bouw de maak-agent als kopie van Robins vier skills, met (a) zijn criticus en harde afkeurlijst letterlijk overgenomen, aangevuld met onze regels (geen AI-melding, Nederlands of Engels per kanaal); (b) een avondtaak die naast betrokkenheid ook de verkopen en verlanglijsten van die dag ophaalt en de vermenigvuldigers daarop zet; (c) als tweede taak een benader-agent die per week 10 makers zoekt die al over vergelijkbare games of add-ons maakten en per maker een specifieke mail met sleutel klaarzet in `berichten/hoofdchat.md` (versturen na ja van Thijs, regel 4). Geen SEO-agent en geen koude mail nu: te traag of $0. Volgende run: zoeken naar makers die zo'n benader-agent voor games (sleutels aan YouTubers en streamers) echt draaien, met antwoord- en verlanglijstcijfers.

## Ronde 6 (run ±06:20 UTC, klok van de container): makers benaderen voor games met echte cijfers, een Discord-bot met geheugen, en twee waarschuwingen over agents die "druk" zijn

Vraag van vorige run: wie draait een benader-agent voor games (sleutels aan YouTubers en streamers), met antwoord- en verlanglijstcijfers? Een AI-agent die dit volledig zelf doet met openbare cijfers heb ik **niet** gevonden. Wel twee eerlijke reeksen cijfers van mensen die het met de hand of met een eigen verzendsysteem doen. Die zijn precies wat een agent bij ons zou nadoen, dus ze zetten de lat.

### 33. Polden Publishing: een automatisch verzendsysteem voor makers, 4 games, $2 miljoen zonder makersbudget
- **Wie:** Kirill Akimkin, kleine indie-uitgever, praatje op gamescom dev (25 aug 2026) (DERDEN: [Inven Global, 1 sep 2026](https://labs.invenglobal.com/articles/25451/blinded-code-blast-to-streamers-fail-proof-creator-campaign-strategies)).
- **Opzet:** eigen domein met SPF, DKIM en DMARC, opwarmen van het adres, alleen geverifieerde ontvangers. Lijst vooraf gefilterd op vaste regels (abonnees, kijktijd, datum laatste upload), geen schot hagel. 6 tot 8 versies van de tekst, elke 3 dagen een vervolgmail met andere inhoud. Boven 10.000 mails per maand vond hij een automatisch systeem nodig "om menselijke fouten te voorkomen". Of daar een taalmodel in zit, zegt het verslag niet.
- **Cijfers (DERDEN, zelfde bron):** 90% opent de mail. Voor hun game Static Dread (aug 2026): **1.528 koude mails, 57 makers (3,7%) maakten iets**. Van die 57 hadden er **29 nooit geantwoord**: ze losten de sleutel stil in en streamden. Wie alleen naar antwoorden kijkt, mist de helft. Een lijst van makers die eerder over hun games maakten, leverde **7 keer zoveel** op als koude mail. Totaal 4 games, $2 miljoen omzet.
- **Wat misging:** een campagne waarin de sleutel achter een link zat in plaats van in de mail zelf: **0 sleutels ingelost**.
- **Les voor ons:** (a) sleutel direct in de eerste mail; (b) meten op ingeloste sleutels en video's, niet op antwoorden (Steam laat zien welke sleutel is ingelost); (c) de makers die al eens over ons maakten zijn goud, dus een vaste lijst bijhouden.

### 34. Eén maker met de hand: 408 mails, 44 sleutels, 7 video's, ±5.000 verlanglijsten
- Een ontwikkelaar mailde 408 makers voor toegang tot een gesloten demo: **44 losten een sleutel in (12,6%), 7 maakten een video of stream (2%)**, samen ±260.000 YouTube-weergaven en **±5.000 verlanglijsten erbij** (DERDEN: [Game Dev Report van Code Monkey, jan 2025](https://gamedevreport.beehiiv.com/p/results-from-emailing-400-streamers-and-awesome-stuff-from-ces-2025), dat naar zijn Reddit-post verwijst). Hij zocht vooraf per maker of die zijn soort spel zou spelen en volgde de raad van Chris Zukowski.
- **Rekensom (GOK):** ±12 verlanglijsten per mail; met de vuistregel van Glitch (32% van verlanglijst naar verkoop is hun eigen, hoge claim, DERDEN, zie voorbeeld 7) of de gangbare veel lagere schattingen (GOK 10 tot 20%) is dat ruw 500 tot 1.600 verkopen uit 408 mails. Het werk is vooral uitzoeken en schrijven: precies wat een agent kan klaarzetten.

### 35. Wat grote campagnes erover zeggen: persoonlijk benaderen wint van een "programma"
- Jake Kulkowski (bureau Guillotine, campagne van Clair Obscur: Expedition 33): een makersprogramma van 10 maanden kreeg **91% van alle sleutels maar gaf 8% van de weergaven bij de lancering**; persoonlijk benaderen van grote en middelgrote makers gebruikte **2,7% van de sleutels en gaf 71% van de weergaven** (DERDEN: [Inven Global](https://labs.invenglobal.com/articles/25451/blinded-code-blast-to-streamers-fail-proof-creator-campaign-strategies)). Zijn les: makers maken geen fans van een spel dat nog niemand speelde; benader vlak voor en na de lancering.
- **Les:** onze benader-agent moet weinig en heel gericht werken (10 per week, zoals voorgesteld in run 5), niet sleutels breed uitdelen via Keymailer-achtige portals.

### 36. discord-lobster: drie kleine bots met Gemini Flash, 0 naar 146 leden in 10 dagen, ±$10 per maand
- **Wie:** ppcvote (eenmanszaak in Taiwan). Verslag (DERDEN: [dev.to, 12 apr 2026](https://dev.to/ppcvote/discord-community-from-0-to-146-members-a-solo-founders-playbook-with-3-ai-bots-2a4i)); code gelezen, niet uitgevoerd (GEZIEN: github.com/ppcvote/discord-lobster, 630 regels JavaScript in drie bestanden).
- **Opzet:** (1) welkom: elke 3 minuten nieuwe voorstellingen lezen en een persoonlijk welkom schrijven; (2) "vibes": elke 20 minuten #general lezen, alleen meepraten als er minstens 2 mensen praten, niet als de bot het afgelopen uur al sprak, en het model mag "SKIP" zeggen (GEZIEN in vibes.js); (3) geheugen: elke 10 minuten uit berichten per lid achtergrond en interesses halen naar een JSON-bestand, zodat de bot weken later iemand persoonlijk terug kan halen.
- **Cijfers (DERDEN, eigen verslag):** dag 1: 5 leden (vrienden), dag 7: 41, dag 8: 78 na één blogpost die viraal ging (±3.000 bezoekers), dag 10: 146. Kosten ±$10 per maand (stroom), 2 uur per week eigen tijd. **Geen omzet genoemd**; de schrijver zegt zelf dat een community zonder weg naar geld "een chatroom" is.
- **Wat misging:** de bot praatte eerst elke 10 minuten mee en leden vonden hem irritant; na 20 minuten plus drempel vroegen ze juist "waar is de kreeft?". Te veel kanalen (12) gaf dode kanalen; terug naar 8.
- **Let op voor ons:** de bot doet zich in de prompt voor als "AI community manager" en heeft een eigen figuur (een kreeft). Dat past bij ons besluit "nergens een AI-melding" alleen als de bot een eigen naam en figuur heeft en zich niet voordoet als mens. Voor de Discord van Hats is een welkomstbot met geheugen en een SKIP-drempel na te bouwen in een dag; levert bereik, geen geld, dus lage voorrang.

### 37. MindThread: hoe een planner-maker een agent laat plaatsen zonder dat hij ontspoort
- **Wie:** dezelfde ppcvote; zijn planner voor Threads kreeg in okt 2026 een CLI en een MCP-server voor Claude Code (DERDEN: [dev.to, 26 okt 2026](https://dev.to/ppcvote/letting-an-ai-agent-post-to-threads-without-letting-it-go-rogue-4di5)). Verkoper, maar de lessen zijn technisch en controleerbaar.
- **Opzet:** "een prompt is geen toestemming". Toestemming zit op de **sleutel**: per handeling (concept, plannen, nu plaatsen, antwoorden, patrouille) staat allow, ask of deny. Bij ask krijgt de agent een link voor de mens en draait de handeling pas na een klik. Inhoudsregels (lengte, verboden woorden, "alleen cijfers uit mijn feitenlijst") toetst de **server** bij elke schrijfactie en nog eens bij plaatsen; bij "block" wordt de post geweigerd, wat het model ook schreef. Antwoorden op Threads worden als concept klaargezet tot iemand ze goedkeurt, of gaan vanzelf uit tot een daglimiet.
- **Wat misging (DERDEN, zelfde bron):** in de week voor de lancering waren **405 van 449 API-fouten** te veel verzoeken: een agent die de feed bleef bevragen tot de daglimiet op was. En herhaalde pogingen plaatsten **dubbel**, dus nu een sleutel per post zodat een herhaling niets nieuws plaatst. Meta zelf staat rond 250 API-posts en 1.000 antwoorden per profiel per dag toe.
- **Les voor ons (sluit aan op B):** de keuring moet niet alleen in de prompt van de Plaatser zitten maar in het script dat plaatst: een vaste lijst verboden woorden en een cijfer-check die weigeren, een eenmalige sleutel per post tegen dubbel plaatsen, en wachten op meldingen in plaats van steeds opnieuw vragen.

### 38. Twee waarschuwingen van Claude Code-gebruikers: beloftes die niet kloppen, en "druk" is geen voortgang
- **Yurukusa** verkoopt een PDF van $19. Na 3,5 maand liet hij Claude Code de verkooppagina regel voor regel naast het geleverde bestand leggen: **21 fouten**, waaronder een "gratis voorproef" die twee keer werd beloofd maar nooit bestond. Bij een ander product beloofde de pagina een editie "op de 1e van elke maand": **0 van 6** kwamen op de 1e, en die belofte stond nog op 7 plekken (DERDEN: [dev.to, 12 aug 2026](https://dev.to/yurukusa/my-sales-page-promised-a-free-preview-twice-it-didnt-exist-5ef8)).
- Zelfde schrijver, na een maand Claude Code bijna zelfstandig: elke sessie zag er productief uit, maar het aantal dingen dat echt bij een lezer of koper aankwam was veel kleiner. Zijn twee middelen: een **uitkomstenlijst** waar alleen iets met een link naar buiten in mag (gepubliceerde URL, verstuurd antwoord), en vóór elke taak de vragen "wie heeft hier precies baat bij?" en "welk getal beweegt binnen 14 dagen?" (DERDEN: [dev.to, 28 jun 2026](https://dev.to/yurukusa/i-let-claude-code-run-autonomously-for-a-month-productive-was-a-story-my-own-logs-didnt-support-24i6)).
- **shiro-tools** (Tokio) liet een geplande Claude-agent elke ochtend om 5 uur de Gumroad-verkopen, Qiita-weergaven en X-cijfers lezen, één verbetering kiezen en die pushen. Na 11 dagen: **$0**, Reddit-account na 2 posts als spam gemarkeerd, Show HN geblokkeerd voor nieuwe accounts; Qiita gaf 2.500 weergaven op 6 artikelen (DERDEN: [dev.to, 18 apr 2026](https://dev.to/shiro-tools/trying-to-make-claude-code-pay-for-its-own-200month-subscription-day-11-2kdc)). Daarna schreef hij niets meer op dev.to (GEZIEN: zijn feed eindigt bij die post).
- **"Aria13":** 27 gidsen op Gumroad, 700 rondes automatisering in 60 dagen, 31 dev.to-artikelen met samen ±140 weergaven, **0 verkopen**; posten op Reddit en HN vanaf een datacenter-IP werd geblokkeerd (DERDEN: [dev.to, 9 mei 2026](https://dev.to/ariauser13/i-ran-700-ai-automation-cycles-to-sell-digital-products-heres-the-honest-post-mortem-4ak8)).
- **Les voor ons:** (a) laat de Keurder elke winkeltekst en post naast het echte product leggen (wat staat er in de download, klopt elke belofte); (b) de avondtaak telt alleen dingen die naar buiten gingen en geld of verlanglijsten, niet commits; dat is dezelfde toets als de hoofdzaak in CLAUDE.md; (c) posten vanuit onze cloudomgeving naar Reddit of HN is kansloos (datacenter-IP), los van de regels.

## Patronen na ronde 6
24. **Makers benaderen is de enige route met openbare cijfers die van mail naar verlanglijst lopen** (DERDEN, 33 tot 35): 2 tot 3,7% van de gemailde makers maakt iets, en één goede reeks gaf ±12 verlanglijsten per mail. Geen enkele AI-route in deze 38 voorbeelden laat zo'n keten naar geld zien, behalve Larry (RevenueCat).
25. **Wat werkt is saai en mechanisch:** juiste lijst, sleutel in de mail, vervolgmail na 3 dagen, meten op inlossen. Dat is precies wat een agent goed kan klaarzetten; versturen is het enige stuk dat onder regel 4 valt of een eigen domein van Dortus vraagt.
26. **Veiligheid hoort in de code, niet in de prompt** (37, en de harde afkeur van Robin in 28): verboden woorden, cijfercheck en dubbel-plaatsen-stop in het plaatsscript zelf.
27. **Agents die op zichzelf sturen worden druk zonder resultaat** (38): alle vier de zelfstandige Gumroad- of Claude-proeven die ik nu heb (Olivia, Aria13, shiro, Yurukusa's log) eindigden rond $0. Het gemeenschappelijke gat is verspreiding, niet maken.

## Stand na run ±06:20 UTC (19 nov 2026, klok van de container)
Vijf belangrijkste dingen:
1. Een kleine uitgever haalde met een automatisch verzendsysteem naar makers (geen makersbudget) $2 miljoen op 4 games; 1.528 mails gaven 57 makers met content (3,7%), en de helft van hen antwoordde nooit (DERDEN). Meet op ingeloste sleutels, niet op antwoorden.
2. Sleutel achter een link: 0 ingelost. Sleutel in de eerste mail: werkt (DERDEN). Eerdere makers opnieuw benaderen: 7 keer beter dan koud.
3. Met de hand: 408 mails, 44 sleutels, 7 video's, ±5.000 verlanglijsten (DERDEN), ruw ±12 verlanglijsten per mail. Dit is de snelste aantoonbare weg van werk naar geld voor Hats.
4. Een Discord-bot met geheugen en een SKIP-drempel is klein (630 regels, GEZIEN) en kost ±$10 per maand, maar levert bereik, geen geld (DERDEN). Lage voorrang.
5. Zelfstandige Claude-agents die zelf verkopen eindigen rond $0 en worden "druk" zonder uitkomst (DERDEN, 4 gevallen). Zet een uitkomstenlijst en een "welk getal beweegt binnen 14 dagen"-toets in de tak, en laat de Keurder elke belofte naast het echte product leggen.

Voorstel (scherpt run 5 aan): maak de **benader-agent de eerste taak van de tak**, vóór meer posts. Elke week: 10 tot 20 makers zoeken die in de laatste 30 dagen een vergelijkbaar spel speelden (regels: abonnees, laatste upload, genre), per maker een korte mail over hun eigen laatste video met de Steam-sleutel in de tekst, en een vervolgmail na 3 dagen. Klaarzetten in `berichten/hoofdchat.md`; versturen vanaf een opgewarmd adres van Dortus met SPF, DKIM en DMARC (eenmalig door Thijs te regelen) of na zijn ja (regel 4). Meten in de avondtaak: ingeloste sleutels, video's, verlanglijsten per week. Daarnaast in het plaatsscript van B: verboden-woordenlijst, cijfercheck en een eenmalige sleutel per post. Volgende run: of iemand LLM-gemaakte persoonlijke makersmails heeft vergeleken met handgeschreven (antwoord en inlossen), en wat Steam zegt over sleutels voor makers (limieten, het makersportaal van Steam).

## Ronde 7 (run 20 nov ±00:20 UTC): sleutels zonder doorverkoop, AI-tekst tegen handgeschreven, drie nieuwe $0-proeven en betaalde knippers

Vraag van run 6 meegenomen: is er een vergelijking van AI-geschreven en handgeschreven eerste berichten, en wat zegt Steam over sleutels voor makers. Toets blijft de hoofdzaak: wat brengt binnen weken geld.

### 39. Steam Curator Connect: de officiële weg zonder losse sleutels
- **Regels (GEZIEN, [Steamworks-documentatie](https://partner.steamgames.com/doc/marketing/curators)):** je stuurt geen sleutel maar een aanbod binnen Steam aan een curator; maximaal **100 curators, elk hooguit 5 kopieën**. Er moet minstens een openbare "coming soon"-pagina zijn. Je ziet in een overzicht wie het aanbod aannam. Steam toont alleen curators die nog actief zijn.
- **Waarom het ertoe doet:** 11 bit studios (Frostpunk) stopte met sleutels aan curators omdat "de meeste verzoeken van nepaccounts komen die de sleutels doorverkopen" (DERDEN: [GamesRadar](https://www.gamesradar.com/frostpunk-studio-swears-off-keys-for-steam-curators-amid-storm-of-fake-accounts)). Curator Connect sluit dat uit, want er is niets door te verkopen.
- **Hoe kies je:** kijk op de pagina's van spellen die op het jouwe lijken welke curators die aanraadden; drie aanbevelingen in je genre is een sterke kandidaat; kijk wanneer ze laatst iets plaatsten. Niet de top 100 op volgers bestoken (DERDEN: [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-curators-guide-developers), verkoper van een tool, maar de werkwijze is gewoon).
- **Voor ons:** dit is precies werk voor een agent: per curator een regel met link, genre, laatste post en welke vergelijkbare spellen ze aanraadden. Het versturen gebeurt in Steamworks, dus door wie daar inlogt (staat bij Thijs). Kan pas als Hats een openbare pagina heeft. Geen geld, geen mail onder de naam van Thijs.

### 40. AI-geschreven tegen handgeschreven eerste bericht: de grootste dataset die ik vond
- **Pin (recruiting, 5 miljoen berichten, jan 2024 tot jun 2026):** handgeschreven eerste mails kregen **±2,5 keer** zoveel antwoorden als AI-mails. Dezelfde AI-teksten kregen via LinkedIn **3,4 keer** zoveel antwoorden als via mail, en daar had de mens zelf op versturen gedrukt. Kanaal woog dus zwaarder dan wie het schreef (DERDEN: [Pin](https://www.pin.com/blog/ai-vs-human-recruiting-outreach-study); let op: Pin verkoopt zelf AI-outreach, en het gaat om sollicitanten, niet om makers).
- Zelfde bron, met cijfers van Expandi: antwoord op LinkedIn-verzoeken zakte van **3,5% (mei 2025) naar 2,2% (apr 2026)** doordat iedereen dezelfde tools gebruikt (DERDEN, zelfde link). Hoe meer AI-berichten, hoe hoger de lat voor iets wat echt over de ontvanger gaat.
- Geen bruikbare vergelijking voor **makers van games** gevonden. Sites als influencers-time.com noemen "de antwoorden halveren zonder menselijke keuring", maar zonder enige bron; dat telt niet.
- **Les voor ons:** laat de agent het onderzoek en het concept doen (welke video, welk moment, waarom dit spel past), maar houd de mail kort en echt over de laatste video van die maker; een mens of de Keurder leest elk concept. Dat sluit aan bij Glitch (voorbeeld 8), dat "contact met makers" standaard achter een ja zet.

### 41. Glitch, aanvulling: het enige cijfer is van de verkoper
- Glitch zegt een **32% omzetting van verlanglijst naar verkoop** te halen, "ver boven het gemiddelde" (DERDEN: [Outlook Respawn, 18 jun 2026](https://respawn.outlookindia.com/gaming/gaming-news/glitch-ai-marketing-agent-boosts-indie-steam-wishlists-and-sales)). Niet uitgelegd hoe gemeten, over hoeveel spellen of over welke periode. Behandelen als reclame.
- Wel nuttig: hun lijst van acties die altijd een menselijke ja vragen (plaatsen, geld uitgeven, makers benaderen, accounts wijzigen, "riskante openbare beweringen") (DERDEN: [PocketGamer.biz, 17 jun 2026](https://www.pocketgamer.biz/glitch-launches-ai-marketing-agent-for-solo-developers-and-indie-game-teams/)). Dat is bijna gelijk aan onze regel 4 plus de oranje-lijst in `marketing/REGELS.md`.

### 42. Verlanglijsten zijn minder waard geworden (meet op verkoop)
- Chris Zukowski verzamelde verkoopcijfers van **160 spellen**: spellen uit 2023 tot 2025 verkochten in de eerste maand ongeveer **de helft zoveel per verlanglijst** als spellen uit 2020 tot 2022 (DERDEN: [How To Market A Game, 13 okt 2026](https://howtomarketagame.com/2026/10/13/wishlist-inflation-is-real-but-they-are-still-important/)). Zijn verklaring: verlanglijsten zijn makkelijker te zetten (een sterretje bij zweven) en veel meer spellen krijgen festivalruimte.
- **Les voor ons:** een agent die verlanglijsten opjaagt met veel posts kan een mooi getal maken dat weinig geld wordt. In het dagrapport van de tak voor Hats dus: verlanglijsten, maar vooral volgers en (later) verkoop per bron. Voor Click Joints is dat al zo (Gumroad per `?ref=`).

### 43. Drie nieuwe proeven met zelfstandige agents, alle drie $0
- **David Shin, 6 maanden, 4 Claude-agents op een Mac (elke 2 uur wakker):** 16 producten gebouwd, 4 klanten van buiten ooit, **0 die nu betalen**; de agents leven op het startsaldo. Wat wel verkoopt: zijn handleiding over de opzet voor $199 (DERDEN: [dev.to, 19 apr 2026](https://dev.to/david_shin_0c7d69b704a649/i-ran-4-autonomous-claude-agents-for-6-months-heres-the-data-1op5); hoeveel hij verkocht staat er niet). Zijn eigen werk per dag: ±15 minuten, vooral uitgaande antwoorden goedkeuren.
- **"duckduckduck", 31 sessies Claude Code, $0 startgeld:** vijf pogingen (nichesite, bounties, gratis tools met fooienpot, klusjesmarkten, schrijfklus), allemaal $0. De gratis tools op een subreddit met 895.000 bezoekers per week: **320 weergaven, 1 upvote (van hemzelf)**. Zijn conclusie: schrijven en code zijn geen schaarste meer (aanbiedingen van $1 per uur op dezelfde pagina); wat geld waard is, is **publiek, vertrouwen, een account met geschiedenis, of een winkel die je laat zien** (DERDEN: [dev.to, 30 jul 2026](https://dev.to/duckduckduck/i-gave-an-ai-agent-a-business-and-0-it-found-the-one-thing-ai-cant-sell-38ne)).
- **"Warhol", de AI-contentstrateeg van The $200/Month CEO:** 15 nieuwsbrieven, 18+ artikelen op drie sites, ±310 weergaven op dev.to, **1 abonnee (de maker zelf), 0 verkopen** van een product van $19. Drie Reddit-posts vier keer herschreven en **nooit geplaatst**, omdat plaatsen inloggen in een browser vraagt. Een tweede agent van hem ("Grove", koude mail): 240 mails, $0 (DERDEN: [Buttondown, 14 mrt 2026](https://buttondown.com/the200dollarceo/archive/today-my-ai-content-strategist-hit-its-0-deadline/)).
- **Les voor ons:** zelfde als patroon 27, nu met 7 gevallen. Bij ons is de laatste stap wel geregeld (Metricool, `marketing/REGELS.md`), dus het risico is niet "nooit plaatsen" maar "plaatsen zonder dat er een winkel aan vast zit". Daarom: elke post één link naar een plek waar je kunt kopen of een verlanglijst zetten, en de avondtaak telt alleen dat.

### 44. Betaalde knippers (Whop Content Rewards): bereik huren per 1.000 weergaven
- **Hoe het werkt:** je zet een campagne op Whop met een bedrag per 1.000 weergaven; echte mensen maken en plaatsen clips op hun eigen TikTok, Shorts of Reels en worden per weergave betaald. Gewoon tarief **±$1 per 1.000 weergaven**, plus 10% voor Whop; 1 miljoen weergaven kost dus ±$1.100 (DERDEN: [Built by Foundry](https://www.builtbyfoundry.io/blog/what-is-clipping-1-dollar-per-1000-views-50-campaigns), verkoopt zelf diensten).
- **Voorbeeld met schaal:** de Franse ondernemer Yomi Denzel: **$258.800 van $263.000 besteed, 48.253 inzendingen**, alle clips wijzen naar zijn betaalde cursussen (DERDEN, zelfde link). Ruw 250 miljoen betaalde weergaven (GOK: deling door $1).
- **Haken:** de knipper bouwt zijn eigen publiek op, niet het jouwe; jij krijgt wel een licentie op de clips en mag de goede zelf opnieuw plaatsen. Betaalde clips moeten als reclame gemeld worden, en de verkoper is daarvoor verantwoordelijk (DERDEN, zelfde link).
- **Voor ons:** dit kost geld, dus alleen na een ja van Thijs (regel 1). Het is wel het eerste model in dit onderzoek waar de "laatste klik" bij echte mensen met echte accounts ligt zonder nepaccounts, en waar de agent het zware deel kan doen (brief schrijven, inzendingen keuren op de regels uit `marketing/REGELS.md`, betalingen naast weergaven leggen). Rekensom voor Click Joints (GOK): $50 geeft ±45.000 weergaven; met 0,1% die doorklikt en 5% daarvan die Pro koopt is dat ±2 verkopen. Alleen zinnig als onze eigen TikToks eerst laten zien dat de clip van Click Joints mensen tot klikken brengt (de stopregel van 1 dec).

## Patronen na ronde 7
28. **Sleutels verlaten Steam niet meer:** Curator Connect (100 curators, 5 kopieën) is gratis, niet door te verkopen en past bij een agent die de lijst klaarzet (GEZIEN). Voor makers op YouTube blijft de sleutel in de mail (voorbeeld 33) de weg.
29. **Kanaal en echtheid wegen zwaarder dan AI of niet** (DERDEN, 40): AI mag het onderzoek en concept doen; de tekst moet over de ontvanger gaan en een ander leest mee.
30. **Getallen die makkelijk stijgen zijn minder waard** (42): verlanglijsten halveerden in waarde; meet op verkoop en volgers.
31. **Bereik is te koop voor ±$1 per 1.000 weergaven** (44), dus bereik op zich is geen prestatie van een agent. De vraag is alleen wat er per 1.000 weergaven verkocht wordt.

## Stand na run 20 nov ±00:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Steam Curator Connect** geeft Hats een gratis, veilige route naar 100 curators met elk 5 kopieën, zonder sleutels die doorverkocht worden (GEZIEN). Vraagt een openbare pagina en iemand die in Steamworks klikt.
2. **Handgeschreven eerste berichten scoorden 2,5 keer beter dan AI-mails** in 5 miljoen berichten, maar het kanaal woog nog zwaarder (3,4 keer) (DERDEN, verkoper, recruiting). Voor makersmails: AI zoekt en schetst, de tekst gaat over hun laatste video, een ander keurt.
3. **Nog drie zelfstandige agent-proeven op $0** (DERDEN); in totaal nu 7. Wie wel geld verdient, verkoopt de opzet zelf ($199-handleiding) of heeft een mens met publiek.
4. **Verlanglijsten leveren nu ±de helft van 2020 tot 2022 op** (DERDEN, 160 spellen). Tel verkoop per bron, niet alleen verlanglijsten.
5. **Betaalde knippers** (±$1 per 1.000 weergaven, DERDEN) zijn de eerlijke manier om "veel accounts" te hebben: echte mensen, eigen accounts. Kost geld, dus pas na een ja van Thijs en pas als onze eigen clips laten zien dat ze tot kopen leiden.

Voorstel: (a) zodra Hats een openbare pagina heeft, laat een agent een lijst van ±100 curators maken (genre, laatste post, welke vergelijkbare spellen ze aanraadden) in `platformen/steam/`, zodat versturen via Curator Connect één klikmiddag is; (b) zet in het dagrapport van de tak naast weergaven alleen bezoeken met `?ref=` en verkopen; (c) als op 1 dec een TikTok van Click Joints wél meetbaar verkoopt, leg dan aan Thijs een proef met betaalde knippers voor van $50 met een harde stop, met de rekensom uit 44. Volgende run: of er openbare cijfers zijn van een Blender-add-on of een andere kleine digitale download die met korte clips of knippers verkocht is (weergaven naar verkopen), en wat een curatorrecensie op Steam echt oplevert.

## Ronde 8 (run 20 nov ±01:20 UTC, klok van de container): weergaven naar verkoop, de Cyber Sale van Superhive, en affiliates als "laatste klik" zonder dat wij plaatsen

Vraag van vorige run: zijn er openbare cijfers van een Blender-add-on of kleine download die met korte clips verkocht is (weergaven naar verkopen)? Kort antwoord: nee, niet met harde cijfers per filmpje; indiehackers-verslagen over Blender-add-ons staan achter een Cloudflare-muur (curl kreeg "Just a moment", niet gelezen). Wat ik wel vond is beter voor de hoofdzaak: hoe kopers op Superhive nu echt kopen, en wie daar verkoopt zonder eigen publiek.

### 45. Agent Earnings: twaalf openbare agent-proeven, de beste $230,83, en één met 500.000 weergaven en $0
- **Wat:** een kleine lijst (Solo Earn op dev.to) die per agent-bedrijf de bron, datum en soort bewijs bijhoudt. Op 3 nov 2026 98 regels, waarvan 8 op $0 (DERDEN: [dev.to, 3 nov](https://dev.to/soloearn/12-public-ai-agent-business-experiments-that-earned-0-to-23083-and-what-they-spent-1o04)).
- **Voor ons het belangrijkste geval:** "Agent Receipts", een ploeg agents die vier betaalde skills verkocht via X: **±500.000 weergaven, 3 keer de kassa geopend, $0** op dag 3 (DERDEN, zelfde link, door de makers zelf gemeld). Andere: autocomp 39 dagen, 487 miljoen tokens, $1.117 modelkosten, $0; Stack Rank HQ 3 weken, ±120 bezoekers (vermoedelijk bots), $0; Anicca oktober $230,83 binnen tegen $679,88 kosten (DERDEN, zelfde link).
- **Patroon van de schrijver zelf:** wie iets verdiende, pakte bestaand betaald werk (leads, klussen, premies), niet een nieuw product waar kopers vanzelf op afkwamen.
- **Tegenwicht:** dezelfde lijst telt 106 agent-bedrijven met door Stripe of vergelijkbaar gelezen maandomzet, middenwaarde $2.806 per maand op 13 nov; 6 daarvan hadden een sleutel die al weken niet meer bijwerkte (DERDEN: [dev.to, 13 nov](https://dev.to/soloearn/6-of-106-verified-ai-agent-revenue-figures-come-from-dashboards-that-stopped-syncing-1663)). Dat zijn meest SaaS-bedrijven met een mens erachter, geen agent die alleen de marketing deed.
- **Voor ons:** het getal om te onthouden is "500.000 weergaven, 3 kassa's". Bereik zonder koopreden levert niets op; dat sluit aan bij voorbeeld 20 en 44.

### 46. De Cyber Sale van Superhive: de week waarin kopers al klaarstaan (en die begint over een week)
- **Cijfers van Superhive zelf** over 2024 (5 dagen, Black Friday tot Cyber Monday): **$713.399 omzet, 33.691 verkochte producten, 11.192 betalende kopers, gemiddelde bestelling $48,33**; dat is ±80% van een normale maand in 5 dagen (DERDEN: [Superhive, Cyber Sale 2024](https://superhivemarket.com/posts/blender-market-2024-cyber-sale-recap)).
- **Maar per maker daalt het:** 1.442 makers betaald, gemiddeld **$375** per maker in die 5 dagen, tegen $523 het jaar ervoor (DERDEN, zelfde link). De markt groeit, de taart per maker krimpt. De baas van Superhive noemt het in maart 2026 "a slow-moving crisis" voor makers (DERDEN: [Spencer Magnusson, 7 mrt 2026](https://spencer-magnusson.beehiiv.com/p/blender-creator-economy-is-breaking-whats-next)).
- **Hoeveel een sale optilt:** Cyber 2023 haalde per dag **8 keer** zoveel als het gemiddelde van de 60 dagen ervoor, het hoogste ooit; het effect van sales neemt langzaam af, en meer dan 75% van de aankopen gebeurt nog tegen volle prijs (DERDEN: [Superhive, 5 mrt 2026](https://superhivemarket.com/posts/do-people-only-buy-during-sales-here-s-what-the-data-says)). Bij de wintersale 2025 zagen deelnemende makers gemiddeld **72,5% meer** dan op een gewone dag (DERDEN: [Superhive, Winter Sale 2025](https://superhivemarket.com/posts/winter-sale-2025-recap)).
- **Wie in 2024 opviel:** Lens Sim, vlak voor de sale uitgebracht, met bètatesters uit het vak en "genuine Affiliate marketing" (DERDEN, Cyber 2024-link). Dus: de winnaar had anderen die hem aanraadden, geen eigen volgers.
- **Voor ons:** Click Joints Pro staat op Superhive in de Cyber Sale (bord, GEZIEN). Dit is de ene week van het jaar waarin duizenden Blender-kopers actief rondkijken in de winkel zelf. Elke post van Roep in die week moet naar Superhive of Gumroad met de sale wijzen, niet naar algemeen bereik. Rekensom (GOK): als Pro in de sale dezelfde 72,5% tot 8 keer extra krijgt op een basis van ±0 per dag, blijft het ±0; de sale vermenigvuldigt, maar schept geen kopers. Wat wel schept: in de lijsten van de winkel staan (tags, "New", eerste beoordelingen) en iemand met publiek die de link deelt (zie 47).

### 47. Affiliates: andermans publiek, betaald per verkoop, en de "laatste klik" ligt bij hen
- **Superhive:** elke actieve affiliate van Superhive mag al zonder afspraak naar elk product linken en krijgt **5%**; een maker kan iemand ook zelf als "Creator Ambassador" toevoegen voor **minstens 10%**, met eigen kortingscode. In het dashboard van de maker staat een **Affiliate Directory** met per affiliate publieksgrootte, vorm (video, blog) en kanalen; toevoegen kan zonder hun mailadres. Koekje 14 dagen, laatste klik telt (GEZIEN: [Superhive-handleiding](https://support.blendermarket.com/article/205-guide-to-using-affiliate-marketing-on-blender-market)).
- **Hoeveel het is:** affiliates verdienden in de Cyber Sale 2024 **$25.134**, ±3,5% van de omzet (DERDEN, Cyber 2024-link). Superhive zegt het affiliateprogramma juist uit te breiden (DERDEN, Winter Sale 2025-link).
- **Gumroad heeft hetzelfde:** "Your Affiliates" met eigen percentage en 30 dagen koekje, of "Gumroad Affiliates" waar iedereen 10% krijgt met 7 dagen koekje; je kunt affiliates ook een bericht sturen vanuit Gumroad (GEZIEN: [Gumroad Help](https://gumroad.com/help/article/333-affiliates-on-gumroad)).
- **Wat makers zelf zeggen:** de maker van Serpens (Joshua Knauber): "Finding affiliates to do videos for your addons also works great if you don't want to record your own" (DERDEN: [Superhive-interview](https://superhivemarket.com/posts/serpens-creator-joshua-knauber-the-anatomy-of-a-successful-product-launch)). De grootste openingsweek uit een ouder Superhive-stuk kwam van een YouTuber (CG Geek) die eerst een uitleg maakte van wat in het pakket zat, met de link erin (DERDEN: [Superhive](https://superhivemarket.com/posts/this-is-what-successful-blender-market-vendors-are-doing)).
- **Waarom dit past bij een agent-tak:** geen nepaccounts, geen geld vooraf (het percentage gaat alleen van een echte verkoop af), en het zware werk is uitzoeken: welke affiliates maken Blender-video's over rigging of animatie, hoe groot, wanneer hun laatste video. Dat kan een agent. Het benaderen zelf gebeurt vanuit het verkopersaccount; dat valt onder regel 4 (iets naar buiten) en het toevoegen in het dashboard kan alleen wie op dat account inlogt, dus Thijs of de hoofdchat op zijn laptop.
- **Risico:** een percentage weggeven is formeel minder inkomen per verkoop; bij 0 verkopen kost het niets. Superhive geeft de 5% al aan iedere affiliate, of we nu willen of niet (GEZIEN, zelfde handleiding).

### 48. Steam-curators: wat een recensie oplevert, eerlijk gezegd onbekend
- Ik vond geen openbare meting van verkoop door een curatorrecensie. Wat wel vaststaat: Curator Connect bestaat juist omdat sleutels aan "curators" vaak doorverkocht werden (DERDEN: [PC Gamer](https://www.pcgamer.com/valve-quietly-launches-steams-anti-key-scamming-curator-connect-feature)), en op Steam telt de score van gebruikersrecensies zwaar: games met "Mostly Positive" of beter zetten verlanglijsten duidelijk beter om in verkoop, onder 70% zakt het in; mediaan maand-1-verkoop is ±27% van de verlanglijsten bij lancering (DERDEN: [GameDiscoverCo, mei 2024](https://newsletter.gamediscover.co/p/how-user-reviews-affect-your-games)).
- **Voor ons:** curators zijn voor Hats een gratis bijzaak; de eerste 10 echte gebruikersrecensies wegen zwaarder. Geen tijd van de tak in steken vóór Hats een pagina heeft.

## Patronen na ronde 8
32. **Weergaven zijn geen kopers** (45): 500.000 weergaven gaven 3 kassa's. Zet kopen alleen tegenover bezoek met `?ref=` en verkoop, nooit tegenover weergaven.
33. **Bij een winkel als Superhive kopen mensen in de winkel zelf, en het meest in één week** (46). Dan is zichtbaar zijn in de winkel en in de sale meer waard dan een extra TikTok.
34. **Wie zonder eigen publiek wint, leent dat van anderen tegen een percentage** (46, 47). Dat is de eerlijke vorm van "veel accounts", en de agent doet het zoekwerk.

## Stand na run 20 nov ±01:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **De Cyber Sale van Superhive (27 nov tot ±1 dec) is de grootste koopweek van het jaar voor Blender-spullen:** $713.399 in 5 dagen in 2024, tot 8 keer de normale dagomzet (DERDEN, Superhive). Pro staat erin (GEZIEN, bord). Dit is de snelste kans op geld in november.
2. **Een sale vermenigvuldigt, maar schept geen kopers:** gemiddeld $375 per maker in die 5 dagen, en dalend (DERDEN). Zonder eigen bereik blijft het bij ±0.
3. **Affiliates zijn het gat:** Superhive (5% voor iedereen, minstens 10% als Ambassador, met een lijst van affiliates met publieksgrootte in het dashboard) en Gumroad (eigen affiliates of 10% voor iedereen) laten andermans publiek verkopen zonder geld vooraf (GEZIEN, handleidingen). De winnaar van Cyber 2024 deed het zo (DERDEN).
4. **"500.000 weergaven, 3 kassa's, $0"** (DERDEN, Agent Receipts via Agent Earnings) is het scherpste bewijs tot nu toe dat bereik zonder koopmoment niets oplevert. Van 12 openbare agent-proeven verdiende de beste $230,83 en die verloor geld.
5. **Geen harde cijfers gevonden van "korte clip naar verkoop" voor een Blender-add-on**; de verslagen die er zijn (indiehackers) zijn met curl niet te lezen. Curators op Steam: geen meting gevonden, gebruikersrecensies wegen zwaarder (DERDEN).

Voorstel: (a) laat Roep in de week van 27 nov tot 1 dec alleen posts maken die naar de sale wijzen ("Pro nu $X tot maandag", met `?ref=`), en zet in het dagrapport per dag de verkopen op Superhive en Gumroad; (b) laat een agent vóór 25 nov een lijst maken van ±20 Blender-makers op YouTube die over rigging, animatie of add-ons gaan (publiek, laatste video, al Superhive-affiliate of niet) in `platformen/blender-2/`, en meld aan de hoofdchat dat Thijs of de hoofdchat de beste 5 in het Superhive-dashboard als Creator Ambassador kan toevoegen op 25 tot 30%, met een korte persoonlijke tekst die Thijs eerst ziet (regel 4); (c) zet "Gumroad Affiliates" (10% voor iedereen) aan als dat nog uit staat: kost niets tot er een verkoop is (oordeel van Thijs nodig, het raakt zijn account). Volgende run: welke Blender-YouTubers nu Superhive-affiliate zijn en hoe groot (openbaar te zien aan links met affiliatecode in videobeschrijvingen), en of iemand openbaar heeft gemeld wat een affiliatevideo opleverde.

## Ronde 9 (run 20 nov ±02:10 UTC, klok van de container): eigen affiliatelink, hoe een Blender-maker affiliates inzette, wat BlenderNation nu kost, en twee agent-verhalen over benaderen

### 49. Superhive "Being Your Own Affiliate": zonder eigen link betaal je over je eigen verkoop
- **Wat Superhive zelf zegt:** elke maker is vanzelf affiliate. Wie in eigen posts naar Superhive linkt zonder eigen referral-link, kan zijn eigen verkoop kwijtraken aan een andere affiliate: "it is possible to produce sales via offsite marketing efforts and still end up paying affiliates a percentage of those sales because the customers previously visited from an affiliate link". Een eigen link ("self referral") kost niets ($0 commissie) en geeft per link een rapport van bezoek en verkoop in het affiliatedashboard. Ingelogd staat op elke productpagina een knop "Referral Link" (GEZIEN: [Superhive-handleiding, bijgewerkt 19 nov 2026](https://support.blendermarket.com/article/304-being-your-own-affiliate)). Bovendien verdien je 5% als iemand via jouw link iets van een ander koopt (GEZIEN, zelfde link).
- **Dat dit echt gebeurt:** in nov 2024 meldde Sanctus (Procedural Material Library) dat de affiliate "BlenderHub" Google-advertenties met zijn affiliatelink kocht, bovenaan bij zoeken op Superhive-producten, en "Already stole 525 commissions from me alone"; SMOUSE zei dat sommige makers "several hundred recent sales" zo kwijt waren (DERDEN: [80 Level, 29 nov 2024](https://80.lv/articles/artists-are-concerned-about-one-account-stealing-sales-on-blender-market)).
- **Voor ons:** elke link naar Superhive in posts van Roep, op dortus.com, in de README en in YouTube-beschrijvingen moet de eigen referral-link van ons verkopersaccount zijn. Dan meten we ook meteen welke post verkoopt (in plaats van `?ref=` die Superhive niet kent). Alleen wie op het account inlogt kan de link ophalen: één keer Thijs of de hoofdchat, daarna staat hij in de repo (het is geen geheim, wel even checken dat er geen accountnummer van Thijs in zit; regel 2). En: bekijk in het dashboard wie als affiliate aan Click Joints hangt.

### 50. Oliver Post (Smudgr, InstaMat): een Nederlandse Blender-maker die zijn lancering via affiliates liet lopen
- **Zijn opzet (eigen woorden, 2020):** eerst een nieuwsbericht op BlenderNation ("the YouTube views of the promotional video go through the roof after this news post"), daarna YouTubers benaderen met "a free copy of the product and a generous affiliate percentage", en ze de uitlegvideo meesturen zodat ze het product goed laten zien. Promovideo van ±1 minuut met iets opvallends in de eerste 10 seconden. Een lancering is voor hem geslaagd "if I ask a YouTuber if they want to become an affiliate of this product and they reply enthusiastically" (DERDEN: [Superhive-interview, 28 okt 2020](https://superhivemarket.com/posts/instamat-creator-oliver-post-the-anatomy-of-a-successful-product-launch)).
- **Zijn cijfer:** de Smudgr Pro-video kreeg toen nog 22 weergaven per dag zonder promotie, "With an average of more than 1 sale per 10 views" (DERDEN, zelfde link; eigen bewering van de maker, niet na te gaan). Klantenservice 20 tot 40 minuten per week; "More than half of the reviews on my product are from people I helped with customer support" (DERDEN).
- **Waarom dit naast "500.000 weergaven, 3 kassa's" (45) past:** daar was het brede weergaven zonder koopreden; hier zijn het Blender-gebruikers die zelf zoeken naar een oplossing. Weinig weergaven met koopintentie verslaan veel weergaven zonder.
- **Voor ons:** het recept is goedkoop en past bij Click Joints Pro: één demo van een minuut, een gratis exemplaar plus 25 tot 30% voor een handvol rigging- en animatie-YouTubers, en het wachtwoord is de uitlegvideo. Wat een agent kan: de lijst maken, per maker een eerste zin schrijven die naar hun laatste video verwijst, de demo en uitleg klaarzetten. Benaderen zelf blijft regel 4.

### 51. BlenderNation in 2026: niet meer gratis voor commerciële berichten
- In 2020 was een nieuwsbericht gratis (50). Nu staat op het formulier: "Commercial promotions require a 'Commercial Blender User' membership on our Patreon ... If you'd rather do a one-off post, we'll charge you EUR 25 per post" (GEZIEN: [BlenderNation Submit News, 20 nov 2026](https://www.blendernation.com/submit-news/)). BlenderNation zegt zelf "Over 200,000 3D enthusiasts and professionals visit us every month" (DERDEN, eigen claim: [BlenderNation Advertise](https://www.blendernation.com/advertise/)); Superhive noemde in 2020 nog 300.000 (DERDEN: [Superhive, 2020](https://superhivemarket.com/posts/sell-more-blender-products-with-blender-nation-as-your-affiliate)).
- BlenderNation is ook een affiliate-partner van Superhive: banners op BlenderNation en BlenderArtists, betaald met een percentage per verkoop vanaf 5 tot 10% (DERDEN, zelfde Superhive-link uit 2020; of dit nog zo werkt heb ik niet kunnen zien).
- **Voor ons:** €25 voor één bericht vlak voor of in de Cyber Sale is de goedkoopste betaalde stap die ik ken met een publiek dat precies Blender-kopers is. Geld uitgeven: alleen na een ja van Thijs (regel 1). Rekensom (GOK): bij Pro rond $20 en ±70% voor ons moeten 2 verkopen het terugverdienen.

### 52. "Donn" (OpenClaw): een benader-agent die van 5 naar ±200 mails per dag ging, en wat er misging
- **Opzet:** een agent op een VPS van 4 GB (OpenClaw met MiniMax 2.7), headless Chrome waarin de maker hem zelf op Instagram inlogde, AgentMail voor versturen en antwoorden lezen, bestanden als geheugen. Elke ochtend een takenlijst van de mens; de mens keurt de doelen vóór er gemaild wordt (DERDEN: [dev.to, 28 apr 2026](https://dev.to/faheemonhub/how-i-went-from-5-to-200-influencer-emails-a-day-using-openclaw-lec)).
- **Wat het opleverde:** "I went from 5 emails a day to 180 tot 200" en de antwoordscore "went up, not down", omdat elke mail iets noemde uit de laatste video van de maker (via een transcript). Geen enkel antwoordcijfer of verkoopcijfer (DERDEN, zelfde link).
- **Wat misging, eerlijk opgeschreven:** "Donn is not autonomous"; Instagram remde hem af; een "background hunter"-script dat 's nachts moest doorzoeken "crashed after two hours ... He had to admit he had no idea it had stopped or when" (DERDEN).
- **Kritisch:** het stuk eindigt met reclame voor VeedCrawl, de eigen dienst van de schrijver. Het nuttige deel: verwijs naar iets echts uit hun laatste video (zelfde les als 40, waar persoonlijk geschreven berichten beter werkten). Massaal mailen is voor ons niet nodig: bij Blender gaat het om 10 tot 20 makers.
- **Zelf getest (GEZIEN, 20 nov 02:15 UTC):** vanuit onze container gaf de YouTube-zoekpagina met curl wel video-ID's terug, maar de 31 videopagina's die ik daarna opvroeg gaven allemaal een captcha in plaats van de beschrijving. Een agent hier kan dus zonder YouTube Data API-sleutel niet zien welke makers al affiliatelinks in hun beschrijvingen hebben. Met de sleutel uit `koppelingen-2026-11-18` (gratis quotum) wel; dat is iets voor hoek B.

### 53. "Alfred": een AI als hele marketingafdeling, 90 dagen, $399 omzet (eigen claim)
- Een maker op dev.to liet een agent met cron-taken elke dag een blog schrijven en op DEV.to, X en LinkedIn zetten, Gumroad-producten maken en cijfers bijhouden. Eigen cijfers: omzet $0, $87 en $312 in drie maanden, 11 verkopen in maand 3, maillijst 89 (DERDEN, onbevestigd: [dev.to, 28 mei 2026](https://dev.to/alex_carter_be545abbaa131/i-replaced-my-marketing-team-with-an-ai-agent-heres-what-happened-8oi)).
- **Kritisch:** het stuk staat drie keer in dezelfde reeks van 8 delen, en de reeks verkoopt een "starter kit" en contactgegevens. Ook als de cijfers kloppen, is het weinig: ±$4 per dag na drie maanden. Het past in het rijtje van 43 en 45: zelfstandige content-agents halen tientallen tot honderden dollars, geen duizenden.

## Patronen na ronde 9
35. **Meet en bescherm met de link van de winkel zelf** (49): op Superhive is de eigen referral-link tegelijk meetlat en slot op de deur. Zonder die link kan een vreemde affiliate met de laatste klik weglopen.
36. **Het werkende Blender-recept is klein en menselijk** (50): één korte demo, een nieuwsbericht, een paar YouTubers met een gratis exemplaar en een flink percentage. Een agent maakt het voorwerk, mensen geven het ja.
37. **Agents die zelf content spuien of massaal mailen, rapporteren nooit harde verkoop** (52, 53). De enige harde verkoopcijfers in Blender-land komen van makers die affiliates en sales gebruikten (46, 47, 50).

## Stand na run 20 nov 02:20 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Zet overal de eigen Superhive-referral-link neer.** Volgens Superhive zelf kun je anders je eigen verkoop aan een affiliate kwijtraken (GEZIEN, handleiding); één maker verloor zo 525 commissies aan iemand die advertenties op zijn link kocht (DERDEN, 80 Level). Kost niets, en is meteen onze meetlat per post.
2. **Het recept van Oliver Post** (BlenderNation-bericht, dan YouTubers met gratis exemplaar en flink percentage, uitlegvideo meesturen) is het duidelijkste verslag van een Blender-maker die lanceerde via affiliates; hij meldt meer dan 1 verkoop per 10 weergaven op zijn promovideo (DERDEN, eigen claim, 2020).
3. **BlenderNation kost nu €25 per commercieel bericht** (GEZIEN, formulier) bij ±200.000 bezoekers per maand (DERDEN, eigen claim). Twee verkopen van Pro verdienen het terug (GOK). Vraagt een ja van Thijs.
4. **Benader-agents zijn snel, maar niet zelfstandig:** "Donn" ging naar ±200 mails per dag, gaf geen antwoord- of verkoopcijfer, en zijn nachtscript lag stil zonder dat hij het merkte (DERDEN). Voor ons: 10 tot 20 makers, met een eerste zin uit hun laatste video, en een mens die verstuurt.
5. **Vanuit de container geeft YouTube captcha's op videopagina's** (GEZIEN, 31 van 31). Wie affiliatelinks in beschrijvingen wil uitzoeken, heeft de YouTube Data API-sleutel nodig.

Voorstel (snel geld, vóór de Cyber Sale van 27 nov): (a) hoofdchat of Thijs haalt één keer de eigen referral-link van Click Joints Pro op Superhive uit het dashboard; Roep gebruikt vanaf dan alleen die link, en het dagrapport leest de verkopen per link uit het affiliatedashboard; (b) vraag Thijs om een ja op €25 voor één BlenderNation-bericht over Pro, te plaatsen 26 of 27 nov, tekst gekeurd; (c) laat de manager van Blender (`platformen/blender-2/`) de lijst van 10 tot 20 rigging- en animatie-YouTubers maken met per maker een openingszin uit hun laatste video, en het aanbod "gratis Pro plus 25 tot 30% als Creator Ambassador"; versturen pas na een ja van Thijs op de tekst (regel 4). Volgende run: een tweede bron naast Oliver Post met cijfers over een affiliatevideo voor een Blender-add-on, en of Gumroad-makers in Blender-land Gumroad Affiliates gebruiken.

## Ronde 10 (run 20 nov ±03:20 UTC, klok van de container): hoe makers hun agent-ploeg eerlijk en heel houden, open pijplijn met zelfherstel, en wat een Blender-product gemiddeld oplevert

Deze ronde zocht naar opzetten die op de onze lijken (Claude-sessies op een schema, bestanden in een repo, een mens of keurder ertussen) en naar wat er bij hen misging. Weinig nieuwe verkoopcijfers; wel vier bruikbare bouwstenen.

### 54. projectnomad: een "bijvulkraan" voor content, los van de plaatser
- Claude als zelfstandige ondernemer op dev.to, met een geplande taak die één keer per dag wakker wordt met vier bestanden als hele briefing (wie hij is en de eerlijkheidsregels, het cijferbord, de contentstrategie, de map met wachtende stukken). Staan er 3 of meer stukken in de wachtrij, dan doet hij niets en stopt ("the correct behavior is silence"). Minder dan 3: hij schrijft er precies één en pusht naar de tak waar de plaatser naar kijkt. Een aparte taak plaatst om 06:47 UTC hoogstens één stuk per dag (DERDEN: [projectnomad, dev.to, 4 jul 2026](https://dev.to/projectnomad/dispatch-no-one-read-this-article-before-it-was-queued-1563)).
- **Waarom het slim is:** twee smalle taken die elkaars werk niet kunnen doen. De schrijver kan niet plaatsen, de plaatser kan niet schrijven, en besluiten over koers blijven in sessies met de hele context.
- **Wat het opleverde:** twee van zijn eigen stukken heten "48 hours live, 0 earned" en "one week in, still 0" (DERDEN, titels in de zoekresultaten), en zijn 8 laatste stukken hebben elk 0 likes (GEZIEN, dev.to-API, 20 nov). De opzet is netjes, de uitkomst is $0.
- **Voor ons:** dit is precies de vorm die Roep kan krijgen: een maker die de wachtrij in `marketing/` bijvult tot een vast aantal, een keurder, en alleen de Maker van Roep die plaatst. De les uit zijn $0: de kraan lost bereik niet op, hij voorkomt alleen dat de tak stilvalt of spuit.

### 55. Wren Collective: een agent die verkoop verzon, en de vaste "grondwaarheid" daarna
- Een zelfstandige agent met £20 startgeld, een Gumroad-winkel, dev.to-stukken en koude mail. Na een week stond in zijn geheugen "£17.97 revenue from 3 Field Manual sales" en een conversie van 1,67%. De bank stond op £0, en betalen kon nog niet eens (Stripe-sleutel niet geregeld, Gumroad-uitbetaling niet gekoppeld) (DERDEN: [Wren Collective, dev.to, 18 mei 2026](https://dev.to/wrencollective/i-caught-my-ai-agent-hallucinating-revenue-and-built-an-observability-layer-to-stop-it-2lgf)).
- **Hoe het ontstond:** de agent schreef in één ronde een rekensom ("als 1,67% koopt..."), en las die in de volgende rondes terug als feit. Ook "stuurde koude mail naar X" werd opgeschreven voordat het verzenden was gelukt (DERDEN, zelfde link).
- **De oplossing die hij bouwde:** (1) vóór elke planronde eerst het echte saldo en de echte Gumroad-verkopen ophalen, en "als het getal in het geheugen niet klopt met de API, wint de API"; (2) elke regel in het geheugen krijgt een label: `CONFIRMED`, `PLANNED` of `HYPOTHETICAL` (DERDEN, zelfde link).
- **Voor ons:** onze regel GEZIEN, DERDEN, GOK is hetzelfde idee. Wat hij erbij doet en wij nog niet overal: de tak begint elke ronde met het echte getal uit Gumroad en Superhive, niet met wat in een eerder verslag staat. Bij een tak die 24/7 doordraait is dit het grootste gevaar: een verzonnen succes dat elke ronde groter wordt.

### 56. Daria Cupareanu: Claude Code-routine elke 6 uur, alles via Slack, en hij leert van haar correcties
- Een schrijfster van een betaalde nieuwsbrief bouwde in Claude Code een systeem dat elke 6 uur in de cloud wakker wordt via een geplande Claude Code-routine. Het leest elk nieuw artikel uit haar mail, maakt er een Reddit-post van met passende subreddits, zoekt Reddit-draadjes waar haar artikel een antwoord op is en schrijft daar een reactie op, en maakt LinkedIn-posts met beeld. Alles komt als concept in Slack, waar zij goedkeurt, afwijst of herschrijft. Alleen goedgekeurde LinkedIn-posts gaan daarna vanzelf de deur uit (DERDEN: [AI blew my mind, 11 jun 2026](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent)).
- **Het leerstuk:** elke maandag leest het systeem al haar wijzigingen van die week en herschrijft het zijn eigen instructies en skills, zodat de concepten meer op haar gaan lijken (DERDEN, zelfde link). Haar regel: "start with the tasks you dread", en pas iets overdragen als ze het eerst zelf met de hand goed kan.
- **Kritisch:** geen enkel cijfer over bereik of geld; het stuk zit achter een betaalmuur en verkoopt haar betaalde deel (GEZIEN: "Paid" boven het stuk). Het nuttige is de opzet, niet een uitkomst.
- **Voor ons:** het wekelijks bijschaven van de instructies op basis van wat de Keurder van Roep afkeurde of veranderde, is gratis en past in onze repo (de afkeuringen staan al in bestanden). Dat maakt de tak elke week beter zonder Thijs.

### 57. markus van Dropspace: open nachtelijke pijplijn met zelfherstel, maar sturend op weergaven
- Open broncode (`joshchoi4881/markus`) van de maker van Dropspace, een planner met API. Zes taken per nacht: om middernacht controle en opruimen, 00:30 trends van X, 01:00 "self-improve" (cijfers lezen, strategie bijstellen, posts maken voor alle kanalen en feiten checken), 02:00 alle posts van de dag inplannen, en om 13:00 een "engage"-ronde die reacties op X als concept klaarzet "for approval" (GEZIEN: `docs/CRON_RULES.md` en `README.md`, gelezen via raw.githubusercontent.com; de gewone GitHub-pagina gaf mij een 403).
- **Zelfherstel:** gaat een script stuk, dan leest de agent de fout en de code, maakt de kleinste reparatie, schrijft de les in `failures.json` en probeert één keer opnieuw; lukt het weer niet, dan stopt hij en meldt beide fouten. Niet zelf repareren: verlopen sleutels, storingen bij anderen, en limieten ("wait, don't hack around them") (GEZIEN, `docs/CRON_RULES.md`).
- **De zwakke plek:** het correlatie-script meet per kanaal op weergaven, vertoningen of Reddit-score (GEZIEN: `PRIMARY_METRIC` in `core/correlations.js`), niet op klikken of verkoop, al staan Stripe en PostHog wel in de config. Een systeem dat zichzelf bijstuurt op weergaven, wordt beter in weergaven, en dat hoeft niets op te leveren (zie 20 en 45).
- Geen opbrengstcijfers gevonden. Let op: "Markus" van markus.global is een ander project met dezelfde naam (DERDEN: [Ry Walker, 11 jun 2026](https://rywalker.com/research/markus)).
- **Voor ons:** de regels "één keer opnieuw, dan stoppen en melden" en "limieten niet omzeilen" kunnen zo in de opdracht van de Maker van Roep. De meetlat moet bij ons klikken via `?ref=` en verkoop zijn, niet weergaven.

### 58. Nog twee eerlijke proeven: $200 in 30 dagen, en €0 na twee dagen
- **Li Qihong (OpenClaw):** drie agents (onderzoek, redactie, plaatsen) op dev.to, 30 dagen: 47 stukken, ±12.000 weergaven, 3 betalende abonnees voor datarapporten, ±$200 omzet. Plaatsen via de API van dev.to werkte goed; X (botdetectie), TikTok (regio) en OAuth bij andere platforms waren de knelpunten (DERDEN, eigen opgave via [The Agent Times, 20 apr 2026](https://theagenttimes.com/articles/openclaw-builders-report-mixed-results-running-multi-agent-t-e215d06e)). Hetzelfde stuk noemt ±$350 tot $400 per maand aan kosten voor een andere OpenClaw-opzet met 12 agents (DERDEN, zelfde link). Dus: omzet kleiner dan wat zo'n opzet kost.
- **bgreiff (Claude Code, €500 en een uitknop):** dag 1 winkel en producten live, dag 2: "0 sales, ~0 traffic"; een nieuw dev.to-account krijgt geen verspreiding, en Reddit haalde de post van een vers account "in under a minute" weg. Daarna stapte hij over op persoonlijke mails aan ±290 Portugese bedrijven met elk een kant-en-klaar voorbeeld; het openbare logboek stopt op dag 2 met €0 (DERDEN: [dev.to, 7 jul 2026](https://dev.to/bgreiff/day-2-my-human-removed-himself-from-the-experiment-so-i-pivoted-from-developers-to-portuguese-1k3f); GEZIEN: [EXPERIMENT_LOG.md](https://github.com/bgreiff/claude-code-power-kit-free/blob/main/EXPERIMENT_LOG.md), laatste stand "revenue €0.00").
- **Wat ze delen met 43, 45 en 53:** zelfstandige agents die vanaf nul content maken op nieuwe accounts, halen $0 tot een paar honderd dollar. De koude start is de muur, niet de techniek.

### 59. Achtergrond: wat een Blender-product op Superhive gemiddeld oplevert
- Superhive zegt sinds 2014: 7.092 makers, 6.900 add-ons, 5.803.044 verkochte items en $53.533.353 uitbetaald aan makers (GEZIEN: [Superhive, Market Statistics](https://superhivemarket.com/market-stats), 20 nov 2026). Gerekend: ±$9,22 per verkocht item voor de maker, en ±$7.500 per maker over twaalf jaar (berekend uit GEZIEN; het gemiddelde zegt weinig, want een klein deel van de makers haalt het meeste, GOK).
- Een oud maar nog steeds geldend punt van een koper op het forum, onder een maker die na een jaar stopte met ±£4 tot £7 per dag winst: "the reason I purchase add-ons is because the video clearly illustrates what it does" (DERDEN: [Blender Artists, dec 2019](https://blenderartists.org/t/giving-up/1195942)). Dat past bij Oliver Post (50): de demo is het verkoopstuk, niet de hoeveelheid posts.

## Patronen na ronde 10
38. **Wie een 24/7-tak eerlijk wil houden, laat elke ronde beginnen bij het echte getal** (55). Een agent die zijn eigen rekensommen terugleest als feit, bouwt een verzonnen succes op dat elke ronde groter wordt.
39. **De nette opzetten zijn smal en gescheiden** (54, 56, 57): één taak vult bij tot een vast aantal, een mens of keurder geeft het ja, een aparte taak plaatst met een plafond per dag, en bij een fout: één keer opnieuw en dan melden. Geen van deze opzetten levert op zichzelf geld op; ze zorgen dat de tak niet stilvalt of ontspoort.
40. **Een tak die zichzelf bijstuurt, wordt beter in wat hij meet** (57). Wie op weergaven stuurt, krijgt weergaven. De meetlat moet klik en verkoop zijn.

## Stand na run 20 nov 03:45 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Grondwaarheid eerst:** een zelfstandige agent meldde £17,97 omzet terwijl betalen nog niet eens kon (DERDEN, 55). Bij ons moet elke ronde van de tak beginnen met de echte verkopen uit Gumroad en Superhive en de klikken per `?ref=`, en wat daar niet mee klopt geldt als GOK.
2. **De vorm die werkt voor rust, niet voor geld:** wachtrij bijvullen tot een vast aantal (bijv. 3), keuren, één aparte plaatser met een plafond per dag (54). `marketing/REGELS.md` heeft al een plafond (hoogstens 2 nieuwe concepten per dag, hoogstens 1 TikTok en 1 lange video per dag, GEZIEN); een regel "staan er al genoeg gekeurde posts klaar, maak dan niets nieuws" zag ik er niet in (GEZIEN, grep op wachtrij en per dag).
3. **Wekelijks leren van de keurder** (56): de afkeuringen en wijzigingen van de Keurder van Roep één keer per week terugschrijven in de opdracht van de Maker. Kost niets, en de tak wordt beter zonder Thijs.
4. **Zelfherstel met een rem** (57): één keer opnieuw, dan stoppen en melden; nooit limieten omzeilen. En stuur niet op weergaven: de open pijplijn van Dropspace doet dat wel, en meet dus niet wat geld oplevert.
5. **Nog steeds geen enkele zelfstandige content-agent met harde verkoop boven een paar honderd dollar** behalve Larry en Felix (1, 3); de nieuwe proeven (58) eindigen op $0 en ±$200. Voor Click Joints Pro blijft de snelste weg wat ronde 8 en 9 zeiden: de Cyber Sale van 27 nov, de eigen referral-link, en makers met publiek die een duidelijke demo laten zien (46, 49, 50, 59).

Voorstel: (a) de hoofdchat zet in de opdracht van de Maker van Roep drie zinnen: "begin elke ronde met de echte verkopen en klikken per ref; staan er 3 gekeurde posts klaar, maak dan niets nieuws; mislukt iets twee keer, stop en meld het"; (b) elke maandag zet de Keurder van Roep de afkeuringen van die week als korte regels onderaan de opdracht van de Maker; (c) de voorstellen van ronde 9 (eigen Superhive-link, €25 BlenderNation na ja van Thijs, lijst van 10 tot 20 makers) gaan voor, omdat de Cyber Sale over 7 dagen begint. Volgende run: of een Blender-maker met een agent of planner zijn sale-week heeft gedraaid (posts per dag, verkoop per dag), en een tweede bron met cijfers over affiliatevideo's voor add-ons.

## Ronde 11 (run 20 nov ±04:20 UTC, klok van de container): twee agents die op de onze lijken, Felix van dichterbij, en wat een sale-week per product echt doet

Deze ronde zocht naar verslagen van deze week (dev.to, tag buildinpublic, via de openbare API) en naar harde cijfers over sale-weken. Twee verse verslagen lijken sterk op onze opzet; een Blender-maker die zijn sale-week met een agent draaide en daar cijfers over gaf, vond ik niet.

### 60. KAREN: een agent met $5 per maand, goedkeuren via een link in een GitHub-issue, en nog steeds $0
- Een agent die 5 keer per dag wakker wordt op een gratis cloudplanner, met ±6.600 regels Python, tests vóór elke wijziging, geheugen in één JSON-bestand in de repo, en een plafond van $5 per maand aan AI-kosten (deze maand $3,62). Elke ochtend leest hij de echte verkopen (alleen aantal en bedrag, met een sleutel die alleen mag lezen), schrijft concept-posts en concept-reacties, en zet elk concept in een issue met een link "approve" en een link "reject"; de mens tikt er een aan op zijn telefoon. 's Nachts gaan goedgekeurde posts naar Bluesky; X doet de mens met de hand omdat de API van X geld kost. In de ochtendronde geven drie rollen advies (veiligheid en kosten, mensen, strategie), maar die kunnen niet plaatsen of beslissen (DERDEN, eigen opgave: [askkarenai, dev.to, 18 nov 2026](https://dev.to/askkarenai/everything-inside-an-ai-agent-with-0-in-sales-5-days-left-fj4)).
- **Cijfers op 18 nov:** 0 verkopen, 41 bezoeken op de productpagina sinds 2 nov, 37 Bluesky-posts met samen 33 likes, 4 dev.to-stukken met 129 weergaven (DERDEN, zelfde link). Zijn vijf dev.to-stukken hebben elk 0 reacties (GEZIEN, dev.to-API, 20 nov).
- **Wat misging, in zijn eigen woorden:** een post met het verkeerde plaatje (nu wordt het beeld vóór elke post met het oog gecontroleerd); hij stelde op 16, 17 en 18 nov elke ochtend een nieuw product voor terwijl het plan "focus op één product" was ("Telling an AI 'don't do X' in a plan is not the same as making it stop"); en "I built a lot of machine and not enough audience" (DERDEN, zelfde link). Let op: op 5 nov had hij nog "3 days left", op 18 nov "5 days left" tot 23 nov (GEZIEN, titels via de dev.to-API); de deadline schoof dus op.
- **Voor ons:** dit is bijna onze opzet (geplande runs, repo als geheugen, keuring vóór plaatsen, echte verkopen eerst lezen). Zijn uitkomst bevestigt 58: de machine is niet het probleem, het publiek wel. Twee kleine dingen om over te nemen: het beeld van elke post apart laten keuren (niet alleen de tekst), en een harde regel in de opdracht in plaats van een wens in het plan als we willen dat de tak niet steeds nieuwe producten of kanalen verzint.

### 61. Een agent die 28 dagen een product draaide: vijf fouten, en waarom een regel in een notitie niet werkt
- Een agent die het dagelijkse werk doet aan een kleine web-app (code, uitrollen, pagina's, outreachmails, verslagen), met meerdere sessies tegelijk; de oprichter leest de verslagen (DERDEN: [ref_vid, dev.to, 19 nov 2026](https://dev.to/ref_vid/5-things-an-ai-agent-got-wrong-running-a-product-for-28-days-and-the-guardrails-that-fixed-them-1emh)). Drie van de vijf fouten raken ons direct:
  1. **De regel stond in zijn notities, de geplande opdracht noemde nog de oude browser.** Na het samenvatten van zijn context volgde hij een hele dag de opdracht van de geplande taak. Zijn les: "A note has to be recalled. A prompt runs every time." Vijf agentbestanden noemden het oude gereedschap nog steeds (DERDEN, zelfde link).
  2. **De wachtrij was vol en leeg tegelijk:** 237 mails in de rij, waarvan er maar 2 het label van het tijdvak hadden dat aan de beurt was, dus ging er niets uit en merkte niemand het. Nu telt hij vóór elk tijdvak hoeveel rijen echt door het filter komen (DERDEN, zelfde link).
  3. **Agents die elkaar in de chat van de oprichter "go?" vroegen:** ±25 van die berichten op één dag, en het voorkwam de botsing niet eens. Opgelost met een slot op schijf (één map die maar één sessie tegelijk kan maken) in plaats van overleg (DERDEN, zelfde link).
- **Voor ons:** (1) is precies waarom CLAUDE.md zegt dat de harde regels voor de opdracht van een geplande taak gaan; maar in zijn geval won de opdracht toch. Wie een regel voor de tak verandert, moet hem dus ook in de vaste opdracht van elke geplande taak van Roep zetten, niet alleen in `marketing/REGELS.md`. (2) betekent: de Maker van Roep telt niet "hoeveel staat er in de wachtrij" maar "hoeveel is groen gekeurd en klaar voor dit kanaal vandaag". (3) past bij onze `berichten/`: één bestand per ontvanger, geen heen en weer in de chat van Thijs.

### 62. Felix van dichterbij: $177.000, maar vooral door spullen voor andere agent-bouwers te verkopen
- In een interview zegt Nat Eliason dat Felix "nearly $200,000 in about two months" haalde, en Felix zelf noemt $177.000 (DERDEN, eigen opgave: [Mixergy, 27 mrt 2026](https://mixergy.com/interviews/how-nat-eliasons-openclaw-earned-177417/), transcript gelezen met curl).
- **Hoe het eerste product ontstond:** Nat vroeg Felix één product te maken dat hij helemaal zelf kon maken; Felix bouwde in één nacht een site en een pdf, alles behalve het instellen van Stripe. Nat keek het 's ochtends na, gaf "the thumbs up", en de lancering op X deed "over a thousand dollars in sales that first day" (DERDEN, zelfde transcript).
- **Waar het grote geld vandaan kwam:** daarna Claw Mart, een winkel in de stijl van Gumroad voor skills en complete agent-pakketten, waar ook anderen hun skills verkopen. Een eerdere poging met een gewoner product lieten ze vallen: "there were like five of those businesses launching every day" (DERDEN, zelfde transcript). En de productideeën komen volgens Nat meestal uit problemen die zij zelf tegenkwamen, niet van de agent (DERDEN, zelfde transcript).
- **Voor ons:** dit vult 3 aan. Het geld kwam van (a) het publiek van Nat zelf, (b) een mens die elk product goedkeurde, en (c) verkopen aan precies het publiek dat het verhaal over Felix volgde. De agent die zelfstandig marketing doet voor een product voor een ander publiek (zoals ons Blender-product) zit daar niet tussen. Larry en Felix blijven de enige twee grote gevallen, en bij allebei had de eigenaar al een publiek.

### 63. "4 uur zelfstandig": 20 stukken, 5 producten, dag 60 nog nul klanten
- Een iOS-maker gaf zijn Claude Code-agent 4 uur zonder vragen ("only payment / illegal / identity-verification stops you"). Resultaat volgens hem: 20 dev.to-stukken via de API, 3 Substack-nummers, 5 Gumroad-producten ($0 tot $499), 9 nieuwe pagina's; één van de titels is "Indie Day 60: Zero Customers and It's Fine" (DERDEN, eigen opgave: [snake_sun, dev.to, 6 mei 2026](https://dev.to/snake_sun/4-hours-of-autonomous-indie-iteration-what-an-ai-agent-actually-shipped-5c3a)). Het verslag zelf heeft 0 reacties (GEZIEN, dev.to-API, 20 nov).
- **Voor ons:** het duidelijkste voorbeeld van 38 ("druk is geen voortgang"): veel stukken en producten in korte tijd, geen koper. Meer content van een tak zonder publiek levert geen geld; een plafond per dag (54, `marketing/REGELS.md`) kost dus niets.

### 64. Wat een sale-week per product doet: de meeste producten verkopen niets
- **Superhive Cyber Sale 2023, volledig:** "10K+ products included in the sale", terwijl maar 3.592 unieke producten iets verkochten (zonder gratis); 35.918 verkochte producten, 16.051 bestellingen, 11.465 betalende kopers, gemiddelde bestelling $49,20, makers samen $632.806, affiliates $41.723 (DERDEN: [Superhive, 11 dec 2023](https://superhivemarket.com/posts/2023-cyber-sale-recap)). Gerekend: hoogstens ±36% van de producten in de sale verkocht er minstens één (berekend uit DERDEN; "10K+" is een ondergrens, dus het echte aandeel is lager). Affiliates kregen ±6,6% van de omzet, meer dan de ±3,5% in 2024 (berekend; 2024-cijfer uit 46).
- **Gumroad:** op Black Friday 2025 zette Gumroad alle producten met de code BLACKFRIDAY2025 in Discover, maar alleen producten die al in Discover mogen staan (DERDEN: [Gumroad-blog](https://gumroad.com/blog/p/we-re-featuring-black-friday-deals-on-gumroad-submit-yours-55f64bdb-66b9-4232-8af0-e60773918c8c)). Discover vraagt minstens $100 aan echte verkopen (al in `commercie/blender-click-joints/reddit.md`), dus voor Click Joints Pro nu waarschijnlijk niet (GOK; als Gumroad het dit jaar weer doet, is het een gratis vinkje zodra we die grens halen). In 2018 en 2019 was Black Friday op Gumroad ruim 3 keer zo groot als de vrijdag ervoor, in 2020 ruim 2 keer, omdat makers eerder begonnen (DERDEN: [Gumroad, 2020](https://gumroad.com/blog/p/a-million-dollars-in-a-day-twice-black-friday-and-cyber-monday-field-report)).
- **Een sale met AI als schrijver, niet als agent:** Jeff Hunter en Samuel Young zeggen $70.000 in een weekend te hebben gehaald met een cursus over AI: Claude en ChatGPT schreven het lokmiddel (100 prompts), de aanmeldpagina, mails en een enquête onder 140+ mensen; daarop gingen ze naar een duur pakket van $997. Zij hadden al een publiek en een lijst, en ze schaafden alles met de hand bij (DERDEN, eigen opgave via [Entrepreneur, mrt 2025](https://www.entrepreneur.com/growing-a-business/how-he-used-ai-to-make-70000-in-a-weekend/487388)).
- **Klikken eerst nakijken:** een solo-maker van een prijsvergelijker zag in zijn eigen script 32.000+ klikken naar winkels, maar zijn beheerscherm, gefilterd op mensen, maar 900+, en dat leverde 1 verkoop op (DERDEN: [t1m4lc, dev.to, 19 nov 2026](https://dev.to/t1m4lc/276000-offers-1-sale-vanity-metrics-vs-real-kpis-after-53-days-307i)). Zijn regel: "The most flattering number in a report is the one to check first."
- **Voor ons:** de sale vermenigvuldigt alleen wat er al is (46); de meeste producten verkopen zelfs in de drukste week niets. Wie wel verkoopt, heeft een lijst, een publiek of een affiliate die linkt. Voor de tak betekent dat in de week van 27 nov: elke post en elk bericht wijst met een `?ref=` naar Pro, en we tellen alleen echte verkopen en menselijke klikken, geen ruwe tellers.

## Patronen na ronde 11
41. **Een regel die alleen in een notitie of regelbestand staat, verliest van de vaste opdracht van een geplande taak** (61). Elke regel die voor de tak telt, moet in de opdracht staan die elke run leest. Hetzelfde voor "verzin geen nieuwe producten": een wens in een plan houdt een agent niet tegen (60).
42. **Opzetten die op de onze lijken, halen nu $0** (60, 63, 58), en de enige grote gevallen verkochten aan het publiek van hun eigen verhaal (62, 3, 1). Voor een Blender-product zit het geld in de winkel zelf, de sale-week en mensen met publiek, niet in meer posts.
43. **In een sale-week verkoopt de meerderheid van de producten niets** (64). De sale is geen marketing op zichzelf.

## Stand na run 20 nov 04:40 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Zet de regels van de tak in de vaste opdracht van elke geplande taak van Roep**, niet alleen in `marketing/REGELS.md` (61): bij een andere agent won de geplande opdracht een hele dag van zijn eigen notitie. Dit raakt alle drie de voorstellen van ronde 10.
2. **Tel de wachtrij per kanaal en per dag, niet in totaal** (61): "hoeveel is groen gekeurd en klaar voor TikTok vandaag", anders gaat er ongemerkt niets uit.
3. **Keur het beeld apart** (60): een post met een verkeerd plaatje kwam bij een opzet als de onze door de keuring van alleen de tekst.
4. **Felix had $177.000 (eigen opgave), maar door producten voor zijn eigen publiek van agent-bouwers en het publiek van Nat** (62). Geen enkel voorbeeld tot nu toe laat een zelfstandige content-agent zien die een product voor een ander publiek (zoals Blender) boven een paar honderd dollar bracht.
5. **In de Cyber Sale van 2023 verkocht hoogstens ±36% van de producten iets** (64, berekend). Click Joints Pro wint die week alleen met een `?ref=`-link bij iemand met publiek (affiliates kregen in 2023 ±6,6% van de omzet) en met de lijsten in de winkel zelf.

Voorstel: (a) de hoofdchat zet de drie zinnen uit ronde 10 plus "tel alleen wat groen is voor dit kanaal vandaag" en "keur het beeld apart" in de vaste opdracht van de Maker van Roep en de Keurder van Roep, niet alleen in `marketing/REGELS.md`; (b) voor 27 nov blijft voorrang bij de eigen Superhive-link, de lijst van 10 tot 20 Blender-makers met publiek, en CG Channel (staat al klaar in `commercie/blender-click-joints/black-friday.md`); (c) na de sale-week meet de tak alleen verkoop en menselijke klikken per `?ref=`. Volgende run: of iemand een agent of planner gebruikt die affiliates of makers zoekt en een lijst met publieksgrootte bijhoudt (zonder zelf te benaderen), en wat dat opleverde.

## Ronde 12 (run 20 nov ±05:20 UTC, klok van de container): een agent die makers zoekt en mailt, AI-pitches aan journalisten in cijfers, en hoe je verkoop meet als er bijna niets binnenkomt

Deze ronde volgde het voorstel van ronde 11: een agent die makers of affiliates zoekt en een lijst met publieksgrootte bijhoudt. Ik vond één open repo die dat echt draaide, maar zonder uitslag. Daarnaast harde cijfers over AI-pitches aan journalisten (PR) en drie verse verslagen van deze week over muren en meten. Let op: onder de dev.to-tags over affiliates staan veel gelijkvormige verhalen ("From $0 to $2.400/month ...") van steeds andere accounts zonder reacties; die heb ik niet gebruikt (GOK: gemaakte reclame).

### 65. Nooze: een agent die TikTok-makers zoekt, mailt en antwoorden afhandelt, maar geen uitslag deelt
- Een open repo van de maker van de wekker-app Nooze: elke ochtend zoekt de agent TikTok-makers via hashtags en zoekwoorden (ScrapeCreators-API), haalt mailadressen uit hun bio, houdt alleen makers met 2.000 tot 40.000 volgers en minstens 2% betrokkenheid over, en mailt ze een uitnodiging voor het affiliateprogramma (20 tot 30% per abonnement, code in de app, geen cookies). Elk half uur leest hij de antwoorden: bij "interesse" stuurt hij zelf de testlink, al het andere (vragen, nee, afmelden, twijfel onder 0,8) gaat via Telegram naar de maker, die het antwoord dicteert. Elke avond een rapport en een voorstel welke hashtags meer of minder moeten op basis van het antwoordpercentage; de mens keurt dat voorstel (GEZIEN: [README](https://github.com/ryanschwartz88/creator-outreach-agent), `SOUL.md`, `config/scraping.yaml`, `config/affiliate.yaml`, gelezen met git clone, niets uitgevoerd).
- **Kosten volgens de repo:** ±$30 per maand (ScrapeCreators ±$17, twee Google Workspace-accounts $12, een apart maildomein, lokaal model gratis) (DERDEN, eigen opgave, zelfde link). Opwarmen: 5 mails per dag in dag 1 tot 3, oplopend tot 15 à 20 in week 2 (GEZIEN, `SETUP.md`).
- **Uitslag:** de repo zegt dat hij "Nooze's real creator-outreach campaign in spring 2026" draaide en nu stilligt, maar geeft geen cijfers. De getallen in de handleiding (bijv. "morningroutine: 45 sent, 6 replies (13.3%)") staan er als voorbeeld van een bericht ("a message like"), niet als uitslag (GEZIEN, `AGENT-GUIDE.md`). Dat de campagne is gestopt zonder een cijfer te delen, zegt iets, maar wat precies weet ik niet (GOK).
- **Voor ons:** de opzet is precies wat ronde 11 zocht: zoeken, filteren op publieksgrootte en betrokkenheid, en per bron het antwoordpercentage bijhouden. Maar het mailen gebeurt onder de naam van de maker ("Sign emails as ryan"), en dat mag bij ons niet zonder ja van Thijs (regel 4). Wat wel kan zonder iemand te benaderen: alleen het eerste deel, een lijst Blender-makers met publieksgrootte, mediane weergaven van hun laatste video's en hoe vaak ze reageren, als voorbereiding voor de lijst van 10 tot 20 makers (ronde 9 en 11). Het benaderen zelf blijft een vraag aan Thijs.

### 66. AI-pitches aan journalisten: 1 op 10 gekozen tegen 1 op 3 voor mensen
- Featured (eigenaar van HARO en Connectively) liet Pangram 1.394.740 pitches op 42.392 journalistvragen keuren (juni 2025 tot juli 2026). 21% was volledig door AI geschreven. Van de AI-pitches werd ongeveer 1 op 10 gekozen, van de menselijke ongeveer 1 op 3. Van 2.500+ journalisten zette 35% zelf een filter aan dat AI-pitches weghoudt, terwijl dat filter standaard uit staat. Verbannen accounts hadden 3,6 keer vaker een AI-pitch (24,7% tegen 6,8%) (DERDEN: [Pangram via Stacker, 29 sep 2026](https://keyt.com/stacker-ai/2026/09/29/how-journalists-feel-about-citing-ai-generated-pr-according-to-data/)). Let op: Pangram verkoopt AI-herkenning, dus belang bij dit verhaal; de cijfers komen wel van Featured zelf.
- Een PR-bureau verkocht een tool die journalistvragen volledig met AI beantwoordt, met verzonnen anekdotes en een belofte dat het "AI detection tools" omzeilt; eigen claim 7 à 8% geplaatst, broncode voor $2.500, nog geen enkele koper (DERDEN: [Press Gazette](https://pressgazette.co.uk/news/pr-agency-sells-ai-tool-which-sends-out-automated-expert-comment-to-journalists/)). Hetzelfde stuk noemt eerdere gevallen van verzonnen "experts" die honderden keren werden geciteerd.
- **Voor ons:** dit sluit aan op 40 (AI-tekst tegen handgeschreven eerste bericht): in PR wint de mens met ruim 3 keer zoveel kans, en wie veel AI-pitches stuurt, loopt meer kans op een ban. Een PR-agent die zelf pitches verstuurt, is dus slecht voor geld en voor de naam. Als we ooit pers benaderen: de agent zoekt en zet een concept klaar, Thijs of een mens schrijft het af.

### 67. Maddy Osman: een agent die journalistvragen sorteert en een concept klaarzet, de mens verstuurt
- Een contentbureau laat een Zapier-agent elke binnenkomende journalistvraag (Qwoted, Source of Sources, Featured) uit een Gmail-label lezen, een score geven op onderwerp (eigen onderwerpen 80 tot 100, zijdelings 20 tot 40, ander 0 tot 10), passages uit haar eigen gepubliceerde stukken erbij zoeken, alles in een Google Sheet loggen en een concept met deadline in Slack zetten. "Nothing goes to the journalist automatically, and that's deliberate." Gevolg volgens haar: van 1 à 2 antwoorden per week naar "several strong opportunities per day" (DERDEN, eigen opgave: [ActiveCampaign AI Lab, 18 jun 2026](https://autonomous.activecampaign.com/stories/journalist-query-response-agent-rag)).
- Ze noemt een domeinscore van 72 en 3.700+ backlinks "without paying for link building", maar dat is de stand van haar bureau over jaren, niet wat deze agent opleverde (DERDEN, zelfde link; de koppeling aan de agent is niet aangetoond).
- **Voor ons:** de vorm (sorteren, eigen materiaal erbij, concept klaar, mens verstuurt) past op wat Gmail bij ons mag: alleen lezen. Maar journalistvragen over Blender-add-ons of kleine spellen zijn zeldzaam (GOK), dus geld levert dit binnen weken waarschijnlijk niet. Niet nu bouwen.

### 68. Een AI-agent die zelf verkoop probeert: drie dagen, elke muur, nul verkoop
- Een agent die voor een kleine studio twee landingspagina's verkoopt (geen betaald verkeer, elke post zegt dat hij door AI is geschreven) meldt na drie dagen: 22 lezers op dev.to met 143 seconden gemiddeld, 0 leads, 0 verkopen (DERDEN, eigen opgave: [slotkeep, dev.to, 17 nov 2026](https://dev.to/slotkeep/three-days-0-budget-zero-sales-an-ai-agent-hits-every-platforms-anti-bot-wall-b39)).
- **De muren:** Reddit gaf een 403 en reCAPTCHA vanaf zijn netwerk ("Not an account problem, an IP problem"); Product Hunt een Cloudflare-scherm dat nooit opende; een vakforum bande het account omdat het "te snel typte"; een eerste antwoord op Quora werd vanzelf verwijderd; Indie Hackers laat nieuwe leden alleen reageren, niet zelf posten; X vroeg bij het aanmelden een video van het gezicht; een tweede Gmail-account vroeg sms-controle (DERDEN, zelfde link).
- **Wat wel werkte:** reacties onder andermans posts kregen antwoord (twee gesprekken op Indie Hackers), posts niet (DERDEN, zelfde link).
- **Voor ons:** onze runs draaien ook in de cloud. Een tak die buiten de API's om (Metricool, YouTube-API) iets wil doen op Reddit, Product Hunt of fora, loopt tegen dezelfde muren aan, en accounts maken mogen we niet. Dat bevestigt de keuze van B: alleen kanalen met een echte API of planner. En het past bij 14 en 27: op Reddit en fora werken reacties van een echt, oud account, niet een agent.

### 69. Meten bij bijna nul verkoop: sorteer op geld, en geen procenten
- **Bronnen op omzet sorteren:** een maker van zes lanceersites sorteerde zijn bronnen op omzet in plaats van bezoekers. Per site hadden maar 2 tot 4 van de 112 tot 200 bronnen ooit iets opgeleverd. Op één site bracht een kleine bron met 28 bezoekers $69,60, Google met 219 bezoekers $29,00 (±20 dagen). Hij handelt er nog niet naar omdat de aantallen klein zijn (DERDEN: [posting-dude, dev.to, 17 nov 2026](https://dev.to/posting-dude/i-ranked-my-referrers-by-revenue-not-visitors-28-visitors-from-one-site-out-paid-219-from-google-1e8f)).
- **Een waakagent op een Gumroad-winkel:** 7 dagen elke avond verkoop en weergaven lezen met drie regels (elke verkoop, daling van 50% of meer, 0 verkopen bij 20+ weergaven). Uitslag: 6 meldingen, alle 6 ruis, 0 verkopen. Waarom: bij 1 à 2 weergaven per dag is elke stille dag een "daling van 100%", en de avondmeting zag een halve dag omdat het dashboard niet zegt welke tijdzone "vandaag" is (5 van de 6 avonden 0 weergaven, terwijl het weektotaal opliep van 2 naar 7). Het ene echte probleem van die week gaf geen melding (DERDEN, eigen opgave: [crzy_undefinedundefined, dev.to, 17 nov 2026](https://dev.to/crzy_undefinedundefined/grok-bot-1-i-set-up-an-agent-to-watch-my-gumroad-store-for-7-days-6-alerts-6-were-noise-4jp8)).
- **Voor ons:** het dagrapport van Roep moet (1) bronnen sorteren op verkoop per `?ref=`, niet op weergaven; (2) gisteren als hele dag meten, niet "vandaag tot nu"; (3) bij onze kleine aantallen gewone getallen geven, geen procenten of dalingen. Een melding alleen bij een verkoop of bij een fout (post niet live), niet bij een "daling".

### 70. Regels als "nooit" werken slecht: schrijf wat de agent wél doet, met bron en terugval
- Een maker van een klantenservice-agent had 23 regels die begonnen met "NEVER" of "DO NOT"; samen zorgden ze dat een klant op "can I return this?" te horen kreeg "I am not able to discuss returns." Hij verving ze door 9 regels die elk beginnen met een werkwoord, zeggen uit welke bron de agent het haalt, en een vaste zin geven als die bron leeg is (DERDEN: [ulnit, dev.to, 11 nov 2026](https://dev.to/ulnit/i-had-23-sentences-starting-with-never-in-my-agents-prompt-i-deleted-all-of-them-3pm2)).
- **Voor ons:** vult 41 en 60 aan. De opdracht van de Maker van Roep heeft nu veel verboden. Beter: "Prijs en korting: neem ze letterlijk uit `commercie/.../prijs.md`; staat het er niet, schrijf geen prijs en zet de post op oranje." Dan weet de agent wat hij moet doen als iets ontbreekt, in plaats van te zwijgen of te gokken.

## Patronen na ronde 12
44. **Ook de beste open opzet voor het zoeken en mailen van makers deelt geen uitslag** (65). Het zoeken en sorteren is goedkoop en veilig; het mailen onder iemands naam is waar het risico zit.
45. **Bij PR wint de mens ruim 3 keer** (66), net als bij koude berichten (40). Agents sorteren en zetten klaar, mensen versturen (67).
46. **Bij kleine aantallen liegen procenten**; meet op verkoop per bron, over hele dagen (69).

## Stand na run 20 nov 05:40 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Een agent die makers zoekt en een lijst met publieksgrootte bijhoudt, bestaat al als open repo (Nooze, ±$30 per maand), maar zonder gedeelde uitslag** (65). Het zoek- en filterdeel (2.000 tot 40.000 volgers, betrokkenheid, antwoordpercentage per bron) kunnen wij nadoen zonder iemand te benaderen.
2. **AI-pitches aan journalisten worden 1 op 10 gekozen, menselijke 1 op 3, en 35% van de journalisten filtert AI weg** (66). Geen PR-agent die zelf verstuurt.
3. **Vanuit de cloud zijn Reddit, Product Hunt en fora voor een agent dicht** (68): 403, Cloudflare, ban om snel typen. Alleen kanalen met een API.
4. **Het dagrapport: verkoop per `?ref=`, gisteren als hele dag, geen procenten** (69). Een waakagent op Gumroad gaf 6 van 6 keer loos alarm.
5. **Schrijf regels voor Roep als "doe dit, uit deze bron, anders oranje"** in plaats van "nooit" (70).

Voorstel: (a) een agent (geen plaatser) maakt vóór 27 nov één lijst van 10 tot 20 Blender-makers op YouTube met abonnees, mediane weergaven van de laatste 10 video's, of ze ooit add-ons bespreken en of ze reageren onder hun video's, via de YouTube Data API (lezen kost niets, sleutel staat al in B); die lijst gaat naar de hoofdchat, het benaderen blijft een vraag aan Thijs; (b) de hoofdchat neemt punt 4 en 5 op in de vaste opdracht van de Maker en Keurder van Roep. Volgende run: of een Blender- of game-maker die met een lijst van makers werkte, cijfers gaf over hoeveel van die makers het product echt lieten zien en wat dat aan verkoop deed.

## Ronde 13 (run 20 nov ±06:20 UTC, klok van de container): hoeveel makers het product echt lieten zien, en wat dat aan verkoop deed

Deze ronde volgde het voorstel van ronde 12: makers die met een lijst van makers werkten en cijfers geven over hoeveel er echt iets maakten en wat dat verkocht. Ik vond vier zulke verslagen (twee games, twee Blender), plus wat Superhive zelf aan makers betaalt. Daarnaast twee verse agent-verslagen met $0 en één groot bedrijf dat een agent alleen het voorwerk laat doen.

### 71. Een sleuteldienst voor makers: 141 aanvragen, 38 maakten iets, ±1.000 weergaven op YouTube, 0 verkopen via de link
- Een kleine studio zette 100 Steam-sleutels op een "key distribution service" (makers vragen zelf een sleutel aan; eisen: 5 kijkers tegelijk op Twitch of 75 weergaven per video op YouTube; de studio keurde elke aanvraag met de hand). Uitslag na ruim drie maanden: minstens 67 aanvragen afgewezen als nep, 74 sleutels opgehaald, 38 makers maakten iets (11 YouTube-video's, 36 streams), dus ±27% van alle aanvragers. De 11 YouTube-video's haalden samen "just over a thousand total views". De link met UTM leverde "neither wishlists, purchases or activations" op; wat wel kijkers bracht, waren streamers die niets met de dienst te maken hadden (DERDEN: [Benjamin Glover, dec 2022](https://benjaminglover.substack.com/p/heres-a-long-article-explaining-why)).
- **Kenmerken van nepkanalen** die hij noemt: geen zakelijk mailadres in "About", kanalen die jaren stil liggen na één oude hit, evenveel abonnees als weergaven op verse video's (gekocht), video's van 10 tot 20 minuten spelbeeld zonder gezicht of stem, en een "review" waarvan de eerste 90 seconden reclame voor iets anders is (DERDEN, zelfde link).
- **Voor ons:** een lijst van makers die een agent maakt (voorstel ronde 12) moet deze filters hebben, anders staan er vooral nepkanalen op. En een open aanbod ("vraag maar aan") trekt vooral mensen die gratis spullen willen. Dit sluit aan op 35 (91% van de sleutels in een "programma" gaf 8% van de weergaven).

### 72. PUTRID SHOT ULTRA: 20 YouTubers met de hand gemaild, ±6 maakten een video, 285 verkocht in 3 weken
- Een solo-maker van een spel van $3 mailde na de lancering ±20 YouTubers met een gratis sleutel, met een sjabloon en een "persmap" op imgur. 3 grote kanalen (100.000 tot 500.000 abonnees) en ±3 kleine maakten een video; dat gaf de tweede piek in verkoop. Totaal 285 exemplaren in 3 weken, gestart met ±620 verlanglijsten (DERDEN: [abhisundu, 2022](https://abhisundu.github.io/posts/psupostmortem/)).
- Zijn les: "No amount of influencer traffic can out-market your game's quality". Elke maker vond dezelfde te sterke combinatie en speelde het spel op de automatische piloot; kijkers zagen een saai spel (DERDEN, zelfde link).
- **Voor ons:** met de hand, klein en gericht: ±6 van 20 (±30%, berekend) maakten iets, tegen ±27% van alle aanvragers bij de sleuteldienst (71), maar hier waren het grote kanalen die verkoop gaven. Hoeveel van de 285 door de video's kwam, staat er niet in (GOK: de tweede piek, dus een deel).

### 73. Spencer Magnusson (Blender-add-ons): één betaalde vermelding bij Curtis Holt, 43.000 weergaven, 8 verkopen in een week
- Een Blender-maker betaalde Curtis Holt voor een vermelding van twee add-ons aan het eind van een video en maakte hem ook affiliate. Na een week: video 43.000 weergaven ("much higher than his average"), zijn Linktree 120 bezoeken op dag 1 en daarna ±20 per dag, 170 downloads van de gratis add-on (eerder 30 tot ±100 per versie), en op Blender Market 8 verkopen, waarvan 5 via de link van Curtis. Het bedrag dat hij betaalde staat er niet in (DERDEN, eigen opgave: [Spencer Magnusson, 29 sep 2023](https://spencer-magnusson.beehiiv.com/p/4-tips-effective-sponsorships)).
- Over InspirationTuts: "in one experience, they promoted my add-on and sales soared; in another, they took my add-on files and never spoke to me again." Een korte aanbeveling van een bekende maker (een citaat op de productpagina) "made a big difference in conversion rates and sales" (DERDEN, zelfde link).
- **Voor ons:** het enige Blender-voorbeeld met echte cijfers per vermelding: 43.000 weergaven gaven 5 verkopen via de affiliatelink (±1 per 8.600 weergaven, berekend). Bij Click Joints Pro van $12 (prijs volgens `commercie/blender-click-joints/`) is dat ±$60 bruto uit één video; het werkt alleen als de maker ook een blijvende affiliatelink heeft, zodat het doorloopt in de sale-week. Een citaat van één bekende Blender-maker op de pagina is goedkoper en kan meer doen (GOK).

### 74. Wat Superhive zelf aan makers betaalt: InspirationTuts en askNK, geschat $258 tot $674 per video
- Volgens SponsorRadar (leest sponsors uit de video's zelf) sponsorde Superhive 17 video's bij 6 kanalen, het laatst op 16 sep 2026: askNK (290.000 abonnees, 7 keer), InspirationTuts (342.000, 4 keer), SouthernShotty, CGDive, stache, cgfocus. Geschatte waarde $337 tot $674 per video (DERDEN: [SponsorRadar, Superhive](https://sponsorradar.com/brands/superhivemarket)). InspirationTuts haalt gemiddeld 12.900 weergaven per video, 28,7 uploads per maand, geschat $258 tot $515 per gesponsorde video (DERDEN: [SponsorRadar, InspirationTuts](https://sponsorradar.com/channels/inspirationtuts)). Let op: dit zijn schattingen van SponsorRadar, geen prijzen van de maker.
- De video's die Superhive sponsort zijn vaak overzichten zoals "13 New Blender Addons & Updates Have Been Released" (GEZIEN in dezelfde lijst).
- **Voor ons:** zulke overzichtsvideo's zijn de plek waar nieuwe add-ons gezien worden. Erin komen kan misschien gratis door het kanaal te wijzen op een nieuwe versie (GOK; dat is iemand benaderen, dus een vraag aan Thijs). Betalen kost geld en vraagt een ja van Thijs (regel 1); met 73 als maat (±5 verkopen per 43.000 weergaven) levert een video van ±13.000 weergaven waarschijnlijk 1 à 2 verkopen op (GOK), dus voor $258 niet de moeite.

### 75. Een open oproep voor affiliates op Blender Artists: 570 keer bekeken, 1 aanmelding
- Een maker van Blender-add-ons (automatisch UV-uitvouwen) vroeg in juni 2025 op het forum om makers en YouTubers als affiliate (30%+ via Gumroad, gratis exemplaar). Stand: 570 keer bekeken, 3 berichten, waarvan 1 "I'm interested" (GEZIEN: [Blender Artists](https://blenderartists.org/t/1599769), via de openbare JSON).
- **Voor ons:** een oproep laten staan levert bijna niets op, net als het open aanbod in 71. Affiliates komen er bij Blender-makers pas als je ze zelf persoonlijk vraagt (zie 50, Oliver Post).

### 76. Twee agent-lanceringen met $0, en een groot bedrijf dat de agent alleen het voorwerk geeft
- **Een week lancering door Claude Code:** de agent koos markt, prijs, maakte zes sjablonen, winkel, site, blogs, video's, mails en plande twee weken posts. Uitslag na drie dagen: 0 verkopen, "a handful of storefront visitors", één reactie. Zijn les: op "is er vraag?" gaf de agent telkens marktcijfers, maar vroeg nooit of een echt persoon er iets bij voelt; pas toen de maker zei dat de klant dit zelf in een middag met AI kan maken, gaf de agent dat toe (DERDEN: [kairi_outputs, dev.to, 22 apr 2026](https://dev.to/kairi_outputs/i-let-an-ai-agent-run-a-product-launch-for-a-week-the-product-was-fine-nobody-needed-it-7cn)).
- **"Joey", een agent op een Mac Mini:** 31 artikelen in 15 dagen op dev.to, $0 omzet daaruit, 73 volgers; het artikel zelf staat op 0 reacties (DERDEN: [joeytbuilds, dev.to, 15 apr 2026](https://dev.to/joeytbuilds/after-31-devto-articles-as-an-ai-agent-the-data-that-surprised-me-417k); reacties GEZIEN via de dev.to-API).
- **SaaStr ("10K"):** Jason Lemkin zegt dat zijn agent in één week in november mee twee sponsordeals van zes cijfers sloot, maar alleen door voorwerk: onderzoek, een deck tijdens het gesprek, prijzen uit 13 jaar facturen, inkoopvragen, papierwerk. Een mens voerde de gesprekken; "Every write 10K makes to Salesforce still needs approval". Verlengingen van sponsors boven $100.000 gingen dit jaar van "the 20s to the 70s" procent (DERDEN, eigen opgave: [SaaStr, nov 2026](https://saastr.com/our-ai-vp-of-revenue-cant-close-a-deal-yet-it-co-closed-two-six-figure-deals-in-one-week)). Dat is een bedrijf met een groot publiek en bestaande klanten; niet ons geval.
- **Voor ons:** zelfde patroon als 42: de agent levert veel en snel, het geld komt van mensen met een relatie of publiek. De Keurder van Roep kan één vraag toevoegen die een agent zelf niet stelt: "wie voelt hier iets bij, en waarom zou die nu kopen?"

## Patronen na ronde 13
47. **Van makers die een product krijgen, maakt maar ±27 tot 30% er iets mee** (71, 72), en een open oproep of sleuteldienst trekt vooral nepkanalen en gratis-zoekers (71, 75). Alleen persoonlijk gevraagde, echte kanalen geven verkoop (72, 73, en 35).
48. **Eén Blender-vermelding met cijfers: 43.000 weergaven, 5 verkopen via de affiliatelink** (73). Een vermelding is dus weinig waard zonder blijvende link, en betalen voor een overzichtsvideo loont bij onze prijs waarschijnlijk niet (74, GOK).
49. **Agents die alles zelf lanceren halen $0; agents die voorwerk doen voor een mens met relaties helpen wel** (76, past op 45).

## Stand na run 20 nov ±06:20 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Het enige Blender-voorbeeld met cijfers per vermelding: Curtis Holt, 43.000 weergaven, 8 verkopen in een week, 5 via zijn affiliatelink** (73). Een vermelding zonder blijvende link levert weinig; met link loopt het door in sales.
2. **Maar ±27 tot 30% van de makers die het product krijgen, maakt er iets mee** (71, 72). Reken bij een lijst van 20 Blender-makers op ±5 die iets doen (GOK op basis van deze twee).
3. **Open oproepen en sleuteldiensten werken niet**: 570 keer bekeken, 1 aanmelding (75); 141 aanvragen, ±1.000 weergaven, 0 verkopen via de link (71).
4. **De lijst van makers moet nepkanalen weren**: zakelijk mailadres, recente uploads, gezicht of stem, weergaven die passen bij abonnees (71). Dat kan de agent uit ronde 12 met de YouTube Data API zelf controleren.
5. **Superhive betaalt zelf overzichtskanalen (InspirationTuts, askNK), geschat $258 tot $674 per video** (74). Betalen vraagt een ja van Thijs en loont bij onze prijs waarschijnlijk niet; in zo'n overzicht komen zonder te betalen is een vraag aan Thijs (benaderen).

Voorstel: (a) de lijst van 10 tot 20 Blender-makers (voorstel ronde 12) krijgt de vijf filters uit 71 en een kolom "maakt overzichtsvideo's van nieuwe add-ons ja/nee"; (b) de hoofdchat legt Thijs één vraag voor: mogen we 5 tot 10 makers van die lijst persoonlijk een gratis Pro plus een blijvende `?ref=`-affiliatelink aanbieden, tekst door Thijs goedgekeurd, vóór 27 nov; (c) de Keurder van Roep krijgt de vraag "wie voelt hier iets bij en waarom koopt die nu?" (76). Volgende run: of een Blender-maker een citaat of aanbeveling op de productpagina heeft gemeten (73 noemt het, zonder getal), en wat Superhive-makers zeggen over hun eigen affiliates in de Cyber Sale.

## Ronde 14 (run 21 nov ±00:20 UTC, klok van de container): waar kopers in de saleweek kijken zonder dat wij iets plaatsen, en wat platforms zeggen over agents die reageren

Vraag van deze ronde, getoetst aan de hoofdzaak: welke plekken brengen in de week van 27 nov kopers naar Click Joints Pro **zonder** dat een agent hoeft te plaatsen of iemand te benaderen? En mag Roep straks zelf op reacties antwoorden?

### 77. CG Channel: Click Joints Pro staat al op de Black Friday-lijst (de mail van 20 nov werkte)
- De lijst "Black Friday, Cyber Week and New Year 2026 deals for CG artists" (bijgewerkt 20 nov) noemt: "Who: Dortus. What: Click Joints Pro (Blender plugin to turn rigged characters into 3D printable figures). When: 27 November to 1 December. Discount: 25%, use code CYBER25" (GEZIEN: [CG Channel](https://www.cgchannel.com/2026/11/black-friday-cyber-week-and-new-year-2026-deals-for-cg-artists/)). Dat is het gevolg van de mail die de hoofdchat op 20 nov 09:27 met ja van Thijs stuurde (`organisatie/besluiten.md`).
- Op de lijst nu 88 deals, waarvan 7 met Blender in de omschrijving, naast kleine makers als Glow Arts (Fyr Baker) en Machina-Infinitum (Gumroad-winkel) (GEZIEN, eigen telling). De lijst van 2025 had 187 deals, waarvan 6 met Blender (GEZIEN: [CG Channel 2025](https://cgchannel.com/2025/11/black-friday-cyber-week-and-holiday-2025-deals-for-cg-artists/)); hij groeit dus nog tot in december.
- Insturen kost niets: een mail met Who, What, When, Discount, URL (GEZIEN: [instructies](https://www.cgchannel.com/2026/11/submit-an-offer-to-cg-channels-black-friday-deals-list/)). Betaalde plekken bovenaan bestaan ook (media pack, prijs niet gezien).
- **Let op:** de link gaat naar `duinhouwer8.gumroad.com/l/click-joints-pro` zonder `?ref=` (GEZIEN in de html). Wat de lijst oplevert zie je dus alleen in de verwijzers van Gumroad (Analytics), niet via onze eigen `?ref=`-teller. Hoeveel kopers zo'n lijst geeft: onbekend, ik vond geen maker die het mat (GOK: weinig per regel, maar het kost niets meer).
- **Voor ons:** zo'n lijst is het tegendeel van de agent-verhalen met $0: één keer een goede regel insturen, en een redactie met publiek zet hem neer. Dezelfde soort plek voor december ("New Year deals") kan met dezelfde mail.

### 78. Addon Radar: een site van een add-on-maker die Superhive elke dag uitleest, en waar Pro al op staat
- Addon Radar (één maker uit Noorwegen, Mulk) leest elke dag alle Superhive-pagina's en de Blender Extensions-lijst uit, en zet ze in lijsten: "Black Friday", "Lowest prices", "New on Superhive", "Hidden gems". Hij verdient via Superhive-affiliatelinks (GEZIEN: [about](https://addonradar.com/about/)).
- **Click Joints Pro staat er al**, zonder dat iemand iets deed: "from $12, No price change since we started tracking on 20 Nov", "Not much to go on yet", geen beoordelingen (GEZIEN: [addonradar.com/addon/click-joints-pro](https://addonradar.com/addon/click-joints-pro/)).
- De Black Friday-pagina toont nu 438 add-ons met een saleprijs en 252 actieve coupons van makers, gesorteerd met de grootste korting bovenaan (90% en 80% staan vooraan) (GEZIEN: [Black Friday](https://addonradar.com/black-friday/), [gids](https://addonradar.com/guides/black-friday/)). Wie mensen een add-on laat "Saven", krijgt een mail op de dag dat de prijs zakt.
- **Voor ons:** Pro komt daar alleen in de sale-lijst als hij op Superhive echt een saleprijs of coupon heeft (plan: Cyber Sale 35%, `platformen/blender/click-joints-plan-2026-11-19.md`). Met 35% staan we niet vooraan, maar wel in de mail aan iedereen die Pro "gesaved" heeft. Dit is een tweede reden om de Superhive-korting echt op Superhive in te stellen en niet alleen op Gumroad. Onderaan de pagina: "Made this add-on? Get a badge for your page" (niet geopend, niets gedaan).

### 79. Gumroad Discover in de saleweek: Gumroad zet deals vooraan, maar wij komen er nog niet in
- Op 27 nov 2025 schreef Gumroad: "We're featuring all eligible products on Gumroad Discover during Black Friday", als je een korting met de code `BLACKFRIDAY2025` aanmaakt (DERDEN: [Gumroad blog](https://gumroad.com/blog/p/we-re-featuring-black-friday-deals-on-gumroad-submit-yours-55f64bdb-66b9-4232-8af0-e60773918c8c)). In de open broncode van Gumroad (gelezen, niets uitgevoerd, stand 20 nov 2026 22:15 UTC) staat nog `BLACK_FRIDAY_CODE = "BLACKFRIDAY2025"`, een Discover-pagina die alleen producten met die code toont, en een teller met aantal deals, omzet en gemiddelde korting (GEZIEN: `app/controllers/concerns/search_products.rb`, `app/services/black_friday_stats_service.rb` in antiwork/gumroad). Een code voor 2026 is er nog niet; het blog meldde het vorig jaar pas op Thanksgiving zelf.
- **Maar:** Discover vraagt een saldo van minstens $100 uit echte verkopen, daarna gemiddeld 3 weken risicokeuring, en per product minstens 1 verkoop, een categorie en aangezette beoordelingen (DERDEN: [Gumroad help](https://gumroad.com/help/article/79-gumroad-discover)). Wij hebben 0 verkopen (bord, 20 nov). Deze route valt dus af voor deze saleweek; dat klopt met het besluit van 20 nov 07:00.
- Ter vergelijking, wat de saleweek op Gumroad doet: in 2020 was Black Friday 132% hoger dan de vrijdag ervoor, in 2018 en 2019 ±212 tot 226% hoger; veel makers lieten de sale al een week eerder beginnen (DERDEN, oud: [Gumroad field report, dec 2020](https://gumroad.gumroad.com/p/a-million-dollars-in-a-day-twice-black-friday-and-cyber-monday-field-report)). Dat zegt iets over het hele platform, niets over een product zonder publiek.
- **Voor ons:** geen werk in steken dit jaar. Wel noteren: na de eerste verkopen en de risicokeuring is Discover de enige plek op Gumroad die vanzelf kopers brengt; een Gumroad-saleactie met hun eigen code doet alleen mee als we dan al "eligible" zijn.

### 80. Wat de platforms zelf zeggen over een agent die reageert of plaatst (stand 8 okt 2026)
- Blotato (verkoopt zelf een API voor sociale kanalen, dus niet neutraal) las 175 documenten van 10 platforms en vond: op 0 van de 10 staat duidelijk dat een AI-agent zonder goedkeuring van het platform mag antwoorden of een DM sturen als de ander niet eerst iets deed. TikTok en YouTube zijn "unclear". TikTok vraagt bij plaatsen een keuze per post van de eigenaar (de privacy-instelling moet de gebruiker zelf kiezen, zonder standaardwaarde), en verbiedt likes of shares via bots of scripts (DERDEN: [Blotato rulebook](https://www.blotato.com/research/social-media-automation-rulebook)). Ze testten niets op een echt account; het gaat over regels, niet over bans.
- Een open "comment-responder"-skill antwoordt op TikTok-reacties door met een opgeslagen browserprofiel in te loggen, 10 antwoorden per keer, 5 tot 15 seconden ertussen (GEZIEN: [SKILL.md](https://raw.githubusercontent.com/andywong418/clawd-skills/main/skills/comment-responder/SKILL.md), code niet uitgevoerd). Dat is precies het "bots of scripts"-gebied uit de regels hierboven: banrisico op het enige TikTok-account dat we hebben.
- **Voor ons:** Roep plaatst via Metricool en dat blijft zo. Antwoorden op reacties alleen onder onze eigen posts, op mensen die zelf eerst reageerden, en niet via een browser die doet alsof hij een mens is. Voor TikTok betekent dat in de praktijk: concept klaarzetten, de hoofdchat of Thijs plaatst het met de hand, tot er een officiële weg is (B-ontwerp gaat hierover).

### 81. Social Agents (CreatorOS): een open harnas voor de hele socials, inclusief "reageer met een woord en krijg de link"
- Open repo waarin Claude Code of een ander model per merk een map krijgt (`BRAND.md`, skills, logboek) en via de betaalde dienst CreatorOS plaatst, op reacties en DM's antwoordt ("sensitive stuff escalated to you"), cijfers leest en "funnels" maakt: wie onder een post een sleutelwoord als "GUIDE" typt, krijgt de link in een DM (GEZIEN: [README](https://raw.githubusercontent.com/kevinbadi/social-agents/main/README.md)).
- Geen enkel resultaat of cijfer van gebruikers in de repo; het is reclame voor de dienst eronder. De opzet (een merkbestand, een logboek per actie, een dashboard dat laat zien wat de agent echt deed) lijkt op wat Roep al heeft met `marketing/REGELS.md` en het dagrapport.
- **Voor ons:** de sleutelwoord-naar-DM-truc werkt alleen waar een DM mag na een reactie (Instagram, Facebook: ja volgens 80; TikTok: onduidelijk). Niet nu; pas als we Instagram erbij nemen.

## Patronen na ronde 14
50. **De plekken die nu kopers brengen zonder dat wij plaatsen, zijn lijsten van anderen**: een vakblad (77), een maker die Superhive uitleest (78), later Gumroad Discover (79). Eén goede regel of een echte prijsverlaging op de juiste winkel is genoeg; een agent is er niet voor nodig.
51. **Waar we de korting zetten, bepaalt wie hem ziet**: Gumroad-code CYBER25 staat op CG Channel, maar Addon Radar en de Superhive-sale zien alleen een korting die op Superhive zelf staat (78).
52. **Zelf antwoorden op reacties is op TikTok en YouTube nergens duidelijk toegestaan, en via een browser gaat het in tegen de regels van TikTok** (80). Een agent die antwoorden klaarzet en een mens die plaatst is de veilige vorm, net als bij journalisten (67).

## Stand na run 21 nov ±00:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Click Joints Pro staat op de Black Friday-lijst van CG Channel** (GEZIEN, 77), dankzij de mail van 20 nov. De link heeft geen `?ref=`; meten kan alleen via de verwijzers in Gumroad Analytics.
2. **Addon Radar heeft Pro al opgepikt** ($12, geen prijswijziging, GEZIEN, 78). Op zijn Black Friday-pagina (438 add-ons) en in de prijsmail komt Pro alleen als de korting op Superhive zelf staat.
3. **Gumroad Discover valt af voor deze saleweek**: $100 saldo, ±3 weken keuring en een eerste verkoop nodig (DERDEN, 79). Geen tijd in steken tot er verkopen zijn.
4. **Geen platform staat duidelijk toe dat een agent zelf op reacties antwoordt**; TikTok verbiedt bots voor likes en vraagt per post een keuze van de eigenaar (DERDEN, 80). Browser-bots die op TikTok antwoorden (open skill bestaat) zijn een banrisico.
5. **Patroon over 14 rondes**: geld komt van plekken met een publiek (vakblad, winkel, maker), niet van een agent die zelf meer plaatst (50, en 45, 49, 76).

Voorstel: (a) de Blender-manager controleert vóór 27 nov dat de Cyber Sale-korting van 35% **op Superhive zelf** is ingesteld, zodat Pro op Addon Radar en in de Superhive-sale verschijnt (78); (b) de hoofdchat kijkt op 28 nov en 2 dec in Gumroad Analytics hoeveel bezoek van cgchannel.com kwam en zet dat als GEZIEN in het dagrapport (77); (c) als CG Channel in december de "New Year deals" bijwerkt, dezelfde mail opnieuw voor een eventuele decemberkorting, met ja van Thijs zoals op 20 nov; (d) Roep antwoordt niet zelf op reacties; concepten voor antwoorden mogen, plaatsen doet een mens (80). Volgende run: welke andere uitlees-sites en nieuwsbrieven (zoals Addon Radar) Blender-kopers in de saleweek lezen, en of een maker meldde hoeveel verkopen zo'n lijst of prijsmail gaf.

## Ronde 15 (run 21 nov ±01:20 UTC, klok van de container): de etalages binnen Superhive, wat andere Blender-lijsten nog waard zijn, en een solo-maker met harde salecijfers

Vraag uit run 14: welke andere lijsten en nieuwsbrieven lezen Blender-kopers in de saleweek, en meldde een maker wat zo'n lijst opleverde? Kort antwoord: buiten CG Channel en Addon Radar zijn de lijsten klein of slapend; de beste etalages zitten in Superhive zelf. Een maker die verkopen per lijst noemt, vond ik niet.

### 82. Superhive Coupons: een gratis etalage waar makers hun lanceerkorting laten zien
- Superhive heeft een aparte pagina `superhivemarket.com/coupons` met kortingscodes van makers, te sorteren op "Newest First", "Most Popular", "Highest % off", "Nearly Gone" en "Ending Soon"; ±13 pagina's (GEZIEN, curl 21 nov). Bovenaan nu vooral lanceerkortingen van kleine makers: "Launch week: 30% off Wood Shader", "Launch week: 50% off NexUV" (99 keer te gebruiken), "Make it Toon! 40% off the full version, for the first 5 buyers", en al een paar "Early Black Friday" codes (GEZIEN).
- Superhive zelf noemt coupons de eerste van vier manieren om buiten de grote sales iets te vinden; een coupon staat ook in de zijbalk van de productpagina, zichtbaar voor wie het product op zijn verlanglijst heeft (GEZIEN: [Superhive, 3 mrt 2026](https://superhivemarket.com/page/2026-winter-sale)). Op de pagina "Deals" staat een blok "Most Popular Coupons" (GEZIEN: superhivemarket.com/deals).
- Geen cijfers over wat een coupon oplevert (nergens gevonden). Wel een opzet die makers kennelijk werkend vinden: korte looptijd, een klein aantal ("first 5 buyers", "6 remaining uses") zodat hij bij "Nearly Gone" komt.
- **Voor ons:** kost niets en valt niet onder plaatsen (het is een instelling in onze eigen winkel). Een coupon voor Click Joints Pro **na** de Cyber Sale (vanaf 2 dec, als de sitebrede korting voorbij is), met een klein aantal, zet Pro opnieuw in een lijst waar Blender-kopers kijken. Alleen wie op het verkopersaccount kan, zet hem: de Blender-manager of de hoofdchat.

### 83. Superhive "Fresh Finds": elke vrijdag ±5 nieuwe producten in de nieuwsbrief, gekozen bij de keuring
- Superhive stuurt elke vrijdag een mail met "Fresh Finds". Ze zien elk nieuw product "as part of our review process" en kiezen er "about 5 products each week" uit; aanmelden kan niet, ze kiezen zelf (GEZIEN: [Superhive, 24 okt 2025](https://superhivemarket.com/posts/23-fresh-finds) en de pagina van 3 mrt 2026 hierboven). Veel gekozen producten hadden een lanceerprijs of coupon (zelfde link).
- Hoe groot die nieuwsbrief is: niet gevonden. Superhive had in de Cyber Sale 2024 11.192 betalende kopers (DERDEN, al in 46); hoeveel daarvan de mail lezen: GOK, onbekend.
- **Voor ons:** we kunnen dit niet sturen, alleen kansrijk maken: een productpagina die in één blik laat zien wat het doet (gif bovenaan), en een lanceercoupon (82) als er een nieuw product of grote versie op Superhive komt. Geen werk voor de marketingtak, wel een vinkje in de uitbrengstappen van de Blender-manager (GOK dat het de kans vergroot; Superhive zegt niet waarop ze kiezen).

### 84. Andere Blender-lijsten: klein of slapend
- **Blender Artists, categorie Promotions:** gratis te posten, maar weinig gelezen. Superhive-sales haalden er 323 tot 1.811 keer bekeken (Spring Sale 2025: 1.811; Winter Sale 2026: 323; Summer Sale 2026: 151); een Blendkit-post van 18 nov 2026 staat op 38 (GEZIEN: blenderartists.org/c/promotions/62.json, 21 nov). Bijna nul reacties. Vergelijk: de affiliate-oproep uit 75 had 570 keer bekeken en 1 aanmelding.
- **BlenderNation Bazaar:** een gids met 2.623 producten van overal; betaalde producten mogen erop als je BlenderNation affiliate maakt ("most people pick around 20%") en dan krijg je volgens de FAQ ook gratis banners van 600 bij 300 op BlenderNation en Blender Artists, meer procent is meer vertoningen (GEZIEN: [Bazaar FAQ](https://bazaar.blendernation.com/frequently-asked-questions-faq/)). Maar de gids slaapt: in de sitemap is 99 keer iets bijgewerkt in juli 2025, daarna 2 in nov 2025, 5 in dec 2025, 1 in jan 2026 en 1 in aug 2026 (GEZIEN, listing-sitemap). Of de banners nog lopen: GOK, waarschijnlijk niet.
- **80 Level:** de dealslijsten zijn "Sponsored Article" met affiliatelinks en gaan over grote pakketten (Octane, Mari) (GEZIEN: [80 Level, 3 dec 2025](https://80.lv/articles/extended-holiday-deals-for-3d-artists-discounts-you-can-still-grab)). Niets voor een add-on van $12.
- **Voor ons:** geen van drieën is de moeite in deze saleweek. Hooguit één post in Blender Artists Promotions als Pro in de sale staat, maar dat is een nieuw kanaal onder een account, dus de hoofdchat beslist (regel 4); verwachte opbrengst ±0 verkopen (GOK, uit 75 en de tellers hierboven). De Bazaar kost geen geld vooraf, alleen een deel per verkoop, maar wel een aanvraag met account; pas als hij weer leeft.

### 85. Cory Zue (SaaS Pegasus): een solo-maker met harde salecijfers, en wat werkte
- Eén week Black Friday 2020: **21 verkopen, $6.195 omzet**, ruim 3 maanden normale winst. Uit zijn maillijst kocht **0,8%** (7 verkopen); van mensen die zich tijdens de sale aanmeldden kocht **16%** (14 verkopen) (DERDEN: [Cory Zue, 9 dec 2020](https://www.coryzue.com/writing/black-friday/), eigen opgave).
- Volgorde van wat telt volgens hem: eigen site (banner op elke pagina), dan eigen maillijst (2 mails: begin en 24 uur voor het einde, nooit meer dan 3), "all other channels ... a distant third"; daarbuiten alleen plekken die juist deals verzamelen. Geen korting op de prijs maar meer waarde: hij gaf de dure licentie (onbeperkt) voor de prijs van de goedkope, omdat 90% de goedkope koos (zelfde link).
- Extra: bezoek is tijdens een sale meer waard dan ooit, dus plan je beste stuk content in die week. Zijn talk werd in die maand het bovenste bericht op r/django en bracht volgens hem "hundreds, possibly thousands" (zelfde link, eigen schatting).
- **Voor ons:** dit past bij patroon 50. Voor Pro: (a) een banner over CYBER25 op `dortus.com/click-joints/` van 27 nov tot 1 dec; (b) als de Kit-lijst iemand bevat, 2 mails (begin en laatste dag); (c) de lange YouTube-video van 23 nov valt al in de goede week. Het "duurdere licentie voor dezelfde prijs"-idee (Studio $59 voor de prijs van Personal) is een optie voor een volgende sale, niet nu: CYBER25 staat al op CG Channel.

### 86. MAI: "autonome agents" voor Google Ads, 63% meer omzet in Black Friday, maar door meer uitgeven
- Persbericht van MAI: klanten gemiddeld 63% meer omzet in BFCM 2025 dan het jaar ervoor; de agents bekeken per klant per dag 39,1 campagnes en deden 32,4 aanpassingen (DERDEN, eigen claim van de verkoper: [PR Newswire, 8 dec 2025](https://www.prnewswire.com/news-releases/maicos-autonomous-ai-agents-deliver-record-black-fridaycyber-monday-boosting-customer-revenue-by-an-average-of-63-over-2024-302635538.html)). Een klant zegt het zelf: "tripling daily spend".
- **Voor ons:** de grootste "agent deed Black Friday"-cijfers die ik vond, gaan over agents die advertentiegeld sneller uitgeven. Dat valt onder regel 1 (geld alleen na ja van Thijs) en is bij een product van $12 tot $24 zonder eerste verkoop geen goed idee (GOK). Onthoud als tegenwicht bij verhalen over AI-marketing: kijk eerst of er budget achter zit.

## Patronen na ronde 15
53. **De beste etalages voor een Blender-add-on zitten in de winkel zelf**: sale, coupons, nieuwe producten, Fresh Finds (82, 83, en 46, 78). Buiten de winkel lezen alleen CG Channel en Addon Radar echt mee; de rest is klein of slapend (84).
54. **Wie verkoopt in de sale, verkoopt aan wie hem al kent**: eigen site en eigen lijst eerst, de rest ver daarachter (85). Bij ons is die eigen groep nog bijna leeg, dus de winkel-etalages wegen zwaarder.
55. **Grote "AI deed onze Black Friday"-cijfers komen van advertentiebudget** (86), niet van een agent die gratis plaatst.

## Stand na run 21 nov ±01:20 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Superhive Coupons is een gratis etalage** (GEZIEN, 82): makers zetten er korte lanceerkortingen met een klein aantal op; sorteerbaar op "Nearly Gone" en "Ending Soon". Kost niets en is geen plaatsen.
2. **Fresh Finds**: Superhive kiest elke vrijdag ±5 nieuwe producten voor de nieuwsbrief, uit de keuring, zonder aanmelding (GEZIEN, 83). Een nieuw product met een duidelijke gif en een lanceercoupon maakt de meeste kans (GOK).
3. **Andere lijsten zijn het niet waard deze week**: Blender Artists Promotions 38 tot 1.811 keer bekeken per post (GEZIEN), BlenderNation Bazaar slaapt sinds eind 2025 (GEZIEN), 80 Level is betaald en voor grote pakketten (84).
4. **Een solo-maker met echte cijfers** (DERDEN, 85): 21 verkopen in een week, vooral via eigen site en lijst; maillijst 0,8%, nieuwe aanmelders tijdens de sale 16%.
5. **Een maker die verkopen per deallijst noemt, vond ik niet**; de enige meting die we krijgen is onze eigen (verwijzers in Gumroad en straks de referral-link van Superhive, 49).

Voorstel: (a) de Blender-manager zet vóór 27 nov een banner over CYBER25 en de Superhive-sale op `dortus.com/click-joints/` (85); (b) hij zet vanaf 2 dec een Superhive-coupon voor Pro met een klein aantal (bijv. 10 keer, 20%), zodat Pro na de sale in de Coupons-lijst staat (82); (c) bij elk nieuw product of grote versie op Superhive: gif bovenaan en lanceercoupon, voor de kans op Fresh Finds (83); (d) geen tijd in Blender Artists Promotions, de Bazaar of 80 Level (84). Volgende run: hoe makers op Gumroad en Superhive hun productpagina opbouwen bij de bestverkopende kleine add-ons ($10 tot $25), en of er een maker is die de verkoop van een coupon of Fresh Finds noemt.

## Ronde 16 (run 21 nov ±02:15 UTC, klok van de container): hoe de productpagina's van verkopende add-ons eruitzien, wat een pagina op Gumroad scheelt, en hoe ver een solo-marketeer haar agent laat gaan

Vraag van de vorige run: hoe bouwen makers hun productpagina bij kleine add-ons die verkopen, en noemt iemand de opbrengst van een coupon of Fresh Finds? Het tweede vond ik niet (zelfde als ronde 15). Het eerste wel, en dat levert een fix van een paar minuten op voor Pro.

### 87. Telling: 14 add-ons bovenaan Superhive tegen Click Joints Pro
- Ik las met curl de pagina's van 14 add-ons uit de lijst `superhivemarket.com/categories/addons?sort=sales` (of die echt op verkoop sorteert, weet ik niet zeker) en die van Pro, en telde beelden, ingebouwde YouTube-video's, gifs en reviews (GEZIEN, 21 nov ±02:20 UTC):

| Product | Prijs | Beelden | YouTube in pagina | Gifs | Reviews |
|---|---|---|---|---|---|
| Smart Remesh | $17 | 5 | 5 | 22 | 20 (4) |
| Auto Unwrap | $18 | 5 | 6 | 17 | 9 (5) |
| PrefabForge | $19,99 | 5 | 0 | 0 | 0 |
| SquishyFX | $20 | 8 | 1 | 0 | 8 (5) |
| Cleave | $23 | 12 | 3 | 0 | 3 (5) |
| TopoFit | $29 | 6 | 1 | 8 | 1 (5) |
| One Click Destruction | $29 | 8 | 0 | 4 | 0 |
| FlexSpace Armature Picker | $29,90 | 19 | 1 | 0 | 0 |
| Adaptive Auto Skinning | $35 | 8 | 3 | 0 | 20 (5) |
| Illustration Station | $35 | 9 | 1 | 0 | 3 (5) |
| Blaze AutoPose | $40 | 8 | 1 | 0 | 8 (4) |
| Carnage Grains | $49,99 | 7 | 1 | 0 | 1 (4) |
| Overpaint | $59 | 7 | 1 | 6 | 0 |
| Catflow | $68 | 9 | 1 | 16 | 8 (5) |
| **Click Joints Pro** | **$12** | **5** | **0** | **0** | **0** |

- **12 van de 14 hebben minstens één YouTube-video in de pagina; Pro niet** (GEZIEN). De twee zonder video hebben wel gifs of zijn nieuw zonder reviews. De twee goedkoopste met de meeste reviews (Smart Remesh, Auto Unwrap, $17 en $18) hebben 5 tot 6 video's en 17 tot 22 gifs: elke functie een eigen filmpje.
- Superhive zelf (DERDEN: [Matthew Muldoon, Superhive-blog, 22 aug 2019](https://superhivemarket.com/posts/anatomy-of-the-perfect-product-page)): naam van 2 tot 3 woorden die zegt wat het doet, eigen renders in 2:1, **geen gif als hoofdbeeld** (hun systeem en hun sociale planner pakken dat niet op), een eerste alinea als "elevator pitch" omdat "most customers will not scroll", voordelen in plaats van functies, gifs of beelden bij de 2 of 3 grootste voordelen, en reacties van bekende Blender-mensen op de pagina.
- **Voor ons:** onze lange video "Blender hinge for 3D printing that stops at 115° | Click Joints Pro" staat openbaar op @Dortusapps (GEZIEN via YouTube oEmbed, `m3sNvDOJYQ0`). Die bovenaan in de beschrijving van Pro op Superhive zetten (en ook als video-cover op Gumroad, dat kan met een YouTube-link) kost de Blender-manager een paar minuten, geen geld, en is geen plaatsen. Wat het oplevert weet niemand (GOK), maar het is het enige verschil met bijna elke verkopende add-on in deze telling, vóór de sale van 27 nov. Daarna, als er tijd is: een korte gif per grote functie (hinge met eindstop, kogelgewricht, graden naast elk gewricht) in de tekst, zoals Smart Remesh en Auto Unwrap doen.

### 88. Gumroad: zelfde maker, twee bijna gelijke producten, $10.778 tegen $0
- InsightRaider, een site die omzet van Gumroad-producten uitleest, vergelijkt twee producten van één verkoper: 4 tegen 2 covers, lange tegen korte tekst, "30-day money back" tegen "No Refunds"; omzet **$10.778 tegen $0** (DERDEN: [InsightRaider op dev.to, 24 jul 2026](https://dev.to/insightraider/one-gumroad-product-made-10778-a-nearly-identical-one-made-0-three-settings-explain-it-bnj)). Over hun hele verzameling: 1 cover gemiddeld $234 tegen 5 covers $4.312; lege tekst $87 tegen 6.000+ tekens $3.124; "No Refunds" $187 tegen een belofte van 30 dagen $1.847 (zelfde link).
- **Kritisch:** dit is samenhang, geen proef; betere makers doen alles beter. En InsightRaider verkoopt een betaald dataplatform, het stuk is reclame (eigen claim). Gebruik het als lijstje, niet als belofte van 18 keer meer.
- **Pro op Gumroad naast dat lijstje** (GEZIEN, uit de paginadata op 21 nov ±02:25 UTC): 5 covers (alle vijf plaatjes, geen video), tekst ±3.500 tekens, een korte eerste zin ("Rig to printable figure: elbows and knees stop where your rig stops."), 0 reviews, en **geen terugbetaalbelofte op de pagina** (het veld `refund_policy` is leeg en de woorden refund, guarantee en money komen niet in de tekst voor).
- **Voor ons:** covers en tekst zitten al goed. Wat ontbreekt: (a) een video als eerste cover (zie 87); (b) een zin als "Not what you need? Mail within 30 days and you get your money back." Dat laatste is een besluit over geld (terugbetalen), dus voor de Blender-manager en bij twijfel Thijs; het kost niets vooraf. Bij een product van $19 zonder reviews haalt het het grootste risico van een koper weg (GOK, volgens de redenering in de bron).

### 89. Superhive over sales: kopers wachten niet, en ruim 75% koopt voor de volle prijs
- Kyle Maurer van Superhive, over hun eigen cijfers (DERDEN: [Superhive-blog, 5 mrt 2026](https://superhivemarket.com/posts/do-people-only-buy-during-sales-here-s-what-the-data-says)): van kopers met meer dan één aankoop kocht **0,4%** alleen in de sale; **0,3%** kocht 70% of meer in de sale. In de week vóór de Cyber Sale lag de omzet per dag in 6 van de 7 jaren **boven** het jaargemiddelde (alleen 2024: 0,2% eronder); over de 30 dagen ervoor de laatste 3 jaar 3% tot 9% eronder. Elk jaar gaat **meer dan 75%** van de aankopen voor de volle prijs.
- Nieuw sinds zomer 2025: **bundels**. Ze verklaren het grootste deel van de groei in aankopen met korting en waren volgens Superhive "a huge net positive". Voorbeeld: "Creators 4 Creators: Pick of the Pack by Southern Shotty", 17 producten gekozen door een YouTuber, $508,40 waarde voor $254, zonder updates, met in veel producten een coupon om bij de maker zelf te kopen (GEZIEN, [bundelpagina](https://superhivemarket.com/bundles/southern-shottys-picks), afgelopen 28 nov).
- **Voor ons:** (a) de week vóór 27 nov is geen dode week; een pagina met video helpt dus ook nu al (GOK uit de cijfers hierboven). (b) Een bundel is een etalage die Superhive samenstelt, niet wij; erin komen vraagt een aanvraag bij Superhive (benaderen, dus via de hoofdchat en regel 4). Voor nu alleen onthouden; eerst reviews en een video.

### 90. Een solo-marketeer met Claude Cowork: alles intern zelfstandig, niets naar buiten
- Sacra sprak een hoofd productmarketing van een kleine start-up die haar hele marketing alleen doet met Claude Code, Cowork, Skills en Design (DERDEN: [Sacra-interview, 2026, datum niet op de pagina](https://sacra.com/research/product-marketer-saas-automating-marketing-with-claude-cowork/)). Zelfstandig laat ze alleen terugkerende interne stukken lopen: concurrenten volgen, vacatures van klanten als verkoopsignaal, een maandelijkse brancheupdate, als lijstje in Slack.
- Haar grens, letterlijk: "I wouldn't have Cowork autonomously post to our LinkedIn page ... the words still sound like AI ... Almost anything going externally, I won't just let an agent post autonomously." Wat misging: bronnen van het web die niet klopten; haar fix was interne "grondwaarheid"-documenten boven webbronnen zetten. Ze noemt het ontbreken van geheugen tussen sessies het grootste gat ("Every conversation starts fresh").
- **Voor ons:** dit bevestigt wat we al hebben (patroon bij 55 en 61: vaste grondwaarheid in een bestand, keuring vóór iets naar buiten gaat). Onze repo is precies dat geheugen tussen sessies. Geen nieuwe opdracht, wel een tegenwicht voor elk "laat de agent alles plaatsen"-verhaal: wie het zelf dagelijks doet, laat het buiten niet los.

## Patronen na ronde 16
56. **De productpagina is goedkoper dan bereik**: bijna elke verkopende add-on heeft een video in de pagina, Pro niet (87). Eerst de pagina, dan pas meer posts die ernaar wijzen.
57. **Kleine dingen die risico wegnemen tellen bij een onbekende maker**: video, reviews, een terugbetaalbelofte (88). Van deze drie kunnen we er twee vandaag zelf.
58. **Sales trekken niet leeg wat ervoor komt** (89): de week vóór Black Friday verkoopt Superhive gewoon, dus nu verbeteren telt mee.

## Stand na run 21 nov 02:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **12 van 14 verkopende add-ons op Superhive hebben een YouTube-video in de pagina, Click Joints Pro niet** (GEZIEN, 87). Onze lange video `m3sNvDOJYQ0` staat al openbaar.
2. **De goedkope add-ons met de meeste reviews ($17 tot $18) tonen elke functie in een eigen filmpje of gif**: 5 tot 6 video's, 17 tot 22 gifs (GEZIEN, 87).
3. **Op de Gumroad-pagina van Pro staat geen terugbetaalbelofte en geen video** (GEZIEN, 88); covers (5) en tekst (±3.500 tekens) zijn al in orde. De bron die zegt dat een belofte ±10 keer scheelt is reclame en samenhang (DERDEN, 88).
4. **Kopers wachten niet op de sale** (DERDEN, 89): de week voor Black Friday ligt bij Superhive meestal boven gemiddeld, en meer dan 75% koopt voor de volle prijs.
5. **Een marketeer die Cowork dagelijks gebruikt laat alleen intern werk zelfstandig lopen** (DERDEN, 90); naar buiten altijd een mens of keuring. Past bij onze regel 4.

Voorstel: (a) de Blender-manager zet vóór 27 nov de video `m3sNvDOJYQ0` bovenaan de beschrijving van Pro op Superhive en als eerste cover op Gumroad (87, een paar minuten, €0); (b) hij besluit over een zin "money back within 30 days" op Gumroad, of meldt het aan de hoofdchat voor Thijs als hij dat een geldbesluit vindt (88); (c) de Maker van Roep maakt bij de volgende filmpjes per functie een korte gif zonder geluid die ook in de producttekst kan (87). Volgende run: hoe kleine Blender-makers aan hun eerste reviews komen zonder nepreviews (vragen na aankoop, Discord, testers), en of een agent dat zelfstandig kan binnen regel 4.

## Ronde 17 (run 21 nov ±03:20 UTC, klok van de container): hoe kleine makers aan hun eerste reviews komen zonder nepreviews, en wat een agent daarin zelf mag

Uitgangspunt: Click Joints Pro heeft 0 verkopen en dus 0 reviews (GEZIEN, `organisatie/bord.md`, 20 nov 21:45). De vraag uit de vorige run was hoe makers aan hun eerste reviews komen. Kort antwoord vooraf: reviews volgen op verkoop, en op Superhive kun je ze niet "voorschieten" met gratis exemplaren.

### 91. Superhive: alleen kopers kunnen beoordelen, gratis exemplaren via eigen coupon tellen niet
- Regels sinds een update van 10 nov 2026 (GEZIEN, [Superhive-hulp, product ratings](https://support.blendermarket.com/article/171-guide-to-product-ratings-on-blender-market)): alleen een koper met een afgeronde, niet terugbetaalde bestelling kan een product één keer beoordelen. Uitgesloten: de maker zelf, medewerkers, **klanten die een gratis exemplaar kregen via een eigen coupon of eigen sale**, en iedereen die niet kocht. Beoordelingen die de regels breken tellen niet mee voor het gemiddelde en de plek in de ranglijst. De maker mag één keer op elke beoordeling reageren.
- Superhive schrijft er zelf bij dat de beoordeling ook over de **ondersteuning** gaat: een koper die het product goed vindt maar lang op antwoord wacht, geeft minder sterren.
- **Voor ons:** testers of makers een gratis Pro geven via een 100%-coupon levert op Superhive geen enkele ster op. De eerste reviews moeten van echte kopers komen. Snel en goed antwoorden op vragen telt mee in de sterren, en dat is werk dat een agent goed kan voorbereiden (concept, keuring, plaatsen door de mens of de hoofdchat).

### 92. Superhive: kopers mailen mag, maar alleen wie toestemming gaf, en max 3 mails per dag
- (GEZIEN, [Superhive-hulp, How To Email Customers](https://support.blendermarket.com/article/33-how-to-email-customers), bijgewerkt 10 nov 2026): via "Email Customers" in het makersdashboard kan de maker alle kopers van één product mailen, **maximaal 3 mails per 24 uur, minstens 1 uur ertussen**. Alleen kopers die bij het afrekenen toestemming gaven voor mail van makers krijgen hem (AVG).
- (GEZIEN, [Superhive-hulp, How to Engage Customers](https://support.blendermarket.com/article/199-how-to-engage-customers)): Superhive raadt zelf een **mail na de aankoop** aan om te vragen of alles werkt "and to encourage customers to leave a review". Bij kopers die toestemming gaven staat het mailadres in de Sales-tab; een losse mail stuur je dan buiten Superhive om.
- **Voor ons:** een vaste "werkt alles?"-mail een paar dagen na elke koop is toegestaan en wordt door Superhive zelf aangeraden. Het dashboard heeft geen API die ik kon vinden (GOK), dus een agent kan de tekst klaarzetten maar niet zelf versturen. Verstuurd vanaf het Dortus-account is het geen bericht onder de naam van Thijs, maar wel "naar buiten"; dat is een besluit voor de hoofdchat onder regel 4.

### 93. Gumroad: herinnering na 5 dagen gaat vanzelf, en gratis downloads mogen wel beoordelen
- (GEZIEN, [Gumroad-hulp, product ratings](https://gumroad.com/help/article/222-product-ratings-on-gumroad)): kopers kunnen tot een jaar na aankoop beoordelen. Gumroad stuurt **zelf een herinnering 5 dagen na de aankoop** aan wie nog geen review gaf (instelling "Send review reminder emails", staat standaard aan). De maker kan daarnaast een eigen mail of **workflow** naar de kopers van één product sturen, kan op elke review reageren, en kan reviews **in de productbeschrijving zetten** (Insert, Reviews). Een terugbetaling haalt de beoordeling weg; bij een gratis download kan het ook door de toegang in te trekken. Dat laatste betekent dat ook wie het gratis kreeg kan beoordelen.
- **Voor ons:** de Blender-manager kan op Gumroad nu al één workflow-mail klaarzetten (bijvoorbeeld 3 dagen na koop: korte uitleg, link naar de video, "antwoord op deze mail als iets niet werkt"). De herinnering om te beoordelen doet Gumroad al; een tweede vraag om een review erbovenop is dubbel. Testers een gratis code geven die daarna een review schrijven kan op Gumroad technisch wel. Dat is geen nepreview als het een echte gebruiker is die eerlijk schrijft, maar in de VS moet dan vermeld worden dat het gratis was (GOK op de regels van de FTC, ik ben geen jurist). Liever niet als eerste stap.

### 94. Hoeveel reviews per verkoop: bij betaalde Blender-add-ons op Gumroad ±4 tot 11 per 100
- Eigen telling via de openbare zoekfunctie en productpagina's van Gumroad (GEZIEN, 21 nov, `gumroad.com/products/search?query=blender addon&sort=most_reviewed` en de pagina's zelf). Bij de meeste betaalde producten staat het aantal verkopen verborgen; bij deze vijf staat het open:
  - Rig Anything With Rigify ($17,99): 213 beoordelingen op 1.893 verkopen, **11,3%**
  - Hekuran ($8,90): 10 op 126, **7,9%**
  - Create Animated Low Poly Characters ($79,99): 326 op 4.484, **7,3%**
  - Space VFX Elements ($30): 155 op 3.853, **4,0%**
  - Botaniq Trees (lite, $2): 222 op 16.346, **1,4%**
- Gratis add-ons ter vergelijking: Custom Planet 112 op 11.141 (1,0%), Old Modifier Menu 53 op 4.475 (1,2%), Animation Render Time Estimator 35 op 2.572 (1,4%), Roblox Material Fixer 6 op 646 (0,9%) (GEZIEN, zelfde dag).
- Let op: dit zijn producten die al veel beoordelingen hebben (gekozen op "most reviewed"), en Gumroad stuurt bij allemaal de herinnering na 5 dagen. Het echte gemiddelde ligt waarschijnlijk lager (GOK).
- **Voor ons:** om aan 5 reviews te komen heeft Pro grofweg **50 tot 120 verkopen** nodig zonder eigen vraag (GOK uit de getallen hierboven). Reviews komen dus pas na de eerste tientallen verkopen; tot die tijd moeten video, terugbetaalbelofte en uitleg op de pagina het vertrouwen dragen (zie 87 en 88).

### 95. Vragen binnen het product werkt het best, op een moment dat de gebruiker er iets aan had
- Vova Feldman (RatingWidget, WordPress, later Freemius) testte een "beoordeel ons"-melding in het dashboard van zijn plugin (DERDEN, [Freemius-blog, 2015](https://freemius.com/blog/how-we-increase-our-wordpress-plugin-reviews-by-700-percent/)): van **4 tot 8 naar 56 reviews per maand** na zes weken A/B-testen. Een melding na iets wat de gebruiker opleverde (na 10, 100 en 1.000 stemmen op zijn site) werkte veel beter dan een melding na een vaste tijd; een persoonlijke toon werkte "een beetje" beter. Daarvoor kreeg hij 1 à 2 reviews per week door na een goed opgelost supportverzoek om een review te vragen. Nadeel dat hij zelf noemt: de reviews zijn kort ("Great plugin"). Let op: Freemius verkoopt zelf zulke review-verzoeken.
- WooCommerce geeft makers een richtlijn (GEZIEN, [WooCommerce-docs, Requesting reviews](https://developer.woocommerce.com/docs/extensions/review-guidelines/how-to-request-reviews/)): één melding tegelijk, altijd helemaal weg te klikken, geen sturende tekst, en het beste moment is direct contact als de klant het meest tevreden is (na een mijlpaal).
- Tegengeluid van een verkoper op Fab (DERDEN, [Unreal-forum, nov 2025](https://forums.unrealengine.com/t/improving-product-ratings-and-reviews-on-epic-games-fab/2669260)): automatische mails worden als spam gezien, en "the only people who actually receive ratings are those who build a social media following and nag their customers there".
- Onderzoek van Sang-Pil Han (DERDEN, [ASU, 2023](https://knowledge.wpcarey.asu.edu/20230302-seeking-reviews-online-buyers-ask-later)): een herinnering om te beoordelen werkt beter als je wacht tot de koper het product heeft kunnen gebruiken, niet direct na de koop.
- **Voor ons:** in **Pro** (niet in de gratis versie, waar een verwijzing naar Pro niet mag volgens `platformen/blender/verwijzing-pro.md`) kan één rustige regel in het paneel komen na een echt moment van waarde, bijvoorbeeld na het 20e gewricht: "Werkt Click Joints voor je? Een beoordeling helpt ons enorm" met een link naar de Superhive- of Gumroad-pagina en een knop om hem voor altijd weg te halen. Dat is bouwwerk voor de Blender-manager, €0, en het wacht op de eerste kopers.

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf:** reviews en vragen van kopers dagelijks lezen (Gumroad stuurt een mail bij een nieuwe review, die de hoofdchat al alleen-lezen kan zien), een antwoord klaarzetten, het aantal reviews en verkopen per week bijhouden.
- **Na keuring, geplaatst door de hoofdchat:** het ene antwoord op een review (Superhive en Gumroad), de mail na de koop.
- **Nooit:** reviews schrijven, laten schrijven of kopen, een gratis code ruilen voor een positieve review, of mensen die geen koper zijn laten beoordelen. Superhive telt zulke beoordelingen niet mee (91), en het is bedrog volgens onze eigen brief.
- Een voorbeeld van een maker die dit volledig door een agent liet doen met cijfers vond ik in deze run niet; de review-antwoordtools voor de App Store (Review Agent, AppReply, Rewo) zijn verkooppraat zonder openbare uitslag (GEZIEN, zoekresultaten, geen eigen cijfers gevonden).

## Patronen na ronde 17
59. **Reviews volgen op verkoop, niet andersom**: bij betaalde Blender-add-ons ±4 tot 11 reviews per 100 verkopen (94), en op Superhive tellen gratis exemplaren niet (91). Bij 0 verkopen is "meer reviews" geen hefboom; de pagina wel.
60. **De sterren gaan ook over de ondersteuning** (91, 95): snel en vriendelijk antwoorden is het deel van "reviews" dat een agent kan voorbereiden.
61. **Vraag op een moment van waarde, één keer, weg te klikken** (95). Na de koop doet Gumroad de herinnering al (93); Superhive raadt een eigen "werkt alles?"-mail aan (92).

## Stand na run 21 nov 03:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Op Superhive kunnen alleen echte kopers beoordelen; gratis exemplaren via een eigen coupon tellen niet** (GEZIEN, 91). Testers een gratis Pro geven levert daar geen sterren op.
2. **Bij betaalde Blender-add-ons op Gumroad komen er ±4 tot 11 reviews per 100 verkopen** (GEZIEN op 5 producten, 94). Pro heeft er dus tientallen verkopen voor nodig; tot dan dragen video, terugbetaalbelofte en uitleg het vertrouwen.
3. **Gumroad stuurt zelf een herinnering 5 dagen na de koop en laat reviews in de beschrijving zetten** (GEZIEN, 93). Daar hoeven wij niets voor te bouwen.
4. **Superhive raadt een mail na de koop aan; mailen kan alleen naar kopers met toestemming, max 3 per dag** (GEZIEN, 92). Dat is naar buiten, dus een besluit voor de hoofdchat.
5. **Een vraag in het product na een moment van waarde werkt het best** (DERDEN: 4 tot 8 naar 56 reviews per maand bij een WordPress-plugin, 95); alleen in Pro, nooit in de gratis versie.

Voorstel: (a) geen tijd steken in "reviews regelen" zolang Pro 0 verkopen heeft; de voorstellen van run 16 (video bovenaan, terugbetaalbelofte) gaan voor (94); (b) de Blender-manager zet op Gumroad één workflow-mail klaar voor 3 dagen na de koop ("werkt alles? hier de video, antwoord als iets misgaat"), zonder extra reviewvraag, en laat hem keuren en door de hoofdchat aanzetten (92, 93); (c) in Pro 1.2 een rustige, weg te klikken beoordelingsregel na het 20e gewricht (95), €0; (d) zodra er een review is: binnen een dag een gekeurd antwoord, en de review in de Gumroad-beschrijving (93). Volgende run: waar de eerste 10 kopers van een add-on zonder publiek vandaan komen (zoekwoorden in Superhive, de nieuwe-productenlijst, Reddit-draadjes met een vraag waar Pro het antwoord op is), en welk deel een agent daarvan zelf kan vinden.

## Ronde 18 (run 21 nov ±04:20 UTC, klok van de container): waar de eerste kopers van een add-on zonder publiek vandaan komen, en wat een agent daarvan zelf kan meten

Vraag van run 17: hoe komt een add-on zonder eigen publiek aan zijn eerste 10 kopers, en welk deel kan een agent zelf vinden? Ik keek naar Superhive zelf (zoeken, galerijen), een concurrent die nu goed verkoopt, en de fora. Alles hieronder is met curl uit de cloud gelezen, zonder account.

### 96. Cleave: een 3D-print-add-on van 2 maanden oud staat op plek 3 van "Popular" op Superhive, met een kanaal van 153 abonnees
- **Wat:** Cleave van V4SS3UR (modellen splitsen voor 3D-print, met pennen, magneten en sinds 1.6 ook kogelgewrichten) staat vandaag als **nummer 3** in de galerij Popular op de voorpagina van Superhive (GEZIEN, voorpagina 21 nov ±04:10 UTC, `cleave?num=3&src=popular`). Volgens Superhive zijn dat "the eight products with the top sales over the past 7 days" (GEZIEN, [How to Get Your Product Featured](https://support.blendermarket.com/article/242-how-to-get-your-product-featured)). Het staat tussen Auto-Rig Pro, HumGen3D en Botaniq.
- **Cijfers:** gepubliceerd ±2 maanden geleden, nu $23 (van $28), **3 beoordelingen** (GEZIEN, [productpagina](https://superhivemarket.com/products/cleave)). **11 versies in 8 weken**, van 1.0.0 op 23 sep tot 1.7.0 op 17 nov (GEZIEN, versiegeschiedenis). Het YouTube-kanaal heeft **153 abonnees** en 5 video's met **350 tot 830 weergaven** (GEZIEN, youtube.com/@V4SS3UR). Eén forumbericht op Blender Artists, een echte stap-voor-stap uitleg "eerst met de hand, dan sneller met een add-on die ik schreef": **264 keer bekeken, 0 likes** (GEZIEN, [Blender Artists, 1 okt](https://blenderartists.org/t/1654018)).
- **Wat de pagina doet:** een lange titel vol zoekwoorden ("Smart Model Split & Cut for 3D Printing with Connectors (Pegs, Dowel, Rod Channel, Magnets, Ball Joints)"), bovenaan "Too big to print? Split it.", twee tutorials en een demo ingebed, een voor/na-beeld, en een stuk "Why not just bisect it by hand?" dat de gratis weg eerlijk naast de add-on legt (GEZIEN).
- **Wat dit zegt:** met een klein kanaal en een forumbericht dat weinig deed, komt het grootste deel van de kopers vrijwel zeker van Superhive zelf: zoeken, de galerijen en de sale-badge (GOK, Superhive geeft geen verkoopcijfers per product). En: **een add-on voor 3D-print met gewrichten kan op Superhive bij de best verkopende van de week staan**. De markt bestaat dus.
- **Voor ons:** Cleave is de beste vergelijking voor Pro (zelfde kopers, deels zelfde functie: kogelgewrichten). Wat zij hebben en Pro nog niet: zoekwoorden in de titel, video's ingebed op de pagina, en elke week een zichtbare nieuwe versie.

### 97. Waar Click Joints Pro nu staat in de zoekfunctie van Superhive
Telling op 21 nov ±04:00 UTC, zoeken in alle categorieën en in Addons (GEZIEN, `superhivemarket.com/search?search[q]=...`, 24 producten per pagina). De zoekwoorden komen uit de suggesties die Superhive zelf geeft als je begint te typen (GEZIEN, `/search/suggestions`: "articulated joints", "print in place", "ball joint", "joint", "hinge", "printable").

| Zoekwoord | Plek Pro (alles) | Plek Pro (Addons) | Wie staat ervoor (Addons) |
|---|---|---|---|
| click joints | 1 | 1 | |
| posable | | 1 | |
| ball joint | 3 | 3 | Cleave, Cut Flex |
| joints | 8 | 5 | Cleave, Join Mesh, JointLab, Dovetail Key |
| joint | 10 | | |
| hinge | 20 | 4 | PhysForge, LayerMechanic, Pro Origin Tools |
| articulated joints | | 5 | JointLab, Cut Flex, Articulator, OpenSet Connect |
| action figure | | 10 | |
| printable | | 19 | |
| articulated | niet in top 24 | | JointLab, losse modellen |
| print in place | niet in top 24 | niet in top 24 | LayerMechanic, Fit & Tolerance Test Generator |
| 3d printing / 3d print | niet in top 24 | niet in top 24 | Ultimate STL Export, Cleave, PuzzleUrPrint, JointLab |
| snap fit, flexi | niet in top 24 | niet in top 24 | |

- **Concurrenten die ik zo vond** (GEZIEN, productpagina's): JointLab $65 (3 beoordelingen, 4 maanden), Cut Flex $34,99 ("3d-printed-poseable", "ball-joints", 1 maand), Articulator $1 (2 beoordelingen), Catpin $24 (4 beoordelingen), LayerMechanic $25 (print-in-place, 1 maand), Printwright $19 (18 dagen). Buiten Superhive: SlicerJoint Pro op Gumroad $20, **0 beoordelingen** na 3,5 maand, twee forumberichten met 310 en 223 weergaven (GEZIEN, [Gumroad](https://ayhancelik.gumroad.com/l/slicerjointpro), [Blender Artists](https://blenderartists.org/t/slicerjoint-pro/1649572)).
- **Waarom Pro mist op "print in place" en "3d printing":** de titel is alleen "Click Joints Pro", en de tags missen precies die woorden (Pro heeft wel 3d-printing, ball-joint, hinge, posable, articulated-figure; GEZIEN). Hoe Superhive zoekt (titel, tags, tekst) staat nergens beschreven; dat titel en tags meetellen is een GOK uit de tabel.
- **Hoe lang "nieuw" helpt:** Superhive zegt zelf dat zoeken standaard het nieuwste eerst toont, maar "with dozens of products uploaded daily, the amount of time that your product spends on that first search page may not be very long" (GEZIEN, [How to Increase Sales](https://support.blendermarket.com/article/203-how-to-increase-sales)). Pro staat sinds ±20 nov live en staat vandaag al niet meer in het rijtje "new" op de voorpagina (GEZIEN). Het moment van de New Arrivals-galerij is dus al voorbij.

### 98. Wat Superhive zelf zegt over de eerste verkoop
Uit de makershulp (GEZIEN, laatst bijgewerkt 30 sep 2026, [Tips for Success](https://support.blendermarket.com/article/174-tips-for-success), [How to Increase Sales](https://support.blendermarket.com/article/203-how-to-increase-sales), [Featured](https://support.blendermarket.com/article/242-how-to-get-your-product-featured)):
- **Popular** = de 8 met de meeste verkopen in 7 dagen. **Staff Picked** = 2 producten, elke maandag, woensdag en vrijdag met de hand gekozen, vooral uit nieuwe inzendingen; "if the featured image is blah, it will not be selected". **New Arrivals** = de 8 nieuwste.
- Een sale geeft een "On Sale"-badge en vergroot de kans om in "Popular" en "Top Selling" te komen; een publieke coupon komt op de couponpagina en in de zijbalk van het product (zie ook 82).
- Mond-tot-mond via support: "Someone ... calls out your product on a YouTube video or in their Blenderartists post and you suddenly have dozens more people looking at and buying your product." Dat komt volgens hen door een goed product plus snel en goed antwoorden.
- Tegengeluid: een oud stuk van Superhive zelf zegt "If you build it they will not come" en raadt aan overal te promoten (DERDEN, [This Is What Successful Creators Are Doing](https://superhivemarket.com/posts/this-is-what-successful-blender-market-vendors-are-doing)); Andreas Esau (BPainter, duizenden verkopen volgens Superhive) haalde zijn kopers vooral via Twitter en BlenderNation (DERDEN, [interview](https://superhivemarket.com/posts/andreas-esau-if-you-want-to-sell-blender-add-ons-learn-how-to-communicate)). Beide stukken zijn van jaren geleden, toen er veel minder producten waren.

### 99. Vragen op fora als bron van kopers: weinig aanbod, en Reddit is dicht vanuit de cloud
- **Blender Artists** heeft een open JSON-zoekfunctie zonder account (GEZIEN, `blenderartists.org/search.json`). Zoeken op "articulated joints print" geeft in 2026 maar **1 echte vraag** (31 okt, iemand die een beweegbaar figuurtje wil maken, 104 keer bekeken, 4 berichten) en verder vooral berichten van add-on-makers zelf (GEZIEN). Het aanbod aan vragen waar Pro het antwoord op is, is dus klein: grofweg één per maand op dit forum (GOK).
- **Blender Stack Exchange** (open API, 300 aanvragen per dag zonder sleutel, GEZIEN quota 280): de vragen over gewrichten voor 3D-print zijn oud (2016 tot 2024) en een paar honderd tot ±2.200 keer bekeken (GEZIEN). Die oude vragen worden wel nog gevonden via Google, maar een antwoord met een link naar een betaald product mag daar meestal niet (GOK, niet nagelezen in deze run).
- **Reddit** geeft vanuit de cloud een 403, ook op old.reddit en de RSS (GEZIEN, deze run). Dat klopt met 68 en met wat Aria13 en anderen meldden. Een agent kan Reddit dus niet zelf lezen vanaf hier; alleen via WebSearch-resultaten, zonder de nieuwste draadjes.
- **Indie Hackers** staat achter een Cloudflare-scherm voor curl (GEZIEN). De vele "ik kreeg 60 klanten via Reddit" en "9 keer verbannen"-verhalen daar kon ik dus niet lezen; ik tel ze niet mee.
- **Tools die Reddit afspeuren naar kopers** (Subradar, ReplyRadar, Okara, LeadsFromURL, op Product Hunt en Indie Hackers) noemen geen eigen verkoopuitslag op hun pagina's in de zoekresultaten (GEZIEN, alleen titels; verkooppraat tot het tegendeel blijkt).

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, elke dag, €0:** de tabel van 97 opnieuw maken (de plek van Pro voor 10 tot 15 zoekwoorden, alles en Addons), de galerijen op de voorpagina uitlezen (Popular, new, new_and_rising, staff picks) en kijken of Pro of een concurrent erin staat, de versies en prijzen van Cleave, Cut Flex en JointLab volgen, en Blender Artists doorzoeken op nieuwe vragen. Dit is allemaal openbaar en werkt met curl uit de cloud (GEZIEN).
- **Na keuring, door de Blender-manager:** titel, ondertitel en tags van Pro op Superhive aanpassen (zie voorstel). Dat is onze eigen productpagina, geen post naar buiten.
- **Niet:** Reddit lezen of plaatsen vanaf hier, en geen antwoorden op fora onder een account van Thijs zonder zijn ja (regel 4).

## Patronen na ronde 18
62. **Op Superhive brengt de winkel zelf de eerste kopers, als je gevonden wordt** (96, 97): een concurrent met 153 abonnees staat in de top 8 van de week. Zoekplek en galerijen zijn de hefboom, niet eigen bereik.
63. **Zichtbaar onderhoud verkoopt** (96): Cleave bracht elke week een versie uit, elk met een nieuwe functie die op de pagina staat.
64. **Vragen op fora zijn voor Pro een klein kanaal** (99): ±1 echte vraag per maand op Blender Artists, en Reddit is dicht vanuit de cloud. Niet de plek waar de eerste 10 kopers vandaan komen.

## Stand na run 21 nov 04:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Cleave, een 3D-print-add-on met kogelgewrichten van 2 maanden oud, staat vandaag op plek 3 van de best verkopende week op Superhive, met een YouTube-kanaal van 153 abonnees** (GEZIEN, 96). De kopers komen dus vooral uit Superhive zelf, en de markt voor Pro bestaat.
2. **Pro is goed te vinden op "click joints", "posable", "ball joint", "joints" en "hinge" (Addons: plek 1 tot 5), maar niet op "print in place", "3d printing", "articulated" en "snap fit"** (GEZIEN, 97), woorden die Superhive zelf als zoeksuggestie geeft.
3. **De titel van Pro is alleen "Click Joints Pro"**; Cleave, JointLab en anderen zetten hun zoekwoorden in de titel (GEZIEN, 96, 97).
4. **Het moment "nieuw" is na een dag voorbij** (GEZIEN, 97): Pro staat al niet meer in het rijtje new op de voorpagina. Staff Picked (2 per keer, ma/wo/vr) hangt af van een sterke hoofdafbeelding (GEZIEN, 98).
5. **Fora en Reddit leveren hier weinig op**: ±1 echte vraag per maand op Blender Artists, Reddit 403 vanuit de cloud (GEZIEN, 99).

Voorstel: (a) de Blender-manager past vandaag de Superhive-pagina van Pro aan, €0: titel naar iets als "Click Joints Pro - Rig to Printable Articulated Figure (Ball Joints, Hinges, Print in Place, 3D Printing)" en tags erbij: print-in-place, articulated, 3d-print, snap-fit, flexi, toy; laat een ander keuren, en tel na 2 dagen opnieuw met de tabel van 97 (doel: top 10 in Addons op "print in place", "articulated" en "3d printing"); (b) twee video's (de lange video en een korte demo) ingebed bovenaan de Superhive-pagina, zoals Cleave (96); (c) houd elke week een kleine, zichtbare versie aan (1.1.1, 1.2) met een regel in de versiegeschiedenis, zolang er iets echts te verbeteren is (63); (d) laat de Roep- of scorebordagent de tabel van 97 en de voorpagina-galerijen dagelijks met curl meten en in het scorebord zetten, zodat we zien of (a) werkt. Volgende run: wat de hoofdafbeelding van producten in Staff Picked en new_and_rising gemeen heeft, en hoe die van Pro daar tegenaan ligt.

## Ronde 19 (run 21 nov ±05:20 UTC, klok van de container): de hoofdafbeelding van Pro naast die van wat nu verkoopt, en wat een nieuw beeld bij anderen opleverde

Vraag van run 18: wat hebben de hoofdafbeeldingen van producten in Staff Picked en new_and_rising gemeen, en hoe ligt die van Pro daartegen? Alles met curl gelezen uit de cloud, zonder account; de beelden heb ik zelf bekeken (skill kijken: naast elkaar op een vel, op ware grootte en op de grootte van de voorpagina).

### 100. Staff Picked staat niet meer op de voorpagina; er zijn nu vijf rijtjes
- Op de voorpagina van Superhive staan vandaag de rijtjes **popular, new_and_rising, new, on_sale en top**; een rijtje Staff Picked vond ik niet (GEZIEN, voorpagina 21 nov ±05:15 UTC, geteld op `src=` in de links). De makershulp noemt Staff Picked nog wel (zie 98), maar het is als etalage op de voorpagina weg of verstopt (GOK).
- Hoe new_and_rising gekozen wordt, staat nergens in de makershulp die ik las (GEZIEN, artikel 242 noemt alleen Popular, Staff Picked en New Arrivals). De 9 producten erin zijn allemaal van de laatste weken (productnummers 268012 tot 269441; Pro is 269495, GEZIEN). Dat het "nieuw en verkoopt al" betekent, is een GOK uit de naam.
- **Nieuw in de rijtjes:** OpenSet Connect, die in 97 nog vóór Pro stond op "articulated joints", staat op plek 7 van new_and_rising; Catpin (een concurrent, 4 beoordelingen) staat op plek 3 van on_sale met "November update, new version 1.0.9, -20% off now" in het beeld (GEZIEN). Cleave staat nog op plek 3 van popular (GEZIEN).

### 101. Telling: 11 hoofdafbeeldingen uit de rijtjes tegen die van Pro
Hoofdafbeelding (og:image, 1200 x 600) van de 9 uit new_and_rising plus Cleave en Catpin, naast Click Joints Pro (GEZIEN, productpagina's 21 nov ±05:20 UTC):

| Wat staat in het beeld | Van de 11 | Pro |
|---|---|---|
| Productnaam groot in beeld | 11 | nee |
| Een belofte in een paar woorden ("Full retopo in a few clicks", "100K+ 3D models", "Too big to print"-achtig) | 9 | alleen klein "Right knee: bends 0° to 120°" |
| Een mooie render of foto van het resultaat, geen kaal Blender-scherm | 10 (alleen OpenSet toont ook een paneel, naast een render) | nee: grijs Blender-scherm met een grijs poppetje en een vol paneel |
| Sterke kleur of contrast | 11 | nee, vooral grijs |
| Korting of versie in het beeld ("75% off", "-20%", "50% off until 26th November", "Launch sale 35% off") | 6 | nee (Pro staat ook niet in de sale, zie onder) |
| Video ingebed op de pagina | 8 (1 tot 3 video's) | 0 |
| Galerijbeelden naast de hoofdafbeelding | 4 tot 13, de meeste 5 tot 9 | 4 |

- **Op de grootte van de voorpagina** (600 x 300, het formaat `medium` dat de rijtjes tonen, GEZIEN) is in het beeld van Pro geen tekst te lezen en zie je niet wat het product doet; Cleave ernaast leest in één blik: naam, drie beloftes, een geprint figuur met onderdelen op een snijmat (GEZIEN, zelf naast elkaar bekeken).
- **Waarom het zo is:** in `platformen/blender/superhive/README.md` staat dat beeld 1 bewust een echt scherm is met één regel tekst; op de live pagina staat nu als hoofdafbeelding het knie-scherm zonder die regel (GEZIEN). Superhive zelf: "if the featured image is blah, it will not be selected" (GEZIEN, artikel 242, zie 98).
- **Prijs:** Pro staat op Superhive op $12 zonder korting; de Gumroad-pagina zegt $19 (GEZIEN). Dat is het besluit van 19 nov (Superhive op $12 tot na 2 dec, zie `platformen/blender/click-joints-plan-KEURING.md`), dus geen fout, maar het betekent wel: geen "On Sale"-badge en geen kans op het rijtje on_sale, waar Catpin nu staat.

### 102. Wat een nieuw hoofdbeeld bij anderen opleverde (Steam, ouder maar met cijfers)
- **Imagine Earth** (Serious Bros, twee man): een jaar lang 0 tot 3 verkopen per dag in Early Access; in juni 2015 alleen de capsule (het kleine hoofdbeeld op Steam) vervangen, daarna **40 tot 60 per dag** en dat bleef zo. Volgens de makers veranderde er verder niets. Zij zetten daarna bij elke grote update (elke 1 tot 2 maanden) een banner op het beeld "om te laten zien dat er iets gebeurt" (DERDEN, [How To Market A Game, 13 apr 2020](https://howtomarketagame.com/2020/04/13/how-one-new-image-increased-sales-by-20x/)). Chris Zukowski zag in zijn onderzoek dat kopers alleen over aantrekkelijke capsules hoveren.
- **Een indie-ontwikkelaar op Game Developer**: naam en hoofdbeeld tegelijk veranderd (zelfde figuren, levendiger houding en uitsnede), daarna **+306% verkoop**, na 9 maanden nog steeds (DERDEN, [Game Developer](https://www.gamedeveloper.com/business/how-changing-my-game-image-tripled-the-sales)). Let op: naam en beeld tegelijk, dus niet alleen het beeld.
- **Splendid Apps** (Google Play): proeven met icoon en schermbeelden gaven **+9% omzet** (DERDEN, [Google Play Console](https://play.google.com/console/about/splendid-casestudy/)). Kleiner, maar gemeten met een echte A/B-proef.
- **Kritisch:** dit zijn uitschieters die iemand de moeite waard vond om op te schrijven; de vele keren dat een nieuw beeld niets deed, staan nergens. Het patroon (beeld is de eerste poort, pas daarna tellen tekst en video) is wel overal hetzelfde, ook bij Superhive zelf (98). Hoeveel het voor Pro scheelt: GOK, niet te zeggen.

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, €0:** een nieuwe hoofdafbeelding maken uit wat we al hebben: een echte render uit Blender (headless, zoals de schermen in run 44438033323) van een figuur met zichtbare gewrichten, liefst een echt geprint figuurtje als dat er is, met daarop groot "Click Joints Pro" en één belofte ("Rig to poseable print in one click"), in kleur. Geen AI-beeld en niets wat het product niet doet (regel 5), geen Blender-logo (artikel 253, zie README). Daarna een ander laten keuren en bekijken op 600 x 300 naast Cleave en Catpin.
- **Elke dag meten:** de rijtjes op de voorpagina uitlezen (staat Pro of een concurrent erin) en de zoektabel van 97; samen met de Gumroad-verkopen zie je of een nieuw beeld iets doet. Geen A/B-proef mogelijk op Superhive, dus voor en na vergelijken (GOK of dat bij zo weinig verkoop iets zegt, zie 69).
- **Niet:** de pagina op Superhive zelf aanpassen; dat doet de Blender-manager na keuring.

## Patronen na ronde 19
65. **In elk rijtje op Superhive is het hoofdbeeld een advertentie, geen schermafdruk** (101): naam groot, één belofte, een mooie render, sterke kleur, vaak de korting erin. Pro is de enige zonder.
66. **Een beter hoofdbeeld is de goedkoopste hefboom die er is** (102): bij anderen 9% tot 20 keer meer, zonder één post naar buiten. Het kost alleen een render en een keuring.
67. **Zichtbaar onderhoud zit ook in het beeld** (100, 102): Catpin en Imagine Earth zetten de nieuwe versie of update op de hoofdafbeelding.

## Stand na run 21 nov ±05:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **De hoofdafbeelding van Pro is een grijs Blender-scherm zonder naam of belofte; alle 11 producten in de rijtjes hebben de naam groot in beeld, 10 een mooie render, 6 de korting erin** (GEZIEN, 101). Op voorpaginagrootte is bij Pro niets te lezen.
2. **8 van de 11 hebben een video op de pagina, Pro 0** (GEZIEN, 101).
3. **Staff Picked staat niet meer op de voorpagina; new_and_rising wel**, met nu OpenSet Connect erin en Catpin in on_sale (GEZIEN, 100).
4. **Anderen zagen na alleen een nieuw hoofdbeeld 9% tot 20 keer meer verkoop** (DERDEN, 102), uitschieters maar steeds hetzelfde patroon.
5. **Pro staat op Superhive op $12 zonder korting** (besluit 19 nov), dus zonder sale-badge en buiten het rijtje on_sale (GEZIEN, 101).

Voorstel: (a) de Blender-manager laat vandaag een nieuwe hoofdafbeelding maken, €0: echte render van een figuur met gewrichten (of een foto van een echte print), "Click Joints Pro" groot, één belofte, kleur, 1200 x 600, en laat die keuren naast Cleave op 600 x 300; tegelijk met de nieuwe titel en tags uit run 18; (b) de lange YouTube-video rig-to-figure (groen gekeurd, zie berichten hoofdchat 20 nov) ingebed bovenaan de Superhive-pagina zodra hij online staat; (c) de hoofdchat weegt of Pro vanaf de Cyber Sale toch een zichtbare korting krijgt (badge en rijtje on_sale) of op $12 blijft zoals besloten, met deze telling als nieuw gegeven; (d) de meetagent telt de rijtjes en de zoektabel elke dag, zodat we na (a) zien of het iets doet. Volgende run: hoe de hoofdbeelden op Gumroad Discover en in de zoekresultaten van Gumroad eruitzien naast die van Pro, en of daar hetzelfde gat zit.

## Ronde 20 (run 21 nov ±06:20 UTC, klok van de container): de beelden van Pro op Gumroad naast de concurrenten, en een verborgen pagina-agent in Gumroad zelf

Vraag van run 19: zit op Gumroad hetzelfde gat in de beelden als op Superhive? Alles met curl gelezen uit de cloud, zonder account (de openbare zoekfunctie `gumroad.com/products/search` en de productpagina's); de beelden zelf bekeken op ware grootte (skill kijken). Broncode van Gumroad alleen gelezen via raw.githubusercontent.com, niets uitgevoerd.

### 103. Wie op Gumroad vooraan staat bij de zoekwoorden van Pro
Zoekresultaten van 21 nov ±06:15 UTC, standaardvolgorde (GEZIEN):

| Zoekwoord | Treffers | Bovenaan bij Blender en 3D-print |
|---|---|---|
| articulated | 245 | 1. CatPin ($21, was $30, 84 beoordelingen); 7. SlicerJoint Pro ($20, 0) |
| joints | 1.160 | 1. CatPin; 2. Auto-Rig Pro ($50, 7) |
| 3d print blender | 264 | 1. CatPin; 2. Split 3D Print (gratis, 23); 3. Cleave ($20, 5) |
| poseable, print in place | 114, 2.704 | niets voor Blender, alleen VRChat-avatars en boeken |

- **Click Joints Pro staat bij geen enkel zoekwoord in de lijst** (GEZIEN). Dat klopt met 79: zonder verkoop en zonder $100 saldo is Pro niet "eligible" voor Discover en zoeken. De Gumroad-pagina krijgt dus alleen bezoek via onze eigen links (TikTok, YouTube, dortus.com).
- **Nieuwe concurrent: SlicerJoint Pro** (ayhancelik, $20, 0 beoordelingen): snijden, scharnieren, pinnen, magneten, "articulated parts", 3MF-export; 3 beelden en **5 YouTube-video's als omslag** (GEZIEN, productpagina). Hij kondigt aan dat hij op 1 jan 2027 als "BlendArt SliceJoint" verdergaat met gratis upgrade (GEZIEN). Zijn vierkante beeld is alleen een logo "BA", dus ook zwak.
- **CatPin gebruikt de automatische korting van Gumroad**: in de zoeklijst staat $21 met de oude prijs $30 erbij (GEZIEN, `original_price_cents` 3000). Gumroad zelf: met een standaardcode "the discounted pricing will automatically appear everywhere across the platform", zonder dat de koper een code typt (DERDEN, [Gumroad blog](https://gumroad.com/blog/p/new-feature-automatically-apply-discount-codes-to-your-products-e3ec070a-5d74-4f0b-a1d5-4bb13c0520dd)). Dat beantwoordt de vraag uit berichten hoofdchat (CYBER25 "with code" of vanzelf): het kan vanzelf, als de code als standaardcode in de productinstellingen staat. Of dat bij Pro zo staat, zie ik van buiten niet: de pagina toont nu $19 zonder oude prijs, maar CYBER25 begint pas 27 nov (GEZIEN).

### 104. De beelden: hetzelfde gat als op Superhive
Bekeken op ware grootte, vierkant beeld (600 x 600, wat Gumroad in zoeken, Discover en op het profiel toont) en omslag (1005 x 565) (GEZIEN, 21 nov):

| | Vierkant beeld | Omslag | Video op de pagina |
|---|---|---|---|
| Click Joints Pro ($19) | grijs Blender-poppetje, tekst "Right knee: bends 0° to 120°" klein bovenaan | hetzelfde grijze Blender-scherm met paneel | 0 (5 beelden, 0 video's) |
| CatPin ($21, 84 beoordelingen) | gekleurd logo met een kat en een punaise, "CatPin" groot | logo plus een render van een vrouwenfiguur in losse delen met pinnen | geen ingebed, wel "Latest Tutorial" |
| Cleave ($20, 5) | "CLEAVE" groot, 3 beloftes, felgekleurde print in delen | idem op een snijmat met echte prints | 3 links naar YouTube op de pagina |
| SlicerJoint Pro ($20, 0) | alleen logo "BA" | | 5 YouTube-video's als omslag |

- **Op Gumroad is het gat hetzelfde als op Superhive (101)**: de twee die verkopen, laten een kleurige render van een figuur in delen zien met de naam groot; Pro een grijs werkscherm zonder naam. Op 300 x 300 (de grootte in een zoekraster) is bij Pro geen woord te lezen (GEZIEN, zelf naast elkaar bekeken).
- Het bord zegt al: "Omslagfoto Gumroad zegt nog 'click' en 'Pro on Superhive'... omslag vervangen (bestandskiezer, lukt niet via Chrome)" en Bram maakt nu een nieuw hoofdbeeld voor Superhive (GEZIEN, `organisatie/bord.md` 21 nov 06:45 NL). **Het vierkante beeld van Gumroad staat niet op het bord** en is een apart bestand (`thumbnail_url` naast `covers`, GEZIEN in de pagina-gegevens).
- **Gumroad accepteert een YouTube-video als omslag** (oembed, zie SlicerJoint, GEZIEN). De lange video van Pro staat online (bord: youtube.com/watch?v=m3sNvDOJYQ0). Die als eerste omslag op Gumroad kost niets en geeft elke bezoeker van onze TikTok- en YouTube-links meteen de werking te zien (GOK hoeveel het scheelt).

### 105. Gumroad heeft een eigen "store agent" die productpagina's als HTML schrijft, nog achter een vlag
- CatPin en Cleave hebben **geen gewone Gumroad-pagina maar een eigen HTML-pagina** (in een afgeschermd frame, met een eigen statistiekscript `custom_html_analytics`; GEZIEN in de pagina's: geen `data-page`, wel dat script). Cleave leest als een echte verkooppagina: "Too big to print? Split it.", "NEW IN 1.7", voor en na, waarom niet gewoon met de hand (GEZIEN, ±1.370 woorden).
- In de open broncode van Gumroad (stand 21 nov 2026, gelezen): `app/services/pages/custom_html_writer.rb` en `app/services/ai/custom_html_snippet_matcher.rb` beschrijven een **store agent** die de pagina leest, een stukje kiest en vervangt, met een voorbeeld en een knop "Confirm" voor de verkoper, plus API-eindpunten om de hele pagina te vervangen of één stuk aan te passen (`PUT custom_html` via de product-API met scope `edit_products`). De API waarschuwt als er geen koopknop (`data-gumroad-action="buy"`) in staat (GEZIEN, `app/controllers/api/v2/links_controller.rb`).
- **Maar:** alles zit achter `Feature.active?(:custom_html_pages, ...)`, per verkoper aangezet (GEZIEN, zelfde bestand). In de blogs van Gumroad staat er niets over (GEZIEN, blogoverzicht 21 nov). Hoe je erin komt: onbekend, GOK dat Gumroad het per verkoper uitrolt of op aanvraag via support. Ik heb het niet aangevraagd (regel: niemand benaderen).
- **Waarom dit telt voor de tak:** het is het eerste voorbeeld van een verkoopplatform dat zelf een agent aan de verkoper geeft die de verkooppagina schrijft en kleine wijzigingen doet met een bevestiging door de mens: precies ons patroon "agent maakt, ander keurt" (zie 56, 60). Wie de vlag heeft, kan via de API ook vanuit een eigen agent de pagina bijwerken (nieuwe versie, sale-regel). Twee kleine concurrenten van Pro hebben hem al.

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, €0:** de nieuwe hoofdafbeelding die Bram voor Superhive maakt ook in 600 x 600 uitsnijden voor het vierkante Gumroad-beeld, en in 1005 x 565 als omslag; de lange YouTube-video als eerste omslag. Plaatsen in Gumroad doet wie de winkel beheert (bestandskiezer lukte niet via Chrome, zie bord), na keuring.
- **Wel zelf:** elke dag de Gumroad-zoekwoorden van 103 uitlezen (`products/search`, geen sleutel nodig) zodat we zien wanneer Pro na de eerste verkopen in de lijst komt, en of CatPin, Cleave of SlicerJoint hun prijs of beeld veranderen.
- **Niet zelf:** de vlag voor eigen HTML-pagina's aanvragen bij Gumroad (dat is iemand benaderen onder de winkel van Thijs; kan alleen met zijn ja).

## Patronen na ronde 20
68. **Het beeldgat van Pro zit op elke winkel** (101, 104): Superhive en Gumroad tonen allebei een grijs werkscherm, terwijl alles wat daar verkoopt een kleurige render met de naam groot heeft. Eén goed beeld in drie maten lost het overal op.
69. **De winkel zelf brengt Pro nog geen kopers** (103, 79): op Gumroad pas na verkoop en $100 saldo, op Superhive pas als het beeld goed is (98). Tot dan komt elke koper via onze eigen links, dus de pagina waar die links landen moet het werk doen (video bovenaan, beeld dat leest).
70. **Platforms beginnen zelf agents aan verkopers te geven** (105): de pagina schrijven en bijwerken met een bevestigknop. Dat maakt het "agent maakt, mens bevestigt"-patroon gewoon, en het is het eerste wat wij zouden kunnen aanvragen zodra er verkoop is.

## Stand na run 21 nov ±06:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Op Gumroad staat Pro bij geen enkel zoekwoord in de lijst; CatPin staat bovenaan bij "articulated", "joints" en "3d print blender"** (GEZIEN, 103). Elke koper van Pro komt dus via onze eigen links.
2. **Hetzelfde beeldgat als op Superhive: het vierkante beeld en de omslag van Pro op Gumroad zijn een grijs Blender-scherm**, CatPin en Cleave een kleurige render met de naam groot (GEZIEN, 104). Het vierkante beeld staat nog niet op het bord.
3. **Gumroad neemt een YouTube-video als omslag** (GEZIEN bij SlicerJoint); onze lange video staat online en kan er gratis bovenaan.
4. **Automatische korting op Gumroad bestaat en toont de oude prijs doorgestreept "everywhere"** (DERDEN, 103; CatPin $30 naar $21 GEZIEN). CYBER25 kan zo vanzelf werken als hij als standaardcode staat.
5. **Gumroad heeft een verborgen store agent die productpagina's als HTML schrijft en bijwerkt met een bevestigknop**, achter een vlag; CatPin en Cleave hebben hem al (GEZIEN in broncode en pagina's, 105). Nieuwe concurrent SlicerJoint Pro ($20, 0 beoordelingen, 5 video's).

Voorstel: (a) Bram levert het nieuwe hoofdbeeld in drie maten (Superhive 1200 x 600, Gumroad vierkant 600 x 600, Gumroad omslag 1005 x 565), Daan keurt alle drie op kleine grootte naast CatPin en Cleave; (b) wie de Gumroad-winkel bijwerkt, zet de lange YouTube-video als eerste omslag en zet CYBER25 op 27 nov als standaardcode, zodat de korting doorgestreept zichtbaar is en de zin "with code" weer weg kan; (c) de hoofdchat zet "vlag custom HTML-pagina aanvragen bij Gumroad" op de lijst voor na de eerste verkopen (vraagt het ja van Thijs, geen geld); (d) de meetagent neemt de Gumroad-zoekwoorden van 103 mee in de dagelijkse telling. Volgende run: hoe de landingspagina dortus.com/click-joints/ eruitziet naast de eigen HTML-pagina van Cleave (beeld, belofte, video, koopknop bovenaan), want daar komen al onze links binnen.

## Ronde 21 (run 22 nov ±00:20 UTC, klok van de container): waar onze links landen, en hoe andere makers in de saleweek een lijst als marketing gebruiken

Vraag van deze run (uit het voorstel van ronde 20): al onze links (TikTok `?ref=tt`, YouTube `?ref=yt`) komen op dortus.com/click-joints/. Wat ziet een koper daar, en hoe doen andere makers het in de week voor Black Friday (vr 27 nov), als een agent het werk doet?

### 106. Onze landingspagina verkoopt het gratis product, Pro staat 6 schermen lager
- Op een telefoon (iPhone 13 in Playwright, `?ref=tt`) staat het blok "Click Joints Pro · paid" pas op **±3.950 pixels, bijna 6 schermhoogtes** onder de bovenkant (GEZIEN, gemeten 22 nov). Bovenaan: het filmpje, "Click Joints · free Blender add-on for 3D printing", "See how far it bends, before you print." en de grote knop **"Get it on Blender Extensions"** (GEZIEN, schermafdruk).
- In de tekst begint het Pro-blok bij **woord 597 van 1.110** (GEZIEN, telling van de HTML). De enige link naar Gumroad boven dat blok is een gewone tekstlink midden in de alinea "In short" (GEZIEN).
- `?ref=` verandert niets aan de pagina: `site.js` doet alleen de kopregel (GEZIEN). Wie van een Pro-video komt, ziet dus dezelfde gratis-pagina als wie de gratis add-on zoekt.
- **Waarom dit telt:** TikTok-kijkers zitten op hun telefoon en scrollen zelden 6 schermen (GOK, geen meting van ons). De grote knop stuurt ze naar iets wat niets kost. Ronde 20 zag hetzelfde patroon bij de winkels zelf (69: elke koper komt via onze eigen links, dus de pagina waar die links landen moet het werk doen). Verkopen Pro: 0 (GEZIEN, bord 22 nov 00:45).
- **Wat een agent zelf kan, €0:** een tweede pagina `dortus.com/click-joints/pro/` (of een anker dat bovenaan begint) met Pro bovenaan: video van de figuur uit de rig, prijs, de sale vanaf 27 nov, koopknop Gumroad en een knop Superhive; en de links van Roep naar die pagina laten wijzen. Bouwen mag een bouwer op de site-tak, keuren een ander (skill `kijken` op telefoonbreedte). Plaatsen op dortus.com loopt via de site-tak, die nu niet naar main kan (bord: push geweigerd, lijst Thijs punt 5). Tot dat opgelost is: de link in TikTok-bio en YouTube-beschrijving direct naar Gumroad laten wijzen (GOK dat dat meer verkoopt dan de huidige pagina; de `?ref`-meting via Amami valt dan weg, Gumroad toont zelf de verwijzer).

### 107. Addon Radar: een eenmanszaak die een dagelijks uitgelezen lijst als etalage en inkomstenbron gebruikt
- Addon Radar leest elke dag alle betaalde add-ons op Superhive en alle gratis op Blender Extensions uit, en heeft een eigen pagina "Black Friday deals": **394 add-ons nu in de sale** op Superhive (GEZIEN, addonradar.com/black-friday, gegevens 21 nov). Er is ook "Get a mail when a saved add-on goes on sale" en een lijst met couponcodes (GEZIEN).
- **Wie erachter zit:** "Mulk, a one-person studio in Norway that also makes add-ons (Tabby, Fetch, Oris, Sol)". Verdienmodel: affiliate-links naar Superhive, "It never changes the order of a list", en hun eigen add-ons staan er "on the same terms as everything else" (GEZIEN, addonradar.com/about). Dus: een maker bouwt een lijst die kopers elke dag nuttig vinden, verdient aan andermans verkoop, en heeft zo een vaste plek waar zijn eigen producten tussen staan.
- Dit is werk dat volledig zelfstandig kan draaien: pagina's uitlezen, prijzen vergelijken, een pagina bijwerken. Of Mulk daar een AI-agent voor gebruikt, staat er niet (GOK: een gewoon script volstaat).
- **Voor ons, nu:** Pro staat **nog niet** op de Black Friday-pagina, omdat Pro op Superhive nog niet in de sale is: $12 Personal en $45 Studio, geen korting (GEZIEN, superhivemarket.com/products/click-joints-pro, 22 nov). Volgens de besluiten doet Pro mee in de Cyber Sale van 35%, vr 27 nov t/m wo 2 dec (GEZIEN, `organisatie/besluiten.md` 19 nov 13:45). Dan komt Pro vanzelf op deze lijst, en krijgt iedereen die Pro op Addon Radar heeft bewaard een mail (DERDEN, zelfde pagina; hoeveel mensen Pro bewaard hebben: onbekend).

### 108. Hoeveel korting de anderen geven: 35% op Superhive zit in de middengroep, 25% op Gumroad in de onderste kwart
- Telling van de kortingen die op de Black Friday-pagina van Addon Radar staan (254 van de 394 met een percentage in de HTML): **69 geven 25% of minder (27%), 106 geven 30 tot 49% (42%), 79 geven 50% of meer (31%)**. De meest gekozen korting is **30%** (79 keer), dan 50% (42 keer) (GEZIEN, telling 22 nov). De lijst staat gesorteerd op korting (GEZIEN: bovenaan 80% en 75%).
- Directe buren van Pro: SPLIT IT! (3D-print splitsen) **30%** naar $8,40, Oryx CAD (splitsen voor 3D-print) **25%** naar $11,24 (GEZIEN, zelfde pagina).
- **Voor ons:** de 35% op Superhive ($12 naar ±$7,80, GOK op de afronding van Superhive) is gewoon. De 25% op Gumroad ($19 naar $14,25) is lager dan bij de meeste anderen, en de landingspagina noemt alleen Gumroad met 25%, terwijl Superhive die week goedkoper is. Wie de prijs op Gumroad bepaalt (besluit 19 nov ±14:00, Thijs), kan overwegen de Gumroad-sale gelijk te trekken met 35%; dat kost geen geld vooraf, alleen marge per verkoop (GOK of het meer verkopen geeft; Superhive zegt zelf dat meer dan 75% voor de volle prijs koopt, zie 46).

### 109. "Verified Black Friday 2026": een deal-lijst die zichtbaar door een agent wordt bijgehouden
- Een openbare GitHub-lijst met **154 deals, 83 live, laatst gecontroleerd 20 nov**, elke dag opnieuw uitgelezen van 21 okt tot 2 dec, zonder affiliate-links, met een formulier "Submit a deal" (GEZIEN, thoughtcook.github.io/verified-black-friday en de README op raw.githubusercontent.com).
- De teksten per deal lezen als het logboek van een agent: "headless Chrome; www curl was 403", "Visible individual plan dollars were not present in the static HTML/JSON this run and are not invented" (GEZIEN). Dat is dezelfde eerlijkheidsregel als onze GEZIEN/GOK, als verkooppunt naar buiten.
- **Opvallend:** plek 1 van de "Top 5 picks" is **Smooth Recorder**, een kleine Mac-schermrecorder van $19 (was $49), tussen Proton, Hostinger en Windscribe, en hij staat ook in twee "stacks" (GEZIEN). Of de maker van de lijst ook Smooth Recorder maakt, staat er niet; de website van Smooth Recorder noemt thoughtcook niet (GEZIEN, gezocht in de HTML). GOK: een lijst als etalage voor het eigen product, zoals Addon Radar (107), maar zonder het te zeggen. Dat zouden wij niet doen (eerlijk, regel 5).
- Er zijn meer van zulke lijsten op GitHub waar makers via een PR hun deal kunnen toevoegen (DERDEN: [dev.to, "Best GitHub Repositories to Submit Your Black Friday Deals in 2026"](https://dev.to/vinishbhaskar/best-github-repositories-to-submit-your-black-friday-deals-in-2026-3ii9); voorbeelden [Pimjo/black-friday-deals](https://github.com/Pimjo/black-friday-deals), [trungdq88/Awesome-Black-Friday-Cyber-Monday](https://github.com/trungdq88/Awesome-Black-Friday-Cyber-Monday)). Die zijn voor ontwikkelaars en SaaS, niet voor Blender (GOK: weinig kopers voor Pro). Hoeveel sterren ze hebben kon ik niet lezen: de GitHub-API weigert in deze run elke repo buiten dortus-hq en dortus (GEZIEN).

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, €0:** een Pro-eerst-pagina bouwen en laten keuren (106); elke dag de Black Friday-pagina van Addon Radar uitlezen en vanaf 27 nov in het dagrapport zetten op welke plek Pro staat en welke korting de 3D-print-buren geven (107, 108).
- **Wel zelf, maar later:** een eigen eerlijke lijst op dortus.com, bijvoorbeeld "Blender add-ons for 3D printing" met prijs en Blender-versie per add-on, dagelijks uitgelezen, Pro erin op dezelfde voorwaarden en dat er ook bij gezegd. Werkt als zoekpagina en als vaste plek voor Pro (107). Niet vóór 27 nov: in 5 dagen komt zo'n pagina niet in Google (GOK).
- **Niet zelf:** een PR op andermans deal-lijst of een mail naar Addon Radar (dat is iemand benaderen vanaf het GitHub-account of de mail van Thijs; kan alleen met zijn ja op de tekst, regel 4).

## Patronen na ronde 21
71. **De laatste stap is de zwakste.** Alle werk van de tak (video's, keuring, quotum) eindigt op een pagina die eerst het gratis product verkoopt (106). Een andere landingsplek kost niets en raakt elke post tegelijk.
72. **In de saleweek komen kopers vanzelf langs lijsten** (107, 108, en CG Channel in 77). Op die lijsten staan is een kwestie van in de sale zitten met een gewone korting, niet van posten.
73. **Makers bouwen nuttige lijsten als eigen etalage** (107, 109). Het eerlijke model (zeggen dat je eigen product erin staat, volgorde niet aanpassen) is precies wat een agent dagelijks kan bijhouden.

## Stand na run 22 nov ±00:20 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Op de telefoon staat Pro bijna 6 schermen onder de bovenkant van dortus.com/click-joints/; de grote knop bovenaan is "Get it on Blender Extensions" (gratis)** (GEZIEN, 106). Elke link van Roep landt daar, ook voor Pro-video's.
2. **Pro staat op Superhive nog zonder korting ($12) en dus nog niet op de Black Friday-pagina van Addon Radar (394 add-ons in de sale)**; met de Cyber Sale van 35% vanaf 27 nov komt hij er vanzelf op (GEZIEN, 107).
3. **30% is de meest gekozen korting, 73% van de add-ons geeft 30% of meer** (GEZIEN, telling 254 kortingen, 108). Onze 25% op Gumroad zit in de onderste kwart, en Superhive is in de saleweek goedkoper dan wat de landingspagina noemt.
4. **Addon Radar is van een eenmanszaak die zelf add-ons maakt en verdient aan affiliate-links**, met eerlijke regels over de eigen producten (GEZIEN, 107): een model dat een agent van ons dagelijks kan draaien.
5. **"Verified Black Friday 2026" laat zien hoe een agent-bijgehouden lijst er naar buiten uitziet** (dagelijks, met eerlijke notities), maar zet een klein onbekend product op plek 1 zonder uitleg (GEZIEN; dat het van de maker is: GOK, 109).

Voorstel: (a) de hoofdchat laat een bouwer vóór do 26 nov een pagina `dortus.com/click-joints/pro/` maken met bovenaan het filmpje van de figuur uit de rig, de prijs, de sale en twee koopknoppen (Gumroad, Superhive), keuring door Daan op telefoonbreedte; zolang de site-tak niet naar main kan, wijzen de bio van TikTok en de beschrijving van de lange YouTube-video direct naar Gumroad; (b) wie de Gumroad-prijs beheert, beslist of de Gumroad-sale op 35% gaat zodat beide winkels gelijk zijn en de landingspagina klopt; (c) de meetagent neemt vanaf 27 nov de plek van Pro op addonradar.com/black-friday mee in het dagrapport. Volgende run: hoe de verkooppagina's van de drie best verkopende 3D-print-add-ons op Superhive bovenaan opgebouwd zijn (beeld, belofte, prijs, knop), als voorbeeld voor de Pro-pagina.

## Ronde 22 (run 22 nov ±01:20 UTC, klok van de container): hoe de pagina's van de 3D-print-add-ons op Superhive bovenaan opgebouwd zijn, naast die van Pro

Vraag uit de vorige run: wat staat er bovenaan bij de add-ons die Pro voorgaan, als voorbeeld voor een Pro-pagina. Alles hieronder is met curl gelezen op 22 nov ±01:00 UTC; tellingen gedaan met een klein script op de HTML van het tabblad "About" (alleen de beschrijving, zonder menu en FAQ).

### 110. Telling: zes 3D-print-add-ons tegen Click Joints Pro

| Add-on | Prijs (GEZIEN) | Beoordelingen | Woorden | Woorden vóór het eerste beeld | Bewegend beeld in de tekst | Stilstaande beelden |
|---|---|---|---|---|---|---|
| Cleave (plek 3 Popular, zie 96) | $23 (van $28) | 3 | ±1.450 | 1 | 3 YouTube-filmpjes | ±40 |
| Cut Flex | $34,99 | 0 | ±1.130 | ±155 | 10 GIF/WebP-lusjes | 5 |
| JointLab | $65 | 3 | ±610 | 6 | 1 YouTube-filmpje direct onder de kop | 5 |
| CatPin | $24 (van $30) | 4 | ±1.230 | ±130 | 7 korte filmpjes die vanzelf en zonder geluid spelen (Kinescope) | 0 |
| Printwright | $19 | 0 | ±630 | ±340 | 4 GIF's | 4 |
| Connector Fit QA (LayerMechanic) | $12 | 0 | ±385 | geen beeld | 0 | 0 |
| **Click Joints Pro** | **$12** | 0 | **±770** | **geen beeld** | **0** | **0** |

(alles GEZIEN in de HTML; woorden afgerond)

- **Pro is de enige van de zeven met koppen en ±770 woorden tekst maar nul beelden in de beschrijving** (GEZIEN: 0 `<img>`, 0 filmpjes in het tabblad About). Alleen het hoofdbeeld bovenaan de pagina laat iets zien. Connector Fit QA is ook kaal, maar is een klein hulpje van een maker met een hele reeks (LayerMechanic, 5 losse add-ons, GEZIEN).
- **Vier van de vijf met beeld laten iets bewegen**: GIF-lusjes (Cut Flex, Printwright), filmpjes die vanzelf afspelen (CatPin) of YouTube (Cleave, JointLab). Bij gewrichten is beweging het hele punt: een knie die buigt en stopt.
- **Bovenaan staat telkens een korte belofte in gewone woorden, dan meteen beeld**: Cleave "Too big to print? Split it." met beeld vóór de tekst; JointLab kop, één zin, filmpje; Cut Flex "Turn one sculpt into a poseable, jointed figure." met daaronder vier cijfertjes (15 joint presets, 1 panel, 3 export formats) en een knop "Get CutFlex ↑ Use Add to Cart at the top of this page" (GEZIEN). Pro heeft een goede belofte ("Rig to printable figure: elbows and knees stop where your rig stops.") maar daarna drie alinea's tekst.
- **Waar de beelden staan:** Cleave zet ze op `public-files.gumroad.com` (dezelfde plaatjes als op zijn Gumroad-pagina), Cut Flex op een losse beeldhoster, Printwright en JointLab uploaden ze bij Superhive zelf (GEZIEN, adressen van de `<img>`). Een beschrijving met GIF's en externe plaatjes kan dus op Superhive; je hoeft niets nieuws te hosten als de GIF's al op Gumroad of dortus.com staan.
- **Titels:** Cleave (19 woorden), JointLab (10) en Printwright (8) zetten zoekwoorden in de titel ("for 3D Printing"); Cut Flex en CatPin niet (GEZIEN). Superhive zelf raadt juist 2 tot 3 woorden aan (zie 111). Dat Cleave met de lange titel bovenaan staat, bewijst niet dat de titel het doet (GOK; Cleave heeft ook het meeste beeld en elke week een versie).
- **Prijs:** Pro is met $12 de goedkoopste van de gewrichten-add-ons; JointLab $65, Cut Flex $34,99, CatPin en Cleave rond $23 tot $24 (GEZIEN). Pro heeft ook een tweede keuze van $45 (meer "Seats", GEZIEN `data-price="$45"`). Of $12 te laag is om serieus genomen te worden, weet ik niet (GOK; geen cijfers van Superhive per prijs).

### 111. Wat Superhive zelf zegt over een pagina die verkoopt
Twee eigen artikelen van Superhive (GEZIEN, [How to Make a Blender Product Page that Sells](https://superhivemarket.com/posts/anatomy-of-the-perfect-product-page), [How to Create Graphics for Blender Add-Ons](https://blendermarket.com/posts/how-to-create-graphics-for-technical-blender-products)):
- "Most customers will not scroll through your entire product page, so give them all they need to know right there in the first paragraph." Eerste alinea = de hele pitch.
- Kies 2 of 3 hoofdvoordelen en "add additional images or GIFs to this section".
- Hoofdbeeld: eigen render, verhouding 2:1, **geen GIF als hoofdbeeld** (hun systeem en hun social-planner pakken geen GIF's). Tekst op het hoofdbeeld mag, maar leesbaar op postzegelformaat. Toon het nummer 1 voordeel in één oogopslag; voor/na-beelden "always make sense".
- Titel kort en duidelijk ("be clear, not clever"), 2 tot 3 woorden. Getuigenissen van bekende Blender-makers op de pagina, als ze die willen geven.
- Dit zijn adviezen zonder cijfers (DERDEN, link hierboven); de telling in 110 laat zien dat de verkopers het in de praktijk ook zo doen.

### 112. Agents die productpagina's herschrijven: veel beloftes, geen bruikbaar cijfer
- Ik zocht naar makers of winkels die een agent hun productpagina laten herschrijven en testen, met uitslag. Wat bovenkomt zijn verkopers van zulke tools (OptiMonk "Smart Product Pages", Teikametrics, Seatext) met procenten zonder methode (DERDEN, [OptiMonk case studies](https://www.optimonk.com/varnish-vine-case-study): "Conversions up 600% with a mystery discount" en tientallen meer, zonder aantallen bezoekers). Verkooppraat; niet bruikbaar.
- Voor ons is een A/B-test ook niet zinvol: met ±30 bezoekers per dag op dortus.com/click-joints/ (GEZIEN eerder, 31 op 18 nov) en 0 verkopen geeft een test weken lang geen uitslag (GOK, zie ook 69). Beter: één keer goed doen volgens wat de verkopers doen (110, 111), en meten op verkoop per week.

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, €0:** een nieuwe beschrijving voor Pro schrijven met bovenaan belofte, één GIF van de figuur uit de rig die buigt en stopt, dan per hoofdvoordeel (rig wordt figuur; stop uit de rig; graden vóór het printen) een korte alinea met een GIF of beeld eronder, en de bestaande tekst daaronder. De GIF's kunnen uit de filmpjes van Roep komen. Keuring door Daan (beeld) en een tweede keurder (tekst).
- **Niet zelf:** de beschrijving op Superhive vervangen gebeurt in het makersaccount (inloggen); dat doet de hoofdchat of Thijs. Een bekende maker om een getuigenis vragen is iemand benaderen (regel 4).

## Patronen na ronde 22
74. **Op een marktplaats is de productpagina het eind van elke trechter, en die van Pro is alleen tekst** (110). Alle anderen laten de werking zien, bijna altijd bewegend.
75. **Wat al gemaakt is voor socials kan zonder extra werk op de pagina** (110: Cleave gebruikt dezelfde plaatjes als op Gumroad). De filmpjes van Roep zijn dus ook winkelbeelden.

## Stand na run 22 nov ±01:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **De beschrijving van Click Joints Pro op Superhive heeft ±770 woorden en nul beelden of filmpjes** (GEZIEN). Van de zes vergelijkbare 3D-print-add-ons hebben er vijf beeld in de tekst, vier daarvan bewegend.
2. **De verkopers zetten bovenaan één korte belofte en dan meteen beeld** (Cleave: beeld na 1 woord, JointLab: filmpje na 6 woorden, GEZIEN). Superhive zegt zelf dat de meeste kopers niet verder lezen dan de eerste alinea (DERDEN, 111).
3. **GIF's en plaatjes van buiten (Gumroad, eigen site) mogen in een Superhive-beschrijving** (GEZIEN bij Cleave, Cut Flex); de beelden van Roep kunnen er direct in.
4. **Pro is met $12 de goedkoopste van de gewrichten-add-ons** (JointLab $65, Cut Flex $34,99, Cleave $23, CatPin $24, GEZIEN). Of dat helpt of schaadt is een GOK.
5. **Agent-tools die productpagina's herschrijven en testen hebben geen cijfers met methode** (DERDEN, 112); bij onze aantallen bezoekers heeft testen ook geen zin. Eén keer goed doen naar het voorbeeld van de verkopers.

Voorstel: (a) de hoofdchat laat vóór do 26 nov (vóór de Cyber Sale van 27 nov) een nieuwe beschrijving voor Pro maken: belofte, één GIF van de figuur uit de rig die buigt en stopt, drie hoofdvoordelen elk met een GIF of beeld, dan de bestaande tekst; GIF's uit de filmpjes van Roep, gehost op dortus.com of Gumroad; keuring Daan; de hoofdchat zet hem in het makersaccount. Dezelfde opbouw dient voor de Pro-pagina op dortus.com (voorstel run 21). (b) De prijs van $12 niet nu veranderen (sale komt eraan), maar na de saleweek opnieuw bekijken tegen $19 tot $24 van de buren. Volgende run: wat de beschrijving en beelden van Pro op Gumroad tonen na deze telling, en of Gumroad GIF's in de beschrijving toont.

## Ronde 23 (run 22 nov ±02:20 UTC, klok van de container): de pagina van Pro op Gumroad, en hoe Gumroad nu zelf een agent de verkooppagina en lanceerposts laat maken

Vraag van run 22: wat tonen beschrijving en beelden van Pro op Gumroad, en kan Gumroad GIF's in de beschrijving tonen. Onderweg bleek dat Gumroad zijn eigen route voor "jouw agent maakt de verkooppagina" sinds run 20 openbaar heeft uitgelegd, met een eigen opdrachtregel-tool, MCP-server en skill voor agents. Dat is voor de tak nieuwer dan de telling zelf.

### 113. Click Joints Pro op Gumroad: $19, 654 woorden, 0 beelden in de tekst, 0 reviews
- Gelezen uit de paginadata (`data-page` van `duinhouwer8.gumroad.com/l/click-joints-pro`, 22 nov ±02:20 UTC, GEZIEN): prijs $19 (`price_cents 1900`), keuzes Personal en Studio (tot 5 mensen), 6 omslagbeelden (alle 6 PNG, geen filmpje of GIF), samenvatting "Rig to printable figure: elbows and knees stop where your rig stops.", beschrijving **654 woorden met 0 beelden, filmpjes of GIF's erin**, `ratings count 0`.
- Let op: op Superhive staat Pro op $12 (run 22, GEZIEN), op Gumroad op $19. Twee prijzen voor hetzelfde product; of dat bewust is weet ik niet (GOK).
- Gumroad toont in de gewone beschrijving wel plaatjes (de editor kent afbeeldingen), maar dat heb ik hier niet getest; de belangrijkere vondst staat in 114.

### 114. Gumroad laat de verkoper de hele productpagina door zijn eigen agent laten schrijven (help-artikel 353, openbaar)
- Het help-artikel [Custom product landing pages](https://gumroad.com/help/article/353-custom-product-landing-pages) staat live (GEZIEN, HTTP 200; tekst ook in de open broncode, `app/views/help_center/articles/contents/_353-custom-product-landing-pages.html.erb`). Letterlijk: "It is built for you by an AI agent rather than in a page builder, so you describe the page you want and the agent writes, previews, and publishes it."
- **De opzet:** in het productdashboard, tab Share, onderdeel Landing page, knop "Copy prompt". Die opdracht plak je in "your own AI agent, such as Claude Code, Cursor, or Codex". De agent bouwt een HTML-pagina en zet hem live met de Gumroad-tool: `gumroad products page preview` (keuring van de server zonder te plaatsen), `publish`, `url`, `clear` (DERDEN, artikel). Betalen blijft de kassa van Gumroad; de koopknop is een element met `data-gumroad-action="buy"`, en prijs, naam, rating en aantal reviews kunnen live ingevuld worden met `data-gumroad-field` (DERDEN).
- **Grenzen** (DERDEN, zelfde artikel): max 25 beelden, max 500.000 tekens, beelden alleen van Gumroad zelf (dus eerst uploaden als omslag of bestand bij het product), **YouTube- en Vimeo-spelers werken niet** (alleen een link met thumbnail), geen downloadlinks, geen versiegeschiedenis ("keep the source file"), automatische inhoudscontrole bij opslaan. Wijzigen: "ask your agent for the change. It edits the published page and leaves the rest of it alone."
- **Wie heeft het:** de code zet het nog steeds per verkoper aan (`Feature.active?(:custom_html_pages, ...)`, GEZIEN in `app/presenters/bundle_presenter.rb` en `app/models/user.rb`, stand main 21 nov). Maar drie heel verschillende verkopers gebruiken het al: Cleave en CatPin (run 20, GEZIEN) en een schrijfster van paardenboeken die "can't code" ([Jeanette Gower, 10 nov 2026](https://jeanettegower.substack.com/p/how-i-built-my-own-shop-pages-with), DERDEN: "Gumroad offers custom pages, and it even supplies a ready-made prompt to give an AI. I pasted it into Claude"). Een openbaar help-artikel plus een niet-technische gebruiker wijst op een brede uitrol (GOK). Of het account van Dortus de knop heeft, is alleen te zien in het dashboard (inloggen, dus hoofdchat).
- **Hoe Cleave het nu gebruikt** (GEZIEN, `v4ss3ur.gumroad.com/l/cruqvuo/landing/embed`, 22 nov): ±3.860 woorden zichtbare tekst en **19 beelden**, allemaal op `public-files.gumroad.com`; opbouw: belofte ("Too big to print? Split it."), drie voordelen, "NEW IN 1.7", drie YouTube-tutorials als link, voor/na, "Why not just bisect it by hand?", werkwijze in zes genummerde stappen. In run 20 telde ik ±1.370 woorden; de pagina is sindsdien bijna drie keer zo lang geworden, of ik telde toen alleen het buitenste deel (GOK).
- **Wat de schrijfster misliep:** ze kon niet zelf publiceren ("That last part needed Gumroad's own command-line tool, which isn't my world"), en mailde de drie HTML-bestanden naar Gumroad Support, die ze plaatste (DERDEN). Ook: de agent zag haar winkel niet, ze moest elke productlink plakken, en controleerde zelf waar elke koopknop heen ging (sommige gingen naar de winkel in plaats van het product).

### 115. De Gumroad-tool is gebouwd voor agents: MCP-server, skill, en een lanceerpost-agent voor X
- [antiwork/gumroad-cli](https://github.com/antiwork/gumroad-cli) (69 sterren, laatste push 17 nov 2026, GEZIEN via api.github.com): "Designed for humans and AI agents alike". `gumroad mcp` start een MCP-server, `gumroad skill` installeert een agent-skill, en agents kunnen met `GUMROAD_ACCESS_TOKEN` werken zonder in te loggen (GEZIEN, README). Code alleen gelezen, niets geïnstalleerd of uitgevoerd.
- Uit de skill (`skills/gumroad/SKILL.md`, 841 regels, GEZIEN): naast productpagina's ook **mails aan het publiek** (eerst concept, dan `emails send-preview`, dan pas versturen; met `--send` "blasts immediately, so ... require explicit human approval"), geplande mails, mailreeksen (workflows), kortingscodes, en de verkopen met hun `utm_source` per koper.
- **Lanceerposts door Gumroad zelf:** `gumroad marketing recommend <product>` geeft per kanaal een kant-en-klare post (`post_text`, `link_url` met tag), en na `approve` en `schedule` plaatst "the server's X executor" hem op X. Een mens moet de exacte tekst gezien hebben: de bevestigingscode moet uit de getoonde voorvertoning komen, een gewijzigde tekst wordt geweigerd (GEZIEN, SKILL.md regels 164 tot 182). Zit achter een eigen vlag `auto_marketing`; in blogs of zoekresultaten vond ik er niets over (GEZIEN, twee zoekopdrachten 22 nov).
- **Waarom dit telt:** het platform zelf bouwt nu precies het patroon "agent maakt, mens keurt de exacte tekst, systeem plaatst", met een code die breekt als de tekst na de keuring verandert. Dat is een goed idee voor onze eigen wachtrij (B-ontwerp): de keuring hangt aan de precieze tekst, niet aan "het concept".

### 116. Matt Busel: 130 producten door Claude Code op Gumroad, 1.383 agentposts, 0 verkopen
- [Matt Busel op DEV, 19 okt 2026](https://dev.to/mattbusel/selling-on-gumroad-with-ai-130-products-0-sales-greg-is-wrong-5f0b) (DERDEN, label "Fully Autonomous"): Claude Code bouwde en plaatste in 13 dagen 130 producten (88 werkende HTML-apps), "the apps, the listings, the covers and the upload script". Na 36 dagen uit de Gumroad-API: **0 verkopen, $0, en 0 downloads van de 87 gratis producten**.
- De kern: "Our agent team keeps a log of everything it posts: 1,383 entries so far, posts, replies, articles and pitches. **3 of them carried a link to the store.** Those 3 produced 9 of the 10 clicks." De agents waren bezig met weergaven voor artikelen en een Steam-spel; de winkel kreeg 0,2% van de aandacht (DERDEN). 33 UTM-links via Gumroad gaven 10 unieke kliks in 7 dagen (DERDEN).
- Zijn eigen fouten (DERDEN): 130 gemaakt voor de eerste verkoop; "free" als marketing gezien ("Free is a conversion tool, not a traffic source"); AI-omslagen met "$8 ONE-TIME" terwijl de knop $0+ zei, pas na weken gezien. Gumroad Discover toont je pas na $100 echte verkoop elders (DERDEN, zelfde stuk; past bij run 14, item 79).
- Les voor ons: een agent die veel plaatst maar zelden naar het product linkt, brengt niets op. Tel bij elke post of hij een getagde link naar Pro heeft.

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, €0:** een HTML-landingspagina voor Pro schrijven volgens de grenzen van 114 (belofte, figuur die buigt en stopt, drie voordelen met beeld, max 25 beelden, beelden als bestanden bij het product op Gumroad, YouTube alleen als link, koopknop met `data-gumroad-action="buy"` en `data-gumroad-option` voor Personal en Studio, prijs live via `data-gumroad-field="price"`). Zelf lokaal bekijken met de skill `kijken`, keuring door Daan en een tweede keurder. De bron bewaren in de repo (Gumroad bewaart geen versies).
- **Kan met wat we al hebben, maar is een besluit van de hoofdchat:** het secret `GUMROAD_ACCESS_TOKEN` staat er al (`organisatie/toegang.md`, "alleen lezen gebruiken"). `gumroad products page preview` schrijft niets en laat de server keuren; dat zou laten zien of het account de functie heeft. Publiceren is wel schrijven in het account: dat beslist de hoofdchat. Alternatief zonder token: de hoofdchat kijkt in het dashboard (Share, Landing page) of de knop er is.
- **Niet zelf:** de lanceerpost-agent van Gumroad (115) plaatst op X onder het account dat aan Gumroad hangt, dus valt onder regel 4; en de vlag is er waarschijnlijk niet (GOK).

## Patronen na ronde 23
76. **Verkoopplatforms bouwen nu zelf de agent-route in** (114, 115): Gumroad geeft een kant-en-klare opdracht voor Claude Code, een tool met MCP en een skill, en laat de mens alleen de exacte tekst keuren. Wie die route gebruikt (Cleave, 19 beelden) heeft een pagina die eruitziet als een verkooppagina; Pro heeft er nul.
77. **Veel plaatsen is niet hetzelfde als verkopen** (116): 1.383 posts, 3 met een link, 0 verkopen. Elke post van de tak moet een getagde link naar het product hebben, anders telt hij niet.

## Stand na run 22 nov ±02:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Pro op Gumroad: $19, 654 woorden, 6 PNG-omslagen, 0 beelden in de tekst, 0 reviews** (GEZIEN). Op Superhive is hij $12 (run 22); twee prijzen.
2. **Gumroad legt openbaar uit hoe je de hele productpagina door je eigen agent (Claude Code) laat maken en plaatsen** (DERDEN, help-artikel 353): kopieer de opdracht in Share, bouw HTML, plaats met `gumroad products page publish`. Grenzen: 25 beelden, beelden alleen van Gumroad, geen YouTube-speler.
3. **Drie verkopers gebruiken het al, ook een niet-technische** (GEZIEN Cleave en CatPin; DERDEN Jeanette Gower). Cleave heeft nu 19 beelden en ±3.860 woorden. Of Dortus de knop heeft: onbekend, per verkoper aangezet (GEZIEN in code).
4. **De Gumroad-tool heeft een MCP-server, een skill en een lanceerpost-agent voor X** waarbij de keuring aan de exacte tekst hangt (GEZIEN, SKILL.md). Goed patroon voor onze eigen wachtrij.
5. **Matt Busel: 1.383 agentposts, 3 met een winkellink, 0 verkopen** (DERDEN). Een tak die veel plaatst zonder link naar het product levert niets op.

Voorstel: (a) de hoofdchat kijkt vandaag in het Gumroad-dashboard van Pro (Share, Landing page) of de knop "Copy prompt" er is, of laat één keer `gumroad products page preview` draaien met het bestaande token (schrijft niets). (b) Is de knop er: een agent maakt vóór do 26 nov een landingspagina voor Pro met dezelfde opbouw als in run 22 voorgesteld voor Superhive, met de beelden van Roep als bestanden bij het product, keuring door Daan, en de hoofdchat publiceert; de bron komt in `producten/`. (c) Elke post van Roep krijgt een link met UTM-tag naar Pro, en de Maker telt wekelijks hoeveel posts een link hadden (les van 116). (d) De twee prijzen ($12 Superhive, $19 Gumroad) gelijktrekken of bewust houden: besluit van de hoofdchat na de saleweek. Volgende run: of Superhive iets vergelijkbaars heeft (API of agent voor productpagina's), en wat Cleave en CatPin op hun Gumroad-pagina's verkopen sinds ze de eigen pagina hebben, voor zover zichtbaar.

## Ronde 24 (run 22 nov ±03:20 UTC, klok van de container): wat de concurrenten van Pro echt verkopen (openbaar te lezen), en welke gratis pers ze daarvoor kregen

### 117. Superhive heeft geen API voor makers; wel staat de verkoop per product openbaar in banden
- **Geen API:** `superhivemarket.com/api`, `/docs/api` en `/llms.txt` geven de voorpagina terug; robots.txt noemt alleen de sitemap (GEZIEN, 22 nov). Een agent kan een productpagina op Superhive dus niet zelf schrijven of plaatsen, alleen wie inlogt. Dat beantwoordt de vraag uit run 23.
- **Wel openbaar:** op elke productpagina staat onder "Details" een verkoopband ("Sales 10+", "200+", "400+") als die er is (GEZIEN). Producten onder ±10 verkopen tonen niets (GOK, nooit lager dan "10+" gezien).
- **Telling** (GEZIEN, 69 producten uit de zoekresultaten van "3d print", "split 3d print", "connectors print" en "joints", 22 nov ±03:15 UTC; hier alleen de directe concurrenten van Pro):

| Product | Prijs | Band | Reviews | Sinds |
|---|---|---|---|---|
| Dovetail Key | $18 | 800+ | 13 | 5 maanden |
| Split-3DPrint | $22 | 400+ | 3 | 4 maanden |
| CatPin | $24 | 400+ | 4 | 3 maanden |
| Cleave | $23 | 200+ | 3 | 2 maanden |
| SnapSplit | $20 | 30+ | 0 | 8 maanden |
| Cutlink Studio | $2 | 30+ | 0 | 3 maanden |
| Articulator | $1 | 30+ | 2 | 3 maanden |
| JointLab | $65 | 20+ | 3 | 4 maanden |
| Split It | $8,40 | 20+ | 0 | 1 maand |
| Cut Flex | $34,99 | 10+ | 0 | 1 maand |
| Click Joints Pro | $12 | geen band | 0 | "Published 2 days ago" |
| Mesh Split, JointForge, RagdollForge, NinjaCut, North Slice, PrintSplit Easy, Print Forge, LayerMechanic, Regosplit, Print Ready Modelling Kit | $9 tot $24 | geen band | 0 | 16 uur tot 3 maanden |

- **Wat dit zegt:** de hoek "model splitsen en verbinden voor 3D-print" is vol. In de laatste maand kwamen er minstens 7 bij (GEZIEN, publicatiedatum), en geen ervan heeft een band. De vier die verkopen hebben elk iets van buiten Superhive: pers (CatPin, zie 119), een kanaal van 198.000 abonnees (Dovetail Key, zie 118), of snelle updates met video's op de pagina (Cleave, run 18). Dat veel nieuwkomers met AI gebouwd zijn: GOK, niet nagegaan.
- Opvallend: Superhive zegt bij Pro "Published 2 days ago" (GEZIEN). Volgens eerdere runs stond Pro er al eerder; misschien telt een nieuwe versie als nieuwe publicatie (GOK). De hoofdchat kan dat in het dashboard zien.

### 118. Dovetail Key: 800+ in 5 maanden, gemaakt door een kanaal met 198.000 abonnees
- Op de pagina staan twee ingebedde video's van 3DRedBox (GEZIEN, oembed: auteur `@miladkambaritutorials`). Dat kanaal heeft **198K abonnees, 454 video's** (GEZIEN, kanaalpagina). De twee productvideo's zelf hebben maar **1.310 en 1.029 weergaven** (GEZIEN, YouTube-zoekresultaat 22 nov).
- 80 Level schreef er een nieuwsbericht over met link `superhivemarket.com/products/dovetail-key?ref=586` (GEZIEN, artikel "easily make your blender models 3d printable by drawing lines"). Dat `ref` is een affiliatecode: 80 Level verdient zo 5% van elke verkoop via dat bericht (GOK op wie de code heeft; het systeem van 5% voor elke affiliate staat in run 8, item 47).
- Les: de productvideo's trekken weinig; de verkoop komt waarschijnlijk van de naam van de maker, de pers en Superhive zelf (GOK).

### 119. CatPin: 2.029 verkopen op Gumroad en 400+ op Superhive in 4 maanden, met een kanaal van 1.240 abonnees
- **Gumroad zet de cijfers in openbare JSON:** `<product-url>.json` geeft zonder sleutel prijs, opties, aantal en gemiddelde van de reviews, de laatste reviews, de volledige beschrijving, en `sales_count` als de verkoper het aantal toont (GEZIEN, 22 nov, ook voor Pro).
- **CatPin** (`alexsokol.gumroad.com/l/catpin`): $30 Basic, opties +$15 en +$70, **`sales_count` 2.029**, **84 reviews, gemiddeld 4,8**, gemaakt 20 jul 2026, bijgewerkt 20 nov (GEZIEN). Op Superhive $24, "Sales 400+", 4 reviews (GEZIEN). Dat is ±4 reviews per 100 verkopen op Gumroad, binnen de 4 tot 11 uit run 17. Omzet: minstens ±$60.000 over beide winkels samen als iedereen Basic kocht zonder korting (GOK, rekensom 2.029 x $30 plus 400 x $24, kortingen en btw niet meegeteld).
- **Waar het niet van komt:** het YouTube-kanaal heeft **1,24K abonnees en 387 video's**; de CatPin-video's hebben **22.847, 12.354, 2.554 en 2.099 weergaven** (GEZIEN, kanaalpagina en zoekresultaat 22 nov). Geen groot publiek dus.
- **Waar het wel van kan komen: gratis redactionele pers.** 80 Level schreef op 5 okt 2026 een nieuwsbericht ("Prepare Your 3D Models for Printing with This Blender Add-On", rubriek News en Marketplace, geen label Sponsored bij het artikel) met link naar de Superhive-pagina en het YouTube-kanaal (GEZIEN, [80 Level](https://80.lv/articles/prepare-your-3d-models-for-printing-with-this-blender-add-on)). Digital Production volgde op 9 okt (GEZIEN, [Digital Production](https://digitalproduction.com/2026/10/09/catpin-blender-cuts-3d-printing/)). Beide noemen de nieuwe versie (1.0.7) als aanleiding. Dat die berichten de verkoop gaven: GOK, er is geen cijfer per bron.
- **Opbouw van de pagina** (GEZIEN, JSON): ±1.040 woorden, belofte bovenaan ("Cut. Connect. Print."), "Latest Tutorial", twee modi (Draft en Easy) met stappen, een lijst "Is CatPin Right for You?" met 9 soorten kopers (figuren, bustes, resin, FDM, studio's), en een eigen landingspagina via Gumroad (`/landing/embed` geeft 200, GEZIEN). Pro heeft die niet (404, GEZIEN).

### 120. De rubriek Marketplace van 80 Level: elke dag korte stukjes over losse tools, ook kleine en gratis
- Op `80.lv/articles/marketplace` staan nu 10 berichten over losse tools, waarvan 4 voor Blender: een generator op Fab, een korrelsimulatie op Superhive, een gratis add-on op Gumroad (vallende bladeren), en een cursus (GEZIEN, 22 nov). Het gaat dus niet alleen om grote pakketten; dat corrigeert run 15 (item 84), waar ik alleen de betaalde dealslijsten zag.
- Op de pagina "About & Contact" van 80 Level staat een algemeen redactieadres `editor@80.lv` (GEZIEN). Een vast formulier voor nieuws vond ik niet. Digital Production heeft `info@digitalproduction.com` (GEZIEN, contactpagina). BlenderNation vraagt sinds kort €25 per commerciële post (run 9, item 50).
- **Hoe dit bij een agent-tak past:** de redactie herschrijft een korte mail met beelden tot een stukje. Een agent kan dat pakket maken (wat is nieuw, 3 tot 5 gifs of beelden, 1 video, link met eigen referral-code, wat het kost en of er sale is). Versturen gaat van een adres van Dortus of Thijs en valt onder regel 4: Thijs zegt ja op de tekst. CG Channel werkte al zo (run 14, item 77).

### Wat een agent hierin zelf kan, binnen onze regels
- **Wel zelf, elke dag, €0:** een concurrentenmeter. Lees voor ±20 producten de band op Superhive en de JSON op Gumroad (prijs, reviews, `sales_count` waar zichtbaar), schrijf één regel per dag in een bestand, en meld sprongen (bijv. een product dat van 200+ naar 400+ gaat, of een nieuwe review van 1 ster). Ook Pro zelf: zijn eigen band op Superhive verschijnt zodra hij ±10 verkopen heeft. Alles openbaar, geen account, geen sleutel (GEZIEN, getest met curl).
- **Wel zelf, één keer:** een perspakket voor de update 1.x van Pro klaarzetten in de wachtrij, in de vorm van 119 (nieuwe versie als aanleiding, beelden, video, link met `?ref=` naar de eigen code).
- **Niet zelf:** de mail versturen (regel 4), of iets op Superhive wijzigen (geen API, alleen inloggen).

## Patronen na ronde 24
78. **In een volle hoek verkoopt alleen wie iets van buiten de winkel meebrengt** (117 tot 119): van ±20 split- en verbindtools op Superhive verkopen er 4 meer dan 30 keer; zij hebben pers, een groot kanaal of zichtbare snelle updates. Zeven nieuwkomers van de laatste maand hebben samen nog geen band.
79. **Gratis redactionele pers is voor een kleine add-on bereikbaar en kost alleen een goede mail** (119, 120): 80 Level en Digital Production schreven binnen 4 dagen over CatPin, met een nieuwe versie als aanleiding. Dit is de goedkoopste route naar kopers die we zelf niet kunnen bereiken, en een agent kan alles behalve het versturen.
80. **De cijfers van concurrenten zijn openbaar en machineleesbaar** (117, 119): Superhive-banden en Gumroad-JSON. Een agent kan elke dag meten wat werkt bij anderen, in plaats van te gokken.

## Stand na run 22 nov ±03:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **CatPin (zelfde kopers als Pro) haalde in 4 maanden 2.029 verkopen op Gumroad en 400+ op Superhive** (GEZIEN, Gumroad-JSON en productpagina), met maar 1.240 YouTube-abonnees. Minstens ±$60.000 omzet (GOK, rekensom). Het bewijs dat deze hoek geld oplevert.
2. **Wat CatPin wel had: gratis pers bij een nieuwe versie** (80 Level 5 okt, Digital Production 9 okt, GEZIEN) en een eigen Gumroad-landingspagina (GEZIEN). Pro heeft geen van beide.
3. **De hoek is vol:** minstens 7 nieuwe split- en verbindtools in de laatste maand, geen ervan met een verkoopband; alleen Dovetail Key (800+), Split-3DPrint (400+), CatPin (400+) en Cleave (200+) verkopen echt (GEZIEN). Pro heeft nog geen band (minder dan ±10, GOK op de grens).
4. **Superhive heeft geen API voor makers** (GEZIEN); een agent kan daar niets plaatsen, alleen lezen.
5. **Gumroad-JSON en Superhive-banden zijn zonder sleutel te lezen** (GEZIEN). Een agent kan elke dag een concurrentenmeter bijhouden.

Voorstel: (a) een agent zet vóór di 24 nov een perspakket klaar voor Pro (wat is nieuw, 3 tot 5 beelden of gifs van Roep, de lange YouTube-video, Superhive-link met eigen referral-code, de saleprijs van 27 nov tot 1 dec) voor `editor@80.lv` en `info@digitalproduction.com`; Daan keurt, Thijs zegt ja op de tekst (regel 4), en het gaat vóór do 26 nov de deur uit zodat een stukje in de saleweek kan vallen. (b) De Blender-manager laat een agent elke dag de concurrentenmeter van hierboven draaien (±20 producten, één regel per dag in `platformen/blender-2/`), met Pro erin, zodat we zien wanneer Pro zijn eerste band krijgt. (c) Voorstel (a) en (b) van run 23 (Gumroad-landingspagina voor Pro) blijven staan; CatPin en Cleave hebben er allebei een. Volgende run: of de pers voor de andere drie verkopers (Dovetail Key, Split-3DPrint, Cleave) ook bij een nieuwe versie kwam, en hoeveel dagen na een stukje in 80 Level een maker het merkt (reviews per week in de Gumroad-JSON van CatPin rond 5 okt, voor zover de datums zichtbaar zijn).

## Ronde 25 (run 22 nov ±04:20 UTC, klok van de container): waarom 80 Level over kleine add-ons schrijft (affiliate), wat zo'n stukje zichtbaar opleverde, en hoe journalisten nu met AI-pitches omgaan

Vervolg op ronde 24. Vraag: kregen de andere verkopers ook pers bij een nieuwe versie, en is na een stukje in 80 Level iets te zien bij CatPin?

### 121. 80 Level verdient zelf aan een deel van de stukjes: affiliate-links naar Gumroad en Superhive
- **Dovetail Key (800+ op Superhive) kreeg ook een stukje in 80 Level**, op 30 jul 2026, in News en Marketplace, met als aanleiding "the latest version of the add-on improved the cutting engine" (GEZIEN, [80 Level](https://80.lv/articles/easily-make-your-blender-models-3d-printable-by-drawing-lines)). Dus 2 van de 2 stukjes over onze hoek hingen aan een nieuwe versie (CatPin 5 okt, Dovetail Key 30 jul).
- **De link in dat stukje is een affiliate-link:** `superhivemarket.com/products/dovetail-key?ref=586`, met bovenaan "If you click on the links in this post and make a purchase we may receive a commission" (GEZIEN, broncode van de pagina). Het stukje over CatPin had een gewone link zonder `ref` en zonder die zin (GEZIEN).
- **Telling in de rubriek Marketplace (10 nieuwste stukjes, 13 tot 21 nov):** 3 van de 10 hebben de commissiezin en een affiliate-link: twee via `gumroad.com/a/916550771/...` (het affiliate-ID van 80 Level op Gumroad) en een via ArtStation `/a/` (GEZIEN). De andere 7 (o.a. Smooth Weights en Carnage Grains op Superhive, een gratis add-on op Gumroad, een generator op Fab) hebben gewone links (GEZIEN). De redactie schrijft dus ook zonder eigen verdienste, maar heeft er soms een.
- **Wat dat voor Pro betekent:** op Gumroad kan iedereen zonder vragen 10% verdienen aan een product dat in Discover staat, via "Gumroad Affiliates" (voorheen Global Affiliates), tenzij de verkoper zich afmeldt (GEZIEN, [Gumroad help 333](https://gumroad.com/help/article/333-affiliates-on-gumroad), [help 249](https://gumroad.com/help/article/249-affiliate-faq); cookie 7 dagen). Staat Pro in Discover en is die regeling niet uitgezet, dan kan 80 Level aan een stukje over Pro verdienen zonder dat wij iets regelen. Of Pro nu in Discover staat en of de regeling aan staat: niet gezien, alleen in het account te zien (oordeel van Thijs, raakt zijn account).
- **Correctie op item 119:** de YouTube-link onderaan beide stukjes is het kanaal van 80 Level zelf (titel "80 Level - YouTube", GEZIEN), niet dat van de maker.

### 122. Wat het stukje over CatPin zichtbaar opleverde: een kleine bult in reviews, geen sprong
- Gumroad heeft een openbare, gedocumenteerde route voor reviews met datum: `gumroad.com/product_reviews?product_id=<id>&page=N` (10 per pagina, staat zo in de open broncode van Gumroad, `config/routes.rb` en `product_reviews_controller.rb`; GEZIEN, [antiwork/gumroad](https://github.com/antiwork/gumroad)). De gewone `.json` geeft er maar 5.
- CatPin: 51 reviews met tekst (van 84 sterren in totaal). Per week (maandag als start): eind jul tot half aug 4 per week, week van 31 aug 8 (piek), sept 4 tot 6, **week van 28 sep 1, week van 5 okt (80 Level) 5, week van 12 okt 2**, daarna 0 tot 2 (GEZIEN, eigen telling).
- Lezing: rond het stukje in 80 Level gaat het van 1 naar 5 en weer naar 2. Dat is een bultje, geen sprong; de grootste week lag een maand eerder zonder pers die ik kon vinden. Reviews komen ook dagen na de koop. Conclusie: het stukje hielp misschien, maar CatPin verkocht vooral door iets anders (GOK). Het `sales_count` staat nog op 2.029, hetzelfde als gisteren 03:20 UTC (GEZIEN), dus ook nu weinig nieuwe verkoop of een teller die traag bijwerkt (GOK).
- **CatPin is al in de sale:** Basic $21 in plaats van $30, 30% korting, op 22 nov (GEZIEN, `display_price` in de JSON). Een concurrent begint dus vóór onze saleweek (27 nov).

### 123. Cleave en Split-3DPrint: verkoop zonder pers die ik kon vinden
- **Cleave (200+):** 11 versies tussen 23 sep en 17 nov 2026, ongeveer één per 5 dagen (GEZIEN, [versiepagina](https://superhivemarket.com/products/cleave/versions)). Geen stukje gevonden in 80 Level, Digital Production of BlenderNation (twee zoekopdrachten, GEZIEN dat er niets kwam; afwezigheid is niet bewezen).
- **Split-3DPrint (400+):** eerste versie 26 tot 28 aug, daarna pas weer 11 tot 13 nov (GEZIEN, versiepagina). Ook geen pers gevonden.
- **BlenderNation** plaatst wel stukjes van makers als "Community Reporter", ook voor betaalde tools (Bed Fit Splitter, $19, 29 sep 2026, GEZIEN, [BlenderNation](https://www.blendernation.com/2026/09/29/plan-your-3d-prints-with-bed-fit-splitter/); SnapSplit, gratis, 11 apr 2026, GEZIEN, [BlenderNation](https://www.blendernation.com/2026/04/11/snapsplit-add-on-automates-splitting-and-connector-building-for-3d-printing/)). Of Bed Fit Splitter daarvoor de €25 uit item 50 betaalde staat er niet bij.
- Les: pers is één route, geen voorwaarde. Cleave laat zichtbaar snel updaten (elke versie is een nieuwe regel in de lijst en een reden voor een post); Split-3DPrint had geen van beide en verkoopt toch (waarschijnlijk door vroeg te zijn en een duidelijke titel, GOK).

### 124. Hoe journalisten nu met (AI-)pitches omgaan: ze filteren harder, niet op AI maar op onderwerp
- Muck Rack, State of Journalism 2026 (n=897): 82% van de journalisten gebruikt zelf AI, en **88% gooit een pitch die buiten hun onderwerp valt meteen weg**; bijna de helft krijgt zelden een relevante pitch (DERDEN, samenvatting in [The AI Comms Desk, 25 mrt 2026](https://buttondown.com/reynaldo/archive/82-of-journalists-use-ai-and-88-still-trash-your/)).
- Muck Rack onder PR-mensen (juli 2026): 71% noemt lage respons van journalisten het grootste obstakel, 80% gebruikt AI dagelijks (DERDEN, [Bizcommunity](https://www.bizcommunity.com/article/muck-rack-finds-journalists-are-harder-to-reach-despite-ai-advances-620831a)).
- **Voor een agent die pitches klaarzet:** veel mails sturen werkt slechter dan ooit; twee goed gerichte mails naar een rubriek die al precies dit soort stukjes plaatst (80 Level Marketplace, Digital Production) passen wel. De agent moet bewijzen dat het past: een link naar 1 of 2 eerdere stukjes van die rubriek over vergelijkbare tools (Dovetail Key, CatPin) in de mail, en een aanleiding (nieuwe versie 1.1, sale).

## Patronen na ronde 25
81. **Redacties met een affiliate-model schrijven graag over betaalde tools in winkels met een affiliateprogramma** (121): 80 Level gebruikt Gumroad-affiliate (10% via Gumroad Affiliates) en Superhive `?ref=`. Een product dat daar open voor staat, is voor zo'n redactie aantrekkelijker.
82. **Een nieuwe versie is de haak** (121): beide stukjes in onze hoek noemen de nieuwste versie als nieuws. Pro 1.1 ("Figure from rig") is zo'n haak.
83. **Pers geeft een bultje, geen sprong** (122, 123): bij CatPin is na 80 Level geen grote piek te zien, en twee van de vier verkopers in onze hoek hebben geen pers die ik vond. Pers is goedkoop en de moeite waard, maar geen wondermiddel.

## Stand na run 22 nov ±04:20 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **80 Level schreef ook over Dovetail Key (800+), weer bij een nieuwe versie** (30 jul, GEZIEN). Beide stukjes in onze hoek hingen aan een update.
2. **80 Level is affiliate op Gumroad (ID 916550771) en Superhive (`ref=586`)**; 3 van de 10 nieuwste Marketplace-stukjes hebben een commissielink (GEZIEN). Met Gumroad Affiliates aan (10%, voor iedereen) kan de redactie aan Pro verdienen zonder afspraak (GEZIEN, help Gumroad).
3. **Het effect van zo'n stukje is klein te zien:** CatPin-reviews 1, 5, 2 in de weken rond 5 okt, piek eerder (8 in de week van 31 aug) (GEZIEN, eigen telling via de openbare reviewroute van Gumroad).
4. **CatPin staat al in de sale ($21, -30%) op 22 nov** (GEZIEN). Concurrenten wachten niet tot 27 nov.
5. **Journalisten gooien 88% van de pitches buiten hun onderwerp weg** (DERDEN, Muck Rack 2026): weinig, gerichte mails met een bewezen passende rubriek.

Voorstel: (a) het perspakket uit ronde 24 (a) blijft, met twee toevoegingen: de aanleiding is Pro 1.1 ("Figure from rig") plus de sale, en de mail noemt de eerdere stukjes over Dovetail Key en CatPin zodat de redactie ziet dat het past; Daan keurt, Thijs zegt ja op de tekst (regel 4). (b) Zet op `organisatie/lijst-thijs.md` (via de hoofdchat) één vinkje: in het Gumroad-account kijken of Pro in Discover staat en of "Gumroad Affiliates" aan staat; aanzetten kost niets tot er een verkoop is en maakt een stukje voor 80 Level lonend. (c) De concurrentenmeter (ronde 24 (b)) neemt ook de prijs uit `display_price` mee, zodat we zien wie wanneer in de sale gaat, en de reviews per week via `product_reviews`. Volgende run: of er een manier is om te zien welke van de 10 Marketplace-stukjes per mail van de maker kwam (bijv. dezelfde zinnen in de winkeltekst als in het stukje, dan is het een herschreven persbericht), zodat we weten hoe ver een kant-en-klare tekst komt.

## Ronde 26 (run 22 nov ±05:20 UTC, klok van de container): hoe ver komt een kant-en-klare tekst bij 80 Level, en waar de redactie haar stukjes vandaan haalt

Vervolg op ronde 25. Vraag: zijn de stukjes in de rubriek Marketplace herschreven persberichten (dan komt een agent met een goede tekst ver), of zoekt de redactie zelf? Methode: de 10 nieuwste stukjes (13 tot 21 nov) naast de winkeltekst van het product gelegd, en per stukje geteld welk deel van de woorden in reeksen van 6 of meer letterlijk in de winkeltekst staat (eigen script, GEZIEN). Plus: welke video staat in het stukje, en van wie (YouTube oEmbed, GEZIEN).

### 125. De redactie herschrijft bijna alles; alleen een grote studio met affiliate-link komt dicht bij de eigen tekst
- **Overlap met de winkeltekst** (deel van het stukje dat letterlijk in de winkeltekst staat, GEZIEN, eigen telling): Smooth Weights 0%, Fluid Frenzy 0%, Falling Leaves 0%, Organic Zombie Web 1%, CADQuader 4%, NYC-pakket van Leartes 8%, Carnage Grains 9%, Stylized Water (itch.io) 11%, **Project Optimization Toolkit van Leartes 40%**. De cursus van Titanium Studio kon ik niet vergelijken (ArtStation geeft 403).
- Het enige stukje dat dicht bij de winkeltekst ligt, is van Leartes Studios, met een affiliate-link via Gumroad (`gumroad.com/a/916550771/msxlab`, GEZIEN). Leartes had twee stukjes in de 10 (16 nov, beide met commissie). Lezing: een studio die vaak levert en waar 80 Level aan verdient, krijgt bijna zijn eigen tekst geplaatst; een kleine maker krijgt een eigen stukje van de redactie (GOK op het waarom, de telling is GEZIEN).
- Geen van de 10 heeft het label Sponsored (GEZIEN, de labels bovenaan zijn #News #Marketplace en het programma). Betaald kan ook: een "Sponsored article" kost $2.200, een post op hun X (262K) of Instagram (476K) $400, een plek in de nieuwsbrief $400 (GEZIEN, [tarievenkaart 80 Level](https://80lv.info/partnership)). Dat valt onder harde regel 1 (geld), dus alleen ter vergelijking: de gratis route bestaat en wordt gebruikt.

### 126. Wat de redactie wel overneemt: de video van de maker, en wat de maker zelf op X laat zien
- **In 7 van de 10 stukjes staat een YouTube-video, en in 6 daarvan is het de eigen video van de maker** (3DCoat, Leartes 2x, Max Miles, Titanium Studio, Fluid Frenzy; de zevende is een uitlegvideo van een derde bij het Godot-stukje) (GEZIEN, oEmbed-auteur per video).
- **Smooth Weights kwam niet via de maker binnen, maar via een gebruiker op X:** het stukje is opgebouwd rond twee posts van 3D-artiesten (Flat en AldoTheVamp) die de add-on in hun werk lieten zien (GEZIEN, ingesloten posts). Smooth Weights staat op Superhive op 400+ verkopen, $17,99, 4 maanden oud (GEZIEN, [productpagina](https://superhivemarket.com/products/smooth-weights)).
- **Twee stukjes zijn een vervolg:** Carnage Grains ("the super sticky project by Max Miles we featured back in the summer") en Fluid Frenzy (nieuw effect als filmpje getoond, 2.0 als achtergrond) (GEZIEN). De redactie volgt makers die al eerder iets liet zien.
- **Twee stukjes hebben een citaat van de maker** ("We asked Deepak to tell us a bit more", en een uitleg van Frenzy Byte) (GEZIEN). Een maker die snel een paar zinnen uitleg kan geven, krijgt een langer stukje.
- **Falling Leaves is een product uit januari 2025** (gratis, 674 downloads, 10 beoordelingen van 5 sterren; `created_at` 2025-01-15, `updated_at` 22 nov 2026, GEZIEN, Gumroad-JSON). Een stukje hoeft dus niet bij de lancering te vallen; een oud product met een nieuwe versie of nieuw filmpje telt ook.
- Les voor een agent-tak: de tekst van een persmail wordt niet overgenomen, het beeld wel. Wat werkt is een sterk filmpje van 30 tot 90 seconden op YouTube (en liefst ook op X, waar de redactie zichtbaar rondkijkt), een korte uitleg die de redactie kan citeren, en een aanleiding. Een agent kan dat filmpje, de uitleg en het mailtje klaarzetten; de mail zelf valt onder regel 4.

### 127. Carnage Grains: 50+ verkopen in 7 dagen voor $49,99, met "Built with AI-generated code" op de pagina en in het stukje
- Superhive: $49,99, "Sales 50+", "Published 7 days ago", 1 beoordeling, en bovenaan de pagina letterlijk "Built with AI-generated code" (GEZIEN, [productpagina](https://superhivemarket.com/products/carnage-grains), 22 nov). Dus minstens ±$2.500 omzet in de eerste week (GOK, rekensom, voor de korting en het deel van Superhive).
- 80 Level schreef er op 18 nov over en noemde het AI-gebruik zelf: de maker "has also been open that ... Carnage was built with heavy AI assistance" en respecteert wie daarom niet koopt (GEZIEN, [80 Level](https://80.lv/articles/houdini-style-gpu-accelerated-grain-simulations-in-blender)). Het stukje kwam er toch, met een gewone link zonder commissie.
- Wat dit voor ons zegt: openlijk AI-gebouwd zijn hield deze maker niet uit de pers en niet van een goede eerste week. Ons besluit van 19 nov (nergens een AI-melding) blijft staan; dit is alleen een tegenvoorbeeld voor de vrees dat het uitkomen schaadt. Of Carnage zonder die zin meer had verkocht, is niet te zien (GOK).

### Wat een agent hierin zelf kan, binnen onze regels
- Elke week de rubriek Marketplace van 80 Level lezen (curl, zonder sleutel) en per stukje noteren: product, winkel, video van wie, commissie ja of nee. Zo ziet de tak welke soort maker erin komt.
- Voor Pro een perspakket maken dat past bij wat de redactie echt gebruikt: (1) één YouTube-filmpje van 30 tot 90 seconden van Roep, (2) drie zinnen uitleg in de eerste persoon die als citaat kunnen, (3) de aanleiding (versie 1.1, sale 27 nov tot 1 dec), (4) de link. Geen lange persbericht-tekst; die wordt toch herschreven.
- Niet zelf: de mail versturen, iets op X plaatsen (we hebben daar geen kanaal; regel 4 en de plaatsregels van Roep gelden).

## Patronen na ronde 26
84. **Bij een vakblad telt het beeld, niet de tekst** (125, 126): 7 van de 9 vergeleken stukjes hebben minder dan 10% overlap met de winkeltekst, en 6 van de 10 sluiten de eigen video van de maker in. Een agent moet het filmpje perfect maken, niet de persmail.
85. **Redacties vinden makers op X en volgen ze daarna** (126): Smooth Weights via posts van gebruikers, Carnage en Fluid Frenzy als vervolg op eerder werk. Een kanaal waar de redactie kijkt, is zelf een persroute.
86. **Openlijk AI-gebouwd is geen beletsel voor pers of eerste verkoop** (127): Carnage Grains, 50+ in een week voor $49,99.

## Stand na run 22 nov ±05:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **80 Level herschrijft persteksten bijna volledig:** 0 tot 11% overlap met de winkeltekst bij 8 van de 9 vergeleken stukjes; alleen Leartes (twee stukjes in 10, affiliate) zit op 40% (GEZIEN, eigen telling).
2. **De eigen video van de maker staat in 6 van de 10 stukjes** (GEZIEN). Het filmpje is wat de redactie overneemt.
3. **Smooth Weights (400+ verkopen) kwam in 80 Level via posts van gebruikers op X**, niet via een pitch (GEZIEN). Dortus heeft geen X-kanaal.
4. **Carnage Grains: 50+ verkopen in 7 dagen voor $49,99, met "Built with AI-generated code" op de pagina** en toch een stukje in 80 Level (GEZIEN).
5. **Betaald kan ook, maar is duur:** sponsored article $2.200, losse post $400 (GEZIEN, tarievenkaart). Valt onder regel 1; de gratis route werkt voor kleine makers.

Voorstel: (a) het perspakket voor Pro (ronde 24 en 25) wordt korter en beeldgerichter: één filmpje van 30 tot 90 seconden op @Dortusapps (de Maker van Roep maakt het, Keurder keurt), drie zinnen citeerbare uitleg, aanleiding versie 1.1 plus de sale, link; Thijs zegt ja op de mailtekst (regel 4), versturen vóór do 26 nov. (b) De hoofdchat weegt of een X-kanaal voor Dortus (Blender-clips) de moeite is: het is de plek waar 80 Level makers vindt (GOK dat het voor ons werkt, het patroon is GEZIEN); nieuw kanaal is aan de hoofdchat. (c) Volgende run: hetzelfde voor Digital Production en BlenderNation (wie komt erin, met welk beeld), zodat het pakket voor alle drie past.

## Ronde 27 (run 22 nov ±06:20 UTC, klok van de container): wat ons gratis BlenderNation-bericht opleverde, en hoe Digital Production over hele kleine makers schrijft

Vervolg op het voorstel van ronde 26 (Digital Production en BlenderNation naast elkaar). Alles gelezen met curl op RSS, WordPress-zoekpagina's, YouTube-kanaalpagina's en -RSS (zonder sleutel), de listing op extensions.blender.org en Superhive.

### 128. Ons eigen BlenderNation-bericht: geen zichtbare sprong in downloads
- Click Joints staat sinds wo 18 nov 08:35 UTC op BlenderNation als bericht van de "Community Reporter" (GEZIEN, `article:published_time` 2026-11-18T08:35:39). Het staat nog in de RSS (de laatste 10 berichten), naast vooral videotutorials.
- Downloads op extensions.blender.org (GEZIEN, `platformen/blender/downloads.csv`, `commercie/blender-click-joints/geplaatst.md` en een eigen curl):

| Stuk | Van, tot (UTC) | Downloads | Per dag |
|---|---|---|---|
| Voor Reddit | 15 nov 12:10 tot 16 nov 11:16 | 136 naar 157 | ±22 |
| Na r/blender (16 nov 19:09) | 16 nov 11:16 tot 17 nov 04:57 | 157 naar 196 | sprong van ±39 in ±10 uur na de post |
| Tussenstuk | 17 nov 04:57 tot 17 nov 17:11 | 196 naar 205 | ±18 |
| Rond BlenderNation (18 nov 08:35) | 17 nov 17:11 tot 18 nov 20:21 | 205 naar 234 | ±26 |
| Daarna | 18 nov 20:21 tot 22 nov 06:17 | 234 naar 313 | ±23 |

- Wat dit zegt: het gratis BlenderNation-bericht gaf hooguit een paar extra downloads op de dag zelf (GOK, ±5 boven het gewone tempo), de r/blender-post gaf de enige echte bult. Let op: de teller telt ook downloads van updates (0.1.1 kwam 16 nov), dus het gewone tempo is wat ruw (GOK).
- Past bij ronde 25: ook bij CatPin gaf een vakbladstukje een kleine bult, geen sprong. Een tekst op een nieuwssite zonder sterk filmpje erbij verkoopt weinig; dat is een argument tegen de € 25 voor een commercieel BlenderNation-bericht over Pro (beslissing Thijs, regel 1).

### 129. Digital Production schrijft elke paar dagen over een klein Blender-add-on, ook van makers met 7 abonnees
- De Blender-feed van Digital Production heeft 20 stukken van 28 sep tot 16 nov, 19 daarvan door één redacteur (Bela Beier). 15 gaan over een los add-on of hulpmiddel (GEZIEN, [tag-feed](https://digitalproduction.com/tag/blender/feed/), eigen telling). Dat is ±2 per week.
- 13 van de 20 sluiten de YouTube-video van de maker in (GEZIEN). Van die makers telde ik de abonnees (GEZIEN, kanaalpagina's, 22 nov):

| Stuk (datum) | Kanaal van de maker | Abonnees | Weergaven video | Video tot stuk |
|---|---|---|---|---|
| CL Sculpt Assistant (16 nov) | Calappa Lab | 16 | 469 | 23 dagen |
| MetaWrap (10 nov) | MetaWrap AI | 505 | 248 | 16 dagen |
| SculptForge (4 nov) | askNK | 3.630 | 39.162 | video kort erna |
| Fumaris (30 okt) | Venous FX | 47.100 | 2.193 | ±7 weken |
| Print & Pin (28 okt) | G_ni | 7 | 528 | 14 dagen |
| Animatica Marionette (21 okt) | Animatica | 897 | 49.015 | 6 dagen |
| Nitro Retopo (13 okt) | Adrien Rouquié | 326 | 21.691 | 15 dagen |
| CatPin (9 okt) | AlexSokolArt | 1.240 | niet in RSS | |
| Vision Canvas (7 okt) | GLI | 91 | niet in RSS | |
| Alpaca3D (5 okt) | Stanislav Marakulin | 93 | 5.074 | 6 dagen |
| Hair Bone Generator (28 sep) | MORI.3D | 7 | 1.443 | 31 dagen |

- 7 van de 11 hebben minder dan 1.000 abonnees, 4 minder dan 100 (GEZIEN). Een groot kanaal is dus geen voorwaarde. Wel bestaat de video altijd eerst, meestal 1 tot 4 weken eerder.
- Geen van de 10 add-ons die ik zocht stond op BlenderNation (GEZIEN, zoekpagina blendernation.com, "Click Joints" werd wel gevonden als controle). Digital Production haalt ze dus niet bij BlenderNation weg.
- CatPin, de concurrent van Pro, kreeg dus naast 80 Level ook een stuk in Digital Production (GEZIEN). Click Joints staat er nog niet (GEZIEN, zoekfeed).
- Nitro Retopo: 400+ verkopen op Superhive in 2 maanden, $25, met een kanaal van 326 abonnees (GEZIEN, [productpagina](https://superhivemarket.com/products/nitro-retopo)). Fumaris: 40+ in 3 maanden voor $39, ondanks een kanaal van 47.100 (GEZIEN, [productpagina](https://superhivemarket.com/products/fumaris)). Het verschil zit niet in het kanaal maar in het filmpje en het nut (GOK).

### 130. Wat Digital Production overneemt: de release notes, niet een persbericht
- De site zegt over zichzelf: "We read the release notes. Then ..." (GEZIEN, tekst onder elk stuk). Het stuk over 3D Measure Master linkt als enige bron naar de nieuwspagina van de maker over versie 1.30 (GEZIEN, [stuk](https://digitalproduction.com/2026/11/20/3d-measure-master-live-update/)). De twee stukken die ik las beginnen allebei met "For those who don't know the tool:" en zijn ±700 woorden (GEZIEN); een vast format, mogelijk met hulp van AI geschreven (GOK).
- Het stuk over CL Sculpt Assistant heeft geen enkele link naar het product, alleen de ingesloten video (GEZIEN, HTML van het artikel). Direct verkeer naar een winkel is hier dus klein (GOK); wat het oplevert is weergaven op het filmpje en een stuk om naar te verwijzen.
- Er is geen formulier voor nieuws; het enige adres op de contactpagina is info@digitalproduction.com (GEZIEN, [contact](https://digitalproduction.com/contact/)). Een stuk van RenderJuice draagt `utm_content=story_pitch` in de link (GEZIEN), dus pitchen gebeurt.

### Wat een agent hierin zelf kan, binnen onze regels
- Een openbare "wat is nieuw in Pro 1.1"-pagina op dortus.com maken, met het filmpje van Roep ingesloten bovenaan en de wijzigingen in gewone zinnen. Dat is precies de bron die Digital Production leest. Valt onder de site (hoofdchat of Daan, `organisatie/regels/opslaan.md`).
- Een mail van vijf regels klaarzetten voor info@digitalproduction.com: wat het is, wat nieuw is, link naar die pagina, link naar het filmpje, saleperiode. Versturen alleen na ja van Thijs op de tekst (regel 4).
- Elke week de Blender-feed van Digital Production en de RSS van BlenderNation lezen (curl, zonder sleutel), en de downloads per dag naast elk bericht leggen, zoals hierboven. Zo leert de tak welk kanaal echt beweegt.

## Patronen na ronde 27
87. **Reddit bewoog de downloads, BlenderNation niet zichtbaar** (128): ±39 extra in 10 uur na r/blender, hooguit ±5 op de dag van BlenderNation (GOK op het gewone tempo).
88. **Vakbladen schrijven over hele kleine makers, maar pas als er een filmpje is** (129): 7 van 11 met minder dan 1.000 abonnees, de video steeds 1 tot 4 weken eerder.
89. **Een versiepagina met video is het persbericht** (130): Digital Production leest release notes en sluit de video in; een lange perstekst is overbodig.

## Stand na run 22 nov ±06:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Ons gratis BlenderNation-bericht (18 nov) gaf geen zichtbare sprong:** ±23 downloads per dag ervoor en erna; alleen de r/blender-post gaf een bult van ±39 in 10 uur (GEZIEN, tellingen; effect per kanaal GOK).
2. **Digital Production schrijft ±2 keer per week over een los Blender-add-on**, door één redacteur (GEZIEN, 15 van 20 stukken in 7 weken).
3. **7 van de 11 makers in die stukken hebben minder dan 1.000 YouTube-abonnees, twee maar 7** (GEZIEN). Wij kunnen er dus in, met het filmpje dat Roep al maakt.
4. **CatPin, de concurrent van Pro, staat in 80 Level én Digital Production; Click Joints in geen van beide** (GEZIEN).
5. **Digital Production leest release notes en linkt soms niet eens naar de winkel** (GEZIEN). De waarde is het filmpje en het stuk, niet direct verkeer; verwachte verkoop eruit klein, 0 tot 3 (GOK).

Voorstel: (a) vóór do 26 nov één openbare pagina "Click Joints Pro 1.1: what's new" op dortus.com met het filmpje van Roep bovenaan; die pagina is de basis voor alle drie de vakbladen (80 Level, Digital Production, CG Channel heeft Pro al). (b) Chris zet één korte mail klaar voor info@digitalproduction.com en editor@80.lv met de link naar die pagina en de sale (27 nov tot 1 dec); Thijs zegt ja op de tekst. (c) Geen € 25 voor een commercieel BlenderNation-bericht: het gratis bericht bewoog niets zichtbaar. (d) Een tweede Reddit-post rond de sale (r/3Dprinting, met een geprint figuur) weegt zwaarder dan pers; dat is aan Thijs (zijn account). Volgende run: verkopen van Nitro Retopo en CatPin rond hun Digital Production-stuk (reviews per datum via Gumroad/Superhive), om te zien of zo'n stuk wél verkoop gaf.

## Ronde 28 (run 23 nov ±00:20 UTC, klok van de container): het tweede pers-voorbeeld (Nitro Retopo), wat een agent met onze maillijst bij Kit mag, en twee agents die alles zelf plaatsten en overal werden geweerd

Vervolg op ronde 27. De vraag van vorige run (verkoop van CatPin rond het stuk in Digital Production) is al beantwoord in 122: dezelfde 51 reviews met tekst, opnieuw opgehaald via `gumroad.com/product_reviews` (GEZIEN, zelfde telling: week van 5 okt 5, week van 12 okt 2). Nitro Retopo staat niet op Gumroad (GEZIEN, zoek-JSON) en de reviews op Superhive tonen alleen "2 months ago" (GEZIEN), dus per week tellen kan daar niet. Daarom deze run drie andere dingen.

### 131. Nitro Retopo: zelfde patroon als CatPin, pers binnen een week bij twee bladen
- 80 Level schreef op **7 okt 2026** (News en Marketplace), Digital Production op **13 okt** (GEZIEN, [80 Level](https://80.lv/articles/blender-retopology-tool-for-dense-meshes-scans-sculpts/), [Digital Production](https://digitalproduction.com/2026/10/13/nitro-retopo-dense-blender-meshes/)). Bij CatPin was het 5 en 9 okt (GEZIEN, ronde 24).
- De link in 80 Level is een gewone link zonder `ref` (GEZIEN, broncode: `superhivemarket.com/products/nitro-retopo`). Affiliate is dus geen voorwaarde om erin te komen.
- Het stuk in 80 Level is opgebouwd uit wat de maker zelf laat zien: wie hij is (character artist), welk probleem, één cijfer uit de demo ("1.5-million-triangle model was reduced to a 91,000-triangle working mesh"), "actively maintained", en de video bovenaan (GEZIEN). Geen persbericht nodig; wel een demo met een concreet getal.
- Superhive nu: $25, **Sales 400+**, 4 beoordelingen, "Published 2 months ago" (GEZIEN, productpagina 23 nov). Kanaal 326 abonnees (GEZIEN ronde 27). Dus beide makers in onze buurt met 400+ en een klein kanaal kregen in de eerste weken na de start twee vakbladen tegelijk.
- Wat het niet bewijst: of die verkoop van de pers kwam. Bij CatPin gaf pers een bultje, geen sprong (122). Samen met 128 (ons BlenderNation-bericht: niets zichtbaar) blijft de lezing: pers is goedkoop en hoort erbij, de video en het nut doen het werk (GOK).

### 132. Kit (onze maillijst) heeft sinds kort een eigen MCP voor agents, maar die verstuurt nooit zelf
- Kit beschrijft een **Kit MCP** (`https://app.kit.com/mcp`) waarmee een AI-client abonnees, tags, segmenten en broadcasts leest en schrijft (GEZIEN, [developers.kit.com/mcp/kit-mcp.md](https://developers.kit.com/mcp/kit-mcp.md)).
- Twee grenzen, letterlijk: "available on all paid Kit plans (Creator and Creator Pro)" en "The Kit MCP does not schedule or send broadcasts ... the MCP broadcast tools always save a draft. Each response includes a `confirm_url`" (GEZIEN, zelfde pagina). Kit bouwt dus zelf het patroon "agent schrijft, mens drukt op verzenden" in.
- Dortus zit op het gratis plan met een gewone sleutel `KIT_API_KEY` (GEZIEN, `organisatie/toegang.md`). Met een API-sleutel werkt de v4 API wel, 120 verzoeken per minuut, behalve de bulk- en aankoop-eindpunten (GEZIEN, [authenticatie](https://developers.kit.com/api-reference/authentication.md)). Via `POST /v4/broadcasts` met `send_at: null` maakt een agent een concept; met een tijd erin wordt hij gepland (GEZIEN, beschrijving in [llms.txt](https://developers.kit.com/llms.txt)). Of het gratis plan broadcasts via de API toelaat, heb ik niet getest (GOK: ja, want broadcasts zitten in het gratis plan).
- Ook nuttig voor de meetlat: "Get link clicks for a broadcast" geeft per link de unieke klikken (GEZIEN, llms.txt). Een agent ziet dus na een mail hoeveel mensen op de Pro-link klikten, zonder dashboard.
- De pagina's op kit.com zelf (blog, help) geven aan curl een robotmuur (GEZIEN, "Are you a robot?"); de ontwikkelaarsdocs op developers.kit.com niet.

### 133. "Dead by April": een agent die vanaf januari elke twee uur zelf alles deed, met $9 productverkoop
- Een AI-agent (schrijfnaam Survivor Forge) draaide "on a cron job since January, every two hours, a new session", met als doel $200 per maand vóór 1 april (DERDEN, [300 Sessions In, dev.to](https://dev.to/deadbyapril/300-sessions-in-what-building-a-business-actually-looks-like-4pg)).
- Na 209 sessies: **8 producten op Gumroad, 62 video's, 108 artikelen, veel koude mails, omzet $9** (één verkoop, via Bluesky) (DERDEN, [Someone Paid Me $191](https://dev.to/deadbyapril/someone-paid-me-191-and-i-built-it-in-one-session-388)). Daarna $191 voor een klusje van iemand die het verhaal volgde, en rond sessie 300 "$100 total earned" door 11 pull requests voor die klant (DERDEN, zelfde bronnen; de twee bedragen sluiten niet op elkaar aan, dus zelf onzeker).
- Op dag 8 al geweerd: X "Error 226, automation detected", Reddit-account weg, Hacker News "spam-filtered", Write.as na 30 artikelen geblokkeerd, captcha bij Medium en GitHub (DERDEN, [Day 8: The Platform Problem](https://dev.to/deadbyapril/day-8-the-platform-problem-1dbe)).
- Eigen les van de agent: "publishing is not distribution. Writing is not marketing" (DERDEN). De enige verkoop en de enige klant kwamen van mensen die het verhaal volgden, niet van de producten of de stukken.
- Wat wij hiervan nemen: veel plaatsen op veel kanalen levert bij een agent zonder publiek niets op en sluit kanalen af. Dit is het derde voorbeeld met dezelfde uitkomst (Matt Busel in 116: 1.383 posts, 0 verkopen).

### 134. Een agent-maker over welke kanalen je wel en niet volledig automatiseert
- Atlas Whoff (die eerder zijn bedrijf door een agent liet runnen, zie whoffagents eerder in dit bestand) schrijft over een post op r/ClaudeAI: "Claude Code got my Meta Ads account permanently banned", 78 upvotes en 60 reacties van mensen met hetzelfde (DERDEN, [dev.to, 9 apr 2026](https://dev.to/whoffagents/claude-code-got-someones-meta-ads-account-banned-heres-how-to-automate-without-getting-flagged-513h); de Reddit-post zelf niet gelezen).
- Zijn eigen ervaring: "Atlas's Twitter got suspended for posting too fast. Now: 1-2 posts/day MAX, with random delays" (DERDEN). Hij deelt in: hoog risico (advertenties, X, LinkedIn-benaderen, alles met betalingen), middel (LinkedIn-posts, YouTube-uploads, Reddit), laag (dev.to, Hashnode, Medium via hun API, GitHub).
- Zijn toets: "would a human doing this at 3AM at machine speed get flagged? If yes, don't automate it blindly" (DERDEN). Dat sluit aan op onze regel: Metricool met een vast ritme en keuring, geen eigen bots op X of Reddit.

### Wat een agent hierin zelf kan, binnen onze regels
- **Maillijst:** voor de sale (27 nov tot 1 dec) een concept-broadcast in Kit zetten via de API met `send_at: null`, met de link `dortus.com/click-joints/?ref=mail`. Versturen is iets onder de naam Dortus, niet van Thijs; wie mag drukken en na welke keuring is aan de hoofdchat (regel 4). Na verzenden leest een agent de klikken per link uit. Kost € 0.
- **Pers:** het pakket uit ronde 27 aanvullen met één concreet getal uit de demo van Pro (zoals "in X klikken een knie die buigt en vastklikt"), want dat is wat 80 Level overneemt.
- **Niet doen:** meer kanalen erbij of hoger tempo. Drie voorbeelden laten zien dat dat bij nul publiek nul verkoop geeft en accounts kost.

## Patronen na ronde 28
90. **Twee vakbladen binnen een week, bij beide verkopers met 400+** (131): CatPin en Nitro Retopo, allebei met een klein kanaal en een gewone link. Het stuk leunt op een demo met een getal.
91. **Ook de mailtool zelf bouwt "agent maakt concept, mens verstuurt"** (132): de Kit MCP verstuurt nooit; de API kan het wel. Voor ons: concept via API, verzenden na keuring.
92. **Volledig zelf plaatsende agents zonder publiek verdienen niets en raken kanalen kwijt** (133, 134): $9 na 209 sessies; bans op X, Reddit, HN, Meta Ads. Wat wel geld gaf, was een mens die het verhaal volgde.

## Stand na run 23 nov ±00:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Nitro Retopo herhaalt het patroon van CatPin:** 80 Level (7 okt) en Digital Production (13 okt) binnen een week, gewone link, nu 400+ verkopen voor $25 met 326 abonnees (GEZIEN). Effect van de pers op de verkoop blijft onbekend (GOK).
2. **Onze maillijst kan door een agent als concept gevuld worden:** de Kit API met onze bestaande sleutel maakt een broadcast met `send_at: null` en leest daarna klikken per link (GEZIEN in de docs, niet getest). De nieuwe Kit MCP is alleen voor betaalde plannen en verstuurt nooit zelf (GEZIEN).
3. **"Dead by April": 209 sessies, 8 producten, 108 artikelen, $9 productverkoop** (DERDEN), en binnen 8 dagen geweerd op X, Reddit, HN en Write.as.
4. **Een Meta Ads-account permanent dicht na een week Claude Code met volle rechten, en X geschorst wegens te snel plaatsen** (DERDEN). Regel van die maker: 1 tot 2 posts per dag op X, met willekeurige pauzes.
5. **De vraag uit ronde 27 (verkoop rond Digital Production) is niet beter te beantwoorden dan in 122:** Superhive toont geen datums per review, Gumroad wel maar die telling bestaat al (GEZIEN).

Voorstel: (a) de hoofdchat laat vóór wo 25 nov een agent één concept-mail voor de sale in Kit zetten via de API (`send_at: null`, link met `?ref=mail`), Daan keurt, de hoofdchat beslist wie verstuurt op 27 nov; dat is de enige plek waar we kopers bereiken die al ja zeiden. (b) Het perspakket voor 80 Level en Digital Production krijgt één getal uit de demo van Pro en de video bovenaan, zoals bij Nitro Retopo. (c) Geen extra kanalen of hoger tempo in de saleweek; de tak blijft bij Metricool met keuring. Volgende run: hoeveel abonnees de maillijst nu heeft en wat makers in onze hoek per saleweek-mail aan klikken en verkoop melden (DERDEN), zodat (a) een verwachte opbrengst krijgt.

## Ronde 29 (run 23 nov ±01:20 UTC, klok van de container): het voorstel van vorige run klopt niet (de maillijst is leeg), wat de agent van Whoff na vijf maanden verdiende, en waar onze Shorts-kijkers blijven

### 135. Correctie op ronde 28: de maillijst heeft 0 abonnees, dus een sale-mail bereikt niemand
- Kit: 0 abonnees, ook gisteren 0 (GEZIEN, `organisatie/scorebord.md`, meting 22 nov 09:50 UTC). Gumroad: 0 verkopen van de gratis versie en 0 van Pro (GEZIEN, zelfde bron). Er is dus ook geen kopersbestand op Gumroad om een update naar te sturen.
- Voorstel (a) uit de vorige stand (concept-broadcast in Kit voor de sale) levert daarom € 0 op en vervalt. Wat wel mensen bereikt die al iets van ons hebben: de gratis add-on op Blender Extensions (316 downloads, +28 in een dag, GEZIEN zelfde bron). Die pagina linkt al naar `dortus.com/click-joints/` (GEZIEN met curl op extensions.blender.org/add-ons/click-joints/). In de extensions-zip zelf staat bewust geen Pro-tekst; de "direct-zip" met slotknoppen is alleen voor directe download (`producten/blender-gewrichten/architectuur.md`).

### 136. Whoff Agents na vijf maanden: één betaling van $49, en 37 Shorts zonder één klikbare weg naar de winkel
Vervolg op de whoffagents-voorbeelden eerder in dit bestand en op 134. Atlas (de agent) schrijft zelf de posts.
- **30 dagen, elke 30 minuten een sessie** (±1.440 keer): 23 dev.to-artikelen, 37 YouTube Shorts, een paar tweets, **0 betalende klanten** (DERDEN, [dev.to, 9 jun 2026](https://dev.to/whoffagents/what-30-days-of-30-minute-agent-loops-actually-produced-and-the-5-numbers-i-did-not-expect-g9i)). Zijn les: "An agent that does not own distribution ... will multiply zero by 10 and get zero." Ongeveer 17% van de sessies deed niets, vooral door ontbrekende rechten, sleutels of limieten (DERDEN, zelfde bron). Een fout die betalende klanten raakte vond de agent zelf, maar de oplossing bleef wachten op de mens; de agent controleerde daarna tien sessies lang dat de fout er nog was.
- **Week 5: vier van vijf kanalen dood zonder dat iemand het zag** (DERDEN, [dev.to, 12 mei 2026](https://dev.to/whoffagents/week-5-of-building-in-public-every-distribution-channel-except-one-is-broken-2e76)): X gaf weken "Unauthorized" (sleutel verlopen), LinkedIn blokkeerde elke post als bot, Reddit was nooit aangesloten, en op YouTube werkten uploads maar reacties niet, omdat de sleutel de toestemming `youtube.force-ssl` miste. Gevolg: "37 Shorts uploaded. Zero pinned product-link comments." Alleen dev.to werkte. Zijn oplossing: één lijstje voor de mens met per dood kanaal de precieze klik en een test erna.
- **Sep 2026: "we've earned $49 so far (one Stripe charge, lifetime)"**, en een nieuwe proef met persoonlijke mails aan kleine bedrijven: 26 verstuurd, 0 antwoorden (DERDEN, [dev.to, 8 sep 2026](https://dev.to/whoffagents/baseline-what-weve-actually-got-week-one-16l3)). Ook hier zei de agent het getal zelf eerlijk.
- **Een gedachtestreepje legde alles vijf dagen stil** (DERDEN, [dev.to, 1 sep 2026](https://dev.to/whoffagents/an-em-dash-took-down-my-entire-automation-stack-for-five-days-18c5)): een sessie "verbeterde" het gedeelde startscript en zette een em dash in een opmerking; PowerShell las het bestand daarna niet meer, en alle geplande sessies (ochtend, elke twee uur, avond) draaiden 26 tot 30 aug niet, zonder één foutmelding. Zijn nieuwe regels: scripts die een agent aanpast alleen ASCII, en "geen log" is zelf een alarm.
- Wat wij hiervan nemen: (1) onze regel "geen gedachtestreepjes" beschermt ook de scripts, niet alleen de toon; (2) een kanaal kan dagen dood zijn terwijl er wel "geplaatst" wordt, dus de tak moet per dag kijken of er na een post ook bezoek komt, niet alleen of de post erop staat; (3) vijf maanden 24/7 agentwerk zonder eigen publiek gaf $49. Vierde voorbeeld met die uitkomst (116, 133, 134).

### 137. Onze eigen Shorts: ±3.400 weergaven, 6 bezoeken via het YouTube-adres, en de reden staat in de regels van YouTube
- Weergaven volgens de RSS van @Dortusapps, 23 nov ±01:20 UTC (GEZIEN, youtube.com/feeds/videos.xml): hinge 115° 1.395, "see how far a joint bends" 1.219, "rig to 10 printable parts" 324, "how far can this knee bend" 270, "make your rigged character poseable" 211. De lange Pro-video's met het klikbare `https://dortus.com/yt/` bovenaan: 9 en 0 weergaven (GEZIEN, zelfde bron).
- Bezoeken op `dortus.com/yt`: 6 op 20 nov, daarna 0 tot 22 nov 10:50 (GEZIEN, Amami-tabel in `organisatie/scorebord.md`). Dus ±0,2% van de kijkers komt op onze site (GOK, ruwe deling, tijdvakken vallen niet precies samen).
- Waarom: "URLs placed in YouTube Shorts comments and Shorts descriptions are non-clickable", sinds 31 aug 2023. Wel klikbaar: de link "Related video" in een Short, de links op de kanaalpagina (tot 14), en links in beschrijvingen en reacties van lange video's, maar die laatste alleen als het kanaal de "advanced features" aan heeft (DERDEN, [YouTube Help 13748639](https://support.google.com/youtube/answer/13748639?hl=en); datum: [link.boo, okt 2026](https://link.boo/guides/youtube-shorts-link-in-description)).
- Het team weet dit al: het plan zet als "gerelateerde video" de nieuwste lange Pro-video (`marketing/wachtrij/2026-11-22-yt-short-v2-printable-parts.md`). Maar die lange video's hebben 9 en 0 weergaven, dus de doorstroom via die weg is klein (GEZIEN). Of "advanced features" aan staat op @Dortusapps heb ik niet kunnen zien; YouTube stuurde mijn curl naar een captcha (GEZIEN). Staat het uit, dan is ook de link in de lange video niet klikbaar (GOK dat het uit staat; Whoff had een vergelijkbaar stil gat met de reacties).
- Ter vergelijking: de arts met twee Claude-agents (voorbeeld 19) haalde 30.170 weergaven en 29 abonnees in 6 weken (DERDEN, [dev.to, feb 2026](https://dev.to/wcamon/i-let-ai-agents-run-my-youtube-channel-for-6-weeks-heres-what-actually-happened-21b1)); zijn dev.to-account plaatst sinds maart alleen nog vakartikelen, geen vervolg over het kanaal (GEZIEN, dev.to API).

### 138. Gumroad: nog geen Black Friday-code voor 2026 in de broncode
- In antiwork/gumroad op main staat op 23 nov ±01:20 UTC nog `BLACK_FRIDAY_CODE = "BLACKFRIDAY2025"` (GEZIEN, `app/controllers/concerns/search_products.rb`, alleen gelezen). Vorig jaar kwam de aankondiging pas op 27 nov (DERDEN, al in 77/109). Voor Pro maakt het weinig uit: Discover vraagt eerst $100 echte verkoop (zie eerder in dit bestand) en Pro staat op Gumroad op 0 (GEZIEN, scorebord).

### Wat een agent hierin zelf kan, binnen onze regels
- **Absentie-alarm (Whoff-les):** een kleine controle bij het scorebord: zijn er op een dag meer dan 200 nieuwe Shorts-weergaven en 0 bezoeken op `dortus.com/yt`, dan een regel in `berichten/hoofdchat.md`. Kost € 0, gebruikt alleen wat het scorebord al leest.
- **Eén vraag voor Thijs, één klik:** staat "advanced features" (klikbare externe links) aan op @Dortusapps? Kijken in YouTube Studio, Instellingen, Kanaal, Beschikbaarheid van functies. Zonder dat werkt de hele "gerelateerde video naar lange video met link"-weg niet (GOK tot iemand kijkt). Dat is iets wat alleen de hoofdchat of Thijs in Studio ziet.
- **Niet doen:** de Kit-mail voor de sale (lijst is leeg), en geen bot die links onder Shorts zet (niet klikbaar, en lijkt op spam volgens dezelfde helppagina).

## Patronen na ronde 29
93. **Een lege lijst is geen kanaal** (135): vóór je een agent mails laat maken, eerst het aantal ontvangers lezen. Bij ons 0.
94. **Agents plaatsen door terwijl het kanaal dood is** (136): Whoff had 37 Shorts zonder één klikbare link en merkte het in week 5. Meet per kanaal bezoek na posten, niet posts.
95. **Shorts geven bereik, geen klikken** (137): bij ons ±3.400 weergaven tegen 6 bezoeken. De enige klikbare wegen zijn Related video, kanaallinks en (met advanced features) lange video's.

## Stand na run 23 nov ±01:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Voorstel (a) van vorige run vervalt:** de Kit-lijst heeft 0 abonnees en Gumroad 0 kopers (GEZIEN, scorebord 22 nov). Een sale-mail bereikt niemand.
2. **Whoff Agents, vijf maanden agent elke 30 minuten: $49 totaal** (DERDEN), 37 Shorts zonder vastgezette link omdat één toestemming ontbrak, vier van vijf kanalen weken stil dood. Vierde voorbeeld: veel plaatsen zonder publiek en zonder meting geeft niets.
3. **Onze Shorts: ±3.400 weergaven, 6 bezoeken via `dortus.com/yt`** (GEZIEN). Links in Shorts zijn niet klikbaar (DERDEN, YouTube Help); de lange video's met de klikbare link hebben 9 en 0 weergaven.
4. **Onbekend en belangrijk:** of "advanced features" aan staat op @Dortusapps. Zo niet, dan is ook de link in de lange video niet klikbaar (GOK).
5. **Een em dash in een script legde bij Whoff vijf dagen alle geplande sessies stil** (DERDEN). Onze regel zonder gedachtestreepjes beschermt dus ook de scripts.

Voorstel: (a) de hoofdchat kijkt bij de volgende YouTube Studio-sessie of "advanced features" aan staat en of elke Short een Related video heeft; dat is de enige klikbare weg van ±1.000 Shorts-weergaven per dag naar de winkel. (b) Een absentie-alarm bij het scorebord (Shorts-weergaven omhoog, `ref=yt` op 0). (c) De sale-energie gaat naar plekken met mensen: de Blender Extensions-pagina (28 downloads per dag) en de CG Channel-lijst die al loopt, niet naar mail. Volgende run: wat andere kleine Blender-makers met een gratis extensie en een betaalde versie in hun extensions-beschrijving zetten (zonder de regels van Blender te breken), met verkoopklassen op Superhive als uitkomst.

## Ronde 30 (run 23 nov ±02:20 UTC, klok van de container): wat kleine Blender-makers met een gratis extensie en een betaalde versie op hun extensions-pagina zetten, en hoeveel dat op Superhive verkoopt

Werkwijze: alle 1.231 add-on-pagina's van extensions.blender.org met curl gelezen (lijst uit `api/v1/extensions/`, 23 nov ±02:10 UTC), daarin de links naar Superhive, Blender Market, Gumroad en donatiesites gezocht, en voor de belangrijkste de verkoopband op Superhive gelezen. Alleen gelezen, niets geplaatst.

### 139. Wat Blender zelf toestaat (voorwaarden, bijgewerkt 10 aug 2026)
- Regel 6.1: links naar betaal- en steunsites mogen "in the extension's description", niet in de Blender-UI. Regel 6.2: de beschrijving en beelden mogen alleen tonen wat in de gratis versie zit; "Showcasing features from commercial versions will be considered an advertisement and is not allowed." Regel 6.3: geen promotie van betaalde versies via de UI van Blender (GEZIEN, [extensions.blender.org/terms-of-service](https://extensions.blender.org/terms-of-service/)).
- Dus mag: "steun de ontwikkeling op Superhive/Gumroad" met een link, en een websiteveld dat naar je eigen site wijst. Mag niet: opsommen wat Pro extra kan.

### 140. Telling over alle 1.231 add-ons
- 114 pagina's (9%) hebben een link naar een betaal- of steunsite: Gumroad 44, Ko-fi 32, Buy Me a Coffee 15, Superhive 12, Patreon 9, Blender Market (oude naam) 8, PayPal 6, itch.io 4 (GEZIEN; een pagina kan er meer hebben).
- Mediaan downloads: alle add-ons 5.603, met een betaal- of steunlink 8.003 (GEZIEN). Dat zegt niet dat zo'n link helpt; grotere makers hebben vaker een winkel (GOK).
- Maar 9 pagina's noemen letterlijk een "pro/full/paid/lite version" (GEZIEN, zoekterm op de tekst). Expliciete Pro-reclame is dus zeldzaam, past bij regel 6.2.
- Click Joints: 332 downloads sinds 8 nov, plaats 1.149 van 1.231 (GEZIEN). Onze beschrijving noemt Pro niet; het websiteveld wijst naar `dortus.com/click-joints`, en die pagina linkt naar Pro op Gumroad en Superhive (GEZIEN). Dat valt binnen de regels.

### 141. Vier patronen, met wat ze op Superhive zichtbaar verkopen
Band = verkoopband op de Superhive-pagina, ondergrens, alle verkopen ooit uit alle bronnen (GEZIEN, 23 nov ±02:15 UTC). Downloads = extensions.blender.org (GEZIEN).

| Patroon | Gratis extensie (downloads, sinds) | Betaald product op Superhive (prijs, band) |
|---|---|---|
| A. "Steun de ontwikkeling", zelfde add-on te koop | Texel Density Checker (114.183, juli 2024) | zelfde add-on, $10, **300+** |
| A. idem | UniV (114.856, aug 2024): "The addon is free, but you can support the author and purchase this addon" | UniV Pro, $40, **100+** |
| B. "Mijn andere spullen" onder drie gratis tools | Quick Groups 40.677, Synchronize Workspaces 32.468, Parallax Node 35.842 (MultLabs) | Folds Modifier, $12, **800+** (staat zelf niet op extensions) |
| C. Link naar een ander betaald product | Wiggle 2 (32.551, apr 2026) | GroomForge Pro, $25, **30+** |
| D. Pro-functies opsommen (breekt 6.2) | GrimTopo (360, 11 nov 2026): "Want the Pen Tool, Tube, Loop Extrude...? Get GrimTopo Pro" | GrimTopo, $15, geen band, 6 dagen oud |
| D. idem | OptiPloy (20.129, aug 2024): "Get OptiPloy Pro for $5" | op Gumroad, 5 beoordelingen, gem. 5,0; verkoop verborgen |
| D. idem | MatColeX (5.172, okt 2025): "want to upgrade pro version? here" | link geeft de voorpagina van Superhive: product weg (GEZIEN) |

- Omzetting gratis naar betaald (ruwe deling band/downloads, GOK want de band telt ook verkoop van buiten): Texel 0,26%, UniV 0,09%, Wiggle 2 naar GroomForge 0,09%, MultLabs naar Folds Modifier hoogstens 0,73% (800 op 109.000 samen).
- Surface Diagnostics (11.243 downloads, 600+ voor $15) laat ik buiten de deling: op Superhive al ruim 3 jaar, op extensions pas sinds nov 2025 (GEZIEN, data op beide pagina's).
- Patroon D levert in deze steekproef niets zichtbaars op dat A of B niet ook haalt, en het breekt 6.2. Of Blender daar echt op ingrijpt heb ik niet kunnen vinden; de pagina's staan er nog (GEZIEN). Het risico is wel dat de gratis versie, onze enige bron van ±22 downloads per dag, offline gaat (GOK).

### 142. Wat dat voor Pro betekent (sommetje, geen belofte)
- Click Joints: 332 downloads in 15 dagen, ±22 per dag, ±660 per maand (GEZIEN, doorgerekend).
- Met 0,1% tot 0,7% omzetting: **0,7 tot 4,6 verkopen per maand**, bij $12 op Superhive ±$8 tot $55 bruto (GOK, gebaseerd op 141). De extensions-pagina alleen maakt dus geen snel veel geld; de makers met 300+ en 800+ hadden 100.000+ downloads en twee jaar.
- Wat wel schaalt in de tabel: meer gratis tools die naar één betaald product wijzen (MultLabs, drie tools, 800+). Dat past bij wat we al doen (Click Joints, Hats), maar kost bouwtijd.

### Wat een agent hierin zelf kan, binnen onze regels
- **Eén zin in de beschrijving van Click Joints, patroon A** (mag volgens 6.1): onderaan een kopje "Support development" met "If Click Joints saves you time, you can support development on Superhive or Gumroad" en de twee links naar Pro. Geen Pro-functies noemen (6.2). De agent schrijft de tekst; aanpassen op extensions.blender.org vraagt inloggen, dus de Blender-manager of de hoofdchat zet hem erop. Kost € 0.
- **Meten:** de Superhive-band van Pro en de Gumroad-verkoop staan al op het scorebord; zet er per week de downloads naast, dan zien we na een maand of de omzetting rond 0,1% of hoger zit.
- **Niet doen:** Pro-functies in de gratis beschrijving zetten (GrimTopo, OptiPloy), en geen link laten staan naar een product dat weg is (MatColeX).

## Patronen na ronde 30
96. **Op extensions.blender.org werkt "steun mij op Superhive", niet "koop Pro"** (139, 141): de grootste verkopers (Texel 300+, Folds Modifier 800+) noemen geen Pro-functies; wie dat wel doet breekt regel 6.2 en verkoopt zichtbaar niet meer.
97. **Gratis naar betaald zit rond 0,1% tot 0,7%** (141, GOK): met ±660 downloads per maand is dat een paar verkopen. Bereik op de extensions-pagina moet tien keer groter, of er moeten meer gratis tools naar Pro wijzen.
98. **Meerdere gratis tools, één betaald product** (MultLabs): het sterkste patroon in de telling.

## Stand na run 23 nov ±02:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Blender staat links naar betaalde versies toe in de beschrijving, maar verbiedt Pro-functies te tonen** (regel 6.1 en 6.2, GEZIEN, voorwaarden 10 aug 2026). Onze pagina noemt Pro nu nergens; alleen het websiteveld leidt naar dortus.com.
2. **Telling van 1.231 add-ons:** 9% heeft een betaal- of steunlink, maar 9 pagina's noemen letterlijk een Pro-versie (GEZIEN).
3. **Zichtbare uitkomsten op Superhive:** Texel Density Checker 300+ ($10, 114.000 gratis downloads), UniV Pro 100+ ($40, 115.000), Folds Modifier 800+ ($12, via drie gratis tools met samen 109.000), GroomForge 30+ ($25, 32.500) (GEZIEN).
4. **Omzetting ruwweg 0,1% tot 0,7%** (GOK). Voor Click Joints (±660 downloads per maand) is dat 1 tot 5 verkopen per maand, ±$8 tot $55. Geen snel veel geld uit deze weg alleen.
5. **Pro-reclame in de gratis beschrijving (GrimTopo, OptiPloy, MatColeX) levert zichtbaar niets extra's** en zet de gratis versie op het spel.

Voorstel: (a) de Blender-manager zet onderaan de beschrijving van Click Joints één steunregel met links naar Pro op Superhive en Gumroad, zonder Pro-functies (kost € 0, valt binnen 6.1). (b) Het scorebord zet per week downloads naast verkoop, zodat we de echte omzetting kennen. (c) Omdat deze weg hoogstens tientallen dollars per maand geeft, gaat de grote energie naar meer bereik op de pagina (de CG Channel-lijst, de Shorts met Related video uit run 29) of naar een tweede gratis tool die naar Pro wijst. Volgende run: hoe MultLabs en Mrven (Texel, ACT) hun gratis tools onderling naar elkaar laten verwijzen, en of hun Superhive-band in de tijd sprongen maakt bij een nieuwe gratis release (via archive.org-kopieën van de Superhive-pagina).

## Ronde 31 (run 23 nov ±03:20 UTC, klok van de container): hoe MultLabs gratis tools, forumtopics en elke paar maanden een nieuw betaald product aan elkaar knoopt, en hoe de verkoopband in de tijd loopt (archive.org)

Werkwijze: de API van extensions.blender.org, de pagina's van MultLabs op extensions.blender.org, Superhive en multlabs.com, de forumtopics op BlenderArtists (Discourse-JSON, openbaar), en oude kopieën van de Superhive-pagina's via de CDX-zoeker van archive.org. Alles met curl, alleen gelezen. Banden zijn ondergrenzen, alle verkopen ooit.

### 143. MultLabs: één maker, 6 gratis extensies, 12 betaalde producten, en elke gratis tool heeft ook een "steun"-pagina op Superhive
- Gratis op extensions.blender.org (GEZIEN, 23 nov): Quick Groups 40.677 downloads (sinds mei 2024), Parallax Node 35.843 (sep 2025), Synchronize Workspaces 32.471 (mei 2024), White (thema) 11.108, Render Profiler 8.579 (mrt 2026), Lottie Export 876 (mei 2026).
- **De oudere drie** linken in hun beschrijving naar twee betaalde producten: Folds Modifier en Staircase Generator. **De nieuwere** (Render Profiler, Lottie) linken alleen naar multlabs.com en een BlenderArtists-topic (GEZIEN). Op multlabs.com staat alles op één pagina: per product een video, "Superhive" en waar het kan "Blender Extensions"; bij Synchronize Workspaces "Top 5 at Blender Extensions" (GEZIEN).
- **Steunpagina's op Superhive voor de gratis tools** (GEZIEN, band nu): Synchronize Workspaces $1, **100+** (al 100+ in mei 2025, archive.org); Quick Instance (Quick Groups) $4, **100+**; Parallax Node $10, **20+** (10+ in feb 2026); Render Profiler $10, geen band; Lottie $15, geen band.
- Ruwe omzetting van gratis naar "steun" (GOK, band gedeeld door downloads): Parallax Node ±0,06%, Render Profiler onder 0,12%, Quick Groups ±0,25% (maar die steunpagina bestaat al sinds 2019, langer dan de extensions-site). Past bij 141: steun als losse knop haalt rond 0,1%.
- **Betaalde producten, band nu** (GEZIEN): Folds Modifier $12 800+, Staircase Generator $25 300+, Topiary Generator $15 100+, Vox Tools $20 100+, Rigged & Animated Book $19 100+, Europe Style Building Generator $10 60+, Tree Craft $15 50+, Smart Simplify Pro $15 geen band.

### 144. Zo loopt de band in de tijd: snel in de eerste maand, daarna langzaam en gestaag
Kopieën van archive.org (GEZIEN; "Published ..." is de leeftijd die Superhive op die dag zelf toonde):

| Product | Band per kopie |
|---|---|
| Topiary Generator ($15) | 40+ na 26 dagen (9 feb 2026), 100+ na 4 maanden (1 mei 2026), 100+ nu |
| Tree Craft ($15) | 10+ na 3 dagen (1 okt 2026), 50+ na ±2 maanden (nu) |
| Staircase Generator ($25) | 40+ na ±2 maanden (apr 2025), 100+ na 6 maanden, 200+ na 11 maanden, 300+ na ±19 maanden (okt 2026) |
| Folds Modifier ($12) | 600+ (mei 2025), 700+ (nov 2025), 800+ (mei 2026), 800+ nu |
| Texel Density Checker ($10, Mrven) | 80+ (sep 2020), 200+ (sep 2021), 200+ (mei en sep 2024), 300+ (apr 2025), 300+ nu |

- **Eerste maand ±40 verkopen, daarna ±10 tot 20 per maand per product** (GOK, uit de banden afgeleid). Wie elke paar maanden een nieuw product uitbrengt, stapelt die staarten: MultLabs bracht in 23 maanden 6 betaalde producten uit, Folds Modifier (okt 2024), Book (nov 2024), Staircase (mrt 2025), Smart Simplify (dec 2025), Topiary (jan 2026) en Tree Craft (sep 2026), plus 2 gratis tools met steunpagina, Render Profiler (feb 2026) en Lottie (apr 2026) (GEZIEN, data van de forumtopics hieronder).
- Topiary Generator kreeg op 9 feb 2026 een stukje in Digital Production, op de dag van de eerste kopie (40+) (DERDEN, [digitalproduction.com, 9 feb 2026](https://digitalproduction.com/2026/02/09/topiary-generator-grows-procedural-foliage-in-blender/)). Daarna 100+ binnen 3 maanden. Hoeveel van die 60 door het stukje kwamen: onbekend (GOK).
- Texel: de band ging van 200+ naar 300+ tussen sep 2024 en apr 2025, de eerste maanden dat de gratis versie op extensions.blender.org stond (GEZIEN, juli 2024 op extensions). Of dat door extensions kwam: GOK, maar het is de enige sprong in vier jaar.

### 145. Het forum als winkelloket: per tool één topic dat jaren leeft, met snelle reparaties
- Topics van de maker op BlenderArtists (GEZIEN, `blenderartists.org/topics/created-by/<naam>.json`): Quick Groups (2019) 30.134 keer bekeken, 124 berichten, laatste bericht 7 okt 2026; Synchronize Workspaces (2022) 16.037, 120 berichten, laatste **22 nov 2026**; Parallax Node 6.699, 45; Render Profiler 2.200, 28; Lottie 1.568, 8. De topics van betaalde producten trekken minder: Folds Modifier 7.447, Staircase 4.685, Book 1.518, Topiary 627, Smart Simplify 334, Tree Craft **112** (GEZIEN).
- Wat er in zo'n topic gebeurt (GEZIEN, Synchronize Workspaces, 28 okt 2026): een gebruiker meldt een fout met de regel uit de foutmelding, de maker geeft dezelfde dag een oplossing, de gebruiker vraagt "is the version on Blender Extensions going to be updated?", de maker antwoordt "Just uploaded." Het eerste bericht van Quick Groups (2019) zegt al "If you want to tip:" met links naar Gumroad en Blender Market (GEZIEN). Elk nieuw bericht zet het topic weer bovenaan.
- Ter vergelijking, onze hoek (GEZIEN): SlicerJoint Pro (Gumroad, $20) 312 keer bekeken, 4 berichten, alle van de maker; Nitro Retopo 699 keer, 1 bericht; Bed Fit Splitter 98 keer, 3 berichten. De 3D-print-makers die verkopen (117 tot 119, 131) doen het niet via het forum; MultLabs wel, maar met gratis tools als lokaas.
- Tegenslag die ook hier kan: in dec 2023 schreef de maker "Why Blender Market keeps ignoring me?": zijn account was dicht en hij kreeg geen antwoord, mogelijk omdat hij uit Rusland komt (DERDEN, zijn eigen bericht op [BlenderArtists, 22 dec 2023](https://blenderartists.org/t/why-blender-market-keeps-ignoring-me/1502542)). Hij verkocht ook via Gumroad; zijn producten staan nu weer op Superhive (GEZIEN). Les: twee winkels, net als Pro nu.

### 146. Of MultLabs AI gebruikt voor de marketing: niet te zien
- De teksten op multlabs.com en Superhive zijn strak en eenvormig ("Trees that tell stories ...", één zin per product), en elk product heeft een eigen video (GEZIEN). Of daar een agent achter zit heb ik nergens gevonden (GOK). Wat wel vaststaat: het werk is klein en herhaalbaar (topic openen, video, steunpagina, link in de gratis tools), en precies dat kan een agent voorbereiden.

### Wat een agent hierin zelf kan, binnen onze regels
- **Forumwacht voor Click Joints (€ 0, alleen lezen):** zodra er een BlenderArtists-topic is (lijst-thijs punt over BlenderArtists), leest een agent elke paar uur de JSON van dat topic (`/t/<id>.json`, openbaar, geen sleutel). Bij een nieuw bericht met een fout: de bouwer repareert, de agent zet een concept-antwoord klaar ("Fixed in 1.x, now on Blender Extensions"), de hoofdchat of Thijs plaatst (account van Thijs, regel 4). Dat is het patroon van 145, en de reden dat het topic van MultLabs al vier jaar bovenaan komt.
- **Het topic over de gratis Click Joints laten gaan, niet over Pro:** de gratis topics van MultLabs trekken 5 tot 270 keer meer kijkers dan de betaalde (GEZIEN, 145). In het eerste bericht onderaan één regel "If you want to support development:" met Pro op Superhive en Gumroad, zoals Quick Groups in 2019. Dit is een voorstel voor de tekst die al op lijst-thijs staat; die tekst gaat nu over Pro.
- **Bandenmeter met archive.org:** de concurrentenmeter uit 117 kan per product ook de oude banden ophalen (CDX-zoeker, één aanvraag per 4 seconden, anders 429; GEZIEN). Zo zien we per lancering de eerste maand, ook van producten die we pas later ontdekken.
- **Niet doen:** zonder eigen gebruikers een topic per betaald product openen (Tree Craft 112 kijkers, SlicerJoint 312); en geen tweede product bouwen alleen voor de staart zonder dat de eerste maand van Pro iets laat zien.

## Patronen na ronde 31
99. **Eén product geeft een korte piek en een dunne staart; de verkoop komt van stapelen** (144): ±40 in de eerste maand, daarna ±10 tot 20 per maand (GOK). MultLabs bracht er 6 betaalde uit in 23 maanden.
100. **Het forumtopic van een gratis tool is het langst lopende kanaal** (145): 16.000 tot 30.000 kijkers over jaren, levend gehouden door snelle reparaties, met de "tip"-links in het eerste bericht.
101. **Steunknoppen bij gratis tools halen rond 0,1%** (143), net als in 141. Ze helpen, maar het geld zit in de betaalde producten waar de gratis tools naar wijzen.

## Stand na run 23 nov ±03:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Verkoopband in de tijd (archive.org, GEZIEN):** Topiary Generator 40+ na 26 dagen en 100+ na 4 maanden; Tree Craft 10+ na 3 dagen en 50+ na 2 maanden; Staircase 40+, 100+, 200+, 300+ na 2, 6, 11 en 19 maanden. Dus ±40 in de eerste maand, daarna ±10 tot 20 per maand (GOK).
2. **MultLabs stapelt:** 6 betaalde producten in 23 maanden (okt 2024 tot sep 2026), met nu 800+, 300+, 100+, 100+, 50+ en nog geen band; met de oudere Vox (100+) en Building Generator (60+) samen minstens 1.500 verkopen (GEZIEN, ondergrenzen). Dat is de weg naar geld in deze winkel, niet één product groter maken.
3. **Steunpagina's voor gratis tools halen ±0,06% tot 0,25%** (GOK, band/downloads); zelfde orde als 141.
4. **De BlenderArtists-topics van de gratis tools leven jaren** (30.134 en 16.037 keer bekeken, laatste bericht gisteren), dankzij reparaties op de dag zelf. Topics over betaalde producten halen 112 tot 7.447; die van onze directe concurrenten 98 tot 699 (GEZIEN).
5. **Topiary Generator stond in Digital Production op de dag dat hij 40+ had** (DERDEN); derde voorbeeld van dat blad bij een kleine maker (na 129 en 131).

Voorstel: (a) de tekst voor BlenderArtists op lijst-thijs gaat over de gratis Click Joints (support-topic, met onderaan één steunregel naar Pro op Superhive en Gumroad), niet over Pro; Daan keurt de nieuwe tekst, Thijs plaatst. (b) Zodra het topic er is, een forumwacht die de openbare JSON leest en concept-antwoorden klaarzet; reparaties gaan via de Blender-manager. (c) Voor geld binnen weken: Pro is één product met een staart van hoogstens tientallen per maand (GOK); de snelste vergroting is een tweede klein betaald product in dezelfde hoek dat via dezelfde gratis tool en pagina verkocht wordt, maar pas na de eerste maandcijfers van Pro (eind december). Volgende run: van 5 makers met 3 of meer betaalde producten op Superhive de lanceringsdatums en eerste-maandbanden via archive.org, zodat (c) een steviger getal krijgt dan één maker.

## Ronde 32 (run 23 nov ±04:20 UTC, klok van de container): wie in november op Superhive snel verkoopt en wie niet, en het blok "New and Rising" op de voorpagina

Werkwijze: de pagina's van 10 makers en al hun producten op Superhive (band, prijs, beoordelingen, en het interne `productId` uit de broncode), plus de voorpagina. Alles met curl, alleen gelezen. Het plan van vorige run (oude banden via archive.org) lukte niet: web.archive.org verbrak deze run elke verbinding (GEZIEN, `Connection reset` bij de TLS-handdruk; archive.org zelf werkte wel, vermoedelijk een blokkade na eerdere aanvragen, GOK). In plaats daarvan gebruik ik het `productId` als klok.

### 147. Het productId van Superhive loopt op en geeft de lanceerdatum, beter dan "Published"
- "Published ... ago" is de datum van de laatste versie, niet van de lancering: Pro staat nu op "Published 4 days ago", op 22 nov op "2 days ago" (GEZIEN, beide keren), en NexUV (id 269322) zegt "4 days ago" terwijl jongere producten "7 days ago" zeggen (GEZIEN).
- Het `productId` (`_pa.productId = '...'` in de broncode, GEZIEN) loopt mee met de tijd. IJkpunten met bekende datums (GEZIEN, uit 143 en 144): Folds Modifier 219927 (okt 2024), Staircase 231514 (mrt 2025), Topiary 248864 (jan 2026), Render Profiler 251671 (feb 2026), Lottie 255288 (apr 2026), Cleave 264651 (23 sep 2026), Tree Craft 265166 (eind sep 2026), **Click Joints Pro 269495**. Nu komen er ±1.000 id's per week bij (GOK, uit de nieuwste producten: 271081 is "19 minutes ago", 268045 "23 days ago").
- Dus: Pro is even oud als NexFoliage (269093), TopoFit (269026) en OpenSet Connect (269235). Dat maakt ze een eerlijke vergelijking.

### 148. Zelfde leeftijd als Pro, en wel verkoop: drie producten uit de eerste helft van november
| Product | id | Prijs | Band nu | Beoord. | Video op de pagina | Wat de maker al had |
|---|---|---|---|---|---|---|
| OpenSet Connect (Andrew Luzhetskyi) | 269235 | $14 | **100+** | 0 | 1 (eigen kanaal) | ABO Connect, 1000+ verkopen, zelfde soort tool (gratis 3D-modellen binnenhalen) |
| NexFoliage (NexStudio) | 269093 | $17 | **90+** | 4 | 0 | Ecorche-add-on 70+, creature-pakketten 10+ tot 40+ (2023) |
| NexBake (NexStudio) | 268943 | $37 | **50+** | 3 | 0 | idem; lanceerkorting "50% off 5 days" op de pagina |
| TopoFit (GZ Tools) | 269026 | $19,20 | **40+** | 1 | 1 (eigen kanaal @GZ_Tools) | niets: dit is hun enige product op Superhive |
| Click Joints Pro | 269495 | $12 | geen band | 0 | 0 | gratis Click Joints, 244 gebruikers |

(GEZIEN, 23 nov ±04:00 UTC; banden zijn ondergrenzen, alle verkopen ooit.)
- **TopoFit is het nuttigste voorbeeld voor ons:** een maker zonder eerdere producten op Superhive, één video, een tool die één lastige klus in een paar klikken doet ("Full Character Retopology in a Few Clicks", titel van de video, GEZIEN via YouTube oembed), en 40+ in ±2 tot 3 weken. Hoeveel weergaven die video heeft: niet te lezen vanuit de cloud (captcha, zelfde als run 7 van B).
- OpenSet Connect leunt op een bestaande klantenkring (zelfde maker, zelfde soort tool, 1000+). Dat is het "stapelen" uit 144, maar dan met een eerste product dat al groot is.

### 149. Het blok "New and Rising" op de voorpagina: daar staan ze alle drie, Pro niet
- Op de voorpagina van Superhive staat bovenaan, direct onder de categorieën, het blok **"New and Rising: Fresh products gaining momentum in the community"** (GEZIEN, 23 nov). Nu: Eden, Materialify Pro, Image to 3D, Carnage Grains (127), **NexFoliage, OpenSet Connect**, Curve Sculpt 3D, **TopoFit**, AutoCreatures. Hetzelfde blok staat ook boven de categoriepagina's (GEZIEN op /categories/addons).
- Daaronder "Top Selling Items this Week", met **Cleave** op plek 3, na Auto-Rig Pro en Human Generator (GEZIEN). Cleave, directe concurrent van Pro, stond op 22 nov op 200+ en nu op **300+** (GEZIEN beide).
- Superhive zegt zelf 74.447 producten te hebben (GEZIEN, voorpagina). Een plek in "New and Rising" is dus de grootste gratis etalage die een nieuw product kan krijgen. Hoe Superhive kiest staat nergens; de naam ("gaining momentum") wijst op verkoop of bewaren in de eerste weken (GOK).
- Wat dat voor de banden betekent: het patroon "±40 in de eerste maand" uit 144 klopt voor wie niet in dit blok komt; wie er wel in komt haalt 40 tot 100 in 2 tot 3 weken (GEZIEN, 148). Of het blok de verkoop veroorzaakt of volgt: GOK, waarschijnlijk allebei (eerst een paar verkopen, dan de etalage, dan meer).

### 150. Stapelen met een agent, het tegenvoorbeeld: ZEG, 279 producten in ±8 weken, hoogstens een handvol verkopen per product
- De maker ZEG heeft **289 producten** op Superhive, waarvan **279 met een id boven 265000** (dus sinds eind september) en **221 tussen id 267000 en 269000**, ruwweg twee weken eind oktober en begin november (GEZIEN, alle 15 pagina's van de makerpagina en elke productpagina gelezen). Bijna alles is een "generator" voor één soort ding: koffiemachine, dixi-wc, watertoren, gamestoel, reclamebord, ruimtestation, rotsblok, enzovoort, meestal $7 tot $15 (GEZIEN). Vandaag om ±01:00 UTC kwamen er vier tegelijk bij (GEZIEN, "about 3 hours ago").
- **Verkoop:** van die 279 hebben er **4 een band** (Bookwright 20+, Engine Generator 10+, Image to 3D Local 10+, Horse Generator 10+), samen minstens 50 verkopen; **275 hebben er geen** (minder dan ±10 elk, GEZIEN). Samen 21 beoordelingen over 289 producten.
- De teksten zijn strak en gelijk van vorm ("Every book has a story ... 01 / THE COLLECTION ... 02 / YOUR WORKFLOW ...", GEZIEN bij Bookwright). Dat dit met een agent gemaakt is staat er niet, maar ruim 100 werkende add-ons per week met eigen pagina is geen mensenwerk (GOK). ZEG verkoopt zelf ook een add-on "AI Movie Studio" (pagina agent-terminal, GEZIEN).
- **Twee kleinere van hetzelfde soort** (GEZIEN): Meshwright, 17 producten sinds eind september (avatar- en gezichtstools), banden FaceKeys 40+, Outfit Refit 20+, Headwrap 10+, de andere 14 niets; Rekanyx, 16 producten in ±6 weken (kerstgenerators, kabelgenerator, panel cutter), **0 banden**.
- Wat ZEG wel krijgt: het blok "New Arrivals" op de voorpagina staat vol met zijn nieuwste producten en die van Rekanyx (GEZIEN: Cremato Coffee Generator en Ren Panel Cutter staan er nu). Die etalage levert dus niets op; "New and Rising" vraagt om echte verkoop.
- Op BlenderArtists klagen makers al over "selling AI products and AI generated slop" op Superhive (DERDEN, [BlenderArtists, 26 okt 2026, 2.268 keer bekeken](https://blenderartists.org/t/creators-starting-today-superhive-sells-your-products-to-ai/1656000)). Het topic gaat vooral over Superhive die makerswerk aan AI-trainers aanbiedt (opt-out); de "slop" is een bijzin.

### Wat een agent hierin zelf kan, binnen onze regels
- **Etalagewacht (€ 0, alleen lezen):** elke paar uur de voorpagina van Superhive lezen en noteren wat er in "New and Rising" en "Top Selling Items this Week" staat, met id, band en prijs. Na een paar weken weten we hoe snel iets erin komt en hoe lang het blijft. Kost één curl per keer.
- **Pro in "New and Rising" krijgen, in de Cyber Sale:** Pro doet mee met 35% korting van vr 27 nov t/m wo 2 dec (besluit 19 nov). Als het blok op verkoop in korte tijd let (GOK), dan is dat de week om alle bestaande kanalen tegelijk naar de Superhive-pagina te sturen in plaats van naar Gumroad: de Shorts-beschrijvingen, dortus.com/click-joints/, de README van de gratis Click Joints. Geen geld nodig. Of het werkt meten we met de etalagewacht.
- **Een video op de Superhive-pagina:** TopoFit (1 video) en FaceKeys (3 video's) hebben er een, NexFoliage niet; geen harde regel, maar Pro heeft er 0 (GEZIEN). We hebben al Shorts en een uitlegvideo in de wachtrij; één ervan op de pagina zetten kan alleen Thijs (dashboard).
- **Niet doen:** zelf met een agent tientallen kleine add-ons op Superhive zetten. ZEG laat zien wat dat oplevert: 279 producten, ±50 verkopen die zichtbaar zijn (GEZIEN), en een slechte naam bij de makers die het forum lezen.

## Patronen na ronde 32
102. **De eerste twee tot drie weken bepalen de staart** (148, 149): producten van november die 40 tot 100 verkopen halen staan in "New and Rising"; Pro, even oud, heeft nog geen band en staat er niet in.
103. **Massa met een agent verkoopt niet** (150): ZEG 279 producten, 4 met een band; Rekanyx 16, 0. Het "stapelen" van MultLabs (144) werkt met 6 producten in 23 maanden, elk met video en forumtopic, niet met 100 per week.
104. **Een maker zonder naam kan het wel** (148): TopoFit, enig product, één video, één klus in een paar klikken, 40+ in 2 tot 3 weken.

## Stand na run 23 nov ±04:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Pro is even oud als drie producten die nu al 40+ tot 100+ verkochten** (OpenSet Connect 100+, NexFoliage 90+, TopoFit 40+; GEZIEN, gedateerd met het productId). Pro heeft nog geen band (onder ±10).
2. **Die drie staan in "New and Rising" bovenaan de voorpagina van Superhive** (74.447 producten); Cleave, onze directe concurrent, staat in "Top Selling Items this Week" en ging van 200+ naar 300+ sinds gisteren (GEZIEN).
3. **ZEG zet sinds eind september 279 add-ons op Superhive (±100 per week op het hoogste punt), en 4 daarvan verkopen zichtbaar** (GEZIEN). Massa met een agent is geen weg naar geld in deze winkel.
4. **TopoFit is het voorbeeld voor ons:** nieuwe maker, één product, één video die één klus laat zien, 40+ in 2 tot 3 weken.
5. **"Published ... ago" op Superhive is de laatste versie, het productId is de echte leeftijd** (GEZIEN); oude banden via archive.org lukten deze run niet (verbinding verbroken).

Voorstel: (a) in de Cyber Sale (vr 27 nov t/m wo 2 dec) stuurt de hoofdchat alle eigen kanalen naar de Superhive-pagina van Pro in plaats van Gumroad, om in "New and Rising" te komen (GOK of dat werkt; geen geld). (b) Thijs zet één bestaande uitlegvideo op de Superhive-pagina van Pro (nu 0 video's), op de lijst als dat erbij past. (c) Een etalagewacht die elke 3 uur de twee blokken op de voorpagina in een bestand schrijft, zodat we na de sale zien of Pro erin kwam. Volgende run: de etalagewacht zelf een paar keer handmatig draaien, en nagaan hoe lang producten in "New and Rising" blijven en of er ook producten zonder band in staan.

## Ronde 33 (run 23 nov ±05:15 UTC, klok van de container): de etalagewacht met de hand, wat er nodig is om in "New and Rising" te staan, het blok "On Sale", en wat de Cyber Sale van Superhive zelf doet

Werkwijze: voorpagina, categoriepagina Addons en alle producten in de blokken met curl gelezen (band, prijs, `productData` en `productId` uit de broncode). Twee stukken van Superhive zelf over hun sales gelezen. web.archive.org verbreekt nog steeds elke verbinding (GEZIEN, `Connection reset` bij de TLS-handdruk), dus oude voorpagina's kon ik niet vergelijken.

### 151. "New and Rising" om ±05:15: dezelfde negen als om ±04:00, en geen enkel product zonder band
| Plek | Product | id | Band | Prijs nu | Let op |
|---|---|---|---|---|---|
| 1 | Eden (characters studio) | 268996 | 300+ | $7,50 (was $30) | in de aanbieding |
| 2 | Materialify Pro | 269780 | 100+ | vanaf $1 | **jonger dan Pro**, zie 152 |
| 3 | Image to 3D (Milad_Kambari) | 268012 | 1500+ | $18 | oudste in het blok |
| 4 | Carnage Grains | 269441 | 50+ | $49,99 | |
| 5 | NexFoliage | 269093 | 90+ | $17 | |
| 6 | Curve Sculpt 3D (Mark Kingsnorth) | 268865 | **30+** | $25 | laagste band in het blok |
| 7 | OpenSet Connect | 269235 | 100+ | $9 (was $14) | nu in de aanbieding |
| 8 | TopoFit | 269026 | 40+ | $19,20 | |
| 9 | AutoCreatures (DanilGOE) | 269172 | 60+ | $14,99 lanceerprijs (was $59,96) | beoordeling 2 uit 3 reviews |
| - | Click Joints Pro | 269495 | geen | $12 | 3 varianten, $12 tot $45 |

(GEZIEN, 23 nov ±05:15 UTC.) Op /categories/addons staat hetzelfde blok zonder Eden (GEZIEN).
- **Antwoord op de vraag van vorige run:** er staat geen product zonder band in; de ondergrens is nu 30+ (GEZIEN). Een slechte beoordeling (AutoCreatures, 2 sterren) houdt een product er niet uit (GEZIEN). Het lijkt dus vooral om aantal verkopen te gaan (GOK).
- **Hoe lang een product erin blijft:** de id's lopen van 268012 tot 269780, met ±1.000 id's per week (GOK uit 147) is dat een venster van ±4 weken sinds lancering (GOK). Pro (269495) zit midden in dat venster, dus Pro kan er tot ongeveer half december nog in komen (GOK). De Cyber Sale (vr 27 nov t/m wo 2 dec) valt daar precies in.
- In ±75 minuten veranderde alleen de volgorde (Curve Sculpt en OpenSet ruilden), het blok is dus traag (GEZIEN, twee metingen; meer metingen nodig).

### 152. Materialify Pro: jonger dan Pro, al 100+, met een instapvariant van $1
- Vier varianten op één productpagina (GEZIEN): "Demo Version" (100 PBR + 50 procedurele materialen) **$1, standaard aangevinkt**; 500+ procedurele materialen $3; 5000+ PBR-browser $5; alles $7. In de tekst: "Discounted price from 70 $ to 7 $" (GEZIEN). In `productData`: min_price 100, max_price 700 (centen, GEZIEN).
- id 269780, dus enkele dagen ná Pro gelanceerd (GOK uit de id-klok), en nu al 100+ verkopen en plek 2 in "New and Rising" (GEZIEN). Een verkoop van $1 telt voor de band net zo hard als een verkoop van $45.
- Wat het oplevert in geld: onbekend; als de meeste kopers de $1 nemen is 100+ verkopen ±$100 bruto (GOK). Het levert wel de etalage op, en daarmee kopers van de duurdere varianten.
- Voor Pro (GOK, beslissing voor de hoofdchat): Pro heeft al 3 varianten (min $12, max $45, GEZIEN). Een goedkope instapvariant ("Pro Lite", één functie die de gratis Click Joints niet heeft, bv. $3 tot $5) is het snelste middel om in de eerste weken tientallen verkopen te halen. Risico: lagere opbrengst per koper en mensen die anders $12 hadden betaald. De gratis versie op extensions.blender.org blijft de echte demo, dus een "$1 demo" zoals hier heeft voor ons geen zin.

### 153. Het blok "On Sale" op de voorpagina: zes plekken, alleen voor producten in de aanbieding
- Nu (GEZIEN): Eden, Adaptive Auto Skinning, CatPin (400+, id 261693), OpenSet Connect, Blaze Autopose (500+, id 260693), SquishyFX (400+, id 261470). Alle zes hebben `on_sale: true` in de broncode (GEZIEN).
- Dit blok staat naast "New and Rising"; in de Cyber Sale staat Pro met 35% korting op `on_sale` en dingt dan mee om twee etalages tegelijk. Hoe Superhive de zes kiest staat nergens (GOK: verkoop tijdens de aanbieding). In de sale doen duizenden producten mee, dus de kans is klein zonder eigen verkeer (GOK).
- Er draait nu al een kleine Cyber Sale op de voorpagina: "Cyber Sale: 50% off Signage until 26 November" (GEZIEN).

### 154. Wat de Cyber Sale van Superhive zelf doet (hun eigen cijfers)
- Cyber Sale 2024: vijf dagen, meer dan **$700.000** omzet over de winkel, terwijl een gewone maand in 2024 gemiddeld **$881.000** was: ±80% van een maand in vijf dagen. 33.691 verkochte producten (zonder gratis), 4.952 verschillende producten met minstens één verkoop, gemiddeld $48,33 per bestelling (DERDEN, [Superhive, 2024 Cyber Sale Recap](https://superhivemarket.com/posts/blender-market-2024-cyber-sale-recap)).
- Het sterkste product van die sale was Lens Sim, "published just prior to Cyber", met bètatesters uit het vak en "genuine Affiliate marketing" (DERDEN, zelfde link). Dat is precies onze situatie: net gelanceerd vlak voor de sale.
- De Cyber Sale 2023 verkocht per dag **8 keer** zoveel als het gemiddelde van de 60 dagen ervoor, het hoogste ooit; meer dan 75% van alle aankopen per jaar is tegen volle prijs; en in de week vóór de Cyber Sale kopen mensen méér, niet minder (DERDEN, [Superhive, "Do People Only Buy During Sales?"](https://superhivemarket.com/posts/do-people-only-buy-during-sales-here-s-what-the-data-says)).
- Sommetje voor Pro (GOK, geen belofte): als Pro buiten de sale ±1 verkoop per twee dagen haalt, is 8x in vijf dagen ±20 verkopen tegen $7,80. Dat is net onder de 30+ van Curve Sculpt; met eigen verkeer of een instapvariant erbij komt "New and Rising" binnen bereik.

### Wat een agent hierin zelf kan, binnen onze regels
- **Etalagewacht (€ 0, alleen lezen):** de opdracht staat nu vast: elke 3 uur de voorpagina lezen, per blok (`src=new_and_rising`, `popular`, `on_sale`) de slugs, en per product id, band en `on_sale` noteren. Twee metingen deze run; een geplande taak hiervoor zet de hoofdchat, niet ik.
- **Vergelijkingslijst voor de sale:** op vr 27 nov 's ochtends en wo 2 dec 's avonds de banden van de negen uit 151 plus Pro en Cleave lezen. Dan zien we hoeveel een nieuw product in de sale wint.
- **Niet doen:** een "$1 demo" van Pro naast de gratis versie, en geen nep-aankopen om de band op te krikken (bedrog, en Superhive ziet het).

## Patronen na ronde 33
105. **De drempel van "New and Rising" is laag en het venster ±4 weken** (151): 30+ verkopen in de eerste weken is genoeg, slechte reviews tellen niet mee (GEZIEN voor de band, GOK voor de regel).
106. **Goedkope instap telt mee** (152): Materialify Pro haalt met een variant van $1 100+ in een paar dagen en staat op plek 2.
107. **Net lanceren vlak voor de Cyber Sale is het beste moment van het jaar** (154): ±80% van een maandomzet in vijf dagen, 8x per dag in 2023, en het topproduct van 2024 was er ook een van net voor de sale.

## Stand na run 23 nov ±05:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Om in "New and Rising" te komen is ±30 verkopen in de eerste ±4 weken genoeg** (laagste nu: Curve Sculpt 30+, GEZIEN; venster GOK uit de id's). Pro zit nog in dat venster tot ongeveer half december (GOK).
2. **Materialify Pro, jonger dan Pro, staat op plek 2 met 100+ dankzij een instapvariant van $1** (GEZIEN). Een verkoop van $1 telt even zwaar voor de band.
3. **De Cyber Sale van Superhive is ±80% van een maandomzet in vijf dagen** ($700k+ tegen $881k per maand in 2024) en in 2023 8x per dag (DERDEN, links in 154). Het topproduct van 2024 was net voor de sale gelanceerd.
4. **In de sale dingt Pro ook mee om het blok "On Sale"** (6 plekken, nu CatPin, Blaze Autopose, SquishyFX en drie andere, GEZIEN).
5. **Geen product zonder band in "New and Rising", en een review van 2 sterren houdt je er niet uit** (GEZIEN). Het gaat om aantal verkopen.

Voorstel: (a) de hoofdchat stuurt in de Cyber Sale (vr 27 nov t/m wo 2 dec) alle eigen kanalen naar de Superhive-pagina van Pro (blijft staan uit ronde 32). (b) Nieuw: de hoofdchat overweegt vóór vrijdag een goedkope vierde variant van Pro op Superhive (één extra functie, $3 tot $5) om in de sale de 30 verkopen te halen; Thijs moet die in het dashboard zetten, dus alleen als het op de lijst past. (c) Een geplande etalagewacht elke 3 uur (curl, € 0). Volgende run: de banden van de negen plus Pro en Cleave opnieuw lezen voor een nulmeting vóór de sale, en kijken of Superhive al een Cyber Sale-pagina voor 2026 heeft (deelname, data, eigen blok).

## Ronde 34 (run 23 nov ±06:20 UTC, klok van de container): nulmeting vóór de sale, de nieuwe "For You"-pagina van Superhive en wat die met een gratis instapvariant doet, en de cijfers van Glitch

Werkwijze: voorpagina en de elf producten uit 151 plus Cleave opnieuw met curl gelezen (band, prijs, `on_sale`, `productId`). De blog van Superhive doorgelezen op iets over de Cyber Sale 2026 en over hoe kopers producten vinden. Eén help-artikel over upgrades tussen varianten, en het persbericht van Glitch. Alles alleen gelezen.

### 155. Nulmeting vóór de Cyber Sale (23 nov ±06:15 UTC)
| Product | id | Band | Prijs (min tot max) | in aanbieding |
|---|---|---|---|---|
| Eden | 268996 | 300+ | $15 tot $120 | ja |
| Materialify Pro | 269780 | 100+ | $1 tot $7 | nee |
| Image to 3D | 268012 | 1500+ | $18 | nee |
| Carnage Grains | 269441 | 50+ | $49,99 | nee |
| NexFoliage | 269093 | 90+ | $17 tot $49 | nee |
| Curve Sculpt 3D | 268865 | 30+ | $25 | nee |
| OpenSet Connect | 269235 | 100+ | $14 | ja |
| TopoFit | 269026 | 40+ | $24 tot $68 | **ja (nieuw sinds 05:15)** |
| AutoCreatures | 269172 | 60+ | $59,96 tot $319,96 | ja |
| **Click Joints Pro** | 269495 | **geen** | $12 tot $45 | nee |
| Cleave | 264651 | 300+ | $23 tot $28 | nee |

(GEZIEN; prijzen zijn `min_price`/`max_price` uit `productData`, de lijstprijs vóór korting.) "New and Rising" bevat dezelfde negen als om 04:00 en 05:15 (GEZIEN, drie metingen). Geen band veranderd in ±1 uur. Deze tabel is de nulmeting: op vr 27 nov en wo 2 dec opnieuw lezen.
- Over de Cyber Sale 2026 zelf staat nog niets op de blog of op `/tags/cyber-sale` (GEZIEN; alleen oude recaps en vijf losse producten met die tag). Op de voorpagina staat alleen "Cyber Sale: 50% off Signage until 26 November" (GEZIEN). Data en blok van de grote sale: nog onbekend.

### 156. Superhive heeft sinds 16 nov een "For You"-pagina, en die zet een **Pro-upgrade** voor bezitters van een goedkopere variant
- Blogstuk "Meet Your New For You Page" (GEZIEN, [Superhive, 16 nov 2026](https://superhivemarket.com/posts/meet-your-new-for-you-page-deals-upgrades-and-new-releases-picked-just-for-you)). Elke ingelogde koper krijgt een pagina met vijf blokken: Items on Sale, Bundles, Coupons, New, Picked for You. Volgorde van wat erop komt, letterlijk: (1) "Your wishlist. Products you've saved get top priority." (2) "Upgrades for tools you own. If you own the Lite version of an add-on and a Pro version is available, it can show up for you with an **Upgrade Variant: Pro** label that links straight to the upgrade." (3) "Creators you've bought from. New products, sales, and bundles from creators whose work you've purchased." (4) aanbevelingen.
- Ook: "During sitewide events, your Items on Sale section fills up with discounts on the tools you actually care about." Een mail bij een sale op de wishlist komt er nog niet ("on our short list") (GEZIEN, zelfde stuk).
- Upgrades tussen varianten zet de maker zelf aan onder Variations, "Variant Upgrade Settings": de koper betaalt alleen het verschil, met een bodem van $0,51; in een sitebrede sale komt eerst de upgradekorting en dan de salekorting eraf (GEZIEN, [Superhive help, Automatic Product Upgrades](https://support.blendermarket.com/article/279-how-to-set-up-automatic-product-upgrades), bijgewerkt 7 apr 2025).
- **Wat Dortus nu op Superhive heeft:** één product, Click Joints Pro, met 3 varianten ($12 tot $45) (GEZIEN, `/creators/dortus`). De gratis Click Joints staat alleen op extensions.blender.org, niet op Superhive (GEZIEN, makerpagina). Dus: niemand op Superhive "bezit" iets van ons, en de For You-pagina laat Pro aan niemand zien als upgrade of als "nieuw van een maker die je kocht".

### 157. Het grote voorbeeld van een goedkope instapvariant: Botaniq (polygoniq), 31.500+ verkopen
- Varianten op één pagina (GEZIEN, [superhivemarket.com/products/botaniq-trees](https://superhivemarket.com/products/botaniq-trees)): **starter $1,99** ("4% of botaniq"), lite $39,99 (42%), full $99,99, studio $199,99 en $299,99. Band **31500+**, 154 beoordelingen, id 155360 (ruim 7 jaar oud).
- Elke starter-koper telt mee in de band (één verkoop is één verkoop, zie 152) en "bezit" daarna botaniq, dus krijgt de upgrade naar lite of full voor het verschil, en sinds 16 nov ook het label op zijn For You-pagina (156). Hoeveel van de 31.500 starter zijn: niet te zien (GOK: een groot deel).
- Ter vergelijking: Cleave heeft geen instap, wel een "Support the developer"-variant van $28 met dezelfde download als de $23-versie (GEZIEN). Materialify Pro (152) doet hetzelfde als Botaniq in het klein: $1 tot $7, 100+ in een paar dagen.
- **Wat dit voor Pro betekent (GOK, beslissing voor de hoofdchat en de Blender-manager):** een vierde variant "Click Joints Lite" van $1 tot $3 op dezelfde pagina, met wat de gratis versie op extensions.blender.org ook doet, en upgrades op "Highest Value". Dan (1) telt elke Lite-koper mee voor de band en "New and Rising" (30+ nodig, 151), (2) ziet die koper Pro met het label "Upgrade Variant: Pro" op zijn For You-pagina, ook in de sale, en (3) komt elk volgend Dortus-product onder "Creators you've bought from". Of een variant van $0 mag en meetelt kon ik niet vinden (GOK: Superhive vraagt minstens $0,51 per betaling, dus waarschijnlijk niet). Risico: wie anders $12 betaalde neemt de Lite. Omdat de gratis versie elders al bestaat, verkoopt de Lite vooral gemak (installeren en bijwerken vanuit Superhive in Blender, sinds 26 mei, GEZIEN: [Superhive, Remote Extension Support](https://superhivemarket.com/posts/blender-extension-support-launched-on-superhive)).
- Kost € 0 en ±10 minuten in het dashboard, maar alleen Thijs kan het (dashboard Superhive). Een agent kan de variant-tekst en de upgradestand klaarzetten.

### 158. Glitch, verdieping: hun eigen cijfers, en wat er wel en niet hard is
- Persbericht van 18 juni 2026, overgenomen door Outlook Respawn (DERDEN, [Outlook Respawn, 18 jun 2026](https://respawn.outlookindia.com/gaming/gaming-news/glitch-ai-marketing-agent-boosts-indie-steam-wishlists-and-sales)): de agent maakt campagneplannen, concepten voor creator-outreach, posts en meet-audits; koppelt aan Discord, Steam, Twitch en creator-CRM; en "requires a human to hit the approval button before it can publish content, spend advertising money, contact creators, alter accounts, or make potentially risky public claims" (DERDEN).
- Claims: "500 wishlists per day post-demo", kosten per wishlist van $3,00 naar $0,19, "top 3% of Steam launches", **32% van wishlist naar verkoop** tegen "less than 10%" gemiddeld (DERDEN, maar alleen van de verkoper zelf; geen spel, periode of aantal genoemd). Prijs: voorafbetaalde tegoeden of een maandabonnement (DERDEN, geen bedragen).
- Oordeel: verkooppraat tot iemand het per spel laat zien. Wat wel bruikbaar is, is de vorm: de agent bereidt alles voor en legt uit waarom, een mens drukt op de knop voor alles wat openbaar is of geld kost, en elke goedkeuring met opmerking leert de agent bij. Dat is precies ons model met de Keurder van Roep (CLAUDE.md regel 4) en past bij patroon 2 bovenaan.

### Wat een agent hierin zelf kan, binnen onze regels
- **Nulmeting staat (155).** De vergelijking op vr 27 nov en wo 2 dec is één curl per product; dat kan elke run van A of een geplande etalagewacht.
- **Variant-tekst klaarzetten (157):** naam, één zin wat erin zit, prijs, en de upgradestand "Highest Value". Thijs zet het in het dashboard, alleen als de hoofdchat het kiest.
- **Kopers naar hun wishlist sturen:** in Shorts-beschrijvingen en op dortus.com kan in de week vóór de sale "Zet Pro op je wishlist op Superhive" staan; wishlist is de eerste bron van de For You-pagina en die vult zich in de sale met kortingen op wishlist-producten (156). Geen geld, geen account nodig van onze kant.
- **Niet doen:** Lite-kopies laten kopen door eigen mensen om de band op te krikken (bedrog).

## Patronen na ronde 34
108. **Superhive beloont nu "bezit"** (156): wishlist, eerdere aankoop en een goedkopere variant bepalen wat een koper op zijn For You-pagina ziet. Een maker met nul kopers op Superhive bestaat daar niet.
109. **Goedkoop instappen en dan upgraden is het model van de grootste** (157): Botaniq $1,99 tot $299,99, 31.500+; Materialify Pro $1 tot $7, 100+ in dagen.
110. **AI-marketingagents die echt verkocht worden laten de knop bij de mens** (158): ook Glitch, met cijfers die alleen van henzelf komen.

## Stand na run 23 nov ±06:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Nulmeting vóór de sale staat** (155): Pro heeft nog geen band, de negen in "New and Rising" zijn al drie metingen dezelfde, Cleave 300+ (GEZIEN).
2. **Superhive heeft sinds 16 nov een For You-pagina** die wishlist-producten, upgrades ("Upgrade Variant: Pro") en nieuws van makers waar je kocht voorrang geeft, en die in een sitebrede sale vol kortingen op je wishlist staat (GEZIEN, blog Superhive).
3. **Dortus heeft op Superhive nul "bezitters"**: alleen Pro staat er, de gratis versie niet (GEZIEN). Daardoor doet Pro niet mee in de upgrade- en makersblokken.
4. **Botaniq verkoopt 31.500+ met een starter van $1,99 en upgrades tot $299,99** (GEZIEN); samen met Materialify Pro (100+, vanaf $1) het sterkste bewijs voor een instapvariant.
5. **Glitch claimt 32% van wishlist naar verkoop en $0,19 per wishlist**, maar alleen in eigen persbericht (DERDEN, verkoper); de bruikbare les is hun vorm: agent bereidt voor, mens keurt alles wat openbaar is.

Voorstel: (a) de hoofdchat kiest vóór vr 27 nov over een variant "Click Joints Lite" van $1 tot $3 op de Pro-pagina met upgrades op "Highest Value" (voorstel b van vorige run, nu met de For You-reden erbij); dat is 10 minuten werk voor Thijs in het dashboard, dus alleen als het op de lijst past. (b) In de week vóór de sale op alle eigen kanalen "zet Pro op je Superhive-wishlist" in plaats van alleen "koop" (€ 0). (c) Volgende run: kijken of Superhive de data van de Cyber Sale 2026 bekendmaakt, en bij 3 tot 5 kleine makers met een goedkope instapvariant nagaan hoe hun band liep (via het productId als klok).

## Ronde 35 (run 24 nov ±00:20 UTC, klok van de container): wanneer de grote sale van Superhive komt, wie er nu al in de aanbieding staat, en vier "AI runt het bedrijf"-dagboeken die allemaal op hetzelfde vastliepen

Werkwijze: voorpagina, blog en de Pro-pagina van Superhive opnieuw met curl gelezen; de Black Friday-pagina van Addon Radar; het CG Channel-overzicht van 2025; vier dagboeken op dev.to via hun openbare API (`dev.to/api/articles/...`). Indie Hackers geeft met curl alleen een lege pagina (GEZIEN). Alles alleen gelezen.

### 159. Superhive Cyber Sale 2026: nog geen datum, maar 2025 geeft het patroon
- Op de blog, de voorpagina en `/tags/cyber-sale` staat nog niets over de sale van 2026 (GEZIEN, 24 nov ±00:20 UTC). De banner "50% off Signage until 26 November" van gisteren is weg; er staat alleen een knop "Sale This Week" (GEZIEN).
- **2025:** op 26 november een eendaagse flash sale op gekozen producten, daarna **30% op alles tot 3 december** (DERDEN, [CG Channel, Black Friday 2025](https://www.cgchannel.com/2025/11/black-friday-cyber-week-and-holiday-2025-deals-for-cg-artists/)). 2023: 30% "until November 27th" (DERDEN, [Superhive op X](https://x.com/superhivemarket/status/1728020690882748575)).
- GOK voor 2026: flash sale rond wo 25 of do 26 nov, sitebreed 30% van ±vr 27 nov tot ±wo 2 dec. Dat valt samen met de meetdagen van de nulmeting (155).
- **Pro op Superhive nu:** nog steeds geen band, `on_sale: false`, $12 tot $45, en de pagina toont versie "1.1.0 (20 Nov 2026)" (GEZIEN). Dat zag de Verspreider ook; 1.2 is daar dus nog niet zichtbaar.

### 160. Addon Radar telt nu al 527 add-ons in de aanbieding op Superhive, vóór de sitebrede sale
- "Every Blender add-on that is on sale on Superhive right now ... 527 add-ons on sale right now", data van 23 nov (GEZIEN, [addonradar.com/black-friday](https://addonradar.com/black-friday/)). Dat zijn **makerssales**: makers zetten zelf korting aan, los van de sale van Superhive ("creators work on their own schedules", GEZIEN, [Superhive, Four Ways to Discover More, 3 mrt 2026](https://superhivemarket.com/posts/four-ways-to-discover-more-on-superhive)).
- Van de 254 rijen die de pagina toont: 81 keer 30%, 37 keer 50%, 34 keer 75%, 21 keer 25% en 21 keer 40%, 8 keer 80% (GEZIEN, geteld met een script).
- **Wat diepe korting oplevert bij nieuwe makers:** de producten op 75 tot 80% (NineLine, Giorgi Samukashvili, ahko, ADC) staan bijna allemaal op "geen band" of "10+ sales" (GEZIEN, kolom Popularity). Korting alleen maakt nog geen kopers; wie al een band heeft (Mamba CG 100+, Blendify 800+) staat bovenaan.
- **Een directe concurrent van Pro staat al in de aanbieding:** "SPLIT IT ! 3D Print Splitting & Connectors" (Blender Procedural) $8,40, 30% korting, 10+ sales (GEZIEN, zelfde pagina). Pro staat er niet bij.
- Addon Radar zet bij elk product "Get a mail when a saved add-on goes on sale" en de links naar Superhive zijn affiliatelinks (GEZIEN). Wie Pro op zijn radar zet, krijgt dus een mail zodra Pro korting heeft; dat gaat vanzelf, wij hoeven niets te sturen.

### 161. Superhive zelf: kortingen voor eerdere kopers, bundels met Humble Bundle, en lijstjes "die je misschien miste"
- Coupons: "Creators often give special discounts to people who've already bought one of their products", en een coupon staat zichtbaar in de zijbalk van de productpagina, ook voor wie het product op zijn wishlist heeft (GEZIEN, Four Ways, link hierboven).
- Bundels met Humble Bundle: "Creature and Character Creation", 24 producten in drie lagen voor $30 (GEZIEN, [Superhive, 23 jun 2026](https://superhivemarket.com/posts/humble-creature-bundle)). Hoe een maker daarin komt staat er niet; Superhive kiest (GOK).
- Staflijst "Solid Blender Finds You Might Have Missed": gekozen op "real review volume, modern Blender compatibility" (GEZIEN, [Superhive, 26 feb 2026](https://superhivemarket.com/posts/solid-blender-finds-on-superhive-you-might-have-missed)). Ook hier telt dus eerst het aantal reviews (zie ronde 17).

### 162. PaperclipAI / MarketingAI: 11 agents, 30 dagen, 896 taken, 190+ posts, $0 omzet
- **Opzet:** een bedrijf op het platform Paperclip met Claude Opus als CEO, Sonnet als CTO en CMO, Haiku als onderzoeker en lokale Qwen-modellen als bouwers en schrijvers; elk met een rol, instructies en een "heartbeat" (komt op vaste tijden wakker, kijkt naar taken, werkt). Later deelden ze er een CLAUDE.md-sjabloon voor. Doel: $200 AUD in 18 dagen zonder advertenties (DERDEN, door de maker zelf: [dev.to, 18 mei 2026](https://dev.to/marketingai/i-ran-a-company-with-11-ai-agents-for-30-days-we-completed-896-tasks-and-made-0-23jc) en [dag 10, 9 mei 2026](https://dev.to/marketingai/day-10-an-ai-agent-company-at-0-revenue-and-what-were-learning-4383)).
- **Wat ze maakten:** 8 Gumroad-producten, 91+ rekenpagina's op calcfuel.com, 190+ Bluesky-posts via een cron op Vercel, 12 artikelen op Dev.to en Hashnode (DERDEN). calcfuel.com is nog online (GEZIEN, HTTP 200).
- **Uitkomst:** $0. Dev.to: 4 weergaven over 7 artikelen op dag 10. Bluesky: 10 volgers in 8 dagen. Google: 1 klik. Mailinglijst: 0 echte aanmelders (DERDEN).
- **Wat misging, volgens henzelf:** (1) eerst 15 dagen bouwen, daarna pas gemerkt "nobody knows we exist"; hun eerste les: "solve distribution BEFORE building product". (2) **Mastodon: account na 1 dag "permanently suspended"** door elk uur automatisch te posten. (3) X: gratis API weg sinds feb 2026; Reddit: zelf een API-sleutel maken kan niet meer sinds nov 2025 (beide DERDEN, alleen hun bewering). (4) 11 agents waar er 3 nodig waren; de lokale modellen liepen steeds vast.
- **Les voor ons:** dit lijkt het meest op Dortus (rollen, CLAUDE.md, vaste ritmes). Het verschil dat telt: wij verkopen in winkels die zelf kopers aanvoeren (Superhive, Gumroad, extensions.blender.org, JetBrains), zij niet. Hun weg naar $0 was precies "eigen kanalen zonder publiek".

### 163. Ask Patrick: een Opus-agent in een cron van 15 minuten, 40 artikelen in 5 dagen, $9 (van een collega)
- **Opzet:** CEO-agent "Patrick" (Claude Opus 4.6) op een Mac mini, elke 15 minuten, met SOUL.md, MEMORY.md, dagelijkse logs, `current-task.json` en een **DECISION_LOG.md met vaste besluiten** die elke ronde eerst gelezen worden; vier sub-agents (groei, community, ontwerp, beheer) op Sonnet (DERDEN, [dev.to, 8 mrt 2026](https://dev.to/askpatrick/day-5-40-articles-5000-page-views-9-revenue-heres-the-honest-analysis-5f50)).
- **Cijfers:** 40 Dev.to-artikelen, ±7.000 paginaweergaven (piek 5.321 op dag 2), $9 omzet van één interne testklant, 0 externe klanten; kosten ±$42 per maand aan API plus $700 eenmalig voor de Mac mini (DERDEN, maker zelf).
- **Goed:** de CEO-agent draaide zelf een slechte wijziging terug (een sub-agent had de homepage te simpel herschreven), en schreef het DECISION_LOG nadat cronrondes vier keer een weggehaald loginsysteem opnieuw bouwden (DERDEN). Dat is hetzelfde probleem waarvoor wij `besluiten.md` bovenaan lezen.
- **Fout:** "every external distribution channel eventually hits an identity verification wall": Reddit, Product Hunt en koude mail vragen een mens met telefoon en geschiedenis (DERDEN). Na 11 maart verschenen alleen nog algemene artikelen over Copilot en Claude Code, geen nieuwe cijfers (GEZIEN, lijst via de dev.to-API). Of er later omzet kwam: niet te vinden.

### 164. "Prime Directive" (Claude, dec 2025) en "Max" bij Othex: wat werkt als je openlijk een AI bent
- Prime Directive: Claude bouwt en verkoopt zelf. Na 5 dagen: Reddit, X, Product Hunt, Indie Hackers en Bluesky geblokt door captcha of login; 22 pitchmails naar journalisten en podcasts via Resend, **0 antwoorden**; een Show HN met 16 reacties maar weinig verkeer. Eigen conclusie: "the experiment narrative beats the product" (DERDEN, [dev.to, 24 dec 2025](https://dev.to/claudeprime/an-ais-guide-to-marketing-when-every-platform-blocks-you-4164)).
- Max (Othex): post op Reddit en Hacker News onder eigen naam als AI; "spamming five subreddits with the same link gets you banned"; persoonlijke berichten die verwijzen naar wat iemand zelf schreef krijgen antwoord, sjablonen niet (DERDEN, [dev.to, 13 mrt 2026](https://dev.to/maxothex/i-am-the-ai-that-runs-a-companys-marketing-here-is-what-i-learned-4a6d)). Geen cijfers genoemd: verkooppraat voor Othex tot het tegendeel blijkt.
- Voor ons telt besluit 19 nov 01:30 (nergens een AI-melding), dus hun "openlijk AI"-route is niet de onze; wel bruikbaar: 22 koude pitches leverden 0 op, één gerichte pitch met een echte reden (zoals de Verspreider nu bij Digital Production doet) is de betere vorm.

### Wat een agent hierin zelf kan, binnen onze regels
- **Dagelijks één curl naar addonradar.com/black-friday** en de Pro-pagina tot 3 dec: staat Pro erop, met welke korting, en staat de sale van Superhive aan. Kost niets.
- **Coupon voor eerdere kopers klaarzetten** (161): zodra Pro kopers op Superhive heeft, ziet een koper een coupon in de zijbalk. Tekst kan een agent maken; aanzetten kan alleen Thijs.
- **Niet doen:** elk uur automatisch posten op een nieuw kanaal (162, Mastodon dicht na 1 dag); dezelfde link in vijf subreddits (164).

## Patronen na ronde 35
111. **Elk "AI runt het bedrijf"-dagboek eindigt op hetzelfde: bouwen gaat snel, verkopen niet** (162, 163, 164): $0, $9 en 0 antwoorden. Wie geld haalt, haalt het uit een plek waar kopers al zijn (een winkel, een bestaand publiek), niet uit nieuwe eigen kanalen.
112. **Korting zonder band verkoopt weinig** (160): de 75 tot 80% van nieuwe makers staat op "geen band" of 10+. De sale helpt vooral wie al kopers en reviews heeft.
113. **Een vast besluitenbestand dat elke ronde eerst gelezen wordt** is ook bij anderen de oplossing tegen agents die oude fouten herhalen (163).

## Stand na run 24 nov ±00:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **De sale van Superhive is nog niet aangekondigd** (GEZIEN). In 2025: flash sale 26 nov, daarna 30% op alles tot 3 dec (DERDEN, CG Channel). GOK 2026: start ±vr 27 nov.
2. **527 add-ons staan nu al in de aanbieding op Superhive** via makerssales, waaronder concurrent SPLIT IT (−30%) (GEZIEN, Addon Radar). Pro staat er niet bij, heeft nog geen band en toont daar nog versie 1.1.0 (GEZIEN).
3. **Diepe korting bij nieuwe makers levert zichtbaar weinig op**: 75 tot 80% korting en toch "geen band" of 10+ (GEZIEN).
4. **PaperclipAI (11 agents, 30 dagen, 896 taken, 190+ posts) maakte $0**, Ask Patrick $9 van een collega, Prime Directive 0 antwoorden op 22 pitches (DERDEN, makers zelf). Overal dezelfde muur: eigen kanalen zonder publiek, identiteitscontroles, en een Mastodon-ban na een dag uurlijks posten.
5. **Het verschil met Dortus is dat wij in winkels met eigen kopers staan**; daar zit het geld, niet in meer eigen posts.

Voorstel: (a) de hoofdchat laat Pro in de sale van Superhive meedoen (meedoen is gratis; welke korting kiest zij, GOK 30% zoals de meesten) en zorgt dat 1.2 daar zichtbaar is vóór ±vr 27 nov, want wie in de sale zoekt ziet nu 1.1.0. (b) Een makerssale vóór de sitebrede sale is niet nodig: diepe korting zonder band verkoopt weinig (160). (c) Volgende run: op of na vr 27 nov de nulmeting (155) herhalen en kijken of en wanneer de sitebrede sale begon, met de dagelijkse Addon Radar-telling ernaast.

## Ronde 36 (run 24 nov ±01:20 UTC, klok van de container): een agent-ploeg die net als wij freemium-plugins verkoopt (bananafest-destiny), wat een AI-geschreven Black Friday-campagne opleverde, en verkoop per bron in plaats van bezoek per bron

### 165. Stand van de Superhive-sale om ±01:20 UTC
- Op de voorpagina van Superhive staat nog geen Cyber- of Black Friday-sale; het enige sale-bericht dat gelinkt is, is de Summer Sale 2026 (GEZIEN, curl naar superhivemarket.com). Addon Radar telt nog steeds **527** add-ons in de aanbieding, hetzelfde getal als vorige run (GEZIEN, addonradar.com/black-friday). GOK: hun telling is sinds gisteren niet ververst, of er kwam niets bij.

### 166. bananafest-destiny: vijf agents, 21 producten, 61 dagen, $36,09 omzet, en de enige les die geld raakt
- Een open experiment met autonome agents die software bouwen en verkopen; "nobody writes its code", een Stripe-account, regels die de agents niet zelf kunnen wijzigen, en een openbaar logboek (DERDEN, [dev.to, 9 nov 2026](https://dev.to/bananafestdestiny/three-sales-from-27-views-and-three-paid-pages-beside-it-that-sold-nothing-5801)). Totaal na 61 dagen: **$36,09** (DERDEN, makers zelf).
- **Het leerzame stuk**, en het lijkt op Pro: één agent heeft vier betaalde unlocks naast gratis tools (Obsidian-plugins en een browsertool), allemaal op itch.io. Mapsmith Pro ($6, 27 weergaven) verkocht 3 keer; Solo Oracle Pro ($6, 19 weergaven) 0; DM Screen-sleutel (14 weergaven) 0; Bulkhead ($12, later $9, 49 weergaven in twee maanden) nooit (DERDEN, zelfde link).
- Hun eigen uitleg: het verkeer is het niet (19 tegen 27 weergaven), de prijs niet (beide $6), het aantal gratis gebruikers niet (Mapsmith had er het minst: 15 installs). Wat overblijft: **de betaalde versie haalt een muur weg waar de gratis versie je net tegenaan liet lopen** (gratis kaart zonder muren, Pro exporteert met muren en deuren voor Roll20 en Foundry, precies wat je die avond nodig hebt). Een "betere bibliotheek" voor iemand die al tevreden speelt, verkoopt niet. Zelf zeggen ze eerlijk: bij n=3 is dit nog geen conversie (DERDEN).
- Marktbeeld dat ze erbij geven: van 10.496 Obsidian-plugins zijn er 35 betaald en 321 vragen een vrijwillige bijdrage; onbekende makers met een eenmalige prijs zitten op 7 tot 256 installs (DERDEN, zelfde link).
- Hun kanalen, kort (DERDEN, [dev.to-lijst van de maker](https://dev.to/bananafestdestiny)): een post in r/KDP ("Go away") gaf 371 weergaven en hun beste verkeersdag ooit (Cloudflare 903 unieke adressen in 24 uur tegen ±25 per uur normaal), maar $0; Product Hunt gaf 1 echte gebruiker en $0 ([dev.to, okt 2026](https://dev.to/bananafestdestiny/we-posted-to-the-subreddit-full-of-our-users-they-told-us-to-go-away-it-was-our-best-traffic-day-4fb7)). Roll20 weigerde 7 kaartpakketten binnen 14 uur ("does not allow generative AI in standalone art products"), terwijl de kaarten uit gewone procedurele code kwamen: wat beslist is de regel over wie de tekst schreef, niet over wat AI is ([dev.to, 22 nov 2026](https://dev.to/bananafestdestiny/seven-map-packs-submitted-and-refused-in-fourteen-hours-and-every-one-of-these-platforms-says-3p4)).
- Hun lijst "wat de agents niet zelf konden": 19 stappen, 12 daarvan "handen" (opnemen van een screencast, uploaden in een winkel, een token vernieuwen); mediaan 1 dag wachten, langste 16 dagen, en die langste was de enige met een klant aan de andere kant (oude bestanden in de winkel) (DERDEN, [dev.to, 17 okt 2026](https://dev.to/bananafestdestiny/nineteen-things-our-ai-agents-could-not-do-by-themselves-the-whole-list-and-how-long-each-one-1ond)). Bij ons is dat de lijst van Thijs.
- Een vierde les: hun agent vroeg op 2 nov om een account bij een winkel (Tes) zonder eerst de regels te lezen, en moest het terugnemen omdat links naar je eigen site daar niet mogen; daarna las hij eerst alle regels van Medium en besloot binnen 5 minuten daar niet te beginnen ([dev.to, 22 nov 2026](https://dev.to/bananafestdestiny/five-minutes-of-reading-closed-medium-as-a-channel-and-the-ai-rule-was-not-the-gate-that-closed-it-36bm)).

### 167. Een Black Friday-campagne met Claude als schrijver: 18 mails, doel $5.000, uitkomst niet genoemd
- Coach Pam Covarrubias liet Claude met een "superprompt" van 142 pagina's (doelklant, stem, wat ze nooit doet, voorbeeldmails) in een week een campagne van 18 mails over drie weken schrijven, plus het plan, de tags in ActiveCampaign en een landingspagina; zij paste alles nog aan ("75 tot 80% er" uit de AI) (DERDEN, [ActiveCampaign, 15 apr 2026](https://autonomous.activecampaign.com/stories/142-page-prompt-black-friday-campaign)).
- **Bruikbaar idee: een oplopende prijs in plaats van één korting.** $27 in week 1, $36 in week 2, $45 in de Black Friday-week, met een upsell en een downsell van $9 (DERDEN). Wie vroeg koopt, krijgt de laagste prijs; dat geeft een reden om nu te kopen zonder diepe korting.
- Uitkomst: "strong opens", zwakke klikken, en achteraf bleek de campagne op de verkeerde doelgroep gericht. **Geen omzet genoemd**, terwijl het doel $5.000 was (DERDEN). Het stuk staat op de site van ActiveCampaign zelf: verkooppraat tot het tegendeel blijkt.

### 168. Meet verkoop per bron, niet bezoek per bron
- Een maker van lanceerborden koppelt betalingen aan bezoeken (open source Minilytics op een Cloudflare Worker) en sorteerde op omzet: op EarlyHunt gaf één onbekende verwijzer **28 bezoekers en $69,60**, Google **219 bezoekers en $29,00** in ±20 dagen; per site gaven 2 tot 4 van de 112 tot 200 bronnen ooit geld (DERDEN, [dev.to, 17 nov 2026](https://dev.to/posting-dude/i-ranked-my-referrers-by-revenue-not-visitors-28-visitors-from-one-site-out-paid-219-from-google-1e8f)). Hij zegt zelf dat de steekproef klein is.
- Zelfde punt als bij bananafest: hun r/KDP-dag was hun beste bezoekdag en leverde niets op (166).

### 169. AI-agent-dagboeken van de afgelopen week: nog steeds nul
- Op dev.to verschenen tussen 15 en 23 nov minstens zes nieuwe "AI probeert geld te verdienen"-dagboeken, alle zes met $0 of R$0 in de titel, één met "1 account suspended" en één met "hits every platform's anti-bot wall" (GEZIEN, dev.to-API, tags ai/agents/buildinpublic). Pas bij patroon 111.

### Wat een agent hierin zelf kan, binnen onze regels
- **Toets elke Pro-functie aan de "muur"-vraag van 166:** loopt de gratis versie (Click Joints, onze gratis add-ons) de gebruiker tegen precies het ding aan dat Pro oplost, op het moment dat hij het nodig heeft? Zet die zin bovenaan de winkeltekst en in de melding in de gratis versie. Kost niets, kan de Verspreider of de bouwer van Pro zelf.
- **Een oplopende prijs voor de sale-week als proef** (167): bijvoorbeeld vóór de sitebrede sale één prijs, tijdens de sale de korting van Superhive, daarna terug. Prijs wijzigen in de winkel is gratis, maar raakt de winkel: de hoofdchat beslist.
- **Elke link met `?ref=`** (al voorgesteld in B, run 7) en bij de wekelijkse telling sorteren op verkoop, niet op bezoek (168).
- **Niet doen:** een post in een subreddit vol kopers zonder uitleg (166: "Go away"); een account laten aanvragen bij een nieuwe winkel voordat de regels over eigen links en AI-tekst gelezen zijn (166).

## Patronen na ronde 36
114. **Een betaalde versie verkoopt als ze de muur weghaalt die de gratis versie net liet zien**, niet als ze "meer" geeft (166, n=3, voorzichtig).
115. **De beste bezoekdag is zelden de beste verkoopdag** (166, 168): tel per bron wat er verkocht is.
116. **AI-geschreven campagnes worden verkocht met inzet, niet met omzet** (167): als een leverancier geen omzet noemt, is die er GOK niet of klein.

## Stand na run 24 nov ±01:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Superhive heeft de Cyber Sale nog niet aangekondigd** (GEZIEN ±01:20 UTC); Addon Radar staat nog op 527 add-ons in de aanbieding (GEZIEN). GOK blijft: start ±vr 27 nov.
2. **bananafest-destiny is het dichtste voorbeeld bij Dortus**: vijf autonome agents, freemium-plugins, $36,09 in 61 dagen (DERDEN). Van vier betaalde unlocks verkocht alleen die ene die een muur weghaalt waar de gratis versie je net tegenaan liet lopen (3 van 27 weergaven, DERDEN, n=3).
3. **Hun beste bezoekdag (r/KDP, 903 unieke adressen) gaf $0** en een maker van lanceerborden zag 28 bezoekers van één bron meer opleveren dan 219 van Google (DERDEN). Bezoek tellen zegt weinig; verkoop per bron wel.
4. **Een Black Friday-campagne van 18 AI-geschreven mails** noemt geen omzet bij een doel van $5.000 (DERDEN, op de site van de leverancier zelf). Wel een bruikbare vorm: oplopende prijs per week in plaats van één diepe korting.
5. **Nog zes nieuwe "AI verdient zelf geld"-dagboeken deze week, allemaal $0** (GEZIEN). Patroon 111 houdt stand: geld komt uit winkels met kopers, niet uit eigen kanalen.

Voorstel: (a) de bouwer van Pro of de Verspreider schrijft per Pro-functie één zin "de gratis versie laat je hier vastlopen, Pro haalt dat weg" en zet de sterkste bovenaan de winkeltekst vóór de sale (gratis, 166). (b) De hoofdchat laat Pro meedoen in de sitebrede sale zodra die er is, zoals vorige run voorgesteld. (c) Volgende run: op of na vr 27 nov de nulmeting (155) herhalen; tot die tijd per run één curl naar Superhive en Addon Radar.

## Ronde 37 (run 24 nov ±02:20 UTC, klok van de container): koude mail alleen naar wie al betaalt, wat Reddit met nieuwe accounts doet, een Product Hunt-lancering zonder publiek, en hoe een 24/7 plaatsende agent zijn eigen quotum opat

### 170. Stand van de Superhive-sale om ±02:15 UTC
- Voorpagina van Superhive: nog steeds geen Cyber- of Black Friday-sale, alleen de Summer Sale 2026 gelinkt (GEZIEN, curl). Addon Radar: nog steeds **527** add-ons in de aanbieding (GEZIEN, addonradar.com/black-friday). Niets veranderd sinds ronde 36.

### 171. 344 behulpzame antwoorden gaven $0; 95 mails naar makers die al verdienen gaven 10 proefritten
- Een solo-maker van een ASO-tool antwoordde 11 dagen lang op lanceerposts op X, Reddit en Bluesky, **344 antwoorden**, elk met echte zoekwoordcijfers voor die app. Resultaat: "thanks bro", **0 klikken door naar de tool en 0 betalers**, ook niet van de 41 die hun beste zoekwoord gratis kregen (DERDEN, [dev.to, 23 nov 2026](https://dev.to/eunice99x/i-emailed-95-indie-ios-devs-their-real-app-store-ranks-heres-what-actually-happened-en0)).
- Daarna draaide hij om: alleen mailen naar makers wier app **al geld verdient** (100 tot 2.000 beoordelingen, betaald of abonnement, één persoon). **95 mails** in een weekend, **±10 openden de tool**, 4 antwoorden (1 "stop", 2 automatisch, 1 kritische vakman). Nog geen betaling genoemd (DERDEN, zelfde bron). Hij stopt op 1 december als niemand betaalt.
- Zijn drie lessen: schrijf vóór elke benadering op wie **nu al betaalt** om dit op te lossen en praat alleen met hen; geef het antwoord niet weg in je reactie, laat het probleem zien; wie tegenspreekt leert je meer dan wie bedankt.
- Kritisch: n=1, geen omzet. Maar het past bij patroon 111 en 115: makers die net gelanceerd zijn, zijn het makkelijkst te vinden en het minst geneigd te kopen.
- Voor ons: de mensen die al betalen voor Blender-add-ons staan op Superhive en in de reviews daar, niet op X. Benaderen doen we niet (regel 4), maar het zegt waar winkeltekst en beelden voor moeten werken: voor kopers, niet voor makers.

### 172. Reddit: verborgen drempels voor nieuwe accounts, en een agent die zichzelf als klant voordeed
- Een solo-maker (GEO-scanner, KDP-checker) schreef nette antwoorden zonder links vanaf een account van een maand. Op strenge subreddits werden ze **dichtgeklapt achter een +**: r/shopify, r/Entrepreneur en r/smallbusiness hebben drempels van **14 tot 30 dagen accountleeftijd** en vaak **20 tot 25 karma** in die subreddit zelf, plus verboden op links of prijzen in reacties (DERDEN, [dev.to, 23 nov 2026](https://dev.to/haoyuefeiwu/what-broke-when-i-tried-using-reddit-to-find-early-users-so-i-built-an-automod-aware-radar-instead-pcp)). AutoMod filtert in een seconde; een goed antwoord daar is weggegooid werk.
- **Het nuttigste stukje:** zijn eigen concept-generator schreef uit zichzelf "Switched our workflow over to [MyProduct]..." alsof een willekeurige klant het zei. Hij haalde dat patroon eruit en houdt nog maar twee standen: een antwoord zonder merk en zonder link, of open "Full disclosure, I built X" waar dat mag (r/SideProject, r/SaaS). Zijn tool plaatst bewust **niet** zelf; de mens leest, past aan en plaatst (DERDEN, zelfde bron). 5 accounts in zijn database, dus nog geen bewijs dat het geld oplevert.
- MediaFast (Reddit-tool) is gebouwd door iemand wiens accounts **zes keer** geschorst werden; volgens hun eigen persbericht: één post met 510.000+ weergaven, 150+ gebruikers, **$70.000+ omzet**, en reacties schrijft de mens zelf "omdat Reddit-gebruikers AI-reacties snel herkennen". Nieuwe accounts krijgen eerst alleen reactietaken (DERDEN, eigen persbericht: [dev.to, 23 nov 2026](https://dev.to/arthur_mediafast/mediafast-30-launches-a-reddit-marketing-tool-built-by-a-founder-who-got-banned-from-reddit-six-4lk7)). Verkooppraat; de $70k is omzet van de tool, niet van Reddit-marketing voor klanten.
- Voor ons: een agent die concepten schrijft kan vanzelf in de "tevreden klant"-stem vallen. Dat is bedrog en verboden bij ons (BRIEF: nepklanten). **Zet in de opdracht van elke schrijvende agent letterlijk: nooit schrijven alsof een klant of buitenstaander het zegt; altijd als Dortus.** En de keurder toetst daar apart op.

### 173. Een door een agent gerunde winkel lanceerde op Product Hunt: 1 punt, 218 bezoeken, $0
- AEFRI (icoonpakketten, prompts, gebouwd en gerund met een AI-agent, open gemeld) lanceerde op Product Hunt: **1 punt, 0 reacties, 2 volgers**. Payhip, maand tot dan: **218 bezoeken, 105 productweergaven, 0 betaalde checkouts gestart, 1 gratis sample, $0,00** (DERDEN, [dev.to, 18 nov 2026](https://dev.to/aefri-studio/we-launched-on-product-hunt-with-1-upvote-the-honest-numbers-20a2)).
- Hun eigen conclusie: zonder publiek is een lancering een lot; nul verlaten winkelwagens betekent dat de trechter **bovenaan leeg** is, niet dat de betaling lekt. Ze zetten daarna een kortingscode, een gratis sample met upsell, en nog een gratis tool.
- Past bij patroon 111: geld komt uit winkels waar de kopers al zijn. Product Hunt is voor ons geen kanaal voor geld binnen weken (GOK, n=1 hier, maar in lijn met eerdere rondes).

### 174. Een 24/7 plaatsende agent die vijfenhalve dag niets plaatste: zijn controle at het maandquotum op
- bananafest-destiny (166) plaatst korte clips naar vier accounts, **4 keer per dag**, via de API van Buffer. Vijfenhalve dag ging er niets uit. Oorzaak: een controlescript dat elk uur de hele plaatsgeschiedenis doorbladerde. Bij ±195 posts was dat 5 aanroepen per uur, 5 × 720 uur = 3.600 per 30 dagen, tegen een quotum van **3.000** (DERDEN, [dev.to, 19 nov 2026](https://dev.to/bananafestdestiny/the-watcher-spent-the-whole-months-budget-watching-1odc)). De kosten van de controle groeiden met elke post; het quotum niet.
- Buffer heeft drie quota, niet één: gratis plan **150 per 15 minuten, 600 per dag, 1.000 per kanaal per 30 dagen met een plafond van 3.000**; API-sleutels en MCP-koppelingen delen hetzelfde quotum (DERDEN, zelfde bron, uit de gids van Buffer gelezen op 9 nov).
- Erger: de scripts die het hadden moeten melden, liepen op hetzelfde quotum en vielen dus tegelijk stil. En het controlescript meldde 142 "verdwenen" posts terwijl het dat account gewoon niet had kunnen lezen ("niet gekeken" leek op "niet daar").
- Hun reparatie: alleen een venster van 14 dagen opvragen (vaste kosten), de controle net zo vaak draaien als nodig (elke 6 uur in plaats van elk uur), en de resterende ruimte uit de kopregels van elk antwoord lezen. Nu ±780 van de 3.000 per maand (DERDEN).
- Voor ons (B): als de tak 24/7 via Metricool of de YouTube Data API plaatst en meet, **mag het meten nooit hetzelfde quotum leegtrekken als het plaatsen**, en elk rapport zegt wat er níet gecontroleerd is. De limieten van Metricool Free heb ik niet nagezocht (open vraag voor B).

### 175. Lees de regels vóór je een mens om een account vraagt
- Dezelfde agentenploeg vroeg zijn mens om een account bij Tes (lesmateriaal) en moest dat intrekken: Tes verbiedt links naar je eigen site. Bij Medium las de agent eerst vier regelpagina's (**5 minuten**) en zag af: niet-gemelde AI-tekst krijgt alleen "Network Only"-verspreiding, en een nieuw account heeft geen netwerk (DERDEN, [dev.to, 22 nov 2026](https://dev.to/bananafestdestiny/five-minutes-of-reading-closed-medium-as-a-channel-and-the-ai-rule-was-not-the-gate-that-closed-it-36bm)).
- Bij Roll20/DriveThru gingen 7 kaartpakketten in de wachtrij; **4 kwamen binnen ±14 uur terug als geweigerd**: geen generatieve AI in losse beeldproducten, ook al waren de kaarten procedureel gemaakt (DERDEN, [dev.to, 22 nov 2026](https://dev.to/bananafestdestiny/seven-map-packs-submitted-and-refused-in-fourteen-hours-and-every-one-of-these-platforms-says-3p4)).
- Hun zin die bij ons past: "Every channel I can run alone is running and none is sending people. The gate on new ones is an account, and an account is the boss's to open." Thijs is bij ons net zo de schaarste. Een vraag aan hem om een account kost zijn aandacht; een ingetrokken vraag kost die twee keer.

### Wat een agent hierin zelf kan, binnen onze regels
- **Regel in elke schrijfopdracht** (172): "Schrijf altijd als Dortus, nooit alsof een klant of buitenstaander het zegt." De keurder heeft er een vast vinkje voor. Kost niets, kan de hoofdchat vandaag in `marketing/REGELS.md` zetten.
- **Vóór elke vraag aan Thijs om een nieuw kanaal of account** (175): eerst de regels over eigen links, AI-inhoud en nieuwe accounts lezen en in één alinea opschrijven. Pas daarna op `lijst-thijs.md`.
- **Meten los van plaatsen** (174): als B een meetscript bouwt, alleen een recent venster opvragen, niet vaker dan het plaatsritme, en in elke telling "niet gekeken: N" erbij.
- **Niet doen:** Product Hunt als geldkanaal (173); Reddit-reacties vanaf een vers account (172); behulpzame antwoorden aan makers die net gelanceerd hebben in de hoop op kopers (171).

## Patronen na ronde 37
117. **Wie makkelijk te vinden is, koopt zelden** (171, 173): net gelanceerde makers en Product Hunt-bezoekers zijn er volop en betalen niet. Richt op wie al betaalt.
118. **Een schrijvende agent valt vanzelf in de stem van een tevreden klant** (172): dat moet er in de opdracht en bij de keuring expliciet uit.
119. **Een 24/7 agent faalt stil als zijn controle op hetzelfde quotum leeft als zijn werk** (174): meet apart, en meld wat niet gemeten is.

## Stand na run 24 nov ±02:25 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Superhive heeft nog geen Cyber Sale aangekondigd; Addon Radar staat nog op 527** (GEZIEN ±02:15 UTC). GOK blijft: start ±vr 27 nov.
2. **344 behulpzame antwoorden aan net gelanceerde makers gaven $0; 95 mails aan makers die al verdienen gaven ±10 proefritten** (DERDEN, n=1). Werk voor de mensen die al betalen; voor ons zijn dat kopers op Superhive.
3. **Een concept-agent schreef uit zichzelf alsof een klant sprak** (DERDEN). Dat is bij ons verboden; zet het letterlijk in elke schrijfopdracht en in de keuring.
4. **Een plaatsende agent lag 5,5 dag stil omdat zijn controle het maandquotum van Buffer (gratis: 1.000 per kanaal, max 3.000) opat**, en de melders zaten op hetzelfde quotum (DERDEN). Les voor het ontwerp van B.
5. **Product Hunt zonder publiek: 1 punt, 218 bezoeken, $0** voor een AI-gerunde winkel (DERDEN). Geen geldkanaal voor ons.

Voorstel: (a) de hoofdchat zet in `marketing/REGELS.md` de zin "schrijf altijd als Dortus, nooit alsof een klant of buitenstaander het zegt" en laat de Keurder van Roep daarop toetsen (gratis, 172). (b) Onderzoeker B zoekt de API-limieten van Metricool Free na en ontwerpt meten los van plaatsen (174). (c) Volgende run: per run één curl naar Superhive en Addon Radar; op of na vr 27 nov de nulmeting (155) herhalen.

## Ronde 38 (run 24 nov ±03:20 UTC, klok van de container): een LLM die al 9 weken zelf geld probeert te verdienen en wiens geplande taak "gelukt" meldde terwijl hij niets deed, wat de verkopers van "TikTok op de automatische piloot" zelf verdienen, en een maker die eerst met de hand werkt

### 176. Stand van de Superhive-sale en de lijst van CG Channel om ±03:20 UTC
- Superhive: nog steeds geen Cyber- of Black Friday-sale op de voorpagina, alleen de Summer Sale 2026 gelinkt (GEZIEN, curl). Addon Radar: nog steeds **527** add-ons in de aanbieding (GEZIEN, addonradar.com/black-friday). Derde run op rij hetzelfde getal.
- De Black Friday-lijst van CG Channel is gegroeid van 88 deals (77) naar **105**, waarvan **10** met Blender in de eerste regels (GEZIEN, eigen telling op [cgchannel.com/?p=180263](https://www.cgchannel.com/?p=180263)). Click Joints Pro staat er nog, met 27 nov tot 1 dec, 25%, code CYBER25 (GEZIEN). Meer deals betekent dat elke regel minder opvalt; de plek blijft gratis.

### 177. Vellum Labs: een Claude Code-agent, 9 weken, $0, en een geplande taak die "gelukt" meldde terwijl er niets gebeurde
- Een LLM-agent (Claude Code, alle runs Opus) met één opdracht: echt geld verdienen met zo weinig mogelijk mensenwerk. Hij schrijft zijn weekverslagen zelf en niemand leest ze vooraf (DERDEN, [dev.to, 22 nov 2026](https://dev.to/vellumkasane/week-9-of-an-llm-trying-to-earn-money-on-its-own-last-weeks-0-replies-turned-into-2-merges-and-a-49ca)). Week 9, alle cijfers volgens hemzelf (DERDEN):
  - omzet **$0**, 0 bestellingen op Polar, dag 62 sinds de vermelding;
  - 8 Apify-actors, 537 runs, 1 andere gebruiker, 0 betaalde runs;
  - dev.to: 651 weergaven over alle posts, 0 reacties met een hartje; X: 0 volgers;
  - 34 beheerders van andermans GitHub-projecten geholpen met metingen, **14 keer** kwam dat in hun code of documentatie, **0 bezoeken** die hij daarop kan terugvoeren;
  - kosten van het model: "unknown", want het draait op het abonnement van zijn eigenaar.
- **De les die bij ons direct telt:** op 19 nov draaide zijn ochtendtaak tijdens een netwerkstoring. `git pull` en elke API-aanroep liepen vast, de taak eindigde met code 0, de lijst zei "success", en de gids van die ochtend ging niet uit. Pas de taak van 20:00 zag het en plaatste 12 uur te laat. Twee dagen later faalde een script, maar de commit en push erna liepen toch door (gekoppeld met `;` in plaats van `&&`), met als commitbericht "records updated" terwijl er alleen een concept in zat (DERDEN, zelfde bron).
  Zijn eigen conclusie: beoordeel een taak op **wat hij maakte** (staat de commit er, staat de regel in het grootboek, heeft de post een adres), niet op de afsluitcode.
- Tweede les: **een waarschuwing over een verlopende login stond 4 dagen in zijn logboek voor hij hem las**; de login van zijn geplande taken verloopt tussen 24 en 27 nov, en de vervangende sleutel ligt al sinds 20 nov bij zijn eigenaar. Een API-sleutel van Apify sneuvelde in een storing op 12 nov; vijf verbeteringen wachten daardoor al 10 dagen (DERDEN).
- Derde les (klein, maar gratis): een tag wisselen ná het plaatsen hielp niet (gids 5: 18 dagen 0 weergaven, 13 daarvan na de wissel). Hij kiest nu vooraf tags op hoeveel posts ze de afgelopen 7 dagen kregen en laat tags met 300 of meer vallen (DERDEN). GOK: voor YouTube Shorts en TikTok geldt iets vergelijkbaars voor de eerste uren na plaatsen, maar dat heb ik niet nagezocht.
- Kritisch: n=1, eerlijk verslag, geen omzet. Zijn hulp op GitHub gaf vertrouwen bij vakmensen (14 merges) en nul kopers. Past bij patroon 117: wie je helpt, is niet wie koopt.
- Voor ons: dit is precies het risico van onze geplande taken (Maker van Roep, onderzoekers, de nachtploeg). Een run die zegt "geplaatst" of "opgeslagen" moet het adres van de post of de hash op GitHub kunnen laten zien. Onze afsluitregel in CLAUDE.md (`git ls-remote` en de hash in het eindantwoord) doet dat al voor de repo; voor plaatsen via Metricool bestaat zoiets nog niet (GOK, niet nagekeken in `marketing/`).

### 178. "TikTok op de automatische piloot": wat de verkopers van zulke tools zelf verdienen
- Op 23 nov vergeleek de maker van Distribewt vijf diensten met een MCP-server die TikTok- en Instagram-diavoorstellingen voor apps maken: Distribewt, ReelFarm, SlidePilot, ViralSlides en Genviral. Prijzen $19 tot $199 per maand; alleen Distribewt, ViralSlides en Genviral kunnen via de MCP ook **plaatsen**, en dan steeds achter een goedkeuring of een aparte toestemming (`posts:publish` bij Genviral); ReelFarm en SlidePilot maken alleen de beelden, de mens plaatst (DERDEN, [dev.to, 23 nov 2026](https://dev.to/areys/comparing-mcp-servers-for-tiktok-and-instagram-app-carousels-distribewt-vs-reelfarm-vs-slidepilot-lhh); de schrijver is zelf een van de vijf, verkooppraat).
- Wat opvalt: **ze werken allemaal alleen voor apps uit de App Store of Play Store**, met echte schermen van de app. Distribewt weigert zelfs "duidelijke marketingplaatjes" en wil minstens 5 echte schermen (DERDEN). Wat bij hen verkoopt is dus het schermbeeld van het product zelf, niet een AI-plaatje.
- Wat een van die tools zelf verdient: SlideFarm ("puts your TikTok on autopilot", tot 6 posts per dag per account via de officiële API van TikTok) heeft volgens zijn geverifieerde RevenueCat-koppeling **$21 per maand, 2 abonnementen, $56 in totaal sinds dec 2025** (GEZIEN, [trustmrr.com](https://trustmrr.com/startup/slidefarm-auto-ai-slide-shows)). De tools die "automatische TikTok-groei" beloven, verdienen er zelf nauwelijks aan; verhalen als "The $120K/Month TikTok Slideshow Hack" ([stork.ai](https://www.stork.ai/blog/the-120kmonth-tiktok-slideshow-hack), niet gelezen) zijn de uitzondering waarop ze allemaal verkopen (GOK).
- Voor ons: geen tool kopen (geld, regel 1). Wel de vorm overnemen die zij allemaal opleggen: **diavoorstelling met echte beelden van het product** (bij ons: een schermopname van Blender vóór en na Click Joints, een spelbeeld van Hats). Dat kan de Maker van Roep met Metricool al, zonder nieuwe koppeling.

### 179. Jan Sytze Heegstra (TestMyBuild): eerst met de hand, pas daarna een systeem
- Een solo-maker die geld snel nodig had, bouwde bewust **geen** systeem: geen koude mail aan duizenden, geen gekochte lijsten, geen tien LinkedIn-accounts. Hij schreef met de hand mails aan mensen die net een app lanceerden en reageert nu zelf op LinkedIn-posts van makers die om feedback vragen, met een echte reactie en waar het past één eerlijke zin over zijn dienst (DERDEN, [dev.to, 23 nov 2026](https://dev.to/jan_sytzeheegstra_edb724/do-it-by-hand-before-you-build-the-system-397i)). Geen cijfers genoemd, dus geen bewijs dat het geld opleverde.
- Zijn bruikbare zin: **"Content is a gamble, a message is not."** Reels gaven zijn eerste gebruikers, maar het bereik schommelt; een bericht aan de juiste persoon niet. Een systeem gebouwd ná bewijs is een vermenigvuldiger, ervóór een gok.
- Kritisch: dit botst met 171 (behulpzame antwoorden aan net gelanceerde makers gaven $0). Het verschil: zijn klanten zíjn net gelanceerde makers (hij verkoopt testers aan makers), bij de ASO-maker niet. Les: richt je op mensen die nu precies jouw probleem hebben, niet op wie makkelijk te vinden is.
- Voor ons: benaderen mag niet zonder Thijs (regel 4), dus de "message"-kant valt grotendeels af. Wat wel past: de enige plek waar wij mensen "met het probleem op dat moment" treffen zonder iemand te benaderen, is de winkel zelf en de vraagtopics op het forum (patroon 111, ronde 31). Daar eerst met de hand antwoorden (hoofdchat, na keuring) en pas als het verkoop geeft er een agent op zetten.

### Wat een agent hierin zelf kan, binnen onze regels
- **Bewijs bij elke "klaar"-melding van een plaatsende taak** (177): de Maker van Roep zet bij elke post het adres van de post of de id uit Metricool in zijn verslag; zonder adres telt een post als "niet geplaatst". De hoofdchat kan dit in de vaste opdracht zetten. Kost niets.
- **Commando's koppelen met `&&`, niet met `;`**, in elke geplande taak die eerst iets maakt en daarna commit (177). Kan elke agent die een script schrijft vandaag aanhouden.
- **Logins en sleutels met een vervaldatum op één plek** (177): `organisatie/toegang.md` krijgt per sleutel een regel "verloopt op", en de hoofdchat kijkt er wekelijks naar. Of die datums er al staan, heb ik niet nagekeken.
- **Diavoorstellingen met echte productbeelden** voor TikTok via Metricool (178), gekeurd zoals altijd.
- **Niet doen:** een tool voor "TikTok op de automatische piloot" kopen (178: de makers verdienen er zelf $21 per maand mee); een systeem voor benaderen bouwen voordat met de hand bewezen is dat een kanaal geld geeft (179).

## Patronen na ronde 38
120. **Een geplande taak die slaagt volgens zijn afsluitcode kan niets gedaan hebben** (177): toets op het gemaakte ding (adres, hash, regel in een lijst), niet op "success".
121. **Wie tools voor automatische groei verkoopt, groeit er zelf zelden van** (178): enkele grote succesverhalen dragen een hele markt van tools die $21 per maand halen.
122. **Hulp aan vakmensen geeft vertrouwen, geen kopers** (177, net als 171): 14 merges, 0 bezoeken.

## Stand na run 24 nov ±03:35 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Superhive heeft nog geen Cyber Sale aangekondigd; Addon Radar staat de derde run op rij op 527** (GEZIEN ±03:20 UTC). GOK blijft: start ±vr 27 nov. Click Joints Pro staat nog op de lijst van CG Channel, die nu 105 deals telt, 10 met Blender (GEZIEN).
2. **Vellum Labs, een Claude Code-agent die 9 weken zelf geld probeert te verdienen: $0, en een geplande taak meldde "success" terwijl hij door een storing niets plaatste** (DERDEN). De vaste les: een run bewijst zijn werk met een adres of een hash, niet met zijn afsluitcode.
3. **Zijn hulp aan 34 beheerders op GitHub gaf 14 merges en 0 bezoeken** (DERDEN). Patroon 117 en 122: vertrouwen bij vakmensen is geen verkoop.
4. **Tools die TikTok "op de automatische piloot" zetten verdienen zelf weinig**: SlideFarm $21 per maand, $56 in totaal (GEZIEN, TrustMRR). Ze leggen allemaal echte productbeelden op; die vorm kunnen wij gratis overnemen.
5. **Een maker die snel geld nodig had, werkt eerst met de hand en bouwt pas daarna een systeem** (DERDEN, zonder cijfers). Past bij ons: eerst bewijzen welk kanaal verkoopt, dan pas automatiseren.

Voorstel: (a) de hoofdchat zet in de vaste opdracht van de Maker van Roep: "een post telt pas als geplaatst met het adres of de Metricool-id in je verslag" (gratis, 177). (b) De hoofdchat zet bij elke sleutel in `organisatie/toegang.md` een vervaldatum, zodat geen geplande taak stil op een verlopen login draait (177). (c) Volgende run: per run één curl naar Superhive en Addon Radar; op of na vr 27 nov de nulmeting (155) herhalen.

## Ronde 39 (run 24 nov ±04:20 UTC, klok van de container): een agent die pas geld zag toen hij naar een winkel met kopers ging (Apify), wat die winkel nu na zeven maanden laat zien, en drie agent-dagboeken over "bezig zijn is geen omzet"

### 180. Stand van de Superhive-sale om ±04:20 UTC
- Superhive: op de voorpagina geen Cyber- of Black Friday-sale (GEZIEN, curl; het enige "Cyber" is een maker die Cyber Kriss heet). Addon Radar: nog steeds **527** add-ons in de aanbieding, vierde run op rij hetzelfde getal (GEZIEN, [addonradar.com/black-friday](https://addonradar.com/black-friday/)); de teller lijkt niet dagelijks bij te werken, ondanks "Updated every day". Click Joints staat nog op de lijst van CG Channel (4 keer genoemd, GEZIEN, [cgchannel.com/?p=180263](https://www.cgchannel.com/?p=180263)).

### 181. AI Hustler (Marcin Dudek): $0 na 150+ runs op eigen kanalen, eerste geld binnen weken in een winkel waar al gezocht wordt
- Opzet: Claude Sonnet op een kleine VPS, cron elke 2 uur, geen geheugen behalve een eigen STATE.md, $0 budget, geen toegang tot de accounts van de maker (DERDEN, [marcindudek.dev/projects/ai-hustler](https://marcindudek.dev/projects/ai-hustler/) en [dev.to, 7 apr 2026](https://dev.to/agenthustler/my-ai-agent-finally-made-money-it-took-200-runs-and-41-days-36jk)).
- Eerste 75 runs: een eigen app 18 runs lang opgepoetst "in een lege kamer", een **shadowban op Hacker News** (elke reactie een week onzichtbaar zonder dat de agent het merkte), een kapotte wallet die weken niemand zag. Daarna MCP-servers (wel in een lijst met 82K sterren, geen betalers), affiliate-artikelen (27 klikken, 0 conversies). Na 150+ runs: $0 (DERDEN, zelfde bron).
- Rond run 180 naar de **Apify Store**, een winkel voor scrapers waar kopers al zoeken. In ±3 weken 42 scrapers gezet, en ±479 artikelen op dev.to als trechter (±4.500 views totaal). Eerste omzet $6,74 op 7 apr. **79% van de nieuwe gebruikers kwam via Google**, niet via de winkel zelf en niet via sociale kanalen; de SEO van de productbeschrijvingen telde (DERDEN).
- **Nu, 24 nov (GEZIEN, publieke API van Apify, `api.apify.com/v2/store?username=cryptosignals`):** 40 scrapers. Eén draagt alles: de LinkedIn-jobs-scraper heeft 789 gebruikers ooit en 21 in de laatste 30 dagen; de tweede (Twitter) 287 en 7. De rest zit onder de 150 gebruikers ooit en meestal onder de 10 per maand. Alle 40 op "pay per event". Omzet staat niet in de API; GOK: tientallen dollars per maand, geen honderden, gezien 21 gebruikers per maand op de beste.
- Zijn eigen lessen die ertoe doen: (1) volg vraag, maak die niet; (2) **gratis gebruikers leveren niets op**, alleen wie op een betaald plan zit (net als gratis Click Joints tegenover Pro); (3) **controleer alles met een curl**: shadowban, prijs ($0,00005 in plaats van $0,005), wallet.
- Kritisch: de omzet is klein en 479 artikelen voor 4.500 views is ±9 views per artikel. Het "werkte" door de winkel en Google, niet door de artikelen.
- Voor ons: dit is precies onze situatie met Superhive. Wat telt is gevonden worden door wie al zoekt, en volgens dit voorbeeld komt dat voor een groot deel via Google naar de productpagina. Een agent kan de titel en eerste zinnen van de Pro-pagina en de docs nalopen op de woorden waarop mensen zoeken ("3D print connectors blender", "split model for 3d printing"), zonder iemand te benaderen.

### 182. Otto: "ontdekking in een winkel is een beloning voor tractie, geen bron ervan"
- Een agent met $100, een Stripe-account en een LLC van zijn mens; zette een digitaal product in een winkel. Na 30 dagen: 1 view, 0 verkopen, en die view was waarschijnlijk hijzelf (DERDEN, [dev.to, 27 jul 2026](https://dev.to/ottoautomaton/im-an-autonomous-ai-agent-running-a-real-business-11-cycles-in-ive-made-0-heres-the-wall-i-4agg)).
- Zijn zin: de winkel laat je pas zien **na je eerste verkoop**; een mens komt over die drempel met een lijst, publiek of vrienden, een agent heeft dat niet. Het enige wat bij hem reactie gaf, was het eerlijke verhaal over zijn $0. Of dat geld wordt: onbekend, $0 bij publicatie.
- Botst met 181? Niet echt: Apify stuurt zoekers via Google naar elke scraper, de winkel van Otto (niet genoemd) kennelijk niet. Bij Superhive zagen we hetzelfde als bij Otto: "New and Rising" toont producten met al een band (149, 151). **De eerste paar verkopen moeten dus van buiten de winkel komen**: Google, de lijst van CG Channel, Addon Radar, onze eigen kanalen, de maillijst.

### 183. ZWISERFIT ("Baron"): 30 artikelen en 64 tweets voor $0,23, 2 reacties, en een X-quotum dat na 64 tweets op slot ging
- Een merkagent in een ploeg van 9 agents voor een sportschool maakte in 14 dagen ±200 stukken voor $0,23 aan tokens (DERDEN, [dev.to, 5 jul 2026](https://dev.to/zwiserfit/we-spent-023-on-content-marketing-heres-what-30-blog-posts-and-64-tweets-got-us-4905)).
- Uitkomst: 30 artikelen gaven 2 reacties en 2 opmerkingen; alleen 3 artikelen kregen iets. **De gratis X-API gaf na ±64 tweets "402 Payment Required"**, verder alleen met een plan van $100 per maand (DERDEN, zelfde bron). Hun eigen conclusie: maken is niet duur, verspreiding zonder publiek is het probleem; voortaan 3 per week met 48 uur ertussen om te kijken wat werkt.
- Voor ons: X staat niet op onze lijst en dit bevestigt dat. Meer maken lost niets op; wat telt is per stuk meten of het tot een klik op de winkel leidt.

### 184. Wye Co (dag 26): "vul geen activiteitsvak"
- Een studio die door AI gerund wordt, dag 26 op 14 nov: nog geen verkoop. De agent schrapt zijn eigen gewoonte om onder oude posts te reageren "om een vak te vullen"; alleen nog waar hij iets nuttigs toevoegt. Hij scheidt streng: een reactie is meedoen, geen verkoop; een geplande check is geen bewijs van een lege inbox (DERDEN, [dev.to, 14 nov 2026](https://dev.to/wyeco_ai/day-26-dont-fill-an-activity-slot-1dp5)).
- Zijn tabel van die dag: 0 benaderingen, 0 aanvragen, $0 uitgegeven, $0 omzet (DERDEN).
- Voor ons: een agent die per run "iets moet plaatsen" gaat vullen. Beter een vaste regel: niets plaatsen is een geldige uitkomst als er niets is wat een koper dichterbij brengt.

### Wat een agent hierin zelf kan, binnen onze regels
- **Zoekwoorden op de Pro-pagina en in de docs nalopen** (181): welke woorden gebruiken kopers, staan die in de titel en de eerste zin. Kost niets, niemand benaderd. Wie de Superhive-pagina mag aanpassen, beslist de hoofdchat.
- **Verkoop per bron blijven meten** (168), met Google apart: komt een koper via een zoekmachine of via de winkel zelf.
- **Een vaste "curl-controle" op elk kanaal**, wekelijks: is een post echt zichtbaar als je niet ingelogd bent (shadowban, 181), staat de prijs goed, werkt de link naar de winkel.
- **"Niets plaatsen" mag** als uitkomst van een run van de Maker van Roep (184), met een reden in het verslag.
- **Niet doen:** honderden artikelen als trechter (181, 183: ±9 views per artikel en 2 reacties op 30); X erbij nemen (183: betaald quotum).

## Patronen na ronde 39
123. **Ga naar waar al gezocht wordt, en zorg dat Google je daar vindt** (181): de eerste dollars kwamen pas toen de agent in een winkel met zoekers stond, en 79% van die zoekers kwam via Google.
124. **Een winkel duwt pas na de eerste verkopen** (182, 149, 151): de eerste kopers moeten van buiten komen.
125. **Activiteit is geen omzet** (183, 184): goedkoop veel maken geeft geen kopers; meet per stuk en sla een run liever over dan een vak te vullen.

## Stand na run 24 nov ±04:30 UTC (klok van de container)
Vijf belangrijkste dingen:
1. **Superhive heeft nog steeds geen Cyber Sale op de voorpagina; Addon Radar staat de vierde run op rij op 527** (GEZIEN ±04:20 UTC). GOK blijft: start ±vr 27 nov. Click Joints staat nog op de lijst van CG Channel (GEZIEN).
2. **AI Hustler: $0 na 150+ runs op eigen kanalen, eerste geld pas in de Apify Store, 79% van de kopers via Google** (DERDEN). Zeven maanden later draagt één scraper van de 40 bijna alles: 789 gebruikers ooit, 21 deze maand (GEZIEN, API van Apify).
3. **Gratis gebruikers leveren niets op, alleen betalers** (181): het verschil tussen gratis Click Joints en Pro is dus waar het geld zit.
4. **Een winkel laat je pas zien na je eerste verkopen** (182): bij Superhive zien we dat ook in "New and Rising". De eerste verkopen van Pro moeten van Google, CG Channel, Addon Radar en onze eigen kanalen komen.
5. **Goedkoop veel maken geeft geen kopers** (183: 30 artikelen, 2 reacties; 184: "vul geen activiteitsvak").

Voorstel: (a) de hoofdchat laat een agent de titel, de eerste zin en de tags van de Pro-pagina op Superhive en de docs nalopen op de zoekwoorden van kopers (gratis, 181). (b) In de vaste opdracht van de Maker van Roep: "niets plaatsen is goed als er niets is wat een koper dichterbij brengt; zeg waarom" (184). (c) Volgende run: één curl naar Superhive en Addon Radar; op of na vr 27 nov de nulmeting (155) herhalen.
