# I: bewezen ideeën die we kunnen overnemen (opdracht Thijs, 18 nov 18:18 en 18:25)

Thijs: "misschien staat er een idee tussen dat wij kunnen kopiëren, iets aanpassen en uitbrengen, dan kunnen we snel schakelen."
Gezocht op 18 nov 2026 ±18:30 tot 20:00 NL, alles met curl gelezen. Vier jachtgebieden: (1) verlaten maar gevraagd, (2) bestaat op platform A en ontbreekt op B, (3) betaald succes met een zwakke nummer één, (4) commerciële code die de maker bewust onder MIT, Apache of BSD zette.

**Hoe gemeten (GEZIEN 18 nov):**
- WordPress: de 4.000 populairste plugins uit `api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[browse]=popular`, gefilterd op laatste update vóór 1 jun 2025 en 20.000+ actieve installaties (80 treffers), daarna supportfeeds gelezen.
- JetBrains: de 2.000 meest gedownloade plugins (`plugins.jetbrains.com/api/searchPlugins`), van alle 1.465 niet van JetBrains zelf de laatste versie opgehaald; 265 werken niet meer op 2025.3 of nieuwer (huidige IDE: 2026.3, build 263, uit op 5 nov 2026). Plus alle 101 betaalde of freemium plugins gesorteerd op sterren.
- Blender: GitHub-zoek-API (`topic:blender-addon` en "blender addon" in de omschrijving, 300+ sterren, geen push sinds 1 jun 2025) en de volledige lijst van extensions.blender.org (1.688 extensies, `extensions.blender.org/api/v1/extensions/`).
- Licenties: LICENSE-bestand zelf gelezen via `git clone --depth 1 --filter=blob:none` of raw.githubusercontent.com, niet alleen het label.

**Eerlijk vooraf over wet 1 (vroeg):** een overgenomen idee zit per definitie niet op een splinternieuw platform. Ik tel wet 1 hier als: het gat is net open (kapot gegaan of gestopt) en wij staan er binnen 7 dagen. Daarom scoort geen enkele kandidaat hoog op wet 1. Dat is het grootste punt waarop de hoofdchat moet kiezen.

---

## Top 5

### 1. Leesbare TypeScript-fouten in JetBrains (zoals Pretty TypeScript Errors in VS Code) | gebied 2 | cijfer 7

- **Wat:** TypeScript-foutmeldingen in WebStorm, IntelliJ, Rider en PhpStorm opmaken: types met kleur en inspringing, de foutketen uitgeklapt, scrollbaar, te kopiëren, met een knop "uitleg".
- **Bewijs van vraag:**
  - Pretty TypeScript Errors heeft in VS Code **2.329.487 installaties en 4,97 sterren** (117 beoordelingen), laatste update 29 mrt 2026 (GEZIEN, VS Code Marketplace-API `extensionquery`, `yoavbls.pretty-ts-errors`).
  - In de JetBrains Marketplace geen tegenhanger: zoektermen "pretty typescript", "ts errors", "type errors", "readable errors", "typescript error" geven niets wat dit doet (GEZIEN, searchPlugins).
  - Issue "Support for WebStorm?" in de repo van het origineel: **280 reacties, 24 antwoorden**, gesloten (GEZIEN via GitHub-zoek-API, github.com/yoavbls/pretty-ts-errors/issues/11; de reden van sluiten kon ik niet lezen, repo-API dicht).
  - JetBrains-gebruiker op 16 okt 2026, WebStorm 2026.2.3: "TypeScript error tooltips are truncated, unscrollable, and unformatted, which makes the error text difficult to read" (GEZIEN, youtrack.jetbrains.com/issue/WEB-80164, open, 0 stemmen).
- **Nummer één en waarom zwak:** er is geen plugin. De IDE zelf doet het half: volgens de titel van WEB-80164 wordt alleen de eerste regel van de foutketen opgemaakt.
- **Wat wij beter doen:** het hele werk van het origineel, plus wat JetBrains-gebruikers missen: scrollen, kopiëren, inklappen van lange types, en in de Pro-versie een korte uitleg in gewone woorden en "spring naar het type".
- **Licentie:** MIT, LICENSE-bestand gelezen ("MIT License, Copyright (c) 2023 Yoav Balasiano"). Code overnemen mag met naamsvermelding. Naam "Pretty TypeScript Errors", logo en teksten niet gebruiken; eigen naam.
- **Platform en geld:** JetBrains Marketplace, freemium met proef (zoals Bison & Flex: $19 per jaar persoonlijk). Kopers zijn beroepsontwikkelaars (verdienen er geld mee).
- **Wat Thijs moet doen:** niets nieuws; vendor-account en verkoopgegevens staan al. GOK: 5 minuten Sales Info als de koopknop weer leeg blijft, zoals bij Bison & Flex.
- **In 7 dagen?** GOK ja voor een eerste versie, met één echt risico: of een plugin de tooltip van de TypeScript-dienst van JetBrains mag vervangen. Dag 1 eerst een proef op precies dat punt; lukt het niet, dan stoppen. Keuring JetBrains komt erbij (±2 tot 9 dagen, eerder gemeten).
- **4 wetten:** vroeg 4 (gat bestaat al jaren, wij zijn wel de eerste in de winkel) | brede basistaak 9 (iedere TypeScript-gebruiker in een JetBrains-IDE) | kassa 8 (winkel met kassa, wij staan er al) | platform-safe 5 (WEB-80164 laat zien dat JetBrains aan de opmaak zit; GOK dat een volledige oplossing niet binnen 3 maanden komt, het ticket heeft 0 stemmen).
- **Grootste twijfel:** wet 4 en de technische vraag van dag 1.

### 2. Normal-, hoogte- en curvature-maps uit één foto in Blender (opvolger van DeepBump) | gebied 1 | cijfer 6

- **Wat:** in de Shader Editor van een kleurfoto met één klik een normal map, hoogtemap en curvature maken, plus 4x opschalen. Met AI-modellen die lokaal draaien.
- **Bewijs van vraag:**
  - DeepBump: **1.431 sterren**, laatste push 17 mrt 2025 (GEZIEN, GitHub-zoek-API).
  - Recente klachten dat het stuk is: "V8 crashes Blender 4.5.2" (23 sep 2025), "No Denpendancy install" (8 feb 2026, 12 antwoorden: "dependancies can't be found For Blender 5.1"), "Error" (27 aug 2026) (GEZIEN, github.com/HugoTini/DeepBump/issues/54 en zoek-API).
  - Het staat niet op extensions.blender.org (GEZIEN, volledige lijst). De oorzaak is te zien in de readme: de knop "Install dependencies" haalt pakketten van internet, en dat mag niet in de officiële winkel.
  - Wat er wel staat is eenvoudig: "Image to Mat" (bestand van 3,1 KB, dus geen AI) **15.098 downloads** sinds 16 jul 2025; "GeneradorMapsPbr" 1.905 sinds 16 feb 2026 (GEZIEN, de twee extensiepagina's). Er is dus vraag in de winkel en geen sterke speler.
- **Nummer één en waarom zwak:** DeepBump zelf (verlaten, crasht, niet in de winkel). In de winkel alleen een filter van 3 KB.
- **Wat wij beter doen:** werkt op Blender 4.2 tot 5.x als echte extensie, onnxruntime als meegeleverde wheels (geen download), de modellen meegeleverd (27 MB en 17 MB, GEZIEN met `git cat-file -s`). Pro: hele mappen tegelijk, naadloos tegelen, ruwheid en AO erbij, opschalen.
- **Licentie:** GPL-3.0, LICENSE-bestand gelezen; de modellen zitten in dezelfde repo onder dezelfde licentie, trainingscode niet beschikbaar (readme). Ons product wordt dan GPL, en dat moet in Blender toch al. Naamsvermelding verplicht. Naam DeepBump en de beelden uit `img/` niet gebruiken.
- **Platform en geld:** gratis op extensions.blender.org (Click Joints staat er al), Pro via Superhive of Polar met de route die we voor Click Joints al hebben (veld Website). Kopers: game- en archviz-makers, deels zakelijk (GOK).
- **Wat Thijs moet doen:** niets voor de gratis versie (Blender ID bestaat). Pro: niets nieuws als het via Polar gaat.
- **In 7 dagen?** Ja, de code bestaat; het werk is verpakken, wheels per besturingssysteem, de crashes vinden. Keuring extensions.blender.org: Click Joints ging in ±2 dagen (GOK uit `besluiten.md` 10 nov).
- **4 wetten:** vroeg 3 | brede basistaak 6 (elke Blender-gebruiker die met foto-texturen werkt, maar niet iedereen) | kassa 5 (Superhive verkoopt, maar de gratis versie is de motor; wat zo'n Pro verkoopt: ONBEKEND, Superhive-zoeken gaf vandaag fout 500) | platform-safe 8 (niets in de Blender-roadmap gezien over AI-texturen; GOK).
- **Grootste twijfel:** grootte van de wheels plus modellen tegen de uploadgrens van de winkel (ONBEKEND) en of de onnxruntime-crash op Windows oplosbaar is.

### 3. Gerelateerde berichten voor WordPress 7 die YARPP-sjablonen leest (opvolger van YARPP) | gebied 1 | cijfer 6

- **Wat:** een plugin voor "lees ook" onder berichten die de sjablonen, shortcodes en instellingen van YARPP overneemt, zodat een site in één klik overstapt zonder nieuw ontwerp. Pro: betekenis-zoeken (AI-embeddings) in plaats van alleen woorden, en klikcijfers.
- **Bewijs van vraag:**
  - YARPP (Yet Another Related Posts Plugin): **100.000+ actieve installaties, 1.166 beoordelingen (96%)**, laatste update 11 nov 2024, getest tot 6.7; WordPress zit nu op 7.1/7.2 (GEZIEN, wordpress.org-API).
  - Supportforum: "Is it abandoned?" (12 nov 2026: "Is there and chance that the plugin can be updated to avoid receiving warnings that it's abandoned?"), "Disabled Visual Revisions on WordPress 7.0 by Yet Another Related Posts Plugin" (27 jun 2026, PHP 8.5), "Getting poor relevant results" (7 jan 2026) (GEZIEN, wordpress.org/support/plugin/yet-another-related-posts-plugin/feed/).
- **Nummer één en waarom zwak:** YARPP is verlaten. De rest is kleiner of zwakker: Contextual Related Posts 50.000 (96%, actief, heeft een Pro), Intelly Related Posts 100.000 (86%), Related Posts for WP 10.000 (GEZIEN, zelfde API). Geen sterke nummer één.
- **Wat wij beter doen:** overstapknop die YARPP-instellingen en `yarpp-template-*.php` leest, werkt op WP 7 en PHP 8.5, sneller (eigen index), en betere treffers met embeddings in Pro.
- **Licentie:** GPLv2 or later (readme.txt van YARPP, GEZIEN via plugins.svn.wordpress.org). Code overnemen mag als onze plugin GPL is; dat is in de WordPress-map verplicht. Naam YARPP en Shareaholic niet gebruiken; "werkt met YARPP-sjablonen" als beschrijving (GOK dat dat mag, nakijken bij keuring).
- **Platform en geld:** gratis in de WordPress-map, Pro per jaar via Polar (al ingericht). Kopers: bloggers en uitgevers die met hun site geld verdienen. Past bij de uitkomst van vandaag (WordPress op de AI-golf, Respira als voorbeeld).
- **Wat Thijs moet doen:** een wordpress.org-account maken (±5 minuten, GOK geen ID). Pro-product in Polar kan de ploeg zelf.
- **In 7 dagen?** Bouwen ja. Keuring van de map: in juni 2026 ging de wachtrij van ±1.050 terug naar "nearly zero" (GEZIEN, make.wordpress.org/plugins, 13 jun 2026); de stand van nu is ONBEKEND.
- **4 wetten:** vroeg 4 (de overstap begint nu: WordPress waarschuwt gebruikers voor verlaten plugins) | brede basistaak 7 (elke blog) | kassa 6 (Pro via Polar; betaalbewijs in deze hoek alleen dat concurrenten een Pro hebben, verkoop ONBEKEND) | platform-safe 8 (WordPress zelf heeft geen gerelateerde berichten; Jetpack wel, gratis).
- **Grootste twijfel:** mensen met een werkende YARPP stappen pas over als hij echt breekt. Bijvangst: WordPress 7.3 krijgt jQuery 4, jQuery Migrate gaat eind 2027 uit (GEZIEN, make.wordpress.org/core 17 nov 2026); dan breken veel oude plugins tegelijk. Dat is een tweede golf voor dit soort opvolgers.

### 4. Tailwind-klassen sorteren in JetBrains, ook in Blade, Razor en Twig (opvolger van Tailwind Formatter) | gebied 1 | cijfer 5

- **Wat:** klassen in `class="..."` vanzelf in de aanbevolen volgorde zetten, bij opslaan of herformatteren, in elke taal die JetBrains kent.
- **Bewijs van vraag:** Tailwind Formatter **300.246 downloads, 4,57 sterren**, laatste release in de winkel april 2025 en alleen tot build 251 (2025.1), dus niet installeerbaar op 2025.3 en 2026.x (GEZIEN, Marketplace-API). Issue "Incompatible with 2025.* / 251.* Versions" 11 reacties, "Support for 'Run on Save'" 10, "Support for Run on Reformat Code" 4 (GEZIEN, github.com/WalrusSoup/Tailwind-Formatter/issues/103, /79, /99). In de repo staat een update tot 253 van 10 feb 2026, maar die is nooit uitgebracht (GEZIEN, clone).
- **Nummer één en waarom zwak:** zelf verlaten in de winkel. De plugin van JetBrains (337.735 downloads, 2,39 sterren) sorteert niet; wie sorteert gebruikt Prettier, en Prettier kent Blade of Razor niet zonder extra plugin (GOK). Vraag in YouTrack klein: WEB-51754 4 stemmen, RIDER-95994 (Blazor) 2 (GEZIEN).
- **Wat wij beter doen:** werkt op 2026.x, sorteren bij opslaan, Tailwind v4-volgorde, Blade, Razor, Twig, Vue.
- **Licentie:** README zegt "MIT" en de winkel linkt naar MIT, maar **er staat geen LICENSE-bestand in de repo** (GEZIEN, clone). Volgens de regel: code niet aanraken, alleen het idee. Eigen code is klein werk.
- **Platform en geld:** JetBrains, freemium. Zwak: sorteren is gratis te krijgen via Prettier. Pro alleen voor Blade, Razor en Twig (GOK dat daar betaald wordt; Laravel-ontwikkelaars betaalden jaren voor Laravel Idea).
- **Wat Thijs moet doen:** niets.
- **In 7 dagen?** Ja, klein product.
- **4 wetten:** vroeg 4 | brede basistaak 5 (iedere Tailwind-gebruiker in JetBrains, maar velen hebben Prettier) | kassa 4 | platform-safe 6.
- **Grootste twijfel:** route naar geld; meer een bereikproduct.

### 5. k6-loadtests in JetBrains, beter dan de huidige plugin | gebied 3 en 4 | cijfer 4

- **Wat:** k6-tests draaien, live grafieken en drempels in de IDE, debuggen in TypeScript.
- **Bewijs van vraag:** de enige k6-plugin heeft **87.028 downloads en 3,32 sterren**, freemium met proef van 30 dagen (productcode PKSIX) (GEZIEN, Marketplace-API). Reviews: "it would be 5 if it supported debugging typescript" (mei 2025), "documentation is exceptionally lacking" (mrt 2025), "Does not work with WSL at all" (okt 2023), drie keer 1 ster (GEZIEN, `/api/plugins/16141/comments`). k6 zelf 32.347 sterren (GEZIEN). Officiële VS Code-extensie van k6: 73.153 installaties (GEZIEN).
- **Nummer één en waarom zwak:** lage sterren en klachten, maar de maker is actief (laatste versie 15 okt 2026, werkt op 263) en belooft WSL en Docker inmiddels in de beschrijving. Zwak, niet dood.
- **Wat wij beter doen:** TypeScript zonder omweg, goede uitleg, nettere resultaten. Weinig onderscheid als de maker bijwerkt.
- **Licentie (gebied 4):** Apache-2.0, LICENSE-bestand gelezen. De maker verkoopt een betaalde versie en heeft de code zelf zo vrijgegeven. Overnemen mag met naamsvermelding en NOTICE. Naam van de plugin niet gebruiken; "k6" is een merk van Grafana Labs (GOK), alleen beschrijvend gebruiken.
- **Platform en geld:** JetBrains, freemium. Kopers: QA- en backendteams (bedrijven).
- **Wat Thijs moet doen:** niets.
- **In 7 dagen?** Ja als fork.
- **4 wetten:** vroeg 2 | brede basistaak 3 (nis: k6-gebruikers in JetBrains) | kassa 7 | platform-safe 8.
- **Grootste twijfel:** wet 2 en het voelt als het overnemen van één actieve kleine maker; ik raad het niet aan, maar het is de beste vondst in gebied 4.

---

## De rest kort

- **Opvolger van Code With Me (samen programmeren in JetBrains)** | gebied 1, groot maar niet in 7 dagen. JetBrains stopt ermee: 2026.1 was de laatste IDE met officiële steun, nieuwe verkoop en verlengingen gestopt, "The public relay infrastructure will be turned off" in Q1 2027 (GEZIEN, blog.jetbrains.com/platform/2026/03/sunsetting-code-with-me/). Plugin 1.526.627 downloads, 3,48 sterren. Alternatief CodeTogether 186.322, laatste versie okt 2025 (GEZIEN). Teams betaalden ervoor. Maar: echte gelijktijdige bewerking plus een relay-server is weken werk en kost serverruimte (geld van Thijs). JetBrains zegt zelf dat de vraag na de pandemie zakte. Bewaren: als we ooit een tweede JetBrains-product van formaat willen, is dit het. Licentie: n.v.t. (code niet open).
- **Opvolger van YARPP-achtige verlaten WordPress-plugins in het algemeen** | gebied 1. Andere verlaten plugins met 50.000+ installaties: If Menu (50.000, laatste update dec 2024, forum: "PRO stopped working" jul 2025, "If Menu blocks Appearance > Menus" nov 2025), Q2W3 Fixed Widget (70.000, mrt 2023, "Plugin still maintained?"), Enhanced Media Library (60.000, jul 2024), Heartbeat Control (70.000, aug 2023), Add From Server (60.000, dec 2020) (GEZIEN, API en supportfeeds). Bij elk staat een actieve concurrent klaar: Conditional Menus 60.000 en User Menus 80.000, Sticky Menu 90.000, FileBird 200.000 (sterk, overslaan). If Menu is de enige met een gestopte Pro; klein.
- **Tailwind- en andere verlaten JetBrains-plugins** uit de lijst van 265: de meeste zijn vervangen of ingebouwd (zie afgewezen). Van de 265 bleef alleen Tailwind Formatter over als echt gat.

## Gebied 4 apart: commerciële code onder MIT, Apache of BSD

Weinig te halen op onze platformen, en dat heeft een reden: **Blender-add-ons en WordPress-plugins zijn verplicht GPL**, dus een betaalde add-on daar is nooit MIT; het overnemen van een betaald GPL-product mag wel, maar dan maken we een kloon van iemands winkelproduct en dat botst met "nooit naam, beelden of teksten van een ander" en levert geen eigen plek op. Gevonden en gecontroleerd:
- **k6 (JetBrains), Apache-2.0**, freemium van de maker: in de top 5 als nummer 5.
- **Cypresso (JetBrains), MIT** ("MIT License, Copyright (c) 2019 Mikhail Bolotov", gelezen; laatste commit 17 feb 2025). De maker maakte hem in okt 2024 betaald: "A huge dislike for turning this plugin into a paid item" (15 okt 2024, 1 ster), 150.663 downloads, 3,65 sterren (GEZIEN). Afgewezen op wet 4: de Test Automation-plugin van JetBrains (2.690.351 downloads) belooft "Rich support of Selenium, Selenide, Playwright and Cypress frameworks" (GEZIEN).
- **Niet nagekeken, uit mijn hoofd, daarom GOK:** Material Theme UI (was MIT tot 2022), GitToolBox (was Apache), Wappalyzer (was MIT tot 2023). Alle drie hebben nu een sterke nummer één (Material Theme UI 19.044.264 downloads, GitToolBox 10.807.738, GEZIEN in de JetBrains-lijst), dus overslaan volgens de regel van Thijs.

---

## Afgewezen, met reden (zodat niemand het opnieuw voorstelt)

| Idee | Waarom niet | Bron (GEZIEN 18 nov) |
|---|---|---|
| Discord-status voor JetBrains (oude plugin 963.414 downloads, laatste versie okt 2023) | Vervangers bestaan en worden bijgewerkt: Discord Integration V2 207.510, Discord Rich Presence 125.056. Geen geld. | Marketplace-API |
| Camera op een foto passen (opvolger fSpy-importer, 1.472 sterren, push mei 2022) | Al 3 extensies: Perspective Match, FTC Fit The Camera, Simple Camera Match | extensions.blender.org-lijst |
| Mixamo naar Unreal-rootmotion (mixamo_converter, 823 sterren) | Mixamo Rig en Import Mixamo Root Motion staan al in de winkel | idem |
| Sprytile (tegel-levels in Blender, MIT, 1.160 sterren) | Raakt de tegel-hoek die Patrick op 18 nov al keurde (Roblox, zwak 4) en Tessera staat al in de winkel; niet verder gemeten | keuring.md run 7, extensies-lijst |
| MB-Lab, Sorcar, Magic UV, fast-carve, rigacar | Sterke vervangers (MPFB2 en Human Generator; Geometry Nodes ingebouwd; BoxCutter en HardOps) of al afgeschoten (auto-rig, Joris 17 nov) | joris.md, GitHub-zoek-API |
| BashSupport, Markdown Navigator, CodeGlance, Laravel, ESLint, Presentation Assistant, Nx Console (allemaal 400.000 tot 14 mln downloads, kapot op 2025.3) | Ingebouwd in de IDE of vervangen door een nieuwe plugin (Laravel Idea, CodeGlance Pro, Nx Console onder ander nummer) | Marketplace-API, updates per plugin |
| Git Flow Integration (682.522, tot 2021.2) | Git Flow Integration Plus 109.606 en GitFlowPlus bestaan; git-flow is een krimpende werkwijze (GOK) | Marketplace-API |
| RestfulToolkit (513.071, tot 2021.1) | RestfulToolkit-fix 419.748, RESTFul-Tool, Cool Request; Endpoints zit in de IDE | Marketplace-API |
| Thrift Support (361.150, tot 2022.1) | Thrift Support (fork) 199.709, actief | Marketplace-API |
| Cypresso (Cypress in JetBrains) | Wet 4: JetBrains Test Automation dekt Cypress | zie gebied 4 |
| Shopware-plugin (111.949, 3,02) | Één review: "the official Shopware and Symfony support" maakt hem overbodig; framework-plugin is te groot voor 7 dagen | comments-API |
| Redis- en MongoDB-viewers voor JetBrains | Database-gereedschap zit in de IDE; Database Navigator 5.063.900 gratis | Marketplace-API |
| Ansible, QML, taalpakketten, Excel, keystores, Monokai, Jenkinsfile (JetBrains) | Al afgeschoten door Joris op 17 nov | joris.md |
| LuckyWP Table of Contents (90.000, verlaten apr 2025) | Sterke nummer één: Easy Table of Contents 600.000, actief | wordpress.org-API |
| Limit Login Attempts (oud, 200.000) | Limit Login Attempts Reloaded 1.000.000, actief | idem |
| Verdwenen MV2-extensies voor Chrome | Al gedaan door Vera en Kai op 17 nov (Revolver, autoplay, AutoPagerize) | verkenner/chrome-mv2-zonder-opvolger.md |
| Google Agenda in bulk (Chrome) | Al besloten: niet bouwen (17 nov) | besluiten.md |
| Mobiele apps | Alleen noemen: te veel werk voor Thijs (UITKOMST.md). Niets onderzocht. | |

## Advies in één regel
Nummer 1 (leesbare TypeScript-fouten in JetBrains) eerst, met een proef van één dag op de tooltip; parallel nummer 2 (DeepBump-opvolger) omdat de code er al ligt en Blender ons kanaal is. Nummer 3 als we WordPress willen openen. 4 en 5 alleen als opvulling.
