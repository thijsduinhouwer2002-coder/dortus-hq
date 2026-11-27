# Tip-reeks 1: Find holes in your model before you print 🔍

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-7).
- nagekeken run 25 (GEZIEN, release regisseur-7, run 45430412786): lengte 44,2 s, geluid GOED (-18,1 dB), synchroon whisper 8 van 10 (zin 9 en 10 niet herkend), met RMS nagemeten 10 van 10: stem zin 9 op 33,1 s bij scène 32,93, zin 10 op 38,1 bij 37,97. Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-7/tip-gat-geluid.mp4
- geluid_check: GOED (gemiddeld -18,1 dB, piek -1,2 dB), zelf gedraaid op het releasebestand 23 nov ±22:08 NL (GEZIEN); ook in CI
- lengte: 0:44,2, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN)
- tijd: voorstel 2026-11-27T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, workflow regisseur-7 (run 45263884196)
- vorige: 2026-11-27-yt-short-tip-gat.md

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

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Versie 2 (Regisseur run 6, 23 nov ±22:00 NL):** Stem nu ElevenLabs Max (opname hoofdchat, in zinnen geknipt met `stem/splits.py`); geen stem- of AI-regel meer in de beschrijving (rood van de Roep-Keurder); bestand eindigt op -geluid.mp4; uitsnede bij STEP 1 verbeterd (de pion stond half buiten beeld, nu midden in beeld). Synchroon in CI: GOED, 10 van 10 zinnen binnen 0,3 s, grootste 0,22 s (GEZIEN, `synchroon-tip-gat.md` in release regisseur-7). Zelf bekeken (Read, GEZIEN): eerste beeld en 5 beelden rond STEP 1 en 2 van het releasebestand van regisseur-7, plus de tegel van 12 beelden van regisseur-5 (zelfde montage op STEP 1 na).
- **Hook (eerste 1,5 s):** "Does your slicer say your model has holes?" gesproken vanaf beeld 1, kop "Got holes?", beeld: de pion met de oplichtende rand van het gat, camera rijdt erheen (beweging vanaf beeld 1, les van Iris 23 nov). Geen productnaam, geen zwevende getallen.
- **Elke stap staat echt in beeld (GEZIEN in de opname):** Tab naar Edit Mode, 2 (randen), Alt A, menu Select > Select All by Trait > Non Manifold met de echte muis (tesseract vond de menuregels, `a_via_menu: true` in film.json), 22 randen lichten op, F maakt een nieuw vlak, Shift Ctrl Alt M opnieuw: 0 randen (metingen `a_randen` 22 en `a_randen_na` 0 in `film-tip.json`). Geen vangnet nodig (log zonder "vangnet").
- **Sneltoets Shift Ctrl Alt M:** in de opname gebruikt bij de tweede check en zichtbaar in het menu van Blender 5.3 (GEZIEN).
- **Model:** eigen schaakpion, gemaakt in `commercie/filmpjes/regisseur-3/tip_opname.py` (draaiprofiel, 8 vlakken weg voor het gat). Geen modellicentie nodig, geen MakeHuman-figuur.
- **Stem:** ElevenLabs, stem "Max - Witty Commercial Actor" (Voice Library), model Eleven v4, opname van de hoofdchat in het account van Thijs (`commercie/filmpjes/regisseur-3/stem/tip-gat-elevenlabs.mp3`, besluit Thijs 23 nov). **Licentie, let op:** het gratis plan is volgens ElevenLabs "Personal use, attribution"; een commerciele licentie zonder naamsvermelding begint bij Starter (DERDEN: https://elevenlabs.io/pricing, gelezen 23 nov ±22:00 NL). Thijs wil geen stemregel in de beschrijving, dus voor plaatsen is Starter of een ja van Thijs op dit risico nodig (gemeld aan de hoofdchat). Valt dat weg: de Kokoro-versie kan met dezelfde workflow (zonder mp3).
- **Synchroon (lokaal, zelfde code):** synchroon2.py met faster-whisper small.en: GOED, 10 van 10 zinnen binnen 0,3 s, grootste verschil 0,187 s (GEZIEN). Transcript gelijk aan het script, op "dortus.com" na (whisper schrijft "dordist.com"; de stem zegt "dortus dot com slash Y T", het adres staat groot op de eindkaart).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540 breed en 20 beelden verspreid over de Short. Hersteld na het eerste kijken: venstertitel zei "Blender 5.3 with Click Joints Pro" (onwaar, geen add-on in beeld; nu "Blender 5.3"), de hook-kop liep over twee regels het venster in (nu "Got holes?"), het menu viel half buiten de uitsnede (nu verschoven), het laatste stuk liep door in het beeld van tip 2 (nu ingekort).
- **Kan beter:** bij "Tab, then 2" zie je de kop met Edit Mode niet goed; de muis staat dan in beeld maar de knoppen zijn klein.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen ging over gaten of Non Manifold (wachtrij en `commercie/geplaatst.md` nagekeken 23 nov, GEZIEN).
- **Releasebestand nagekeken (23 nov ±18:52 NL, GEZIEN):** run 45227517215 geslaagd; zelfde delen en metingen als de lokale opname (menu echt geraakt, randen 22 naar 0, hoogte 310 naar 217 mm); synchroon in CI GOED (10 van 10, grootste 0,18 s); eerste beeld op 540 breed en 6 beelden van het releasebestand zelf bekeken, gelijk aan de lokale bouw.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
