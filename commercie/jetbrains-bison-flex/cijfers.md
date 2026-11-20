# Bison & Flex (JetBrains): cijfers

Door Chris. Meten op dag 0 (lancering), dag 7, dag 30, daarna elke week. Alleen aanvullen.

## Dag -? (7 nov 2026): nulmeting markt, nog niet ingediend
Onze plugin: niet live, 0 downloads, 0 proeven, 0 licenties.

Concurrenten en buren (GEZIEN 7 nov, `https://plugins.jetbrains.com/api/searchPlugins?search=<woord>&max=20`):
| Plugin | Downloads | Laatste versie | Prijs |
|---|---|---|---|
| Bison Language Support (16595) | 13.020 | 2 sep 2023 | gratis |
| GoYacc Support (11444) | 21.167 | 2 mei 2020 | gratis |
| ANTLR4 Helper (32227) | 269 | onbekend | $20 / $40 |
| ANTLR v4 (7358) | 788.253 | 27 aug 2026 | gratis |

Plugins die de IDE aanraadt per bestandssoort (GEZIEN, `https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.<soort>`): `*.y` 2 (GoYacc, Bison Language Support), `*.l` 0, `*.yy` 1 (GameMaker Tools), `*.ll` 2 (LLVM, NPCoding Compiler IR Files).

Vraag: YouTrack IDEABKL-7544 8 stemmen; Stack Overflow 49288299 1.238 keer bekeken.

## Hoe meten na de lancering
- Downloads: `https://plugins.jetbrains.com/api/plugins/<id>` (veld `downloads`) en de zoek-API.
- Proeven en licenties: alleen in het verkopersaccount van Thijs zichtbaar (GOK). Vraag Jet of er een openbare weg is; anders op de lijst van Thijs een vaste vraag per week.
- Bison Language Support elke week meten: groeit die door terwijl wij erbij komen, dan winnen wij de `.y`-zoekers niet.

## Dag -1 (8 nov 2026, 14:50 UTC): geüpload, nog verborgen
Bron: `https://plugins.jetbrains.com/api/plugins/35901` en `/api/plugins/16595` (GEZIEN).
- Bison & Flex (35901): `approve: false`, 0 downloads, `pricingModel: FREE` (Sales Info nog niet goedgekeurd), `productCode: PBISONFLEX`, proef 30 dagen, tags Inspection, Navigation, Programming Language, licentie-URL en documentatie-URL gevuld.
- Bison Language Support (16595): 13.024 downloads (7 nov: 13.020). Groeit ±4 per dag (GOK, twee metingen).
- Volgende meting: de dag dat Hidden uitgaat (dag 0), dan dag 7 en dag 30.

## Stand 9 nov 2026, 03:50 UTC (run 22, GEZIEN)
- 35901: `isHidden: true`, `pricingModel: FREE`, 0 downloads, `/updates` leeg, niet in `/plugins/list` (wat de IDE ziet). Nog in moderatie.
- Bison Language Support (16595): 13.024 downloads.
- Let op: `approve` van de plugin zegt niets over goedkeuring (ook live plugins staan op `false`); seintje in `lancering.md`, deel run 22.

## Dag 0 (17 nov 2026, ±15:00 UTC, run 80, GEZIEN)
Openbaar sinds ±12:55 UTC (13:55 NL). Bronnen: `/api/plugins/35901`, `/api/plugins/35901/updates`, `/api/marketplace/plugin/35901/prices?countryCode=US|NL`, `/api/marketplace/plugin/35901/programs`, `/api/searchPlugins?search=<woord>&max=20`.
- Bison & Flex (35901): `isHidden: false`, `pricingModel: FREEMIUM`, 1 download (versie 2026.1.1; 2026.1.0 heeft 0), geen beoordelingen. Proef 30 dagen.
- Prijs live: VS $19 persoonlijk en $49 zakelijk per jaar; NL € 19 en € 49 (met btw € 22,99 en € 59,29). Geen maandprijs (besluit Jet: ook $1,90 / $4,90 per maand). Geen staffelkorting.
- Kortingsprogramma's: geen (`[]`). BashSupport Pro ter vergelijking: STUDENT, CLASSROOM, OPEN_SOURCE, EDUCATIONAL_ORGANIZATION, START_UP, NON_PROFIT, DEVELOPER_RECOGNITION, GRADUATION. Gemeld aan de hoofdchat.
- `buyUrl: null` is normaal bij verkoop via JetBrains: zo staan ook BashSupport Pro, Monokai Pro, JPA SQL, Database Helper en Bitbucket Integration Pro. De site van JetBrains leest null als "verkocht via JetBrains".
- Aanraden bij een onbekend bestand (`getImplementations`): `*.l` nog leeg, `*.y` alleen GoYacc en Bison Language Support. Wij staan er (nog) niet in; opnieuw meten op dag 7.
- Zoekpositie (top 20): bison 2, yacc 3, lex 9, flex niet, lexer niet, parser niet, grammar niet, "bison flex" 1, "flex lexer" 2, "clion yacc" 1.
- Bison Language Support (16595): 13.056 downloads (8 nov 13.024: +32 in 9 dagen, ±3,6 per dag).
- Volgende meting: dag 7 (24 nov).

## Dag 3 (20 nov 2026, ±14:50 UTC, run 89, GEZIEN)
- Bison & Flex (35901): 16 downloads (2026.1.1: 15, 2026.1.0: 1), dag 0 nog 1. Geen beoordelingen. `pricingModel: FREEMIUM`.
- Zoekpositie (top 20): bison 2, yacc 3, lex 9, flex niet (gelijk aan dag 0).
- Bison Language Support (16595): 13.073 (dag 0: 13.056, +17 in 3 dagen, ±5,7 per dag). Wij haalden in 3 dagen ±5 per dag: ongeveer gelijk aan de grote gratis concurrent.
- Geld: de proef duurt 30 dagen, dus de eerste betalingen kunnen pas vanaf ±17 dec (GOK). Volgende meting: dag 7 (24 nov).
