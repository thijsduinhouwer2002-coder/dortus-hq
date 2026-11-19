# Keuring blender-gewrichten plaatje 20 (Fit test strip), 19-11-2026, automatische keurder
Wat ik keurde: commit cc7162dce, bestand producten/blender-gewrichten/e2e/scherm_testkaart.py (alleen tekst gelezen, niets gedraaid of bekeken)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het script maakt met de knop `click_joints.testkaart` een kogelset en een scharnierset en rendert twee plaatjes (20 en 20d). Dat past bij de beschrijving van de commit. | Feit (uit de code) | Hoog | Een groene run met de regel "KAART BEELD OK" en beide pngs op tak `schermen`. |
| 2 | De commit zegt "stap in e2e-workflow", maar in de meegestuurde wijziging staat alleen het script. Zonder die stap draait het script nooit. | Vermoeden | Midden | De workflow-diff (`.github/workflows/...`) met een aanroep van dit script en een eis op de regel "KAART BEELD OK". |
| 3 | Het script eist 2 sets van 10 delen en 5 getallen per set via de eigenschap `cj_kaart_getal`. Ik kan niet zien of de add-on die eigenschap zet. | Vermoeden | Midden | Een run waarin de log "getallen [..]" met vijf waarden toont. |
| 4 | Het script geeft zelf geen foutcode bij "FOUT"; het logt alleen. Het werkt dus alleen als de workflow op die regel controleert. | Feit | Hoog | De workflow-stap met een grep op "KAART BEELD OK". |
| 5 | Welke set de kogelset is, wordt bepaald met `sorted(groepen)[0]`. Dat klopt zolang de eerste collectie "Fit test" heet en de tweede "Fit test.001". Heten ze anders, dan kan het dichtbijplaatje stilletjes de scharnierset tonen. | Vermoeden | Midden | De werkelijke collectienamen in de log ("Fit test...: 10 delen"). |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het script is 135 regels, ruim onder de 400. | Feit | Hoog | Bestandsgrootte |
| 2 | Er is geen test aangepast om te slagen; het is een nieuw beeldscript. Optillen en kleuren gaan met `delta_location` en objectkleur, dus delen en export blijven onaangeroerd. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 3 | De docstring zegt "14 mm opgetild", maar de code gebruikt `OPTIL_MM = 22.0`. Dat is een kleine tegenstrijdigheid in de uitleg. | Feit | Hoog | Netheid |
| 4 | Er staan geen persoonsgegevens of sleutels in. Er worden geen cijfers beweerd die een label GEZIEN, DERDEN of GOK nodig hebben. | Feit | Hoog | Persoonsgegevens, cijferlabels |
| 5 | Het plaatje is een Workbench-render van echte add-on-uitvoer, geen AI-beeld. Het is bedoeld voor Superhive (Pro), dus de ToS 6.2-regel (alleen gratis functies) speelt niet. | Feit | Midden | Geen AI-beeld op Steam, ToS 6.2 |
| 6 | `architectuur.md` is niet meegewijzigd. Voor een testhulp is dat waarschijnlijk niet nodig, maar ik zie niet of daar een lijst met e2e-scripts staat. | Vermoeden | Laag | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik heb geen beeld gezien. Dit zijn punten om te letten als Daan het plaatje bekijkt.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De scharnierset staat 30 mm achter de kogels. De kogelset kan hem deels verbergen (vermoeden). | Kijk op het plaatje of beide sets los van elkaar leesbaar zijn; zo niet, zet de sets naast elkaar. | klein |
| 2 | Warm bovenste deel en koel onderste deel met de opgetilde helft maakt het gewricht goed leesbaar. Dat is de bedoeling, maar of de getallen op 1920 breed groot genoeg zijn kan alleen Daan zien. | Daan let op leesbaarheid van de getallen op plaatje 20d en op mobiele formaat. | klein |
| 3 | Plaatje 20 laat een "opengewerkt" beeld zien (opgetild). Een koper kan denken dat de kaart zo geprint wordt. | Zet een korte bijschrifttekst in het winkelplaatje ("shown pulled apart"). | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.

Kan:
- Laat de workflow-diff zien of controleer dat de stap erin staat en op "KAART BEELD OK" faalt (A2, A4).
- Kies de kogelset op een eigenschap van de delen (bijvoorbeeld soort) in plaats van op de volgorde van de collectienamen (A5).
- Zet de docstring gelijk met de code: 22 mm in plaats van 14 mm (B3).
- Beeld en speelplezier keuren Daan en Iris nog; een keuring van de agent is er nodig bij live zetten.

---
Automatische keurder, model `claude-sonnet-5-5`, 20026 tokens in, 4031 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
