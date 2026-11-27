# itch.io-proefpagina: hoe de beelden gemaakt zijn (Sanne, 27 nov 2026, issue #314)

Plakkaart met alle vakken: `PAGINA.md`. Niets hiervan is openbaar; plaatsen doet alleen de hoofdchat na het ja van Thijs.

## Bron: een eigen film van het echte spel
Godot 4.3 Linux onder Xvfb (1920 x 1080), main 559b2d4, lege map, `--write-movie --fixed-fps 5`, argumenten
`hoogte=160 vers=1 zaad=7 balk=0 duur=2700 uitleg_klik=6 koper=1 koper_wacht=8` (zelfde soort speler als in de films van Iris: koopt zodra het kan, graaft). Gestopt na ±24 min speeltijd. 0 SCRIPT ERROR (GEZIEN). Uit het log: reus Sir Hulk binnen op 1226 s, Ruby Gloop gekocht op 1365 s (GEZIEN). De film zelf staat niet in de repo (te groot); alleen het bronbeeld van de omslag (`bron-omslag-f5850.png`, beeld 5850 = 1170 s).

## Omslag `omslag-630x500.png`
`python3 maak_omslag.py bron-omslag-f5850.png 1050 omslag-630x500.png 1.75`: uitsnede van 360 px uit het spel (Gloop op de troon, hoedenberg, schat), 1,75x vergroot, logo uit `ontwerp/steam/winkelpagina/logo-1082x720.png` in een lucht van een bureaublad, taakbalk onderaan. Geen nagetekende figuren: alles onder de lucht is spelbeeld.
Waarom zo: elk echt schermbeeld van het spel haalde plek 2 in de blinde test, elke 3D-header plek 3 ("cheap", "mobile-game-like", GEZIEN in `organisatie/blindtest/uitslag/`). Blinde test: `organisatie/blindtest/sets/hats-itch-omslag.json`.

## Schermen
1 en 2: kopie van de geslaagde bureaubladschermen van Iris (b4d960c minuut 54, f0c2a6a minuut 20). 3 tot 5: uitsneden uit de film hierboven, 2x vergroot (Lanczos), beelden 6750, 6450 en 6150.
