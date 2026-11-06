# JetBrains: marktmeting 6 nov 2026 (16:00 UTC)

**Hoe gemeten:** de Marketplace-API (`/api/searchPlugins`, velden downloads, rating en pricingModel) via de leestool (WebFetch), niet via curl. Het cijfer in de tabellen is het veld rating uit die zoekresultaten. Toen kregen curl en Gradle nog 403. Sinds ±16:00 UTC werkt curl wel. Voortaan meten met curl, nooit met WebFetch (regel in CLAUDE.md). Alle cijfers hieronder zijn GEZIEN, tenzij anders vermeld. Downloads zijn opgeteld over de hele levensduur van een plugin en tellen ook proefversies mee. Aantal betalers is nergens te zien.

## Totalen (GEZIEN)
- Betaalde plugins (PAID): 539 bij zoeken gesorteerd op downloads (16:00 UTC), 533 bij een tweede telling door de controleur zonder sortering (±16:15 UTC). Het verschil is niet verklaard. Freemium: 243.
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

## Meting D, deel 1 (16:17 UTC, met curl)
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
- Nagekeken door een controleur (16:25 UTC): cijfers klopten, tekst daarna verbeterd op 4 punten.
- Nog te doen voor het bouwbesluit: leeftijd (eerste uitgave) van Liquid Hero, Caddyfile Pro en de andere Pro-plugins, zodat downloads per maand te zien zijn, en de reviews van de gratis Liquid-plugin lezen om te zien wat er mist.
