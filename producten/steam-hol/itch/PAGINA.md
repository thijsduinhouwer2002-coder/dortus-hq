# itch.io-proefpagina Hats of the Fallen: plakkaart (Sanne, 27 nov 2026, issue #314)

**Niet openbaar zetten.** Plaatsen doet alleen de hoofdchat, en pas na het ja van Thijs op het spel (#314 punt 3, `organisatie/plan-tot-half-december.md`). De pagina vraagt een itch.io-account van Thijs; aanmaken en inloggen doet Thijs zelf. Alle spelerstekst hieronder is **CONCEPT** tot Thijs hem in eigen woorden schrijft of goedkeurt.

Lat: Rusty's Retirement en Spirit City: Lofi Sessions (`organisatie/lat/hats.md`). Wat hun pagina doet en wij overnemen: in zin 1 soort en plek ("sits at the bottom of your screen while you do other things"), dan pas de haak; korte kopjes die een daad zijn; schermen die het spel op een bureaublad tonen (GEZIEN in de lat, 25 nov). Wat wij beter doen dan zij (gaten uit de lat): je kunt weghalen en geld terugkrijgen, het spel pakt nooit de focus, en na minuut 25 komt er nog steeds iets nieuws (robijnen, reuzen).

## Vakken op itch.io, van boven naar onder (Create new project)

| Vak | Invullen |
|---|---|
| Title | Hats of the Fallen |
| Project URL | hats-of-the-fallen |
| Short description or tagline | Your taskbar has a basement now. An idle trap game that sits on top of your taskbar while you work. |
| Classification | Games |
| Kind of project | Downloadable |
| Release status | Prototype |
| Pricing | No payments (gratis) |
| Uploads | de speeltest-zip van de nieuwste groene run van `steam-hol-exe.yml` op main (HetHol.exe en LEES-MIJ-EERST.txt), vinkje "Windows"; of met de workflow `itch-uitbrengen.yml` (vraagt de sleutel van Thijs) |
| Description | tekst hieronder |
| Genre | Simulation |
| Tags (max 10) | idle, incremental, cozy, desktop, dungeon, traps, slime, cute, relaxing, singleplayer (GOK dat ze alle tien zo op itch.io bestaan; itch.io laat zich niet met curl lezen, dus Thijs of de hoofdchat ziet bij het typen welke er als voorstel verschijnen) |
| AI generation disclosure | No (beelden uit code en Blender, geen AI; zelfde als `platformen/steam/app-aanmaken.md`) |
| App store links | leeg tot de Steam-pagina live is, dan de Steam-link |
| Custom noun | leeg |
| Community | Comments aan (vragen van spelers komen dan bij ons binnen; triage via skill `triage`) |
| Visibility | **Draft** tot het ja van Thijs |
| Cover image | `omslag-630x500.png` (blinde test: zie onder) |
| Screenshots | `schermen/1-*.png` tot en met `schermen/5-*.png`, in die volgorde |
| Trailer | leeg (er is nog geen trailer) |

## Description (CONCEPT, Engels, ±170 woorden)

> **Hats of the Fallen** is an idle game that sits on top of your taskbar while you work. Heroes walk in for Gloop's gold. Every hero who falls into a trap leaves a hat on Gloop's head, and the ones who get away come back with a grudge.
>
> **Dig the tunnel.** Click the dirt to dig a way in for the heroes.
>
> **Set the traps.** Click the tunnel to set a trap. Each hero has a hat, a name and a habit: the knight is slow and tough, the thief jumps over spikes.
>
> **Watch the hats pile up.** Gold buys bigger traps and a bigger Gloop. Later on the gold turns to rubies, and now and then a giant shows up wearing a crown.
>
> **It stays out of your way.** The sky above the tunnel is see-through and clicks go straight to your work. It never takes focus. Pause, sound and size sit in the tray menu.
>
> Free prototype for Windows. Made by Dortus.

Regels die deze tekst volgt: elke zin klopt met het spel op main van 27 nov (reuzen #291, robijnen #280 en #298, doorklikbare lucht en geen focus #24, menu Pause, Sound, Height, Quit in de zip-uitleg). Geen CPU-belofte (geen eigen meting op een gewone laptop), niets over printen of AI, geen belofte van updates.

## Schermen (allemaal echt spelbeeld, niets nagetekend)

| Nr | Bestand | Wat je ziet | Bron |
|---|---|---|---|
| 1 | `schermen/1-bureaublad-55min.png` | het hol onder een notitievenster op een bureaublad, Bard Colossus met kroon in de gang, robijnen om Gloop | Iris, main b4d960c, minuut 54, blinde test GESLAAGD (plek 2, `organisatie/blindtest/uitslag/hats-speelscherm-60min-b4d960c-2026-11-27-2049.md`) |
| 2 | `schermen/2-bureaublad-20min.png` | hetzelfde bureaublad na 20 min, Royal Gloop op de troon | Iris, f0c2a6a, blinde test GESLAAGD (plek 2, `.../hats-speelscherm-20min-f0c2a6a-2026-11-27-1052.md`) |
| 3 | `schermen/3-held-op-weg-naar-gloop.png` | 2x ingezoomd: held met emmerhoed in de gang, twee dichte luiken, hoedenberg en Gloop met kroon op de troon (minuut 22) | eigen film van main 559b2d4, beeld 6750 (zie `LEESMIJ.md`) |
| 4 | `schermen/4-reus-in-de-gang.png` | 2x: reus Sir Hulk met kroon loopt langs de stekelput, "+30 x4" van een vangst (minuut 21) | idem, beeld 6450 |
| 5 | `schermen/5-gloop-en-het-bord.png` | 2x: Gloop, de schat en het bord: "Next: Ruby Gloop, 87 gold to go" en "Sir Hulk ducks in. He does not fit." (minuut 20) | idem, beeld 6150 |

## Omslag

`omslag-630x500.png`, gemaakt met `maak_omslag.py` uit een echt beeld van het spel (zie `LEESMIJ.md`): lucht van een bureaublad met het logo (`ontwerp/steam/winkelpagina/logo-1082x720.png`, gekeurd door Daan 17 nov), daaronder het hol 1,75x vergroot, onderaan een taakbalk. Blinde test: set `organisatie/blindtest/sets/hats-itch-omslag.json`, uitslag in `organisatie/blindtest/uitslag/`. Gaat pas naar buiten als hij daar GESLAAGD staat en Daan ja zegt (CLAUDE.md regel 9).
