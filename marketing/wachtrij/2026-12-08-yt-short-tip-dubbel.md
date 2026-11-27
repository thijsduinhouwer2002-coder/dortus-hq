# Tip-reeks 11: Is your model secretly in two pieces? Fix it in Blender 🔧

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-13).
- nagekeken run 25 (GEZIEN, release regisseur-13, run 45430299425): lengte 42,4 s, geluid GOED (-16,6 dB), synchroon GOED 12 van 12 (0,18 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL; recept v3 Malikose: vraag aan de kijker als hook, één les die je kunt nadoen)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-13/tip-dubbel-geluid.mp4 (workflow regisseur-13, run 45324700553 op commit b30d281, opname uit run 45323240801; door de Regisseur nagekeken 24 nov run 13)
- stem_tekst: `commercie/filmpjes/regisseur-13/tip-dubbel-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: GOED, gemiddeld -16,7 dB, piek -1,4 dB (GEZIEN, zelf gedraaid op het releasebestand)
- lengte: 43,4 s, 1080 x 1920 (ffprobe, GEZIEN)
- synchroon: GOED, 12 van 12 zinnen binnen 0,3 s, grootste 0,253 s, gemiddeld 0,143 s (GEZIEN, synchroon-tip-dubbel.md in de release)
- beelden: 13 beelden zelf bekeken met Read, eerste beeld groot: blauwe vaas op het raster, kop "Two pieces?", geen getallen, de knik in het midden zichtbaar (GEZIEN). Bovenkant oranje en onderkant blauw na L, Merge-menu met By Distance onder de muis, hele vaas oranje na L opnieuw (GEZIEN). Kan beter: het eerste beeld mag dichterbij; bij TIP ("Check every model") staat de vaas nog in Edit Mode.
- metingen (film.json van de lokale proef, Blender 5.3.0, GEZIEN): vaas 45,9 x 45,9 x 60 mm; voor: 672 punten, 96 losse randen (boundary); L met de muis op de bovenkant kiest 289 van 578 vlakken; M > By Distance via het echte menu (`d_via_menu` true, geen vangnet): 48 punten weg, 0 losse randen; L opnieuw kiest 578 van 578 vlakken.
- tijd: voorstel 2026-12-08T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 13; opname in workflow regisseur-13 (Blender 5.3.0, xvfb, echte muis en toetsen, gedeelde hulpcode van Olaf)
- vorige:

## Titel
Is your model secretly in two pieces? Fix it in Blender 🔧

## Tekst
```
A model can look like one piece but be two loose parts with double points on the seam.
1. Press Tab, point at the top and press L. Only the top lights up.
2. Press A, then M and pick By Distance. Blender removed 48 double points here.
3. Press Alt A, then L again. Now the whole vase lights up: one part.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Is your model secretly in two pieces?" vanaf beeld 1, kop "Two pieces?", beeld: een blauwe vaas die langzaam draait (echte Blender), de naad in het midden zie je als een knik in het licht. Geen productnaam, geen getallen.
- **Merge by Distance:** Blender-handleiding: "Mesh ‣ Clean up ‣ Merge by Distance. Merges the selected vertices that are closer to each other than a certain distance." en Merge, "Shortcut: M", optie "By Distance" (DERDEN: https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/cleanup.html en https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/merge.html, met curl gelezen 24 nov).
- **Select Linked:** Blender-handleiding: "Selects all the geometry that's connected directly or indirectly to the current selection." (Ctrl L; DERDEN: https://docs.blender.org/manual/en/latest/modeling/meshes/selecting/linked.html, met curl gelezen 24 nov). L onder de muis zelf getoetst: kiest 289 van 578 vlakken, alleen de bovenkant (GEZIEN, film.json).
- **"48 double points" en "the edge is open":** de vaas is in het script gemaakt met ring 6 twee keer (48 punten per ring). Gemeten in film.json: 96 losse randen voor, 0 na; 48 punten weg na By Distance (GEZIEN). "Open" betekent hier: randen met maar één vlak (boundary), wat Blender ook onder Select Non Manifold vindt.
- **Wat het voor een print betekent:** niet geclaimd. Geen slicer genoemd, geen belofte dat de print beter wordt; alleen "Every printer is different: print a small test first."
- **Model:** eigen vaas van 60 mm hoog, in het script gemaakt. Geen modellicentie nodig.
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-dubbel-elevenlabs.mp3` in `commercie/filmpjes/regisseur-13/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over dubbele punten, losse delen of Merge by Distance (wachtrij, `commercie/geplaatst.md` en YouTube-RSS nagekeken 24 nov, GEZIEN). Verwant aan tip-gat (Non Manifold, gaten), maar ander probleem, andere knop en ander beeld.

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
