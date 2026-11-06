# JetBrains: marktmeting 6 nov 2026 (16:00 UTC)

**Hoe gemeten:** de Marketplace-API (`/api/searchPlugins`, velden downloads, rating en pricingModel) via de leestool (WebFetch), niet via curl. Het cijfer in de tabellen is het veld rating uit die zoekresultaten. Toen kregen curl en Gradle nog 403. Sinds ±16:00 UTC werkt curl wel. Voortaan meten met curl, nooit met WebFetch (regel in CLAUDE.md). Alle cijfers hieronder zijn GEZIEN, tenzij anders vermeld. Downloads zijn opgeteld over de hele levensduur van een plugin en tellen ook proefversies mee. Aantal betalers is nergens te zien.

## Totalen (GEZIEN)
- Betaalde plugins (PAID): 539 bij zoeken gesorteerd op downloads (16:00 UTC), 533 bij een tweede telling door de controleur zonder sortering (±16:00 UTC). Het verschil is niet verklaard. Freemium: 243.
- Ter vergelijking: in juli 2020 waren er 46 betaalde plugins ([JetBrains-blog](https://blog.jetbrains.com/platform/2020/07/one-year-of-paid-plugins-on-the-marketplace/), DERDEN).

## Wat verkoopt: de betaalde top 48 op downloads (GEZIEN)
Twee groepen vallen op.

**1. Taalondersteuning voor een bestandssoort die de IDE zelf niet goed kent.** 9 van de 48 zijn zo'n taalplugin (SystemVerilog Studio staat buiten de top 48, gevonden via zoeken):

| Plugin | Downloads | Cijfer |
|---|---|---|
| BashSupport Pro | 620.266 | 4,91 |
| OrchidE (Ansible) | 355.450 | 3,08 |
| Nginx Configuration Pro | 268.231 | 4,41 |
| Jenkinsfile | 162.049 | 4,17 |
| Wolfram Language | 132.469 | 4,81 |
| Firebase Rules | 129.902 | 4,51 |
| CMake Plus | 58.892 | 4,44 |
| Qt Style Sheets Editor | 39.718 | 3,56 |
| RDF and SPARQL | 37.384 | 4,77 |
| SystemVerilog Studio | 13.039 | 4,41 |

Eén maker (`co.anbora.labs`) heeft er meerdere: KS-Explorer, Jenkinsfile, Firebase Rules, JMeter, IReport 6.

**2. Koppelingen met een dienst:** Redis, DynamoDB, Elasticsearch, Bitbucket, GitLab, Hybris, AEM. Die vragen een eigen backend-kennis per dienst en vallen voor ons af als eerste product.

## Controle kandidaat C (visuele editor), stap 3 uit `kandidaten.md`
Eis: minstens 3 betaalde visuele editors met elk meer dan 5.000 downloads. **Gehaald** (GEZIEN):

| Plugin | Downloads | Cijfer |
|---|---|---|
| Yaoqiang BPMN Editor | 89.158 | 3,84 |
| PolyBPMN visualizer | 65.458 | 4,82 |
| JFormDesigner | 52.460 | 3,66 |
| SequenceDiagram.org | 15.839 | 3,80 |
| Mermaid Studio | 15.441 | 4,29 |
| IReport 6 | 7.420 | 4,40 |

Maar bij diagrammen is gratis aanbod groot: plantuml4idea 5.089.819, Diagrams.net Integration 499.736, Excalidraw Integration 48.439, ERD Editor 32.937, Penstock (BPMN) 30.251. Allemaal FREE.

## Bestandssoorten nagelopen (GEZIEN, alle prijsmodellen)
- **DBML:** 5 plugins, de grootste 5.272 downloads (gratis). Eén betaalde, DBML Pro: 184 downloads. Klein.
- **JSON Schema visueel:** JSON Schema Visualizer/Editor, betaald, 3.443 downloads, cijfer 3,02. Klein of slecht gemaakt, niet te zeggen welke van de twee.
- **OpenAPI visueel:** OpenAPI GUI Editor, betaald, 2.269. De gratis teksteditors halen 0,7 tot 10,7 miljoen.
- **XState / statemachines:** vrijwel niets (xstate: 1 resultaat, 154 downloads). Geen bewijs van vraag.
- **Excalidraw, draw.io, PlantUML, Protobuf, GraphQL, Terraform, Kubernetes, Docker Compose:** goed gedekt door gratis plugins, vaak van JetBrains zelf.

## Conclusie
- Betaalde taalondersteuning heeft meer bewijs dan betaalde visuele editors: 10 plugins tussen 13.000 en 620.000 downloads, tegen 6 tussen 7.000 en 89.000.
- Kanttekeningen: de taalgroep is breder gekozen dan de editorgroep, downloads tellen over de hele levensduur (oude plugins hebben voorsprong), en het gratis aanbod naast de taalplugins is nog niet gemeten. Dat laatste moet in de volgende meting.
- Taalondersteuning heeft geen JCEF nodig en past in de standaard testopzet van IntelliJ (GOK: alleen een lege plugin is gebouwd, zie `bouwsjabloon.md`).
- Onbekend blijft hoeveel van die downloads betalen. De oudste klant van BashSupport Pro had in 2020 een klantnummer onder de 11.000 ([plugin-dev.com](https://www.plugin-dev.com/intellij/general/marketplace-stats/), DERDEN), dat zegt weinig over het aantal betalers nu.

## Volgende meting
Kies een taal of bestandssoort voor kandidaat D: zoek per soort (bijvoorbeeld Caddyfile, Justfile, HAProxy, systemd units, Earthfile, Nix, Helm-templates, Ansible-alternatieven, PowerShell DSC) het aantal plugins, downloads en of er een betaalde is. Meet ook het grootste gratis alternatief naast de bestaande betaalde taalplugins (bijvoorbeeld bij Bash en Nginx). Kies er één waar gratis ondersteuning ontbreekt of slecht is (cijfer onder 3,5), en waar ontwikkelaars veel mee werken.

## Meting D, deel 1 (16:12 UTC, met curl)
Zoekopdracht per soort, top 6 op downloads, alle prijsmodellen (GEZIEN). Alleen wat ertoe doet:

**Betaald naast gratis levert in 2 gevallen een tiende tot een twintigste op** (leeftijd niet gemeten):
- Bash: gratis BashSupport 14.499.118, betaald BashSupport Pro 620.266.
- Nginx: gratis Nginx Configuration 2.762.004 en nginx Support 276.860, betaald Nginx Configuration Pro 268.231.

**Waarschuwing: nieuwe betaalde taalplugins halen weinig.** Een reeks "Pro"-plugins voor kleine talen staat laag: Mojo Pro 3.001, Flexible Haskell 2.671, Nix Pro 1.463, Caddyfile Pro 769, Elixir Pro 489, Gleam Pro 86, Nim Pro 49. Hun leeftijd is nog niet gemeten, dus per maand is onbekend.

**Veel gebruikt, maar de gratis plugin scoort slecht (cijfer onder 3,5):**

| Soort | Gratis plugin | Downloads | Cijfer | Betaald ernaast |
|---|---|---|---|---|
| Liquid (Shopify, Jekyll) | Liquid | 328.663 | 2,61 | Liquid Hero 3.350, Liquid for Shopify & Jekyll 598 |
| Caddyfile | Caddyfile support (en Caddyfile: 16.136, cijfer 4,55) | 94.403 | 2,55 | Caddyfile Pro 769 |
| Bicep (Azure) | Bicep | 92.193 | 2,29 | geen in top 6 |
| Jsonnet | Jsonnet (en Jsonnet Language Server: 51.972, cijfer 4,56) | 68.617 | 2,42 | geen in top 6 |
| Arduino | Arduino Support | 48.724 | 3,35 | Flexible For Arduino (freemium) 13.304 |

**Goed gedekt door gratis (cijfer 4 of hoger, of van JetBrains zelf):** Just, systemd, Nix, Helm values, Zig, Nim, Solidity, Makefile, Terraform, Twig, Ini, Toml.

**Te klein (grootste plugin onder 5.000):** HAProxy, Earthfile, KDL, Gleam, Cairo, Typst, Pkl, G-code.

## Tussenstand D
- Kortste lijst: Liquid, met Caddyfile als reserve. Jsonnet valt af, want Jsonnet Language Server (gratis, cijfer 4,56) dekt het goed. Caddyfile heeft ook een goede gratis tweede plugin, dat maakt het zwakker. Bicep valt af, want Microsoft maakt zelf Bicep-gereedschap (GOK, niet nagekeken).
- Liquid springt eruit: de meeste gebruikers (328.663, ruim 3 keer de nummer 2), een laag cijfer (2,61) en geen goede gratis plugin ernaast. Wel heeft de betaalde Liquid Hero al cijfer 4,64 en 3.350 downloads. Maar dat zij klein zijn kan ook betekenen dat niemand betaalt.
- Nagekeken door een controleur (16:13 UTC): cijfers klopten, tekst daarna verbeterd op 4 punten.
- Nog te doen voor het bouwbesluit: leeftijd (eerste uitgave) van Liquid Hero, Caddyfile Pro en de andere Pro-plugins, zodat downloads per maand te zien zijn, en de reviews van de gratis Liquid-plugin lezen om te zien wat er mist.

## Meting D, deel 2: leeftijd en downloads per maand (16:14 UTC, met curl)
Leeftijd = datum van de oudste versie in `/api/plugins/{id}/updates`. Het veld `cdate` van de plugin zelf is niet de startdatum (BashSupport Pro gaf daar 2026, terwijl hij in 2020 begon). Downloads per maand = alle downloads gedeeld door het aantal maanden, dus een gemiddelde (GEZIEN, rekensom eigen).

| Plugin | Soort | Eerste versie | Downloads | Per maand |
|---|---|---|---|---|
| BashSupport Pro | taal, oud | 2020-06 | 620.266 | 8.038 |
| Nginx Configuration Pro | taal, oud | 2021-12 | 268.231 | 4.599 |
| Mermaid Studio | diagram met voorbeeld | 2026-01 | 15.441 | 1.682 |
| Mojo Pro | taal, nieuw | 2026-05 | 3.001 | 567 |
| Nix Pro | taal, nieuw | 2026-05 | 1.463 | 250 |
| Liquid Hero | taal | 2025-07 | 3.350 | 208 |
| Caddyfile Pro | taal, nieuw | 2026-07 | 769 | 196 |
| Liquid for Shopify & Jekyll | taal, nieuw | 2026-07 | 598 | 175 |
| SystemVerilog Studio | taal, oud | 2020-05 | 13.039 | 167 |
| Gleam Pro | taal, nieuw (pas 1 maand oud) | 2026-10 | 86 | 86 |

Ter vergelijking, gratis: Caddyfile support (eerste versie 2025-05) haalt 5.334 per maand.

**Belangrijk (GEZIEN):** de gratis Liquid-plugin (id 14388) is van JetBrains zelf. Mojo Pro, Nix Pro, Gleam Pro, Elixir Pro en Nim Pro zijn allemaal van één maker (`jetplugins`), die in 2026 een hele reeks betaalde taalplugins uitbrengt.

## Tussenstand na deel 2
- De grote betaalde taalplugins bestaan al lang. Misschien komt hun voorsprong daardoor (GOK). Nieuwe betaalde taalplugins uit 2026 halen 86 tot 567 downloads per maand.
- Mermaid Studio, uit januari 2026 en van soort C, haalt 1.682 per maand: drie keer de beste nieuwe taalplugin. Eén voorbeeld, dus geen wet.
- Liquid wordt zwakker: we zouden concurreren met de eigen plugin van JetBrains, en Liquid Hero haalt na 16 maanden maar 208 per maand.
- **Besluit: geen bouwbesluit. Richting D is niet meer de voorkeur. C en D staan weer naast elkaar.** Reden: het bewijs voor D kwam van oude plugins, en dat voordeel hebben wij niet.
- Nagekeken door een controleur: akkoord, twee kleine punten verwerkt.
- Volgende meting: alle betaalde en freemium plugins met een eerste versie in 2025 of 2026, gerangschikt op downloads per maand. Dan zien we welk soort nieuw betaald product nu groeit.

## Meting deel 3: nieuwe betaalde en freemium plugins (16:16 UTC, met curl)
**Hoe:** alle betaalde en freemium plugins opgehaald (891 stuks bij doorbladeren, meer dan de 539 plus 243 die de zoekfunctie als totaal gaf; niet verklaard). Daarvan 355 met minstens 1.000 downloads. Per plugin de oudste versie opgezocht. **Valkuil:** sommige makers verwijderen oude versies (Bitbucket Integration Pro, id 13538, lijkt uit juli 2026 maar heeft een laag id en bestaat dus veel langer). Daarom alleen geteld: id vanaf 27000 (rond 2025 aangemaakt, GOK op basis van Liquid Hero 27826 uit juli 2025) en oudste versie vanaf januari 2025. Dat geeft 102 plugins (GEZIEN).

**Nieuwe plugins die een bestandssoort openen die de IDE zelf niet kan tonen (per maand, GEZIEN):**

| Plugin | Model | Sinds | Downloads | Per maand |
|---|---|---|---|---|
| Omni Viewer | freemium | 2025-09 | 62.355 | 4.635 |
| Mermaid Studio Core | freemium | 2026-04 | 26.433 | 3.808 |
| Hex Editor | freemium | 2025-09 | 47.267 | 3.479 |
| SQLite Lens | freemium | 2026-08 | 5.209 | 2.057 |
| Mermaid Studio | betaald | 2026-01 | 15.441 | 1.682 |
| XLSX Lens | freemium | 2026-08 | 3.618 | 1.447 |
| Notebook Lens | freemium | 2026-08 | 2.304 | 973 |
| Heap Dump Lens | freemium | 2026-08 | 1.649 | 727 |
| JSONL Lens | freemium | 2026-08 | 1.880 | 635 |
| DuckDB Lens | freemium | 2026-08 | 1.383 | 592 |

Onder 590 per maand staan nog meer nieuwe viewers: PRISM Log Viewer 467, Log Lens 457, Mermaid Companion 438, Parquet Lens 506 (GEZIEN). Vijf van de Lens-plugins zijn van één maker, twilight-ventures (GEZIEN, 5 nagekeken). Die zijn allemaal pas ±3 maanden oud, dus hun cijfer per maand is nog onzeker.

**Nieuwe taalplugins, ter vergelijking (GEZIEN):** BatchCraft (Windows batch, betaald, pas 1 maand) 8.879 per maand, Flexible Swift 1.887, Flexible For Arduino 1.847, Firebase Pro 1.105, Jinja2 Enhanced Support 1.048, Google Apps Script Support 990, Flexible Julia 841, LaTeX Pro 771, Ansible Pro 767, Serverless Insight 754, Robot Framework Professional 610, AsciiDoc Pro 597. In de telling zitten meer nieuwe taalplugins dan nieuwe viewers.

**Losse zoektocht naar bestandssoorten (GEZIEN):** Word (docx): Document Viewer 36.509 downloads, cijfer 3,11. Parquet en Avro: goed gedekt door gratis plugins (Avro and Parquet Viewer 225.192, cijfer 4,77). PDF: PDF Viewer 413.292, cijfer 4,43. Pcap: alleen Omni Viewer en een binaire inspecteur.

## Tussenstand na deel 3
- Nieuwe viewers en nieuwe taalplugins halen ongeveer dezelfde aantallen: ruwweg 450 tot 4.600 per maand voor viewers, 600 tot 1.900 voor taalplugins, met BatchCraft als uitschieter na 1 maand. Er is geen duidelijk verschil.
- Bijna alle nieuwe viewers zijn freemium. Dat steunt freemium als model.
- Een groot deel van de nieuwe viewers komt van één maker (twilight-ventures). Wie een viewer maakt, concurreert direct met die reeks.
- **Besluit: nog geen voorkeur tussen C-breed (viewer of editor voor een bestandssoort die de IDE niet kent) en D (taalondersteuning). Wel: freemium.** Geen bouwbesluit.
- Of een viewer goed te bouwen is met JCEF of een eigen Swing-weergave is een GOK, nog niet geprobeerd.
- Kansen om na te lopen: Word (gratis Document Viewer, cijfer 3,11), soorten die Omni Viewer en de Lens-reeks nog niet doen, en waarom BatchCraft zo snel groeit.
- Nagekeken door een controleur: cijfers klopten, de vergelijking was eerst te scheef. Verbeterd volgens zijn punten.

## Meting deel 4: mogelijke reden dat BatchCraft snel groeit (16:20 UTC, met curl)
- BatchCraft (betaald, 7 dagen proef, maker kitss-tech) haalt 9.054 downloads sinds zijn oudste versie in oktober 2026 (GEZIEN, zie deel 3).
- Voor `.bat` en `.cmd` bestonden al twee gratis plugins met veel downloads, maar beide zijn verlaten: Batch Scripts Support, 2.061.264 downloads, laatste versie december 2021, en CMD Support, 2.245.589 downloads, cijfer 2,6, laatste versie maart 2015 (GEZIEN).
- **Werkhypothese (GOK):** een betaalde, moderne vervanger voor een verlaten gratis plugin met veel downloads kan snel groeien, omdat de gebruikers er al zijn en niemand ze bedient. Dit is één voorbeeld.

Andere zwakke gratis plugins nagekeken (laatste versie, GEZIEN; cijfers uit de zoekresultaten van deel 1 en de zoekterm cmd en applescript). Nagekeken door een controleur: downloads en datums klopten, de kop was eerst te stellig.

| Plugin | Downloads | Cijfer | Laatste versie | Maker |
|---|---|---|---|---|
| AppleScript Support | 82.447 | 3,84 | okt 2021 | onbekende maker |
| Jsonnet | 68.617 | 2,42 | mrt 2024 | onbekende maker (gratis Jsonnet Language Server bestaat wel) |
| Document Viewer (Word) | 36.509 | 3,11 | aug 2026 | Syncfusion, wordt onderhouden |
| SimpleSqliteBrowser | 488.055 | 3,03 | apr 2026 | wordt onderhouden |
| Caddyfile support | 94.403 | 2,55 | jul 2026 | wordt onderhouden |
| Liquid, Blade, R Language, Big Data File Viewer | 0,3 tot 4,2 miljoen | 2,61 tot 3,28 | okt 2026 | JetBrains zelf, dus niet tegen concurreren |

## Volgende stap
Zoek systematisch (met curl) gratis plugins met meer dan 100.000 downloads, niet van JetBrains, waarvan de laatste versie ouder is dan 2 jaar, voor een taal of bestandssoort die nog veel gebruikt wordt, en waar nog geen goede nieuwe vervanger is. Dat is het bouwbesluit: kies er één, freemium.

## Meting deel 5: verlaten gratis plugins (16:21 UTC, met curl, afgemaakt in deel 6)
- Gratis plugins met minstens 100.000 downloads: 870. Daarvan niet van JetBrains en laatste versie voor november 2024: 219 (GEZIEN). De hele lijst staat in `data/verlaten-gratis-2026-11-06.tsv`.
- Veel daarvan zijn al vervangen: CodeGlance (1.758.526, laatst 2018) door CodeGlance Pro (4.691.766, gratis), Thrift Support (361.136, laatst 2022) door een gratis fork (199.360, cijfer 4,69), Robot Framework-plugins door nieuwe, Ansible door OrchidE en Ansible Pro (GEZIEN).
- Batch en CMD zijn nu door BatchCraft genomen.
- Eerste kandidaat zonder zichtbare vervanger in de top 6: **Git Flow Integration**, 682.493 downloads, cijfer 4,37, laatste versie augustus 2021 (GEZIEN). Of git flow nog veel gebruikt wordt is niet gemeten.
- Volgende run: de 219 aflopen, per stuk kijken of er een nieuwe vervanger is, en of de taak of taal nog leeft. Daarna één kiezen.

## Meting deel 6: waarom BatchCraft groeit, en wat dat zegt (17:00 tot 17:10 UTC, met curl)

**1. Welke van de 219 werken niet meer in een nieuwe IDE (GEZIEN).** Per plugin de nieuwste versie opgehaald en gekeken tot welke IDE-versie hij werkt (`until`). 76 van de 219 werken niet in IDE 2025.2 of nieuwer, 138 hebben geen bovengrens, 5 werken nog net. Lijst: `data/verlaten-gratis-compat-2026-11-06.tsv`. Voorbeelden: Git Flow Integration (682.493, werkt tot 2021.2), Git Flow Integration Plus (109.574, tot 2024.1), Luanalysis (155.671, tot 2023.3), GDScript (111.825, tot 2024.2), Minecraft NBT Support (101.777, tot 2022.3), RESTFul-Tool (621.552, tot 2024.1).

**2. Wie zit er al in die gaten (GEZIEN).**
- Git flow: de grootste nieuwe uit 2026 is Git Flow Helper (9.448 downloads in totaal). Er zijn ook onderhouden oudere plugins: GitFlowPlus (24.561, bijgewerkt maart 2026) en GitFlowTools (10.260, augustus 2026). Bezet, en geen uitschieter.
- Lua: JetBrains bracht in november 2026 zelf een Lua-plugin uit (id 34924), en EmmyLua (1.013.855) wordt onderhouden. Lua valt af.
- Pascal: twee nieuwe freemium plugins in oktober en november 2026 (Pascal Flow van meanmail.dev, Pasforge van KITSS TECH).
- GDScript: de nieuwste plugin werkt tot 2025.1. Niet verder uitgezocht, Rider heeft eigen Godot-steun (niet gemeten).

**3. De maker van BatchCraft deed precies onze hypothese, 27 keer (GEZIEN).** KITSS TECH zette in oktober 2026 27 plugins op de Marketplace (`data/maker-kitss-tech-2026-11-06.tsv`). BatchCraft heeft er 9.054. De andere 26 hebben 16 tot 379 downloads. Daaronder zitten ook vervangers van verlaten plugins met veel downloads: Pinwise voor Python requirements (de oude Requirements-plugin heeft 2.968.692) heeft 43, Pasforge voor Pascal (I-Pascal 151.908) heeft 31, Rolewise voor Ansible (YAML/Ansible support 724.027) heeft 379, Graphlume voor DOT (DOT Language 154.562, laatste versie augustus 2024) heeft 29. Alle 27 namen nagelopen tegen de 219: dit zijn de vijf die een plugin uit die lijst vervangen. **De werkhypothese uit deel 4 klopt dus niet zoals hij er stond:** een verlaten gratis plugin met veel downloads vervangen geeft geen groei vanzelf. 1 van de 5 vervangers van KITSS groeide, met eerste versies tussen 5 en 15 oktober 2026.

**4. Wat BatchCraft wel anders heeft (GEZIEN, de reden is een GOK).** De IDE raadt zelf plugins aan als je een bestand opent dat hij niet kent. De lijst die hij toont komt van de Marketplace: `https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.bat`. Voor `*.bat` geeft die precies drie plugins: CMD Support (laatste versie 2015), Batch Scripts Support (2021) en BatchCraft (GEZIEN). Elk Gradle-project heeft een `gradlew.bat` en elk Maven-project met wrapper een `mvnw.cmd` (GOK dat bijna elk project die heeft, wel zeker dat Gradle hem standaard maakt). In een test met IntelliJ IDEA 2026.2 en 2025.2 Community is `gradlew.bat` een onbekend bestand (GEZIEN, `data/ide-bestandssoort-test-2026-11-06.tsv`). Dus: wie een Java- of Android-project opent en `gradlew.bat` aanklikt, krijgt BatchCraft aangeraden, naast twee verouderde plugins. Dat verklaart het snelle groeien beter dan "verlaten" alleen (GOK). Steun voor die GOK (GEZIEN): van de vijf vervangers van KITSS staat alleen BatchCraft in de aanraadlijst van zijn bestandssoort. Voor `*.pas` raadt de IDE I-Pascal, Pascal Flow en Flexible Delphi aan, niet Pasforge; Pascal Flow (aangeraden) heeft 2.344 downloads, Pasforge (niet aangeraden) 31. Pascal Flow komt wel van meanmail.dev, een bekende maker, en dat kan ook meetellen (niet gemeten). Graphlume staat niet bij `*.dot`, Rolewise niet bij `*.yml`, en `requirements.txt` kent de IDE al met Python erbij. Voor `*.cmd` raadt de IDE vijf plugins aan, waaronder BatchUI en EPICS Workbench.

**Niet onderzocht:** of BatchCraft ook is uitgelicht op de Marketplace (staff pick, nieuw en opvallend) of ergens is aangeprezen. Dat kan de groei ook (deels) verklaren. **Downloads zijn geen gebruikers:** BatchCraft bracht 3 versies uit en ook updates tellen als download, dus 9.054 is meer dan het aantal gebruikers.

**Kanttekening bij de test:** de testomgeving laadt niet alle meegeleverde plugins (bijvoorbeeld `.vue` en `.ini` kwamen uit als onbekend in IDEA 2026.2, terwijl daar plugins van JetBrains voor zijn). Een "onbekend" in de test betekent dus niet zeker onbekend bij de gebruiker. Voor `gradlew.bat` is er geen plugin van JetBrains (GEZIEN in de aanraadlijst), dus daar klopt het wel.

**5. Aanraadlijst voor ruim 170 bestandssoorten (GEZIEN).** `data/aanraden-per-bestandssoort-2026-11-06.tsv` en, met downloads en datum van de aangeraden plugins, `data/aangeraden-plugins-2026-11-06.tsv` (19 soorten). Uitkomst: bijna elke veelvoorkomende soort die de IDE niet zelf kent, heeft een gratis plugin van JetBrains die onderhouden wordt: `.env` (.env files, 32.700.066), `.log` (Ideolog, 13.048.215), `Makefile` (7.314.825), `.ini` (8.764.067), `.http`, `.tf`, `.graphql`, `.proto`. PowerShell (1.504.442), CODEOWNERS (466.335) en `.gitattributes` (759.790) hebben een gratis plugin die in 2026 nog bijgewerkt is. Batch is in deze 19 de enige veelvoorkomende soort waar alleen verlaten gratis plugins tegenover stonden. Voor `.npmrc`, `Podfile` en `.dockerignore` raadt de Marketplace helemaal niets aan (GEZIEN); `.dockerignore` kent IDEA 2026.2 zelf, `.npmrc` en `Podfile` niet in de test. Nog niet uitgezocht of daar vraag naar is.

## Tussenstand na deel 6
- Het patroon is smaller dan gedacht. Niet "verlaten plugin", maar: **een bestand dat in heel veel projecten zit, dat de IDE niet kent, zonder plugin van JetBrains, en waar de aangeraden gratis plugins verlaten zijn.** Dan zet de IDE zelf je product voor de gebruiker. Eén voorbeeld (BatchCraft), dus nog een GOK.
- Concurrenten die op grote schaal plugins maken (KITSS TECH 27 in een maand, meanmail.dev 30 in totaal) zitten al in veel gaten. Een gat vinden en snel bezetten is dus waar het om gaat, en de meeste pogingen leveren weinig op.
- **Geen bouwbesluit.** Er is nog geen tweede bestandssoort gevonden die aan alle vier de eisen voldoet.
- Nagekeken door een controleur: afgekeurd op 6 punten (git flow fout, 1 van 4 moest 1 van 5 zijn, Pascal zonder meting, downloads zijn geen gebruikers, *.cmd ontbrak, uitlichting niet genoemd). Alles verwerkt, herkeuring akkoord.
- Volgende meting: per aangeraden bestandssoort (de lijst van ruim 170 en meer) automatisch nagaan of er een plugin van JetBrains bij zit en of de beste niet-JetBrains-plugin na 2024 nog is bijgewerkt. Over blijft een korte lijst. Daarna per soort schatten hoe vaak hij in projecten voorkomt (bijvoorbeeld via de zoekfunctie van GitHub op bestandsnaam).

## Meting deel 7: bouwbesluit stap 1, 302 bestandssoorten (17:14 tot 17:19 UTC, met curl)
**Hoe:** voor 302 bestandssoorten en bestandsnamen de aanraadlijst van de Marketplace opgehaald, en per aangeraden plugin de maker, downloads en datum van de nieuwste versie. Alles in `data/bestandssoorten-stap1-2026-11-06.tsv` (GEZIEN). Of de IDE de soort zelf al kent is hier niet gemeten (zie de kanttekening bij deel 6).

**Uitkomst (GEZIEN):**
- 122 van de 302 hebben een plugin van JetBrains in de lijst. 57 hebben helemaal geen aangeraden plugin.
- Soorten zonder JetBrains-plugin waar de nieuwste andere plugin van voor 2025 is: maar 7 (plus `*.pbf` zonder datum), allemaal klein (de grootste is SVG2VectorDrawable bij `*.svg` met 152.773, maar `.svg` kent de IDE zelf). Daar zit geen tweede batch tussen.
- Zwak bediend, maar ook niet groot: NSIS (`*.nsi`, gratis plugins uit 2015, nieuwe betaalde met 66), AppleScript (gratis uit 2021, nieuwe betaalde met 274), Org (`*.org`, Org4Idea uit 2018, wel OrgMode met 1.656 downloads, bijgewerkt oktober 2026), Julia (2021, nieuwe betaalde Flexible Julia 9.048, maar die bracht sinds januari 2026 meer dan 100 versies uit en elke update telt als download).
- Opvallend: `Jenkinsfile` heeft een **betaalde** plugin met 162.049 downloads (Jenkinsfile, bijgewerkt september 2026). Maker is Anbora Labs, ook van de betaalde Procfile-plugin. Let op: 47 versies sinds januari 2025 en elke update telt als download, dus 162.049 zegt weinig over kopers. Dat een betaald product voor zo'n bestand groot kan worden is een GOK.
- Geen enkele plugin aangeraden voor onder meer `Podfile`, `.npmrc`, `*.webmanifest`, `*.heapsnapshot`, `*.cpuprofile`, `*.geojson`, `*.ics`, `*.srt`, `*.vtt`. (Ook `*.csproj`, `*.razor` en `*.xaml`, maar die kent Rider zelf, GOK, dus geen gat.)

## Tussenstand na deel 7
- Batch lijkt een buitenkans die er nu niet meer is: in 302 soorten geen tweede veelvoorkomende soort met alleen verlaten plugins en zonder JetBrains (GEZIEN voor deze 302, meer soorten bestaan).
- Overgebleven sporen voor de volgende run: (a) soorten zonder enige aangeraden plugin die toch vaak in projecten zitten, bijvoorbeeld `Podfile` (staat in de map ios van Flutter-projecten die voor iOS bouwen, GOK) en `.npmrc`; eerst echt testen of de IDE ze kent. (b) Betaalde plugins voor veelvoorkomende bestanden die het goed doen (Jenkinsfile 162.049, BatchCraft) als bewijs dat mensen voor zoiets betalen. (c) Terug naar C-breed: viewers voor bestanden zonder aanbod (`*.heapsnapshot`, `*.cpuprofile`).
- Nagekeken door een controleur: afgekeurd op 6 kleine punten (8 moest 7, OrgMode vergeten, Jenkinsfile en Flexible Julia te stellig door updates, Rider-soorten, Podfile). Alles verwerkt.
- **Geen bouwbesluit.**

## Meting deel 8: kent IDEA 2026.2 deze soorten zelf? (17:20 UTC, verbeterd 18:10 UTC na controle)
**Hoe:** eerste poging (17:20) zocht op losse tekst in de meegeleverde plugins. Dat kan geen verschil zien tussen "de IDE noemt de naam" en "de IDE kent het bestand als soort", en gaf daardoor twee foute conclusies. De controleur deed het opnieuw in IntelliJ IDEA **Ultimate** 2026.2, build 262.8665.258 (163 meegeleverde plugins), en zocht in alle 5.524 xml-bestanden uit de jars op echte registraties (`<fileType>` met `fileNames`, `patterns` of `extensions`, en FileTypeFactory), plus op tekst in de jars (GEZIEN).
- `.npmrc`: **geen bestandssoort.** Geen `<fileType>`. De Node.js-code leest wel de instellingen uit het bestand, maar wie het aanklikt krijgt een onbekend bestand. Past bij de test uit deel 6 (UNKNOWN). Mogelijk gat (GEZIEN dat er geen soort is, vraag niet gemeten).
- `*.cpuprofile`: **geen bestandssoort, en ook niet in de V8-profiler.** Alleen in uitlegtekst van de tsconfig- en jsconfig-schema's en in de terminal-aanvulling. De profiler leest V8-logbestanden, geen .cpuprofile. Mogelijk gat.
- `*.heapsnapshot`: **geen bestandssoort, wel te laden** via een menu-actie in de Node.js-profiler (Load V8 Heap Snapshot, met een eigen bestandskiezer). Aanklikken in de projectboom geeft geen viewer. Klein aanbod, het gat is kleiner.
- `Podfile`: **geen bestandssoort geregistreerd.** De naam staat alleen als tekst in een statistieklijst van appcode.cocoapods, de Kotlin-wizard (`../iosApp/Podfile`), een woordenlijst en de terminal-aanvulling. Er zit geen Ruby-plugin in IDEA, dus het wordt ook niet als Ruby herkend. RubyMine niet bekeken.
- `*.webmanifest`: **geen bestandssoort geregistreerd.** De JSON-plugin kent alleen `har;json;jsonc` en losse namen als `.babelrc`, dus het wordt niet als JSON herkend. Wel heeft het platform een mime-type (`application/manifest+json`) en een eigen icoon voor `webmanifest`. Of de IDE het daardoor toch als tekst met icoon toont is niet getest.
- **Gevolg:** spoor (a) en (c) uit deel 7 worden door deze meting **niet** kleiner. Alle vijf zijn geen bestandssoort in IDEA Ultimate 2026.2, en alleen bij `*.heapsnapshot` is er wat aanbod. Of er genoeg vraag is, en of mensen ervoor betalen, is nog niet gemeten. Dat is de volgende stap: per soort schatten hoe vaak hij in projecten voorkomt.
- **Nakijken:** controleur keurde de eerste versie af op 6 punten (npmrc en cpuprofile fout, heapsnapshot te stellig, "nergens gevonden" niet letterlijk waar, editie en methode ontbraken, gevolg verkeerd). Alles hierboven verwerkt, de controleur deed de meting zelf opnieuw, dus deze versie steunt op zijn bevindingen.
