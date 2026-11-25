# Keuring loopbeelden helden Hats, 25 nov 2026, Daan
Wat ik keurde: commit 4341d40 (alle vier) en 5339c96 (ridder en heks), `producten/steam-hol/bewijs-loop/` (GIFs op ware maat en 2x, `bladen-2x.png`), `godot/kunst/3d/sprites.json` (issue #35)
Akkoord: ja op de beelden. Nog niet af voor de speler: zie moet 1 (los van deze keuring, voor de eigenaar van het spel).

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen |
|---|---|---|---|---|
| 1 | 12 beelden per soort, alle helden kijken naar rechts, de kant waarheen ze lopen: de maanloop is weg | feit (beeld voor beeld bekeken) | hoog | |
| 2 | Ridder (5339c96): benen wisselen duidelijk, hij zakt door per stap, schild laat de benen vrij. Niet meer stijf | feit | hoog | |
| 3 | Heks (5339c96): bruine laarsjes stappen onder de mantel uit, de zoom zwaait mee. De benen vallen niet meer weg | feit | hoog | |
| 4 | Dief laag en voorover met lange stappen, bard rechtop met een hupje: leest per soort | feit | midden | |
| 5 | Voeten tegen de streepjes: in de GIFs staat de steunvoet op het oog stil. Ik heb het niet per pixel gemeten | vermoeden | midden | voet-x per beeld meten in de GIF |
| 6 | Hoed: de sprites zijn zonder hoed (HOL_VERBERG); het spel zet de hoed erop met `kruin` per beeld, zodat hij met het hoofd meegaat. Zonder hoed lijken ridder en heks op elkaar (kaal hoofd); de soort lees je dus pas in het spel | feit (sprites.json, held.py) | hoog | GIF uit het spel met hoed |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Snelheden in LEESMIJ met GEZIEN en bron | feit | hoog | regel 5 |
| 2 | Ridder en heks GIFs uit een snelle render (kwart samples); de bladen komen op volle kwaliteit uit de workflow. Eerlijk vermeld | feit | hoog | |

## Deel C: zou een speler het leuk vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het spel gebruikt `stap_px` en `loop_fps` nog niet (gezocht in `godot/**/*.gd`: geen treffer). De helden lopen nu 8 spelpx/s; de bladen zijn gemaakt voor 2,6 tot 7,4. In het spel glijden de voeten dus nog, en dat ziet een speler als goedkoop | held.gd laten lopen met `stap_px` x `loop_fps` per soort | klein |
| 2 | Ridder en heks lopen even snel (2,6 spelpx/s): ridder zwaar en heks glijdend is goed, maar dezelfde tred naast elkaar kan herhalend voelen | heks iets ander tempo (bijv. 9 fps) | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom |
|---|---|---|
| Top, op het niveau van de beste? | 8 | Schattige, leesbare loop op ±30 px; vier duidelijk verschillende tredes. Naast de helden in Rusty's Retirement en Bongo Cat (lat `organisatie/lat/hats.md`) houdt het stand |
| Zou ik het spelen op basis hiervan? | 8 | Ja, de helden voelen levend |
| Trots, Thijs? | 8 | Ja, zodra moet 1 in het spel zit |

## Moet (voor het spel, niet voor deze beelden)
1. `stap_px` en `loop_fps` uit `sprites.json` gebruiken in het spel, anders glijden de voeten alsnog. Bewijs: GIF uit het echte spel (met hoed) waarin de steunvoet stil staat.

## Kan
- Heks een eigen tempo.
- Voet-x per beeld meten en in LEESMIJ zetten als bewijs voor "glijdt niet".
