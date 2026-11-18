# A. Posten en plannen: koppelingen naar sociale kanalen (zoeker A, 18 nov 2026)

Opdracht: `BRIEF.md` hoek A. Bouwt voort op `platformen/ideeen/marketing-2026-11-18/PLAN.md` (Automatiseren 1 Weekpakket en 3 Scorebord).

## Eerst: drie dingen die ik zag en die de keuze bepalen
1. **Metricool Free is de flessenhals.** 20 posts per maand, en een post die naar YouTube en TikTok gaat telt twee keer (KEURING.md punt d, DERDEN: `metricool.com/pricing/`). Bij 2 kanalen houden we dus ±10 filmpjes per maand over (GOK, rekensom). Free kan Bluesky erbij (1 per merk, GEZIEN op de prijspagina), maar dat telt dan ook mee in de 20. Mastodon kent Metricool niet (GEZIEN, staat niet in de lijst).
2. **Het netwerk in deze agentsessie is ruimer dan BRIEF.md zegt** (GEZIEN 18 nov, curl): `api.bsky.app` (zoeken en profielen, zonder sleutel), `mastodon.social`, `mastodon.gamedev.place`, de YouTube-RSS (`youtube.com/feeds/videos.xml`), `api.buffer.com` en `api.postiz.com` gaven antwoord. `www.reddit.com` gaf een 403-pagina, `www.googleapis.com/youtube` een 403 "Permission denied" zonder sleutel (of dat de allowlist is of het ontbreken van een sleutel, weet ik niet: GOK). Andere agentsessies kunnen een ander netwerk hebben; Actions heeft open netwerk.
3. **Eigen API van TikTok, X en Reddit valt af** (zie Afgevallen). YouTube, Bluesky en Mastodon kunnen wel rechtstreeks en gratis.

## Top 5

### 1. YouTube rechtstreeks via de YouTube Data API, vanuit GitHub Actions
- **Wat:** een workflow die een goedgekeurd filmpje zelf op @Dortusapps zet als Short, met titel, beschrijving en een vaste publicatietijd (`status.publishAt`), en daarna de cijfers per filmpje ophaalt (weergaven, likes, en met de YouTube Analytics API ook `averageViewPercentage` en `engagedViews`).
- **Probleem dat het oplost:** elk filmpje op YouTube kost nu 1 van de 20 Metricool-posts; dit haalt YouTube uit die pot, zodat Metricool helemaal voor TikTok @dortusstudio overblijft. Ook de mislukte uploads op `<` en `>` (filmpje 7, besluit 18 nov 20:40) kan de workflow vóór het uploaden afvangen met een test. En het doel van Chris (vóór 1 dec één filmpje boven 1.000 weergaven) krijgt echte kijkduurcijfers, zodat we zien wát werkt.
- **Hoe het koppelt:** REST API (`POST https://www.googleapis.com/upload/youtube/v3/videos`) met OAuth (eenmalige toestemming, daarna een refresh token als GitHub-secret). Python met `google-api-python-client` of een kort curl-script.
- **Waar het draait:** GitHub Actions (start bij een tag-push of bij een wijziging in de wachtrijmap, net als de uitgave-workflows in `toegang.md`).
- **Kosten:** gratis. Uploaden kost 1 eenheid in een aparte "Video Uploads"-pot van 100 per dag (GEZIEN, `developers.google.com/youtube/v3/docs/videos/insert`, 18 nov). Belangrijk, ook GEZIEN op die pagina: "Videos uploaded from unverified API projects are not restricted to private viewing mode." Een eigen Google-project zonder keuring mag dus openbaar plaatsen.
- **Getest:** deels. De regels op de documentatiepagina gelezen (GEZIEN). Uploaden niet getest: daar is een OAuth-token voor nodig.
- **Moeite:** 4 tot 6 uur (GOK): workflow, controle op `<` en `>` en lengte, cijfers terugschrijven naar `organisatie/scorebord-data.csv`.
- **Harde regel 4 (bijgesteld 18 nov 23:17):** @Dortusapps is een Dortus-kanaal, dus een keuring door een ander is genoeg; Thijs hoeft geen ja te geven. Agents plaatsen niet zelf: de workflow plaatst alleen een filmpje met een keurbestand (skill `keuren`) erbij, en alleen de hoofdchat zet de start (tag of wachtrijbestand). Extra vangnet: uploaden als `private` met `publishAt` in de toekomst, dan staat het filmpje tot dat moment ingepland en kan Thijs het in YouTube Studio nog tegenhouden.
- **Wat Thijs doet (±15 min, GOK):** in Google Cloud (zelfde project als de nog te maken `YOUTUBE_API_KEY`) de YouTube Data API en YouTube Analytics API aanzetten, een OAuth-client maken, één keer inloggen met het @Dortusapps-account om toestemming te geven, en drie secrets zetten (`YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`). De hoofdchat kan hem in Chrome naar de juiste pagina's leiden.

### 2. Cijfers lezen zonder sleutel: YouTube-RSS, Bluesky en Mastodon in het scorebord
- **Wat:** een stap in `scorebord.yml` die elke dag de openbare cijfers ophaalt: weergaven per YouTube-filmpje uit de RSS-feed, volgers en likes/reposts per Bluesky-post, en hoe druk onze hashtags zijn op Mastodon en Bluesky.
- **Probleem dat het oplost:** PLAN.md punt 3 (Scorebord elke dag) heeft nu geen YouTube-cijfers (`scorebord.yml` en `dashboard.yml` lezen YouTube niet, GEZIEN met grep), en de `YOUTUBE_API_KEY` ontbreekt nog (`toegang.md`). Dit werkt vandaag al zonder sleutel en zonder Thijs.
- **Hoe het koppelt:** openbare HTTP: `https://www.youtube.com/feeds/videos.xml?channel_id=<kanaal-ID van @Dortusapps, staat openbaar op de kanaalpagina>` (geeft `<media:statistics views=...>` per filmpje), `https://api.bsky.app/xrpc/app.bsky.actor.getProfile` en `app.bsky.feed.searchPosts`, `https://mastodon.social/api/v1/tags/<tag>`.
- **Waar het draait:** Actions (scorebord) en ook in een agentsessie (alle drie gaven hier antwoord).
- **Kosten:** gratis, geen account.
- **Getest: ja.** GEZIEN 18 nov: de RSS van @Dortusapps gaf het Ebb-filmpje "Breathing exercise on your watch?" met 56 weergaven. Bluesky zonder sleutel: blendernation.com 8.525 volgers, blender.org 14.522, jetbrains.com 7.132; in de nieuwste 100 posts met `#gamedev` zat 1,3 uur, met `#b3d` 31,5 uur, met `#3dprinting` 22,6 uur. Mastodon.social, gebruik in 7 dagen: `#gamedev` 1.138 keer door 816 accounts, `#3dprinting` 306, `#blender` 149, `#b3d` 112. Let op: de RSS toont alleen de nieuwste openbare uploads (ik zag er één), dus voor oudere filmpjes is later toch de API nodig.
- **Moeite:** 2 tot 3 uur (GOK).
- **Harde regel 4:** niet van toepassing (alleen lezen).
- **Wat Thijs doet:** niets.

### 3. Buffer Free met de Buffer-MCP: tweede planner voor Bluesky, Mastodon en TikTok @hatsofthefallen
- **Wat:** een gratis Buffer-account als tweede wachtrij naast Metricool, met 3 kanalen. De hoofdchat zet posts klaar via de Buffer-MCP (zoals nu met Metricool), of een workflow via de Buffer-API.
- **Probleem dat het oplost:** Metricool Free heeft 1 merk; @hatsofthefallen op TikTok erbij kost Starter (E-automatiseren.md, € 16 tot 20 per maand). Buffer Free neemt die gratis, plus Bluesky en Mastodon, waar de Blender- en gamedev-mensen zitten (cijfers bij punt 2). Zo kost de wekelijkse post per product (PLAN.md: post per versie op BlenderArtists, r/Jetbrains) geen plek in de 20 van Metricool.
- **Hoe het koppelt:** MCP op afstand (`https://mcp.buffer.com/mcp`, gaf 401 zonder login, dus hij bestaat: GEZIEN) en een GraphQL-API (`https://api.buffer.com`, gaf "An authentication JWT or Access Token is required": GEZIEN).
- **Waar het draait:** MCP in de hoofdchat (als koppeling in Claude); API in Actions of een agentsessie (bereikbaar, GEZIEN).
- **Kosten:** gratis tot 3 kanalen, 10 ingeplande posts per kanaal tegelijk ("refill anytime"), 1 API-sleutel met 1.000 aanvragen per kanaal per maand (tot 3.000) (GEZIEN, `buffer.com/pricing`, 18 nov). MCP: "MCP access is included on every plan, including Free" (GEZIEN, `buffer.com/mcp`). Betaald pas bij meer kanalen: Essentials $5 per kanaal per maand (GEZIEN).
- **Getest:** deels: MCP-adres en API antwoorden, prijzen gelezen. Niet ingelogd (mag niet).
- **Moeite:** 1 uur voor de hoofdchat om het in het weekpakket op te nemen (GOK); 2 tot 3 uur als er een workflow bij moet (GOK).
- **Harde regel 4 (bijgesteld 18 nov 23:17):** past goed. Buffer zegt zelf: "Posts created through your AI assistant land in your Buffer queue as drafts or scheduled posts" (GEZIEN, `buffer.com/mcp`). Agents en de hoofdchat zetten alles als **concept**; na een keuring door een ander zet de hoofdchat het op ingepland. TikTok @hatsofthefallen valt onder de Dortus-kanalen uit de regel. Bluesky en Mastodon zijn nieuwe kanalen en staan nog niet in de regel (die noemt YouTube, TikTok en de Discord van Hats): de hoofdchat legt in de besluiten vast dat ze erbij horen, anders geldt daar de ja van Thijs.
- **Wat Thijs doet (±15 min, GOK):** Buffer-account aanmaken (inloggen met Google), een Bluesky-account en een Mastodon-account voor Dortus maken (voorstel: Mastodon op `mastodon.gamedev.place`, 35.607 gebruikers, GEZIEN via de openbare API) en die met TikTok @hatsofthefallen koppelen, de Buffer-koppeling toevoegen in Claude, en een API-sleutel als secret `BUFFER_API_KEY` zetten (mag later).

### 4. Releasepost naar Bluesky en Mastodon bij elke tag-push
- **Wat:** een stap in de bestaande uitgave-workflows (`click-joints-uitgave.yml`, `jetbrains-bison-flex-upload.yml`, later Steam) die na een geslaagde uitgave een korte post met GIF of clip plaatst op Bluesky en Mastodon.
- **Probleem dat het oplost:** PLAN.md punt 4: wat een versie oplevert is "de post erbij". Nu moet iemand die post apart klaarzetten; zo gaat hij vanzelf mee met de uitgave en is de clip uit het Uitgavepakket (PLAN.md Automatiseren 5) meteen gebruikt.
- **Hoe het koppelt:** GitHub Actions: `myConsciousness/bluesky-post` (BSD-3, 46 sterren, laatst bijgewerkt 16 aug 2026, invoer o.a. `text`, `media`, `video`, `link-preview-url`; GEZIEN in `action.yaml`) en `cbrgm/mastodon-github-action` (Apache-2.0, 39 sterren, bijgewerkt 13 nov 2026, invoer o.a. `message`, `media-paths`, `scheduled-at`; GEZIEN in `action.yml`). Of een eigen script met `@atproto/api`.
- **Waar het draait:** Actions.
- **Kosten:** gratis. Bluesky: 5.000 punten per uur, een post kost 3 punten, dus ruim 1.666 posts per uur (DERDEN, `docs.bsky.app/docs/rate-limits`). Mastodon: gratis per server.
- **Getest:** deels. `@atproto/api` geïnstalleerd met npm en gestart: profiel van blendernation.com gelezen en in een proeftekst 3 links/hashtags herkend (GEZIEN). Niet geplaatst (geen account, mag niet).
- **Moeite:** 2 uur voor de eerste workflow, daarna een kwartier per extra workflow (GOK).
- **Harde regel 4 (bijgesteld 18 nov 23:17):** de posttekst staat als bestand in de repo (`commercie/<product>/post-<versie>.md`, gemaakt met skill `update-tekst`) en wordt vóór de tag gekeurd door een ander (skill `keuren`). De workflow plaatst alleen als dat bestand een regel `gekeurd: <datum> door <naam>` heeft; anders slaat hij de stap over. Agents plaatsen niet zelf, dus de tag die de post meeneemt zet de hoofdchat (of de workflow wacht op een tweede tag `post-<versie>` van de hoofdchat). Zelfde kanttekening als bij 3: Bluesky en Mastodon eerst als Dortus-kanaal vastleggen in de besluiten. PLAN.md Keuzes 2 is hiermee beantwoord: keuring is genoeg.
- **Wat Thijs doet (±10 min, GOK):** dezelfde Bluesky- en Mastodon-accounts als bij punt 3; in Bluesky een app-wachtwoord maken en in Mastodon een toegangssleutel met alleen schrijfrecht, en die als secrets `BLUESKY_APP_PASSWORD` en `MASTODON_TOKEN` zetten. Punt 3 en 4 kunnen samen (Buffer voor de weekposts, Actions voor de releaseposts) of los.

### 5. Reserve: Zernio Free als uitweg voor TikTok als Metricool en Buffer vol zitten
- **Wat:** een plan-dienst met API en MCP, gratis voor 2 accounts met onbeperkt posts, inclusief TikTok, YouTube, Bluesky en Reddit.
- **Probleem dat het oplost:** de grens van 20 posts (Metricool) en 10 in de wachtrij per kanaal (Buffer). Als filmpjes gaan lopen en we vaker willen posten op TikTok, is dit de gratis stap vóór Metricool Starter.
- **Hoe het koppelt:** API en MCP (staat op hun site, niet zelf geprobeerd).
- **Waar het draait:** hoofdchat (MCP) of Actions (API).
- **Kosten:** 1 tot 2 accounts gratis, daarna $6 per account per maand voor 3 tot 10; "2 accounts free to start, no credit card"; "Unlimited posts" en analytics bij elk plan (GEZIEN, `zernio.com/pricing`, 18 nov).
- **Getest:** nee. Alleen de prijspagina gelezen. Jonge dienst, dus eerst kijken of het blijft werken.
- **Moeite:** 1 uur (GOK).
- **Harde regel 4:** zelfde als Buffer: als concept klaarzetten, na een keuring zet de hoofdchat op ingepland. Of Zernio een conceptstand heeft, heb ik niet gezien (GOK).
- **Wat Thijs doet:** pas als het nodig is: account maken en TikTok koppelen (±10 min, GOK).

## Advies in één zin
Begin met 2 (vandaag, zonder Thijs), dan 1 (haalt YouTube uit de Metricool-pot en geeft kijkduur), dan 3 en 4 samen als Thijs één kwartier heeft voor Buffer, Bluesky en Mastodon; 5 alleen als we tegen de grens lopen.

## Afgevallen
- **Eigen TikTok-API (Content Posting):** "All content posted by unaudited clients will be restricted to private viewing mode" (GEZIEN, `developers.tiktok.com/docs/en/content-posting-api-get-started`); een keuring voor één klein account is veel werk. Via Metricool of Buffer gaat het wel openbaar.
- **X (Twitter):** gratis laag dicht voor nieuwe projecten sinds 6 feb 2026; ongeveer $0,015 per post en $0,20 per post met een link (DERDEN, `opentweet.io/answers/is-the-x-api-free-in-2026`). Kost geld en Metricool Free sluit X ook uit.
- **Reddit-API:** zelf een sleutel maken kan niet meer, elke app moet door Reddit worden goedgekeurd, en via de API geplaatste posts worden vaker weggefilterd (DERDEN, `postpone.app/blog/changes-to-reddit-posting-in-postpone`). Reddit blijft met de hand (Thijs plakt), zoals nu in `goedkeuren.md`.
- **Postiz (gitroomhq/postiz-app, 41.905 sterren, AGPL):** Cloud kost vanaf $29 per maand, alleen 7 dagen proef (GEZIEN, `postiz.com/pricing`); zelf draaien vraagt een server die altijd aanstaat, en die hebben we niet. De CLI (`npm i postiz`, versie 2.0.29) start wel (GEZIEN, `postiz --help`).
- **Mixpost (inovector/mixpost, 3.947 sterren), trypost, postbase, postsider, posthive:** allemaal zelf te draaien op een eigen server; zelfde reden als Postiz.
- **Upload-Post:** Free is 10 uploads per maand, 2 profielen, en TikTok zit niet in Free (GEZIEN, `upload-post.com/pricing`). De MCP (`@upload-post/mcp` 0.26.5) start en meldt 120 functies (GEZIEN, met npx en een nep-sleutel), maar Buffer geeft meer voor € 0.
- **Ayrshare, Blotato, Publer:** betaald, prijzen niet nagekeken.
- **Metricool Starter (€ 16 per maand):** kost geld; eerst de gratis wegen hierboven.
- **Losse Bluesky- en Mastodon-MCP's (bijv. `@thenavidm/bluesky-mcp-cli`, `@pipeworx/mcp-mastodon`):** niet nodig; lezen gaat met curl, plaatsen hoort in een workflow met een goedkeurregel, niet in een vrije agentsessie.
- **`youtube-uploader-extra` en andere uploaders die een verstopte Chrome besturen:** tegen de regels van YouTube, en Playwright werkt bij ons niet.
- **`youtube-uploader-mcp` (anwerj, 71 sterren) en `joinhackyard/youtube-channel-mcp`:** doen hetzelfde als voorstel 1 maar als MCP; een workflow in Actions past beter bij onze goedkeuring en ons netwerk.
- **Threads, Instagram, Facebook, LinkedIn:** niet waar onze kopers zitten (GOK); Metricool Free kan Threads al als we het willen.

## Bronnen
- https://developers.google.com/youtube/v3/docs/videos/insert (quotum uploads, niet-geverifieerde projecten, publishAt)
- https://developers.google.com/youtube/analytics/metrics (engagedViews, averageViewPercentage)
- https://www.youtube.com/@Dortusapps en de RSS-feed `youtube.com/feeds/videos.xml?channel_id=...`
- https://docs.bsky.app/docs/rate-limits
- https://docs.bsky.app (api.bsky.app, searchPosts, getProfile)
- https://github.com/myConsciousness/bluesky-post
- https://github.com/cbrgm/mastodon-github-action
- https://mastodon.social/api/v1/tags/gamedev en https://mastodon.gamedev.place/api/v1/instance
- https://buffer.com/pricing
- https://buffer.com/mcp
- https://developers.buffer.com/
- https://metricool.com/pricing/
- https://zernio.com/pricing
- https://developers.tiktok.com/docs/en/content-posting-api-get-started
- https://opentweet.io/answers/is-the-x-api-free-in-2026
- https://www.postpone.app/blog/changes-to-reddit-posting-in-postpone
- https://postiz.com/pricing en https://github.com/gitroomhq/postiz-app
- https://www.upload-post.com/pricing en https://www.npmjs.com/package/@upload-post/mcp
- https://github.com/inovector/mixpost
