# Fakkel in 3D (Daan, 13 nov 2026)

Aanleiding: het blad `deco` (Bram, 23:30) maakte van de pixelfakkel een 3D-fakkel, maar de vlam las als een wit ei op een stokje. Oorzaak: emissie 9 en 14 met view transform Standard knipt naar wit.

Nieuw ontwerp (in `fakkel.py` als proef, in `hol.py` op tak `ontwerp/steam-fakkel`):
- vlam als druppel met een punt die iets opzij buigt, in drie lagen: rood-oranje rand (ff5a1f, emissie 1,6), oranje (ff9b2a, 2,4), geel hart (ffe27a, 3,2), geen schaduw;
- donkere omwikkelde kop (3a2418), steel van kamerhout (6e4632), ijzeren beugel met ring aan de muur;
- zelfde hoogte als de oude fakkel, zodat het vak in `sprites.json` (6 bij 12 spelpixels) blijft passen;
- ladderpalen ook in kamerhout, minder oranje.

Beelden (GEZIEN met Read):
- `vergelijk-huidig-gekozen-zonderbeugel.png`: links groot (oud, gekozen, zonder beugel), midden op ware grootte 4x, rechts de pixelfakkel uit de strook.
- `deco-links-oud-rechts-nieuw-4x.png`: het echte blad `deco` uit de pijplijn, oud en nieuw.
- `hol-boven-oud-onder-nieuw.png`: het hele hol op 1440x240, boven oud, onder nieuw.

Draaien: `venv/bin/python fakkel.py /abs/pad/uit.png 900 600 48` (venv met `bpy==5.2.4`, Python 3.13).
