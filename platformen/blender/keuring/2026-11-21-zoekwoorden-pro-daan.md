# Keuring zoekwoorden en tags Click Joints Pro, 21 nov 2026, Daan
Wat ik keurde: `platformen/blender/superhive/zoekwoorden.md` (Bram, commit dc08923), zinnen nagelopen in `producten/blender-gewrichten/click_joints/` op main, live tags met curl
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | 9 gewrichten uit de rig: STANDAARD = schouders, ellebogen, heupen, knieën, nek (rig.py r20), 2+2+2+2+1. "articulated / poseable / action figure" klopt. | feit | hoog | |
| A2 | Kogel op schouder, heup, nek; scharnier met eindstop op elleboog en knie (figuur.py r5 en r25, rig.py r8 tot 12). "ball and socket" en "hinge with end stop" kloppen. | feit | hoog | |
| A3 | Rigify en Mixamo staan in de herkende namen (rig.py r3, VOORVOEGSELS) en er zijn proeven voor (e2e/proef_rigify.py, toetsen_rig.py). | feit | hoog | |
| A4 | Knop "Export {STL/3MF}" (paneel.py r118 tot 119). Clearance staat in het paneel. | feit | hoog | |
| A5 | Live tags nu 12: 3d-printing, 3mf, action-figure, articulated-figure, ball-joint, hinge, joints, miniatures, posable, poseable, rig-to-print, stl (GEZIEN, curl op de productpagina 21 nov). Klopt met wat Bram schrijft. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen "print in place", "flexi", "miniature", "click" of "snap": goed weggelaten, geen ongeteste belofte. | feit | hoog | eerlijk |
| B2 | Effect gemarkeerd als GOK; meting Afkijker als GEZIEN met bron. Geen persoonsgegevens. | feit | hoog | 2, 5 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | "poseable action figure STL" trekt ook mensen die een kant-en-klaar STL zoeken. Niet onwaar (je exporteert STL), wel een kans op teleurgestelde klikkers. | Mag blijven; de titel zegt meteen dat het een add-on is. | geen |
| C2 | De tag "articulated-figure" (waar we nu 6e staan) wordt "articulated figure blender". Of Superhive dat als dezelfde tag telt weet ik niet (GOK). | Vervang de losse tag `articulated` door precies `articulated figure`, zodat de oude tag blijft. "articulated" staat straks toch al in titel en tekst. | klein |

## Moet / Kan
Moet: niets.
Kan 1: tag `articulated` vervangen door `articulated figure` (C2).
Na een dag dezelfde meting opnieuw (tabel in split-3dprint.md), samen met de nieuwe titel.
