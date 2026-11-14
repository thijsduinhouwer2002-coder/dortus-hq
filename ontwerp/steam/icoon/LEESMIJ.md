# App-icoon Het Hol (Daan, 14 nov 2026)

Waarom: in het echte bureaublad van Olaf (run 43632041232) staat in de taakbalk het blauwe Godot-robotje. `export_presets.cfg` heeft `application/icon=""` en `project.godot` geen `config/icon`. Elke koper ziet dat icoon bij elke start, en het staat op winkelscherm 2.

- Gloop versie 1 met alleen de kroon, op een pruimtegel met ronde hoeken. Render: `GLOOP_ICOON=1 <venv>/bin/python producten/steam-hol/modellen/gloop.py <uit.png> 1 2 1024 1024 48` (zonder die variabele verandert er niets aan Gloop in het spel).
- `maak_icoon.py` maakt alles hieronder uit `gloop-kroon-1024-render.png`.
- `hol.ico`: 16, 24, 32, 48, 64, 128, 256. Voor 16 en 24 een eigen kleine tegel (Gloop groter, groen voller), moet van de frisse kijker.
- `icoon-tegel-256.png` en `-512.png`: voor `config/icon` in Godot en elders.
- `steam-community-184.jpg`: community-icoon voor Steamworks (184 x 184).
- `proef-taakbalk.png`: ware grootte op lichte en donkere taakbalk, met en zonder tegel. Gekozen: met tegel (zonder vloeit het mintgroen weg op een lichte taakbalk).
- `taakbalk-voor-boven-na-onder-3x.png`: het echte bureaublad, boven nu (Godot), onder met dit icoon.

Frisse kijker (agent, kreeg alleen de plaatjes), letterlijk: "Een mintgroen slijmwezentje met één groot oog en een gouden kroontje" ... "Vanaf 24 px herken ik een groen wezen met een kroon. Op 16 px is het alleen een groen klompje met een geel puntje erop." ... "Met tegel. De donkerpaarse tegel geeft een vaste vorm en een sterk contrast met de lichte taakbalk" ... "Een 7." Moet: "Maak voor 16 en 24 px een vereenvoudigde variant: het wezen groter in de tegel" (gedaan). Kan: groen iets voller (gedaan op de kleine maten).
