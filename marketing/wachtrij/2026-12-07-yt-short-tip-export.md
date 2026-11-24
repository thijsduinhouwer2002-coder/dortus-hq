# Tip-reeks 10: Tiny print in your slicer? Fix it in Blender 🔍

- status: wacht (de Regisseur zet hem op open zodra hij het releasebestand van regisseur-12 zelf heeft nagekeken: synchroon, geluid_check, beelden, vangnet-regels, metingen van beide STL-bestanden)
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL; recept v3 Malikose); onderwerp nr. 1 van de gratis tips in `commercie/filmpjes/scripts/volgorde-stem.md` (week 50 nr. 4), hier als Blender-tip zonder add-on
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-12/tip-export-geluid.mp4 (workflow regisseur-12, nog niet nagekeken)
- stem_tekst: `commercie/filmpjes/regisseur-12/tip-export-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: nog niet (de workflow draait hem op het releasebestand en faalt bij FOUT)
- lengte: nog niet gemeten (de workflow faalt buiten 40 tot 60 s)
- tijd: voorstel 2026-12-07T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 11; opname in workflow regisseur-12 (Blender 5.3.0, xvfb, echte muis)
- vorige:

## Titel
Tiny print in your slicer? Fix it in Blender 🔍

## Tekst
```
Your model looks right in Blender but comes out tiny in the slicer? An STL file has no unit.
1. Press N: Blender shows 60 mm, but with Unit Scale 1 the file gets 0.06.
2. Most slicers read that number as millimetres: 0.06 mm.
3. File > Export > STL, set Scale to 1000, then Export STL.
4. Now the file says 60 mm, the same as in Blender.

Measured in Blender, not print tested by us yet.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your print tiny in the slicer?" vanaf beeld 1, kop "Tiny in your slicer?", beeld: een oranje label met afgeronde hoeken en een gat dat langzaam draait (echte Blender). Geen productnaam, geen zwevende getallen.
- **Scale bij STL-export:** Blender-handleiding, STL export: "Scale: Value by which to scale the exported objects in relation to the world's origin." en "Scene Unit: Apply current scene's unit (as defined by unit scale) to exported data." (DERDEN: https://docs.blender.org/manual/en/latest/files/import_export/stl.html, met curl gelezen 24 nov).
- **Unit Scale verandert alleen wat je ziet:** Blender-handleiding Scene Properties: "This only influences the values displayed in the user interface and not how things behave internally." (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/scene/properties.html, met curl gelezen 24 nov).
- **"inside the file it is 0.06" en "now the file says 60 mm":** het script exporteert eerst met Scale 1 (onzichtbaar) en leest het STL-bestand na (`j_stl_zonder`), daarna via het echte venster met Scale 1000 (`j_stl_met`), in `film.json`. Moet 0,06 en 60 zijn; nog na te kijken in de release. Klopt het niet, dan gaan zin 3 en 7 eruit.
- **"Most slicers read that as mm":** STL bewaart geen eenheid (algemene kennis, ook in het script van Sanne week 50 nr. 4, gekeurd door Daan); "most" omdat we niet elke slicer zelf zagen (GOK voor de uitzonderingen). Geen slicer-naam genoemd of getoond.
- **Echte menu's:** File > Export > STL met de echte muis (OCR, drempel 35 %), Scale in het venster met dubbelklik en 1000 getypt, knop Export STL geklikt. Nakijken in het log of er een vangnet-regel staat (`j_via_venster`).
- **Model:** eigen label van 60 x 30 x 4 mm, in het script gemaakt (kubus, afgeronde hoeken, gat). Geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-export-elevenlabs.mp3` in `commercie/filmpjes/regisseur-12/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over exportschaal of eenheden (wachtrij en regisseur-log nagekeken 24 nov, GEZIEN; tip-maat gaat over het printbed, niet over de export).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
