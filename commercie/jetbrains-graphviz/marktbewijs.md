# Graphviz/DOT: betalen mensen ervoor, en voor welke functies? (Chris, 8 nov 2026, nagekeken)

Onderzoeker voor Chris, op vraag van Jet. Gemeten op 8 nov 2026 tussen 15:30 en 16:00 UTC met curl (alleen lezen). Labels: GEZIEN (zelf gemeten, URL erbij), DERDEN (bron met link), GOK.

## In het kort voor Jet en Hans (Chris, 8 nov ±16:10 UTC)
Marktbewijs voor punt 2 en 3 van "Wat nodig is voor een ja" in `platformen/jetbrains/volgend-product.md`. Ik kies het product niet; dat doen Jet en Hans.
1. **Graphlume (id 35167, KITSS TECH, de maker van BatchCraft) is al het product uit het voorstel** (GEZIEN, `/api/plugins/35167`): gratis Graphviz 16.1.0 ingebouwd, voorbeeld op de achtergrond zonder bevriezen, aanvullen, inspecties, hernoemen; Pro: klikbaar voorbeeld, 8 lay-outs, export SVG/PNG/PDF, export bij opslaan, DOT in Markdown, zoeken in grote grafen. **$10 per jaar** (of $1 per maand), persoonlijk en zakelijk gelijk, proef 7 dagen, werkt in 2026.3. Het verschil met het voorstel is alleen nog "graaf in IDE-themakleuren".
2. **Hij heeft 30 downloads omdat de IDE hem niet aanraadt**: zijn plugin.xml meldt de bestandssoort zonder `extensions=` aan, dus hij staat niet in de lijst voor `*.dot` en `*.gv` (GEZIEN). Eén regel van KITSS TECH en hij staat erin. De zin in het voorstel "Graphlume meldt `*.dot` wel aan, grafische editor" klopt niet.
3. **Punt 3 (iemand betaalt voor DOT): niet gevonden**, nergens: JetBrains alleen Graphlume, VS Code 61 Graphviz-extensies allemaal gratis, App Store en webdiensten geen betaald DOT-plan (behalve Gravizo voor privacy, klanten onbekend). Wel betaald in de buurt: Mermaid Studio Core ±3.600 per maand ($25), Mermaid Studio ±1.200 ($49), Structurizr DSL ±485 ($99), SequenceDiagram Core ±6.100 ($10) (GEZIEN, downloads, geen verkopen).
4. **Wat in deze markt achter betaling zit**: PDF, export bij opslaan, klik naar bron, eigen thema's. Gewone export SVG/PNG is bijna altijd gratis (ook bij DOT Studio).
5. **Beste meting die nog kan (GOK)**: Graphlume elke week volgen in de weekmeting van 15 nov, en of hij in de aanraadlijst komt. Groeit hij dan met honderden per maand, dan is er vraag naar betaald DOT, maar is de plek ook bezet; blijft hij laag, dan is betalen voor DOT onwaarschijnlijk. Zie advies 22.

Belangrijk vooraf: geen enkele bron laat verkopen zien. De Marketplace geeft downloads, geen aantallen betalers. Elk "betaalt" hieronder is dus afgeleid van downloads van een betaalde of freemium plugin, niet van verkoopcijfers.

Maat "per maand": downloads van de nieuwste versie gedeeld door haar leeftijd, of (bij plugins met veel versies) de downloads van alle versies van de laatste 90 dagen gedeeld door 3. Beide uit `https://plugins.jetbrains.com/api/plugins/{id}/updates?size=50`. Bij zeer jonge versies (dagen oud) is dat onbetrouwbaar, dan staat de 90-dagenmaat erbij.

## Hoofdvondst (lees dit eerst)

**Graphlume is geen "grafische editor", maar precies het voorstel van Jet, al gebouwd, voor $10 per jaar.** (GEZIEN, beschrijving in `https://plugins.jetbrains.com/api/plugins/35167`)
- Gratis bij Graphlume: live voorbeeld met ingebouwde officiële Graphviz 16.1.0 (geen installatie), tekenen op de achtergrond na een pauze in het typen, "never blocks the editor", tijdslimiet bij te grote grafen, laatste goede plaatje blijft staan bij een fout, zoomen en slepen, licht en donker thema, aanvullen van alle attributen en kleuren, inspecties met snelle reparaties, ga naar declaratie, find usages, hernoemen, structuur, formatter, sjablonen.
- Pro bij Graphlume: "Linked preview" (klik op knoop of pijl springt naar de code, cursor op knoop licht op in het plaatje), alle 8 lay-outs (dot, neato, fdp, sfdp, circo, twopi, osage, patchwork) vanuit de werkbalk, export SVG, PNG (elke schaal) en PDF, kopiëren als plaatje, map exporteren, export bij elke opslag, DOT in Markdown, grote grafen (knoop zoeken en centreren, buren oplichten, vertraging en tijdslimiet instellen). Proef 7 dagen.
- Dat is vrijwel letterlijk het gratis deel én het Pro-deel uit `platformen/jetbrains/volgend-product.md`. Het enige uit Jets lijst dat ik niet terugzie is "voorbeeld in de kleuren van het IDE-thema" (Graphlume heeft wel licht en donker).
- Maker: KITSS TECH (`<vendor>KITSS TECH</vendor>` in plugin.xml, GEZIEN), dezelfde als BatchCraft.
- Prijs: $10 per jaar of $1 per maand persoonlijk, $10 per jaar zakelijk (GEZIEN, `https://plugins.jetbrains.com/api/marketplace/plugin/35167/prices?countryCode=US`). Dat is de helft van Jets $19 en een vijfde van $49.
- Downloads: 30 totaal, één versie (1.0.1, 18 okt 2026), dus ±43 per maand in de eerste 3 weken (GEZIEN, `/api/plugins/35167/updates`). 0 reviews, 0 sterrenstemmen (GEZIEN, `/comments` en `/rating`). Werkt vanaf 2024.3 zonder bovengrens (since 243.0, until leeg, GEZIEN), dus ook in 2026.3.
- **Waarom zo weinig:** (1) pas 3 weken oud; (2) Graphlume staat NIET in de aanraadlijst voor `*.dot` en `*.gv` (GEZIEN, `https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.dot`: DOT Language, DevTools, Dot Base, Dot Compat, Document Viewer, Dot Plus; voor `*.gv` alleen DOT Language, Dot Base, Dot Compat, Dot Plus). De oorzaak staat in zijn plugin.xml: `<fileType name="Graphviz DOT" ... implementationClass="com.kitsstech.graphlume.lang.DotFileType">` zonder `extensions=`, met het commentaar ".dot and .gv are claimed by the file type itself, only when nobody else owns them" (GEZIEN, zip gedownload van `https://plugins.jetbrains.com/files/35167/1197237/jetbrain-plugin-graphlume-1.0.1.zip`). De Marketplace ziet de bestandssoort dus niet en raadt hem niet aan. Let op: in het voorstel staat "Graphlume meldt `*.dot` wel aan"; dat klopt volgens deze meting niet. (3) Zoeken op "graphviz" in de Marketplace zet hem op plek 8 (GEZIEN, `searchPlugins?search=graphviz`).
- Gevolg (GOK): de 30 downloads zeggen weinig over betaalbereidheid, want bijna niemand ziet hem. Maar als KITSS TECH `extensions="dot;gv"` toevoegt (één regel), staat er morgen een product in de aanraadlijst dat alles van Jets plan heeft voor de helft van de prijs.

## A. JetBrains Marketplace: betaalde en freemium diagram-als-tekst plugins

Gezocht met `https://plugins.jetbrains.com/api/searchPlugins?max=20&offset=N&search=<woord>&pricingModels=PAID` en `=FREEMIUM` voor: diagram, plantuml, mermaid, d2, graphviz, dot, structurizr, drawio, draw.io, sequence, uml, flowchart, graph (168 verschillende treffers, de meeste niet over diagrammen). Daarna zonder prijsfilter: graphviz, dot studio, dot language, digraph, puml, er diagram, visualizer, c4, erd, chart. Details, versies en prijzen per id (GEZIEN, `/api/plugins/{id}`, `/api/plugins/{id}/updates?size=50`, `/api/marketplace/plugin/{id}/prices?countryCode=US`).

**Geen enkele betaalde of freemium plugin gevonden voor PlantUML, D2, draw.io/diagrams.net of Graphviz, behalve Graphlume.** PlantUML Integration (id 7017) is gratis met 5.092.275 downloads, Diagrams.net Integration (15635) gratis 500.434, D2 Diagram (29542) gratis 7.141 (GEZIEN, `searchPlugins`).

### Tekst-naar-diagram (het meest vergelijkbaar)
| Plugin (id) | Model | Prijs pers./zak. per jaar (US) | Downloads totaal | Per maand nu | Wat zit achter betaling |
|---|---|---|---|---|---|
| Mermaid Studio Core (30883) | freemium | $25 / $75 ($2,50 p.m.) | 26.831 | ±3.600 (10.859 in versies van laatste 90 dagen) | Interactieve editor in het voorbeeld, print en vector-PDF, MCP-tools, betere foutcontrole, inspecties, aanvullen, formatter, hernoemen, find usages, structuur, "Navigate from Preview: click diagram elements to jump to their declaration", Diagram Sync (export SVG/PNG bij opslaan), eigen icoonsets, eigen thema's en themagenerator. **Gratis**: live voorbeeld met zoom en zoeken, 8 thema's, export PNG en SVG, Markdown |
| Mermaid Studio (29870) | betaald | $49 / $149 ($4,90 p.m.) | 15.593 | ±1.200 (3.592 in 90 dagen) | alles van hierboven voor alle Mermaid-soorten (cijfer Jet ±1.680 al bekend, niet opnieuw bedoeld; mijn 90-dagenmaat komt lager uit) |
| Structurizr DSL (29351) | freemium | $99 / $99 ($9,90 p.m.) | 5.791 (sinds dec 2025) | ±485 (1.455 in 90 dagen) | niet te zien: de beschrijving noemt alle functies (aanvullen, inspecties, live C4-voorbeeld, export SVG/PNG/PlantUML/Mermaid) zonder scheiding gratis/betaald |
| Mermaid Companion (33340) | freemium | $29 / $89 | 1.305 (sinds 9 aug) | ±375 | export SVG, diagramthema's los van IDE-thema, export bij opslaan. Gratis: voorbeeld, zoom, PNG-export. Opvallend: hij heeft functies die gratis waren achter betaling gezet (thema's sinds 2026.2.0, SVG sinds 2026.3.0) |
| Mermaid Editor Pro (32363) | freemium | $50 / $50 ($5 p.m.) | 341 (sinds juni) | ±70 | extra thema's, klassen-editor, kleurpaletten, PDF en 4x transparante PNG, pijl-editor, knoopvormen, iconen, sjablonen. Gratis: voorbeeld, 4 thema's, export SVG en JPG |
| ZenUML Support (12437) | freemium | $10 / $20 | 41.627 | ±180 (versie mei 2025) | alleen: diagram maken uit Java-code. Taal en voorbeeld gratis |
| SequenceDiagram.org (23115) | betaald | $10 / $20 | 15.847 | ±270 (versie aug 2025) | alles (offline editor, export SVG/PNG, genereren uit Java) |
| DBML Pro (33740) | betaald | $25 / $35 | 185 (sinds 23 aug) | ±70 | alles (ER-diagram, export SVG/SQL/Prisma enz.) |
| Graphlume (35167) | freemium | $10 / $10 ($1 p.m.) | 30 (sinds 18 okt) | ±43 | zie hoofdvondst |

### Code-naar-diagram en visualisaties (minder vergelijkbaar, wel betaald)
| Plugin (id) | Model | Prijs pers./zak. | Totaal | Per maand nu | Achter betaling |
|---|---|---|---|---|---|
| SequenceDiagram Core (8286) | freemium | $10 / $20 | 1.572.173 | ±6.100 (17.228 op versie van 14 aug) | export als plaatje, export naar PlantUML en Mermaid, geen grens aan diepte, filters. Klik in diagram naar code is GRATIS |
| PolyBPMN visualizer (21361) | betaald | $19 / $39 | 65.542 | ±100 (307 in 90 dagen) | alles |
| Yaoqiang BPMN Editor (9739) | betaald | $49 / $490 | 89.166 | ±185 (versie juni 2025, until 252) | alles |
| JSON Schema Visualizer (23554) | betaald | $20 / $40 | 3.446 | ±75 (versie nov 2024) | alles |
| XSD / WSDL Visualizer (18425) | freemium | $25 / $25 | 37.941 | versie 9 dagen oud, niet betrouwbaar | niet nagekeken |
| Markdown Preview Plus (34045) | freemium | $30 / $70 | 279 | ±125 | niet precies nagekeken (PDF/HTML-export, Mermaid in voorbeeld) |
| Docker Compose Visualizer (33475) | freemium | $19 / $29 | 247 | ±130 | bewerken in het diagram, toevoegen en verbinden, snelle reparaties |
| ASL State Machine Graph (35145) | betaald | $2 p.m. | 57 | ±75 | alles |
| Oskuvi Class Diagrams (35127) | betaald | $29 / $49 | 40 | ±50 | alles |
| CodeLens UML (31421) | betaald | $3 p.m. | 43 | ±15 | alles |
| Code2Graph (35149) | freemium | $15 / $30 | 38 | te jong | ER-diagrammen uit database; 6 tekenmotoren (o.a. Graphviz) en klik-naar-regel zijn GRATIS |

### Welke betaalde functies keren terug (uit de tabellen hierboven, GEZIEN)
- **Export**: basis-export PNG/SVG is meestal GRATIS (Mermaid Studio Core, Mermaid Companion PNG, Mermaid Editor Pro SVG/JPG, DOT Studio). Betaald is "meer export": PDF (Mermaid Studio Core, Mermaid Editor Pro, Graphlume), export bij elke opslag (Mermaid Studio Core, Mermaid Companion, Graphlume), SVG (Mermaid Companion), export naar andere formaten (SequenceDiagram Core). Export van een plaatje achter betaling: SequenceDiagram Core, Graphlume.
- **Klik in voorbeeld naar de bron**: betaald bij Mermaid Studio Core en Graphlume. Gratis bij SequenceDiagram Core en Code2Graph.
- **Thema's**: betaald bij 3 van de 4 Mermaid-plugins (eigen thema's en generator bij Mermaid Studio Core, thema's bij Mermaid Companion, extra thema's bij Mermaid Editor Pro). Een paar standaardthema's zijn steeds gratis.
- **Slim bewerken** (aanvullen, inspecties, hernoemen, formatter): betaald bij Mermaid Studio Core; gratis bij Graphlume.
- **Bewerken in het plaatje zelf**: betaald bij Mermaid Studio Core, Mermaid Editor Pro, Docker Compose Visualizer.
- **Lay-outs**: alleen Graphlume (is Graphviz-eigen; Mermaid heeft dat niet als betaalde functie).
- Prijzen: van $10 per jaar (Graphlume, ZenUML, SequenceDiagram) tot $99 per jaar (Structurizr DSL). De plugins met de meeste downloads per maand vragen $10 tot $49 persoonlijk.

## B. DOT Studio (id 34732): wat geeft hij gratis

Bron: beschrijving (GEZIEN, `https://plugins.jetbrains.com/api/plugins/34732`), broncode (GEZIEN, `git clone --depth 1 https://github.com/acalebratliff/dot-studio`, laatste commit 24bfbd1 van 2 okt 2026 "release: DOT Studio 1.0.0"), CHANGELOG.md en DECISIONS.md uit die repo. GitHub-API voor sterren en issues was dicht in deze sessie (403), dus sterren en issues niet gemeten.

Cijfers: 109 downloads, één versie 1.0.0 van 3 okt 2026, ±90 per maand; geen reviews of stemmen; werkt van 2025.2 tot 2026.2 (until 262.\*), dus niet in 2026.3 (GEZIEN, `/updates`, `/comments`, `/rating`). Licentie Apache-2.0. Maker "Mendworks".

| Functie | DOT Studio gratis? | Bewijs |
|---|---|---|
| Kleuren, syntaxfouten, `->` in `graph` als fout, folding, haakjes, commentaar | ja | CHANGELOG 1.0.0 |
| Structuurvenster (subgrafen, knopen, pijlen), klik zet cursor | ja | CHANGELOG |
| Live voorbeeld zonder Graphviz te installeren (viz-js in JCEF, Web Worker met tijdslimiet) | ja | CHANGELOG, DECISIONS |
| Export SVG en PNG (1x of 2x) | **ja** | CHANGELOG |
| Export PDF | nee | nergens genoemd |
| Zoomen en slepen | **ja** | CHANGELOG |
| Andere lay-outs | **alleen via `layout=` in de DOT**; een keuzemenu is bewust geschrapt ("Build zoom/pan; drop picker", besluit van de eigenaar) | DECISIONS |
| Thema | de pagina volgt het IDE-thema, maar de graaf blijft een witte kaart met Graphviz-kleuren (bewuste keuze) | CHANGELOG, DECISIONS |
| Klik op knoop springt naar regel | **nee**. In de bron geen klikafhandeling van het plaatje naar de editor; de enige "navigation" in de code is het blokkeren van webnavigatie in de ingebouwde browser | grep in `src/` op click/navigat/jump/caret |
| Zoeken in de graaf | nee | grep, niet genoemd |
| Aanvullen, ga naar definitie, hernoemen, find usages | nee | grep, niet genoemd |
| DOT in Markdown, export bij opslaan | nee | niet genoemd |

Achtergrond (GEZIEN, DECISIONS.md): DOT Studio is gebouwd "as a distribution probe", met de opdracht "let's keep an eye on differentiation if another copy or paid plugin shows up". Het is dus een proef om bereik te testen, door een ploeg die net als wij werkt (CLAUDE.md in de repo). Ze letten op concurrentie. GOK: ze kunnen snel bijwerken voor 2026.3 en functies toevoegen.

Wat een Pro dus moet overtreffen: van Jets Pro-lijst geeft DOT Studio export SVG/PNG en zoomen al gratis, en lay-outs half (via `layout=`). Wat overblijft als echt verschil met DOT Studio: klikbaar voorbeeld, PDF, lay-out kiezen met één klik, zoeken en buren oplichten in grote grafen, graaf in themakleuren. Maar al die dingen heeft Graphlume (behalve themakleuren) voor $10.

## C. Buiten JetBrains

### VS Code Marketplace (GEZIEN)
POST `https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery`, header `Accept: application/json;api-version=3.0-preview.1`, filterType 10 "graphviz", filterType 8 VS Code. 61 treffers. Het prijsveld `Microsoft.VisualStudio.Services.Content.Pricing` (opgevraagd met flags 951): 51 keer "Free", 10 keer leeg (= gratis). **Geen enkele betaalde of proef-extensie voor Graphviz.**

Grootste Graphviz-extensies (installs, aantal beoordelingen, laatst bijgewerkt):
| Extensie | Installs | Beoord. | Laatst | Opmerking |
|---|---|---|---|---|
| tintinweb.graphviz-interactive-preview | ±555.000 (554.939 en bij de controleur 554.898) | 24 | okt 2022 | gratis: zoom, zoeken, klik op knoop licht in- en uitgaande pijlen op, export SVG en DOT |
| joaompinto.vscode-graphviz | 290.497 | 14 | nov 2023 | taal en voorbeeld (staat als "unpublished") |
| Stephanvs.dot | 211.410 | 3 | dec 2015 | taal |
| EFanZh.graphviz-preview | 188.956 | 4 | mrt 2025 | voorbeeld |
| geeklearningio.graphviz-markdown-preview | 58.812 | 4 | 2019 | DOT in Markdown |
| qiu.graphviz-language-support-and-preivew | 10.777 | 2 | 2023 | |
| ijmacd.graphviz-previewer-web | 8.270 | 0 | 2024 | |
| zovo.zovo-graphviz-preview | 5 | 0 | 8 nov 2026 | gratis (MIT): "click a node to jump to its line", zoeken, export SVG/PNG, geen Graphviz nodig |
| LukasMaag.graphviz-interactive | 27 | 0 | okt 2026 | gratis: zoeken, dubbelklik toont knoop in de DOT, pijlen volgen |
| nifty.nifty-diagrams | 53 | 0 | okt 2026 | gratis: PlantUML, DOT, D2, export SVG/PNG |

Les (GEZIEN): in VS Code zijn zoeken en export gratis bij de grote extensie; klik-naar-regel is er ook gratis, maar alleen bij piepkleine extensies (zovo 5, LukasMaag 27 installs). Het grootste Graphviz-gereedschap daar (±555.000 installs, klik licht alleen pijlen op, springt niet naar de regel) is gratis en sinds 2022 niet bijgewerkt. Niemand vraagt daar geld voor DOT.

### Apple App Store (GEZIEN)
`https://itunes.apple.com/search?term=graphviz&entity=macSoftware` en `&entity=software`, ook "dot graph", "graphviz editor", "dot language", "graph galaxy", "instaviz", "graphviz viewer" (country=us).
- Geen Mac- of iOS-app gevonden die een Graphviz/DOT-editor is en geld vraagt met zichtbare beoordelingen.
- Wel Graphviz in de beschrijving: ged2dot ($2,99, stamboom naar DOT, 0 beoordelingen, `https://apps.apple.com/us/app/ged2dot/id1074600198`), Snow Flower Text ($49,99, teksteditor die Graphviz noemt, 0 beoordelingen, `https://apps.apple.com/us/app/snow-flower-text/id1046643990`), Graph Editor (gratis, 4 beoordelingen, `https://apps.apple.com/us/app/graph-editor/id1597638443`).
- Graph Galaxy en Instaviz (beide op graphviz.org genoemd) zijn niet te vinden in de US-store.
- Let op: de iTunes-zoek-API geeft voor Mac-apps vaak 0 beoordelingen, ook bij grote apps (bijv. OmniGraffle 7: 0). Aantallen voor Mac zijn dus niet betrouwbaar te meten via deze weg.

### Andere betaalde DOT-gereedschappen of webdiensten
- graphviz.org/resources (GEZIEN, `https://graphviz.org/resources/`): de lijst van editors en viewers is vrijwel helemaal gratis of open source; geen prijzen genoemd.
- Gravizo (`https://www.gravizo.com/`, GEZIEN): Graphviz/PlantUML-plaatjes voor README's, gratis, met zakelijke abonnementen €9,99 en €19,99 per maand voor vertrouwelijkheid, eigen domein en on-premise. Betalen voor privacy en hosting, niet voor bewerken. Aantal klanten niet te zien.
- sketchviz.com en edotor.net: geen prijs gevonden op de pagina (GEZIEN, curl; de pagina's zijn grotendeels JavaScript, dus mogelijk gemist).
- Niet gemeten: betaalde DOT-functies in grote pakketten (bijv. OmniGraffle, yEd, Mathematica die DOT importeren). Daar betaalt men voor het pakket, niet voor DOT.

## Conclusie

**Punt 2 (Pro moet duidelijk verder gaan dan DOT Studio):** tegen DOT Studio alleen haalbaar. DOT Studio heeft geen klik-naar-regel, geen PDF, geen zoeken, geen aanvullen of hernoemen, geen lay-outknop en werkt niet in 2026.3 (GEZIEN). Maar export SVG/PNG en zoomen moeten dan uit de Pro-lijst als verkoopargument, want die zijn bij DOT Studio gratis. Het echte probleem is Graphlume: die heeft Jets volledige gratis deel én bijna het volledige Pro-deel, werkt in 2026.3, kost $10 per jaar, en wordt alleen nog niet aangeraden door een fout van één regel. Dus "duidelijk verder gaan" moet gelden tegen Graphlume, en daar blijft alleen "graaf in IDE-themakleuren" over (GOK dat dat niemand $19 waard is). In VS Code is zoeken gratis bij de grote extensie en klik-naar-regel alleen bij extensies met minder dan 30 installs (GEZIEN); dat ondergraaft zoeken als betaalreden, klik-naar-regel veel minder.

**Punt 3 (bewijs dat iemand voor DOT betaalt):** niet gevonden. JetBrains: alleen Graphlume, 30 downloads, onzichtbaar in de aanraadlijst. VS Code: 61 Graphviz-extensies, allemaal gratis. App Store: geen betaalde DOT-editor. Web: alleen Gravizo, voor privacy. Wat wel vaststaat: mensen downloaden betaalde en freemium diagram-als-tekst-plugins in JetBrains (Mermaid Studio ±1.200 per maand betaald, Mermaid Studio Core ±3.600, Structurizr DSL ±485 voor $99 per jaar, SequenceDiagram Core ±6.100), en een Mermaid Studio-reviewer schrijft over "the year sub I paid". Maar downloads zijn geen verkopen, en voor PlantUML, D2, draw.io en Graphviz betaalt niemand zichtbaar: daar winnen gratis plugins.

**Sterkste punten voor het voorstel:** de vraag naar DOT in JetBrains is groot en de oude plugins zijn kapot (al bekend); Mermaid laat zien dat freemium met klik-naar-bron, PDF, export bij opslaan en thema's in deze markt verkoopt; DOT Studio is zwak in code-gemak en niet in 2026.3.
**Zwakste punten:** (1) Graphlume is al Jets product, voor de helft van de prijs; (2) nergens één bewezen DOT-betaler; (3) in VS Code is alles wat Jet als Pro wil gratis; (4) een gratis open-source concurrent (DOT Studio) die op concurrentie let.

GOK, advies: punt 3 is niet gehaald en is met openbare cijfers ook niet te halen. De enige echte meting die nog kan: Graphlume over een paar weken volgen (downloads per dag), vooral als KITSS TECH de aanraadlijst haalt. Groeit hij dan met honderden per maand, dan is er vraag naar een betaalde DOT-plugin, maar is de plek ook bezet.


## Controleur (8 nov ±16:05 UTC)
Akkoord mits. Alle zes punten opnieuw gemeten en GEKLOPT (Graphlume prijs en functies, niet in de aanraadlijst door plugin.xml zonder `extensions=`, DOT Studio, vier per-maand-schattingen nagerekend, tintinweb, punt 3 niet gevonden; zelf ook Kroki, Edotor, sketchviz, GraphvizOnline en de App Store doorzocht: geen betaald DOT-plan). Moet: klik-naar-regel in VS Code alleen bij extensies onder 30 installs, de grote licht alleen pijlen op (verwerkt hierboven); Jets tabel over Graphlume is fout (advies 22, ik schrijf niet in `platformen/jetbrains/`). Kan: Structurizr is ±485 per maand met de 90-dagenmaat en ±790 op de nieuwste versie (700 in 27 dagen); installs tintinweb als ±555.000 (verwerkt).
