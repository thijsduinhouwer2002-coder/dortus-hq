# Graafmoment in de 3D-stijl (Daan, 14 nov 2026)

Waarom: in de echte strook van main (run 43553365825) is het hol helemaal 3D, maar een cel die je graaft brokkelt nog open met paarse 2x2-stippen, pixelsteentjes en ronde stofvlekken uit `hol.gd` `_brokkel()`. Dat is het moment waarop de speler zelf iets doet, dus het moet er net zo zacht en tastbaar uitzien als Gloop.

## Wat er ligt
- `graaf_3d.png`: 4 beelden van 64 x 64 bladpixels naast elkaar (256 x 64), 16 x 16 spelpixels per beeld, dezelfde 4 bladpixels per spelpixel als `hol_proef.png`. Doorzichtig. Elk beeld is de aarde die nog over is (86, 58, 30 en 10 procent, zoals de oude stippen), met grove brokken, een lichte breukrand, vijf kluitjes die naar de vloer vallen (bolletjes met licht van linksboven en een schaduwtje) en een stofwolkje dat groeit en vervaagt.
- `maak_graaf.py`: maakt het blad uit het echte 3D-stuk `aarde` in `godot/kunst/3d/hol_proef.png`, dus kleur en korrel zijn gelijk aan de cel ernaast. Na een nieuwe render van het hol: `python3 maak_graaf.py <hol_proef.png> <uitmap>`.
- Beelden, met Read GEZIEN: `graaf-3d-rij-3x.png` (aarde, beeld 0 tot 3, open gang), `graaf-3d-strook160-beeld1-3x.png` en `-beeld2-3x.png` (in de echte strook van main, cel links onder).

## Hoe het spel het tekent (voor Bram of Olaf)
In `hol.gd` `_brokkel()`: als `res://kunst/3d/graaf_3d.png` bestaat en `met_3d` aan staat, teken alleen
`draw_texture_rect_region(GRAAF3D, Rect2(x, y, KOL, KOL), Rect2(beeld * 64, 0, 64, 64))` met lineair filter (zoals `hol_3d.gd`), en sla de pixelsteentjes en de stofcirkels over: die zitten al in het blad. Zonder het blad blijft alles zoals nu.

## Graafrand (scheur in plaats van de gele stippels): nog niet
`graafrand_3d.png` en `maak_graafrand.py` zijn een proef: een scheur met drie zandkleurige kiezels. Frisse kijker: past beter bij de 3D-stijl, maar op ware grootte minder duidelijk dan de stippels (5 van 10). Zie `graafrand-voor-na-ware-grootte.png`. **Niet inbouwen**; de stippels blijven tot een betere versie.

## Frisse kijker
Ronde 1: 4 van 10 (kluitjes leken deuken: het licht stond omgekeerd; rafelige rand; vloer al in beeld 1). Alle drie verwerkt in ronde 2 (licht linksboven, grove brokken, gat begint hoger).

## Gezien bij de ingang (niet van mij, wel melden)
`pixelresten-bij-ingang-main-8x.png`: op main staan boven de ladder nog pixelstukjes met zwarte rand: een groen-geel figuurtje rechtsboven op het gras, een beige blok en een zwart trapje met gele pixels half achter het zweetwolkje. Waarschijnlijk pixelplantje (maaiveld, komt goed met de versiering) en iets van een pixelhoed of pixelteken achter het 3D-wolkje.
