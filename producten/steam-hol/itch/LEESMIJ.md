# itch.io-proefpagina: hoe de beelden gemaakt zijn (Sanne, 27 nov 2026, issue #314)

Plakkaart met alle vakken: `PAGINA.md`. Niets hiervan is openbaar; plaatsen doet alleen de hoofdchat na het ja van Thijs.

## Bron: een eigen film van het echte spel
Godot 4.3 Linux onder Xvfb (1920 x 1080), main 559b2d4, lege map, `--write-movie --fixed-fps 5`, argumenten
`hoogte=160 vers=1 zaad=7 balk=0 duur=2700 uitleg_klik=6 koper=1 koper_wacht=8` (zelfde soort speler als in de films van Iris: koopt zodra het kan, graaft). Gestopt na ±24 min speeltijd. 0 SCRIPT ERROR (GEZIEN). Uit het log: reus Sir Hulk binnen op 1226 s, Ruby Gloop gekocht op 1365 s (GEZIEN). De film zelf staat niet in de repo (te groot); alleen het bronbeeld van de omslag (`bron-omslag-f5850.png`, beeld 5850 = 1170 s).

## Omslag v1 (nu `omslag-v1-630x500.png`, NIET GESLAAGD; de omslag van nu is v5, zie onderaan)
`python3 maak_omslag.py bron-omslag-f5850.png 1050 omslag-630x500.png 1.75`: uitsnede van 360 px uit het spel (Gloop op de troon, hoedenberg, schat), 1,75x vergroot, logo uit `ontwerp/steam/winkelpagina/logo-1082x720.png` in een lucht van een bureaublad, taakbalk onderaan. Geen nagetekende figuren: alles onder de lucht is spelbeeld.
Waarom zo: elk echt schermbeeld van het spel haalde plek 2 in de blinde test, elke 3D-header plek 3 ("cheap", "mobile-game-like", GEZIEN in `organisatie/blindtest/uitslag/`). Blinde test: `organisatie/blindtest/sets/hats-itch-omslag.json`.

## Schermen
1 en 2: kopie van de geslaagde bureaubladschermen van Iris (b4d960c minuut 54, f0c2a6a minuut 20).

3 tot 5 (nieuw 28 nov, keuring Daan #324 M2 en K3): 16:9 (1920 x 1080), elk een hoek van een bureaublad zoals op een scherm met schaal 200%, met per scherm een ander werkvenster (recepten, spreadsheet, mail) zodat ze als drie momenten lezen.
- Bron: nieuwe eigen film van main e72baf9, Godot 4.3 Linux onder Xvfb, `--write-movie` (avi, mjpeg-kwaliteit 0,97) `--fixed-fps 5`, argumenten `hoogte=160 vers=1 zaad=7 balk=0 duur=1500 uitleg_klik=6 koper=1 koper_wacht=8`. 0 SCRIPT ERROR (GEZIEN). Uit het log: hol-niveau 9 op 1295 s, reus Sir Hulk binnen op 1301 s met "Sir Hulk ducks in. He does not fit." (GEZIEN).
- Bronbeelden in deze map: `bron-scherm3-1400s.png`, `bron-scherm4-1330s.png`, `bron-scherm5-1305s.png` (1920 x 160, ware grootte).
- `python3 maak_schermen.py <bron> <x0> <web|blad|mail> <uit>`: neemt 960 px van het spelbeeld en verdubbelt elke pixel (NEAREST, geen Lanczos, dus geen vage rand van het opblazen). Venster, lucht en taakbalk zijn op 2x getekend. Het donkere randje en de lichte gloed om helden horen bij het spel (Olaf #242, #276), niet bij het vergroten.
- Gebruikt: `bron-scherm3-1400s.png 400 web`, `bron-scherm4-1330s.png 0 blad`, `bron-scherm5-1305s.png 960 mail`.

**28 nov (Daan #337 M1):** scherm 3 (held valt in de put) weggelaten, op 480 breed een warboel; staat nu in `oud/`. Oud 4 en 5 heten nu 3 en 4. Omslag ronde 2: `maak_omslag_bureau.py`, zie `PAGINA.md`.
Omslag ronde 2 uitslag: v5 GESLAAGD plek 1,0, v4 plek 2,0 (`organisatie/blindtest/uitslag/hats-itch-omslag-2026-11-28-0350.md`); v5 is nu `omslag-630x500.png`.
