# Loopbeelden helden (Mila, 25 nov 2026, issue 32)

- `<soort>-loop-ware-maat.gif`: strook 120 px (3 schermpixels per spelpixel), 3 s. `-2x.gif`: dubbel.
- Gemaakt met `pijplijn/loop_gif.py` uit de bladen in `godot/kunst/3d/`: stap1 tot stap6 achter elkaar, de held schuift per beeld `stap_px` spelpixels, op `loop_fps` beelden per seconde. De streepjes op de vloer liggen 4 spelpixels uit elkaar: de voet op de vloer moet er stil tegen staan.
- `bladen-2x.png`: de 12 beelden per blad: rust, stap1 tot stap6, schrik, vallen, kijk, draai, sprong.

Per soort (GEZIEN in `godot/kunst/3d/sprites.json`):

| soort | stap_px | loop_fps | snelheid (spelpx/s) | loop |
|---|---|---|---|---|
| ridder | 0,327 | 8 | 2,6 | korte zware stappen met een stamp (zakt door op elke voet), wiegt heen en weer, schild hoger zodat je de benen ziet |
| dief | 0,618 | 12 | 7,4 | laag en voorovergebogen, lange snelle stappen |
| bard | 0,403 | 10 | 4,0 | rechtop, hupje in elke doorzwaai |
| heks (magiër) | 0,327 | 8 | 2,6 | lange mantel tot net boven de laarsjes, die eronder uit stappen; zoom zwaait mee, vrije hand zwaait |

Let op voor het spel: de helden lopen nu 1 spelpixel per stap op 8 beelden per seconde (8 spelpx/s). Bij die snelheid glijden korte beentjes altijd. Kies per soort: langzamer lopen (snelheid hierboven), of loop_fps omhoog tot snelheid / stap_px.
Alle helden kijken nu naar rechts in beeld, de kant waarheen ze lopen. Tot 25 nov keken ze naar links terwijl ze naar rechts liepen (een maanloop).

Run 2 (25 nov): ridder en heks verbeterd op de twee zwakke plekken uit keuring #35 (heks benen weg onder de jurk, ridder stijf). De GIFs van ridder en heks komen uit een snelle render (kwart samples); de workflow rendert de bladen daarna op volle kwaliteit.
