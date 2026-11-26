# Worm en mot in de huisstijl (Mila, 26 nov 2026, issue #179)

Model `modellen/beestjes.py` (3D uit code in Blender, geen AI, geen gekocht pakket), bladen uit de pijplijn:
- `godot/kunst/3d/worm.png` (184 x 40, 4 beelden: op, piek, links, rechts; cel 10 x 10 spelpixels, 30 px op strook 120)
- `godot/kunst/3d/mot.png` (86 x 28, 2 beelden: open, dicht; cel 10 x 7 spelpixels)
Gegevens per beeld (anker, nul_y, kruin) staan in `godot/kunst/3d/sprites.json`. Elk deel heeft een donkere rand (omgekeerde schil), zoals vat en schedel lezen.

## Beelden
- `strook120-1x.png`: ware maat, in een gangbeeld van build 3fddb22 (strook 120). `strook120-2x.png`: hetzelfde op 2x.
- `alle-beelden-1x.png` en `-6x.png`: alle 6 beelden op gangkleur.
- Let op: de dieren zijn er in Python ingeplakt (bilineair, zoals Godot ze lineair tekent), niet in het spel zelf; dat doet Olaf.

## Blinde lezer (GEZIEN, 26 nov, een losse Claude zonder hint, alleen de uitsneden `blind2-*`)
Ronde 1 (worm 7 x 7, mot 7 x 5): worm op 1x "kleine roze vlek", pas op 4x "worm"; mot open op 1x "moth", mot dicht op 1x "vogel of blad". Niet goed genoeg: worm groter en strepen donkerder, mot dicht minder hoog.
Ronde 2 (nu): eerst 1x opgeschreven, dan 2x.
- p (worm, op): 1x "worm", 2x "earthworm, coming up out of a hole".
- q (worm, links): 1x "worm", 2x "earthworm, with big eyes".
- r (mot, open): 1x "moth" (tweede gok vlinder), 2x "moth".
- s (mot, dicht): 1x "moth" (tweede gok vlinder), 2x "moth".
Zijn slotzin: "The two worms and the two moths are recognisable at 1x already."

## CPU
GOK: twee kleine bladen (samen ±8 kB als PNG); ze tekenen alleen tijdens hun moment, net als de vleermuis (12 beelden per s). Meten kan pas als Olaf ze in `systemen/leven.gd` zet; eis uit #179: hooguit +1 procent.
