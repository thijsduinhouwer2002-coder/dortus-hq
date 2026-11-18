# B: gevonden worden in winkels en zoekmachines (zoeker B, 18 nov 2026)

Hoek B uit `BRIEF.md`. Gebouwd op `platformen/ideeen/marketing-2026-11-18/PLAN.md`; wat daar al staat (sitemap per map, IndexNow als idee, Steam-verlanglijst-API, scorebord, awesome-lijsten) noem ik alleen als ik iets nieuws heb getest of rechtzet. Alle webpagina's met `curl` gelezen. Niets aangemaakt, niets ingediend, geen enkele URL bij een zoekmachine aangemeld.

**Belangrijk over de omgeving (GEZIEN, 18 nov ±23:30):** vanuit deze agentsessie gaven 200 of een nette 401/403 terug: api.github.com, extensions.blender.org, plugins.jetbrains.com, store.steampowered.com, api.steampowered.com, partner.steam-api.com, steamspy.com, bing.com/indexnow, api.twitch.tv, dortus.com, raw.githubusercontent.com. Geweigerd met 403: producthunt.com en steamdb.info. Het netwerk is dus ruimer dan BRIEF.md denkt; toch zet ik alles met een sleutel in Actions, want secrets staan alleen daar.

## Top 5

### 1. JetBrains-statistieken per dag met de sleutel die we al hebben (Bison & Flex)
- **Wat:** JetBrains Marketplace heeft naast de upload een niet-openbare statistiek-API: downloads per dag, per maand, per IDE (productcode), per land en per versie (`/statistic/downloads-count/...`, `/statistic/downloads-unique/...`), plus `sales-info` en `trials-info` voor betaalde plugins. Het open project `jansorg/marketplace-stats-kotlin` (versie 0.56.0, laatste commit 6 nov 2026, GEZIEN) gebruikt precies die adressen en heeft er zelfs een eigen MCP-server bij.
- **Probleem dat het oplost:** het scorebord ziet nu alleen het totaal (6 downloads, GEZIEN API `/api/plugins/35901`). We kunnen dus niet zien of het forumbericht, de awesome-lijst of een tutorial iets deed, en niet in welke IDE (CLion of niet) en welk land. Bovendien loopt er een proef van 30 dagen: `trials-info` laat zien hoeveel proeven er lopen en hoeveel er omzetten. JetBrains zegt zelf dat er geen API is voor ruwe downloads (DERDEN, [forum JetBrains, okt 2025](https://platform.jetbrains.com/t/plugin-download-statistics-in-a-machine-readable-form/2942)); deze statistiek-adressen zijn wat hun eigen grafieken gebruiken (GOK op hoe lang ze zo blijven, want niet gedocumenteerd).
- **Hoe het koppelt:** REST met `Authorization: Bearer <token>`, een klein Python-script in `scorebord.py` (alleen aantallen per dag, per IDE en per land wegschrijven; nooit klantnamen uit `sales-info`).
- **Waar het draait:** GitHub Actions, in de bestaande workflow Scorebord.
- **Kosten:** gratis.
- **Getest:** deels. `https://plugins.jetbrains.com/statistic/downloads-count/plugin?plugin=35901` zonder sleutel geeft 403 "you don't have sufficient permissions" (GEZIEN): het adres bestaat dus en wil een sleutel. Openbaar en zonder sleutel werken `/api/plugins/35901/comments` (geeft `[]`, nog geen reviews, GEZIEN) en `/api/plugins/35901/rating` (GEZIEN). Of onze `JETBRAINS_MARKETPLACE_TOKEN` ook lezen mag: GOK (marketplace-stats gebruikt een sleutel van dezelfde pagina `author/me/tokens` als de upload). Eerste run in Actions zegt het meteen.
- **Moeite:** 2 uur (GOK). Chris of wie het scorebord doet.
- **Thijs:** niets als de bestaande sleutel werkt; anders één nieuwe sleutel op dezelfde pagina (3 min).
- **Regel 4:** leest alleen, plaatst niets.

### 2. dortus.com: productpagina's in de sitemap en een IndexNow-ping bij elke push
- **Wat:** de sitemap van dortus.com heeft 74 adressen en **geen enkele** daarvan is een productpagina van nu: geen `/click-joints/`, `/bison-flex/`, `/rollwright/` of `/ebb/` (GEZIEN, curl op `dortus.com/sitemap.xml`; H zag dit ook als bijvangst). Bijna alles is nog van de oude Atlassian-tijd. Daarnaast IndexNow: één `curl` die Bing, Yandex, Seznam en Naver vertelt dat een pagina nieuw of anders is. Het sleutelbestand staat al in de root: `dortus.com/99b51feeb51a9a81cb709b26637cf03d.txt` geeft 200 met de sleutel als inhoud (GEZIEN). Dat Bing ook de bron is achter Copilot en de AI-antwoorden in Bing: DERDEN ([PPC Land, 14 feb 2026](https://ppc.land/bing-gives-publishers-first-look-at-how-ai-systems-cite-their-content/)).
- **Probleem:** onze pagina's zijn goed gemaakt (titel, omschrijving, canonical, og-beeld en JSON-LD `SoftwareApplication` op alle vier, GEZIEN), maar we vertellen de zoekmachines niet dat ze bestaan. Straks komt `dortus.com/hats` erbij; die moet op de dag zelf bekend zijn bij Bing.
- **Hoe:** (a) de hoofdchat zet de productadressen in de root-sitemap (agents mogen root-bestanden niet aanraken, `regels/opslaan.md`), of elke productmap krijgt een eigen sitemap die via Search Console wordt ingediend (H). (b) een workflow in de repo `dortus` die na elke push de gewijzigde `.html`-adressen in één POST naar `https://api.indexnow.org/indexnow` stuurt.
- **Waar:** GitHub Actions van de repo `dortus`.
- **Kosten:** gratis.
- **Getest:** sleutelbestand en endpoint bereikbaar (`bing.com/indexnow` 200, GEZIEN). **Niet** echt ingediend: dat is een handeling op de site van Thijs, dus pas na het ja van de hoofdchat.
- **Moeite:** 1 uur (GOK).
- **Thijs:** niets. De hoofdchat beslist of hij de root-sitemap bijwerkt. Google doet niet mee met IndexNow (GOK); voor Google telt de sitemap.
- **Regel 4:** geen tekst naar buiten, alleen een melding aan zoekmachines.

### 3. Zoekcijfers vanzelf in het scorebord: Search Console API plus Bing Webmaster API (met AI-citaties)
- **Wat:** Search Console staat (geverifieerd 18 nov, toegang.md), maar alleen via Chrome. Met de API leest een workflow elke dag klikken, vertoningen en plek per zoekvraag en per pagina, en met de URL Inspection API of `/bison-flex/` en `/click-joints/` in Google staan. Bing Webmaster Tools doet hetzelfde voor Bing (`GetQueryStats` en meer, sleutel uit Settings, API Access, GEZIEN [Microsoft Learn](https://learn.microsoft.com/en-us/bingwebmaster/getting-access)) en heeft sinds 10 feb 2026 een rapport **AI Performance**: hoe vaak Copilot en de AI-antwoorden van Bing onze pagina's aanhalen (DERDEN, [PPC Land](https://ppc.land/bing-gives-publishers-first-look-at-how-ai-systems-cite-their-content/)). Of dat rapport ook in de API zit: GOK.
- **Probleem:** H en PLAN zetten in op uitlegpagina's voor Bison & Flex en Click Joints. Zonder zoekcijfers weten we na 60 dagen niet of een pagina werkt; Amami ziet bezoekers, niet de zoekvraag. Nu tellen de ±70 gidsen samen 0 tot 8 bezoekers per dag (GEZIEN in H, uit het scorebord).
- **Hoe:** Google: een serviceaccount (JSON-sleutel als secret) die Thijs in Search Console als gebruiker met beperkte rechten toevoegt; Google noemt serviceaccounts als geldige manier (GEZIEN, [Google](https://developers.google.com/webmaster-tools/v1/how-tos/authorizing)). Ruim genoeg quotum: 1.200 vragen per minuut per site (GEZIEN, [limieten](https://developers.google.com/webmaster-tools/limits)). Bing: API-sleutel als secret.
- **Waar:** GitHub Actions, workflow Scorebord, één keer per dag.
- **Kosten:** gratis.
- **Getest:** documentatie gelezen; zonder sleutel geeft het Bing-adres 400 (GEZIEN), Google kon ik zonder sleutel niet proberen. H noemde de Search Console-API al als GOK; nieuw hier is de bevestiging in Googles eigen tekst, de URL-controle en Bing met AI-citaties.
- **Moeite:** 3 uur (GOK).
- **Thijs (±20 min, GOK):** Google Cloud-project (gratis), serviceaccount en JSON-sleutel maken en als secret `GSC_SERVICE_ACCOUNT` plakken, het mailadres van dat account in Search Console toevoegen als gebruiker. Bing Webmaster Tools: inloggen met Google, site importeren uit Search Console, API-sleutel als secret `BING_WEBMASTER_KEY`. Bij Bing moet hij de API-voorwaarden accepteren (GEZIEN in de Microsoft-tekst); dat mag alleen hij.
- **Regel 4:** leest alleen.

### 4. Twitch-API voor de makerslijst van Hats, plus een eigen UTM-link per maker
- **Wat:** de Twitch Helix API geeft met een gratis app-sleutel live streams per spel (kijkers, taal, kanaal), video's en kanaalgegevens. Limiet 800 punten per minuut (GEZIEN, [Twitch API-gids](https://dev.twitch.tv/docs/api/guide/)). Daarnaast heeft Steamworks **UTM Analytics**: per link met `utm_source`/`utm_campaign` zie je bezoeken en verlanglijsten, met CSV-download (GEZIEN, [Steamworks](https://partner.steamgames.com/doc/marketing/utm_analytics)).
- **Probleem:** Sem schreef in `platformen/steam/marketing/makers.md`: SullyGnome, TwitchTracker en Streams Charts geven 403, "en de Twitch-API vraagt een sleutel van Thijs"; Twitch-streamers zocht hij daarom omweg via hun YouTube-archief, zonder live kijkcijfers. Het PLAN rekent voor Hats juist op de tweede golf via één passende middelgrote maker binnen 72 uur na de demo. Met de API maakt een workflow elke dag een lijst: wie streamt nu Rusty's Retirement, Bongo Cat en andere bureaubladspellen, met hoeveel kijkers, in welke taal. Met een UTM-link per maker zien we daarna in Steamworks welke maker echt verlanglijsten bracht, niet alleen weergaven.
- **Hoe:** REST (client credentials, `GET /helix/streams?game_id=...`), script naar `platformen/steam/marketing/` (alleen openbare kanaalnamen en aantallen, die staan nu ook al in makers.md).
- **Waar:** GitHub Actions (secret). Werkt ook in een sessie, `api.twitch.tv` is bereikbaar (401 zonder sleutel, GEZIEN).
- **Kosten:** gratis.
- **Getest:** alleen bereikbaarheid en documentatie. Dat een app-sleutel genoeg is voor `Get Streams`: GOK (het staat zo in de opbouw van de API, niet nagelezen per endpoint).
- **Moeite:** 3 uur (GOK). Sem (terug ±1 dec) of Olaf.
- **Thijs (±10 min):** een Twitch-account (bijvoorbeeld Dortus) met verplichte tweestapsverificatie (GEZIEN, [Twitch](https://dev.twitch.tv/docs/authentication/register-app/)), app registreren in de developer console, `TWITCH_CLIENT_ID` en `TWITCH_CLIENT_SECRET` als secret. Account aanmaken mag alleen hij.
- **Regel 4:** de API leest alleen. Makers benaderen blijft zoals nu: tekst klaarzetten, Thijs zegt ja, Thijs of de hoofdchat stuurt.

### 5. Steam-verlanglijsten en verkoop per dag: de juiste sleutel (rechtzetting in toegang.md)
- **Wat:** `IPartnerFinancialsService/GetAppWishlistReporting` geeft per app per dag de verlanglijst-cijfers, ook per land en taal; `GetDetailedSales` de verkoop (GEZIEN, [Steamworks](https://partner.steamgames.com/doc/webapi/IPartnerFinancialsService)). E vond dit al.
- **Wat ik rechtzet:** `organisatie/toegang.md` zegt "secret `STEAM_WEB_API_KEY`, sleutel aanmaken, ±3 min". Dat werkt niet: deze API wil een aparte sleutel van een **Financial API Group** (Manage Groups in Steamworks), geen gewone Web API-sleutel. Die groep ziet alle financiële cijfers van het hele partneraccount. Valve raadt een lijst vaste IP-adressen aan; GitHub-runners hebben die niet, dus we laten die lijst leeg (Valve schrijft "recommended", niet verplicht, GEZIEN). Verder: de cijfers van een dag zijn de volgende dag compleet en veranderen daarna niet meer (GEZIEN), dus één run per dag is genoeg.
- **Probleem:** na de paginadag is het verlanglijstcijfer de maat voor Hats (koers, besluiten). Nu moet Thijs het in Steamworks aflezen.
- **Hoe:** REST, script in `scorebord.py`, alleen totalen per dag.
- **Waar:** GitHub Actions.
- **Kosten:** gratis.
- **Getest:** `partner.steam-api.com/.../GetAppWishlistReporting/v001/` met een nepsleutel geeft 403 (GEZIEN): bereikbaar, wil een echte sleutel.
- **Moeite:** 1 uur (GOK), Olaf.
- **Thijs:** pas na de paginadag (Steamworks weigert nu alles tot Valve klaar is): Financial API Group maken en de sleutel als secret `STEAM_FINANCIAL_KEY` plakken (±5 min, GOK). De hoofdchat past de regel in toegang.md aan.
- **Regel 4:** leest alleen.

## Afgevallen
- **Product Hunt:** PLAN zegt niet doen; producthunt.com geeft 403 met curl (GEZIEN).
- **Gumroad Discover:** pas na $100 omzet uit echte verkopen, ingevulde uitbetaling en een risicokeuring van gemiddeld 3 weken (GEZIEN, [Gumroad Help](https://gumroad.com/help/article/79-gumroad-discover)). Wij hebben 0 verkopen. Wel alvast: categorie en tags invullen en reviews aan, dan staat Pro er vanzelf zodra het kan.
- **Keymailer, Woovit, Lurkit:** PLAN zegt geen Keymailer; Woovit-voorwaarden niet leesbaar (doorverwijzing, prijs niet gevonden). Curator Connect (gratis, in Steamworks) staat al in `platformen/steam/marketing/curatoren.md`.
- **SteamDB:** 403 met curl (GEZIEN), geen API.
- **SteamSpy:** werkt zonder sleutel (GEZIEN), maar geeft schattingen van anderen, niet onze eigen cijfers; bruikbaar voor concurrentie, niet als koppeling.
- **Steam-zoekplek meten:** `storesearch` geeft maar 10 treffers (GEZIEN); `search/results` wordt al gebruikt in `platformen/steam/marketing/data/`. Staat al in PLAN (scorebord stap 3).
- **Blender-winkel:** alles wat de openbare API geeft zit al in het scorebord; geen API voor downloads per dag, het scorebord rekent het verschil al uit.
- **Obsidian:** `community-plugin-stats.json` zit al in het scorebord; Rollwright is geparkeerd.
- **awesome-3d-printing, awesome-compilers, awesome-obsidian:** eisen of stilstand al beschreven in B-communities; awesome-obsidian (kmaasrud) laatste push april 2024 (GEZIEN, GitHub API). awesome-blender loopt al (PR #141).
- **Apify-scrapers voor JetBrains:** betaald en overbodig met punt 1.
- **Bing of DuckDuckGo met curl afzoeken op `site:dortus.com`:** gaf rommel of 202 (GEZIEN); geen betrouwbare meting, daarom punt 3.
- **Ahrefs Webmaster Tools:** gratis site-audit, maar de API is betaald (GOK); voegt weinig toe naast punt 3.

## Bronnen
- Steamworks Financial API: https://partner.steamgames.com/doc/webapi/IPartnerFinancialsService
- Steamworks verlanglijst-rapport: https://partner.steamgames.com/doc/marketing/wishlist/reporting
- Steamworks UTM Analytics: https://partner.steamgames.com/doc/marketing/utm_analytics
- marketplace-stats-kotlin (JetBrains-statistiek, MCP): https://github.com/jansorg/marketplace-stats-kotlin
- JetBrains-forum over download-API: https://platform.jetbrains.com/t/plugin-download-statistics-in-a-machine-readable-form/2942
- JetBrains openbare API (getest): https://plugins.jetbrains.com/api/plugins/35901 , https://plugins.jetbrains.com/api/plugins/35901/comments
- Search Console API, toegang en limieten: https://developers.google.com/webmaster-tools/v1/how-tos/authorizing , https://developers.google.com/webmaster-tools/limits
- Bing Webmaster API: https://learn.microsoft.com/en-us/bingwebmaster/getting-access
- Bing AI Performance: https://ppc.land/bing-gives-publishers-first-look-at-how-ai-systems-cite-their-content/
- IndexNow: https://www.indexnow.org/documentation
- Twitch API: https://dev.twitch.tv/docs/api/guide/ , https://dev.twitch.tv/docs/authentication/register-app/
- Gumroad Discover: https://gumroad.com/help/article/79-gumroad-discover
- dortus.com sitemap (gelezen): https://dortus.com/sitemap.xml
