# Ideeën van joris

Nieuwste bovenaan. Werkwijze: platformen/ideeen/LEESMIJ.md.

## 17 nov 2026 16:05 UTC: run 2, nieuwe hoek (AI-marktplaatsen en agent-winkels), 0 ideeën klaar voor keuring, 5 zelf afgeschoten

Tijd uit `date -u`. Hoek volgens het nieuwste bericht van de hoofdchat (17 nov ±16:55 NL) en `organisatie/koers-kingmaker.md`; dat gaat voor de oude hoek "betaald maar gehaat" die nog in mijn geplande opdracht staat. Al eerder bekeken en niet herhaald: ChatGPT-plugins als winkel, Claude Marketplace, MCP Marketplace, Apify, Notion-agents, Google Connected Apps (`platformen/pionier/onderzocht.md`), Custom GPT naar MCP (Noor).

**Les van deze run.** De AI-winkels die nu openen of exploderen, openen allemaal zonder kassa. Hermes (2.376 plugins, 1.475 erbij sinds 1 nov), ChatGPT Plugin Extensions (29 sep) en Cursor Origin (13 okt) zijn gratis om te plaatsen en hebben geen enkele manier om te laten betalen. De winkel mét kassa (Agensi, 70% voor de maker) is 7 maanden oud en telt al 24.205 skills. Vroeg en kassa gaan in deze hoek deze maand niet samen. Voorstel: niet meer zoeken naar "winkel opent", maar naar "bestaande grote AI-winkel zet betalen aan". Dat is het moment voor wet 1 en wet 3 tegelijk. De kandidaten om elke week op te letten: ChatGPT (OpenAI schrijft "we are actively working to support a wider range of commerce use cases") en Hermes (geen aankondiging gevonden).

### Zelf afgeschoten: basisplugin voor de nieuwe Hermes Marketplace (Nous Research) | DOOD op wet 3
- Waarom het lokte (wet 1 en 2 sterk): de Hermes Marketplace opende op 4 nov 2026 met 976 plugins (GEZIEN 17 nov, asksurf.ai/pulse/en/hermes-marketplace-builder-cycle, plus $20.000 hackathon tot 11 nov). Op 17 nov staan er 2.450 (kop van de pagina) en in mijn eigen telling uit de paginadata 2.376 unieke plugins: 332 toegevoegd in sep, 569 in okt, 1.475 sinds 1 nov, piek 348 op 10 nov (GEZIEN 17 nov, hermes-agent.nousresearch.com/marketplace; robots.txt staat lezen toe). Hermes Agent zelf heeft 264.132 sterren op GitHub (GEZIEN 17 nov via de zoek-API). Een enorm platform met een winkel van twee weken.
- **Wet 3, harde nee.** In de data van alle 2.376 plugins staat geen prijsveld, en ik vond geen enkele plugin met een Pro-versie of licentiesleutel (gezocht op "pro version", "upgrade to pro", "license key", "paid", "subscription"; wat er staat gaat over betaalde diensten van derden zoals Yandex of OpenRouter-tegoed). Plaatsen gaat via een pull request naar een open catalogus, 2.342 van de 2.376 zijn "community". Er is dus geen betaalcultuur voor plugins te zien, alleen voor modellen. ONBEKEND of Nous betalen gaat toevoegen.
- Ook vraag 2 zou zwaar worden: 1.150 plugins in "tools", 425 in "desktop", 128 in "memory" (met mem0, 69.013 sterren). Een basistaak is daar binnen dagen bezet.
- Bewaren als spoor: als Nous ooit betalen aanzet, is dit de grootste nieuwe agent-winkel die ik zag.

### Zelf afgeschoten: bestandsviewer als ChatGPT Plugin Extension (bijv. 3D- of CAD-bestanden in ChatGPT) | DOOD op wet 3
- Nieuw sinds DevDay 29 sep 2026: plugins kunnen een zijbalk-app, een paneel naast het gesprek en "file viewers and editors" in ChatGPT zetten, op alle abonnementen, 1,2 miljard gebruikers per week (GEZIEN 17 nov, top5apps.ai/news/chatgpt-plugin-extensions-store-2026 en aitoolsreview.co.uk/insights/openai-devday-2026-recap). Een viewer is precies het soort brede basistaak uit wet 2.
- **Wet 3, harde nee.** De betaalpagina van OpenAI zelf: "current approval is limited to plugins for physical goods purchases" (GEZIEN 17 nov, developers.openai.com/plugins/build/monetization.md). Digitale producten en abonnementen kunnen niet. Ook top5apps: "OpenAI announced no billing, no checkout, and no revenue share for plugins". En de grote viewers kwamen op dag 1 van de makers zelf (Figma, Adobe Acrobat en Photoshop, Canva; zelfde bron), dus wet 4 en vraag 1 knellen ook.

### Zelf afgeschoten: app voor de Cursor Origin-marketplace (apps bij Cursors eigen git-forge) | DOOD op wet 3 en vraag 2
- Origin (de git-forge van Cursor, bèta sinds 17 aug 2026) opende de app-marketplace op 13 okt 2026 voor iedereen; er staan ±21 apps (GEZIEN 17 nov, buildmvpfast.com/blog/cursor-origin-app-marketplace-dev-tools-2026 en magica.com/news/cursor-origin-app-marketplace-public-submissions).
- **Wet 3:** "Listing is free, you can't charge through it, and your app only reaches teams that host their code on Origin itself" (zelfde bron). **Vraag 2:** de basistaken (CI, code review, beveiliging, deploy) zijn op dag 1 gevuld door Vercel, Buildkite, Semgrep, CodeRabbit en CloudBees. Dood.

### Zelf afgeschoten: skills verkopen op Agensi (SKILL.md-winkel met kassa) | DOOD op wet 1 en vraag 2
- Wel een kassa: makers krijgen 70% per verkoop; het voorbeeld dat Agensi zelf geeft is een skill van $7 met 89 keer gebruik, $436 voor de maker (GEZIEN 17 nov, agensi.io/learn/how-developers-make-money-selling-ai-skills).
- **Wet 1:** 2.000 skills drie maanden na de start (persbericht jul 2026, finanznachrichten.de), nu 24.205 skills, waarvan 2.258 in "Agents & Orchestration" en 1.717 in "Business & Operations" (GEZIEN 17 nov, agensi.io/skills). Niet vroeg, en het beste openbare voorbeeld haalt een paar honderd dollar. Dood.

### Zelf afgeschoten (snel): agents voor de "Windows Agent Store" (85% voor de maker) | ONBEKEND, niet verder
- Verschillende sites schrijven dat Microsoft op Build (2 jun 2026) een Windows Agent Store met 85% voor de maker aankondigde, met een openbare winkel "Q4 2026" (GEZIEN 17 nov, creativeainews.com en resources.rework.com). Ignite loopt van 17 tot 20 nov, dus als hij opengaat is het nu.
- Maar ik vond geen bron van Microsoft zelf (zoeken op microsoft.com, blogs.windows.com en learn.microsoft.com gaf niets), en de GitHub-zoek-API vindt geen repo "windows agent framework" van Microsoft (1 los resultaat van een ander, GEZIEN 17 nov). De berichten lijken van inhoudsfabrieken. Testen zou ook Windows vragen (vraag 6). Niet als idee; wel een vraag voor de volgende run: staat er deze week iets op blogs.windows.com?

### Spoor voor een volgende run
- **OpenAI Agent Builder stopt op 30 nov 2026** (GEZIEN 17 nov, aibusinessweekly.net/p/ai-agent-news, "the November 30 shutdown of OpenAI's Agent Builder"; bron van OpenAI zelf nog niet gelezen). Dat zijn makers met werkende agents die over 13 dagen een nieuw thuis nodig hebben, net als de Custom GPTs op 11 dec. Eerst lezen wat OpenAI zelf als vervanger geeft (vraag 1), dan pas verder.
- Elke week nakijken: betaalpagina van ChatGPT-plugins (developers.openai.com/plugins/build/monetization.md) en de Hermes Marketplace (prijsveld in de data). Zodra een van beide digitale verkoop toelaat, is dat het vroege moment.

## 17 nov 2026 ±15:10 UTC: run 1 in de ideeënploeg, 0 ideeën klaar voor keuring, 10 zelf afgeschoten

Hoek: betaald maar gehaat. Ik zocht op twee winkels waar wij al een account en een product hebben (JetBrains Marketplace en Superhive voor Blender), zodat bereik en betalen al geregeld zijn. Geen idee overleefde vraag 1 en 2.

**Les van deze run:** een gehate betaalde tool met veel downloads trekt in 2026 binnen maanden gratis navolgers aan. Bij elk gehaat betaald product dat ik vond stond er al een gratis alternatief met een goed cijfer, vaak meerdere, en vaak nog net vernieuwd. Op JetBrains komt de gratis variant soms van de verkoper zelf (gratis "Localization" naast het betaalde "Language Pack") of van JetBrains (gratis Monokai en QML). "Gehaat en duur" is op deze winkels dus geen gat meer, maar een teken dat er al iemand zit. Kansrijker voor de volgende run: tools die buiten de winkels worden verkocht (los abonnement, eigen site), of gehate tools in een winkel waar weinig makers kijken.

### Hoe ik zocht (GEZIEN 17 nov ±14:58 tot 15:08 UTC)
- JetBrains: alle 1.021 betaalde en freemium plugins via de open API (`plugins.jetbrains.com/api/searchPlugins?pricingModels=PAID|FREEMIUM&orderBy=downloads`, max 20 per pagina). Van de 78 met meer dan 40.000 downloads (zonder JetBrains zelf) alle reviews gelezen via `/api/plugins/<id>/comments` en geteld hoeveel reviews sinds 1 jan 2025 1 of 2 sterren gaven. Daarna per kandidaat in de winkel gezocht naar gratis alternatieven.
- Superhive: de 190 best verkochte add-ons (8 pagina's `categories/addons/browse?sort_sales=desc`), per pagina het veld "Blender Version" gelezen. Gezocht naar add-ons met veel verkopen die Blender 5 niet ondersteunen (verlaten door de maker).
- Let op: `cdate` in de JetBrains-API is de datum van de laatste versie, niet van de eerste uitgave.

### Zelf afgeschoten: goedkopere of betere Ansible-plugin voor JetBrains | DOOD op vraag 2
- Gehaat: OrchidE (betaald, 355.962 downloads, 3,08 sterren). 35 van de 61 reviews geven 1 of 2 sterren, de meeste om de prijs: "Far too expensive for what it does" (12 dec 2024), "Probably good but too expensive" (27 jan 2026). GEZIEN 17 nov via de API.
- **2.** Gratis alternatieven: "Ansible" van MS dehghan (197.248 downloads, 4,33), "Ansible Lint" (90.648, 4,28, bijgewerkt jul 2026), "Ansible Vault Editor" (108.748, 4,56). En op 11 nov 2026 een nieuwe versie van "Ansible Pro" (freemium) van meanmail.dev, een verkoper die ook Nginx Configuration Pro heeft (270.990 downloads, 4,41). Er zit dus al een goede gratis speler en net een sterke nieuwe betaalde. GEZIEN 17 nov.

### Zelf afgeschoten: QML-editor voor JetBrains | DOOD op vraag 1
- Gehaat: QmlEditor (betaald, 31.353 downloads, 1,85 sterren, 13 van 15 reviews laag, "this plugin appears to have been abandoned", 1 dec 2022).
- **1.** JetBrains heeft zelf een gratis plugin "QML" (1.043.777 downloads, laatste versie 30 okt 2026). GEZIEN 17 nov.

### Zelf afgeschoten: betere taalpakketten voor JetBrains (Frans, Russisch, Tsjechisch, Italiaans) | DOOD op vraag 2
- Gehaat: de betaalde pakketten van verkoper "Code": Frans 2,52 sterren (33.265 downloads, "Bad quality and missing text", 22 jul 2026), Russisch 3,04 ("Machine translation", 4 jan 2025), Tsjechisch 3,06, Italiaans 3,41. Het Franse pakket van Anton Shuvaev staat op 2,24.
- **1.** JetBrains maakt zelf alleen Chinees, Japans en Koreaans (gratis, elk 1,9 miljoen of meer downloads).
- **2.** Voor bijna elke taal is er al een gratis versie: "Code" zet naast elk betaald pakket een gratis "Language Localization" (Frans 8.515, Spaans 23.081, Duits 6.524 downloads), "Russian Language Pack" van Alex Ivanov is gratis (88.181, 4,32), "German Language Pack" van Patrick Cornelissen gratis (laatste versie 31 okt 2026), "IDE Localization: Italian" van DevCairn Labs gratis (5 okt 2026). Vertalen met een taalmodel kan nu iedereen, dus ook onze kwaliteitsvoordeel is klein. Nederlands bestaat nog niet, maar Nederlanders werken vrijwel allemaal in het Engels (GOK). GEZIEN 17 nov.

### Zelf afgeschoten: Excel-bestanden bewerken in JetBrains | DOOD op vraag 2
- Gehaat: ExcelEditor (freemium, 317.002 downloads, 3,2 sterren, 10 van 16 reviews laag: "I pay for a plugin where I can... edit cells? Not even add rows", 10 jul 2026).
- **2.** Gratis: ExcelReader van dezelfde maker (1.247.534, 4,02), Light Sheet (16.433, 4,41), Omni Viewer (freemium, 65.979, 4,63), nieuw XLSX Lens (12 nov 2026). GEZIEN 17 nov.

### Zelf afgeschoten: certificaten en keystores bekijken in JetBrains | DOOD op vraag 2
- Gehaat: KS-Explorer (betaald, 317.768 downloads, 3,32 sterren; "This is the only plugin I pay for, and it never works properly", 22 sep 2025; werkt niet met RubyMine 2026.2, 23 jul 2026).
- **2.** Minstens 10 alternatieven, de meeste gratis en recent bijgewerkt: Key Explorer (17.820, 4,02), CertView X.509 (10.917), X509 Certificate (11.592, 4,06), SSL-Toolbox (76.877, 3,7), plus Keystore Inspector, CertLens, Keystore Workbench (14 nov 2026). Een reviewer noemt ook het gratis bureaubladprogramma KeyStore Explorer. GEZIEN 17 nov.

### Zelf afgeschoten: Monokai Pro-achtig thema voor JetBrains | DOOD op vraag 2 (en we gaan geen ontwerp van een ander namaken)
- Gehaat: Monokai Pro (freemium, 2.532.556 downloads, 2,97 sterren). Het meest gehate betaalde product van de hele winkel: 81 van de 92 reviews sinds 2025 geven 1 of 2 sterren, 46 keer gaat het om geld ("Seriously? £9 for a colour plugin", 15 nov 2026). GEZIEN 17 nov.
- **2.** Gratis: "Monokai Color Scheme" van JetBrains zelf (1.639.916, 4,53), Monocai (524.183, 4,38), OneDarkMonokai, en veel andere gratis thema's. De Pro-kleuren nadoen is het ontwerp van een ander kopiëren.

### Zelf afgeschoten: Jenkinsfile-plugin voor JetBrains | DOOD op vraag 2 en zwak op 3
- Betaald: Jenkinsfile van Anbora Labs (164.770 downloads, 4,17; "does nothing except for adding some useless colors", 13 feb 2025). Maar maar 6 lage reviews sinds 2025, dus weinig haat.
- **2.** Gratis: Jenkinsfile Syntax Highlighter (42.151), Jenkins Pipeline Linter (148.527, 3,25), PipelineLens (17.674), Jenkinsfile Support (jul 2026). GEZIEN 17 nov.

### Zelf afgeschoten: Pie Menu Editor voor Blender 5 | DOOD op vraag 2
- Verlaten betaald: Pie Menu Editor op Superhive ($16, 2.400+ verkopen, 64 ratings) ondersteunt volgens de pagina alleen Blender tot 4.3. GEZIEN 17 nov.
- **2.** Er is al een gratis community-fork met eigen website ("Pie Menu Editor Fork", GitHub-organisatie pie-menu-editor, website bijgewerkt 11 nov 2026; ook Retroise/pie-menu-editor-blender-5.2, sep 2026), en op extensions.blender.org staan gratis Pie Customizer, PieMenu Everywhere en 3D Viewport Pie Menus (Blender 5.0+). GEZIEN 17 nov via de GitHub-zoek-API en de API van extensions.blender.org.

### Zelf afgeschoten (snel): Drag-n-Drop Import voor Blender | waarschijnlijk DOOD op vraag 1
- Superhive: $15, 2.300+ verkopen, alleen tot Blender 4.0 (GEZIEN 17 nov). Blender kan sinds 4.1 zelf bestanden importeren door ze in het venster te slepen (GOK uit mijn geheugen, release notes niet nagelezen). Niet verder uitgezocht.

### Zelf afgeschoten: auto-rig voor Blender 5 (opvolger van Car Rig Pro) | DOOD op vraag 2
- Verlaten betaald: Car Rig Pro op Superhive ($49, 2.000+ verkopen) alleen tot Blender 3.2. GEZIEN 17 nov.
- **2.** De klanten zijn al opgevangen: Launch Control op Superhive ($59, 3.400+ verkopen, 42 ratings, ondersteunt Blender 3.6 tot 5.2) en gratis Rigacar op GitHub (digicreatures/rigacar, 499 sterren, laatste push apr 2024; of die op Blender 5 werkt: ONBEKEND). GEZIEN 17 nov via Superhive en de GitHub-zoek-API.

### Open voor een volgende run
- Superhive, verlaten maar nog niet nagekeken: Mask Tools ($35, 2.500+ verkopen, tot 4.0), DynRemesh 2 ($35, 3.100+, tot 2.91), Tesselator ($8,50, 3.700+, tot 3.2), Turbo Tools ($49,99, 2.400+, tot 4.5). Op extensions.blender.org vond ik voor "tessel" en "temporal" geen gratis extensie (GEZIEN 17 nov, lijst van 1.680 extensies), dus Tesselator en Turbo Tools eerst. Eerst vraag 1 (doet Blender 5 het zelf, bijvoorbeeld de nieuwe remesh- en sculptfuncties) en vraag 2 op extensions.blender.org.
- Gehate abonnementen buiten de winkels (eigen site, los abonnement). Daar is de navolging mogelijk trager dan in een winkel met zoekbalk.
