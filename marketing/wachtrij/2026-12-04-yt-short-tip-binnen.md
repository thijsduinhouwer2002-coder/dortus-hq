# Tip-reeks 7: Is your model inside out? Find it in 2 clicks 🔴

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-9).
- nagekeken run 25 (GEZIEN, release regisseur-9, run 45430299112): lengte 42,1 s, geluid GOED (-16,3 dB), synchroon GOED 10 van 10 (0,287 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets; recept v3 Malikose)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-9/tip-binnen-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-9/tip-binnen-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: GOED (gemiddeld -16,2 dB, piek -1,4 dB) op de lokale bouw 24 nov ±00:25 NL (GEZIEN); de workflow regisseur-9 draait dezelfde controle op het releasebestand en faalt bij FOUT
- lengte: 0:43,0, staand 1080x1920 (ffprobe lokale bouw, GEZIEN; de workflow faalt buiten 40 tot 60 s)
- tijd: voorstel 2026-12-04T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 8; opname en montage eerst lokaal (Blender 5.3.0, xvfb), releasebestand uit workflow regisseur-9 (neemt zelf opnieuw op met hetzelfde script)
- vorige:

## Titel
Is your model inside out? Find it in 2 clicks 🔴

## Tekst
```
Is your 3D model secretly inside out? Some faces can point inward without you noticing.
Check it in two clicks, fix it in one:
1. Open the Overlays menu (the small arrow next to the Overlays button) and tick Face Orientation. Red = you see the back of a face.
2. Press Tab for Edit Mode, then A to select everything.
3. Press Shift N (Mesh > Normals > Recalculate Outside).
No red left: every face points outward. Run this check before you export to your slicer.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your 3D model secretly inside out?" vanaf beeld 1, kop "Inside out?", beeld: een blauwgroene fles met een rode band (Face Orientation aan) die draait en inzoomt (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen.
- **Face Orientation kleurt de achterkant rood:** Blender-handleiding: "Face Orientation: Highlights the backside of faces in red. In general, if a face is shown in red on the outside of a mesh, it's most likely oriented incorrectly and needs to have its normal flipped." (DERDEN: https://docs.blender.org/manual/en/latest/editors/3dview/display/overlays.html, met curl gelezen 23 nov). In de Short als "The Blender manual says red on the outside most likely needs a flip."
- **Shift N draait de gekozen vlakken naar buiten:** Blender-handleiding: "Mesh ‣ Normals ‣ Recalculate Outside ... Shortcut: Shift-N ... Flips the orientation of the selected faces where necessary, making them all point outward" (DERDEN: https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html, met curl gelezen 23 nov).
- **"96 faces pointed inward, now zero":** zelf geteld in de opname (`binnen_tellen` in `tip_opname.py`: vlakken waarvan de normaal naar de as wijst): 96 van de 448 vlakken voor, 0 na Shift N (`g_binnen_voor: 96`, `g_binnen_na_toets: 0`, `g_binnen_na: 0` in `film.json`, GEZIEN). Geen vangnet nodig.
- **Elke stap echt in beeld (GEZIEN in de opname, `film.json`):** het pijltje naast de Overlays-knop met de echte muis aangeklikt (plek 1852, 80), "Face Orientation" in het menu gevonden met OCR en aangeklikt (`g_overlay_menu: true`), menu dicht met Escape, rood bleef; Tab en A met echte toetsen (`g_alles_toets: true`); Shift N met een echte toets (`g_binnen_na_toets: 0`). Log zonder één "vangnet"-regel.
- **Model:** eigen fles, gemaakt in `commercie/filmpjes/regisseur-9/tip_opname.py` (90 mm hoog, 448 vlakken; een band van de schouder is met opzet omgedraaid, zoals na een slordige Extrude of Mirror). Geen modellicentie nodig, geen MakeHuman-figuur.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-binnen-elevenlabs.mp3` in `commercie/filmpjes/regisseur-9/`, dan bouwt de workflow vanzelf opnieuw.
- **Synchroon:** GOED, 10 van 10 zinnen binnen 0,3 s, grootste 0,287 s (zin 3), gemiddeld 0,16 s (synchroon2.py met small.en op de lokale bouw, GEZIEN); ook in CI. Eerdere bouw had zin 8 op -0,93 s: meetfout (whisper plakte "Run" aan "zero", de klank begon echt op 29,0 s, zelf gemeten met RMS); opgelost door zin 7 en 8 anders te zeggen.
- **Zelf bekeken (Read, GEZIEN):** eerste beeld op 720 breed en twee tegels van 16 beelden (drie bouwen), plus ruwe opnamebeelden van het menu. Hersteld voor aanleveren: het Overlays-menu bleef open staan over de fles (nu Escape, twee keer opnieuw opgenomen), hook-beeld was een fles zonder rood (nu de rode band vanaf beeld 1, dichterbij, naar het kan-punt van Iris), STEP 1 begon met een lege hoek. Kan beter: de klik op het pijltje zelf valt net buiten de uitsnede (je ziet het menu verschijnen, niet de klik); het rode stuk komt in de hook en bij WHY twee keer voor.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over normalen, Face Orientation of Shift N (wachtrij, `commercie/geplaatst.md` en YouTube RSS nagekeken 23 nov ±23:50 NL, GEZIEN). Tip-dikte noemt normalen alleen als bijzin bij Solidify Offset.
- **Eerlijk:** de Short zegt niet dat een slicer hierdoor faalt (geen bron die we lazen); alleen wat de handleiding zegt en wat we zelf telden.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
