# YouTube Short reeks 1, nr 3: His elbow stops at 140 degrees, red past it: 3D printed figure in Blender

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- kanaal: youtube-short
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-shorts-1/short-3-elbow-140-geluid.mp4
- geluid_check: GOED (gemiddeld -17,1 dB, piek -1,5 dB), 21 nov 2026 ±14:45 NL, op het releasebestand (`geluid_check.txt` in de release en zelf nagemeten)
- lengte: 0:10,8, staand 1080x1920
- tijd: (leeg: de hoofdchat plant in YouTube Studio in, 2 tot 3 per dag)
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: Shorts-agent van de hoofdchat (21 nov 2026)
- vorige:

## Titel
His elbow stops at 140 degrees, red past it: 3D printed figure in Blender

## Tekst
```
His elbow bends to 140 degrees and stops there, the limit comes from his rig. Push it further and the arc turns red and tells you how far past the stop you are. Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro 1.1, on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- Beeld: echte staande opname in Blender 5.3.0 met Pro 1.1.0 (zip gebouwd uit commit f727466, dezelfde code als de Gumroad-zip 1.1.0, `platformen/blender-2/gumroad-1.1.md` punt 1), script `commercie/filmpjes/youtube-shorts-1/opname.py` (CJ_SOORT=pro), workflow `youtube-shorts-1.yml` run opname 44904545146, montage 44906228659, `opname-pro.log` en `film-pro.json` in de release. Lichtblauwe MakeHuman-figuur (base.obj, CC0; de kleur is invoer, de add-on kleurt bogen, banden en rood). Geen AI-beeld, geen stem, geen persoon.
- Linkerelleboog 0 tot 140 "from rig" (Limit Rotation 140 in de rig, `producten/blender-gewrichten/e2e/proef_mens.py`), stop 140, voorbij de stop rood bij 152.0° (51 rode vlakken), in beeld "+12° past limit" van de add-on: `film-pro.json` (elleboog_stop, elleboog_pose_rood, elleboog_rood_vlakken), GEZIEN.
- Tekst in beeld (bovenaan, Engels): "His elbow stops at 140°" (0 tot 4.9 s); "Past 140°: red, and it says how far" (4.9 tot 10.77 s). Onderaan de hele tijd het meetadres en "Measured in Blender, not print tested by us yet."
- Geluid: met code gemaakt (`commercie/filmpjes/geluid/geluid.py`: sinustonen en ruis), geen muziek van een ander, geen stem.
- Wat Pro 1.1 kan (Figure from rig, scharnier met eindstop bij ellebogen en knieen, kogel bij schouders, heupen en nek, boog met graden bij elk gewricht, stop uit Limit Rotation of gespiegeld of preset, rood voorbij de stop, Exploded view, export STL of 3MF, "Not print tested by us yet"): `platformen/blender-2/gumroad-1.1.md` (gekeurd door Daan).
- dortus.com/yt: 200, Pro-pagina "Click Joints Pro for Blender: rig to printable figure" (GEZIEN met curl 21 nov ±14:10 NL). Geen Gumroad-adres in titel of tekst. Geen prijs of korting.
- Niet gelijk aan een post van de laatste 14 dagen op YouTube (`commercie/geplaatst.md`: filmpje 2, filmpje 5 op een los been, lange video m3sNvDOJYQ0); deze reeks laat steeds een hele figuur of één gewricht van een figuur zien.
- Zelf bekeken (skill kijken), op het releasebestand: 5 beelden en 4 uit overzicht-3.jpg: elleboog dichtbij, boog 140, rood met "+12° past limit" (klein maar leesbaar op volle maat), terug naar 90.

## Keuring
- keurder: Roep-Keurder, 21 nov 2026 ±21:00 NL
- 1 bron klopt: ja (bronnenlijst in het concept; losse cijfers GEZIEN in beeld)
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (6 beelden uit de video gehaald en geopend: begin, eerste seconde, midden, eind; echte Blender-opname met Click Joints Pro, geen AI-beeld; geluid_check GOED op het gedownloade releasebestand)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: goed: media-URL geeft met GET 200/206 (HEAD geeft 401 op de opslagserver van GitHub, geen fout in het bestand); geen < of >; geen Gumroad-adres; geen klikbare URL; elke Short is oranje (REGELS en vaste opdracht)
- uitkomst: oranje
- reden: Elke YouTube Short is oranje; alle 10 vragen ja en techniek goed, dus de hoofdchat kan hem in de ronde van 21:17 groen zetten (REGELS 21 nov).

## Oranje-besluit
- hoofdchat, 21 nov 2026 21:20 NL: **groen.** Alleen oranje omdat het een Short is (oude opdracht van de Keurder); alle 10 vragen ja en techniek goed. REGELS.md deel YouTube Short (keuze Thijs 21 nov ±12:40): de hoofdchat plant hem in YouTube Studio in.

## Na plaatsen
(alleen de hoofdchat: regel onderaan `commercie/geplaatst.md`)
