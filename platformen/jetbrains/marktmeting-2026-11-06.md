# JetBrains: marktmeting 6 nov 2026 (16:00 UTC)

**Hoe gemeten:** de Marketplace-API (`/api/searchPlugins`, velden downloads, rating en pricingModel) via de leestool (WebFetch), niet via curl. Het cijfer in de tabellen is het veld rating uit die zoekresultaten. curl en Gradle krijgen nog steeds 403 van de proxy. Alle cijfers hieronder zijn GEZIEN, tenzij anders vermeld. Downloads zijn opgeteld over de hele levensduur van een plugin en tellen ook proefversies mee. Aantal betalers is nergens te zien.

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
- Taalondersteuning heeft geen JCEF nodig en past in de standaard testopzet van IntelliJ (GOK: nog niet gebouwd, want Gradle is geblokkeerd).
- Onbekend blijft hoeveel van die downloads betalen. De oudste klant van BashSupport Pro had in 2020 een klantnummer onder de 11.000 ([plugin-dev.com](https://www.plugin-dev.com/intellij/general/marketplace-stats/), DERDEN), dat zegt weinig over het aantal betalers nu.

## Volgende meting
Kies een taal of bestandssoort voor kandidaat D: zoek per soort (bijvoorbeeld Caddyfile, Justfile, HAProxy, systemd units, Earthfile, Nix, Helm-templates, Ansible-alternatieven, PowerShell DSC) het aantal plugins, downloads en of er een betaalde is. Meet ook het grootste gratis alternatief naast de bestaande betaalde taalplugins (bijvoorbeeld bij Bash en Nginx). Kies er één waar gratis ondersteuning ontbreekt of slecht is (cijfer onder 3,5), en waar ontwikkelaars veel mee werken.
