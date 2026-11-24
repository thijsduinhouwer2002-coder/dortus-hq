# Keuring blender-gewrichten (kan A3, weggevallen voet), 24-11-2026, automatische keurder
Wat ik keurde: commit 249647626 (3cd52e7..2496476): `click_joints/betaald/rig.py` (alleen een commentaar) en `e2e/toetsen_robot_meer.py` (nieuwe toets)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De opdracht is het "Kan" van Daan bij Pro 1.2.6: toets dat het vangnet een weggevallen voet nog vangt. De nieuwe functie `weggevallen_voet` doet dat. Ze meet het verlies met alleen de scheen en met scheen plus voet, en eist boven 6% in het eerste geval en op of onder 6% in het tweede. | Feit (diff) | hoog | Niet nodig. |
| 2 | De rig.py-wijziging is alleen een commentaar. De add-on werkt dus hetzelfde en het akkoord van Daan voor 1.2.6 (tak 6dc287f) blijft gelden. | Feit (diff) | hoog | Een `git diff` op de zip-inhoud zonder commentaar. |
| 3 | De uitslag "bol 25,9 mm, 32 en 35% zonder voet, 0% met voet" komt uit een lokale run op 5.3.0. Een CI-run in 4.2.23, 5.2.3 en 5.3.0 staat niet in de tekst. | Vermoeden | midden | Een groene e2e-run op de nieuwe commit, met de regels `A3 Left ankle` en `A3 Right ankle` in het log. |
| 4 | De toets pakt voet en scheen via `fig.lees(d)` en de naam "Left ankle" of "Right ankle". Ze eist daar precies twee delen en meldt anders een fout. Of dat op de robot klopt, kan ik uit de tekst niet halen. | Vermoeden | midden | De run op de robot, zonder de fout "voet en scheen niet te vinden". |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is nieuw en er is geen toets aangepast of versoepeld om te slagen. De grens `VERLOREN_MAX` (6%) is bestaand en wordt alleen gelezen. | Feit (diff) | hoog | Tests niet aanpassen om te slagen: voldaan. |
| 2 | De toets rekent de bol zelf uit (`max(0.6 * lengte, 15 * u)`) en leest hem niet uit rig.py. Verandert de formule in rig.py, dan blijft de toets groen terwijl ze iets anders meet. | Feit (diff) | hoog | Kan, geen blokkade. |
| 3 | Het commentaar noemt eerst "±48%" en nu "32 tot 35%" voor een weggevallen voet. Er staat niet waarom dat verschilt, en de getallen hebben geen label GEZIEN, DERDEN of GOK. | Feit (diff) | hoog | Cijfers met GEZIEN/DERDEN/GOK. Kan. |
| 4 | `rig.py` is minstens 693 regels lang, want de hunk begint daar. Dit was al zo vóór deze commit, en de wijziging zelf is één regel. | Feit (regelnummer in diff) | midden | Bestanden onder ±400 regels. Kan, voor later splitsen. |
| 5 | De toets maakt kopieën en een samengevoegd object. Ze ruimt het object op en zet `cj_deel` terug. De losse mesh-kopieën van de voet en scheen blijven mogelijk als wees-data achter. Dat doet er in een wegwerp-Blender niet toe. | Vermoeden | laag | Kan. |
| 6 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. `architectuur.md` hoeft niet bij te werken, want er verandert geen gedrag. | Feit (diff) | hoog | Geen persoonsgegevens, architectuur bijgewerkt: voldaan. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De wijziging raakt alleen een toets en een commentaar. Er is niets te zien of te spelen, dus ik kan hier niets over de gebruiker zeggen. | Niet van toepassing. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Wacht op een groene CI-run in 4.2.23, 5.2.3 en 5.3.0 voordat je de toets als bewezen telt. Nu is er alleen een lokale run op 5.3.0.
2. Laat de toets de bolmaat uit één gedeelde functie in rig.py halen in plaats van de formule te kopiëren.
3. Zet GEZIEN voor de gemeten percentages in het commentaar en leg in een regel uit waarom het getal van ±48% naar 32 tot 35% ging.
4. Splits `rig.py` later onder de ±400 regels.

---
Automatische keurder, model `claude-sonnet-5-5`, 20205 tokens in, 3336 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
