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

## Meting deel 5: verlaten gratis plugins (16:21 UTC, met curl, NOG NIET NAGEKEKEN)
- Gratis plugins met minstens 100.000 downloads: 870. Daarvan niet van JetBrains en laatste versie voor november 2024: 219 (GEZIEN). De hele lijst staat in `data/verlaten-gratis-2026-11-06.tsv`.
- Veel daarvan zijn al vervangen: CodeGlance (1.758.526, laatst 2018) door CodeGlance Pro (4.691.766, gratis), Thrift Support (361.136, laatst 2022) door een gratis fork (199.360, cijfer 4,69), Robot Framework-plugins door nieuwe, Ansible door OrchidE en Ansible Pro (GEZIEN).
- Batch en CMD zijn nu door BatchCraft genomen.
- Eerste kandidaat zonder zichtbare vervanger in de top 6: **Git Flow Integration**, 682.493 downloads, cijfer 4,37, laatste versie augustus 2021 (GEZIEN). Of git flow nog veel gebruikt wordt is niet gemeten.
- Volgende run: de 219 aflopen, per stuk kijken of er een nieuwe vervanger is, en of de taak of taal nog leeft. Daarna één kiezen.
