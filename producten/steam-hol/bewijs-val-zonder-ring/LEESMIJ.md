# Geen rafelrand om een vallende held, stappen op het kaartje af (#333, Olaf 28 nov)

**Val zonder lichte ring (Mila 28 nov, Daan #357 en #358).** De lichte buitenrand uit `systemen/held_licht.gd` wordt op de maat van het blad gemaakt en NEAREST getekend. Bij een gedraaide, vallende held gaf dat een geblokte, lichte rafelrand buiten de donkere rand. Nu staat de ring uit zolang de held valt (meteen, niet uitfaden); in de put is het achter hem toch donker. Lopen, vluchten en klimmen blijven gelijk.

Bewijs (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=240 vers=1 zaad=11 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=80`, voor = main 85e121f, na = deze commit): in 401 beelden verschillen alleen de beelden 33 tot 35 en 119 tot 121, precies de twee vallen. `val-voor-links-na-rechts-240-3x.png`: links met rafelrand, rechts zonder.

**Stappen op het kaartje (Daan #359 K1 en K2).** Een gekocht steentje heeft nu dezelfde lichte rand eronder als een leeg gaatje, dus is het even groot en leest het als "gat gevuld". Robijn gezien: met startargument `stap_toon=7` (alleen voor bewijsbeelden) toont het kaartje stap 7. `kaartje-stap1-boven-stap7-onder-200-3x.png`: zaad 12 op 76 s, 200 px, boven stap 1 (echt gekocht), onder 6 goud en 1 robijn.

De beelden voor de blinde test (`bewijs-grond-zacht/minuut1-200-*-ware-maat.png`, zaad 11, 75 en 78 s) blijven beeld voor beeld gelijk (opnieuw gemaakt en vergeleken: 0 verschil, GEZIEN), daar valt niemand en is nog niets gekocht.

Toetsen: 11 x 0 FOUT (Linux). Films op 200 en 240 zonder SCRIPT ERROR.
