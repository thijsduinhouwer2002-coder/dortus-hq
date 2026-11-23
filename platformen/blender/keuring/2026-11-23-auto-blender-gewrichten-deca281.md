# Keuring Keuringsbestand A Figure from rig betrouwbaar (blender-gewrichten), 23-11-2026 23:42 NL, automatische keurder
Wat ik keurde: commit deca2818f, bestand `producten/blender-gewrichten/keuring/2026-11-24-betrouwbaar-rig-A.md` (alleen tekst gezien, geen runs, JSON of logs)
Akkoord: ja

Dit ja geldt alleen voor het toevoegen van dit keuringsbestand. Het oordeel erin ("nee" voor tak `claude/betrouwbaar-rig`) blijft staan: niet uitbrengen tot de twee moet-punten uit dat bestand zijn opgelost.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één nieuw markdownbestand, geen code. De add-on en het eerdere ja van Daan voor 0.1.1 en 1.0.2 blijven dus onaangetast. | feit | hoog | Een `git diff --stat` van 6ad5870..deca281 met precies dit ene bestand. |
| 2 | Het formulier is gevolgd: kop, drie delen, moet/kan-lijst, en Akkoord "nee" past bij de twee moet-punten. De "Wat ik keurde"-regel loopt over meerdere regels en achter "Akkoord: nee" staat uitleg. Dat is kleine afwijking van het formulier. | feit | hoog | |
| 3 | De getallen kloppen onderling. 28 van 51 wordt 44 van 51 op dezelfde zes figuren, plus 7 voor robot-fijn is 51 van 60. De tellingen robot 6, robot-fijn 7 en kleding 8 geven samen 9 ontbrekend, dus 51. | feit (uit de tekst gerekend) | hoog | |
| 4 | De cijfers uit de runs (45273407326, 45275271607, 45279729768, 45275271494) en de JSON op tak `betrouwbaar-uitslag` kan ik niet nalopen. Ik neem ze als bewering van de andere keurder. | vermoeden | midden | De JSON-bestanden en run-logs, of een telling door een tweede keurder. |
| 5 | Moet 1 (verlies meten bij kogelsneden) is onderbouwd. A9 noemt een gemeten verlies van 7,1 tot 10,7% bij de knight in 4.2, door het vangnet gevangen. Dat het risico bij kogels "niet aangetoond" is, staat er eerlijk als vermoeden in. | feit (gemeten waarde), vermoeden (risico) | midden | Een meting van volume A plus B tegen de bron bij elke kogelsnede. |
| 6 | Moet 2 gaat over cijfers in verslag en bericht, niet over het product. Dat is verdedigbaar, omdat het bericht aan Bram een te rooskleurig getal gaf ("28 naar 51 van 60"). | feit | midden | |
| 7 | Kleine onduidelijkheid in A6: 553 tegenover 558 kogelsneden wordt "klein verschil" genoemd, zonder reden. | feit | hoog | De telling opnieuw uit de JSON. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het bestand is ongeveer 57 regels, ruim onder de ±400. | feit | hoog | Bestanden onder ±400 regels |
| 2 | Ik zie in de tekst geen persoonsgegevens, sleutels of wachtwoorden. De keurder meldt zelf dat de GitHub-API zonder sleutel is gebruikt. | feit | hoog | Geen persoonsgegevens |
| 3 | Uitkomsten staan met feit of vermoeden, zekerheid en wat het zou bevestigen. Het "GOK"-stapje in A6 is als zodanig gemerkt. | feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | B1 in het bestand meldt dat de ondergrens voor 4.2 naar de gemeten stand is gezet. Dat noemt de keurder zelf een eis die naar de uitslag is gezet. Dat hoort bij de tak, niet bij dit bestand, en staat daar open vermeld. | feit | hoog | Tests niet aangepast om te slagen |
| 5 | Deel B in het bestand is bewust beperkt ("aparte keurder"). Een volledige regelkeuring van de tak is dus nog nodig. | feit | hoog | Twee keurders bij zwaar werk |
| 6 | `architectuur.md` hoeft voor een los keuringsbestand niet bij te werken. | feit | hoog | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging. De C-punten in het bestand zelf (releasenote "5.2 en nieuwer", statusregel bij trage 4.2, vaag "place it by hand a few mm") zijn redelijk. Ik kan ze niet beoordelen zonder het scherm. | Een korte samenvatting van drie regels bovenaan het bestand, zodat Thijs of Bram de uitkomst direct leest. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Geen.

**Kan**
1. Bestandsnaam en kop hebben 24 nov, terwijl de commit van 23 nov 23:42 NL is. Zet de datum gelijk aan de commit.
2. Zet "Akkoord: nee" kaal op de regel en de uitleg eronder, zoals het formulier vraagt.
3. Leg het verschil 553 tegenover 558 (A6) uit of haal het weg.
4. Laat een tweede keurder de cijfers uit de JSON en logs naslaan. Ik kon alleen de tekst zien.
5. Het eindoordeel voor de tak blijft "nee" tot moet 1 en 2 uit het bestand zijn opgelost. Keur die daarna opnieuw, alleen die punten.

---
Automatische keurder, model `claude-sonnet-5-5`, 23429 tokens in, 5390 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
