# Broncode: godot-demo-projects (de voorbeelden van de makers van Godot)

Uitgeplozen door de Afkijker op 25 nov 2026, voor issue #20 (bijsturing hoofdchat 25 nov 10:55, project 1 van 4). Code gelezen met `git clone --depth 1 --sparse` van https://github.com/godotengine/godot-demo-projects (laatste commit 281a99f, 25 nov 2026), alleen de mappen `2d/`, `audio/` en `gui/`, alleen gelezen, niets uitgevoerd. Godot-documentatie met curl.

## Waarom dit project
- Hats is gebouwd in Godot 4.3 (`producten/steam-hol/godot/project.godot` r. 8). Dit zijn de voorbeelden van de makers zelf: zo bedoelen zij beweging, animatie en geluid.
- Aantal sterren en de issues van dit project kon ik niet lezen: GitHub-pagina's en de GitHub-API buiten onze drie repo's zijn in deze geplande taak geblokkeerd (403). Het is het officiële voorbeeldenpakket van Godot (GEZIEN, eigenaar `godotengine`).
- **Licentie: MIT** (GEZIEN, `LICENSE.md` r. 1 tot 21, "Copyright (c) 2014-present Godot Engine contributors"). Code overnemen mag, met naamsvermelding in `CREDITS`. Hieronder gaat het vooral om werkwijzen; die zitten ook gewoon in Godot zelf.

## Wat ze slim doen (bestand en regels)
1. **Bewegen met een curve, niet recht.** De tween-demo laat elke beweging een eigen soort curve kiezen (`2d/tween/main.gd` r. 39 tot 41: `set_ease`, `set_trans`). Groter worden doen ze met een doorschieter: `TRANS_ELASTIC` en `EASE_OUT`, het ding schiet iets voorbij zijn maat en veert terug (r. 125). Een sprong is twee helften: omhoog met `EASE_OUT` (snel weg, traag bovenin), omlaag met `EASE_IN` (traag bovenin, snel neer), beide `TRANS_SINE` (r. 74 tot 76).
2. **Alles in één ketting.** Eén tween doet stap na stap (bewegen, kleuren, knipperen, wachten, aftellen), met `parallel()` voor wat tegelijk moet (r. 53 tot 60) en `tween_interval` voor een rustpunt (r. 92, r. 113). Eén regel per stap, makkelijk bij te stellen.
3. **Snelheid van alles op één knop.** `set_speed_scale` zet het tempo van de hele ketting in één keer (r. 25, r. 195 tot 199). Handig om een moment trager of sneller te proeven zonder getallen overal te veranderen.
4. **Hetzelfde geluid, andere toon.** In de platformer klinkt de gewone sprong op toon 1,0 en de dubbele sprong met hetzelfde bestand op toon 1,5 (`2d/platformer/player/player.gd` r. 80 en r. 84). Eén wav, twee gevoelens: de tweede sprong klinkt "hoger", dus beter.
5. **Loslaten telt.** Laat je de springknop vroeg los, dan wordt de sprong korter (`velocity.y *= 0.6`, r. 32 tot 34). Kleine reactie op wat de speler doet, groot gevoel van controle.
6. **Het beeld volgt de beweging.** Welk loopje speelt, hangt af van de echte snelheid: stil, rennen, springen, vallen (`player.gd` r. 61 tot 75, `get_new_animation`). Geen klok die los van de beweging loopt.
7. **Geluid op het ritme.** `audio/bpm_sync/bpm_sync.gd` r. 26 tot 35 rekent de echte tel van de muziek uit, met de vertraging van de geluidskaart erbij (`get_output_latency`). Zo kan iets precies op de maat gebeuren.
8. **Effecten op een geluidsbus.** `audio/audio_effects/default_bus_layout.tres` laat alle effecten van Godot zien (galm `AudioEffectReverb` r. 33, toon `PitchShift` r. 29, enzovoort), aan of uit per bus.

In Godot zelf (geen demo-code, GEZIEN in de documentatie met curl):
- `Tween.interpolate_value(begin, verschil, tijd, duur, soort, ease)` is een losse rekenfunctie: dezelfde curves als hierboven, ook voor wie alles zelf tekent in `_draw` (https://docs.godotengine.org/en/stable/classes/class_tween.html).
- `AudioStreamRandomizer` met `random_pitch`: "Pitch will be randomly chosen within a range of 1.0 / random_pitch and random_pitch" (https://docs.godotengine.org/en/stable/classes/class_audiostreamrandomizer.html). Eén regel instelling, geen eigen code.

## Wat gebruikers vragen of klagen
Niet gelezen: de GitHub-issues van dit project zijn in deze taak geblokkeerd. Geen GOK opgeschreven.

## Zo doen zij het, zo doen wij het (Hats, `producten/steam-hol/godot/`)
GEZIEN in onze code op 25 nov 2026: Hats gebruikt nergens een Tween, `ease()` of `interpolate_value` (grep op `Tween`, `ease(`, `smoothstep(`: 0 treffers). Alle beweging is met de hand gerekend. Dat werkt, en op sommige plekken al met een goede curve (het getal stijgt met een ease-out, `kern/klap.gd` r. 99; de held zakt versnellend de put in, `systemen/held_beeld.gd` r. 368; de sprong is een sinusboog, `systemen/held_loop.gd` r. 186). Maar:

| Moment | Zij | Wij nu | Wat beter kan |
|---|---|---|---|
| Het getal "+9" na een vangst | groter worden met doorschieter (`TRANS_ELASTIC`/`BACK`, `EASE_OUT`) | van 1,5 keer recht naar 1,0 in 0,12 s (`kern/klap.gd` r. 72 tot 77, `maat`) | klein beginnen, voorbij de maat schieten en terugveren (BACK, ±0,25 s): het getal "landt" |
| Plof, hap en munt | één wav, toon per gebeurtenis anders (1,0 en 1,5) | elke plof en munt klinkt precies gelijk (`kern/geluid.gd` r. 43 tot 57: geen `pitch_scale`) | toon elke keer iets anders (±6%), en bij een reeks ("x2", "x3") de munt een stapje hoger per vangst: het oor hoort de reeks groeien |
| Sprong van de held over een val | omhoog EASE_OUT, omlaag EASE_IN (zwaarte) | gelijke sinusboog (`held_loop.gd` r. 186) | prima zo; hooguit iets langer bovenin hangen |
| Tempo van een moment proeven | één `speed_scale` | getallen verspreid over `klap.gd`, `held_beeld.gd`, `hol.gd` | later: één tempo-getal per moment, handig voor Iris en Sanne |
| Galm in het hol | galm-effect op een bus | geen bus-effecten (geen bus-indeling in het project) | een lichte galm op de geluidsbus past bij "kelder"; eerst proeven, het moet zacht blijven (Hats staat naast werk aan) |

## Wat Dortus ervan leert
1. **Beste idee (issue #73 bij Sanne): de klap klinkt en springt levendiger.** (a) Elke plof, hap en munt een iets andere toon (±6%, `pitch_scale` in `kern/geluid.gd` r. 56, of `AudioStreamRandomizer`), (b) bij een reeks gaat de munt een halve toon omhoog per vangst, (c) het getal "+9" springt met een doorschieter (`Tween.interpolate_value` met `TRANS_BACK`, `EASE_OUT` in `kern/klap.gd` `maat`). Klein werk, dicht punt 3 van Iris ("een klap zonder tok voelt half") verder en past in het weekdoel (leuk een 8). Geen nieuwe tekst, geen tijdsdruk, geen schermschudden.
2. Hetzelfde geldt voor Click Joints en Click Cuts niet (Blender-add-ons zonder beweging); voor Ebb (Garmin) is de les "beweging met een curve" bruikbaar voor de ademcirkel, als die ooit recht op en neer gaat.
3. Licentie: MIT, dus een paar regels code overnemen mag met naamsvermelding in `CREDITS`; met `interpolate_value` en `AudioStreamRandomizer` uit Godot zelf is overnemen niet eens nodig.

Niets overgenomen. Niets uitgevoerd.
