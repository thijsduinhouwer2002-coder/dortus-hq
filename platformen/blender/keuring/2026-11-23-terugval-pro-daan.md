# Keuring terugval naar Exact in Pro (herkeuring), 23 nov 2026, Daan
Wat ik keurde: tak `claude/blender-solver-terugval` op 957a9ac (`betaald/terugval.py`, `betaald/__init__.py`, toets `solver_terugval`, `architectuur.md`, `platformen/blender/pro-1.2.2.md`), e2e-runs 45194995297 (542c4be) en 45202556640 (957a9ac).
Akkoord: nee (één kleine moet, alleen in de testhaak)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Mijn moet van 14:45 is opgelost: de terugval staat alleen in Pro, `gewricht.py` is niet geraakt (diff tegen main raakt alleen `betaald/`, e2e en teksten). | feit (git diff) | hoog | |
| A2 | De toets draait echt met de Pro-zip: in het log van e2e 5.2.3 (job 137789569374) staan "TERUGVAL 0x open ... solver=['MANIFOLD','MANIFOLD']" en "TERUGVAL 1x open ... solver=['EXACT','EXACT'] hulp=[]", beide stappen OK, delen gesloten, passing groen. De gratis zip meldt netjes "gratis zip, toets overgeslagen". | feit (log GEZIEN) | hoog | |
| A3 | **e2e op 957a9ac is rood op 5.2.3**: bij "2x open" crasht de testhaak `_maak_open` met `IndexError: BMElemSeq[index]: outdated internal index table, run ensure_lookup_table() first` (terugval.py r. 48). De operator gooit dan een Python-fout in plaats van de nette weigering, dus stap "terugval 2x open" faalt. 4.2.23 en 5.3.0 liepen nog om 15:24 UTC. | feit (log GEZIEN) | hoog | `bm.faces.ensure_lookup_table()` voor `bm.faces[0]`, daarna e2e groen in alle drie |
| A4 | Het pad voor kopers (FORCEER_OPEN 0) raakt `_maak_open` nooit, dus de fout zit alleen in de test. Maar het echte geval "ook Exact open" is daardoor nog niet bewezen: precies dat wil stap 2x laten zien. | feit (code) | hoog | groene stap 2x |
| A5 | `snij` maakt eerst een kopie van het werk (`bak(werk, ...)`), dus de tweede snede begint met hetzelfde figuur; `_ruim_extra` haalt alleen wat de eerste snede in de hulpcollectie zette weg. Klopt. | feit (code gelezen) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Toets niet versoepeld; de 2x-stap is juist strenger dan op 542c4be. | feit | hoog | tests niet aangepast om te slagen |
| B2 | `terugval.py` 97 regels; `architectuur.md` bijgewerkt. | feit | hoog | |
| B3 | Releasenotes 1.2.2: "Tested on Blender 4.2 LTS, 5.2 LTS and 5.3" mag pas na groene e2e op de laatste commit. Effect op verkoop staat als GOK. | feit | hoog | eerlijk |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Een koper ziet niet dat er een tweede snede was. Kan prima, maar bij een trage Exact-snede (groot figuur) lijkt Blender even vast te zitten. | Eén regel in de statusbalk, bv. "Retried with Exact solver", als de terugval gebeurde. | klein |
| C2 | Releasenotes lezen helder; "fast solver" is goed gekozen voor wie Manifold niet kent. | | |

## Moet (blokkeert akkoord)
1. `_maak_open`: `bm.faces.ensure_lookup_table()` vóór `bm.faces[0]`; e2e groen in 4.2.23, 5.2.3 en 5.3.0 met stap "terugval 2x open" OK in het Pro-log. Dan herkeur ik alleen dat (log lezen), de rest is ja.

## Kan
1. C1: statusregel na een terugval.
