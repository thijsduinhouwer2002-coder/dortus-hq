# Check if a joint bends too far before you 3D print it

- status: rood
- kanaal: youtube-short
- soort: tip
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-tips-1/tip-2-check-bend-before-print-geluid.mp4
- geluid_check: GOED (gemiddeld -16,2 dB, piek -1,4 dB), 21 nov 2026 ±19:00 NL, lokaal gemaakt met dezelfde code; op het releasebestand: `geluid_check.txt` in release youtube-tips-1
- lengte: 0:30,8, staand 1080x1920 (ffprobe op het nieuwe releasebestand)
- tijd: (leeg: de hoofdchat plant in YouTube Studio in, 2 tot 3 per dag)
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: Chris
- vorige: 2026-11-22-yt-short-tip-buigen.md

Soort: `soort: tip` (opdracht hoofdchat 21 nov ±17:58: tip of demo, om na een week te vergelijken op klikken naar /yt en /tt). Bestandsformaat zelf is video.

## Titel
Check if a joint bends too far before you 3D print it

## Tekst
```
Check if a joint bends too far before you print. Step 1: every joint shows its range in degrees, read from the rig. Step 2: turn on Show bend range and drag Bend to the stop, here 120 degrees. Step 3: past the stop the arc turns red and says how far. Step 4: back inside the stop, the red is gone. Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro 1.1, on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- Herstel 22 nov (v2): de eerste versie was rood, het bestand duurde op CI ±17 min (stilstaand eindbeeld, en de beelden pasten niet bij de stappen). `tip.py` knipt nu elk stuk op vaste lengte (-t) en stopt met FOUT buiten 20 tot 60 s; zelfde bestandsnaam opnieuw gemaakt in release youtube-tips-1. Workflow-run op 7c9714a gelukt; het releasebestand zelf gedownload en nagemeten: ffprobe 31,07 s (split, 2,8 MB) en 30,77 s (buigen, 2,7 MB); geluid_check.txt in de release GOED (gemiddeld -16,4 en -16,3 dB, piek -1,3 en -1,4). Releasebestand zelf bekeken (skill kijken), 1 beeld per 2 s: tekst past bij het beeld (lijst, Bend 0,30 tot 120, rood met +12° past limit bij 131,40 en 132, terug 116 en 60; bij split: Figure from rig, lijst, Exploded view, 3MF-export).
- Getallen: knie_stop 120 (Bends 0° to 120°, van de rig), rood tot 132 ("+12° past limit" in beeld), rood_na_terug 0: film.json youtube-pro-3, GEZIEN in beeld (Bend 120.00, 131.70, 132.00, 60.00 in het paneel).
- Vorm: tip in het echte Blender-scherm, kijkvenster boven, paneel van de add-on onder, stap voor stap (afgekeken van Malikose, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md`). Click Joints Pro lost het probleem op (Afkijker 21 nov ±19:05, punt 2). Onderin alleen "Blender 5.3 + Click Joints Pro" en de printzin, geen adres of prijs in beeld.
- Gemaakt door `commercie/filmpjes/youtube-tips-1/tip.py` uit opname-ruw.mkv van release youtube-pro-3 (Blender 5.3.0, Pro 1.1.0, MakeHuman base.obj CC0); workflow `youtube-tips-1.yml`. Het script knipt, snijdt bij en zet tekst; bogen, getallen, rood, knoppen en lijst komen van de add-on. Geen AI-beeld, geen stem, geen persoon. Geluid met code (`commercie/filmpjes/geluid/geluid.py`), geen muziek van een ander.
- Zelf bekeken (skill kijken): 1 beeld per 2 s van het lokaal gemaakte bestand; tekst steeds in de band bovenaan, paneel leesbaar.
- Geen prijs, geen korting, geen Gumroad-adres.
- Niet gelijk aan de demo-Shorts in de wachtrij: daar alleen het kijkvenster en één belofte; hier het paneel erbij en de stappen.

## Keuring
- Keurder 22 nov ±21:30 NL: rood. Eerste beeld is weer een grijze kale pop vol getallen (onder shorts-4), "read from the rig" klopt niet (2 van 9 from rig), bijna gelijk aan knee-bend-v2 en knie-te-ver (vraag 8), 30,8 s waar REGELS 40 tot 60 s vraagt; ffprobe en geluid_check GOED. Zie `marketing/keuring/2026-11-22-yt-tips-v2.md`.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de hoofdchat of de Maker: regel onderaan `commercie/geplaatst.md`)
