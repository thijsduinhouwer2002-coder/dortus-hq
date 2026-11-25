# Keuring Click Cuts winkeltekst: Lay parts flat en Free cut, 25 nov 2026, Daan
Wat ik keurde: commit 9ef2e20 (`platformen/blender/superhive/click-cuts-winkeltekst.md` en `click-cuts-winkeltekst-lang.md`), issue #110.
**Akkoord: ja**

## Deel A: klopt elke zin met 1.0.0?
| # | Zin | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|---|
| 1 | "Lay parts flat ... On by default" | `eigenschappen.py` r. 74: `plat`, name "Lay parts flat", default True. | feit | hoog |
| 2 | "on export" | `exporteer.py` r. 123 tot 132: alleen in de export, pennenplaten blijven zoals ze zijn. | feit | hoog |
| 3 | "usually a cut face" | `plat.py`: grootste platte vlak wint; bij een stuk van een gesplitst model bijna altijd een snijvlak, bij een stuk met eigen platte bodem kan die winnen. "usually" is dus precies goed, niet te veel beloofd. | feit | hoog |
| 4 | "if it still fits your printer ... Otherwise the part keeps its own way up" | `plat_matrix` (exporteer.py r. 62): None als geen plat vlak op het bed past, dan verandert alleen de hoogte. Klopt. | feit | hoog |
| 5 | Free cut "at any angle through one part ... with pins and numbers like the other cuts" | `vrije_snede.py` r. 1 tot 12: één stuk, elke hoek, pennen en nummers uit dezelfde planner. Klopt. | feit | hoog |
| 6 | Oude zin "Not automatically" en "Parts are not laid flat" weg, ook uit "Bewust niet" en deel 6 | Nu consequent in beide bestanden. | feit | hoog |

## Deel B: regels
| # | Bevinding | Regel |
|---|---|---|
| 1 | Geen belofte dat het klikt, past of dat wij printten. Geen AI. | 5 |
| 2 | Bronnen per zin staan erbij (r. 64 tot 67 en codetabel). | 5 |

## Deel C: goed genoeg?
| Vraag | Cijfer | Waarom |
|---|---|---|
| Op niveau van de beste in de winkel? | 8 | Plat leggen is bij Cleave en CatPin een los verkooppunt; nu staat het er ook, kort en eerlijk ("if it still fits"). |
| Zou ik kopen op basis van dit? | 8 | Het gat "moet ik alles zelf in de slicer draaien" is weg. |
| Trots? | 8 | |

## Moet
Geen.

## Kan
- K1: FAQ "Can I choose where it cuts, so it does not go through a face?": het antwoord zegt geen ja of nee. Begin met "Partly." of "Yes, with Free cut:", dan leest de koper meteen het antwoord. "a face" kan ook een vlak betekenen; "through a character's face" is duidelijker.
- K2: de lange tekst schrijft nog "Colour per part" en "millimetres", de korte "millimeters". Kies één spelling (de korte en de Pro-tekst zijn Amerikaans).

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
