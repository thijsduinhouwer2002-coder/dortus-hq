# Tip-reeks 9: Put your name on a 3D print with Blender ✍️

- status: open (run 12: nieuwe opname nagekeken, Object > Convert > Mesh nu echt in beeld, `t_conv_menu` true, GEZIEN)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-11).
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL; recept v3 Malikose)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-11/tip-tekst-geluid.mp4 (workflow regisseur-11, run 45308576710 van 24 nov 01:55 UTC, door de Regisseur nagekeken 24 nov run 12)
- stem_tekst: `commercie/filmpjes/regisseur-11/tip-tekst-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: GOED, gemiddeld -16,7 dB, piek -1,3 dB (GEZIEN, geluid_check.txt in de release)
- lengte: 43,8 s (ffprobe, GEZIEN)
- synchroon: GOED, 11 van 11 zinnen binnen 0,3 s, grootste 0,293 s (zin 10), gemiddeld 0,153 s (GEZIEN, synchroon-tip-tekst.md in de release van run 45308576710)
- beelden: 16 beelden zelf bekeken met Read, eerste beeld groot: dikke oranje letters HELLO op het Blender-raster, kop "Your name in 3D?", geen zwevende getallen (GEZIEN). Object-menu open met Convert en het submenu Mesh, Point Cloud, Grease Pencil (GEZIEN). Kan beter: de ondertitel "Convert, Mesh." ligt even over het woord Mesh in het submenu.
- tijd: voorstel 2026-12-06T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 10; opname in workflow regisseur-11 (Blender 5.3.0, xvfb, echte muis)
- vorige:

## Titel
Put your name on a 3D print with Blender ✍️

## Tekst
```
Want your name or a word on a 3D print? Text in Blender starts flat, so there is nothing to print. Make it solid:
1. Add > Text. It starts 1 mm tall: press S, type 20, Enter.
2. Tab, delete the word, type your name, Tab.
3. Object > Convert > Mesh.
4. Tab, A, E, type 3, Enter: every letter is now 3 mm thick. Press N to check the Dimensions.
5. File > Export > STL and open it in your slicer.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Want your name on a 3D print?" vanaf beeld 1, kop "Your name in 3D?", beeld: de dikke oranje letters HELLO die draaien (eind van de opname, echte Blender). Geen productnaam, geen zwevende getallen.
- **Object > Convert > Mesh:** Blender-handleiding: "Converts the selected curve, metaball, surface, or text object to a mesh object." (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/object/editing/convert.html, met curl gelezen 24 nov).
- **Tekst bewerken met Tab:** Blender-handleiding Text Editing (DERDEN: https://docs.blender.org/manual/en/latest/modeling/texts/editing.html, met curl gelezen 24 nov).
- **Export als STL:** Blender-handleiding, File > Import/Export > Stl (DERDEN: https://docs.blender.org/manual/en/latest/files/import_export/stl.html, met curl gelezen 24 nov).
- **"Flat, zero thickness, nothing to print":** een tekstobject zonder Extrude heeft alleen een vlak; in de opname van opzij gezien (deel t_plat) en gemeten in `film.json` (`t_maat_hello` = 58,2 x 14,0 x 0,0 mm, GEZIEN).
- **1 mm hoog en 3 mm dik:** de scène staat op 1 eenheid = 1 mm (Units: Millimeters, Unit Scale 0.001); nieuwe tekst heeft grootte 1. Gemeten in `film.json`: `t_maat_begin` 1,9 x 0,7 x 0 mm (hoogte van een hoofdletter is minder dan de lettergrootte 1), `t_maat_20` 38,0 x 13,8 x 0, `t_maat_dik` 58,2 x 14,0 x 3,0 mm (GEZIEN). "Only 1 mm tall" slaat op de lettergrootte 1 mm; de letter zelf meet 0,7 mm.
- **Echte menu's:** Add > Text en Object > Convert > Mesh met de echte muis (OCR, drempel 35 %), toetsen echt via xdotool. In film.json: `t_add_menu` true en `t_conv_menu` true, dus geen vangnet bij de menu's (GEZIEN).
- **Model:** de tekst HELLO in het standaardlettertype dat met Blender meekomt (het ingebouwde lettertype van Blender, meegeleverd met Blender, GPL-programma; alleen in beeld, geen bestand dat we verkopen). Verder geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-tekst-elevenlabs.mp3` in `commercie/filmpjes/regisseur-11/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over tekst op een model (wachtrij, geplaatst.md en regisseur-log nagekeken 24 nov, GEZIEN).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
