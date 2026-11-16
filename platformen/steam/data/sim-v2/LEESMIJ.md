# Voortgang versie 2 nagerekend (Sanne, 16 nov 2026)

Brams sim met lagen (`producten/steam-hol/sim/`), met twee kleine aanpassingen van mij, alleen in een kopie (Brams bestanden zijn niet veranderd):
- `sim-aanpassing.diff`: upgrade stap 4 tot 6 krijgt een eigen prijsfactor per laag (`laag_factor_hoog`).
- `voortgang_lagen_sanne.py`: Brams script, met mijn 15 niveaus met een prijs (`DINGEN`) en 20 kamertjes aankleding (`DECOR`, prijs 1,25 x goud per uur van die laag), en uitvoer naar `voortgang-lagen-sanne.json`.

Opnieuw draaien: kopieer `sim.py` uit Brams map, pas `sim-aanpassing.diff` toe, zet het script ernaast, en:
```
OUD_GOUD=0.5 HOOG=1,1.2,1.5,1.8 DINGEN="{6:1,7:1,14:1,16:1,17:1,22:2,23:2,24:2,29:2,32:3,33:3,38:3,42:4,43:4,45:4}" DECOR="{21:2,25:2,26:2,27:2,28:2,30:3,31:3,34:3,35:3,36:3,37:3,39:3,40:4,41:4,44:4,46:4,47:4,48:4,49:4,50:4}" python3 voortgang_lagen_sanne.py 500,750,1000 45,126,353,600,1000,1600 1,1.2,2.2,3.2
```
Uitkomst: `voortgang-v2-uitkomst.txt` (8 zaden, GEZIEN). De kamertjes hangen in deze sim aan een hol-niveau (zo kan de sim ze kopen); in het spel komen ze per laag vrij. Weg zijn op halve snelheid zit niet in deze sim (die rekent alleen open tijd).
