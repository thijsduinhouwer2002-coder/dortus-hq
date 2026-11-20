# Click Joints Pro: Rig to printable figure in Blender (lange YouTube-video 2)

- status: groen
- kanaal: yt-lang
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-pro-3/click-joints-pro-rig-to-figure-geluid.mp4
- geluid_check: GOED (gemiddeld -16,3 dB, piek -0,4 dB), 20 nov 2026 ±15:25 NL, eindrun 44752221946 (`geluid_check.txt` in de release) en zelf nagemeten op het releasebestand
- lengte: 2:19, liggend 1920x1080
- tijd: 2026-11-23T17:00:00+01:00   (kan ook di 24 nov 17:00)
- doel: https://dortus.com/yt/
- gemaakt_door: filmagent van de hoofdchat (20 nov 2026)
- vorige:

Let op voor de Maker: plak de hoofdstukken uit `hoofdstukken.txt` in de release (staan hieronder al, zelfde run). Wil de hoofdchat de korting erbij, dan na de eerste alinea de regel "Click Joints Pro is 25% off from Nov 27 to Dec 1." toevoegen; dan is dit concept oranje (korting, REGELS). Zonder die regel is het een gewone post.

## Titel
Blender rig to 3D printable figure: one button, hinges and ball joints | Click Joints Pro

## Tekst
```
https://dortus.com/yt/

Got a rigged figure in Blender? Click Joints Pro 1.1 turns it into printable parts with one button. Figure from rig puts a hinge with an end stop at every elbow and knee, and a ball joint at shoulders, hips and neck. Next to each joint you see how far it bends, in degrees.

The end stop comes from Limit Rotation in your rig. No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part. Drag Bend to check a hinge: past the stop the arc turns red and shows how far you went. Then Exploded view, and export every part as STL or 3MF.

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different. Recorded in Blender 5.3 with the add-on itself, on a MakeHuman figure (CC0) with a simple 20-bone rig. Works best on figures with separate arms and legs, about 200 mm tall or more.

0:00 What it does
0:10 Start with a rigged figure
0:24 One button, every joint
0:40 Every range in degrees
0:56 Bend to the stop
1:07 Past the stop
1:19 Exploded view
1:37 Export STL or 3MF
1:49 Good to know
2:03 Where to get it

Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
Already bought Pro? 1.1 is a free update.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

## Eerste reactie
```
Click Joints Pro with Figure from rig, one button from rig to printable figure: https://dortus.com/yt/
```

## Bronnen
- Beeld: echte opname in Blender 5.3.0 met de betaalde add-on 1.1.0, workflow `.github/workflows/youtube-pro-3.yml`, script `commercie/filmpjes/youtube-pro-3/opname.py` (opname run 44749515895, montage eindrun 44752221946), montage `maak.py`, release `youtube-pro-3`. Bogen, getallen, rood, lijst en paneel komen van de add-on; het script zet alleen camera, scrollt de zijbalk en drukt op de knoppen. Vergrote stukken zijn uitsneden van de echte zijbalk. Geen AI-beeld, geen stem, geen persoon. Geluid met code gemaakt (`commercie/filmpjes/geluid/geluid.py`).
- 9 gewrichten, ellebogen 0 tot 140, knieën 0 tot 120, kogels ±20, herkomst from rig, mirror, preset: `film.json` in de release (metingen.regels en samenvatting "9 joints · 2 rig · 2 mirror · 5 preset"), GEZIEN.
- Knie stopt op 120, rood voorbij de stop (7 rode vlakken bij 132), weg na terug (0): `film.json` (knie_pose_stop 120,0, knie_pose_rood 132,0, rood_vlakken 7, rood_na_terug 0), GEZIEN. In beeld "+12° past limit".
- Export: 10 bestanden 3MF, melding "10 3MF files", `film.json` metingen.export en `opname.log`, GEZIEN.
- 220 mm en 20 botten: `producten/blender-gewrichten/e2e/proef_mens.py` via scherm_mens (CJ_HOOGTE 220) en logregel "RIG: 20 botten" in `opname.log`, GEZIEN. Linkerknie 120 en linkerelleboog 140 in Limit Rotation: docstring `e2e/scherm_mens.py`.
- Limit Rotation, mirror, preset, botnamen (Rigify, Mixamo ...), "about 200 mm", clearance 0.2 mm, gratis update, "Not print tested by us yet": Gumroad-tekst 1.1 `platformen/blender-2/gumroad-1.1.md` (gekeurd Daan).
- Gratis versie op extensions.blender.org: `commercie/blender-click-joints/`.
- https://dortus.com/yt/: gaf 200 met curl, 20 nov 2026 ±15:00 NL, GEZIEN.
- Zelf bekeken (skill kijken): 11 beelden uit de video (0:03, 0:20, 0:27, 0:36, 1:00, 1:12, 1:25, 1:45, 1:55, 2:10, plus 0:36 opnieuw na een kleine fix), de laatste drie uit het releasebestand zelf: titel en onderschriften binnen beeld, vergroting van lijst, Hinge-schuif (120,00 en 131,70) en export leesbaar, rood en "+12° past limit" zichtbaar, eindkaart met dortus.com/yt.
- Geen gelijke post in de laatste 14 dagen (`commercie/geplaatst.md`): de lange video van 20 nov gaat over het losse scharnier, niet over Figure from rig.

## Keuring
- keurder: Roep-Keurder, 20 Nov 2026 20:45 NL
- 1 bron klopt: ja
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (beelden op 0,1, 1, 20, 40, 60, 69, 80, 100, 120 en 138 s bekeken: hoofdstuktitels, paneel, graden en eindkaart kloppen; geluid_check zelf gedraaid: GOED)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: liggend 2:19; titel onder 100 tekens; geen < of >; geen gumroad.com; https://dortus.com/yt/ op de eerste regel en in de eerste reactie; hoofdstukken beginnen op 0:00; media-URL geeft via GET 302 en downloadt (HEAD via de proxy geeft 401, GEZIEN); geen Short
- uitkomst: groen
- reden: Echte Blender-opname met alle bronnen, https://dortus.com/yt/ op de eerste regel en in de eerste reactie, geen korting in de tekst, alle 10 ja.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
