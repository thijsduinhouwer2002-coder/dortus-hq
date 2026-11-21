# Keuring "Where to find it" in de Pro-tekst, 21 nov 2026, Daan
Wat ik keurde: `platformen/blender/superhive/where-to-find-it.md` (Bram, commit 2c05374), namen nagelopen in `producten/blender-gewrichten/click_joints/` op main
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Tabblad "Click Joints" klopt (`bl_category`, paneel.py en betaald/figuur.py r212). | feit | hoog | |
| A2 | Paneel "Figure joints" (figuur.py r208), knop "Figure from rig" (rig.py r595), "More bones (ankles too)" (figuur.py r226), "Or put the 3D cursor on a joint, then:" (r228): letterlijk gelijk. | feit | hoog | |
| A3 | "Place hinge, bends up to:" (scharnier.py r274), vak "Hinge", "Show bend range" en schuif "Bend" (scharnier_boog.py r387, 399, 401): gelijk. | feit | hoog | |
| A4 | "2  Joint" met "Place joint" en "3  Fit and export" met "Export STL/3MF" (paneel.py r79, 85, 89, 119): gelijk. | feit | hoog | |
| A5 | "Skipped: ..." is een melding (rig.py r758, `self.report` WARNING), niet in de lijst. De rechtzetting van "the list tells you why" klopt. | feit | hoog | |
| A6 | Eindstop 30° tot 150° klopt met `eindstop(grens, lo=30, hi=150)` (rig.py r106). | feit | hoog | |
| A7 | De knop "Figure from rig" staat er alleen als de mesh een armature heeft (figuur.py r221). De tekst zegt "Select the rigged mesh first": eerlijk. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen nieuwe belofte; geen "click", "holds a pose" of "print tested". | feit | hoog | eerlijk |
| B2 | Bron van de live tekst met tijd en GEZIEN. Geen persoonsgegevens. | feit | hoog | 2, 5 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | De regel "press N ... Click Joints tab" vangt precies de klacht uit de Split-review. Goed. | | |
| C2 | Het laatste punt is een lange regel met drie plekken. Leest zwaar op Superhive. | Mag als drie korte stukken met puntkomma, zoals nu; of alleen "N panel › Click Joints". | klein |

## Moet / Kan
Moet: niets.
Kan 1: bij "the Bend slider shows up under Hinge" toevoegen "when a hinge part is selected" (het vak verschijnt alleen bij een scharnierdeel).
