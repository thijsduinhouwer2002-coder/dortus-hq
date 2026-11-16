# Hoedenwand (Mila, 16 nov 2026)
Elke held die Gloop opat, laat een hoed achter die scheef half in de aardwand boven de gang blijft steken. Dichtheid en eigen gezicht in één: de wand is het logboek van wie Gloop at. Uitleg en doelbeeld: `ontwerp/steam/winkelpagina/vol/LEESMIJ.md`.
- `hoedenwand.py`: holte (donker), de hoed uit `producten/steam-hol/modellen/hoeden.py` (schaal 1,25, zijwaarts gekanteld), een platte aardrand met kluitjes en steentjes ervoor. Doorzichtige achtergrond. Camera en licht uit `gedeeld.py`.
- `renders/wand-<nr>.png`: alle 10 hoeden (kanteling -22, 18, -15, 25, -18, 20, -25, 15, -12, 22 graden), 400x300, 32 samples, ±6 s per stuk op de CPU (bpy 5.2.4).
- GEZIEN met Read: alle tien als blad op aardkleur, en op 50 px in de strook (doelbeeld): elke hoed blijft herkenbaar, de holte maakt dat hij IN de wand zit.
- Zwak: de onderrand van de aardschijf is iets donkerder dan de wand van het spel; als het in de pijplijn zit, de aardkleur gelijk trekken met `aardemat("pruim")` uit `hol.py`.
- `wortels.py` en `renders/wortels-1..3.png`: wortels onder het gras geprobeerd. GEZIEN in het doelbeeld: te dun en vaag op 600, en ze liepen over de kamers. Niet gebruikt; als iemand het opnieuw probeert: dikker (2x), lichter en alleen tussen kamers.
