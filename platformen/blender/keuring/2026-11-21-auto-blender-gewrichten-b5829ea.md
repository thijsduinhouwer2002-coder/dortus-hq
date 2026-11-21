# Keuring blender-gewrichten, gidsscript scharnier (schermen voor gidspagina 2), 21-11-2026, automatische keurder
Wat ik keurde: commit b5829ea87 (reeks 7f3b812..b5829ea), alleen `producten/blender-gewrichten/e2e/scherm_gids_scharnier.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt de add-on niet: er is alleen een nieuw script dat drie schermen maakt (g1-voor, g2-pose, g3-voorbij). Het akkoord van Daan voor 0.1.1 en 1.0.2 blijft dus gelden. | Feit | hoog | De diff toont één nieuw bestand onder `e2e/`. |
| 2 | Het script gebruikt `sp.been()`, `sp.SPELING`, `plaats_scharnier(stand="115")`, `cj_scharnier_boog`, `cj_scharnier_pose` en `toon_bereik`. In de tekst kan ik niet zien of die bestaan en zo heten. | Vermoeden | midden | Een groene run van het script in de betaalde build met "GIDS OK" voor alle drie de plaatjes. |
| 3 | De commitregel zegt ook "gids 1 klaar voor main" en "gidspagina 2 ter keuring". De gidspagina's zelf zitten niet in deze diff, dus die kan ik niet keuren. | Feit | hoog | De pagina's of hun bestanden bij de keuring meesturen. |
| 4 | Het derde plaatje moet "3 graden voorbij de stop, rood" laten zien. Het script logt alleen het aantal rode vlakken en eist niet dat dat groter dan 0 is. | Vermoeden | midden | Het logregel `rood_vlakken=` met een waarde groter dan 0, en het plaatje zelf. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast of verzwakt. Alleen een nieuw schermenscript. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is 116 regels. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Het gaat om een los hulpscript voor de site, geen onderdeel van de add-on. Een regel over de e2e-schermen zou netter zijn. | Feit | hoog | architectuur.md bijgewerkt (kan) |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in het script. | Feit | hoog | Geen persoonsgegevens |
| 5 | De plaatjes komen uit de echte Blender via een schermopname (`import -window root`), dus geen AI-beeld. De docstring zegt "alleen voor de site", dus ze komen niet op extensions.blender.org. Dat is goed, want ze tonen betaalde functies. | Feit | hoog | Geen AI-beeld; alleen gratis functies op extensions.blender.org |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Ik kan de plaatjes niet zien. Of het houten been en de zijbalk duidelijk leesbaar zijn, blijft een vermoeden. Daan moet ze bekijken. | Daan bekijkt g1, g2 en g3 voor ze op de gids komen. | klein |
| 2 | Alle drie de plaatjes gebruiken dezelfde camerahoek (25 graden, 12 graden). Naast elkaar kan dat saai of weinig onderscheidend overkomen. Dat is wel handig om te vergelijken. | Eventueel bij g3 een iets dichtere camera op de rode plek. | klein |
| 3 | De "voor"-stand (g1) toont het been heel. Een kijker ziet pas in g2 wat de add-on doet. | Een bijschrift op de gids dat uitlegt wat er tussen g1 en g2 gebeurt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Na `wiel_naar_tabblad` controleren of het tabblad echt gelukt is. Nu gaat het script na 14 pogingen gewoon door en kan het een plaatje van het verkeerde tabblad maken.
- Het script laten falen (afsluiten met een foutcode) als een plaatje ontbreekt of `import` niet bestaat. Nu staat alleen "GIDS FOUT" in het log, en een andere fout in de timer laat Blender open hangen tot de CI-timeout.
- In het log eisen dat `rood_vlakken` groter dan 0 is bij g3 (zie A4).
- Een regel over de gidsschermen in `architectuur.md`.
- Voor de gidspagina's zelf (A3) een aparte keuring, plus Daan op uiterlijk, voor ze live gaan.

---
Automatische keurder, model `claude-sonnet-5-5`, 19419 tokens in, 3587 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
