# Tip-reeks 8: Will your print fall over? Check it before you print ⚖️

- status: open (releasebestand nagekeken door de Regisseur, run 10, 24 nov)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Make your prints poseable: Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-10).
- nagekeken run 25 (GEZIEN, release regisseur-10, run 45430299421): lengte 42,8 s, geluid GOED (-16,6 dB), synchroon GOED 10 van 10 (0,23 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: tip (opdracht hoofdchat 23 nov 17:45 NL; recept v3 Malikose)
- product: click-joints-pro (tip zonder reclame in het midden, alleen de eindzin naar dortus.com/yt)
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-10/tip-val-geluid.mp4 (workflow regisseur-10, run 45294223456, nagekeken)
- stem_tekst: `commercie/filmpjes/regisseur-10/tip-val-stem.txt` (voor de ElevenLabs-stem Max van de hoofdchat)
- geluid_check: GOED, gemiddeld -16.4 dB, piek -1.3 dB (zelf gedraaid op het releasebestand, GEZIEN)
- lengte: 43,7 s, 1080 x 1920 (ffprobe, GEZIEN); synchroon 10 van 10 binnen 0,3 s, grootste 0,247 s (synchroon-tip-val.md in de release, GEZIEN); 17 beelden zelf bekeken: geen afgesneden menu, stip en voet leesbaar. Kan beter: bij WHY staat geen lijn van de stip naar de grond, je moet zelf zien dat de stip rechts van de voet valt.
- tijd: voorstel 2026-12-05T12:00:00+01:00 (de hoofdchat kiest)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 9; proefopname lokaal (Blender 5.3.0, xvfb), releasebestand uit workflow regisseur-10 (neemt zelf op met hetzelfde script)
- vorige:

## Titel
Will your print fall over? Check it before you print ⚖️

## Tekst
```
Tall or leaning model? Check if it will stand before you print.
1. Object > Set Origin > Origin to Center of Mass (Volume). The orange dot jumps to the balance point.
2. View > Viewpoint > Front. Is the dot outside the foot? Then it tips over.
3. Fix: Tab, 3 for face select, click the bottom face (View > Viewpoint > Bottom), press S, type 3, Enter.
4. Set the origin again: the dot is now inside the foot.
A wider foot or less lean keeps your print standing.

Every printer is different: print a small test first.
Screen recording in Blender 5.3 (no add-on used).
More Blender tips for 3D printing: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blendertips #shorts
```

## Eerste reactie
(leeg)

## Bronnen
- **Hook (eerste 1,5 s):** "Will your print fall over?" vanaf beeld 1, kop "Will it fall over?", beeld: een oranje scheve toren die draait en inzoomt. Geen productnaam, geen zwevende getallen.
- **Origin to Center of Mass:** Blender-handleiding: "Origin to Center of Mass: Moves the origin to the calculated center of mass of model (assuming the mesh has a uniform density)." (DERDEN: https://docs.blender.org/manual/en/latest/scene_layout/object/origin.html, met curl gelezen 24 nov). Een print met infill is niet overal even dicht: daarom "Every printer is different".
- **Stip buiten de voet = valt om:** Wikipedia, Support polygon: "its support polygon is a horizontal region over which the center of mass must lie to achieve static stability" (DERDEN: https://en.wikipedia.org/wiki/Support_polygon, met curl gelezen 24 nov). Let op: de bron zegt ook "necessary ... but not sufficient"; de Short zegt alleen dat een stip buiten de voet omvalt, niet dat een stip binnen de voet altijd blijft staan ("keeps your print standing" bij TIP is algemeen; de keurder mag dit strenger willen).
- **Gemeten in de lokale proef (GEZIEN, log 24 nov ±01:20 NL):** eigen scheve toren 80 mm, voet x van -12,0 tot 12,0 mm, zwaartepunt op x 19,9 mm (buiten); na S 3 op het ondervlak voet -36,0 tot 36,0 mm, zwaartepunt x 12,6 mm (binnen). De workflow meet opnieuw in `film.json` (`v_stip`, `v_na`).
- **Echte menu's:** Object > Set Origin > Origin to Center of Mass (Volume) en View > Viewpoint > Front/Bottom met de echte muis (OCR). In de proef met drempel 60 % vond OCR het vooraanzicht niet (vangnet via script); nu drempel 35 % (les run 8). Nakijken in het log van de workflow of er een vangnet-regel staat.
- **Model:** eigen toren, gemaakt in `commercie/filmpjes/regisseur-10/tip_opname.py`. Geen modellicentie nodig.
- **Oorsprong-stip groter:** Voorkeuren > Themes > 3D Viewport > Object Origin Size op 10 (gewone Blender-instelling, zodat de stip op een telefoon te zien is).
- **Stem:** tijdelijk Kokoro-82M, af_heart, Apache 2.0, commercieel gebruik toegestaan (DERDEN: https://huggingface.co/hexgrad/Kokoro-82M). ElevenLabs-opname (Max) gevraagd aan de hoofdchat: `tip-val-elevenlabs.mp3` in `commercie/filmpjes/regisseur-10/`.
- **Nieuw onderwerp:** geen Short van de laatste 14 dagen over zwaartepunt of omvallen (wachtrij en regisseur-log nagekeken 24 nov, GEZIEN).

## Keuring
(leeg tot de Keurder komt)

## Oranje-besluit
(alleen de hoofdchat, alleen bij oranje)

## Na plaatsen
(alleen de Maker)
