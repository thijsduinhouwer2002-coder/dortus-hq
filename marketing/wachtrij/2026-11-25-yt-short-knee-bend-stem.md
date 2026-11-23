# Stem-proef 1: How far does this knee bend? Check before you 3D print 🦵 | Blender

- status: open
- kanaal: yt-short
- soort: video
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/stem-proef-1/knee-bend-stem-staand.mp4
- geluid_check: GOED (gemiddeld -16,3 dB, piek -1,4 dB), 23 nov 2026 ±12:35 NL, in workflow run 45164459011 (`geluid_check.txt` in de release), GEZIEN
- lengte: 0:58,4, staand 1080x1920 (GEZIEN, `lengtes.txt` in de release)
- tijd: voorstel wo 25 nov 2026 17:00 NL, of later: de hoofdchat kiest (zie "Let op" onder Bronnen)
- doel: dortus.com/yt (over te typen; niet klikbaar in een Short). Als gerelateerde video: de nieuwste lange Pro-video.
- gemaakt_door: stem-agent (opdracht hoofdchat 23 nov 2026 ±11:45 NL)
- vorige:

## Titel
How far does this knee bend? Check before you 3D print 🦵 | Blender

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
- **Wat nieuw is:** de eerste Short met voice-over. Een Engelse AI-stem leest per stap één zin; het beeld wisselt op de zin (zoom naar het deel van het scherm waar de zin over gaat), in de stijl van het uitlegfilmpje van Thijs: Blender-scherm in een net venster met zachte schaduw op een lichte achtergrond met zachte kleurvlakken, label in een gekleurde pil, grote vette kop, de gesproken zin eronder. Eindbeeld: icoon, "Click Joints Pro", de samenvatting uit de Gumroad-tekst in één zin, dortus.com/yt. Machine en licenties: `commercie/filmpjes/stem/LEESMIJ.md`.
- **Stem:** Kokoro-82M v1.0, stem `af_heart`, Apache 2.0 voor model en stemmen (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Geen ElevenLabs gebruikt.
- **Synchroon (GEZIEN, `synchroon-staand.md` in de release):** faster-whisper small.en vond alle woorden van alle 15 zinnen terug in het transcript. Per zin het begin van de stem tegen de scènewissel in het beeld: 15 van 15 binnen 0,3 s, grootste verschil 0,18 s, gemiddeld 0,12 s. Alleen de ruwe woordtijden van whisper: één zin wijkt 0,33 s af (zin 9, whisper zet het woord "At" te vroeg); daarom verfijnt de meting tot het begin van de klank.
- **Geluid:** stem boven de zachte eigen ondergrond van `commercie/filmpjes/geluid/geluid.py` plus een zacht tikje bij elke muisklik; geen muziek van anderen.
- **Teksten tegen de bronnen:** "a joint at every shoulder, elbow, hip, knee and neck" en de samenvatting "Rig to printable figure: elbows and knees stop where your rig stops" komen uit `platformen/blender-2/gumroad-1.1.md`; "export ... 3MF" idem ("export to STL or 3MF"). Wat in beeld staat (opname van youtube-shorts-4, GEZIEN in 16 beelden van het releasebestand): lijst "9 joints · 2 rig · 2 mirror · 5 preset", "Left knee · Hinge · 0–120° · from rig", "Right knee ... mirror" (kader eromheen bij de zinnen over de knie), schuif op 120.00 bij "end stop", schuif op 132.00 met rode boog en "+12° past limit" bij "Go further", heupkogels uit elkaar bij "Exploded view", klik op 3MF en Export 3MF. Exploded view staat niet in gumroad-1.1.md, de knop zit wel in de add-on (keuring yt-shorts-3, A13). Geen "holds a pose", geen prijs, geen korting.
- **Beeld:** ruwe opname en renders uit release youtube-shorts-4 (Blender 5.3.0, Click Joints Pro 1.1.0, echte muis, niets met de hand gedraaid); eerste beeld render-2 (sprong, knieën 115°), "Print a test joint first" op render-4, eindbeeld render-1. De studio-release `studio-1` bestond nog niet (GEZIEN 23 nov ±11:50 NL: 404).
- **Let op voor de Keurder en de hoofdchat:**
  1. Zelfde onderwerp als de Short Ij-jc6t4WNo (knee-bend-v2, zonder stem). Daarom een andere titel. Voorstel: minstens twee dagen ertussen, en dan vergelijken: weergaven en kijkduur met stem tegen zonder stem. Dat zegt of de stem geld waard is.
  2. Recept v2 punt 4 zegt "geen AI-stem"; de voice-over is de nieuwe wens van Thijs (via de hoofdchat, 23 nov ±11:45). De Keurder keurt dus op de stijl van Thijs, niet op dat punt.
  3. `kanaal: yt-short` volgens LEESMIJ (de opdracht noemde `youtube-short`; de keuring van reeks 3, B6, rekende dat als afwijking).
  4. De stem in de beschrijving eerlijk gemeld ("Voice: AI text to speech").
  5. De onderste ±18% van het beeld is leeg gehouden voor titel en kanaalnaam van de Shorts-speler; printzin op ±80%.
- Liggende versie (1920x1080, zelfde script en stem, ook 15 van 15 binnen 0,3 s): `knee-bend-stem-liggend.mp4` in dezelfde release; geen concept, alleen ter vergelijking voor lange video's.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
