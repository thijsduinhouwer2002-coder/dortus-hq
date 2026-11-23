# Keuring blender-gewrichten (toets Labels en rood deel B), 23-11-2026, automatische keurder
Wat ik keurde: commit 89b6cd117 (alleen `producten/blender-gewrichten/e2e/toetsen_figuur.py`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt alleen een toets toe (`mooier`). Die controleert de schakelaar Labels (Selected, None, All, los gewricht) en dat voorbij de stop heel deel B rood wordt en daarbinnen terugkeert. Dat past bij de titel "Pro mooier". | Feit | Hoog | n.v.t. |
| 2 | Of de toets slaagt, kan ik niet zien. Er staat geen run of log bij. | Vermoeden | Midden | Een groene run van de e2e-workflow op deze commit, met de regels van `mooier` in het log. |
| 3 | De commit zegt dat e2e ook op de tak `pro-mooier` draait. Het workflowbestand zit niet in de wijziging. | Vermoeden | Midden | Een `.github/workflows/*.yml` in een andere commit met `pro-mooier` bij de takken, of een run op die tak. |
| 4 | De toets roept `labels.toon(ctx, a, b)`, `labels.met_naam` en `beweeg.pose` aan zonder dat ik de code zie. Dat de namen en argumenten kloppen, blijkt alleen uit een run. | Vermoeden | Laag | Een groene run, of de Pro-modules `labels.py` en `scharnier_beweeg.py` inzien. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er wordt geen bestaande toets aangepast of versoepeld. De wijziging voegt alleen een aanroep en een nieuwe functie toe. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is met deze toevoeging nog ver onder de ±400 regels, voor zover uit de diff te schatten. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet aangepast. Het is een toetswijziging, dus dat hoeft hier niet. In het zichtbare deel staat Labels of rood deel B ook niet. | Vermoeden | Laag | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan niets zien of spelen. Of boog, label en rood deel B er goed uitzien, kan alleen Daan beoordelen op een schermafbeelding. | Een schermafbeelding van Selected, All en de rode stand op de tak `schermen`. | Klein |
| 2 | De toets zet de selectie op "niets" en laat die zo achter. Latere stappen in `main` kunnen daarvan afhangen. | Aan het eind van `mooier` de selectie herstellen, of `a` weer actief maken. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bevestig dat de e2e-run op deze commit groen is, ook op de tak `pro-mooier` (deel A 2 en 3).
- Laat `mooier` de selectie en `cj_labels` terugzetten (de huidige selectie en actieve object, ook de eerdere stand), zodat de rest van `main` niet verandert door deze toets (deel C 2).
- Laat Daan de uitkomst beoordelen op een schermafbeelding (deel C 1).

---
Automatische keurder, model `claude-sonnet-5-5`, 18626 tokens in, 2411 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
