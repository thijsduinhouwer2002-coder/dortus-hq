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
