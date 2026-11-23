# Tip-reeks 4: Round model on one tiny point? Give it a flat bottom 🥚

- status: wacht (releasebestand nog niet nagekeken; de Regisseur zet hem op open)
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-4/tip-plat.mp4
- stem_tekst: `commercie/filmpjes/regisseur-4/tip-plat-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED lokaal op dezelfde code (GEZIEN); op het releasebestand: volgt
- lengte: 0:44,6 lokaal, staand 1080x1920 (GEZIEN); releasebestand: volgt
- tijd: voorstel 2026-12-01T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-4
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
- **Releasebestand:** volgt.

## Keuring
(open)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
