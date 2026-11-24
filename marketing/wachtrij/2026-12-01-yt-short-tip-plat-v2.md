# Tip-reeks 4: Round model on one tiny point? Give it a flat bottom 🥚

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-7).
- nagekeken run 25 (GEZIEN, release regisseur-7, run 45430412786): lengte 43,7 s, geluid GOED (-16,6 dB), synchroon GOED 10 van 10 (0,18 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-7/tip-plat-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-4/tip-plat-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED (gemiddeld -16,4 dB, piek -1,4 dB), zelf gedraaid op het releasebestand 23 nov ±22:08 NL (GEZIEN); ook in CI
- lengte: 0:44,6, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN)
- tijd: voorstel 2026-12-01T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-7 (run 45263884196)
- vorige: 2026-12-01-yt-short-tip-plat.md

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

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Versie 2 (Regisseur run 6, 23 nov ±22:00 NL):** Geen stem- of AI-regel meer in de beschrijving (rood van de Roep-Keurder); bestand eindigt op -geluid.mp4; uitsnede bij STEP 1 verbeterd (het ei stond in de hoek, nu midden in beeld). Synchroon in CI: GOED, 10 van 10 zinnen binnen 0,3 s, grootste 0,2 s (GEZIEN, `synchroon-tip-plat.md` in release regisseur-7). Zelf bekeken (Read, GEZIEN): eerste beeld en 5 beelden rond STEP 1 en 2 van het releasebestand van regisseur-7, plus de tegel van 11 beelden van regisseur-5.
- **Hook (eerste 1,5 s):** "Does your round model touch the bed in just one tiny point?" vanaf beeld 1, kop "One tiny point?", beeld: het ei op zijn punt, zoom naar het punt (beweging vanaf beeld 1).
- **Elke stap staat echt in beeld:** Tab, 1, numpad 1, Alt Z, kader slepen en S Z 0 Enter allemaal met echte toetsen en de echte muis (lokaal GEZIEN: `d_voor_ortho` ORTHO, `d_xray` true, 193 punten gekozen met het kader, geen vangnet). Vlak na S Z 0: breedte 28,8 mm (`d_vlak_breed`), in de Short "about 29 mm". Na het plat maken zet het script het ei op het grid (geen stap in de Short).
- **Beweringen:** S Z 0 schaalt de gekozen punten op de Z-as naar nul rond hun midden: zo werkt schalen met een as in Blender (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/object/editing/transform/scale.html). "More rows, wider base": volgt uit het ei zelf (ring 4 heeft straal 14,5 mm, ring 5 groter), geen printbewering.
- **Model:** eigen ei uit `commercie/filmpjes/regisseur-4/tip_opname.py` (`ei()`). Geen modellicentie nodig.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Tijdelijke stem tot de ElevenLabs-opname er is (voorleestekst `commercie/filmpjes/regisseur-4/tip-plat-stem.txt`).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 10 van 10 zinnen binnen 0,3 s (GEZIEN).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld en 10 tot 12 beelden per Short. Hersteld na kijken: camera op de vaasrand (eerst de buitenkant, nu de rand van boven zodat voor en na het verschil te zien is), kaders op Offset en Even Thickness, hook van het ei dichterbij, uitsnede stap 1 met Edit Mode, Shorts verlengd van 36 en 37 s naar 44 s.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over wanddikte of een platte onderkant (GEZIEN, wachtrij en RSS 23 nov).
- **Releasebestand nagekeken (23 nov ±21:35 NL, GEZIEN):** run 45247413525 geslaagd; metingen in `film-tip.json` gelijk aan de lokale opname (menu echt geraakt, dikte 2,0 mm, breedte 82,0 mm voor en na, 193 punten, voet 28,8 mm, geen vangnet); synchroon in CI GOED (10 van 10); eerste beeld op 540 breed en 10 beelden van het releasebestand zelf bekeken.
- **Kan beter:** bij tip-dikte valt het kader op Offset iets te laag (raakt de regel Even Thickness); de tekst in het Properties-paneel is klein op een telefoon.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
