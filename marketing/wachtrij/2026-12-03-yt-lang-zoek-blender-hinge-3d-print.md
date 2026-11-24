# Blender hinge for 3D printing, with an end stop (zoekvraag-video 2)

- status: ingepland
- kanaal: yt-lang
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/youtube-zoek-1/zoek-b-blender-hinge-3d-print-geluid.mp4
- geluid_check: GOED (gemiddeld -16,3 dB, piek -1,1 dB), 21 nov 2026 ±13:30 NL, `geluid_check.txt` in release youtube-zoek-1 (run 44901209695, groen)
- lengte: 1:50, liggend 1920x1080
- tijd: 2026-12-03T17:00:00+01:00
- doel: https://dortus.com/yt/
- gemaakt_door: Chris
- vorige:

Let op voor de Maker: hoofdstukken staan in `zoek-b-hoofdstukken.txt` in de release (hieronder al overgenomen).

## Titel
Blender hinge for 3D printing: a hinge with an end stop

## Tekst
```
https://dortus.com/yt/

Blender hinge for 3D printing, the short answer: cut the part where it should bend, put a hinge in the cut with clearance, and give it an end stop so it stops where it should.

In this video we do it with Click Joints Pro 1.1 on a rigged figure: elbows and knees get a hinge, and each hinge takes its range from Limit Rotation in your rig (no limit on one side: it takes the other side, no limit at all: a preset). Drag Bend to check it: the knee stops at 120 degrees, and past the stop the arc turns red and shows how far you went. Then Exploded view and export every part as STL or 3MF.

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different. Recorded in Blender 5.3 with the add-on itself, on a MakeHuman figure (CC0) with a simple 20-bone rig. Clearance is 0.2 mm by default.

0:00 The short answer
0:10 Place the hinges
0:33 The end stop
0:54 Past the stop
1:06 Check and export
1:25 Good to know
1:38 Where to get it

No rig? Put the 3D cursor where the part should bend and pick Elbow or Knee.

#blender #3dprinting #b3d
```

## Eerste reactie
```
Click Joints Pro, a hinge with an end stop for 3D printing in Blender: https://dortus.com/yt/
```

## Bronnen
- Zoekvraag: YouTube-suggestie "blender hinge 3d print" bij `curl "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=blender+hinge"`, 21 nov 2026 ±12:40 NL, GEZIEN.
- Beeld: geknipt uit de echte opname van release `youtube-pro-3` (`opname-ruw.mkv`, Blender 5.3.0, betaalde add-on 1.1.0, opname run 44749515895). Script `commercie/filmpjes/youtube-zoek/maak_zoek.py` (video b), workflow `.github/workflows/youtube-zoek.yml`, release `youtube-zoek-1`. Geen AI-beeld, geen stem, geen persoon.
- Knie stopt op 120, rood voorbij de stop (132, 7 rode vlakken), weg na terug: `film.json` in release `youtube-pro-3`, GEZIEN.
- Limit Rotation, mirror, preset, presets Elbow en Knee, clearance 0.2 mm, "Not print tested by us yet": `platformen/blender-2/gumroad-1.1.md` (gekeurd Daan).
- Zelf bekeken (skill kijken): beeld op 4 s (antwoord in drie regels leesbaar, label "Right knee" vrij van het titelvak), overzicht `zoek-b-overzicht.jpg`.
- Verschil met eerdere posts: de lange video van 20 nov ging over het losse scharnier (andere opname), die van 23 nov over Figure from rig. Deze heeft de zoekvraag als titel en het antwoord eerst. Keurder beslist over punt 8.

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
- ingepland: 22 nov 2026 20:15 NL, Metricool-nummer 437867758, moment 2026-12-03 17:00 NL, status PENDING (GEZIEN createScheduledPost). Keuring groen Roep-Keurder commit c71ce042. Techniek: media GET 206 (HEAD 401 op de opslagserver), geen < of >, geen Gumroad, https://dortus.com/yt/ op regel 1 en in de eerste reactie.
- gelezen: 24 nov 2026 20:15 NL: hoofdchat paste de tekst aan op 24 nov 17:51 (Fit test-zin), Metricool-nummer nu 440578360, moment ongewijzigd, PENDING, geen draft (GEZIEN getScheduledPosts).
