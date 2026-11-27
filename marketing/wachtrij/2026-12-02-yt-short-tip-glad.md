# Tip-reeks 5: Smooth in Blender, blocky in your print? ✨

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-7).
- nagekeken run 25 (GEZIEN, release regisseur-7, run 45430412786): lengte 50,1 s, geluid GOED (-16,9 dB), synchroon GOED 12 van 12 (0,187 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-7/tip-glad-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-6/tip-glad-stem.txt` (voor de ElevenLabs-stem van de hoofdchat)
- geluid_check: GOED (gemiddeld -16,6 dB, piek -1,4 dB), zelf gedraaid op het releasebestand 23 nov ±22:08 NL (GEZIEN); ook in CI
- lengte: 0:51,0, staand 1080x1920 (ffprobe op het releasebestand, GEZIEN)
- tijd: voorstel 2026-12-02T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur, opname workflow regisseur-6 (run 45253552937), montage workflow regisseur-7 (run 45263884196)
- vorige:

## Titel
Smooth in Blender, blocky in your print? Fix it ✨

## Tekst
```
Does your model look smooth in Blender, but blocky when you print it? Shade Smooth only changes how Blender draws it. Your slicer gets the flat faces.
1. Right click > Shade Flat to see what you will really print.
2. Modifier properties > Add Modifier > Generate > Subdivision Surface.
3. Set Levels Viewport to 2.
4. Hover over the modifier and press Ctrl A to apply it.
Our test ball went from 96 to 1,440 real faces and looks round even with flat shading.
It gets a little smaller, so check the size before you export.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Does your model look smooth in Blender, but blocky when you print it?" vanaf beeld 1, kop "Blocky print?", beeld: de groene bal die inzoomt (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen (eerste beeld zelf bekeken op 540 breed, GEZIEN).
- **Shade Smooth is alleen een look:** Blender-handleiding: "Activating the smoothing features does not actually modify the object's geometry; it changes the way the shading is calculated" (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/object/editing/shading.html, met curl gelezen 23 nov).
- **Elke stap echt in beeld (GEZIEN in de opname, `film-tip.json` release regisseur-6):** rechtsklik > Shade Flat via het echte menu (`e_flat_via_menu: true`), Add Modifier > Generate > Subdivision Surface met de echte muis (`e_via_menu: true`), Levels Viewport 2 in de UI (`e_levels_ui: 2`), Ctrl A met de muis boven de modifier (`e_apply_toets: true`).
- **96 naar 1.440 vlakken:** gemeten in de opname (`e_vlakken_voor: 96`, `e_vlakken_na: 1440`, GEZIEN) en klopt met de rekensom 72 vierkanten x 16 + 24 driehoeken x 12 = 1.440.
- **"It gets a little smaller":** zelf gemeten in Blender 5.3.0 met dezelfde bal uit `tip_opname.py`: 40,0 x 40,0 x 40,0 mm voor, 37,2 x 37,2 x 39,2 mm na Subdivision Surface niveau 2 toepassen (GEZIEN, 23 nov ±21:55 NL, achtergrondrun). Niet als getal in het filmpje, wel als reden voor "check the size".
- **Model:** eigen bal, gemaakt in `commercie/filmpjes/regisseur-6/tip_opname.py` (draaiprofiel, 12 rondom, 8 stappen). Geen modellicentie nodig, geen MakeHuman-figuur.
- **Stem:** Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). Tijdelijke stem tot de ElevenLabs-opname er is.
- **Synchroon in CI:** GOED, 12 van 12 zinnen binnen 0,3 s, grootste 0,187 s (GEZIEN, `synchroon-tip-glad.md` in release regisseur-7).
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 540 breed, tegel van 12 beelden van versie regisseur-6, en 8 beelden van het releasebestand van regisseur-7 (hook, Shade Flat met menu, 96 vlakken, Add Modifier, 1.440 vlakken). Kan beter: bij STEP 2 is het paneel vooral leeg en staat "Add Modifier" rechts bovenaan; in de volgende opname het paneel smaller maken.
- **Hersteld na eigen controle van versie regisseur-6 (niet aangeleverd):** bij STEP 1 viel het rechtsklikmenu half buiten de uitsnede, en STEP 2 begon met een leeg donker vlak waarin "Add Modifier" klein bovenaan stond. Nieuwe uitsneden in `commercie/filmpjes/regisseur-7/tip-glad.json`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over Shade Smooth of Subdivision Surface (wachtrij en `commercie/geplaatst.md` nagekeken met grep 23 nov, GEZIEN).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
