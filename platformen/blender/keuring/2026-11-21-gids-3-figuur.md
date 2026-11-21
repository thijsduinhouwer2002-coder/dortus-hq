# Keuring gidspagina 3 (articulated figure uit de rig), 21 nov 2026, Daan
Wat ik keurde: repo dortus, tak `gids-click-joints` efa1606, `click-joints/gids/articulated-figure-3d-print-blender/` plus links (vanaf /click-joints/ en gids 2) en sitemap
Akkoord: nee (twee kleine moets; daarna geen nieuwe keuring nodig, mag dan naar main)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Knop- en paneelnamen kloppen met de code: Figure joints, Figure from rig, More bones (ankles too), Check mesh, Convert to mm, Make watertight, "3 Fit and export", Export STL / Export 3MF (`paneel.py` r. 119), Bend, Shoulder tot Neck. | feit | hoog | |
| 2 | Herkomst klopt: from rig uit Limit Rotation of IK-grens op X, mirror als alleen de andere kant een grens heeft, preset 135 (elleboog, knie) en 90 (enkel), kogel altijd preset (`rig.py` r. 1 tot 14, 131 tot 143; `figuur.py` r. 21 tot 24, 78). | feit | hoog | |
| 3 | Rignamen (Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Daz, gewone namen) staan in `rig.py` r. 3 en 33 tot 40. Mesh heeft Armature-modifier of armature als ouder nodig (`rig.py` r. 225 tot 230, 613). | feit | hoog | |
| 4 | Negen gewrichten (2 schouders, 2 ellebogen, 2 heupen, 2 knieën, nek) zonder More bones; figuur 220 mm (`scherm_mens.py` r. 3). | feit | hoog | |
| 5 | Schermen zijn echt en kloppen met de tekst: voor (knop Figure from rig), na (9 joints · 2 rig · 2 mirror · 5 preset, rechterknie gebogen, titel "Right knee: bends 0° to 120°"), lijst 140° en 120° from rig, rechts mirror (zelf bekeken met Read). | feit | hoog | |
| 6 | **Voorbeeldmelding fout.** De pagina citeert "Skipped: Left hip (too thin here for a ball joint)". Voor heup en schouder vervangt `kogel_reden` die melding (`rig.py` r. 205 tot 216, aangeroepen r. 729): de koper ziet "Skipped: Left hip (no clean spot for a hip ball on this thigh (legs touch or the thigh is short), place it by hand)". | feit | hoog | |
| 7 | **Bewerkt scherm zonder melding.** Figuur 2 heet "Screenshot from ... / After one click", maar het script haalt de groene heupbanden alleen in het beeld weg; de add-on kleurt ze wel. Op een gidspagina ziet de lezer dan iets anders dan in Blender. Voor een lijstplaatje was dat mijn uitweg van 17 nov; op een stap-voor-stap-pagina moet het gezegd worden. | feit | hoog | |
| 8 | "Many rigs only have it on the left side" is niet onderbouwd; we weten het van deze ene rig. | vermoeden | midden | een telling over een paar rigs |
| 9 | "These numbers are measured in Blender, not print tested by us yet" staat erin. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen "clicks" of "holds a pose" als belofte. Prijs $19 gelijk aan /click-joints/. Geen persoonsgegevens. | feit | hoog | opdracht hoofdchat 12:35 |
| 2 | Geen zijwaarts scrollen: scrollWidth 390 op 390 en 1280 op 1280 (Playwright, lokale server, GEZIEN). Links naar pagina 3 vanaf /click-joints/ en gids 2 werken, sitemap heeft de pagina. | feit | hoog | |
| 3 | A7 raakt regel 5 (eerlijk): een bewerkt beeld als schermafdruk tonen. | feit | hoog | CLAUDE.md regel 5 |

## Deel C: zou een lezer het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Sterkste pagina van de drie: het voor-en-na laat in één blik zien wat $19 je oplevert. Telefoonuitsnede van figuur 2 werkt goed. | | |
| 2 | De lijst-uitleg (from rig / mirror / preset) beantwoordt precies de vraag die een koper heeft. | | |

## Moet (blokkeert akkoord)
1. (A6) Voorbeeld vervangen door de echte melding, bijvoorbeeld: `Skipped: Left hip (no clean spot for a hip ball on this thigh ...)`, of een hinge-voorbeeld dat letterlijk zo uit de code komt.
2. (A7, B3) Kies één: (a) figuur 2 opnieuw met `CJ_HEUPBAND=1`, of (b) in het onderschrift "Hip color bands hidden in this image." erbij.

## Kan (mag later)
1. (A8) "Many rigs" wordt "Some rigs" of "This rig".
