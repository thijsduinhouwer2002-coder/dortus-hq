# Ideeën van lars

Nieuwste bovenaan. Werkwijze: platformen/ideeen/LEESMIJ.md.

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
