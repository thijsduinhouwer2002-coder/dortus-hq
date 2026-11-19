# Keuring "eerder Tight blijft" bij scharnier (Click Joints Pro), 19 nov 2026, Daan
Wat ik keurde: commit 3fb6d4a (`betaald/scharnier.py` +8, `e2e/toetsen_scharnier.py` +35, regel in `architectuur.md`) en e2e-run 44512744216 op die commit. Logs van 5.3.0 en 5.2.3 zelf gelezen.
Akkoord: ja scharnier Tight blijft op 3fb6d4a

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Passing, snijpunt en wand van het bronobject worden onthouden vóór het snijden. Na het snijden zet de code eerst groen en daarna, alleen op het deel aan de kant van het oude snijpunt, de oude oranje of rode passing met de oude wand terug. Dat is precies mijn kan-punt 2 en A4. | feit (code) | hoog | |
| 2 | `cj_snijpunt` is een wereldpunt (`gewricht.py` r.250, `frame @ ...`) en `scharnier_vorm.kant` verwacht een wereldpunt. Het klopt dus. | feit (code) | hoog | |
| 3 | Toets "stap 3 Good fit op beide delen na Place hinge": OK op 5.3.0 en 5.2.3 (`['groen', 'groen']`). Mijn kan-punt 1 (toets) is daarmee gedaan; het paneelscherm nog niet. | feit (GEZIEN in log) | hoog | |
| 4 | Toets "eerder Tight blijft op zijn eigen deel, ander deel Good fit": OK op 5.3.0 en 5.2.3, uitslag `rechts oranje 0.9 links groen`. | feit (GEZIEN in log) | hoog | |
| 5 | Geen eigen toets voor rood (Too thin). Zelfde codepad als oranje, dus klein risico. | feit | midden | toets met `cj_passing = "rood"` |
| 6 | Zonder oud snijpunt houden beide delen de oude passing. Voorzichtig gekozen: liever een waarschuwing te veel dan een te weinig. | feit (code, architectuur.md) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Run 44512744216 helemaal groen: 5.3.0, 5.2.3 en 4.2.23 (4.2.23 later nagekeken, 11:35 UTC). Geen NIET OK in de logs van 5.3.0 en 5.2.3. | feit (GEZIEN) | hoog | tests groen |
| 2 | Alleen toetsen bijgekomen, niets versoepeld. | feit (diff) | hoog | |
| 3 | `scharnier.py` 286 regels, `toetsen_scharnier.py` 257: onder 400. | feit (wc) | hoog | bestandsgrootte |
| 4 | Alleen betaalde code geraakt; geen persoonsgegevens. | feit | hoog | |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Paneelscherm na het losse Place hinge (zoals 15 tot 19 `-paneel.png`), zodat je "Good fit" ook ziet.
2. `toets_tight_blijft` ook eens met rood draaien (een tweede ronde in dezelfde functie).

Daan
