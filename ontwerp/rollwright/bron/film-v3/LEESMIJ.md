# Film v3 Rollwright (Daan, 8 nov 2026)

Bron van `ontwerp/rollwright/demo-v3.gif` en `demo-v3.mp4`.

- Beelden in het venster: echte Obsidian, run 42495072998 (tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright-reclame2`, rustige Classic van 0.3.2). Zet die PNG's in `fr/` naast `film.html`.
- Lettertypen in `f/`: Cinzel 700 (1.ttf), Fraunces 600 (2.ttf), Inter 500 en 700 (3.ttf, 4.ttf), van Google Fonts (OFL).
- Maken: `node shot.cjs all/%d.png $(python3 -c "print(' '.join(str(i/25) for i in range(375)))")`, daarna ffmpeg (mp4: crf 18; gif: fps 15, breedte 880, 128 kleuren, bayer).
- Eerlijk: alles binnen het venster is de echte gratis plugin. Vonken, warm licht, kaartlijnen en de grote d20 vallen buiten het venster: dat is de presentatie, niet de plugin.
