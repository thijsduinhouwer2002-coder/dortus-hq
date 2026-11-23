# Keuring blender-gewrichten, terugval naar Exact bij open delen, 23-11-2026, automatische keurder
Wat ik keurde: commit 2560c3a0b (05fa37c..2560c3a), bestanden `click_joints/gewricht.py` en `e2e/toetsen_correcties.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
De opdracht is het bericht "spoor Olaf" uit de commit. Dat bericht staat niet in de aangeleverde tekst, dus ik toets tegen de commitregel en de ontwerpregels over solvers.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij Manifold met open delen snijdt de operator één keer opnieuw met Exact. Pas als dat ook open is, weigert hij met de melding, ruimt hij de hulpcollectie op en blijft het figuur heel. | Feit (diff) | hoog | Niet van toepassing, de logica is in de diff te lezen. |
| 2 | De toets bootst "Manifold geeft open delen" na met `FORCEER_OPEN`. Hij eist bij 1 keer open twee gesloten delen met solver EXACT en bij 2 keer open een nette weigering. | Feit (diff) | hoog | Een groene run in Blender 5.2.3 (4.5+) met de regels `TERUGVAL 1x open` en `TERUGVAL 2x open` in het log. |
| 3 | Het is niet bewezen dat een echte Manifold-fout met Exact wel gesloten delen geeft. De toets forceert de fout alleen. | Vermoeden | midden | Het figuur uit het spoor van Olaf nogmaals plaatsen en zien dat de delen via Exact gesloten zijn. |
| 4 | De tweede poging draait `een_lid.bereid` opnieuw op hetzelfde `werk`. Of `bereid` na `reset()` een schone beginstand geeft, is in deze wijziging niet te zien. | Vermoeden | midden | De toets "1x open" op een figuur met een lid dat bereid echt wijzigt. Controleer ook dat het resultaat gelijk is aan een directe Exact-snede. |
| 5 | `gegevens["cj_solver"]` en `cj_solver_terugval` worden gezet. Dat `gegevens` voor deze regels bestaat en op de delen terechtkomt, is buiten de diff. | Vermoeden | midden | De toetsregel `d.get("cj_solver") == "EXACT"` die in de run slaagt. |
| 6 | De akkoordregel in `ontwerp.md` geldt voor 0.1.1 en 1.0.2 en zegt dat de add-on sinds run 43793388355 niet is veranderd. Deze wijziging verandert de add-on wel, dus dat akkoord dekt haar niet. | Feit | hoog | Een nieuwe groene run en een bijgewerkt akkoord voor de volgende versie. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is niet gewijzigd. Daar staat nog "Manifold op 4.5+, anders Exact" bij `gewricht.py`, zonder de terugval, `cj_solver`, `cj_solver_terugval` en de testhaak `FORCEER_OPEN`. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is alleen een toets toegevoegd. Geen bestaande toets is aangepast of losgemaakt. | Feit (diff) | hoog | Tests niet aangepast om te slagen |
| 3 | De bestandsgrootte van `gewricht.py` en `toetsen_correcties.py` is uit de diff niet te halen. Beide groeien (±25 en ±35 regels). | Vermoeden | laag | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 5 | `CHANGELOG.md` is niet bijgewerkt voor deze zichtbare verbetering (minder mislukte sneden). De sectie Unreleased staat er al. | Feit | hoog | Changelog vanuit de gebruiker geschreven |
| 6 | Het commentaar noemt "1.2.2". Dat past bij geen versie in het ontwerp (gratis 0.1.1, Pro 1.0.2). | Feit | midden | Duidelijkheid van versienummers |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie hier geen beeld of speelervaring, alleen tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een gebruiker merkt niet dat er opnieuw gesneden is. `cj_solver_terugval` staat alleen op het deel. | Een korte infomelding bij de terugval, bijvoorbeeld "Cut retried with the exact solver". | klein |
| 2 | De tweede snede kan bij grote figuren merkbaar langer duren. Het ontwerp noemt een doel van 5 s per gewricht. | Een meting op het figuur van 200K driehoeken met de terugval aan. | klein |
| 3 | Als beide sneden mislukken, geeft de melding het aantal foute randen van de laatste poging. Daar kan een gebruiker niets mee. | Voeg een tip toe, bijvoorbeeld "Try Make watertight or move the cursor a little". | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met de terugval naar Exact, de eigenschappen `cj_solver` en `cj_solver_terugval` en de testhaak `FORCEER_OPEN` (deel B, rij 1).

**Kan**
- Laat een groene run in 5.2.3 zien met de regels `TERUGVAL 1x open` en `TERUGVAL 2x open`. De toets slaat 4.2 over, omdat daar geen Manifold is (deel A, rij 2).
- Controleer dat `een_lid.bereid` na `reset()` een schone beginstand geeft (deel A, rij 4).
- Voeg een regel toe aan Unreleased in `CHANGELOG.md` (deel B, rij 5).
- Haal "1.2.2" uit het commentaar of zet het op het juiste versienummer (deel B, rij 6).
- Voeg een infomelding bij de terugval toe en een bruikbare tip bij de weigering (deel C, rijen 1 en 3).
- Meet de snelheid op het figuur van 200K driehoeken met de terugval aan (deel C, rij 2).
- Zet vóór uitbrengen een nieuw akkoord in `ontwerp.md` voor de versie met deze wijziging (deel A, rij 6).

---
Automatische keurder, model `claude-sonnet-5-5`, 19798 tokens in, 5023 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
