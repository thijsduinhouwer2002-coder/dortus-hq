# Tip-reeks 6: Bulging first layer? Fix it in Blender before you slice 🐘

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-8).
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL, voorbeeld Thijs: BlenderSecrets; recept v3 Malikose)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-8/tip-voet-geluid.mp4
- stem_tekst: `commercie/filmpjes/regisseur-8/tip-voet-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: GOED (gemiddeld -15,9 dB, piek -1,4 dB) op de lokale bouw 23 nov ±23:12 NL (GEZIEN); de workflow regisseur-8 draait dezelfde controle op het releasebestand en faalt bij FOUT
- lengte: 0:46,1, staand 1080x1920 (ffprobe lokale bouw, GEZIEN; de workflow faalt buiten 40 tot 60 s)
- tijd: voorstel 2026-12-03T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 7; opname en montage eerst lokaal (Blender 5.3.0, xvfb), releasebestand uit workflow regisseur-8 (neemt zelf opnieuw op met hetzelfde script)
- vorige:

## Titel
Stop the bulging first layer before you slice 🐘

## Tekst
```
Does the bottom edge of your print bulge out, like a little lip? That is elephant foot: the first layer gets squished wider than the rest.
Give the bottom edge a small slope in Blender before you slice:
1. Press Tab for Edit Mode, then 3 for face select.
2. View > Viewpoint > Bottom, then click the bottom face.
3. Press Ctrl B, type 0.5 and press Enter.
Now the bottom edge has a 0.5 mm slope all the way around. Print guides suggest 0.2 to 0.5 mm; the wider first layer fills that slope.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Does the bottom edge of your print bulge out, like a little lip?" vanaf beeld 1, kop "Bulging bottom edge?", beeld: het oranje bakje dat draait en inzoomt (beweging vanaf beeld 1). Geen productnaam, geen zwevende getallen.
- **Elephant foot, eerste laag breder:** Prusa: "When printing the first layer is squished against the heated print bed and as a result, it's usually a bit wider than it should be." (DERDEN: https://help.prusa3d.com/article/elephant-foot-compensation_114487, met curl gelezen 23 nov).
- **Schuine onderrand van 0,2 tot 0,5 mm:** QIDI: "A 0.2–0.5 mm chamfer around the model's base absorbs whatever expansion is left." (DERDEN: https://qidi3d.com/blogs/news/fix-3d-print-elephant-foot, met curl gelezen 23 nov). Ook Tom's Hardware noemt chamfers als oplossing (DERDEN: https://www.tomshardware.com/3d-printing/how-to-fix-elephant-foot-issues-in-3d-prints). In de tekst als "Print guides suggest", niet als eigen meting.
- **Bevel op een gekozen vlak schuint de randen van dat vlak af:** zelf gezien in de opname: na Ctrl B, 0.5, Enter is het ondervlak 59,0 x 39,0 mm (was 60,0 x 40,0) en begint de volle zijkant op 0,5 mm hoogte (`f_onder_na: [59.0, 39.0, 0.5]` in `film-tip.json`, GEZIEN).
- **Elke stap echt in beeld (GEZIEN in de opname, `film.json`):** Tab en 3 met echte toetsen (`f_mode: EDIT`, vlakselectie aan, geen vangnet); View > Viewpoint > Bottom met de echte muis (OCR vond `View`, `Viewpoint` en `Bottom`, beelden 305 tot 320 tonen de klik op Bottom en daarna "Bottom Orthographic"; de controle in het script keek te vroeg tijdens het draaien en deed daarna een onzichtbaar vangnet, in de nieuwe versie wacht hij 0,8 s); klik op het ondervlak met de muis (`f_klik_goed: true`); Ctrl B, 0.5, Enter getypt (`f_bevel_toets: true`, ondervlak 59,0 x 39,0 mm).
- **Model:** eigen bakje, gemaakt in `commercie/filmpjes/regisseur-8/tip_opname.py` (60 x 40 x 22 mm, wanden 3 mm). Geen modellicentie nodig, geen MakeHuman-figuur.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-voet-elevenlabs.mp3` in `commercie/filmpjes/regisseur-8/`, dan bouwt de workflow vanzelf opnieuw.
- **Synchroon:** GOED, 10 van 10 zinnen binnen 0,3 s, grootste 0,227 s (synchroon2.py met small.en op de lokale bouw, GEZIEN); ook in CI.
- **Zelf bekeken (Read, GEZIEN):** eerste beeld en STEP 2 op 540 breed, tegel van 16 beelden van de tweede bouw, plus 8 ruwe opnamebeelden per deel. Hersteld na de eerste bouw (niet aangeleverd): hook-kop liep over twee regels het venster in (nu "Bulging edge?"), en bij WHY, TIP, STEP 1 en STEP 3 viel het bakje rechts buiten de uitsnede. Kan beter: het eerste beeld is rustig (klein bakje dat inzoomt); het onderwerp "slope" is in een zijaanzicht amper te zien, daarom RESULT als close-up van de hoek in het onderaanzicht.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over elephant foot, chamfer of Bevel (wachtrij, `commercie/geplaatst.md` en YouTube RSS nagekeken 23 nov ±23:00 NL, GEZIEN).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
