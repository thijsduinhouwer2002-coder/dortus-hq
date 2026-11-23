# Fit test hook-B (oude manier): Still guessing joint clearance? Print this first 🧪 | Blender

- status: open
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- hook: oude manier (recept v3); tweeling van fit-hook-a, zelfde rest
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-2/fit-groot-b.mp4
- geluid_check: GOED (-16,4 dB, piek -1,2 dB), zelf gedraaid op het releasebestand 23 nov 2026 ±16:10 NL, GEZIEN; ook in CI (`geluid_check.txt` in release regisseur-2)
- lengte: 0:44,7, staand 1080x1920, h264 plus aac (ffprobe, GEZIEN); sha256 klopt met SHA256SUMS.txt van release regisseur-2 (run 45200069027)
- tijd: voorstel 2026-11-28 17:00 NL; A en B twee dagen uit elkaar, de hoofdchat kiest
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur (opdracht Thijs 23 nov, recept v3), workflow regisseur-2 (nieuwe vorm groot: beeld schermvullend, grote ondertitels)

## Titel
Still guessing joint clearance? Print this first 🧪 | Blender

## Tekst
```
Which clearance fits your printer? Find out before you print a whole figure.
1. In Click Joints Pro 1.2, press Fit test: ball or Fit test: hinge.
2. You get five joints from 0.10 to 0.30 mm clearance, each with its number on top.
3. Print the strip, try each joint, and pick the gap that fits your printer.
4. Put that number in Clearance before you cut the joints in your figure (default 0.2 mm).

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro 1.2. Voice: AI text to speech (Kokoro, Apache 2.0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Still guessing your joint clearance?" gesproken vanaf het eerste beeld, grote kop "Guessing the gap?" (groot, 1,4x). Beeld: de twee strips dichtbij (render-2), dus het probleem "welke speling", niet de productnaam. Geen productnaam in de hook.
- **Fit test: ball / Fit test: hinge, vijf gewrichten van 0.10 tot 0.30 mm, elk met zijn nummer, "so you know which gap fits your printer":** releasenotes 1.2.0 in `platformen/blender/pro-1.2.0.md` (regel "New: Fit test strip") en de knopnamen daar (regel 8).
- **"for knees and elbows" bij de scharnier-strip:** "Elbows and knees get a hinge with an end stop" in `platformen/blender-2/gumroad-1.1.md`.
- **Clearance 0.2 mm standaard:** `platformen/blender-2/gumroad-1.1.md` ("Clearance 0.2 mm by default").
- **Printzin:** "Not print tested by us yet: print a test joint first, every printer is different" (`gumroad-1.1.md`). Geen foto van een geprinte strip: die hebben we niet.
- **Herstel 23 nov ±16:10 (Regisseur run 2):** de versie uit regisseur-1 viel af om drie redenen: het MakeHuman-figuur (Thijs: nep), het beeld stond in een klein venster met veel lege ruimte (saai), en er waren geen grote ondertitels. Nu: geen figuur meer (alleen render-2 met de strips en de Blender-stukken zonder figuur), beeld bijna schermvullend, hook-render over het hele scherm met zoom 1,00 naar 1,18 (beweging vanaf beeld 1, les van Iris), grote ondertitels van 2 tot 3 woorden die met de stem meelopen (getallen geel). Zin 8 begint nu met "Put that number in Clearance".
- **Beeld:** echte opname Blender 5.3.0 met Click Joints Pro 1.2.0 (tag click-joints-pro-v1.2.0, release regisseur-1, run 45187577798), echte muis en klikken op de knoppen (OCR). Montage `commercie/filmpjes/regisseur-2/montage2.py`. Geen figuur in beeld, dus geen modellicentie nodig; alleen onze eigen strips.
- **Stem:** Kokoro-82M, stem af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Geen ElevenLabs (geen geheim ELEVENLABS_API_KEY, geen betaald plan).
- **Synchroon:** CI (`synchroon2.py`, faster-whisper small.en) GOED, 10 van 10 zinnen binnen 0,3 s, grootste verschil 0.16 s (`synchroon-fit-groot-b.md` in de release, GEZIEN). Eigen transcript met faster-whisper base.en (audio als numpy-array) op het releasebestand: alle zinnen gelijk aan het script, whisper schrijft "0.1 to 0.3 millimeters" en "0.2 millimeters" (GEZIEN). De oude meetfout op zin 8 kwam door synchroon.py (zocht maar 0,4 s vooruit, whisper legde het eerste woord in de vorige zin); synchroon2 zoekt 0,6 s voor en na, eerst na 300 ms stilte.
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540x960 en 11 beelden van 0,7 tot 43 s. Eerste beeld: grote kop "Guessing the gap?" over de oranje en blauwe strips die het hele scherm vullen, geen productnaam, geen zwevende getallen. Kan beter: in scène 6 ("Fit test: hinge") valt de knop Fit test: hinge rechts net buiten de uitsnede tijdens de zoom naar de strip; de ondertitel van scène 3 staat over de panelregels (wel leesbaar door de donkere rand).
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over de Fit test strip (RSS en `commercie/geplaatst.md` nagekeken 23 nov, GEZIEN).
- **Meten (recept v3 punt 4):** na 48 uur weergaven en "bleef kijken" van A tegen B, uitslag in `commercie/filmpjes/regisseur-log.md`.

## Keuring
(open)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
