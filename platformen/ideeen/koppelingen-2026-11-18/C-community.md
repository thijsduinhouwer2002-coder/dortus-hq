# C: community en mond-tot-mond (zoeker C, 18 nov 2026, ±23:20 tot 23:55)

Bouwt voort op `platformen/ideeen/marketing-2026-11-18/PLAN.md` (punt 4 "vermeldingen volgen", punt 6 "Kit met formulier") en op J (`J-publiek-doorverwijzen.md`, Kit en Discord). Wat daar al staat, herhaal ik niet; ik zeg alleen wat er nieuw bij komt en wat ik vanavond zelf getest heb.

**Stand vanavond (GEZIEN, curl 18 nov ±23:30):** op geen enkele productpagina van dortus.com staat een aanmeldformulier; `dortus.com/hats/` geeft 404; de beveiligingsregel van de site staat nog op `form-action 'self'` (dus een Kit-formulier wordt tegengehouden). Click Joints: 234 downloads en **0 reviews** op extensions.blender.org. Bison & Flex: 6 downloads, **0 reviews** (JetBrains-API). Er draait nog geen workflow die vermeldingen of vragen zoekt (geen yml gevonden met Alerts, RSS of Reddit).

## Top 5

### 1. Vraagradar: elke paar uur zoeken naar mensen die vragen om wat wij maken
- **Wat:** een klein Python-script in een GitHub Actions-workflow dat op vaste tijden nieuwe posts en reacties leest en filtert op onze woorden (productnamen, maar vooral vragen: "ball joint" plus "print", "articulated figure", "bison" of "yacc" plus "clion", "desktop pet"). Nieuwe treffers (met link, datum, bron) gaan naar `organisatie/radar.md` en één regel in `berichten/hoofdchat.md`. Een agent zet bij de beste treffers een conceptantwoord in de weekwachtrij (`organisatie/goedkeuren.md`).
- **Probleem dat het oplost:** de eerste gebruikers komen van plekken waar al mensen zitten (PLAN, punt 1), en een antwoord op een echte vraag is het enige soort post dat op Reddit en forums niet als reclame voelt. Nu zien we zulke vragen alleen als iemand toevallig kijkt. Raakt Click Joints (r/3Dprinting, r/customactionfigures, r/blender, BlenderArtists, Blender Stack Exchange), Bison & Flex (r/Compilers, r/Jetbrains, Stack Overflow, Hacker News, JetBrains-forum) en Hats (desktop pet, desktop companion). Ook onze eigen namen, zodat PLAN punt 4 (RSS en Google Alerts) in dezelfde workflow kan.
- **Hoe het koppelt (alles zonder sleutel, getest):**
  - Reddit: niet direct (reddit.com geeft 403 "blocked due to a network policy", ook de RSS; GEZIEN). Wel via het openbare archief **Arctic Shift**: per subreddit alle nieuwe posts (`/api/posts/search?subreddit=..&after=..&limit=100&sort=asc`) en reacties (`/api/comments/search`), filteren doen we zelf. Werkt vanuit de sessie (GEZIEN: r/blender had posts van 4 minuten oud). Zoeken op tekst bij Arctic Shift geeft vaak "Timeout. Maybe slow down a bit"; daarom alles ophalen en zelf filteren, met 3 seconden tussen verzoeken.
  - Hacker News: Algolia-API `search_by_date` met `numericFilters=created_at_i>..`, `typoTolerance=false` en `advancedSyntax=true` (zonder die twee gaf "yacc" 22.629 treffers in 30 dagen, met 7; GEZIEN).
  - Discourse-fora: `search.json?q=<woord> after:<datum> order:latest` op blenderartists.org, platform.jetbrains.com, forum.obsidian.md, devtalk.blender.org (alle vier 200, GEZIEN).
  - Stack Exchange-API (Stack Overflow, blender.stackexchange): werkt zonder sleutel, quotum 300 per dag (GEZIEN: na 3 verzoeken nog 257).
  - GitHub issues zoeken (`api.github.com/search/issues`, 200 GEZIEN) en Mastodon-hashtags (`/api/v1/timelines/tag/b3d`, 200 GEZIEN).
- **Proef vanavond (30 dagen terug, GEZIEN):** r/customactionfigures 1.044 posts gelezen, 49 met onze woorden (o.a. "Looking for articulated hand", "Can I paint an articulated action figure body"); r/3Dprinting 600 posts gelezen (afgebroken door de snelheidsgrens), 12 treffers (o.a. "Gap/Print in place issues", "Fully Articulated 3D printed Custom Action Figure"); r/Compilers 221 posts, 2 treffers (o.a. "a lexer generator", 16 nov); r/Jetbrains 157 posts, 0 treffers. HN: 7 keer "yacc" in 30 dagen, waaronder vandaag het verhaal "Write text parsers with yacc and lex" (1 punt, 0 reacties, dus geen kans). BlenderArtists: 9 topics met "print in place" in 30 dagen. Stack Overflow: in een heel jaar maar 1 vraag met tag `bison`, 2 met `flex-lexer` (GEZIEN); Stack Overflow is voor Bison & Flex dus geen bron meer. Blender Stack Exchange: 25 vragen met tag `3d-printing` in een jaar (GEZIEN).
- **Eerlijk:** veel ruis. Van de 49 treffers is maar een klein deel een echte vraag waar Click Joints het antwoord is (GOK: 1 op 10). Daarom filtert het script op vraagwoorden ("how", "looking for", "any addon", "?") en kijkt een agent of mens voor er iets gebeurt.
- **Waar het draait:** GitHub Actions (cron, bijvoorbeeld 07:00 en 19:00). Alle bronnen werkten ook vanuit de sessie, dus testen kan in de sessie. Of Arctic Shift GitHub-adressen even goed toelaat: niet getest (GOK: ja, het is een openbare dienst zonder sleutel).
- **Regel 4:** de radar plaatst niets. Antwoorden op Reddit en forums gaan onder de accounts van Thijs, dus als concept in het weekpakket met zijn ja; Thijs plaatst met de hand. Een treffer over Hats die in de eigen Discord past, mag na een keuring door de hoofdchat geplaatst worden (regel 4 sinds 18 nov 23:17).
- **Kosten:** € 0 (Actions-minuten in een openbare repo zijn gratis; alle API's gratis).
- **Getest:** ja, alle bronnen met curl en een proefscript van 50 regels (staat niet in de repo, alleen in /tmp).
- **Moeite:** 3 tot 4 uur (GOK), het meeste werk is het woordenfilter. Kan voortbouwen op `platformen/verkenner/data/reacties-script.py` (zelfde curl-aanpak voor Discourse en HN). Logisch bij Chris (PLAN punt 4 staat al bij hem).
- **Wat Thijs doet:** niets om het te bouwen. Daarna: de goedgekeurde antwoorden plaatsen (±2 minuten per stuk, alleen als er echt een passende vraag is).
- **Waarom niet F5Bot of Syften:** zie Afgevallen.

### 2. De gratis mails van JetBrains laten werken voor Bison & Flex
- **Wat:** JetBrains stuurt elke proefgebruiker van een betaalde plugin vanzelf drie mails: een welkomstmail met links naar de pluginpagina, documentatie, bugtracker en contact van de maker; een herinnering als de proef bijna afloopt; en een maand na aankoop een mail met de vraag om de plugin te beoordelen (DERDEN, [JetBrains-blog](https://blog.jetbrains.com/?p=276197/)). De links komen uit de velden van onze pluginpagina.
- **Probleem:** Bison & Flex heeft 0 reviews en de welkomstmail is nu half leeg: in de JetBrains-API staan `bugtrackerUrl`, `forumUrl` en `sourceCodeUrl` leeg; alleen `docUrl` wijst naar `https://dortus.com/bison-flex/` (GEZIEN, `plugins.jetbrains.com/api/plugins/35901`). Elke proefgebruiker komt dus via die mail op onze pagina terecht, en daar staat nu geen aanmeldvak en geen reviewvraag.
- **Hoe het koppelt:** (a) velden invullen in het Marketplace-dashboard: bugtracker naar de meldingenrepo `bison-flex` (die bestaat sinds 18 nov), forum naar GitHub Discussions van die repo (zet de hoofdchat met één vinkje aan); (b) op `dortus.com/bison-flex/` een vak "One email per new version" (Kit, tag `jetbrains`, zie voorstel 3) en een regel "Like it? A rating on JetBrains Marketplace helps other C developers find it"; (c) reviews volgen via de open API `plugins.jetbrains.com/api/plugins/35901/comments` (werkt zonder sleutel, gaf `[]`, GEZIEN) in de radar van voorstel 1, zodat elke review binnen een dag een antwoordconcept krijgt (skill `triage`; JetBrains raadt aan op 1 tot 3 sterren te antwoorden, DERDEN, [reviewbeleid](https://plugins.jetbrains.com/docs/marketplace/reviews-policy.html)).
- **Waar het draait:** dashboard: hoofdchat in Chrome. Pagina: repo `dortus`. Reviews lezen: Actions (werkt ook in de sessie).
- **Regel 4:** de reviewvraag op de pagina en antwoorden op reviews staan onder de naam Dortus, niet onder die van Thijs. Volgens regel 4 (18 nov 23:17) mogen posts op Dortus-kanalen na een keuring; of een winkelantwoord als Dortus-kanaal telt staat er niet letterlijk (GOK: ja). Tot de hoofdchat dat beslist: keuring plus ja van Thijs.
- **Kosten:** € 0.
- **Getest:** API's ja (pluginvelden en reviews gelezen). De mails zelf niet gezien (we zijn geen proefgebruiker).
- **Moeite:** 1 uur (GOK).
- **Wat Thijs doet:** ja op de twee zinnen; verder niets.

### 3. Eén Kit-aanmelding die drie trechters opvangt, plus dagelijks tellen
- **Wat:** wat J al voorstelde (Kit, tags per product), maar nu concreet: (a) in de repo `dortus` de beveiligingsregel aanpassen naar `form-action 'self' https://app.kit.com https://app.convertkit.com` (voorbeelden posten naar `app.convertkit.com/forms/<id>/subscriptions`, DERDEN, [gist](https://gist.github.com/panphora/168cc4beb03f6b5b2d4f4aa2ba3b32ce); welk domein Kit nu gebruikt kon ik niet lezen, kit.com geeft 403, dus beide toestaan, GOK), of zonder siteaanpassing linken naar een gratis Kit-landingspagina; (b) een gewoon HTML-formulier zonder script op `dortus.com/click-joints/`, `/bison-flex/` en een nieuwe `/hats/`; (c) een stap in `scorebord.yml` die elke dag het aantal abonnees per tag uit de Kit-API haalt (secret `KIT_API_KEY` staat er al) en het aantal Discordleden via `discord.com/api/v9/invites/<code>?with_counts=true`.
- **Probleem:** drie stromen komen nu op pagina's zonder aanmeldvak uit: de Website-knop van Click Joints Free in Blender (234 downloads), de welkomstmail van JetBrains (voorstel 2), en straks de Hats-pagina en Hat Tower. Mail is 10 keer sterker dan social (PLAN punt 2). Zonder teller zien we ook niet of het werkt.
- **Hoe het koppelt:** HTML-formulier naar Kit; Kit-API v4 vanuit Actions. `api.kit.com/v4/account` geeft zonder sleutel 401, dus de API is bereikbaar (GEZIEN). De Discord-invite-API werkt zonder sleutel (GEZIEN vanavond op twee openbare servers: 6.183 en 9.883 leden). De invitecode van de Hats-server staat niet in de repo; die moet erbij.
- **Waar het draait:** formulieren: dortus.com (GitHub Pages). Tellen: Actions.
- **Regel 4:** aanmelden zelf is geen post. Elke mail aan de lijst maakt een workflow als concept (`send_at: null`, zie J); Thijs drukt op verzenden. De belofte op het formulier (bijv. "One email when the free demo is playable") eerst langs Thijs.
- **Kosten:** € 0 tot 10.000 abonnees (DERDEN, J).
- **Getest:** gedeeltelijk: CSP, 404 op /hats/, Kit-API bereikbaar, Discord-teller. Het formulier niet (geen Kit-formulier-ID; account is van Thijs).
- **Moeite:** 1,5 uur (GOK) inclusief de teller.
- **Wat Thijs doet:** de bevestigingsmail van Kit aanklikken (staat al in `toegang.md`); in Kit één formulier maken en het formulier-ID geven (±3 minuten, of de hoofdchat via Chrome); ja op de beloftezin; postadres pas bij de eerste mail (J 0.3).

### 4. Verwijzers die alleen bij verkoop iets krijgen: Superhive en Gumroad
- **Wat:** beide winkels van Click Joints Pro hebben een eigen verwijzingsprogramma. **Superhive:** de maker kiest per verwijzer (site of YouTube-kanaal) een percentage; hun "premium affiliate" is BlenderNation, met volgens Superhive meer dan 300.000 bezoekers per maand en advertentieplek naar rato van het percentage, "start as low as 5-10%" (DERDEN, [Superhive](https://superhivemarket.com/posts/sell-more-blender-products-with-blender-nation-as-your-affiliate), ouder bericht); verwijzers moeten een Superhive-account hebben (DERDEN, [hulp](https://support.blendermarket.com/article/157-how-to-add-new-affiliates-to-products)). **Gumroad:** eigen verwijzers met een eigen percentage en 30 dagen cookie, aanmelden kan via een formulier zonder dat wij iemand benaderen; daarnaast "Gumroad Affiliates" waar iedereen 10% krijgt, uit te zetten (DERDEN, [Gumroad](https://gumroad.com/help/article/333-affiliates-on-gumroad)).
- **Probleem:** Click Joints Pro heeft makers nodig die het laten zien (PLAN: tweede golf via een middelgrote maker), maar wij betalen niemand vooraf. Een verwijzerslink geeft een maker een reden zonder dat wij geld uitgeven. BlenderNation staat in `geplaatst.md` al op "wacht"; een verwijzerspercentage kan daar een extra reden zijn.
- **Hoe het koppelt:** instellingen in het Superhive- en Gumroad-dashboard (hoofdchat in Chrome). Meten: verkopen met verwijzer lezen via de Gumroad-API in Actions (secret `GUMROAD_ACCESS_TOKEN` staat er; of het verwijzerveld in de API zit: GOK). Een regel "Make Blender videos? Earn X% per sale" op `dortus.com/click-joints/` met de aanmeldlink van Gumroad. Makers die de radar (voorstel 1) vindt, krijgen die link pas als Thijs het bericht goedkeurt.
- **Waar het draait:** winkeldashboards; meten in Actions.
- **Regel 4 en regel 1:** geen uitgave vooraf, alleen een deel van een verkoop. Toch gaat het over geld en een afspraak onder de naam Dortus: **Thijs kiest het percentage** en zegt ja op de zin op de site. Niemand benaderen zonder zijn ja op de tekst.
- **Kosten:** € 0 vooraf; per verkoop via een verwijzer het gekozen percentage.
- **Getest:** nee (dashboards achter inlog). Alleen de hulppagina's gelezen.
- **Moeite:** 30 minuten in Chrome (GOK), zodra Superhive de keuring rond heeft.
- **Wat Thijs doet:** een percentage kiezen (voorstel: 20 tot 30% op Gumroad, GOK), en zeggen of Gumroad Affiliates (10% voor iedereen) aan mag blijven.

### 5. Reviewvangnet: reviews vragen op het goede moment en elke review zien
- **Wat:** één lijst met alle reviewplekken die de radar elke dag leest, plus een vaste, korte vraag om een review op de plekken waar dat mag. Lezen: JetBrains (API, voorstel 2), extensions.blender.org (`/add-ons/click-joints/reviews/` geeft 200 en "0 reviews", GEZIEN; HTML lezen), Gumroad (beoordelingen staan in de productpagina, GOK op de precieze plek), Steam `appreviews` vanaf de paginadag (vanuit de sessie gaf dat een 302, GEZIEN; in Actions niet getest). Nieuwe review: regel in `berichten/hoofdchat.md` en een antwoordconcept via skill `triage`.
- **Vragen, alleen waar het mag:**
  - Click Joints Free: niet in Blender zelf (regels 6.1 en 6.3 van extensions.blender.org, zie J; een reviewknop in de add-on kan als promotie gelden, GOK, dus niet doen). Wel in de README van de meldingenrepo `click-joints`, op `dortus.com/click-joints/` en onderaan elke versiepost op BlenderArtists: "If it worked for your print, a rating on extensions.blender.org helps others find it."
  - Click Joints Pro: in de downloadtekst van Gumroad (geen Blender-regels). De winnaars met veel beoordelingen staan juist op Gumroad: Blosm 1.618, CAD Sketcher 1.349 (GEZIEN in A-blender).
  - Bison & Flex: de automatische mail van JetBrains (voorstel 2) plus de pagina.
  - Hats: Steam verbiedt beloningen voor reviews (besluit); alleen een gewone vraag na de demo, later.
- **Probleem:** 0 reviews op 234 downloads (Click Joints) en 6 downloads (Bison & Flex). In de winkel is het aantal sterren het eerste wat een nieuwe bezoeker ziet; ons eigen bewijs is nu leeg.
- **Waar het draait:** lezen in Actions (zelfde workflow als voorstel 1). Teksten op site, README en winkelpagina's.
- **Regel 4:** de vaste reviewzin één keer keuren (en langs Thijs zolang niet beslist is of winkelpagina's Dortus-kanalen zijn, zie voorstel 2); antwoorden op reviews per stuk in het weekpakket.
- **Kosten:** € 0.
- **Getest:** JetBrains en Blender ja; Gumroad en Steam nee.
- **Moeite:** 1 uur bovenop voorstel 1 (GOK).
- **Wat Thijs doet:** ja op de vaste zin.

## Afgevallen
- **F5Bot** (Reddit, HN, Lobsters per mail): gratis plan is 5 woorden, alleen mail, tot 2 uur vertraging, en "personal use only"; RSS, JSON en Discord pas vanaf Gold $49,99 per maand (GEZIEN, f5bot.com/tiers). Mail komt bij Thijs binnen, en Gmail mogen agents niet lezen (regel 7). Onze eigen radar doet hetzelfde gratis.
- **Syften** (veel bronnen, ook Bluesky en Discourse): vanaf $29,95 per maand, MCP pas bij PRO $119,95 (GEZIEN, syften.com). Geld; niet nodig zolang de eigen radar werkt.
- **Officiële Reddit-API** (OAuth-app): vraagt een app bij Reddit en account van Thijs, en Reddit laat zakelijk gebruik alleen met toestemming toe (GOK, niet nagelezen). Arctic Shift volstaat. Risico: Arctic Shift is een vrijwilligersdienst; valt hij weg, dan valt Reddit uit de radar (de rest blijft werken).
- **PullPush** (ander Reddit-archief): gaf "error code: 521" (server plat, GEZIEN).
- **Bluesky zoeken:** `public.api.bsky.app` gaf 403, `bsky.social` 401 vanuit de sessie (GEZIEN). Hoort bij hoek A; in Actions misschien wel bereikbaar (GOK).
- **Lobsters:** zoeken werkt (200), maar onze woorden komen er bijna niet voor (GOK); reactiezoeken gaf 404. Later toevoegen als het vrijwel gratis is.
- **Open-source Reddit-monitors op GitHub** (redsignal 31 sterren, Reddit-Scraper-with-Push-Notifications 28, GEZIEN via de zoek-API): draaien op PRAW met een Reddit-app of als eigen server met webinterface. Te zwaar; ons script is 50 regels.
- **TrendWatch** (Actions-sjabloon voor trendalarmen): vraagt een sleutel bij een derde (100 verzoeken per maand gratis, DERDEN, README) en meet zoektrends, geen gesprekken.
- **Eigen Discord-bot voor de Hats-server:** een bot die antwoordt moet altijd aan staan (of via een Interactions-adres op bijvoorbeeld Cloudflare Workers draaien) en vraagt een Discord-app van Thijs. Voor een server zonder spelers levert dat nu niets; J zegt al: Discord pas openen als er iets te spelen is. Wat wel kan zonder bot: de webhook (staat er) voor aankondigingen, die volgens regel 4 (18 nov 23:17) na een keuring zonder ja van Thijs mogen, en de ledenteller (voorstel 3). Opnieuw bekijken na de demo.
- **Discord Server Discovery en Disboard:** Discovery vraagt een minimum aan leden en weken activiteit (DERDEN, [peakbot](https://peakbot.pro/blog/how-to-get-server-on-discord-server-discovery)); Disboard werkt met handmatig "bumpen" elke paar uur. Niet nu.
- **Google Alerts opnieuw voorstellen:** staat er al (secret `GOOGLE_ALERTS_FEEDS`); hoort als extra bron in de radar van voorstel 1.
- **Stack Overflow voor Bison & Flex:** 1 vraag met tag `bison` in een jaar (GEZIEN). Wel meenemen in de radar (kost niets), maar geen eigen werk aan.
- **Show HN als moment:** verboden voor gegenereerde tekst (PLAN). HN blijft alleen een bron om te lezen.
- **Een aanmeldveld in de IDE of in Blender:** JetBrains vraagt dan toestemming en privacybeleid, Blender verbiedt promotie (J). De pagina's van voorstel 3 vangen dezelfde mensen.

## Bronnen
- F5Bot prijzen: https://f5bot.com/tiers
- Syften: https://syften.com/
- Arctic Shift (Reddit-archief): https://arctic-shift.photon-reddit.com/api/posts/search
- HN Algolia-API: https://hn.algolia.com/api/v1/search_by_date
- Stack Exchange-API: https://api.stackexchange.com/2.3/questions
- JetBrains automatische mails aan proefgebruikers: https://blog.jetbrains.com/?p=276197/
- JetBrains reviewbeleid: https://plugins.jetbrains.com/docs/marketplace/reviews-policy.html
- JetBrains plugin-API Bison & Flex: https://plugins.jetbrains.com/api/plugins/35901 en `/comments`
- Blender reviews Click Joints: https://extensions.blender.org/add-ons/click-joints/reviews/
- Kit-formulier voorbeeld: https://gist.github.com/panphora/168cc4beb03f6b5b2d4f4aa2ba3b32ce
- Discord invite-teller: https://discord.com/api/v9/invites/<code>?with_counts=true
- Gumroad verwijzers: https://gumroad.com/help/article/333-affiliates-on-gumroad
- Superhive verwijzers: https://superhivemarket.com/posts/sell-more-blender-products-with-blender-nation-as-your-affiliate en https://support.blendermarket.com/article/157-how-to-add-new-affiliates-to-products
- Discord Discovery: https://peakbot.pro/blog/how-to-get-server-on-discord-server-discovery
- GitHub-zoeken naar monitors: https://api.github.com/search/repositories?q=reddit+keyword+monitor
