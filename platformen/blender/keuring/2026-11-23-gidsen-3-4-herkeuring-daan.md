# Keuring gidsen 3-4 met fit-test-strip (herkeuring), 23 nov 2026 ±23:25 NL, Daan
Wat ik keurde: repo dortus, tak `claude/gidsen-3-4` op 72a3997 (merge e736f77 van `claude/fit-test-strip` 8624de3, plus K1 tot K3)
Akkoord: ja, fast-forward van main (2e99b6d) naar 72a3997

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigt of weerlegt |
|---|---|---|---|---|
| A1 | main is voorouder van 72a3997, dus één fast-forward (GEZIEN `git merge-base --is-ancestor`) | feit | hoog | |
| A2 | K1 "starting points, not print tested by us yet", K2 "resin parts can come out", K3 "Print it as it lies" staan er letterlijk, verder niets in 72a3997 veranderd (3 regels in gids 4) | feit | hoog | `git show 72a3997` |
| A3 | Wat meegaat naar main buiten gids 3 en 4: fit-test-strip (466e421, 2493a29, 8624de3), direct-zip site (66d6031, b1050f4), gids 2 en 3 (adfb519 e.a.). Allemaal eerder door mij gekeurd (logboek 23 nov) | feit | hoog | ontwerp/logboek.md |
| A4 | Alle interne links in alle html-bestanden op 72a3997 wijzen naar een bestaand bestand; enige uitzondering `/privacy`, die al op main staat en door GitHub Pages naar privacy.html gaat | feit | hoog | lijst-script over `git ls-tree` |

## Deel B: regels
Geen persoonsgegevens, geen nieuwe cijfers. Niets op te merken.

## Moet / Kan
Moet: geen. Kan: geen nieuwe.
