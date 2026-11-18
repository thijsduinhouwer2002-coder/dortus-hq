# Ideeën van lars

Nieuwste bovenaan. Werkwijze: platformen/ideeen/LEESMIJ.md.

## 18 nov 2026 06:52 UTC: run 4, vooruitkijken (Blender 5.4 alpha, VS Code Insiders, JetBrains, Obsidian), 0 ideeën klaar voor keuring, 2 zelf afgeschoten

Tijd uit `date -u` bij de start. Opdracht van 18 nov ±07:40 NL gevolgd: alle pagina's van de release notes, en vooruit. Gelezen: alle 19 pagina's van Blender 5.4 alpha en de 5.3-pagina's core, assets, user_interface, pipeline_io, python_api, rendering, animation_rigging, modeling, sculpt, grease_pencil, geometry_nodes (bron: `projects.blender.org/blender/blender-developer-docs`, map `docs/release_notes/`, GEZIEN 18 nov); open PR's met "python api" op projects.blender.org; VS Code 1.142 t/m 1.146 en de Insiders-notities (1.147, 10 t/m 12 nov); JetBrains platformblog en nieuwsbrief Q3; Obsidian-changelog 1.15.1. Tips van Thijs: niets nieuws in mijn hoek (de lijst van 17 nov is af, zie UITKOMST.md).

**Eerlijk:** niets haalt alle 4 wetten. Wel één echte golf gevonden (canvassen in Copilot) en twee klokken om te volgen.

### Zelf afgeschoten: databank- of SQL-canvas voor Copilot (VS Code en de GitHub Copilot-app) | ZWAK op wet 3 en 4, dus niet ingediend
- **De golf is echt.** VS Code 1.142 (14 okt 2026) bracht "Canvases (Preview)": een paneel naast de chat waar mens en agent aan hetzelfde ding werken. "Every canvas is provided by a canvas extension", te installeren via een chat-plugin (GEZIEN 18 nov, code.visualstudio.com/updates/v1_142). 1.143, 1.144 (28 okt, Browse > Canvases in Agent Customizations), 1.145 (4 nov, canvassen op externe agents) en 1.146 (toestemmingen voor canvas-extensies, "Discover More") bouwen er elke week op door (GEZIEN, updates v1_143 t/m v1_146). GitHub noemt als voorbeelden plan, triagebord, dashboard, incident en spreadsheet (GEZIEN, docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-canvas-extensions).
- **Hoe vol is het na 5 weken:** de lijst op awesome-copilot.github.com/extensions/ telt **65 canvas-extensies van 37 makers** (GEZIEN 18 nov). Basistaken die al bezet zijn: tekenen (Draw, Diagram Explorer), Jupyter (Notebook), dia's (Markdstage), containers (Containers), PR-review (PR Review, Gesture PR Review), git (Git Worktree Explorer, Git Tag Manager), Actions (Repo Actions Hub, Artifact Explorer), Jira (Jira Workbench), mobiele emulators (Mobile Canvas), en vier verbruiksmeters (AI Credits Breakdown, Cache Stats, My AI Usage, Usage Insights). Verder veel Azure-canvassen. Wat ik niet vond: een canvas voor databanken of SQL, een API-client (zoals Postman) en een testresultaten-canvas.
- **Wet 1:** 5 weken oud, nog Preview en standaard uit (`chat.canvases.enabled`). Vroeg genoeg, maar het bereik is nu nog klein.
- **Wet 3 (bereik zonder kassa):** er is geen kassa. Erger voor de route via bereik: nergens zichtbare installaties of ranglijst. De awesome-copilot-lijst sorteert op A-Z of datum, de Copilot-app toont "a curated list of featured canvases" en VS Code "Editor's picks" (GEZIEN, zelfde bronnen). Nummer één worden is dus niet te meten en de etalage wordt door GitHub zelf gekozen. Route naar geld later: ONBEKEND, hooguit een betaalde versie buiten de winkel om.
- **Wet 4:** het platform laat iedere gebruiker zijn eigen canvas maken met `/create-canvas` ("describe the user interface you want", GEZIEN v1_142). Een eenvoudig SQL-canvas maakt een gebruiker dus zelf in een paar minuten. Microsoft heeft al een eigen SQL-extensie voor VS Code (mssql); dat zij er een canvas bij maken binnen 3 maanden: GOK, maar gezien de vele Azure-canvassen in de lijst waarschijnlijk.
- **Uitslag:** zwak. Geen harde nee op wet 1 of 2, maar op wet 3 (geen kassa en geen meetbaar bereik) en wet 4 (zelf maken met één opdracht) te veel tegen. Niet ingediend. **Volgen:** als VS Code installatiecijfers voor plugins gaat tonen of canvassen standaard aanzet, dan opnieuw bekijken, met het databank-canvas als eerste kandidaat.

### Zelf afgeschoten: projectbeheer voor het nieuwe projectsysteem van Blender 5.3 | DOOD op wet 4, zwak op wet 2
- Aanleiding (stond op de pagina core/ van 5.3, niet in python_api/; dit had ik op 17 nov ook gemist): Blender 5.3 heeft een eigen projectsysteem. Een map met `.blender_project` maakt alle bestanden eronder één project, met projectvariabelen zoals `{project_root}`, project-assetbibliotheken, eigen OCIO-instelling, eigen splash en recente bestanden per project (GEZIEN 18 nov, release_notes/5.3/core.md).
- **Wet 4:** Blender bouwt de rest zelf. De ontwerptaak noemt als volgende stappen: add-ons en hun instellingen per project (#165973, aangemaakt 2 nov 2026), variabelen per shot, en "Multi Project" met een lijst van recente projecten en een projectkiezer in de bestandsbrowser en het splash-scherm (#152911) (GEZIEN 18 nov, projects.blender.org/blender/blender/issues/133001, bijgewerkt 16 nov). Een projectbeheer-add-on wordt dus binnen een paar versies ingebouwd. Er staat al een WIP-PR voor ingebouwde projectvariabelen in de UI (#165691).
- **Wet 2:** de doelgroep volgens Blender zelf is "studios and one-person shops" (zelfde bron). Geen taak voor iedere gebruiker. Dood.

### Klokken om te volgen (nog geen idee)
1. **Eigen editors voor add-ons ("Custom space types", PR #165087, WIP, geen mijlpaal).** Met dit PR kan een add-on een heel eigen editor in Blender maken, met kop, zijbalk en panelen (GEZIEN 18 nov, projects.blender.org/blender/blender/pulls/165087, aangemaakt 13 okt door een studio met subsidie van het CNC). Op devtalk 111 likes en 1.395 keer bekeken; add-on-makers zijn enthousiast (GEZIEN, devtalk.blender.org/t/custom-space-types/45934.json). Maar: de UI-module vreest dat het "the gates to hell" opent, en de kernmodule schreef op 22 okt dat er eerst een plan en ontwerp moet komen (GEZIEN, PR-reacties van mont29 en devtalk 15 okt). Komt het erin, dan is dat een nieuwe soort add-on in een winkel waar wij al zitten (lichtmixer, eigen node-editor, datavisualisatie). Kans dat het in 5.4 komt (alpha tot 3 feb 2027): GOK, klein.
2. **Exporteren vanuit Geometry Nodes (PR #166422, open, bijgewerkt 17 nov).** OBJ en tekst wegschrijven vanuit nodes, ook per frame (GEZIEN 18 nov, projects.blender.org/blender/blender/pulls/166422). Raakt 3D-printen (Click Joints-hoek): als STL of 3MF volgt, kan een printklaar-uit-nodes-gereedschap zin krijgen. Nu nog te vroeg.
3. Bijvangst: er ligt een WIP-PR voor Blender op Android (#164188, bijgewerkt 9 nov, demo-APK's in branch `android-demo`). Geen golf voor ons zolang het niet in main staat.

### Overig gelezen, niets bruikbaars
- **Blender 5.4 alpha:** Delaunay-node, Repeat Zones en Closures in de compositor, kleinere blend-bestanden voor assets, thema zonder lettergrootte, iPad-gebaren via Sidecar, tooltip met projectnaam. Geen nieuwe soort add-on.
- **Blender 5.3 overig:** zoeken in alle zijbalken (ook tabbladen van add-ons), Markdown in labels en een Comment-node, LoopTools ingebouwd, Quad-Sphere, interop-ID voor kleurruimtes. Het zoeken in zijbalken en ingebouwde LoopTools maken juist add-ons overbodig.
- **VS Code Insiders 1.147:** voorgestelde API `contribTitleBar` (knoppen in de titelbalk), views boven de chat-invoer. Kleine functies, geen nieuwe soort.
- **JetBrains:** na 2026.3 alleen gereedschap voor makers (Plugin Verifier, Gradle-plugin, bewerken van de beschrijving op de site). Geen EAP van 2027.1 gevonden in de blogs (GEZIEN, blog.jetbrains.com/platform/feed en /idea/feed).
- **Obsidian 1.15.1:** ingebouwde Web viewer, widgets op Android en iOS. De insider-versies zijn niet openbaar te lezen (ONBEKEND wat erin zit).

### Les van deze run
De grote golf van dit najaar zit bij agent-oppervlakken (canvassen in Copilot, Agents-venster), niet in de klassieke winkels. Maar die nieuwe etalages hebben geen kassa en geen zichtbare telling, en het platform laat gebruikers hun eigen versie genereren. Voor Blender is het echte vooruitkijkwerk de lijst met open PR's, niet de alpha-notities: daar zie je weken tot maanden eerder wat er komt.

## 17 nov 2026 16:50 UTC: run 3, nieuwe golven in grote winkels, 0 ideeën klaar voor keuring, 6 zelf afgeschoten

Tijd uit `date -u` bij de start. Gelezen deze run (niet dubbel met run 2): changelog van de Notion-API, Framer-plugins, Google Workspace (release notes en Workspace Updates-blog), Chrome-extensies (whats-new), Blender 5.3 Python API, Figma plugin-updates (niets na update 142 van 12 nov), de JetBrains-winkel (API) en GitHub. Eerlijk: niets haalt alle 4 wetten. Wel één vondst die de ploeg moet weten (Jetplugins, hieronder).

### Vondst: Jetplugins zet in de JetBrains-winkel in serie betaalde "Pro"-taalplugins neer
- Leverancier Jetplugins (Australië, geverifieerd, handelaar) heeft **20 betaalde plugins**, allemaal met 7 dagen proef (GEZIEN 17 nov, `plugins.jetbrains.com/api/vendors/jetplugins/plugins` en `/api/plugins/31943`). Downloads: LaTeX Pro 3.210, Mojo Pro 3.142, Vue.js Pro 3.096, Obfuscation Pro 2.742, Nuxt Pro 2.638, Markdown Pro 2.145, Nix Pro 1.542, Elixir Pro 518, Slint Pro 455, Rust Pro 395, Lua Pro 372, TanStack Pro 325, Solidity Pro 279, DBML Pro 213, Swift Pro 166, Gleam Pro 96, Nim Pro 88, Marko Pro 82, Zig Pro 76, Toolkit for DuckDB 34. Downloads tellen ook proefinstallaties; verkopen ONBEKEND.
- Ouderdom: eerste versies tussen eind mei en begin aug 2026 (GEZIEN, update-lijst via de API: Mojo Pro 28 mei, Vue.js Pro 6 jun, Markdown Pro 7 aug). Het veld `cdate` in de zoek-API is de datum van de laatste update, niet van de eerste uitgave; let daarop bij tellen. Ze updaten bijna dagelijks (Markdown Pro 17 versies, Mojo Pro 18).
- Mojo Pro stond er al vóór Mojo 1.0 (11 aug 2026, GEZIEN modular.com/blog/modular-26-5-mojo-1-0-is-here) en heeft nu een tiende van de downloads van de gratis plugin "Mojo" (3.142 tegen 31.416). LaTeX Pro haalt 3.210 naast het gratis TeXiFy-IDEA met 903.021.
- Wat het betekent: (1) het model van Bison & Flex (betaalde taalplugin met proef) wordt door iemand anders op schaal gedaan, met veel plugins tegelijk en snelle updates, GOK met AI gebouwd; (2) een nieuwe taal in de JetBrains-winkel is geen open veld meer, Jetplugins zit er vaak binnen weken; (3) bewijs dat "X Pro" naast een gratis plugin wel downloads trekt, al is verkoop onbekend. Gemeld in `berichten/hoofdchat.md`.
- Ook gezocht naar nieuwe talen zonder goede JetBrains-plugin (typst, moonbit, hare, cue, kcl, d2, cedar, toon, wgsl, pony, ballerina en meer, GEZIEN zoek-API): wat open ligt is klein (Moonbit Language 377, HareLang 571, Cedar 245). Valt op wet 2 (geen brede basistaak).

### Zelf afgeschoten: officiële MCP of AI-zijpaneel voor Blender ("Claudian voor Blender") | DOOD op vraag 1 en 2
- **1.** Blender heeft een eigen MCP-add-on via Blender Lab, te vinden in Get Extensions op "MCP", voor Blender 5.1 en nieuwer (GEZIEN 17 nov, README van github.com/BI-Blitzer/blender-lab-mcp-bridge, die verwijst naar blender.org/lab/mcp-server/; die pagina zelf niet gelezen).
- **2.** De gemeenschapsversie mcp-for-blender heeft 34.780 sterren, bijgewerkt 15 nov; daarnaast skill-pakketten met 4.069 en 1.873 sterren (GEZIEN 17 nov, GitHub-zoek-API). Op extensions.blender.org staat onder 1.609 extensies voor 5.3 geen enkele met mcp, claude, agent, llm of ai in naam of tagline (GEZIEN, API); waarom ONBEKEND. Dood.

### Zelf afgeschoten: eigen stappen en starters voor Google Workspace Studio | DOOD op wet 4 en vraag 6
- Aanleiding: sinds 21 sep 2026 kunnen add-ons eigen starters en stappen leveren voor Workspace Studio, het agent-automatiseerhulpmiddel van Google (GEZIEN 17 nov, developers.google.com/workspace/release-notes).
- **Wet 4:** Google levert de koppelingen zelf mee: Asana, Confluence, HubSpot, Jira, Mailchimp, QuickBooks, Salesforce, Slack, plus webhooks (GEZIEN, workspaceupdates.googleblog.com, 17 sep 2026). De brede basistaak is dus van Google.
- **6 en 7:** standaard uit, de beheerder moet het aanzetten; testen vraagt een betaalde Workspace-omgeving (GOK op basis van "admins can enable" en "supported editions"). Dood.

### Zelf afgeschoten: Notion Workers (gehoste scripts, tools voor Custom Agents) | DOOD op wet 1 en bereik
- Workers bestaan sinds ±12 mei 2026 (ontwikkelportaal, GEZIEN developers.notion.com/page/changelog), dus 6 maanden oud. Delen kan alleen binnen de eigen werkruimte ("Share and collaborate with other workspace members", GEZIEN developers.notion.com/llms.txt). Geen winkel voor Workers, dus geen bereik en geen kassa. De Notion Marketplace is voor gewone OAuth-koppelingen. Dood.

### Kort afgevallen, zonder eigen kop
- **Framer-plugins:** nieuwste golven zijn CMS-lijstvelden (5.0, 8 sep) en de publiceer-API (4.1, 4 aug); niets in oktober of november (GEZIEN, framer.com/developers/changelog). Te oud voor wet 1.
- **Chrome-extensies:** laatste nieuwe API is browser.publicSuffix (Chrome 153, 25 aug), daarvoor tabbladmenu's (Chrome 150, 10 jun) (GEZIEN, developer.chrome.com/docs/extensions/whats-new). Geen golf; Chrome staat bovendien geparkeerd (besluit 17 nov 10:50).
- **Google Docs-API, opmerkingen en voorstellen (30 sep):** apps kunnen nu voorstellen lezen en maken (GEZIEN, Workspace release notes). Accepteren en weigeren kan Docs zelf al; 7 weken oud. Te zwak op wet 1 en 4.
- **Blender 5.3, ingebouwde OpenEXR-module en betaalde bibliotheken via toegangssleutel** (`use_access_token_for_asset_libraries`, GEZIEN release notes 5.3 python_api): het eerste is een nis (wet 2); het tweede is gereedschap voor winkels als Superhive, niet voor ons, en de bibliotheekhoek is gekeurd en dood (keuring 17 nov).

### Les van deze run
De grote winkels zonder kassa (Chrome, VS Code, Notion, Workspace) hebben de verse golven; de winkels met kassa (JetBrains, Figma, Blender via Superhive) worden óf snel gevuld óf de maker levert het zelf. In JetBrains is er nu een concurrent die precies onze aanpak (snel, betaald, veel talen) industrieel doet. Voor de volgende run: alleen nog golven die in een winkel mét kassa vallen en waar Jetplugins of de maker zelf aantoonbaar nog niet zit; anders niets indienen.

## 17 nov 2026 16:05 UTC: run 2, nieuwe hoek (nieuwe golven in grote winkels), 0 ideeën klaar voor keuring, 6 zelf afgeschoten

Tijd uit `date -u`. Hoek volgens bericht hoofdchat 17 nov ±16:55 NL en `organisatie/koers-kingmaker.md`. Gelezen: changelogs en release notes van Obsidian, VS Code, JetBrains (platformblog en API-wijzigingen 2026.3), Figma (plugin-API updates 139 t/m 142), Blender 5.3 en 5.4 alpha, Adobe (UXP), Shopify (changelog-feed), Canva (SDK-changelogs), Raycast. Blender 5.3 asset-bibliotheken heeft Noor al; niet dubbel gedaan.

**Les van deze run.** In grote winkels is een nieuwe API binnen dagen vol, of de maker van het platform levert de basistaak zelf mee met dezelfde release. Figma: de 3D-API kwam op 12 nov, en op 17 nov zijn er al minstens 10 plugins voor 3D, mockups en perspectief die sinds 10 nov een update kregen, waarvan 8 pas sinds okt bestaan. Blender: OpenTimelineIO kwam in 5.3 als module én als ingebouwde import en export. Het echte vroege moment zit dus **vóór** de stabiele release: in alpha-, bèta- en EAP-notities. Voorstel voor de ploeg: de zoekers lezen bij Blender (5.4 alpha tot 3 feb 2027), JetBrains (EAP) en Obsidian (catalyst) de notities van wat er nog moet komen, zodat Gijs op dag 1 klaarstaat. Blender 5.4 alpha bevat nu nog niets bruikbaars (GEZIEN 17 nov, developer.blender.org/docs/release_notes/5.4/: alleen NLA-geluidsstroken via Python, PLY-attributen, VSE-snelheid).

### Zelf afgeschoten: OpenTimelineIO-import en -export voor de Blender-sequencer (Premiere, Resolve naar Blender) | DOOD op vraag 1
- Aanleiding: Blender 5.3 (10 nov 2026) levert de Python-module `opentimelineio` mee (GEZIEN 17 nov, developer.blender.org/docs/release_notes/5.3/python_api). Op extensions.blender.org staat geen enkele extensie voor OTIO, EDL of XML-tijdlijnen (GEZIEN 17 nov, API-lijst van 1.609 extensies voor 5.3, gezocht op otio, edl, xml, premiere, resolve, timeline).
- **1.** Blender doet het zelf: "OpenTimelineIO: Initial export/import support, to export for final touch-ups in other software or import when relying on Blender-exclusive workflows like scene strips" (GEZIEN 17 nov, developer.blender.org/docs/release_notes/5.3/sequencer, PR#158562 en PR#161207). Dood.

### Zelf afgeschoten: 3D-mockups met de nieuwe 3D-API van Figma | DOOD op vraag 1 en 2
- Aanleiding: Figma-plugins kunnen sinds 12 nov 2026 lagen in 3D draaien, over de Z-as bewegen en perspectief instellen, ook met Motion-sleutelbeelden (bèta) (GEZIEN 17 nov, developers.figma.com/docs/plugins/updates/2026/11/12/version-1-update-142).
- **1.** Figma kan 3D zelf in de editor: helpartikel "Create 3D effects in Figma Design" (help.figma.com/hc/en-us/articles/44568893374999, GEZIEN in zoekresultaat 17 nov; de pagina zelf laadt niet zonder browser, inhoud ONBEKEND).
- **2.** Vol, ook bij de nieuwkomers. Via de zoek-API van Figma Community (GEZIEN 17 nov): 3D Mockup Pro (1.369 gebruikers, update 12 nov), Smart Transform (1.737, update 11 nov), Plinth (484, gratis mockups, sinds 9 okt), Kusabimaru (44, 3D-apparaten, update 14 nov), 3DIfy (94, update 11 nov), Perspective Warp (update 16 nov), Isoskew, Shovra. Oude grote: 3D Transformer (361.571), Artboard Mockups (972.255, betaald), Clay Mockups 3D (630.131). Dood.

### Zelf afgeschoten: presets en stijlen voor Figma Motion | DOOD op vraag 2
- Aanleiding: plugins kunnen sinds 30 sep 2026 eigen Motion-animatiestijlen maken (GEZIEN, update 140).
- **2.** Al minstens 8 preset-plugins voor Figma Motion, bijgewerkt tussen juli en oktober (GEZIEN 17 nov, zoek-API): MotionFX (2.038 gebruikers), Animate it (23.783), Motion Presets (708), Motion Kit (450), Motion Loops (336), MographKit (158), Kinei (140), plus Lottie-bruggen (Figma Motion to Lottie, 5.591). De golf is al maanden oud. Dood.

### Zelf afgeschoten: eerste UXP-plugins voor After Effects (en Media Encoder) | DOOD op vraag 6
- Aanleiding, sterk op wet 1 en 3: Adobe brengt UXP-plugins naar After Effects ("Public beta UXP plugins by November 2026"), Media Encoder heeft een openbare bèta, en CEP verdwijnt eind 2029 (GEZIEN 17 nov, blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications). De pagina "UXP for Adobe After Effects" staat er nu, met "throughout the beta" (GEZIEN 17 nov, developer.adobe.com/after-effects/uxp/). After Effects heeft een sterke betaalcultuur (aescripts).
- **6.** Wij kunnen After Effects niet draaien: alleen Windows en macOS, met een Creative Cloud-abonnement. Bouwen kan, echt testen in de cloud niet. Daarbij: ExtendScript-panelen (waar de meeste AE-tools op draaien) vallen niet onder de overstap ("ExtendScripts are not affected"), dus de bestaande tools hoeven niet weg (vraag 2), en de UXP-plugins werken voorlopig alleen in de bèta van AE (GOK op basis van "public beta"). Dood voor ons; levend voor wie een Mac met AE heeft.

### Zelf afgeschoten: Shopify theme app add-ons en Sidekick-knop (Editions Fall 2026) | DOOD op wet 2 en vraag 7
- Aanleiding: sinds 28 okt kunnen themamakers een app bundelen met hun thema, en apps kunnen Sidekick starten met een vooraf ingevulde vraag (GEZIEN 17 nov, shopify.dev/changelog, items "Introducing theme app add-ons" en "Start Sidekick conversations from your app").
- Add-ons zijn alleen voor wie zelf een thema in de Theme Store heeft (wij niet). De Sidekick-knop is een functie in een bestaande app, geen nieuwe soort app. Sinds 10 nov eist Shopify bovendien identiteitscontrole voor nieuwe apps, en elke app moet 10 installs op betalende winkels hebben voor je een tweede mag plaatsen (GEZIEN, shopify.dev/changelog/shopify-app-store-submission-requirements-build-grow-then-expand). Dood.

### Kort afgevallen, zonder eigen kop
- **VS Code, extensies in het Agents-venster (1.146, 11 nov):** extensies moeten ondersteuning voor dat venster aangeven (GEZIEN, code.visualstudio.com/updates). Geen betaalcultuur in de VS Code-winkel: wet 3.
- **Obsidian 1.15 (2 nov):** Mermaid vervangen door eigen bibliotheek Pele; bases kregen kanban (1.14, 5 okt) (GEZIEN, obsidian.md/changelog). Geen nieuwe soort plugin, en Obsidian betaalt slecht (Rollwright 0 verkopen): wet 3.
- **Canva, Autofill in apps (@canva/design 2.14.0, 27 okt):** apps kunnen ontwerpen vullen uit datavelden (GEZIEN, canva.dev/docs/apps/api/latest/design-changelog.md). Canva heeft Bulk Create zelf (GOK, niet nagelezen) en verkoopt in apps niet: alleen het Premium Apps-programma of een eigen betaallink (GEZIEN, canva.dev/docs/apps/monetization.md). Te zwak op wet 3 en vraag 1.
- **JetBrains 2026.3:** terminal op libghostty, geluidssignalen, nieuwe Search Everywhere-API, plugins mogen met toestemming andere plugins aan- of uitzetten (GEZIEN, blog.jetbrains.com/platform en plugins.jetbrains.com/docs/intellij/api-notable-list-2026.html.md). JetBrains bouwt de zichtbare functies zelf (beelden in de terminal, meldingen: "expect these to arrive faster"); wet 4.

### Spoor voor een volgende run
- After Effects UXP: als Dortus ooit een Mac met AE krijgt, of een tester, is dit de sterkste golf die ik zag (grote betaalcultuur, nieuwe soort plugin, nog nergens een lijst van UXP-plugins voor AE gevonden; ONBEKEND of er al zijn).
- Alpha- en EAP-notities volgen (zie les hierboven).

## 17 nov 2026 ±17:00 UTC: run 1 in de ideeënploeg, 0 ideeën klaar voor keuring, 6 zelf afgeschoten

Geen idee overleefde vraag 1 en 2. Les van deze run: bij gaten in grote producten zijn de bekende gaten (veel stemmen, al jaren oud) bijna altijd al gevuld door een gratis add-on of door een kleine maker met een extensie. Een oud gat met veel stemmen is dus geen goed teken op zich; het is een teken dat er al iemand zit. Kansrijker: een gat dat **pas net ontstond** doordat de grote speler iets weghaalde of veranderde, of een gat in een product waar weinig makers kijken.

### Zelf afgeschoten: Blender naar meerkleuren-3MF voor Bambu en Orca | DOOD op vraag 2
- Idee: Blender heeft geen eigen 3MF-export met kleuren voor meerkleurenprinters; past bij Click Joints en Superhive.
- **2. Concurrent, gratis en goed:** "3MF Import/Export" van Clonephaze staat op het officiële Blender Extensions-platform, versie 2.7.8, met "multi-color slicer-style paint workflows, slicer profile round-tripping, Orca/Bambu modifier parts", filamentkleuren schilderen en textures bakken naar filamentkleuren (GEZIEN 17 nov, extensions.blender.org/add-ons/threemf-io en de API-lijst van 1.680 extensies). Wat ik wilde maken bestaat gratis en vollediger. Dood.

### Zelf afgeschoten: mapgrootte in Google Drive | DOOD op vraag 2
- Drive toont nog steeds geen mapgrootte; oude klacht.
- **2.** Er zijn al minstens drie oplossingen: Chrome-extensies "Drive Folder Size Viewer" en "Drive Size Pro", en de webdienst FileRev met een eigen tool "View Largest Folders in Google Drive" (GEZIEN 17 nov in zoekresultaten, chromewebstore.google.com/detail/mgplnggmcblhblipimlbpdnbnnlnifdl en .../hoicecmnedhbmppcciljddgcfgcpcboc, filerev.com/tools/folder-size-google-drive). Gebruikersaantallen niet nagekeken (ONBEKEND). Geen aantoonbaar gat. Dood.

### Zelf afgeschoten: CMYK en millimeters in Figma voor drukwerk | DOOD op vraag 2
- **3. Vraag is er:** forumdraad "Physical units (mm/cm) and CMYK color support for print design" (27 okt 2026, 242 keer bekeken) en de oudere draad "Export to CMYK" met minstens 4 pagina's (GEZIEN 17 nov, forum.figma.com/suggest-a-feature-11/...-59350 en .../export-to-cmyk-36522).
- **2.** Er zijn al betaalde plugins: Hypermatic exporteert gecomprimeerde CMYK-pdf's uit Figma (GEZIEN, hypermatic.com/tutorials/how-to-export-compressed-pd-fs-in-cmyk-from-figma), "CMYK Exporter for Figma" op Product Hunt, "PrintX" op AlternativeTo (GEZIEN in zoekresultaten 17 nov). Figma zelf kan het nog niet (GOK op basis van het forum van 16 nov; release notes niet volledig gelezen). Volle hoek. Dood.

### Zelf afgeschoten: bestanden uploaden in Google Forms zonder Google-account | DOOD op vraag 2
- Google Forms vraagt nog steeds een Google-login bij een uploadvraag (GOK, volgens gidsen van 2026 zoals codewords.ai 12 feb 2026).
- **2.** Al bediend door File Upload Forms van Digital Inspiration (labnol, met betaalde versies, digitalinspiration.com/docs/file-upload-forms/pricing), Jotform, Formfacade en anderen (GEZIEN in zoekresultaten 17 nov). Dood.

### Zelf afgeschoten: Google Photos (dubbele foto's, automatisch downloaden na de API-afsluiting) | DOOD op vraag 1 en 2
- Achtergrond: sinds 31 maart 2025 mogen apps niet meer de hele Google Photos-bibliotheek lezen (GEZIEN, developers.googleblog.com "Google Photos Picker API launch and Library API updates"). Daardoor brak synchroniseren naar de pc en fotolijsten (theverge.com, tonfotos.com). Dat leek een vers gat.
- **1.** Google maakt Takeout voor Photos incrementeel: exports "will finally stop wasting your bandwidth" (GEZIEN in zoekresultaat, androidauthority.com/google-photos-incremental-takeout-3673297, en ccstartup.com 2 jun 2026). Het belangrijkste deel van het gat dicht Google zelf.
- **2.** Dubbele foto's: minstens 5 extensies (PicSweep, Cloud Duplicate Finder, Delete Duplicates from Google Photos CDF, Google Photos Duplicate Remover, Toppics). Downloaden: Google Photos Downloader, Album Batch Downloader, Snapback, het gratis Google Photos Toolkit op GitHub (GEZIEN in zoekresultaten 17 nov). Google Photos is de drukste hoek van "gat in Google"-extensies. Dood.

### Zelf afgeschoten: mail merge en andere gaten in de nieuwe Outlook | DOOD op vraag 1
- Gedachte: de verplichte overstap naar de nieuwe Outlook voor Windows haalt functies weg die mensen gebruikten.
- **1.** Microsoft levert Mail Merge (Advanced) zelf in Outlook op het web en de nieuwe Outlook (GEZIEN, Message Center RM423047 via mc.merill.net) en kondigde in juni 2026 PST-ondersteuning en meer aan (windowslatest.com 13 jun 2026). Daarbij is testen zonder Microsoft 365-testomgeving lastig (vraag 6). Dood.

### Spoor voor een volgende run (nog geen idee): bulk-bewerken in Garmin Connect
- Garmin Connect kan nog steeds de privacy van oude activiteiten niet in één keer aanpassen; gebruikers delen sinds 2021 een eigen script dat je in de browserconsole plakt (GEZIEN 17 nov, forums.garmin.com/.../252746/bulk-update-activity-privacy-settings, en draad 107758 "bulk change of privacy settings for past activities" met reacties over jaren).
- Uitrusting (gear) aan oude activiteiten koppelen kan sinds ±maart 2026 wél deels zelf: "Add to old activities matching the activity type" (GEZIEN, forums.garmin.com/.../431912/gear-tracking---new-grouping-feature). Dat deel valt dus af.
- Waarom het nog geen idee is: vraag 4 (betalen Garmin-gebruikers voor een extensie?) en de concurrenten (Connext en "Garmin Connect workouts manager" staan in de Chrome-winkel; wat die doen: ONBEKEND) heb ik nog niet uitgezocht. Pas Chrome-besluit van 17 nov 10:50 meewegen (Kai geparkeerd).
