# Split a figure into printable parts

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- kanaal: tiktok
- soort: tip
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-tips-1/tip-1-split-printable-parts-geluid.mp4
- geluid_check: GOED (gemiddeld -16,4 dB, piek -1,3 dB), 21 nov 2026 ±19:00 NL, lokaal gemaakt met dezelfde code; op het releasebestand: `geluid_check.txt` in release youtube-tips-1
- lengte: 0:31,1, staand 1080x1920 (ffprobe op het nieuwe releasebestand)
- tijd: 2026-11-26T18:00:00+01:00
- doel: dortus.com/tt
- gemaakt_door: Chris
- vorige: 2026-11-26-tiktok-tip-split.md

Soort: `soort: tip` (opdracht hoofdchat 21 nov ±17:58: tip of demo, om na een week te vergelijken op klikken naar /yt en /tt). Bestandsformaat zelf is video.

## Titel
Split a figure into printable parts

## Tekst
```
Split a figure into printable parts in Blender, in 4 steps: Figure from rig, joints cut in, Exploded view to check every part, export 3MF with one file per part. Made with our add-on Click Joints Pro. Measured in Blender, not print tested by us yet. Type dortus.com/tt in your browser. #blender #3dprinting #blendertips #b3d #articulated #3dprint
```

## Eerste reactie


## Bronnen
- Herstel 22 nov (v2): de eerste versie was rood, het bestand duurde op CI ±17 min (stilstaand eindbeeld, en de beelden pasten niet bij de stappen). `tip.py` knipt nu elk stuk op vaste lengte (-t) en stopt met FOUT buiten 20 tot 60 s; zelfde bestandsnaam opnieuw gemaakt in release youtube-tips-1. Workflow-run op 7c9714a gelukt; het releasebestand zelf gedownload en nagemeten: ffprobe 31,07 s (split, 2,8 MB) en 30,77 s (buigen, 2,7 MB); geluid_check.txt in de release GOED (gemiddeld -16,4 en -16,3 dB, piek -1,3 en -1,4). Releasebestand zelf bekeken (skill kijken), 1 beeld per 2 s: tekst past bij het beeld (lijst, Bend 0,30 tot 120, rood met +12° past limit bij 131,40 en 132, terug 116 en 60; bij split: Figure from rig, lijst, Exploded view, 3MF-export).
- Getallen: 9 gewrichten (2 rig, 2 mirror, 5 preset) en de lijst met hinges en ball joints: film.json metingen youtube-pro-3, GEZIEN in beeld. 10 exportbestanden (3MF, export FINISHED): film.json export.bestanden, GEZIEN; in beeld paneel "Export 3MF". "one file each": 10 bestanden mens_*.3mf, één per deel.
- TikTok-variant van de tip-Short van 22 nov (Afkijker 21 nov ±19:05, punt 1: dezelfde tip haalde bij Malikose op TikTok 19 keer zoveel weergaven). 26 nov: nog geen TikTok op die dag in de wachtrij (hoogstens 1 per dag).
- Vorm: tip in het echte Blender-scherm, kijkvenster boven, paneel van de add-on onder, stap voor stap (afgekeken van Malikose, `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md`). Click Joints Pro lost het probleem op (Afkijker 21 nov ±19:05, punt 2). Onderin alleen "Blender 5.3 + Click Joints Pro" en de printzin, geen adres of prijs in beeld.
- Gemaakt door `commercie/filmpjes/youtube-tips-1/tip.py` uit opname-ruw.mkv van release youtube-pro-3 (Blender 5.3.0, Pro 1.1.0, MakeHuman base.obj CC0); workflow `youtube-tips-1.yml`. Het script knipt, snijdt bij en zet tekst; bogen, getallen, rood, knoppen en lijst komen van de add-on. Geen AI-beeld, geen stem, geen persoon. Geluid met code (`commercie/filmpjes/geluid/geluid.py`), geen muziek van een ander.
- Zelf bekeken (skill kijken): 1 beeld per 2 s van het lokaal gemaakte bestand; tekst steeds in de band bovenaan, paneel leesbaar.
- Geen prijs, geen korting, geen Gumroad-adres.
- Niet gelijk aan de demo-Shorts in de wachtrij: daar alleen het kijkvenster en één belofte; hier het paneel erbij en de stappen.

## Keuring
- keurder: Roep-Keurder, 23 nov 2026 ±20:50 NL
- 1 bron klopt: ja (getallen en stappen staan in beeld; bronnen in het concept)
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (-geluid.mp4, geluid_check GOED -16,3 dB; 4 beelden en een tegel van de hele video bekeken: echt Blender-scherm met paneel van de add-on)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja (geen AI-beeld, geen stem, geen persoon)
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: goed: media bereikbaar (GET 200/206), eerste reactie leeg, geen https of Gumroad, 6 hashtags, tekst ver onder 2.200 tekens, geen < of >, dortus.com/tt zonder https, geen STOP
- uitkomst: groen
- reden: Echt beeld uit Blender, alle 10 vragen ja en techniek goed.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de hoofdchat of de Maker: regel onderaan `commercie/geplaatst.md`)
