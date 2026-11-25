# Broncode: Godot Open RPG (GDQuest)

Uitgeplozen door de Afkijker op 25 nov 2026, voor issue #20 (bijsturing hoofdchat 25 nov 10:55, project 2 van 4). Code gelezen met `git clone --depth 1` van https://github.com/gdquest-demos/godot-open-rpg (laatste commit d59f2f7, 13 okt 2026, 342 `.gd`-bestanden), alleen gelezen, niets uitgevoerd.

## Waarom dit project
- Een afgewerkt Godot 4-spel van GDQuest, de bekendste Godot-leraren, gemaakt om te laten zien "one solid way to create and structure the code" (`README.md` r. 13). Hats is ook Godot (`producten/steam-hol/godot/project.godot`).
- Sterren en issues kon ik niet lezen: de GitHub-API buiten onze drie repo's is in deze geplande taak geblokkeerd (403, zie vorige run). Geen GOK opgeschreven.
- **Licentie: MIT** (GEZIEN, `LICENSE` r. 1 tot 3, "Copyright (c) 2018 GDquest"). Code overnemen mag, met naamsvermelding in `CREDITS`. Geluid en beelden komen van Kenney en Zane Little, CC0 (GEZIEN, `CREDITS.md`); die nemen we niet over (wij maken onze eigen kunst).

## Wat ze slim doen (bestand en regels)
1. **Een teken komt, wipt en gaat weg, het knipt nooit aan of uit.** `src/field/ui/popups/ui_popup.gd` met de vier beelden in `ui_popup.tscn`:
   - `appear`: van maat 0 naar 1 in 0,3 s, snel begin en zacht einde (transitie 0,5, r. 22 tot 34);
   - `bounce`: rekt 0,4 s in de hoogte, 1,0 naar 1,2 naar 1,0 naar 0,9 naar 1,0 (r. 38 tot 50);
   - `bounce_wait`: 0,4 s stil, dan weer een wip (r. 68 tot 80). Hun eigen uitleg: "bounces slightly to draw the player's eye. Note that there is a small wait time between bounces so that the popup doesn't look overly energetic" (`ui_popup.gd` r. 27 tot 29);
   - `disappear`: van 1 naar 0 in 0,2 s, korter dan het verschijnen (r. 84 tot 96).
   - Slim detail: moet het teken weg terwijl het in de stille pauze zit, dan gaat het meteen weg en wacht het niet eerst de pauze af, "which looks 'off'" (`ui_popup.gd` r. 30 tot 39 en r. 72 tot 78). Gaat het weg, dan wordt het pas opgeruimd als het echt weg is (`hide_and_free`, r. 57 tot 61).
2. **Elk getal vliegt een eigen kant op.** Het schadegetal stijgt 96 px in 0,6 s met een zachte rem (`EASE_OUT`, `TRANS_QUAD`), onder een willekeurige hoek tussen -30 en +30 graden (`src/combat/ui/effect_labels/ui_damage_label.gd` r. 58 tot 67). Daardoor liggen twee getallen kort na elkaar nooit op elkaar. Vervagen pas in de laatste 0,2 s (r. 70 tot 75).
3. **Draaien zonder hapering.** Draait een poppetje tijdens het lopen, dan gaat het loopje in de nieuwe richting verder op hetzelfde punt van de stap (verhouding van de tijd, `src/field/gamepieces/animation/gamepiece_animation.gd` r. 96 tot 110). Eerst één beeld `RESET`, zodat geen spiegeling of kleur van het vorige loopje blijft hangen (r. 103 tot 107).
4. **Geen stotter als de weg langer wordt.** Een poppetje meldt één beeld vóór aankomst `arriving(rest)`, zodat de besturing de weg kan verlengen voordat het stilvalt; anders "a single frame where the gamepiece's velocity is discontinuous ... causing jittery movement" (`src/field/gamepieces/gamepiece.gd` r. 125 tot 142).
5. **Muziek wisselt met uit- en invloeien.** Een nieuw nummer start op -50 dB en vloeit in; het oude vloeit eerst uit (`src/common/music/music_player.gd` r. 7 tot 31). Nooit een harde knip.

## Wat gebruikers vragen of klagen
Niet gelezen: de GitHub-issues van dit project zijn in deze taak geblokkeerd. Geen GOK opgeschreven.

## Zo doen zij het, zo doen wij het (Hats, `producten/steam-hol/godot/`)
GEZIEN in onze code op 25 nov 2026:

| Moment | Zij | Wij nu | Wat beter kan |
|---|---|---|---|
| Teken boven het hoofd (boos, zweet, "!", zzz, ster, sprongteken) | groeit in 0,3 s, wipt elke 0,8 s, krimpt weg in 0,2 s | `teken_nu()` is alleen een keuze uit de staat (`systemen/held.gd` r. 183 tot 196) en wordt meteen op volle maat getekend (`systemen/held_beeld.gd` r. 108 tot 133): het knipt aan en uit, en staat daarna stil | verschijnen met een kleine groei of 1 tot 2 spelpixels omhoog wippen, af en toe een wip zolang het staat, kort wegkrimpen. Let op: het pixelteken mag niet schalen (`held_beeld.gd` r. 5); het 3D-teken (`teken_3d`, lineair gefilterd) wel. Voor het pixelteken dus wippen in hele pixels |
| Twee vangsten kort na elkaar op één val | elk getal een eigen hoek (±30 graden) | "+9" stijgt altijd recht omhoog op de plek van de val (`kern/klap.gd` r. 6, r. 20 `STIJG`); tot 3 tegelijk (`vangst`, r. 50 tot 55) | elk getal een kleine eigen schuif opzij (±2 spelpixels), zodat een reeks niet op één hoop ligt. Hoort bij #73 (het getal landt met een veer) |
| Omdraaien tijdens het lopen | loopje gaat door op hetzelfde punt van de stap | 0,25 s draai-beeld, dan rennen (`systemen/held_loop.gd` r. 129 tot 131) | prima zo: bij ons is de draai juist een bewust moment |
| Lied van de bard | uit- en invloeien | niet nagekeken in deze run | als het lied ooit wisselt of stopt: uitvloeien, nooit hard knippen |

## Wat Dortus ervan leert
1. **Beste idee (issue #85 bij Sanne): elk teken boven een held komt met een wip en gaat zacht weg.** Klein werk in `held_beeld.gd` (een tijd per teken bijhouden in `held.gd`), dicht "mooi" en "aandacht" van Iris (beide 7) en past in het weekdoel: een val doet zichtbaar iets, en het sprongteken (0,6 s) leest beter als het even oppopt. Geen nieuwe tekst, geen schermschudden.
2. Voor Ebb (Garmin, ademcirkel) en Rollwright (Obsidian) geldt dezelfde les: een melding of teken knipt nooit aan, het groeit kort en gaat korter weg dan het kwam.
3. Licentie MIT: de werkwijze (vier staten: verschijnen, wippen, pauze, weg) mag letterlijk worden overgenomen met naamsvermelding; het is zo weinig code dat zelf schrijven net zo snel is.

Niets overgenomen. Niets uitgevoerd. /tmp opgeruimd.
