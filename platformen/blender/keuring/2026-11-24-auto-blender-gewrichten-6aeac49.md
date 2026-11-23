# Keuring blender-gewrichten, herkeuring betrouwbaar-rig A, 24-11-2026, automatische keurder
Wat ik keurde: commit 6aeac4923, bestand `producten/blender-gewrichten/keuring/2026-11-24-betrouwbaar-rig-A.md` (alleen een keuringstekst, geen code)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt alleen een herkeuring toe. De add-on, het ontwerp en de changelog blijven gelijk, dus er verandert niets voor de gebruiker. | Feit | Hoog | Het bestandenlijstje bevat één markdownbestand. |
| 2 | De herkeuring zegt dat er tussen 1945f46 en 37de78bce niets meer verandert in `click_joints/`. Daardoor zou de meting op 1945f46 voor de eindstand gelden. Dat kan ik uit deze tekst niet nagaan. | Vermoeden | Midden | `git diff 1945f46 37de78bce -- click_joints/` zou leeg moeten zijn. |
| 3 | De cijfers in de herkeuring (60 van 60 in 5.x, 51 van 60 in 4.2, verlies onder 6%) kan ik niet nalopen. Ze zijn intern consistent en het document noemt de runs, dus ze zijn controleerbaar. | Vermoeden | Midden | De JSON van run 45282711505 zou deze tellingen moeten geven. |
| 4 | De e2e voor 4.2.23 is nog niet klaar, zegt het document zelf: de job hangt op stap 18 en de e2e op 25efd95 en 37de78bce loopt nog. Toch staat er "Akkoord: ja". Voor deze tekstwijziging is dat te verdedigen, voor uitbrengen niet. | Feit | Hoog | Een groene e2e op de eindcommit in 4.2.23. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen code of toets aangepast om te slagen. Het document zegt zelfs dat toets `CJ_HERKANS=3` zwak is. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Er is geen persoonsgegeven, sleutel of wachtwoord te zien. Het document zegt dat de GitHub-API "zonder sleutel" is gebruikt. | Feit | Hoog | Geen persoonsgegevens |
| 3 | `architectuur.md` hoeft hier niet mee te veranderen, want er is geen code gewijzigd. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | Feit en vermoeden zijn per punt gescheiden, met zekerheid erbij. Dat past bij het formulier, al mist het document de vaste kopjes A, B en C. | Feit | Hoog | Formulier keuren |
| 5 | In kan 3 staat "eindcommit (45288814521)". Dat lijkt een run-id en geen commit, wat verwarrend is. | Vermoeden | Laag | Duidelijkheid, geen harde regel |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen. De Engelse zinnen in `redenen.py` heeft Daan nog niet gezien, zoals het document zelf zegt. | Daan laat die zinnen nakijken voor het uitbrengen. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Voordat er wordt uitgebracht moet de e2e op de echte eindcommit helemaal groen zijn, ook in 4.2.23. Nu loopt hij nog en hangt de 4.2-job.
2. De toets `CJ_HERKANS=3` slaagt ook als het terugdraaien kapot is, zegt de herkeuring (H3). Maak hem scherper met een 50% nep op een snede die anders blijft staan, bijvoorbeeld de nek of een heup.
3. De releasenote moet "some knees" veranderen in "some knees, shoulders and hips" (H8), voordat Daan hem keurt.
4. Controleer met `git diff` dat `click_joints/` echt gelijk bleef tussen 1945f46 en 37de78bce. Ik kon dat uit tekst niet bevestigen.
5. Verwijs in de tekst naar een echte commit-hash in plaats van een run-id, zodat "eindcommit" niet verwarrend is.

---
Automatische keurder, model `claude-sonnet-5-5`, 19743 tokens in, 2601 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
