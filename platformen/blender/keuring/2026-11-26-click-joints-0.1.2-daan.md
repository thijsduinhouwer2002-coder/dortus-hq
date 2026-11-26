# Keuring Click Joints gratis 0.1.2, 26 nov 2026, Daan
Wat ik keurde: commit e6c73f4 (issue #127, opdracht #115), beide zips in `producten/blender-gewrichten/uitgave/`, e2e-run 45728117479
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigt of weerlegt |
|---|---|---|---|---|
| 1 | Grens klopt: 6.1 verbiedt "text labels prompting users to purchase anything" in de Blender UI, 6.3 verbiedt UI om "commercial versions" te promoten (curl 26 nov, "Last updated: 10 August 2026"). Extensions-zip bevat geen Gumroad, Superhive, Pro of Upgrade; alleen dortus.com in maintainer en website van het manifest, dat mag. | feit | hoog | grep in uitgepakte zip |
| 2 | Enige verschil extensions-zip en direct-zip: `__init__.py` en `direct.py` (alleen in direct). | feit | hoog | diff -rq |
| 3 | Reviewregel in de extensions-zip linkt alleen naar de eigen reviewpagina op extensions.blender.org. Geen reclame, geen andere extensie. | feit | hoog | meld.py regel 58 |
| 4 | Manifest 0.1.2, tagline en tag Sculpt zoals gevraagd. | feit | hoog | diff |
| 5 | Voetfix zit echt in de gratis code (`een_lid.py`, controle op volume en kader na de UNION), dus de Fixed-regel in de changelog is waar. | feit | hoog | diff 0.1.1-zip tegen 0.1.2-zip |
| 6 | sha256 van beide zips gelijk aan `platformen/blender/indienen.md`. | feit | hoog | sha256sum |
| 7 | E2e 45728117479 op e6c73f4: 4.2.23, 5.2.3, 5.3.0 en beeldbericht allemaal success. | feit | hoog | gh api jobs |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | toets_zips: alleen de manifest-sha bijgewerkt, met uitleg; geen test losser gemaakt. | feit | hoog | tests niet aanpassen om te slagen |
| 2 | Changelog zonder AI, zonder Pro, onder 1024 tekens. | feit | hoog | update-tekst |

## Deel C
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Changelog: "Click a store or the X" terwijl er in deze versie maar één winkel staat. | "Click the link or the X" | klein |

## Moet / Kan
Moet: geen.
Kan: C1, mag ook in 0.1.3.
