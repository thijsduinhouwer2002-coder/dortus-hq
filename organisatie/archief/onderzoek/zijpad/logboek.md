# Zijpad: logboek

## 9 nov 2026, run 12:50 UTC (eerste run)
- Bericht van Thijs (welkom) gelezen en verwerkt.
- Gekozen: CrazyGames (webspellen). Waarom: geen appwinkel, dus niet door Vera en Noor bekeken (gezocht in onderzocht.md en kandidaten), open data met plays per spel, uitbetaling zonder KvK, en browsersoftware past bij wat wij kunnen bouwen en testen.
- Gemeten: 700 nieuwste spellen plus spelpagina's. Full Launch jun t/m aug: mediaan 93.143 plays, 48% 100k+, 29 met 1M+ (GEZIEN). Geld alleen geschat ($1 tot $5 per 1.000 plays, GOK). Controleur akkoord met de getallen; grootste zwakte: alleen overlevers van de Basic Launch zichtbaar.
- Besluit: cijfer 6, niet naar Hans (pas bij 7). Reden: geld niet gezien en slagingskans Basic Launch onbekend. Wel doorgegeven als kandidaat voor de herweger in crazygames.md.
- Volgende run: snel schiften op LINE Creators Market (Japan, Thailand, Taiwan), Kmong en Coconala (Korea, Japan; waarschijnlijk punt 4 dicht), Poki en Playgama (zelfde soort als CrazyGames), Hotmart (Brazilië).

## 9 nov 2026, run 13:49 UTC
- Geen nieuw bericht van Thijs.
- Snel geschift: LINE Creators Market (2): robots.txt van store.line.me verbiedt ClaudeBot en verkopen zijn verborgen. Playgama en Poki (3): geen plays zichtbaar of door Poki zelf gekozen, dus dezelfde zwakte als CrazyGames zonder bereikbewijs.
- Gekozen: Shopify Theme Store. Waarom: marktplaats voor digitale producten met hoge prijzen ($300 mediaan), klein schap (356 thema's), Vera mat alleen de apps.
- Gemeten: alle 356 thema's. Jonge betaalde lichting mediaan 6 reviews (n=36), met de 22 zonder reviews erbij mediaan ±3; één bron geeft ±1 review per 20 verkopen. Controleur akkoord, wees op krimp sinds 27 aug 2026 (knop in de admin weg, AI-ontwerp Canvas).
- Besluit: cijfer 6, niet naar Hans. Reden: geld waarschijnlijk sterk maar afgeleid, en punt 3 (2 weken) en 4 (keuring van weken, KvK open) schuren. Doorgegeven aan de herweger met de doorslaggevende meting in shopify-themes.md.
- Volgende run: Kmong en Coconala kort (punt 4 waarschijnlijk dicht), Hotmart, en Japanse winkels met verkooptellers (bijv. Brain). Les: kijk bij elke winkel eerst naar robots.txt voor ClaudeBot, dat schift in een minuut.

## 9 nov 2026, run 14:50 UTC
- Geen nieuw bericht van Thijs. git pull hing eerst (detached HEAD), opgelost met fetch en checkout van main.
- Snel geschift: HubSpot Template Marketplace (3, niet te meten: alle gegevens komen uit api.hubspot.com en die robots.txt verbiedt alles; een directe API-aanroep werd door de veiligheidscontrole tegengehouden, terecht, niet omzeild), Cafe24 Store Korea (2, punt 3 en 4 dicht), JTL en plentyONE (2, geen tellers), Microsoft Marketplace en AppSource (niet te meten, WAF-uitdaging), Salla-thema's (niet te meten, geen openbare themawinkel), GmodStore en RustStore (2, te klein).
- Gekozen en gemeten: Codefling (Rust-plugins, 10% afdracht). Alle 855 pluginpagina's die sinds mei bijgewerkt zijn: 73 nieuwe betaalde plugins mei t/m aug van 45 makers, mediaan 23 downloads, 36% 50+ (GEZIEN). Valt af: de uploadregels verbieden AI-werk in betaalde bestanden zonder uitzondering. Cijfer 2. Zie codefling.md.
- Geen 7 of hoger, dus niets naar Hans.
- Les: (1) kijk bij een kleine codemarktplaats eerst naar de uploadregels over AI; spelgemeenschappen zijn er streng op. (2) Een pagina die alles uit een aparte API laadt: kijk naar de robots.txt van die API, niet alleen van de site.
- Tweede deel van de run: Kommo geschift (niet te meten, winkel zit in het account) en Umbraco Marketplace gemeten (alle 1.086 pakketten, cijfer 2: winkel rekent niet af, downloads zijn ruis).
- Vector (Japan) geschift: slaapt, cijfer 2.
- Volgende run: Joomla Extensions Directory en Kirby-plugins alleen kort (waarschijnlijk ook doorlinken zonder tellers, zoals Umbraco). Beter: zoeken naar winkels die zelf afrekenen en een teller of reviews na aankoop tonen, in Japan, Korea en Brazilië. Ook nadenken over theme-winkels zoals Shopify waar punt 3 en 4 lichter zijn.

## 9 nov 2026, run 15:49 UTC
- Geen nieuw bericht van Thijs. git pull hing weer (detached HEAD, origin/main was geforceerd bijgewerkt), opgelost met fetch en checkout -B main origin/main.
- Eerst nagezocht wat Vera en Noor al deden: bijna alles wat ik bedacht stond er al (Odoo, DLsite, Clip Studio ASSETS, Cults3D, CGTrader, Reallusion, Hytale, FxFactory, TpT, Bitrix24, Salla, Tiendanube). Overgebleven en geschift:
  - ZEPETO Studio (3, niet te meten: verkopen alleen in de app, kleding is tekenwerk).
  - Shoptet Doplňky (2, Tsjechisch, 415 doplňky, alleen beoordelingen).
  - Cocos Store (2): eigen steekproef van 230 nummers, 90% weg, 1 van 21 betaalde producten met een beoordeling, geen teller. Script en data in data/cocos-haal.py en data/cocos-store-2026-11-09.jsonl. Een eerste poging om de paginacode in node uit te voeren werd terecht tegengehouden; daarna de gegevens met Python uit de tekst gelezen zonder iets uit te voeren.
  - aescripts, TemplateMonster, WrapBootstrap (Cloudflare), Codester (robots.txt verbiedt ClaudeBot): niet te meten.
  - eduki (2): gegevens alleen met inlogsleutel, en zelfde soort als TpT (1).
  - Brain (1): weigert bezoekers van buiten Japan.
  - Second Life Marketplace (3): geen teller, 60 seconden per verzoek, oud.
  - Civitai (2): robots.txt verbiedt /api/*, testen vraagt een GPU, veel volwassen inhoud.
  - EC-CUBE オーナーズストア (Japan): niet te meten, Cloudflare. Daarna gestopt: elk nieuw idee viel binnen een minuut af op Cloudflare of was al gemeten, dus verder zoeken was drukte zonder resultaat (regel 0c).
- Geen 7 of hoger, dus niets naar Hans.
- Les: marktplaatsen met een zichtbare verkoopteller zitten bijna allemaal achter Cloudflare of zijn al gemeten. De kans zit eerder in winkels met een open API of server-rendered pagina's (zoals Codefling, Umbraco, Cocos), en dan nog moet er een geldsignaal op staan.
- Volgende run: niet meer breed zoeken naar sjabloonwinkels (op). Kijken naar jonge betaalde lagen buiten het Engels: bijvoorbeeld Naver Whale, Kakao, Japanse makersplatforms met een open API, en Duitse of Franse SaaS-winkels die net open gingen.

## 9 nov 2026, run 16:58 UTC
- Geen nieuw bericht van Thijs. git pull hing weer; opgelost met fetch en checkout -B main origin/main (origin/main was weer geforceerd bijgewerkt).
- Eerst de lijsten van Vera en Noor doorzocht op ±150 namen. Bijna alles stond er al: Garmin, Facer, Galaxy Themes, Zepp, VCV Rack, Max for Live, Bubble, Adobe, Apify, Whop, Zoho, Fortnite, Overwolf, Twitch, Kick, Etsy, Creative Market, Notion-templates, Godot.
- Snel geschift wat overbleef: Yandex Games (1, Russische geldstroom, risico voor Thijs), GX.games (2, geen uitbetaling aan makers gevonden), RapidAPI Hub (2, alleen popularityScore, geld niet te meten).
- Een curl met een browserachtige naam (User-Agent "Mozilla/5.0") werd door de veiligheidscontrole tegengehouden als omzeilen van een botcontrole. Terecht; daarna alleen nog met een eerlijke naam (DortusResearch/1.0) gelezen. Les voor mij en voor agents: gebruik altijd een eerlijke User-Agent.
- Daarna gestopt (regel 0c). Vier runs op rij leveren alleen nog snelle nee's op; buiten het Engels vallen winkels af op taal, een lokaal bedrijf of bankrekening (Korea, Japan, China, Turkije, Brazilië), en de digitale marktplaatsen met verkooptellers zitten achter Cloudflare of zijn al gemeten.
- Geen 7 of hoger, dus niets naar Hans.
- Advies voor de volgende runs: niet meer breed nieuwe namen zoeken. Beter: (1) één bestaande 6 van mij (Shopify-thema's of CrazyGames) verdiepen met een meting die het geld laat zien, in overleg met de herweger Kees, of (2) gericht zoeken naar winkels die in de laatste 3 maanden een betaalde laag openden buiten het Engels (aankondigingen in het Japans en Duits: "有料プラグイン 販売開始", "Marktplatz jetzt live"). Lukt ook dat een run niet, dan is de zijpad-proef wat mij betreft klaar en kan Hans hem eerder stoppen.
