# Hook-A (probleem): Your figure's knees bend too far? Check before you print 🦵 | Blender

- status: groen
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- hook: probleem (recept v3); tweeling van hook-b, zelfde rest
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/stem-proef-1/knee-hook-a-staand.mp4 (komt erin zodra workflow stem-proef klaar is)
- geluid_check: GOED lokaal (-16,4 dB, piek -1,3 dB), 23 nov 2026 ±13:00 NL, GEZIEN; CI-uitslag in `geluid_check.txt` van de release
- lengte: 0:56,9 lokaal, staand 1080x1920 (GEZIEN)
- tijd: voorstel 2026-11-25 17:00 NL; A en B twee dagen uit elkaar, de hoofdchat kiest
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Chris (opdracht hoofdchat 23 nov ±12:45, recept v3)
- vorige: 2026-11-25-yt-short-knee-bend-stem (zelfde film zonder echte hook)

## Titel
Your figure's knees bend too far? Check before you print 🦵 | Blender

## Tekst
```
How far can the knee of your 3D printed figure bend? Check it in Blender before you print.
1. Select your rigged figure and press Figure from rig.
2. The list shows every joint with its range: our left knee is a hinge from 0 to 120°, from the rig. The right knee mirrors it.
3. Drag the Bend slider. At 120° it reaches the end stop; past it you see a red arc and "+12° past limit".
4. Exploded view shows the ball joints. Export every part as 3MF.

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro 1.1. Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us. Voice: AI text to speech (Kokoro, Apache 2.0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Your figure's knees bend too far?" (gesproken 0,15 tot 1,84 s), grote kop "Knees bending too far?" in rood label PROBLEM. Beeld vanaf het eerste beeld: de knie op 132° met de rode boog en "+12° past limit" (opname youtube-shorts-4, deel knie_rood, bronbeelden 40 tot 97), dus het probleem, niet het product. Geen productnaam in de hook. GEZIEN in beelden op 0,3, 0,9 en 1,5 s.
- **Rest:** zin 2 tot 15 gelijk aan `2026-11-25-yt-short-knee-bend-stem` (groen gekeurd 23 nov ±12:45); alleen de oude openingszin "How far can this knee bend? Let's check it before we print." is vervangen door de hook.
- **Synchroon (lokaal, GEZIEN):** 15 van 15 binnen 0,3 s, grootste 0,19 s, faster-whisper small.en vond alle woorden terug.
- **Script:** `commercie/filmpjes/stem/proef-1-hook-a.json`; montage.py kreeg `groot` (kop 1,4x) voor de hook.
- **Meten (recept v3 punt 4):** na 48 uur weergaven en "bleef kijken" van A tegen B in YouTube Studio, uitslag in `commercie/filmpjes/regisseur-log.md`.

## Keuring
- keurder: Daan, 23 nov 2026 ±14:45 NL (opdracht hoofdchat 12:05, punt 2)
- 1 beweringen kloppen met een bron: ja (lijst, schuif 120/132, +12° past limit, Export 3MF in beeld)
- 2 geen AI-zinnen, AI-stem gemeld: ja (Kokoro, Apache 2.0, in de tekst)
- 3 geen medische claim: ja
- 4 niets over Hats: ja
- 5 echt beeld zelf bekeken, geluid_check GOED: ja (eerste beeld op 540 px en 13 beelden van 0,05 tot 55 s; naam eindigt niet op -geluid.mp4, wel geluidsspoor en GOED)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja (57 s, hook in de eerste seconde)
- 8 niet gelijk aan een post van de laatste 14 dagen: ja, op het randje (derde/vierde knie-Short in een week, maar A/B-proef op opdracht hoofdchat)
- 9 geen AI-beeld, AI-stem volgens uitzondering, echte hook in 1,5 s: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: goed (titel onder 100, geen < >, 1 emoji, 5 hashtags, dortus.com/yt over te typen, geen prijs)
- uitkomst: groen
- reden: echte opname, tekst klopt met beeld en hook staat in de eerste seconde; kan-punten in `marketing/keuring/2026-11-23-yt-short-knee-hook-ab-daan.md`.

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
