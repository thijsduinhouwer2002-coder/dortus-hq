# Loopbeelden helden (Mila, 25 nov 2026, issue 32)

- `<soort>-loop-ware-maat.gif`: strook 120 px (3 schermpixels per spelpixel), 3 s. `-2x.gif`: dubbel.
- Gemaakt met `pijplijn/loop_gif.py` uit de bladen in `godot/kunst/3d/`: stap1 tot stap6 achter elkaar, de held schuift per beeld `stap_px` spelpixels, op `loop_fps` beelden per seconde. De streepjes op de vloer liggen 4 spelpixels uit elkaar: de voet op de vloer moet er stil tegen staan.
- `bladen-2x.png`: de 12 beelden per blad: rust, stap1 tot stap6, schrik, vallen, kijk, draai, sprong.

Per soort (GEZIEN in `godot/kunst/3d/sprites.json`):

| soort | stap_px | loop_fps | snelheid (spelpx/s) | loop |
|---|---|---|---|---|
| ridder | 0,322 | 8 | 2,6 | korte zware stappen, armen stil, wiegt heen en weer |
| dief | 0,618 | 12 | 7,4 | laag en voorovergebogen, lange snelle stappen |
| bard | 0,403 | 10 | 4,0 | rechtop, hupje in elke doorzwaai |
| heks (magiër) | 0,327 | 8 | 2,6 | glijdt in haar lange jurk, vrije hand zwaait |

Let op voor het spel: de helden lopen nu 1 spelpixel per stap op 8 beelden per seconde (8 spelpx/s). Bij die snelheid glijden korte beentjes altijd. Kies per soort: langzamer lopen (snelheid hierboven), of loop_fps omhoog tot snelheid / stap_px.
Alle helden kijken nu naar rechts in beeld, de kant waarheen ze lopen. Tot 25 nov keken ze naar links terwijl ze naar rechts liepen (een maanloop).
