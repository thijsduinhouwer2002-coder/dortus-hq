# Bron film v4 en poster v4 (Daan, 9 nov 2026)

Opnieuw maken in een lege map:
1. `fr/`: alle bestanden uit tak `schermen`, map `rollwright/ontwerp-ontwerp-rollwright-reclame5/` (run 42534527947).
2. `f/`: de vier lettertypen uit `producten/obsidian-rollwright/e2e/ontwerp/drowned.css` op tak `ontwerp/rollwright-reclame5` (base64; Cinzel, Cinzel Decorative, IM Fell English en cursief, SIL OFL), als `cinzel.woff2`, `cinzeldec.woff2`, `fell.woff2`, `felli.woff2`.
3. Van dezelfde tak, uit `e2e/vaults/ontwerp/`: `wolf-head.svg`, `jaw-trap.svg` (ook als `lorc_wolf-trap.svg`) en `drowned-banner.png` (ook als `banner.png`). Iconen: game-icons.net, Lorc, CC BY 3.0.
4. `python3 build.py`, daarna `python3 mk.py a` of `python3 mkb.py`.
5. Beelden: `node shot.cjs a-r.html alla/%d.png 17.4 25` (A) of `node shot.cjs b-r.html allb/%d.png 16.6 25` (B).
6. MP4: `ffmpeg -framerate 25 -i allb/%04d.png -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart uit.mp4`. GIF: fps 15, breedte 760 (B: 720, onder 10 MB), 128 kleuren, bayer 4.
7. Poster: `node pshot.cjs poster-v4.html uit.png` (2400x1600). `card.png` is een uitsnede van `fr/groot-nat20.png` (860,300 tot 1365,505).

Eerlijk: alles in het venster en in de tegels is de echte gratis plugin (rustige Classic 0.3.2) of de echte optionele skins. Stralen, vonken, rood waas, de bestiariumbladen en de woorden vallen buiten de opname. De perkamentnotitie is een snippet van de gebruiker.
