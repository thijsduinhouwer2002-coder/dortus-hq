# Keuring gidspagina 1 (ball joint in Blender), 21 nov 2026, Daan
Wat ik keurde: repo dortus, tak `gids-click-joints` commit 373c858, `click-joints/gids/ball-joint-3d-print-blender/index.html` en de 4 schermen. Bekeken in Chromium op 1280 en 390 breed.
Akkoord: ja

## Deel A: doet het wat beloofd is? (opdracht hoofdchat 21 nov 12:35 NL)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Alle knop- en meldingnamen bestaan in de gratis add-on: Check mesh, Convert to mm, Make watertight, Ball, Diameter, Auto, Clearance, Place joint, Good fit, Tight, Too thin, Bends, Bend, past limit, Exploded view (grep in `producten/blender-gewrichten/click_joints/`, niet in `betaald/`). | feit | hoog | |
| A2 | Getallen kloppen met de code: Tight onder 1.5, Too thin onder 0.8 mm (`passing.py` r6-7), Auto 60% en stappen van 0.5 mm (r18-19), speling 0.20 standaard (ook zichtbaar in de schermen). | feit | hoog | |
| A3 | Schermen zijn echt: Blender-viewport met het paneel "Click Joints", waarden in scherm 2 (Wall 1.54, Clearance 0.20 measured, Bends ±20°) gelijk aan het onderschrift; scherm 4 toont "+8° past limit" in rood. | feit | hoog | |
| A4 | "not print tested by us yet" staat er letterlijk in. "click" alleen als werkwoord voor een knop en in "not a promise that your print clicks"; geen "holds a pose". | feit | hoog | |
| A5 | Schermen tonen "Report a problem" onderaan; dat zit pas in 0.1.2, de live 0.1.1 heeft het niet. Verder gelijk. Een lezer ziet één knop meer: geen schade. | feit | hoog | zodra 0.1.2 live is, vervalt dit |
| A6 | Pro-prijs $19 gelijk aan de voorpagina van dortus.com. | feit | hoog | |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen zijwaarts scrollen: scrollWidth 1280/1280 en 390/390. | feit | hoog | kijken |
| B2 | Geen persoonsgegevens. Merkregel Blender Foundation staat onderaan. | feit | hoog | 2 |

## Deel C: zou een lezer het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Op de telefoon (390) is het paneel in de schermen onleesbaar klein; juist dat paneel is het bewijs. | Op telefoon een uitsnede van alleen het paneel (bv. `<picture>` met een bijgesneden versie onder 600 px). | klein |
| C2 | In scherm 1 en 2 staat "Exploded view" aan (blauw), terwijl het onderschrift bij scherm 3 zegt dat dat de uitgeklapte weergave is. Lezer kan denken dat het altijd aan moet. | Bij de volgende CI-opname scherm 1 en 2 met Exploded view uit. | klein |
| C3 | Onderschrift "Green ring: good fit": het groen is de hele snijband, geen ring. | "Green: good fit." | klein |
| C4 | Sterk: opent met de drie fouten die je pas na het printen ziet, en geeft de getallen ook aan wie met de hand werkt. Dat wekt vertrouwen. | | |

## Moet / Kan
Moet: niets. Mag naar main.
Kan: C1, C2, C3.
