# Gereedschap: gespecialiseerde tools als extra handen (regel van Thijs, 13 nov 14:03)

Thijs: "tools zijn echt gespecialiseerd in 1 ding, dus daar kunnen we veel meer mee. Zie ze als agents die jij aanstuurt." Claude is all-round; voor specialistisch werk (beeld, 3D, geluid, video, data) zoekt elke Claude **eerst** een gespecialiseerd hulpmiddel, probeert het, en doet het pas daarna met de hand.

## De regel
1. **Voor je iets specialistisch met de hand maakt:** zoek 10 minuten naar een tool die het beter kan (open source, gratis, een Python-pakket, een koppeling of skill). Probeer de beste één keer echt.
2. **Werkt het:** gebruik het, en zet het in de lijst hieronder met wat het kan en hoe je het start.
3. **Werkt het niet of kost het geld, een account of een sleutel van Thijs:** noteer het hieronder en zet de vraag op `organisatie/lijst-thijs.md`. Nooit zelf een account maken of betalen.
4. **Geen AI-beeld of AI-geluid in producten voor Steam** (anders een openbare AI-melding op de winkelpagina, regels Valve jan 2026). Gereedschap dat zelf maakt met code of regels mag wel: Blender, Godot, sfxr, ffmpeg, enzovoort.
5. Netwerk: in de werkomgeving werken alleen PyPI, npm en GitHub; in GitHub Actions is het hele internet open. Zware of netwerkdingen draaien in Actions.
6. Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

## Kaart: welk programma is waar gekoppeld (15 nov 2026, hoofdchat)
Twee plekken. **In de cloud** (GitHub Actions en de werkomgeving van de agents): draait altijd, ook als de pc van Thijs uit staat. **Op de pc van Thijs** (lokale koppeling via de Claude-app): werkt alleen als zijn pc aan staat en het programma open is.

| Programma | In de cloud | Gebruikt voor | Bewijs |
|---|---|---|---|
| Blender (echt, 4.2 tot 5.3, met scherm via xvfb) | ja | Click Joints testen, winkelplaatjes, demofilm Pro | workflows `blender-gewrichten-e2e`, `click-joints-pro-film` (v2 groen 15 nov) |
| Blender als Python-pakket (bpy) | ja | 3D-figuren en sprites Hats of the Fallen | `ontwerp/steam/proef-3d/` |
| Obsidian (echt, via ObsidianLauncher) | ja | Rollwright testen met schermafbeeldingen | workflow `rollwright-e2e` |
| Godot 4.3 (Windows-runner) | ja | het spel bouwen, schermen en winkelbeelden | workflows `steam-hol*` |
| Connect IQ SDK en simulator | ja | Ebb en Ebb Calm | workflow `garmin-proef` |
| IntelliJ/CLion | ja | Bison & Flex testen en film | workflows `jetbrains-bison-flex-*` |
| ffmpeg | ja | films en GIF's | `click-joints-pro-film` |
| sfxr-geluiden | ja | geluiden in het spel | `producten/steam-hol/godot/geluid/` |
| Blender MCP / Obsidian MCP op de pc van Thijs | nee | live meekijken terwijl Claude in jouw Blender werkt | niet ingesteld; vraagt ±10 min van Thijs |

In de klikbare connector-lijst van Claude staan geen koppelingen voor Blender, Obsidian of Godot (gezocht 15 nov). Wat wel bestaat en later kan helpen: vidIQ (YouTube-onderzoek), Metricool (berichten plannen), TinyFish (websites zoals Reddit lezen). Allemaal met een account van Thijs, nu niet nodig.

## In gebruik (bewezen)
| Tool | Waarvoor | Hoe | Bewijs |
|---|---|---|---|
| Blender (`pip install bpy==5.2.4`) | 3D-figuren en -werelden met code, gerenderd tot plaatjes | venv, script in `producten/steam-hol/modellen/` | `ontwerp/steam/proef-3d/` (13 nov) |
| Godot 4 | het spel Hats of the Fallen | Actions, Windows-runner | `producten/steam-hol/` |
| Connect IQ SDK + simulator | Garmin-apps bouwen en schermen | Actions | Ebb, Ebb Calm |
| Echte Blender in Actions | Click Joints testen | Actions | `platformen/blender/` |
| Pillow, ImageMagick | beelden samenstellen, verkleinen, bladen | Python | overal |

## Kandidaten (nog proberen, eerste wie het nodig heeft)
| Tool | Waarvoor | Wie |
|---|---|---|
| ffmpeg | korte films en GIF's van de echte app (forumbericht, winkelvideo, Steam-trailer) | Chris, Mila |
| sfxr / jsfxr (geluid uit regels, geen AI) | geluidjes voor Hats of the Fallen (munt, hap, val) | Olaf |
| Blender Grease Pencil of toon-shader (Freestyle) | getekende randen op 3D-figuren | Daan, Mila |
| Godot-shaders (rand, glans, wiebel) | levendigheid in het spel zonder extra plaatjes | Bram |
| Lospec-paletten | vaste kleurensets | Daan, Mila |
| Claude-skill video-making / Motion-artifact | promo-filmpje Ebb, trailer Hats of the Fallen | hoofdchat |
| Claude Design-artifact | concept nieuwe dortus.com | hoofdchat |
| Exa-zoekskill (met marktdata) | onderzoek markten en concurrenten | hoofdchat, op vraag van Vera |
| Canva-koppeling (Thijs moet koppelen) | opmaak van social- en forumplaatjes | alleen als nodig |
- **Geluid met code (Chris, 17 nov 2026):** numpy (sinustonen, ruis via FFT) plus ffmpeg (`-c:v copy` houdt het beeld gelijk, `volume` voor één vaste versterking, `loudnorm` alleen om te meten). Werkt goed voor korte filmpjes zonder rechten van anderen. Voorbeeld: `commercie/filmpjes/geluid/geluid.py`. Les: `loudnorm` met een doel van -16 LUFS schakelt bij een hoge piek stil over op compressie en plet een klik; meet liever en geef één vaste versterking.
