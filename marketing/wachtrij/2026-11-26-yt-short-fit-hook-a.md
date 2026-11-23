# Fit test hook-A (probleem): Which joint gap fits your 3D printer? Test it first 🧪 | Blender

- status: open
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- hook: probleem (recept v3); tweeling van fit-hook-b, zelfde rest
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-1/fit-hook-a-geluid.mp4
- geluid_check: GOED (-16,3 dB, piek -1,4 dB), zelf gedraaid op het releasebestand 23 nov 2026 ±14:45 NL, GEZIEN; ook in CI (`geluid_check.txt` in de release)
- lengte: 0:44,3, staand 1080x1920, h264 plus aac (ffprobe, GEZIEN); sha256 klopt met SHA256SUMS.txt van de release (run 45183978863)
- tijd: voorstel 2026-11-26 17:00 NL; A en B twee dagen uit elkaar, de hoofdchat kiest
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur (opdracht Thijs 23 nov, recept v3), workflow regisseur-1

## Titel
Which joint gap fits your 3D printer? Test it first 🧪 | Blender

## Tekst
```
Which clearance fits your printer? Find out before you print a whole figure.
1. In Click Joints Pro 1.2, press Fit test: ball or Fit test: hinge.
2. You get five joints from 0.10 to 0.30 mm clearance, each with its number on top.
3. Print the strip, try each joint, and pick the gap that fits your printer.
4. Set that clearance before you cut the joints in your figure (default 0.2 mm).

Measured in Blender, not print tested by us yet. Print a test joint first, every printer is different.

Screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro 1.2. Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), clothes, colours and rig added by us. Voice: AI text to speech (Kokoro, Apache 2.0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Not sure which gap your printer needs?" gesproken vanaf het eerste beeld, grote kop "Which gap fits?" (groot, 1,4x). Beeld: de twee strips dichtbij (render-2), dus het probleem "welke speling", niet de productnaam. Geen productnaam in de hook.
- **Fit test: ball / Fit test: hinge, vijf gewrichten van 0.10 tot 0.30 mm, elk met zijn nummer, "so you know which gap fits your printer":** releasenotes 1.2.0 in `platformen/blender/pro-1.2.0.md` (regel "New: Fit test strip") en de knopnamen daar (regel 8).
- **"for knees and elbows" bij de scharnier-strip:** "Elbows and knees get a hinge with an end stop" in `platformen/blender-2/gumroad-1.1.md`.
- **Clearance 0.2 mm standaard:** `platformen/blender-2/gumroad-1.1.md` ("Clearance 0.2 mm by default").
- **Printzin:** "Not print tested by us yet: print a test joint first, every printer is different" (`gumroad-1.1.md`). Geen foto van een geprinte strip: die hebben we niet.
- **Beeld:** echte opname Blender 5.3.0 met Click Joints Pro 1.2.0 (tag click-joints-pro-v1.2.0), echte muis en klikken op de knoppen (opname.py, OCR), renders in de studio van `commercie/filmpjes/studio`. Figuur MakeHuman CC0 1.0 (`commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md`).
- **Stem:** Kokoro-82M, stem af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Geen ElevenLabs (geen geheim, geen betaald plan).
- **Synchroon:** eigen transcript met faster-whisper base.en (audio als numpy-array) op het releasebestand: alle 10 zinnen woord voor woord gelijk aan het script (whisper schrijft "0.1 to 0.3 millimeters"), begin van elke zin binnen 0,15 s van de geplande stem (GEZIEN, 23 nov). `synchroon.py` in CI (small.en) zegt 9 van 10: zin 8 ("Set that clearance") 0,41 s te vroeg. Dat is een meetfout van de klank-verfijning: hij legt het begin vóór het begin van de scène, terwijl montage.py de stem altijd 0,10 s ná de scène start; whisper zelf geeft 28,74 s tegen gepland 28,87 s. Daarom faalt de workflow-run op die ene stap; de film zelf is goed. Gemeld aan de hoofdchat.
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 1080x1920 en 14 beelden (1 tot 43,5 s). Eerste beeld: grote kop "Which gap fits?" boven de oranje en blauwe strips met hun getallen, geen productnaam, geen zwevende getallen. Strip-beelden in Blender nu rustig (geen bogen of graden van de figuur erover). Kan beter: in scène 8 valt de waarde 0.20 rechts net buiten de uitsnede (de stem zegt hem wel); de renders staan in een smal venster en mogen groter.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over de Fit test strip (RSS en `commercie/geplaatst.md` nagekeken 23 nov, GEZIEN).
- **Meten (recept v3 punt 4):** na 48 uur weergaven en "bleef kijken" van A tegen B, uitslag in `commercie/filmpjes/regisseur-log.md`.

## Keuring
(open)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
