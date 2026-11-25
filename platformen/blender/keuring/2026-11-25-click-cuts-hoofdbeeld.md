# Keuring hoofdbeeld Click Cuts (paard voor en na), 25 nov 2026, Daan
Wat ik keurde: `ontwerp/cuts-hoofdbeeld/beelden/paard-2400x1200.jpg` en `paard-1920x1080.jpg`, `paard.json`, blinde test `organisatie/blindtest/uitslag/click-cuts-hoofdbeeld-2026-11-25-0059.md` (issue #34)
Akkoord: nee (één moet, klein: één regel tekst)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Alle getallen in het beeld kloppen met `paard.json`: 520 mm hoog, bed 256 mm, 12 parts, 48 pins, 12 keer groen, `alle_passen: true`, grootste stuk 192,8 mm | feit (GEZIEN) | hoog | |
| 2 | "Pins, holes and part numbers on every cut" is te sterk. De add-on meldt bij sommige sneden "Glue this joint" (`split_joints/verbinders.py:111-112`, `verbind_3d.py:153`): daar komt geen pen. Een koper met zo'n model ziet een belofte die niet klopt. De changelog zegt het wel goed: "with pins, pin holes and part numbers" zonder "every". | feit | hoog | |
| 3 | "Every part fits." en "every part fits the bed" kloppen: Split to fit snijdt tot alles past, en de controle zegt het per deel | feit | hoog | |
| 4 | Licentie: Horse Statue 01, Poly Haven, CC0 (staat in `paard.json` en LEESMIJ). Geen AI-beeld, geen foto van een print, geen bewering dat wij printten | feit | hoog | |

## Deel B: regels
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Blinde test GESLAAGD: plek 1,0 bij Gemini en 1,0 bij ChatGPT tegen Cleave, Split 3D Print en SnapSplit | feit (GEZIEN) | hoog | regel 9 |
| 2 | Geen persoonsgegevens, geen AI genoemd | feit | hoog | regel 2 en 5 |

## Deel C: zou een koper het leuk vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Op ±400 px breed (Superhive-lijst) leest "Click Cuts" en "Pick your printer. Click once. Every part fits." goed; de drie regels en de onderschriften zijn dan te klein om te lezen. Niet erg: de korte variant scoorde ook plek 1 tot 1,5 | niets nodig voor live | |
| 2 | Het groene en roze deel tonen zichtbare facetten (hoekige vlakken), de rest is glad. Naast Cleave (echte prints op een snijmat) valt dat op bij 100% | glad renderen (smooth shading of hogere resolutie van het model) bij een volgende versie | klein |
| 3 | Beide rechters vragen hetzelfde: laat zien dat je de snede kunt bijsturen, en een stukje van het echte paneel. Goed voor de galerij, niet voor dit hoofdbeeld | galerijbeeld met paneel en Free cut | midden |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste? | 8 | Naast [Cleave](https://assets.superhivemarket.com/store/product/264651/image/xlarge-40fa5c2d6ae39125cd932fe28b2ddab2.jpeg) (sterk, echte prints): wij zijn duidelijker over het probleem (te groot, gouden doos, 1 click, past). Cleave oogt rijker. |
| Zou ik het kopen op basis hiervan? | 8 | Het probleem en de oplossing staan in 3 seconden in beeld |
| Zou Thijs er trots op zijn? | 8 | Ja, mits de belofte klopt (moet 1) |

## Moet (blokkeert akkoord)
1. Regel 2 in beide formaten: haal "on every cut" weg. Voorstel: "Pins, holes and part numbers added for you" (of "Pins, holes and part numbers on the cuts"). Daarna alleen deze regel nakeuren; geen nieuwe blinde test nodig, want het beeld blijft gelijk en de variant zonder de drie regels slaagde ook.

## Kan
- Facetten op het groene en roze deel glad maken.
- Galerijbeeld met het paneel en bijsturen van de snede (vraag van beide rechters).
