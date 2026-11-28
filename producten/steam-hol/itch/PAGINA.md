# itch.io-proefpagina Hats of the Fallen: plakkaart (Sanne, 27 nov 2026, issue #314)

**Niet openbaar zetten.** Plaatsen doet alleen de hoofdchat, en pas na het ja van Thijs op het spel (#314 punt 3, `organisatie/plan-tot-half-december.md`). De pagina vraagt een itch.io-account van Thijs; aanmaken en inloggen doet Thijs zelf. Alle spelerstekst hieronder is **CONCEPT** tot Thijs hem in eigen woorden schrijft of goedkeurt.

Lat: Rusty's Retirement en Spirit City: Lofi Sessions (`organisatie/lat/hats.md`). Wat hun pagina doet en wij overnemen: in zin 1 soort en plek ("sits at the bottom of your screen while you do other things"), dan pas de haak; korte kopjes die een daad zijn; schermen die het spel op een bureaublad tonen (GEZIEN in de lat, 25 nov). Wat wij beter doen dan zij (gaten uit de lat): je kunt weghalen en geld terugkrijgen, het spel pakt nooit de focus, en na minuut 25 komt er nog steeds iets nieuws (robijnen, reuzen).

## Vakken op itch.io, van boven naar onder (Create new project)

| Vak | Invullen |
|---|---|
| Title | Hats of the Fallen |
| Project URL | hats-of-the-fallen |
| Short description or tagline | Your taskbar has a dungeon now. An idle trap game that lives just above your taskbar while you work. |
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
| Cover image | `omslag-630x500.png` (= v5, blinde test GESLAAGD plek 1,0). Opvolger v6 of v7 (hol op ware maat, Daan #348 M1) in de blinde test; de geslaagde wordt de omslag na een ja van Daan |
| Screenshots | `schermen/1-*.png` tot en met `schermen/4-*.png`, in die volgorde (ronde 3, 28 nov: één overzicht en drie grote spelmomenten, Daan #348) |
| Trailer | leeg (er is nog geen trailer) |

## Description (CONCEPT, Engels, ±170 woorden)

> **Hats of the Fallen** is an idle game that sits on top of your taskbar while you work. Heroes walk in for Gloop's gold. Every hero who falls into a trap leaves a hat on Gloop's head, and the ones who get away come back with a grudge.
>
> **Dig the tunnel.** Click the dirt to dig a way in for the heroes.
>
> **Set the traps.** Click the tunnel to set a trap. Each hero has a hat, a name and a habit: the knight is slow and tough, the thief jumps over spikes.
>
> **Watch the hats pile up.** Gold buys bigger traps and a bigger Gloop. Later on your traps start to glow with rubies, and now and then a giant shows up wearing a crown.
>
> **It stays out of your way.** The sky above the tunnel is see-through and clicks go straight to your work. It never takes focus. Pause, sound and size sit in the tray menu.
>
> Free prototype for Windows. Made by Dortus.

Regels die deze tekst volgt: elke zin klopt met het spel op main van 27 nov (reuzen #291, robijnen #280 en #298, doorklikbare lucht en geen focus #24, menu Pause, Sound, Height, Quit in de zip-uitleg). Geen CPU-belofte (geen eigen meting op een gewone laptop), niets over printen of AI, geen belofte van updates.

## Schermen (allemaal echt spelbeeld, niets nagetekend)

| Nr | Bestand | Wat je ziet | Bron |
|---|---|---|---|
| 1 | `schermen/1-op-je-scherm.png` | "zo zit het op je scherm": een heel bureaublad van 1920 x 1080 met een notitievenster, onderaan de strook op ware maat (240 px), een val vangt een held: "+26 x2", het bord "Tibbe II took the short way down. +26" | eigen film main 46ca6e9, `hoogte=240`, 1365 s |
| 2 | `schermen/2-reus-met-kroon.png` | 16:9, spreadsheet erboven, spel 2x: reus Sir Hulk met kroon komt de ladder af, bordje "9" van het hol-niveau, kamers met fijne korrel | idem, 1258 s |
| 3 | `schermen/3-gloop-en-een-held.png` | 16:9, mail erboven, spel 2x: een held met een zweetdruppel loopt de gang in naar Gloop met kroon op de troon, hoedenberg en schat | idem, 1376 s |
| 4 | `schermen/4-kopen-met-undo.png` | 16:9, recepten erboven, spel 2x: Gloop op de troon en het kaartje "Trick Lid, Bought." met Undo +70 | idem, 681 s |

Ronde 3 (28 nov, Daan #348 M2, M3, K2): de oude vier (twee bijna gelijke bureaubladen en twee schermen van vóór de fijne korrel ca6f928) staan in `oud/v5-schermen/`. Alle vier nu uit één eigen film van main 46ca6e9 (na ca6f928 en 52507cc), op `hoogte=240`: geen blokjes van 5 x 5 meer, scherm 2 tot 4 elke pixel precies 2x (NEAREST). Het echte icoon staat in elke taakbalk.

## Omslag

`omslag-630x500.png`, gemaakt met `maak_omslag.py` uit een echt beeld van het spel (zie `LEESMIJ.md`): lucht van een bureaublad met het logo (`ontwerp/steam/winkelpagina/logo-1082x720.png`, gekeurd door Daan 17 nov), daaronder het hol 1,75x vergroot, onderaan een taakbalk. Blinde test: set `organisatie/blindtest/sets/hats-itch-omslag.json`, uitslag in `organisatie/blindtest/uitslag/`. Gaat pas naar buiten als hij daar GESLAAGD staat en Daan ja zegt (CLAUDE.md regel 9).

### Uitslag blinde test omslag (27 nov, Gemini flash-lite, GEZIEN in de runs 46067538274 en 46067751109)
v1 (hol 1,75x), v2 (ware grootte, groot logo) en v3 (1,25x): alle drie **NIET GESLAAGD**, plek 3,0, eerste keus steeds Spirit City. Zinnen: "cheap and generic mobile-game", "no clear indication that it makes a good background PC companion", "adopt a softer, less saturated art style that feels more native to a PC desktop". De echte bureaubladschermen halen wel plek 2. **Volgende ronde:** omslag als uitsnede van een echt bureaubladscherm (venster plus hol op ware grootte, zoals scherm 1) met een vlakke, rustige titel in plaats van het 3D-logo, minder verzadigd. Tot dan geen omslag naar buiten.

### Ronde 2 omslag (28 nov, Sanne): bureaublad met vlakke titel
`maak_omslag_bureau.py` (zie de kop van het script): hol uit een eigen film (`bron-scherm5-1305s.png`, x 1035 tot 1455, 1,5x), erboven een werkvenster, onderaan een taakbalk met het echte icoon, titel vlak (Poppins Bold), geen 3D-logo.
- `omslag-v4-630x500.png`: de titel staat als kop in een Notes-venster ("A tiny dungeon above your taskbar.", afvinklijst met "check on Gloop").
- `omslag-v5-630x500.png`: titel vlak in de lucht met het label "Lives above your taskbar", een mailvenster rechts.
**Uitslag (Gemini flash-lite, GEZIEN, `organisatie/blindtest/uitslag/hats-itch-omslag-2026-11-28-0350.md`): v5 GESLAAGD plek 1,0 (beide rondes eerste keus, vóór Rusty's Retirement), v4 GESLAAGD plek 2,0.** Het eerste beeld van Hats ooit op plek 1. Reden letterlijk: "It explicitly shows it lives above your taskbar next to real windows". Wens van de rechter: titel iets eigener en verzorgder. v5 is nu `omslag-630x500.png` (oude v1 heet `omslag-v1-630x500.png`). Gaat naar buiten na ja van Daan en het ja van Thijs op het spel.

### Ronde 3 omslag (28 nov, Sanne, Daan #348 M1 en K1)
Zelfde opbouw, titel en venster als v5, maar het hol komt uit een nieuwe eigen film van main 46ca6e9 (na de fijne korrel ca6f928 en de knoppen 52507cc) op `hoogte=240`, dus op ware maat: `bron-omslag6-240-1338s.png`, x 820 tot 1450 (hoedenberg, Gloop met kroon op de troon, schat), niet meer 1,5x opgeschaald.
- `omslag-v6-630x500.png`: alleen het nieuwe hol.
- `omslag-v7-630x500.png`: ook de titel met de gouden rand van het houten bord uit het spel (K1), vlak, geen 3D.
Blinde test: set `hats-itch-omslag` ronde 3. Uitslag volgt in `organisatie/blindtest/uitslag/`.
