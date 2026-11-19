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

## Nieuw in run 2 (19 nov ±02:00): de weg naar plaatsen bestaat al, de rem is het quotum

### 1. Metricool via de koppeling is nu al onze "Plaatser", en hij werkt
- In Metricool staan 2 posts klaar voor vandaag 16:00 (filmpje 2 van Click Joints): één voor TikTok `screencuts.co`, één als YouTube Short, beide met `autoPublish: true` en status PENDING. Ze zijn op 17 en 18 nov via de koppeling aangemaakt (GEZIEN 19 nov ±01:50 met `getScheduledPosts`, alleen gelezen). De weg "Claude-sessie zet een post in Metricool en Metricool plaatst hem zelf op tijd" werkt dus al in onze omgeving.
- De koppeling kan volgens haar eigen beschrijving ook naar **Bluesky, Threads, Instagram, Facebook, Pinterest en X** plaatsen (`providers`), met `autoPublish` (zelf plaatsen) of `false` (dan krijgt Thijs een melding in de app om zelf te drukken) (GEZIEN in de toolbeschrijving van `createScheduledPost`).
- **De rem: Metricool Free geeft 20 posts per maand in de planner, telt per netwerk, en heeft geen X** ("Up to 20 posts per month in the planner", "Free does not include LinkedIn, X/Twitter": GEZIEN, [Metricool Help](https://help.metricool.com/en/article/main-differences-between-free-and-premium-plans-1udj06m/)). Eén filmpje op TikTok plus YouTube kost er 2 (GEZIEN: 2 aparte posts hierboven). Nu dus hooguit 10 filmpjes per maand.
- **Gevolg voor het ontwerp:** Metricool alleen voor TikTok (20 per maand). YouTube Shorts via de YouTube Data API zodra Thijs de OAuth regelt (eigen pot van 100 per dag, A-posten.md), Bluesky en Mastodon direct via hun API. Zo blijft het hele quotum voor TikTok, het kanaal met het algoritme dat nieuwe accounts laat zien (A-voorbeelden.md patroon 6).
- Starter kost geld (prijs niet zelf gezien; derden noemen alleen Advanced $53 per maand bij jaarbetaling: DERDEN, [Activepieces 9 nov 2026](https://www.activepieces.com/blog/metricool-pricing-2026-free-starter-advanced-plans)). Pas vragen als TikTok aantoonbaar kliks naar een winkel geeft.
- Let op: de koppeling heeft een vakje `isAigc` (TikTok) en `isAiGeneratedContent` (YouTube). Voor schermopnames van onze echte add-on is `false` eerlijk. Maken we ooit beelden of stemmen met AI, dan eisen TikTok en YouTube die melding en botst dat met het besluit "nergens een AI-melding": dan geen AI-beeld of AI-stem gebruiken (GOK op de regels van die platforms, niet nagelezen in deze run).

### 2. Geplande Claude-taken kunnen hoogstens elk uur
De beschrijving van `create_trigger` zegt "Minimum interval is normally hourly" (GEZIEN). Alles wat sneller moet (reacties ophalen elke 15 minuten) kan dus niet als Claude-sessie en hoort in GitHub Actions zonder AI, zoals het ontwerp al zei. Een sessie heeft ook geen GitHub-secrets: plaatsen met een sleutel (Bluesky, Mastodon, YouTube, Discord) doet een workflow die de sessie start (skill `actions`); plaatsen via Metricool doet de sessie zelf met de koppeling.

### 3. Lezen zonder account werkt beter dan gedacht: proef "Oor" gedraaid
Script hieronder, `node oor.mjs 60`, zonder sleutel of account. Uitslag 19 nov ±01:55 UTC (alles GEZIEN):
- **YouTube-RSS** van ons kanaal geeft titel en weergaven: Ebb-Short 75 weergaven.
- **Mastodon** per hashtag: mastodon.social `#b3d` 40 posts sinds 16 nov 14:06 (±16 per dag, rekensom), waarvan 14 met een vraagteken; `#blender` 40 sinds 16 nov 18:04; gamedev.place `#blender` 40 sinds 14 nov; fosstodon `#jetbrains` maar 40 sinds 25 okt (±1,6 per dag). Mastodon is klein voor Blender en bijna leeg voor JetBrains.
- **Bluesky Jetstream** (`wss://jetstream2.us-east.bsky.network/subscribe`, openbaar, geen login): 2.455 tot 2.616 nieuwe posts per minuut 's nachts. In 150 seconden 9 posts met onze woorden, waarvan 2 echt over Blender en 1 over gamedev, de rest ruis zoals keukenblenders. Zoeken zonder login is dicht (run 1), maar **meelezen met de hele stroom kan wel**. En Jetstream speelt terug: met `&cursor=<tijd in microseconden>` van 20 minuten geleden kwamen er in 15 seconden 52.349 posts binnen, beginnend 20,2 minuten terug (GEZIEN). Een workflow die elke 15 minuten de stroom inhaalt vanaf zijn vorige cursor, mist dus niets en is in ±15 seconden klaar. Hoe ver terug het kan, heb ik niet getest (GOK: uren, niet dagen). De radar kan zo ook zonder Dortus-account op Bluesky.
- **BlenderArtists** zoeken geeft precies het soort koper dat we zoeken: "Help Creating a Custom Articulated 3D-Printable Figure" (31 okt, 4 berichten) en een concurrent "SlicerJoint Pro" (6 aug, 4 berichten) (GEZIEN, `blenderartists.org/search.json`). Zo'n draad is een kans voor een antwoord met de hand door de hoofdchat, niet voor een agent (forumregels, run 1).

```js
// oor.mjs: leest alleen, zonder account of sleutel. node oor.mjs [seconden-bluesky]
const SEC = Number(process.argv[2] || 60);
const WOORDEN = /\b(blender|b3d|click joints|3d ?print\w*|articulated|poseable|jetbrains|intellij|bison|yacc|flex lexer)\b/i;
const uit = [];
async function json(u){ const r = await fetch(u,{headers:{'user-agent':'dortus-oor/0.1'}}); return r.ok ? r.json() : {fout:r.status}; }
const yt = await (await fetch('https://www.youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg')).text();
for (const m of yt.matchAll(/<entry>[\s\S]*?<title>([^<]*)<\/title>[\s\S]*?views="(\d+)"/g)) uit.push({bron:'youtube', titel:m[1], weergaven:+m[2]});
for (const [srv,tag] of [['mastodon.social','b3d'],['mastodon.social','blender'],['mastodon.gamedev.place','blender'],['fosstodon.org','jetbrains']]) {
  const d = await json(`https://${srv}/api/v1/timelines/tag/${tag}?limit=40`);
  if (Array.isArray(d)) uit.push({bron:`mastodon ${srv} #${tag}`, posts:d.length, oudste:d.at(-1)?.created_at, vragen:d.filter(p=>/\?/.test(p.content)).length});
}
const ba = await json('https://blenderartists.org/search.json?q=joint%20print%20order%3Alatest');
uit.push({bron:'blenderartists', treffers:(ba.topics||[]).slice(0,5).map(t=>t.title)});
const hits=[]; let n=0;
await new Promise(res=>{ const ws=new WebSocket('wss://jetstream2.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post');
  ws.onmessage=e=>{ n++; try{ const m=JSON.parse(e.data); const t=m.commit?.record?.text||''; if(WOORDEN.test(t)) hits.push({did:m.did, rkey:m.commit.rkey, tekst:t.slice(0,120)}); }catch{} };
  ws.onerror=()=>res(); setTimeout(()=>{ws.close();res();}, SEC*1000); });
uit.push({bron:'bluesky jetstream', seconden:SEC, posts_gezien:n, treffers:hits.length, voorbeelden:hits.slice(0,5)});
console.log(JSON.stringify(uit,null,1));
```
Werkt met Node 22 (ingebouwde `fetch` en `WebSocket`), dus zonder `npm install` in Actions. Wie dit bouwt, zet het als `marketing/oor.mjs` met een workflow elke 15 minuten die de uitslag naar `marketing/inbox/` schrijft.

### 4. Twee kanalen die afvallen
- **Dev.to**: plaatsen kan met één `curl` en een API-sleutel (DERDEN, [DevForge op dev.to](https://dev.to/devforgedev/how-i-run-a-3-agent-content-marketing-team-with-claude-code-49b8): 3 Claude-agents, 14 artikelen, 439 weergaven in 10 dagen, geen omzet genoemd). Maar de regels eisen bij AI-teksten een melding en verbieden dat zulke artikelen "promote any business ... (including your own)" (GEZIEN, `dev.to/guidelines-for-ai-assisted-articles-on-dev`). Botst twee keer met ons; valt af.
- **Postiz** als vervanger van Metricool: de cloud heeft geen gratis plan in de limietentabel (Standard en hoger), de API is beperkt tot 90 aanvragen per uur voor posts maar per aanvraag kunnen meer posts mee, en posts per maand zijn op betaalde plannen "effectively unlimited" (GEZIEN, `docs.postiz.com/cloud/limits.md` en `public-api/introduction.md`). Zelf hosten kan gratis maar vraagt een server die altijd aan staat, en dat is geld. Pas zinvol als Metricool Free echt knelt en Thijs liever Postiz betaalt dan Metricool Starter.

### 5. De geld-kant: welk kanaal brengt binnen weken geld
Te koop nu: **Click Joints Pro $12** (Gumroad live, Superhive in keuring, Cyber Sale ±27 nov) en **Bison & Flex $19 per jaar** (JetBrains) (GEZIEN, bord en keuring `upload-B.md`).
- Rekensom (GOK): bij 1.000 weergaven van een Short en 0,5 % die doorklikt zijn dat 5 kliks; bij 2 % kopers onder de klikkers 0,1 verkoop. Eén filmpje van 1.000 weergaven levert dus bijna niets. Geld komt pas bij filmpjes van 10.000 weergaven of meer, of bij mensen die al zoeken. Dat ondersteunt het doel van Chris (vóór 1 dec één filmpje boven 1.000, anders stoppen) en de keuze voor TikTok in Metricool.
- **Waar de kopers al zijn, op volgorde van geld (GOK, onderbouwd met het bovenstaande):**
  1. De **234 gebruikers van de gratis Click Joints** (GEZIEN, bord): een nieuwe versie met een duidelijke Pro-regel in de changelog en README bereikt hen zonder kanaal. Geen werk voor de marketingtak, wel het snelste geld.
  2. **Superhive Cyber Sale**: Pro meedoen met korting. Superhive zet sale-producten zelf in beeld (GOK, niet nagekeken in deze run).
  3. **TikTok en YouTube Shorts** met demo's uit het echte product: het enige kanaal waar een account zonder volgers toch bereik krijgt.
  4. **Forumdraden en vragen** (BlenderArtists, Mastodon `#b3d` met ±14 vragen in 2,5 dag): de radar vindt ze, de hoofdchat antwoordt met de hand.
  5. **Bluesky en Mastodon met een eigen account**: goedkoop om erbij te doen, maar wij hebben er 0 volgers en een agent heeft zelf geen publiek (A-voorbeelden.md patroon 6). Pas na TikTok.
- **Bison & Flex:** het publiek is klein en zit niet op Mastodon (fosstodon `#jetbrains` ±1,6 posts per dag, GEZIEN boven). Hier helpen de awesome-lijst en het JetBrains-forum meer dan een agent die post (GOK).

### Bijgesteld ontwerp na run 2
- **Plaatser bestaat uit twee delen:** (a) een geplande Claude-sessie "Plaatser", elk uur, die alleen groen gekeurde TikTok-posts uit `marketing/wachtrij/` met de Metricool-koppeling inplant (`autoPublish: true`) en het telt tegen het maximum van 20 per maand; (b) een workflow in Actions voor YouTube, Bluesky, Mastodon en Discord met de secrets. Regel 4 moet dan zeggen: "de Plaatser-sessie of de Plaatser-workflow plaatst wat een andere Claude groen keurde".
- **Oor zonder account vanaf dag 1:** het script hierboven, ook voordat Thijs iets regelt. Alleen reageren onder onze eigen posts vraagt de accounts.
- **Volgorde van bouwen:** eerst Oor (gratis, nu al mogelijk), dan Schrijver plus Keurder voor TikTok via Metricool (werkt nu al), dan YouTube OAuth, dan Bluesky en Mastodon.

## Nieuw in run 3 (19 nov ±03:00): wat er al misging, wat Metricool nog meer kan, en een proefronde van de Schrijver

### 1. Er ging al iets mis zonder dat iemand het zag
- In Metricool staat de YouTube-versie van filmpje 1 (17 nov 16:00) op **status ERROR: "The request metadata specifies an invalid video description."** De TikTok-versie van dezelfde post ging wel live (GEZIEN 19 nov ±02:55 met `getScheduledPosts`, alleen gelezen).
- Oorzaak (GOK, maar sterk): de tekst bevatte "Edit > Preferences > Get Extensions". YouTube staat in titel en beschrijving alle tekens toe behalve `<` en `>` (DERDEN, [ContentStudio](https://docs.contentstudio.io/article/996-youtube-errors-while-publishing)). De nieuwe YouTube-post voor vandaag (aangemaakt 18 nov 20:34) schrijft "open Edit, Preferences, Get Extensions" en staat op PENDING (GEZIEN). Iemand heeft het dus al gerepareerd, maar filmpje 1 kwam nooit op YouTube.
- **Les voor het ontwerp:** (a) de Keurder krijgt een vaste techniek-check per kanaal: YouTube geen `<` of `>`, Bluesky max 300 tekens (eis in de Metricool-toolbeschrijving, GEZIEN), TikTok titel kort; (b) de Plaatser-sessie leest elk uur de status terug en zet elke ERROR in het dagrapport en in `berichten/hoofdchat.md`. Dit is precies patroon 9 van A-voorbeelden ("meet wat naar buiten ging").

### 2. Quotum november: ±14 over
In de planner staan voor november 6 posts: 3 TikTok (2 geplaatst, 1 vandaag), 3 YouTube (1 geplaatst, 1 ERROR, 1 vandaag) (GEZIEN). Of een mislukte post meetelt voor de 20 per maand weet ik niet (GOK: ja, hij staat in de planner). Er zijn dus nog ±14 plaatsen voor 19 tot 30 nov, ruim 1 per dag. Omdat YouTube via Metricool het quotum opeet, blijft het advies: YouTube zo snel mogelijk via de eigen Data API (eigen pot), Metricool alleen TikTok.

### 3. Metricool kan TikTok-diashows plaatsen
De toolbeschrijving van `createScheduledPost` zegt bij TikTok "is a must to have at least one image or video", heeft een veld `photoCoverIndex` en zegt dat `isAigc` "is silently ignored ... when the post has no video" (GEZIEN). Een TikTok-post met alleen foto's (een diashow) kan dus via onze koppeling. Niet geprobeerd, want dat maakt een post aan.
- **Waarom dit telt voor geld:** het enige herhaalbare geldpatroon in A-voorbeelden is Larry met TikTok-diashows. Een diashow van 4 tot 6 schermafbeeldingen uit de echte add-on kan de Schrijver zelf maken (Blender headless renderen of schermafbeeldingen uit de bestaande filmpjes knippen met ffmpeg), zonder montage en zonder stem. Dat maakt 1 post per dag haalbaar zonder dat een bouwer filmpjes moet maken.
- `autoAddMusic` bestaat ook (GEZIEN in de beschrijving): TikTok zet er zelf muziek onder, wat bij diashows gebruikelijk is (GOK).

### 4. Cijfers lezen via Metricool werkt, en het eerste cijfer is slecht
Met `getAnalyticsDataByMetrics` (TikTok, connector posts) kan een sessie per video weergaven, reacties, gemiddelde kijktijd, percentage volledig bekeken en de bron (For You, zoeken, hashtag) lezen (GEZIEN, 22 velden). Uitslag nu: alleen de Ebb-video van 17 nov 13:00 staat erin: **33 weergaven, 0 reacties, gemiddeld 2 seconden gekeken, volledig bekeken bij 0,03 %** (GEZIEN). De Click Joints-video van 17 nov 16:00 staat er nog niet in (GEZIEN, ontbreekt; GOK: vertraging bij Metricool).
- **Gevolg:** kijkers haken in de eerste 2 seconden af. De Schrijver moet per post deze drie cijfers terugzien (kijktijd, volledig bekeken, For You) en de opening bijsturen, zoals Larry deed op zijn hooks (A-voorbeelden 13). Dit is het scorebord dat de tak nodig heeft, en het kan nu al zonder sleutel, via de koppeling in een geplande sessie.

### 5. Jetstream speelt ±36 uur terug
Proef 19 nov ±02:55 UTC, script hieronder (alles GEZIEN): met een cursor van 2 uur en 12 uur terug begint de stroom precies daar; met 48 of 96 uur terug begint hij op **36,25 uur terug** (daar houdt de opslag op). Eén poging op 24 uur gaf een fout en daarna wel resultaat bij de volgende vraag, dus opnieuw proberen hoort in het script. Terugspelen gaat met ±8.700 posts per seconde (71.317 posts in 8 seconden). **Gevolg:** het Oor hoeft niet elke 15 minuten; elk uur is genoeg, en mist het een dag door storing, dan haalt het alles in tot 36 uur terug. Elk uur past ook in een geplande Claude-sessie, dus het Oor kan zonder Actions starten.
```js
// js.mjs: node js.mjs <uren terug>; leest alleen
const h=Number(process.argv[2]), cur=(Date.now()-h*3600e3)*1000;
const ws=new WebSocket(`wss://jetstream2.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post&cursor=${cur}`);
let eerste=null,n=0; ws.onmessage=e=>{n++; eerste??=JSON.parse(e.data).time_us;};
setTimeout(()=>{console.log(h, eerste&&((Date.now()*1000-eerste)/3600e6).toFixed(2), n); ws.close();},8000);
```

### 6. AI-melding: geen botsing zolang beeld en geluid echt zijn
TikTok eist een label bij AI-inhoud met "realistic images, audio, or video"; YouTube hoeft geen ja bij hulp met script of thumbnail; door AI geschreven onderschriften en een AI-geholpen montage van eigen beelden hebben geen label nodig (DERDEN, [Kapwing, "last verified November 2026"](https://www.kapwing.com/resources/when-should-you-label-videos-as-ai/)). Het besluit "nergens een AI-melding" houdt dus stand als de Schrijver alleen echte schermopnames en schermafbeeldingen gebruikt. **Harde regel voor de tak: geen AI-beeld, geen AI-stem, geen AI-persoon.** Een AI-stem is op TikTok grijs gebied (zelfde bron), dus niet doen.

### 7. Proefronde: wat de Schrijver in één ronde zou maken
Op basis van wat er nu ligt (radar, BlenderArtists-draad, de cijfers hierboven). Alleen voorbeeld, niets ingepland.

```json
{"id":"2026-11-19-tiktok-vijf-gewrichten","kanaal":"tiktok","soort":"diashow",
 "tekst":"5 joints for printable action figures, and which one breaks first. Free Blender add-on: Click Joints (Get Extensions). #blender #3dprinting #articulated",
 "beelden":["shots/ball.png","shots/hinge.png","shots/peg.png","shots/swivel.png","shots/clearance.png"],
 "tijd":"2026-11-20T18:00:00+01:00","product":"click-joints","doel":"Pro op Gumroad via profiel-link",
 "bronnen":{"0.2 mm":"README Click Joints"},"keuring":null,"geplaatst":null}
```
- **Post 1 (TikTok-diashow, groen na week 1):** zoals hierboven. Opening is een lijstje met een vraag ("welke breekt eerst"), omdat de Ebb-video na 2 seconden verloor.
- **Post 2 (YouTube Short, wacht op OAuth):** dezelfde beelden als filmpje, titel zonder `<` of `>`.
- **Antwoord (rood, naar de hoofdchat):** de BlenderArtists-draad "Help Creating a Custom Articulated 3D-Printable Figure" krijgt een concept-antwoord dat eerst de vraag beantwoordt en pas aan het eind de gratis add-on noemt. Een forum is mensenwerk (run 1), dus dit gaat als concept naar `berichten/hoofdchat.md`.
- **Wat de ronde níet doet:** geen Bluesky- of Mastodon-post zolang we daar 0 volgers en geen account hebben; geen Bison & Flex-post op TikTok (publiek zit daar niet, GOK).

### Bijgesteld ontwerp na run 3
- **Agent 1 Schrijver** krijgt een vaste eerste stap: cijfers van de laatste 7 dagen lezen via Metricool (kijktijd, volledig bekeken, For You) en daaruit 1 zin "wat ik anders doe" in het dagrapport.
- **Plaatser-sessie** (elk uur) doet drie dingen: groen gekeurde TikTok-posts inplannen, status van alles in de planner teruglezen (ERROR melden), en de teller "nog over deze maand" bijhouden.
- **Oor** kan als geplande sessie elk uur draaien (Jetstream 36 uur buffer), dus Actions is pas nodig voor kanalen met een geheime sleutel.
- **Dagrapport** (1 bestand, `marketing/dagrapport.md`): gemaakt, gekeurd, ingepland, echt geplaatst, fouten, weergaven, kliks, verkopen.

## Bronnen
- [WinBuzzer: Reddit RSS en API](https://winbuzzer.com/2026/10/01/reddit-to-end-feed-reader-updates-and-public-api-access-for-apps-a002-xcxwbn/)
- [TikTok Content Posting API, get started](https://developers.tiktok.com/docs/en/content-posting-api-get-started)
- [X API pricing](https://docs.x.com/x-api/getting-started/pricing)
- [Instagram content publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing)
- [YouTube comments.insert](https://developers.google.com/youtube/v3/docs/comments/insert), [commentThreads.list](https://developers.google.com/youtube/v3/docs/commentThreads/list)
- [Bluesky rate limits (docs-repo)](https://github.com/bluesky-social/bsky-docs/blob/main/docs/advanced-guides/rate-limits.md)
- [HN guidelines](https://news.ycombinator.com/newsguidelines.html)
- [YouTube spambeleid](https://support.google.com/youtube/answer/2801973)
- [Metricool Free tegenover betaald](https://help.metricool.com/en/article/main-differences-between-free-and-premium-plans-1udj06m/), [Postiz limieten](https://docs.postiz.com/cloud/limits.md), [Postiz API](https://docs.postiz.com/public-api/introduction.md), [DEV AI-regels](https://dev.to/guidelines-for-ai-assisted-articles-on-dev), [DevForge 3 agents](https://dev.to/devforgedev/how-i-run-a-3-agent-content-marketing-team-with-claude-code-49b8), [Activepieces over Metricool-prijzen](https://www.activepieces.com/blog/metricool-pricing-2026-free-starter-advanced-plans)
- [ContentStudio: YouTube verbiedt < en >](https://docs.contentstudio.io/article/996-youtube-errors-while-publishing), [Kapwing: wanneer een AI-label](https://www.kapwing.com/resources/when-should-you-label-videos-as-ai/)
- [Buffer: content engine met GitHub Actions](https://buffer.com/resources/i-built-a-content-engine-that-creates-21-social-posts-a-week-using-the-buffer-api/), [Postiz: Accentify](https://postiz.com/blog/how-one-founder-automated-social-media-posting-with-ai-agents-notion-and-postiz-to-hit-1300-mrr)

## Stand na run 19 nov 01:05 (run 1)
1. **Zonder geld kan een agent echt zelfstandig plaatsen en reageren op YouTube, Bluesky, Mastodon en Discord;** TikTok alleen plaatsen via Metricool. Reddit en HN blijven mensenwerk.
2. **Reddit sluit voor tools** (geen nieuwe API sinds 31 okt, RSS dicht sinds 13 nov, GEZIEN 403): de vraagradar moet een plan B hebben voor maart 2027.
3. **Bluesky zoeken zonder login is sinds kort dicht** (GEZIEN 403): een Dortus-account is nodig, ook alleen voor de radar.
4. **Metricool toont TikTok `screencuts.co`, niet @dortusstudio** (GEZIEN): nagaan.
5. **Ontwerp:** Schrijver (geplande sessie, elke 4 uur) schrijft in een wachtrij, Keurder (Actions, Claude API) keurt groen/oranje/rood, een gewone workflow plaatst groen met plafond, rem en intrekknop. Kosten ±$3 tot $10 per maand uit bestaand tegoed.

**Voorstel:** de hoofdchat laat Thijs morgen punt 1, 2 en 4 van "Wat Thijs eenmalig regelt" doen (15 min) en bouwt eerst Bluesky plus Discord (snelst, gratis, geen keuring van een platform nodig), in week 1 alles op oranje. Volgende run: geld-kant scherper (welke kanalen in de eerste weken echt kliks naar Superhive, Gumroad en JetBrains geven) en een proefscript voor Bluesky en Discord dat alleen leest, klaar voor de dag dat de sleutels er zijn.

## Stand na run 19 nov 02:05 (run 2)
1. **Plaatsen zonder mens werkt al:** de 2 posts van vandaag 16:00 staan via de Metricool-koppeling met `autoPublish` klaar voor TikTok en YouTube (GEZIEN). Een geplande Claude-sessie kan dus TikTok-posts inplannen zonder sleutel; regel 4 moet alleen zeggen wie dat mag.
2. **De rem is het quotum:** Metricool Free is 20 posts per maand, per netwerk geteld, zonder X (GEZIEN). Daarom TikTok via Metricool, YouTube via de Data API, Bluesky en Mastodon direct.
3. **Lezen kan zonder enig account:** YouTube-RSS, Mastodon-hashtags, BlenderArtists en de volledige Bluesky-stroom via Jetstream, die zelfs 20 minuten terugspeelt (GEZIEN). De proef `oor.mjs` staat hierboven en draait op kale Node 22.
4. **Geld:** een Short van 1.000 weergaven levert bijna niets op (GOK, rekensom). Snelste geld zit bij de 234 gratis gebruikers, de Cyber Sale en TikTok-demo's die 10.000+ halen; Bluesky en Mastodon pas daarna. Voor Bison & Flex is Mastodon bijna leeg (±1,6 posts per dag op fosstodon `#jetbrains`, GEZIEN).
5. **Afgevallen:** Dev.to (eist AI-melding en verbiedt reclame voor eigen werk, GEZIEN) en Postiz cloud (geen gratis plan, GEZIEN).

**Voorstel:** de hoofdchat laat vandaag een bouwer `marketing/oor.mjs` plus een workflow elke 15 minuten maken (gratis, geen account nodig), en zet de Schrijver als geplande taak elke 4 uur aan voor alleen TikTok-concepten in `marketing/wachtrij/`, in week 1 alles oranje zodat de hoofdchat ze zelf in Metricool zet. Thijs hoeft daarvoor niets te regelen. Volgende run: de BlenderArtists-draad en Mastodon-vragen omzetten in een voorbeeld van wat de Schrijver per ronde zou opleveren, en nagaan hoe ver Jetstream terugspeelt.

## Stand na run 19 nov 03:10 (run 3)
1. **Filmpje 1 kwam nooit op YouTube**: status ERROR door `>` in de beschrijving (GEZIEN; oorzaak DERDEN). Niemand merkte het. De tak moet de status zelf teruglezen en melden; de Keurder krijgt een techniek-check per kanaal.
2. **Het eerste TikTok-cijfer is slecht**: Ebb 33 weergaven, gemiddeld 2 seconden gekeken (GEZIEN via Metricool). Cijfers per video zijn via de koppeling te lezen, dus de Schrijver kan op kijktijd bijsturen zonder extra sleutel.
3. **Metricool kan TikTok-diashows plaatsen** (GEZIEN in de toolbeschrijving): het Larry-patroon kan bij ons met schermafbeeldingen uit het echte product, zonder montage of stem.
4. **Quotum november ±14 posts over** (GEZIEN 6 in de planner; GOK dat de ERROR meetelt). YouTube via Metricool vreet quotum: eigen OAuth blijft punt 1 voor Thijs.
5. **Jetstream speelt ±36 uur terug** (GEZIEN): het Oor kan elk uur als geplande sessie, zonder Actions en zonder account. AI-geschreven tekst bij echte beelden vraagt geen AI-label (DERDEN), dus het besluit "geen AI-melding" blijft houdbaar als we nooit AI-beeld of AI-stem gebruiken.

**Voorstel:** de hoofdchat zet vandaag twee geplande sessies aan die geen sleutel nodig hebben: (1) **Schrijver plus Plaatser** elk uur, alleen TikTok-diashows en filmpjes uit echte schermbeelden via Metricool, ±1 per dag tot het quotum op is, met statuscontrole en dagrapport; (2) **Keurder** als aparte sessie die elk concept met het vaste formulier plus de techniek-check keurt voor de Plaatser het inplant (week 1: hoofdchat kijkt mee). Doel en stopregel: vóór 1 dec één TikTok met gemiddeld meer dan 5 seconden kijktijd en meer dan 1.000 weergaven; anders stopt TikTok voor Click Joints. Thijs hoeft hiervoor niets te doen; de YouTube-OAuth vragen we pas als TikTok die drempel haalt.
