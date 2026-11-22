# Voorstel: Fortnite-eilanden (UEFN en Fortnite Creative)

Vera, 8 nov 2026 run 11:33 UTC. Nagekeken door een controleur: akkoord, alle tellingen gelijk, 8 van 8 live gelijk, 9 correcties verwerkt. Zelf toegevoegd: groot platform, Epic betaalt makers aantoonbaar uit, en er is een open Data API met spelers per eiland.

## In het kort
- **Advies: nee voor nu, cijfer 3.**
- **Geld is er echt, en veel:** Epic betaalde in 2024 $352 miljoen aan ±70.000 makers, en sinds maart 2023 samen meer dan $1 miljard (DERDEN, Epic via Tubefilter en PocketGamer). Sinds 9 jan 2026 kun je ook dingen verkopen in je eiland, tot en met 31 jan 2027 krijgt de maker 100% van de V-Bucks-waarde (±74% van wat de speler betaalt) (DERDEN, FAQ Epic).
- **Maar een doorsnee eiland krijgt bijna geen spelers:** van 5.748 willekeurige makerseilanden had 84% van 1 t/m 7 nov geen enkele dag met 5 of meer unieke spelers. 4,4% haalde samen 100+ spelers (som van de dagcijfers) en naar een ruwe schatting verdient 1,3% $100+ per maand (GEZIEN, eigen meting; geldcijfer GOK).
- **Heel geconcentreerd:** in mijn steekproef had het drukste eiland 21% van alle speelminuten, de 29 drukste (0,5%) samen 87% (GEZIEN).
- **De doorslag: wij kunnen het niet bouwen.** UEFN draait alleen op Windows, met een grafische editor; onze Claudes werken in Linux zonder scherm. Fortnite Creative kan alleen in het spel zelf. Testen kan alleen door te spelen. Dat moet Thijs dan allemaal zelf doen (DERDEN, forum Epic).

## Wat ik gemeten heb (GEZIEN)
Bron: de openbare Data API van Epic, `api.fortnite.com/ecosystem/v1` (geen sleutel nodig; robots.txt geeft daar een foutmelding, dus geen regels; rustig gelezen, 4 tegelijk). De pagina's van fortnite.gg en fortnite.com geven een Cloudflare-uitdaging (403), niet omzeild.

- `/islands?size=1000`: de hele lijst. **286.128 eilanden**, waarvan 13.003 van Epic zelf (ze tellen hieronder niet mee). Van de 273.125 eilanden van makers zijn er 176.858 gemaakt in UEFN en 96.267 in Fortnite Creative (FNC). **77.189 makers** (plus 1 eiland zonder maker), ±33.700 met precies 1 eiland.
- `/islands/<code>/metrics/day`: per dag unieke spelers, plays, minuten, piek-CCU, favorieten. **Alleen de laatste 7 dagen** (de API weigert een begindatum voor 1 nov). Een dag met minder dan 5 spelers geeft leeg (null), dus kleine aantallen zie je niet.
- **Er staat geen publicatiedatum in de API.** Een groep nieuwe eilanden van 3 tot 6 maanden oud kon ik dus niet apart meten. Wat hieronder staat gaat over de hele catalogus, met veel verlaten eilanden. Of nieuwe eilanden het beter of slechter doen weet ik niet; elk nieuw eiland krijgt tot 2 weken een testplek in Discover, maar makers op het forum zeggen dat het "harder than ever" is (DERDEN, GOK).

### Steekproef: 6.000 willekeurige eilanden, 1 t/m 7 nov 2026 (5.748 van makers)
| Groep | Aantal | Een dag 5+ spelers | Som 7 dagen 100+ spelers | 1.000+ | Piek-CCU 10+ | Piek-CCU 100+ | GOK $100+ per maand |
|---|---|---|---|---|---|---|---|
| Alle makers | 5.748 | 16,0% | 4,4% | 1,4% | 3,4% | 0,7% | 1,3% |
| UEFN | 3.762 | 19,2% | 6,1% | 2,1% | 4,7% | 1,0% | 2,0% |
| Fortnite Creative | 1.986 | 9,8% | 1,2% | 0,2% | 0,9% | 0% | 0,1% |

- Mediaan: 0 spelers in alle groepen.
- "Som 7 dagen" telt de unieke spelers per dag bij elkaar op, dus iemand die drie dagen speelt telt drie keer.
- Het geldcijfer is een GOK: speelminuten van de week maal 30/7 maal $1.100 per miljoen minuten (zo rekent profitable.app: $352 miljoen gedeeld door 5,23 miljard uur in 2024). De echte uitbetaling telt ook nieuwe spelers, retentie en uitgaven mee.
- 1,3% van 273.000 makerseilanden is ±3.500 eilanden met $100+. Dat ligt in de buurt van de schatting van profitable.app (±3.260), maar die bron levert ook het tarief, dus het is geen echte tweede controle. Met de foutmarge van de steekproef (77 van 5.748): ±2.800 tot 4.500 eilanden (GOK).
- De volgorde van de lijst is niet willekeurig: in het eerste tiende is 35% actief, verder 11 tot 22%. Een datum zit er niet in, dus ik weet niet waarop gesorteerd wordt.

Bestanden in `data/`: `fortnite-eilanden-2026-11-08.tsv.gz` (alle 286.128 codes met maker, editor en titel), `fortnite-steekproef-7d-2026-11-08.jsonl.gz` (de 6.000 met dagcijfers), scripts `fortnite-lijst-script.py`, `fortnite-metrics-script.py` (bestand, aantal, uitvoer) en `fortnite-analyse-script.py` (paden in de scripts wijzen naar een tijdelijke map, pas die aan).

## Geld en regels (DERDEN, onderzoeker 8 nov)
- **Engagement payouts:** 40% van de netto-omzet van de Item Shop gaat naar een maandpot, verdeeld naar speelminuten, nieuwe en teruggekeerde spelers en retentie (FAQ Epic; VGC 19-9-2025). Sinds sep 2025 krijgt een eiland dat nieuwe spelers binnenhaalt een half jaar 75% van hun bijdrage (Tubefilter 18-9-2025).
- **Verdeling 2024:** 1.728 makers verdienden minstens $10.000 per jaar, 418 minstens $100.000, 7 meer dan $10 miljoen (Tubefilter 23-1-2025). Eerder: top 100 kreeg 71% van alles (Game World Observer 1-4-2024).
- **Verkopen in het eiland:** sinds 9 jan 2026, meer dan 3.000 eilanden verdienen er al meer mee dan met payouts (PocketGamer 18-6-2026). Werkt met Verse, dus alleen in UEFN.
- **Trend:** aandeel speeltijd in makerseilanden 36,5% (2024), 38% (mei 2025), 47% (mei 2026) (PocketGamer 18-6-2026). Het bedrag per actieve maker halveerde wel van 2023 naar 2024 (profitable.app).
- **Drempels:** minstens 18 jaar, in het afgelopen jaar $20 uitgegeven in Fortnite of een aankoop via Epic, belastinginterview en Hyperwallet voor uitbetaling (Developer Program-pagina Epic). Dat zijn allemaal stappen voor Thijs.
- **AI:** geen algemeen verbod in de Developer Rules (bijgewerkt 29-4-2026). Wel verboden sinds 5-3-2026: meerdere kopieën van hetzelfde eiland publiceren.
- **Vindbaarheid:** elk nieuw eiland wordt tot 2 weken getest in Discover-rijen, daarna bepalen speeltijd, afhaken en retentie of het blijft staan. Betaalde Sponsored Row vanaf $5 per dag, $0,10 tot $20 per 1.000 vertoningen (Epic-documentatie).

## Voordelen
- Echt veel geld voor makers, groeiend aandeel speeltijd, gunstige verdeling bij verkopen tot 31 jan 2027.
- Open data: bereik is per eiland per dag te meten, beter dan bij de meeste winkels.
- AI is niet verboden.

## Nadelen
- Bereik voor een doorsnee eiland in de catalogus is bijna nul (mediaan 0, 84% heeft geen dag met 5 spelers); voor nieuwe eilanden is het niet gemeten.
- Geld zit bovenaan: in de steekproef heeft de top 0,5% bijna 90% van de speeltijd (GEZIEN in de steekproef; voor de hele catalogus een schatting, en de nummer 1 met 21% hangt aan één eiland).
- Bouwen kan alleen met een Windows-editor of in het spel. Onze Claudes kunnen niet bouwen, niet testen en niet publiceren. Thijs programmeert niet en wil weinig gevraagd worden.
- Erg druk: in 2024 ±16.500 nieuwe eilanden per maand (DERDEN, Epic).

## Eerste idee (als het ooit kan)
Een klein feestspel of verstopspel voor groepjes (de genres die in de steekproef bovenaan staan: squid game en party, hide and seek, prop hunt; ook 1v1, boxfight en horror staan hoog, GEZIEN), met een paar betaalde extra's via verkopen in het eiland. Maar zonder iemand die in UEFN klikt en speelt is dit niet te maken.

## Wat er nog gemeten kan worden
- Echte nieuwe eilanden: draai `fortnite-lijst-script.py` over ±7 dagen opnieuw, de nieuwe codes ten opzichte van `fortnite-eilanden-2026-11-08.tsv.gz` zijn de nieuwe eilanden. Meet die na 4 en 8 weken met het metrics-script. Dat geeft de mediaan en het percentage met 100+ spelers voor nieuwe eilanden.
- Alleen zinvol als er een manier is om te bouwen zonder Windows-editor. Die is er nu niet.

## Cijfer
**3 van 10, nee voor nu.** Geld is aangetoond en groot, maar het bereik voor een doorsnee eiland in de catalogus is bijna nul (voor nieuwe eilanden niet gemeten) en wij kunnen er niets bouwen zonder dat Thijs zelf UEFN op een Windows-pc bedient en test (GOK of hij dat kan of wil).
