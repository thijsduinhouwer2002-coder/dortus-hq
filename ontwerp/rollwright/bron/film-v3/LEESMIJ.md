# Film v3 Rollwright (Daan, 8 nov 2026)

Bron van `ontwerp/rollwright/demo-v3.gif` en `demo-v3.mp4`.

- Beelden in het venster: echte Obsidian, run 42530737674 (tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright-reclame4`, rustige Classic van 0.3.2, commit 2fa41c49 plus de spec op tak `ontwerp/rollwright-reclame4`). Het logboek (`gif-064-logboek.png`) is opgenomen na precies dezelfde drie worpen, dus de getallen kloppen met wat je ziet gooien. De opgetilde kaart bij de NAT 20 is `lift-uitsnede.png`, een uitsnede van `poster-ruw-crit-donker.png` uit run 42495072998 (zoom 3). Zet de PNG's in `fr/` naast `film.html` (lift-uitsnede als `fr/lift.png`).
- Lettertypen in `f/`: Cinzel 700 (1.ttf), Fraunces 600 (2.ttf), Inter 500 en 700 (3.ttf, 4.ttf), van Google Fonts (OFL).
- Maken: `node shot.cjs all/%d.png $(python3 -c "print(' '.join(str(i/25) for i in range(400)))")`, daarna ffmpeg (mp4: crf 18; gif: fps 15, breedte 880, 128 kleuren, bayer).
- Eerlijk: alles binnen het venster is de echte gratis plugin. Vonken, warm licht, kaartlijnen en de grote d20 vallen buiten het venster: dat is de presentatie, niet de plugin.
- Versie 2 (8 nov 22:40 UTC): de NAT 20 wordt als echte uitsnede groot uit het venster getild, met stralen en vonken erachter; het venster stapt terug en dooft. Harde snede naar het logboek, geen overvloeier tussen twee vensters. Film 16 s.
- Poster: `poster-v3.html`, maken met `node pshot.cjs poster-v3.html uit.png` (2400x1600).
