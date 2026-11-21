# YouTube Short reeks 2, nr 10: How far can a 3D printed knee bend? Check it in Blender

- status: groen
- kanaal: youtube-short
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-shorts-2/short-10-knee-too-far-geluid.mp4
- geluid_check: GOED (gemiddeld -17,2 dB, piek -1,2 dB), 21 nov 2026 ±16:00 NL, lokaal gemaakt met dezelfde code; op het releasebestand: `geluid_check.txt` in release youtube-shorts-2
- lengte: 0:15,7, staand 1080x1920
- tijd: (leeg: de hoofdchat plant in YouTube Studio in, 2 tot 3 per dag)
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: Chris
- vorige:

## Titel
How far can a 3D printed knee bend? Check it in Blender

## Tekst
```
How far can a 3D printed knee bend? This knee stops at 120 degrees, read from the rig. Bend past it and the arc turns red and says how far. Back inside the stop, the red is gone. Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro 1.1, on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- Beeld: opname-ruw.mkv uit release youtube-pro-3, dichtbij de rechterknie, stukken buig, rood en terug. Nieuw tegen Short 2 (knie 120): de titel is een zoekvraag en het stuk terug (rood weer weg, film.json rood_na_terug 0) zit erbij.
- Getallen: knie_stop 120, rood tot +12° voorbij de stop (film.json youtube-pro-3, GEZIEN in beeld "+12° past limit").
- Tekst in beeld: "How far can a / printed knee bend?" (0 tot 3,0 s); "Stop at 120°, / read from his rig" (3,0 tot 7,6 s); "Past 120°: / the arc turns red" (7,6 tot 12,6 s); "Back inside the stop: / red is gone" (12,6 s tot eind). Het rood verschijnt al rond 7 s, net voor de tekst: klein, geen bezwaar.
- Geknipt en van tekst voorzien door `commercie/filmpjes/youtube-shorts-2/kort.py` (kopie van reeks 1, andere stukken; workflow `youtube-shorts-2.yml`, release youtube-shorts-2). Bogen, getallen, rood en lijst komen van de add-on; het script kleurt niets. Geen AI-beeld, geen stem, geen persoon. Grijze of lichtblauwe MakeHuman-figuur (base.obj, CC0).
- Geluid: met code gemaakt (`commercie/filmpjes/geluid/geluid.py`), geen muziek van een ander, geen stem. geluid_check eerst lokaal door Chris op dezelfde code en dezelfde ruwe opnames (21 nov ±16:00 NL); de release draait dezelfde check (`geluid_check.txt`).
- Wat Pro 1.1 kan: `platformen/blender-2/gumroad-1.1.md` (gekeurd door Daan). dortus.com/yt: Pro-pagina (GEZIEN met curl door de Shorts-agent 21 nov ±14:10 NL). Geen Gumroad-adres, geen prijs of korting.
- Variant op reeks 1 (zoals Cleave doet), niet hetzelfde filmpje: andere stukken of een andere belofte, zie hieronder.
- Zelf bekeken (skill kijken): 1 beeld per seconde van het lokaal gemaakte bestand. Tekst staat steeds in het vlak bovenaan, meetadres en printzin onderaan leesbaar.

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
