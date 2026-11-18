# Keuring README Click Joints (uiterlijk en belofte), 18 nov 2026, Daan
Wat ik keurde: `producten/blender-gewrichten/repo-click-joints/README.md` en `media/click-joints.gif` op main 8f4a6a7 (concept van Bram, 54a86b3)
Akkoord: ja (18 nov ±21:45 UTC, na herkeuring van de moet op GIF a04e06c). Eerder: nee, één kleine moet (eerste beeld van de GIF).

## Deel A: doet het wat beloofd is?
Toets van de hoofdchat (18 nov): beeld bovenaan, belofte in één zin, gratis tegenover Pro duidelijk. GIF bekeken als blad van 12 en 6 losse beelden met Read (GEZIEN), tijden en helderheid per beeld nagemeten met PIL.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | GIF staat bovenaan, 540x304, 144 beelden van 110 ms (16 s), loopt eindeloos, 1,9 MB. Echte 3D, houten pop, groene ring op de snede, gloed, uitgeklapte onderdelen. Ziet er verzorgd en eigen uit, past bij poster en winkelbeelden. | feit (GEZIEN) | hoog | |
| 2 | **Het eerste beeld is bijna zwart:** een stukje donkere arm van dichtbij, gemiddelde helderheid 7 van 255 (beelden 6 tot 30 zitten op 18, het uitklapbeeld op 65). Dat beeld zie je terwijl 1,9 MB laadt, en GitHub toont alleen het eerste beeld aan wie "minder beweging" aan heeft staan. Dan staat er bovenaan de README een zwart vlak met een stokje. | feit (helderheid gemeten, beeld GEZIEN); hoe vaak het eerste beeld lang blijft staan is vermoeden | hoog / midden | README openen met een trage verbinding of met minder beweging aan |
| 3 | Belofte in één zin, vet, direct onder de GIF: "Click where it should bend, ... and shows how far it bends before you print." Klopt met wat de GIF laat zien (klikken op een plek, buigen, passing). | feit | hoog | |
| 4 | De graden en het rood voorbij de grens staan niet in de GIF; de zin belooft "how far it bends". De lijst eronder zegt het wel. Geen fout, wel een gemiste kans. | feit | hoog | |
| 5 | Gratis tegenover Pro: kopjes "Free" en "Pro, in addition to everything above", prijs en link bij Pro, en "The free Click Joints stays free". In één blik duidelijk. | feit | hoog | |
| 6 | Het label "Exploded view" in de GIF is een pilletje van ±8 px hoog, op 540 breed niet te lezen. | feit (GEZIEN) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens: `thijs@dortus.com` is het zakelijke adres en staat al in de README van Rollwright; de Gumroad-link is de bestaande openbare winkel. | feit | hoog | harde regel 2 |
| 2 | Alleen gratis functies in beeld (geen scharnier met eindstop), dus de GIF belooft niets wat alleen Pro kan. | feit (GEZIEN) | hoog | eerlijk |
| 3 | Regels en claims (versies, prijzen) keurden A en B al; niet opnieuw gedaan. | feit | hoog | |

## Moet (blokkeert akkoord)
1. **Laat de GIF beginnen bij de hele pop** (een beeld rond nummer 6, de pop staat er heel en helder op), niet bij het zwarte stokje. Het makkelijkste: de beelden draaien zodat de lus bij 6 begint en 0 tot 5 achteraan komen; de lus blijft gelijk, alleen het startbeeld verandert. Toets: beeld 0 van de nieuwe GIF heeft een helderheid van minstens 15 en de hele pop staat erin.

## Kan (mag later)
1. Laat in één kort stuk de gradenmeter zien, of rood voorbij de grens, zodat "how far it bends" ook in beeld zit.
2. Het label "Exploded view" twee keer zo groot, of weg.

## Herkeuring moet 1, 18 nov 2026, Daan
Wat ik keurde: `media/click-joints.gif` op a04e06c (Bram).
- Beeld 0 bekeken met Read: de hele houten pop, helder, arm en knie opzij (GEZIEN). Helderheid beeld 0: 17,2 (lat 15), zelf nagemeten met PIL.
- 540x304, 144 beelden van 110 ms = 16,0 s, loop 0 (eindeloos), 1,76 MB (GEZIEN).
- Moet 1: opgelost. Kan 1 en 2 blijven voor een volgende film.
**Akkoord: ja.** De hoofdchat mag README en GIF in de repo click-joints zetten.
