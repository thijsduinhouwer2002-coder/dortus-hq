# Keuring gedeelde opname-hulpcode, 24 nov 2026, Daan
Wat ik keurde: `commercie/filmpjes/opname/blender_opname.py`, `proef_tip12.py`, `.github/workflows/opname-gedeeld-proef.yml` (Olaf), tegen `commercie/filmpjes/regisseur-12/tip_opname.py`. Run 45318804778: completed success op b168522 (GEZIEN via de Actions-API); de bestanden zijn sindsdien niet veranderd.
Akkoord: ja, geen moet

## Deel A: doet het hetzelfde?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | `ocr` is gelijk aan het origineel op de bestandsnamen na (nu per tag, zodat twee opnames elkaar niet overschrijven). | feit (diff) | hoog | |
| A2 | `menu_pad(["File","Export","STL"])` doet stap voor stap wat regisseur-12 met de hand deed: zelfde drempels, zelfde horizontale beweging (+330) het submenu in, zelfde twee keer Escape bij een mis. Het eerste zoekvak is iets ruimer (x -200, breedte 900 in plaats van -100 en 800); dat kan alleen meer vinden. | feit | hoog | |
| A3 | Mist de eerste knop, dan geen Escape (origineel wel). Er is dan niets geopend, dus goed. | feit | hoog | |
| A4 | De proef vergelijkt delen, maten en aantal beelden met release regisseur-12 en faalt bij verschil. Groen. | feit | hoog | |

## Deel B: regels en veiligheid als algemeen menupad
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Workflow: `contents: read`, geen release, geen plaatsing. | feit | hoog | |
| B2 | Pad van één stap: na de eerste klik slaat de lus over en volgt een tweede klik op dezelfde knop, dus het menu gaat open en weer dicht. | feit | hoog | robuust |
| B3 | Bij vier of meer niveaus: twee Escapes sluiten misschien niet alles als Blender per Escape één niveau sluit. Nu alleen met drie niveaus gebruikt. | vermoeden | laag | robuust |
| B4 | Submenu dat links uitklapt (rand van het scherm): het zoekvak rechts mist, dus Escape en False. Faalt veilig. | feit | midden | |
| B5 | Dubbelzinnige naam (twee regels met hetzelfde woord in het zoekvak): de eerste regel van tesseract wint, meestal de bovenste. Bij gewone exportnamen geen probleem. | feit | midden | |
| B6 | Bestanden onder 450 regels; `blender_opname.py` 445, net onder de grens van ±400 plus marge. Bij groei splitsen. | feit | hoog | bouwen.md |

## Moet
Geen.

## Kan
- K1 (B2): bovenaan `menu_pad` een `if len(pad) < 2: raise ValueError(...)` of een pad van één stap gewoon één klik laten zijn.
- K2 (B3): Escape zo vaak als er niveaus open zijn (`i - 1`), dat kost niets.
- K3 (B5): zeg in de docstring dat je de volle tekst van het item geeft, bv. "STL (.stl)", als een woord vaker voorkomt.
- K4: `woord` buiten de reeks geeft een IndexError in `ocr`; kleine check.
