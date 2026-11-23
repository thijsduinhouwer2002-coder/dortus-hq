# Tip-reeks 1: Find holes in your model before you print 🔍

- status: wacht
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-3/tip-gat.mp4
- geluid_check: GOED (gemiddeld -16,4 dB, piek -0,7 dB), lokaal gebouwd met dezelfde code 23 nov ±18:20 NL (GEZIEN); op het releasebestand: `geluid_check.txt` in release regisseur-3
- lengte: 0:41,7, staand 1080x1920 (ffprobe op de lokale bouw, GEZIEN)
- tijd: voorstel 2026-11-27T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-3 (run 45227517215)
- vorige:

## Titel
Find holes in your model before you print 🔍

## Tekst
```
Does your slicer say your model has holes? Check it in Blender first:
1. Select your model, press Tab for Edit Mode, then 2 for edge select.
2. Press Alt A so nothing is selected.
3. Select > Select All by Trait > Non Manifold (or Shift Ctrl Alt M).
4. Every open edge lights up. Hover over the view and press F to fill the hole.
5. Run the check again: nothing lights up, so the mesh is closed.

Measured in Blender, not print tested by us yet.
Screen recording in Blender 5.3 (no add-on used). Voice: AI text to speech (Kokoro, Apache 2.0).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Does your slicer say your model has holes?" gesproken vanaf beeld 1, kop "Got holes?", beeld: de pion met de oplichtende rand van het gat, camera rijdt erheen (beweging vanaf beeld 1, les van Iris 23 nov). Geen productnaam, geen zwevende getallen.
- **Elke stap staat echt in beeld (GEZIEN in de opname):** Tab naar Edit Mode, 2 (randen), Alt A, menu Select > Select All by Trait > Non Manifold met de echte muis (tesseract vond de menuregels, `a_via_menu: true` in film.json), 22 randen lichten op, F maakt een nieuw vlak, Shift Ctrl Alt M opnieuw: 0 randen (metingen `a_randen` 22 en `a_randen_na` 0 in `film-tip.json`). Geen vangnet nodig (log zonder "vangnet").
- **Sneltoets Shift Ctrl Alt M:** in de opname gebruikt bij de tweede check en zichtbaar in het menu van Blender 5.3 (GEZIEN).
- **Model:** eigen schaakpion, gemaakt in `commercie/filmpjes/regisseur-3/tip_opname.py` (draaiprofiel, 8 vlakken weg voor het gat). Geen modellicentie nodig, geen MakeHuman-figuur.
- **Stem:** Kokoro-82M, stem af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Geen ElevenLabs (geen geheim, geen betaald plan).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 10 van 10 zinnen binnen 0,3 s, grootste verschil 0,187 s (GEZIEN). Transcript gelijk aan het script, op "dortus.com" na (whisper schrijft "dordist.com"; de stem zegt "dortus dot com slash Y T", het adres staat groot op de eindkaart).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540 breed en 20 beelden verspreid over de Short. Hersteld na het eerste kijken: venstertitel zei "Blender 5.3 with Click Joints Pro" (onwaar, geen add-on in beeld; nu "Blender 5.3"), de hook-kop liep over twee regels het venster in (nu "Got holes?"), het menu viel half buiten de uitsnede (nu verschoven), het laatste stuk liep door in het beeld van tip 2 (nu ingekort).
- **Kan beter:** bij "Tab, then 2" zie je de kop met Edit Mode niet goed; de muis staat dan in beeld maar de knoppen zijn klein.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over gaten of Non Manifold (wachtrij en `commercie/geplaatst.md` nagekeken 23 nov, GEZIEN).
- **Status wacht:** de release regisseur-3 wordt gemaakt door run 45227517215 (zelfde code, nieuwe opname in CI). Status gaat op open als ik het releasebestand heb nagekeken.

## Keuring
(open)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
