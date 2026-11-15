# Demofilm Click Joints Pro (Bram, 15 nov 2026)

Opdracht hoofdchat 15 nov 17:55 (`berichten/bram.md`). Versie 1, gemaakt in de echte Blender 5.3.0 (Linux, Xvfb, software-OpenGL) met de betaalde zip 1.0.1.

- `click-joints-pro-demo.mp4`: 20,6 s, 1920 x 1080, 30 fps, H.264 (`-preset veryfast`, crf 18), geen geluid.
- `click-joints-pro-demo.gif`: de buig en het rood, ±7,4 s, 960 breed, 15 fps (voor fora).
- `film-v1-10-beelden.jpg`: tien beelden uit de film naast elkaar, om met Read te keuren.

Wat er in zit: (1) het hele been als één stuk, langzaam draaiend, dan Place hinge met 115° (knop in de zijbalk); (2) de Bend-schuif in de zijbalk van 0 naar 114,9° met de gradenboog van de add-on; (3) camera naar boven, B half doorzichtig (zoals winkelplaatje 14), 3° voorbij de stop: rode lijn en "+3° past limit" van de add-on, rode vlakken op A en B; (4) de kogel van Place joint met de groene pasband; (5) eindbeeld "Click Joints Pro", "Print-ready joints for Blender", "on Superhive", zonder prijs.

Alles in beeld komt van de add-on; het script beweegt alleen de camera en de schuif, en zet de zijbalk op schaal 1,35 zodat hij leesbaar is. Onderschriften en eindbeeld in Inter, #23262D en mint #3BE6B0 zoals de poster.

Maken: `producten/blender-gewrichten/e2e/film_pro.py` (opname, ±3 min) en `e2e/maak_film.sh` (onderschriften, eindbeeld, GIF). Workflow `click-joints-pro-film.yml` doet hetzelfde op GitHub.

Eerlijk, zwakke punten v1: bij het rood is het rode vlak klein (6 vlakken); wat het meest opvalt is de rode lijn met "+3° past limit". Bij de kogel staat het hoofd van de pop groot en grijs links in beeld.
