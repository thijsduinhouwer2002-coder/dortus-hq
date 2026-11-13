# 3D-pijplijn Het Hol (Bram, 13 nov 2026)

Van een `.py`-model in `producten/steam-hol/modellen/` naar een blad dat Godot toont. Besluit Thijs 13 nov 13:35, zie `ontwerp/steam/3d-stijl.md`.

## Zo werkt het
1. Zet je model in `sprites.json`: welk script, welke argumenten (`{uit} {w} {h} {samples}` worden ingevuld), de cel in spelpixels, `px` (bladpixels per spelpixel, 4 = scherp tot strook 160 px) en de beelden (`frames`: naam en `[breed, hoog]`, geschaald rond de vloer; `[1.3, 0.42]` is plat).
   Een beeld mag ook `{"schaal": [1, 1], "stand": "hap"}` zijn: dan draait het model apart met `{stand}` ingevuld in de argumenten (standaard `rust`). Zo kan Daan standen (knipperen, kauwen, hap) als argument van zijn model maken.
2. Je model roept zoals altijd `gedeeld.render(...)` aan. Met `HOL_FRAMES` maakt die dan meerdere beelden; zonder verandert er niets.
3. `render.py` snijdt strak bij (de vage uitloop van de schaduw telt niet mee), schaalt zodat het eerste beeld precies in de cel past (alle beelden dezelfde schaal), verkleint met Lanczos op voorvermenigvuldigde alfa (geen donkere randjes) en schrijft `godot/kunst/3d/<naam>.png`, `.png.import` (mipmaps) en `sprites.json` (maten, anker, kruin per beeld).
4. In Actions (`.github/workflows/steam-hol-modellen.yml`): bij elke push in `modellen/` of `pijplijn/` op main of `claude/steam-*`. Is het blad veranderd, dan commit hij het terug op dezelfde tak en start hij de Windows-run (`steam-hol.yml`), met schermbeelden op 96, 120 en 160 px op tak `schermen`.

Lokaal: `python3 -m venv ~/bpyenv && ~/bpyenv/bin/pip install bpy==5.2.4 pillow`, dan `BPY_PYTHON=~/bpyenv/bin/python python3 render.py gloop` (±2 min voor 2 beelden op 640 px, 48 samples). `HOL_HERGEBRUIK=1` snijdt en schaalt opnieuw zonder te renderen, `HOL_SNEL=1` rendert met een kwart van de samples.

## In het spel
Godot tekent het blad met filter lineair via een `CanvasTexture` (alleen dat lijf; de rest blijft nearest). Gloop: `systemen/slijm.gd`, functies `beeld_3d()` en `_teken_3d()`; `met_3d = false` geeft de oude pixel-Gloop terug. Voorlopig 3D voor rust, slapen, plat en opstaan; hap en spugen blijven pixels tot Daan die beelden in 3D heeft (dan erbij in `frames`).

## Zuinig
Het blad van Gloop is 198 x 64 pixels (±13 kB als PNG, in het geheugen ±67 kB met mipmaps). Gloop tekent alleen opnieuw als er iets gebeurt, net als eerst. Meting van CPU met het nieuwe blad: zie `platformen/steam/taken.md`.
