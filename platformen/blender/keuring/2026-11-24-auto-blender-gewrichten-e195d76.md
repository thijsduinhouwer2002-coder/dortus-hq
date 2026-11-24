# Keuring blender-gewrichten, 24-11-2026 13:32 NL, automatische keurder
Wat ik keurde: commits 9057e2f..e195d76, alleen `producten/blender-gewrichten/ontwerp.md` (één nieuwe regel "Akkoord: ja" bovenaan)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen het ontwerpbestand: er is een akkoordregel voor Pro 1.2.6 (robot-enkels) bijgekomen. Er is geen code, add-on of winkeltekst veranderd, dus er is niets nieuws om tegen de belofte te toetsen. | Feit | hoog | Het diff-overzicht (één bestand, één toegevoegde regel plus lege regel). |
| 2 | De regel noemt tak `claude/blender-pro-1.2.6-robot-enkels` 6dc287f en e2e-run 45384569641, groen in 4.2.23, 5.2.3 en 5.3.0. Ik kan dat niet nakijken, want de run en de tak zitten niet in deze wijziging. | Vermoeden | midden | Het log van run 45384569641 en `git diff` van 6dc287f tegen de gekeurde add-on. |
| 3 | De regel verwijst naar `platformen/blender/keuring/2026-11-24-daan-middag.md` deel 1. Dat bestand is niet meegestuurd, dus ik kan de inhoud van Daans oordeel niet controleren. | Vermoeden | midden | Dat keuringsbestand lezen: staat daar echt "ja" voor 1.2.6 en dezelfde "kan" over de hap in de hiel? |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast en geen code gewijzigd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | In de wijziging staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | hoog | Geen persoonsgegevens |
| 3 | Het akkoord noemt het bewijs (tak, commit, run-id, drie Blender-versies) en de "kan" apart. Dat is de vaste vorm van de eerdere akkoordregels. | Feit | hoog | Akkoord van Daan bovenaan `ontwerp.md` bij uiterlijk |
| 4 | De commit heet "zes keuringen (...), logboek", maar in deze wijziging zit alleen de 1.2.6-regel. De andere vijf (Click Cuts M1, Docs-tab, review-zin, Ebb, video guide) horen bij andere producten of bestanden en zijn hier niet gekeurd. | Feit | hoog | Alleen het meegestuurde bestand telt voor deze keuring |
| 5 | `ontwerp.md` is erg lang geworden met een stapel oude akkoordregels. Dat is een leesbaarheidskwestie, geen regelbreuk, want de 400-regelsgrens geldt voor code. | Vermoeden | laag | Het regelaantal van `ontwerp.md` (niet meegestuurd) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging, dus ik kan hier niets over de gebruikerservaring zeggen. | Beeld en gevoel van de robot-enkels keuren Daan en Iris op de echte add-on. | klein |
| 2 | De "kan" uit het akkoord (hap uit de hiel van de blokvoet kleiner) is iets wat een gebruiker na 30 seconden kan opvallen. | Die hap in een volgende patchversie verkleinen, zoals Daan al noemde. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de akkoordregel dat de run en tak niet in deze commit zitten, of link naar het logbestand, zodat een volgende keurder het sneller kan nakijken.
- Overweeg de oude akkoordregels van `ontwerp.md` naar een eigen geschiedenisbestand te verplaatsen, zodat het huidige akkoord direct leesbaar blijft.
- Verklein de hap uit de hiel van de blokvoet (al als "kan" genoemd door Daan).

---
Automatische keurder, model `claude-sonnet-5-5`, 17925 tokens in, 1705 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
