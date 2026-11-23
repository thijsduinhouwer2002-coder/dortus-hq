# Tip-reeks 4: Round model on one tiny point? Give it a flat bottom 🥚

- status: open
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-4/tip-plat.mp4
- stem_tekst: `commercie/filmpjes/regisseur-4/tip-plat-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED op het releasebestand (gemiddeld -16,5 en -16,4 dB, piek -1,4 dB), zelf gedraaid 23 nov ±21:35 NL (GEZIEN); ook in CI
- lengte: 0:44,6, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN; sha256 klopt met SHA256SUMS.txt)
- tijd: voorstel 2026-12-01T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-4 (run 45247413525)
- vorige:

## Titel
Round model on one tiny point? Give it a flat bottom 🥚

## Tekst
```
Does your round model touch the bed in just one tiny point? Give it a flat bottom in Blender before you slice:
1. Tab for Edit Mode, 1 for vertex select.
2. Numpad 1 for the front view, Alt Z to see through.
3. Drag a box around the bottom rows of points.
4. S, Z, 0, Enter: the points line up flat.
Here the egg now stands on a flat circle about 29 mm wide. More rows give a wider base, fewer rows keep more of the round shape.

Measured in Blender, not print tested by us yet.
Screen recording in Blender 5.3 (no add-on used). Voice: AI text to speech (Kokoro, Apache 2.0).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```
Komt er een ElevenLabs-stem, dan wordt de stemregel: "Voice: AI text to speech (ElevenLabs, elevenlabs.io)".

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Does your round model touch the bed in just one tiny point?" vanaf beeld 1, kop "One tiny point?", beeld: het ei op zijn punt, zoom naar het punt (beweging vanaf beeld 1).
- **Elke stap staat echt in beeld:** Tab, 1, numpad 1, Alt Z, kader slepen en S Z 0 Enter allemaal met echte toetsen en de echte muis (lokaal GEZIEN: `d_voor_ortho` ORTHO, `d_xray` true, 193 punten gekozen met het kader, geen vangnet). Vlak na S Z 0: breedte 28,8 mm (`d_vlak_breed`), in de Short "about 29 mm". Na het plat maken zet het script het ei op het grid (geen stap in de Short).
- **Beweringen:** S Z 0 schaalt de gekozen punten op de Z-as naar nul rond hun midden: zo werkt schalen met een as in Blender (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/object/editing/transform/scale.html). "More rows, wider base": volgt uit het ei zelf (ring 4 heeft straal 14,5 mm, ring 5 groter), geen printbewering.
- **Model:** eigen ei uit `commercie/filmpjes/regisseur-4/tip_opname.py` (`ei()`). Geen modellicentie nodig.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0 (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 10 van 10 zinnen binnen 0,3 s (GEZIEN).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld en 10 tot 12 beelden per Short. Hersteld na kijken: camera op de vaasrand (eerst de buitenkant, nu de rand van boven zodat voor en na het verschil te zien is), kaders op Offset en Even Thickness, hook van het ei dichterbij, uitsnede stap 1 met Edit Mode, Shorts verlengd van 36 en 37 s naar 44 s.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over wanddikte of een platte onderkant (GEZIEN, wachtrij en RSS 23 nov).
- **Releasebestand nagekeken (23 nov ±21:35 NL, GEZIEN):** run 45247413525 geslaagd; metingen in `film-tip.json` gelijk aan de lokale opname (menu echt geraakt, dikte 2,0 mm, breedte 82,0 mm voor en na, 193 punten, voet 28,8 mm, geen vangnet); synchroon in CI GOED (10 van 10); eerste beeld op 540 breed en 10 beelden van het releasebestand zelf bekeken.
- **Kan beter:** bij tip-dikte valt het kader op Offset iets te laag (raakt de regel Even Thickness); de tekst in het Properties-paneel is klein op een telefoon.

## Keuring
(open)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
