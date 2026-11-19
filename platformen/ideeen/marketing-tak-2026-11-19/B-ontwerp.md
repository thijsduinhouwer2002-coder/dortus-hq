# B. Hoe wij het bouwen: een marketingtak die zelf plaatst en reageert (onderzoeker B, 19 nov 2026)

Opdracht: `BRIEF.md` hoek B. Bouwt voort op `marketing-2026-11-18/PLAN.md`, `koppelingen-2026-11-18/A-posten.md` en `C-community.md`, `organisatie/toegang.md` en de regel "Posten op de kanalen van Dortus" (`regels/thijs.md`, 18 nov 23:17). Wat daar al staat herhaal ik niet; ik zet er de nieuwe metingen van vannacht naast.

## Eerst: vier dingen van vannacht die het ontwerp bepalen
1. **Reddit gaat dicht voor tools.** Reddit stopte op 31 okt 2026 met nieuwe API-aanvragen, zette de RSS voor niet-ingelogden uit op 13 nov 2026 en begint op 12 jan 2027 met het afsluiten van apps die niet geregistreerd zijn; de rest van de openbare API sluit in maart 2027 (DERDEN: [WinBuzzer 1 okt 2026](https://winbuzzer.com/2026/10/01/reddit-to-end-feed-reader-updates-and-public-api-access-for-apps-a002-xcxwbn/)). Zelf gezien: `www.reddit.com/r/blender/new/.rss` en `.json` geven 403, en de MCP-server `reddit-mcp-buddy@1.3.0` (npx, zonder account) meldt bij `browse_subreddit` letterlijk dat logged-out RSS op 13 nov stopte en dat hij goedgekeurde sleutels nodig heeft (GEZIEN). Gevolg: Reddit valt af voor zelfstandig plaatsen én wordt wankel voor de vraagradar (Arctic Shift gaf om 00:50 eerst 200, daarna "Timeout. Maybe slow down a bit": GEZIEN; of het na maart blijft werken: GOK, waarschijnlijk niet).
2. **Bluesky zoeken zonder login is dicht.** `public.api.bsky.app/xrpc/app.bsky.feed.searchPosts` gaf 403 (GEZIEN 19 nov 00:50); op 18 nov werkte zoeken nog wel (A-posten.md). Profielen lezen werkt nog (`getProfile` voor blender.org: GEZIEN). Zoeken op Bluesky kan dus alleen nog met een eigen Dortus-account (app-wachtwoord).
3. **TikTok via onze eigen API kan niet openbaar plaatsen.** "All content posted by unaudited clients will be restricted to private viewing mode" (GEZIEN, `developers.tiktok.com/docs/en/content-posting-api-get-started`). Een eigen TikTok-app kan pas openbaar plaatsen na een audit. Metricool en Buffer zijn wel goedgekeurd, dus TikTok loopt via hen.
4. **Wat Metricool bij ons echt ziet.** Via de koppeling (alleen lezen, `getBrandSettings`): één merk met label `screencuts.co`, TikTok-account `screencuts.co` en YouTube-kanaal `UCTspMNCOwnBkGT2LZ7tB2dg`, tijdzone Europe/Amsterdam (GEZIEN 19 nov 00:52). De brief noemt TikTok @dortusstudio; welke van de twee nu het Dortus-kanaal is, moet de hoofdchat nagaan. De functie "post ter keuring sturen" (`createScheduledPostForReview`) vraagt volgens de koppeling zelf "a plan with team management", dus niet in Free (GEZIEN in de toolbeschrijving; dat Free het niet heeft: GOK, niet geprobeerd want het zou iets aanmaken).

## Per kanaal: wat een agent zelfstandig kan

Legenda plaatsen/reageren/lezen: **ja** = met een API die wij gratis kunnen krijgen, **via** = alleen via een planner, **nee** = niet zonder mens.

| Kanaal | Plaatsen | Reageren | Lezen (reacties, cijfers) | Hoe | Kosten | Regels en praktijk | Getest hier |
|---|---|---|---|---|---|---|---|
| **YouTube** @Dortusapps | ja (Data API, `videos.insert`) | ja (`comments.insert`, 50 eenheden per keer, GEZIEN in de docs) | ja (`commentThreads.list` 1 eenheid, GEZIEN; RSS zonder sleutel, A-posten) | OAuth-token als GitHub-secret, workflow in Actions | gratis; uploads in een eigen pot van 100 per dag (A-posten, GEZIEN 18 nov) | Spambeleid noemt "Using automated tools or AI to churn out high volumes of similar content with minimal changes" (GEZIEN, `support.google.com/youtube/answer/2801973`). Weinig en verschillend = veilig. | googleapis geeft 403 zonder sleutel (GEZIEN) |
| **TikTok** | via Metricool (Free 20 per maand, telt mee met YouTube) of Buffer | nee: de Content Posting API heeft geen reacties (GOK, niet gevonden in de docs) | via Metricool-cijfers (koppeling) | Metricool-koppeling in de hoofdchat | € 0 | Eigen app alleen privé tot audit (GEZIEN, zie boven) | 404/401 zonder token (GEZIEN) |
| **Instagram** | ja (Graph API, zakelijk account plus Meta-app), max 100 API-posts per 24 uur (GEZIEN, `developers.facebook.com/docs/instagram-platform/content-publishing`) | ja (reacties beheren via dezelfde API, GOK) | ja | Meta-app, of Buffer/Metricool | € 0 | Meta keurt de app voor openbaar gebruik; eigen account zonder keuring gaat meestal (GOK) | 400 zonder token (GEZIEN) |
| **X** | ja, betaald: $0,015 per post, $0,20 per post met link (GEZIEN, `docs.x.com/x-api/getting-started/pricing`) | ja, $0,015 per reactie (zelfde pagina) | $0,005 per gelezen post (zelfde pagina) | API-sleutel met tegoed | geld, dus ja van Thijs | Links kosten 13 keer zoveel: X wil geen links | 401 zonder token (GEZIEN) |
| **Bluesky** | ja (`@atproto/api`, app-wachtwoord) | ja (antwoord-post, notificaties lezen) | ja met login; zoeken zonder login nu 403 (GEZIEN) | secret `BSKY_HANDLE` plus `BSKY_APP_PASSWORD`, script in Actions | gratis | Limiet 5.000 punten per uur, een post kost 3: max 1.666 posts per uur (GEZIEN, `bluesky-social/bsky-docs` rate-limits.md). Ruim genoeg. | `bsky.social` antwoordt (GEZIEN); MCP `@semihberkay/bluesky-mcp@1.0.6` start met npx en heeft `create-post`, `get-timeline`, `like-post`, `repost` (GEZIEN), maar geen notificaties of zoeken |
| **Mastodon** | ja (token, `POST /api/v1/statuses`) | ja | ja, zonder login per hashtag (GEZIEN: `mastodon.gamedev.place/api/v1/timelines/tag/godot` gaf posts van vannacht) | token als secret | gratis | Elke server eigen regels; gamedev.place staat bots toe als ze gemarkeerd zijn (GOK, niet gelezen) | ja (GEZIEN) |
| **Reddit** | nee (geen nieuwe API-toegang sinds 31 okt, DERDEN boven) | nee | wankel (zie punt 1) | hoofdchat met de hand, op het account van Thijs met zijn ja | € 0 | Valt onder de naam van Thijs; blijft zo | 403 (GEZIEN) |
| **Discord** van Hats | ja (webhook staat er, `toegang.md`) | ja met een bot-token: `GET/POST /channels/{id}/messages` via REST, elke 15 minuten uit Actions, geen server die altijd aan staat (GOK dat dit binnen de limieten past; bots zijn toegestaan, alleen "self-bots" op een gewoon account niet) | ja met bot | secret `DISCORD_BOT_TOKEN` | gratis | eigen server, wij maken de regels | `discord.com/api/v10/gateway` 200 (GEZIEN) |
| **Hacker News** | **nooit** | nooit | ja (Algolia, GEZIEN 200) | alleen lezen voor de radar | € 0 | "Please don't put generated text in HN posts ... please don't automate posting" (GEZIEN, `news.ycombinator.com/newsguidelines.html`) | ja |
| **Productforums** (BlenderArtists, Discourse) | technisch ja met een gebruikerssleutel, maar de communities verwachten mensen | nee, hoofdchat met de hand | ja: `blenderartists.org/latest.json` 200 (GEZIEN) | lezen in de radar | € 0 | elke post van ons valt op; één post per versie, met de hand | lezen ja |
| **Steam** (Hats) | nee: geen API voor aankondigingen (PLAN.md) | nee | wishlist-cijfers later (`toegang.md`) | concept, Thijs plakt | € 0 | n.v.t. | n.v.t. |
| **Mail** (Kit) | ja: `POST /v4/broadcasts`; met `send_at: null` blijft het een concept, met een tijd wordt hij ingepland (GEZIEN in het voorbeeld op `developers.kit.com/api-reference/broadcasts/create-a-broadcast`) | n.v.t. | ja (abonnees, opens) | secret `KIT_API_KEY` staat er | gratis tot 10.000 | mail aan onze lijst gaat onder de naam Dortus, maar PLAN.md zegt: mail is het sterkste kanaal, dus extra keuring | `api.kit.com` 401 zonder sleutel (GEZIEN) |

**Wat dit betekent:** zonder geld kan een agent zelfstandig plaatsen én reageren op YouTube, Bluesky, Mastodon en de Discord van Hats, en plaatsen (niet reageren) op TikTok via Metricool. Reddit, Hacker News, Steam en de fora blijven mensenwerk. X kan alles maar kost per post.

## Hoe anderen het zelfstandig plaatsen technisch rond krijgen
Drie patronen die ik vond (de voorbeelden zelf zoekt hoek A):
1. **Cron in GitHub Actions plus een planner-API.** Een maker zet elke maandag 09:00 met GitHub Actions een week posts klaar uit zijn eigen databases en sjablonen (gemaakt met Claude Code) en duwt ze via de Buffer-API naar Instagram, Threads en Bluesky (DERDEN, [Buffer-blog](https://buffer.com/resources/i-built-a-content-engine-that-creates-21-social-posts-a-week-using-the-buffer-api/)). Let op: daar schrijft de AI de sjablonen, niet elke post.
2. **Agent schrijft in een database, een vaste cronjob plaatst.** Accentify: eigen agent op Claude/ChatGPT, Notion als bron, Postiz plaatst op X, Instagram, TikTok, YouTube en Facebook; 30.000 installs en $1.300 MRR (DERDEN, [Postiz-blog](https://postiz.com/blog/how-one-founder-automated-social-media-posting-with-ai-agents-notion-and-postiz-to-hit-1300-mrr)). Verkooppraat van Postiz zelf, en de maker zegt dat zijn pieken uit productupdates kwamen, niet uit marketing.
3. **Direct naar de API van het kanaal** bij Bluesky en Mastodon, met een klein script bij elke release (DERDEN, [ikristina](https://ikristina.github.io/blog/automating-social-media-posts), [woodwardweb](https://www.woodwardweb.com/post/2025/08/automated-bluesky-integration)).

Gemene deler: **de agent plaatst nooit zelf; hij schrijft in een wachtrij, en een vast stuk code plaatst wat in de wachtrij klaarstaat.** Dat past precies bij onze regel 4 en bij wat we al hebben (`opdracht.yml`, `keurder.yml`).

## Ontwerp: de tak "Roep" (2 agents plus code)

### Opbouw
```
bronnen (scorebord, radar, changelogs, reacties)
   -> Agent 1 "Schrijver" (geplande Claude-sessie, elke 4 uur)
        schrijft concepten in marketing/wachtrij/<datum>-<kanaal>-<slug>.json
   -> Agent 2 "Keurder" (Actions, Claude API, bij elke push in de wachtrij)
        keurt met vast formulier; zet status: groen / oranje / rood
   -> Workflow "Plaatser" (Actions, cron elke 15 min, geen AI)
        plaatst alles wat groen is en waarvan de tijd om is; schrijft URL terug
   -> Workflow "Oor" (Actions, cron elke 15 min, geen AI)
        haalt nieuwe reacties op (YouTube, Bluesky, Mastodon, Discord) naar marketing/inbox/
   -> Schrijver beantwoordt ze in zijn volgende ronde (of sneller: zie Reageren)
```
Twee agents is genoeg: één die maakt, één die keurt. Het plaatsen zelf is gewone code, zodat er nooit een agent op een knop drukt (regel 4 blijft letterlijk waar: geen agent plaatst; de keuring is door een ander).

### Agent 1: Schrijver
- **Draait als:** een geplande taak zoals deze sessie, elke 4 uur (6 keer per dag). Geen extra geld: dat valt onder het abonnement (GOK, net als de onderzoekers nu).
- **Leest:** `organisatie/scorebord-data.csv` (wat werkte), `organisatie/radar.md` (vragen van mensen), changelogs van de producten, `marketing/inbox/` (reacties), en wat er vandaag op Bluesky en Mastodon onder `#b3d`, `#blender`, `#gamedev`, `#3dprinting` loopt.
- **Schrijft per ronde:** hoogstens 3 nieuwe posts en alle antwoorden op reacties. Elk concept is een JSON met kanaal, tekst, beeldpad (uit het echte product), geplande tijd, product, doel (link naar winkel of Kit), en de bron van elke bewering.
- **Ideeën halen uit, op volgorde van geld:** (1) een nieuwe versie of functie van een product dat te koop is (Click Joints Pro, Bison & Flex), (2) een vraag uit de radar die ons product oplost, (3) wat in het scorebord het best liep, opnieuw in een andere vorm, (4) een trend onder de hashtags.

### Agent 2: Keurder
- **Draait als:** een workflow naar het model van `keurder.yml`, start bij elke push in `marketing/wachtrij/`. Een andere Claude dan de schrijver, dus "keuring door een ander".
- **Formulier (vast, 8 vragen):** klopt elke bewering met de bron; geen AI-zin en geen AI-melding (besluit 19 nov); geen medische claim (Ebb); geen spelerstekst Hats (die schrijft Thijs); beeld komt uit het echte product en `geluid_check.py` zegt GOED bij filmpjes; geen persoonsgegevens; past de lengte en het kanaal; is dit niet bijna gelijk aan een post van de laatste 14 dagen (tegen de YouTube-regel over "high volumes of similar content").
- **Uitkomst:**
  - **groen:** eigen kanaal, gewone post of antwoord op een gewone vraag. Plaatser zet hem eruit op de geplande tijd.
  - **oranje:** iets wat lastig terug te draaien is: mail aan de Kit-lijst, een prijs of korting, een klacht van een gebruiker, alles over Hats. Wacht 12 uur in `marketing/oranje.md`; de hoofdchat leest dat in haar ronde van 08:00 en 20:00 en zet hem op groen of rood. Geen reactie binnen 24 uur: rood.
  - **rood:** onder de naam van Thijs (Reddit, persmensen, makers, HN) of tegen een regel. Gaat nooit vanzelf; de schrijver zet een concept in `berichten/hoofdchat.md`.
- **Model:** Haiku of Sonnet via de variabele `KEURDER_MODEL`. Een post is kort, dus een keuring kost weinig (GOK: ±3.000 tokens per keuring, bij 30 per dag ±$3 tot $10 per maand uit het bestaande API-tegoed van $200; de echte prijs staat onderaan elke keuring zoals nu bij `keurder.py`).

### Reageren op reacties
- **Oor** haalt elke 15 minuten nieuwe reacties op: YouTube `commentThreads.list` (1 eenheid), Bluesky `listNotifications`, Mastodon `notifications`, Discord-kanaal via bot. Geen AI, dus gratis en snel.
- **Antwoordregels:** vraag over het product (installeren, prijs, werkt het in versie X) = groen, antwoord binnen 4 uur. Lof = een like, geen tekst (minder kans op blunders). Klacht of bug = oranje plus een melding in de loket-repo (skill `triage`). Ruzie, politiek, iets over AI = niet reageren, melden.
- **Sneller dan 4 uur kan:** de Oor-workflow mag zelf de keurder aanroepen met een antwoord dat hij uit een vaste antwoordenlijst (`marketing/antwoorden.md`, geschreven en gekeurd vooraf) kiest. Geen vrije tekst zonder schrijver.

### Ritme (GOK, bijstellen na 14 dagen meten)
| Kanaal | Posts | Reageren |
|---|---|---|
| YouTube Shorts @Dortusapps | 1 per dag (eigen pot, telt niet mee in Metricool) | binnen 4 uur |
| TikTok via Metricool | ±4 per week (20 per maand) | niet mogelijk via API; hoofdchat kijkt 2 keer per dag in de app |
| Bluesky Dortus | 1 tot 2 per dag | binnen 4 uur |
| Mastodon (gamedev.place) | 1 per dag | binnen 4 uur |
| Discord Hats | 2 tot 3 per week (devlog) | binnen 1 uur overdag |
| Kit-mail | 1 per maand, oranje | n.v.t. |

### Vangnetten tegen blunders
1. **Rem:** een bestand `marketing/STOP`. Staat het er, dan plaatst de Plaatser niets. Thijs of de hoofdchat kan het met één commit zetten.
2. **Plafond in code:** per kanaal per dag een maximum (YouTube 2, Bluesky 4, Mastodon 3, Discord 3, TikTok 1). Meer kan de Plaatser niet, ook niet als de keurder zich vergist.
3. **Terugdraaien:** elke geplaatste post krijgt zijn ID in `marketing/geplaatst.csv`; een workflow `intrekken` haalt hem weg op YouTube, Bluesky, Mastodon en Discord.
4. **Week 1 alles oranje:** eerste 7 dagen zet de keurder niets op groen; de hoofdchat ziet elke post. Daarna alleen de soorten waarbij in week 1 niets fout ging.
5. **Meten:** elke post heeft een doel-link met UTM; het scorebord telt klikken naar winkel en Kit per post. Na 14 dagen een kanaal zonder één klik naar een winkel stopt (koers Kingmaker).

## Wat Thijs eenmalig regelt (samen ±45 minuten, GOK)
1. **Bluesky-account Dortus** plus app-wachtwoord als secrets `BSKY_HANDLE`, `BSKY_APP_PASSWORD` (5 min).
2. **Mastodon-account** op gamedev.place plus token als `MASTODON_TOKEN` (5 min).
3. **YouTube OAuth** voor uploaden en reageren (`YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`, ±15 min, zie A-posten.md punt 1).
4. **Discord-bot** in de Hats-server, token als `DISCORD_BOT_TOKEN` (5 min).
5. **Zeggen welk TikTok-account** van Dortus is (`screencuts.co` of @dortusstudio) en dat in Metricool zetten (5 min).
6. **Ja op de regelwijziging:** "een workflow plaatst wat een andere Claude groen keurde" in plaats van "de hoofdchat plaatst". Dat beslist de hoofdchat morgen met Thijs.

## Kosten per maand
- Bluesky, Mastodon, YouTube, Discord, Metricool Free, Kit Free, GitHub Actions: **€ 0** (Actions is gratis voor openbare repo's, GOK dat dit zo blijft).
- Keurder via de Claude API: **±$3 tot $10** uit het tegoed dat er al is (GOK).
- Schrijver als geplande sessie: geen extra kosten (GOK).
- **Niet zonder ja van Thijs:** X (bij 2 posts per dag met link ±$12 per maand, rekensom op GEZIEN-prijs $0,20), Metricool Starter voor meer TikTok-posts, Buffer betaald.

## Bronnen
- [WinBuzzer: Reddit RSS en API](https://winbuzzer.com/2026/10/01/reddit-to-end-feed-reader-updates-and-public-api-access-for-apps-a002-xcxwbn/)
- [TikTok Content Posting API, get started](https://developers.tiktok.com/docs/en/content-posting-api-get-started)
- [X API pricing](https://docs.x.com/x-api/getting-started/pricing)
- [Instagram content publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing)
- [YouTube comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert), [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list)
- [Bluesky rate limits (docs-repo)](https://github.com/bluesky-social/bsky-docs/blob/main/docs/advanced-guides/rate-limits.md)
- [HN guidelines](https://news.ycombinator.com/newsguidelines.html)
- [YouTube spambeleid](https://support.google.com/youtube/answer/2801973)
- [Buffer: content engine met GitHub Actions](https://buffer.com/resources/i-built-a-content-engine-that-creates-21-social-posts-a-week-using-the-buffer-api/), [Postiz: Accentify](https://postiz.com/blog/how-one-founder-automated-social-media-posting-with-ai-agents-notion-and-postiz-to-hit-1300-mrr)

## Stand na run 19 nov 01:05 (run 1)
1. **Zonder geld kan een agent echt zelfstandig plaatsen en reageren op YouTube, Bluesky, Mastodon en Discord;** TikTok alleen plaatsen via Metricool. Reddit en HN blijven mensenwerk.
2. **Reddit sluit voor tools** (geen nieuwe API sinds 31 okt, RSS dicht sinds 13 nov, GEZIEN 403): de vraagradar moet een plan B hebben voor maart 2027.
3. **Bluesky zoeken zonder login is sinds kort dicht** (GEZIEN 403): een Dortus-account is nodig, ook alleen voor de radar.
4. **Metricool toont TikTok `screencuts.co`, niet @dortusstudio** (GEZIEN): nagaan.
5. **Ontwerp:** Schrijver (geplande sessie, elke 4 uur) schrijft in een wachtrij, Keurder (Actions, Claude API) keurt groen/oranje/rood, een gewone workflow plaatst groen met plafond, rem en intrekknop. Kosten ±$3 tot $10 per maand uit bestaand tegoed.

**Voorstel:** de hoofdchat laat Thijs morgen punt 1, 2 en 4 van "Wat Thijs eenmalig regelt" doen (15 min) en bouwt eerst Bluesky plus Discord (snelst, gratis, geen keuring van een platform nodig), in week 1 alles op oranje. Volgende run: geld-kant scherper (welke kanalen in de eerste weken echt kliks naar Superhive, Gumroad en JetBrains geven) en een proefscript voor Bluesky en Discord dat alleen leest, klaar voor de dag dat de sleutels er zijn.
