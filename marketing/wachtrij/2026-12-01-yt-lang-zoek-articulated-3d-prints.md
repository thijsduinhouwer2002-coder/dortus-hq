# How to make articulated 3D prints in Blender (zoekvraag-video 1)

- status: ingepland
- kanaal: yt-lang
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-zoek-1/zoek-a-articulated-3d-prints-blender-geluid.mp4
- geluid_check: GOED (gemiddeld -16,3 dB, piek -0,6 dB), 21 nov 2026 ±13:30 NL, `geluid_check.txt` in release youtube-zoek-1 (run 44901209695, groen)
- lengte: 1:45, liggend 1920x1080
- tijd: 2026-12-01T17:00:00+01:00
- doel: https://dortus.com/yt/
- gemaakt_door: Chris
- vorige:

Let op voor de Maker: hoofdstukken staan in `zoek-a-hoofdstukken.txt` in de release (hieronder al overgenomen). Geen korting in de tekst: de Cyber Sale is 1 dec voorbij.

## Titel
How to make articulated 3D prints in Blender

## Tekst
```
https://dortus.com/yt/

How to make articulated 3D prints in Blender, the short answer: cut the model where it bends, put a joint in every cut with a bit of clearance, then check the fit and export every part.

In this video we do it on a rigged figure with Click Joints Pro 1.1. One button (Figure from rig) cuts the figure at every joint: a hinge with an end stop at elbows and knees, a ball joint at shoulders, hips and neck. Next to each joint you see how far it bends, in degrees. Exploded view shows every part before you print, clearance is 0.2 mm by default, and every part exports as STL or 3MF.

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different. Recorded in Blender 5.3 with the add-on itself, on a MakeHuman figure (CC0) with a simple 20-bone rig. Works best on figures with separate arms and legs, about 200 mm tall or more.

0:00 The short answer
0:12 Cut where it bends
0:34 A joint in every cut
0:55 Check the fit and export
1:19 Good to know
1:33 Where to get it

No rig? Put the 3D cursor on a joint and pick the body part (shoulder, hip, neck, elbow, knee, ankle).
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

## Eerste reactie
```
Click Joints Pro, one button from a rigged figure to printable parts with joints: https://dortus.com/yt/
```

## Bronnen
- Zoekvraag: YouTube-suggestie "how to make articulated 3d prints in blender" bij `curl "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=how+to+make+articulated"`, 21 nov 2026 ±12:40 NL, GEZIEN.
- Beeld: geknipt uit de echte opname van release `youtube-pro-3` (`opname-ruw.mkv`, Blender 5.3.0, betaalde add-on 1.1.0, opname run 44749515895, gekeurd groen door de Roep-Keurder 20 nov). Script `commercie/filmpjes/youtube-zoek/maak_zoek.py` (video a), workflow `.github/workflows/youtube-zoek.yml`, release `youtube-zoek-1`. Geen AI-beeld, geen stem, geen persoon. Geluid met code (`commercie/filmpjes/geluid/geluid.py`).
- 9 gewrichten, knie 120, elleboog 140, 10 delen als 3MF: `film.json` in release `youtube-pro-3` (metingen), GEZIEN.
- 220 mm, 20 botten: zie de bronnen van `2026-11-23-yt-lang-pro-rig-to-figure.md` (zelfde opname).
- Clearance 0.2 mm, "about 200 mm", presets zonder rig, "Not print tested by us yet": Gumroad-tekst 1.1 `platformen/blender-2/gumroad-1.1.md` (gekeurd Daan).
- Gratis versie op extensions.blender.org: `commercie/blender-click-joints/`.
- Zelf bekeken (skill kijken): overzicht van 12 beelden (`zoek-a-overzicht.jpg`) en beelden op 3, 20, 40, 60, 75 en 98 s: antwoord in drie regels leesbaar, vergroting van knop, lijst, Hinge en export leesbaar, eindkaart met dortus.com/yt. Kan: het titelvak raakt het label "Right knee: bends 0° to 120°" bovenin de eerste 12 s.
- Niet gelijk aan een post van de laatste 14 dagen: zelfde opname als de video van 23 nov, maar andere titel, opbouw (antwoord eerst, zoekvraag als onderwerp) en tekst; ligt 8 dagen later. Keurder beslist.

## Keuring
- keurder: Roep-Keurder, 21 nov 2026 ±21:00 NL
- 1 bron klopt: ja (bronnenlijst in het concept; losse cijfers GEZIEN in beeld)
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (6 beelden verspreid over de video, 8 tegels erbij geopend: echte Blender-schermopname met Click Joints Pro, einde met eindkaart; geluid_check GOED op het gedownloade bestand; duur 105 s en 111 s klopt met het concept)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: goed: eerste regel van de beschrijving https://dortus.com/yt/ en dezelfde URL in de eerste reactie; liggend 1920x1080; titel onder 100 tekens; geen < of >; geen Gumroad-adres; media-URL geeft met GET 200/206 (HEAD geeft 401 op de opslagserver, geen fout in het bestand); gewone lange video, geen Short, geen prijs
- uitkomst: groen
- reden: Alle 10 vragen ja, echt Blender-beeld, meetadres op de eerste regel en in de eerste reactie, geen Gumroad-adres.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
- ingepland: 22 nov 2026 20:15 NL, Metricool-nummer 437867666, moment 2026-12-01 17:00 NL, status PENDING (GEZIEN createScheduledPost). Keuring groen Roep-Keurder commit c71ce042. Techniek: media GET 206 (HEAD 401 op de opslagserver, zoals de Keurder zag), geen < of >, geen Gumroad, https://dortus.com/yt/ op regel 1 en in de eerste reactie.
- gelezen: 24 nov 2026 20:15 NL: hoofdchat paste de tekst aan op 24 nov 17:51 (Fit test-zin), Metricool-nummer nu 440578342, moment ongewijzigd, PENDING, geen draft (GEZIEN getScheduledPosts).
