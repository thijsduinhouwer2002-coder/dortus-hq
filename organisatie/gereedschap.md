# Gereedschap: gespecialiseerde tools als extra handen (regel van Thijs, 13 nov 14:03)

Thijs: "tools zijn echt gespecialiseerd in 1 ding, dus daar kunnen we veel meer mee. Zie ze als agents die jij aanstuurt." Claude is all-round; voor specialistisch werk (beeld, 3D, geluid, video, data) zoekt elke Claude **eerst** een gespecialiseerd hulpmiddel, probeert het, en doet het pas daarna met de hand.

## De regel
1. **Voor je iets specialistisch met de hand maakt:** zoek 10 minuten naar een tool die het beter kan (open source, gratis, een Python-pakket, een koppeling of skill). Probeer de beste één keer echt.
2. **Werkt het:** gebruik het, en zet het in de lijst hieronder met wat het kan en hoe je het start.
3. **Werkt het niet of kost het geld, een account of een sleutel van Thijs:** noteer het hieronder en zet de vraag op `organisatie/lijst-thijs.md`. Nooit zelf een account maken of betalen.
4. **Geen AI-beeld of AI-geluid in producten voor Steam** (anders een openbare AI-melding op de winkelpagina, regels Valve jan 2026). Gereedschap dat zelf maakt met code of regels mag wel: Blender, Godot, sfxr, ffmpeg, enzovoort.
5. Netwerk: in de werkomgeving werken alleen PyPI, npm en GitHub; in GitHub Actions is het hele internet open. Zware of netwerkdingen draaien in Actions.
6. Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

## In gebruik (bewezen)
| Tool | Waarvoor | Hoe | Bewijs |
|---|---|---|---|
| Blender (`pip install bpy==5.2.4`) | 3D-figuren en -werelden met code, gerenderd tot plaatjes | venv, script in `producten/steam-hol/modellen/` | `ontwerp/steam/proef-3d/` (13 nov) |
| Godot 4 | het spel Het Hol | Actions, Windows-runner | `producten/steam-hol/` |
| Connect IQ SDK + simulator | Garmin-apps bouwen en schermen | Actions | Ebb, Ebb Calm |
| Echte Blender in Actions | Click Joints testen | Actions | `platformen/blender/` |
| Pillow, ImageMagick | beelden samenstellen, verkleinen, bladen | Python | overal |

## Kandidaten (nog proberen, eerste wie het nodig heeft)
| Tool | Waarvoor | Wie |
|---|---|---|
| ffmpeg | korte films en GIF's van de echte app (forumbericht, winkelvideo, Steam-trailer) | Chris, Mila |
| sfxr / jsfxr (geluid uit regels, geen AI) | geluidjes voor Het Hol (munt, hap, val) | Olaf |
| Blender Grease Pencil of toon-shader (Freestyle) | getekende randen op 3D-figuren | Daan, Mila |
| Godot-shaders (rand, glans, wiebel) | levendigheid in het spel zonder extra plaatjes | Bram |
| Lospec-paletten | vaste kleurensets | Daan, Mila |
| Claude-skill video-making / Motion-artifact | promo-filmpje Ebb, trailer Het Hol | hoofdchat |
| Claude Design-artifact | concept nieuwe dortus.com | hoofdchat |
| Exa-zoekskill (met marktdata) | onderzoek markten en concurrenten | hoofdchat, op vraag van Vera |
| Canva-koppeling (Thijs moet koppelen) | opmaak van social- en forumplaatjes | alleen als nodig |
