# Pro-Short: Turn your rigged figure into printable parts in one click 🔥

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-14).
- nagekeken: Regisseur run 15, 24 nov (release nagekeken, uitsneden hersteld, opnieuw gemonteerd)
- kanaal: yt-short
- soort: video
- soort_reeks: Pro (script week 49 nr. 1, `commercie/filmpjes/scripts/week-49-click-joints.md`, ja Daan; Pro-lijst nr. 1 in `scripts/volgorde-stem.md`)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-14/pro-robot-delen-geluid.mp4 (workflow regisseur-14, montage van run 15 met nieuwe uitsneden, run 45337604854 groen, sha256 96a7cad12b1d5080f5c9de9adfaf59091db14aeff58ec6ab40c20163b48b6b37; geluid GOED, synchroon 13 van 13, beelden gelijk aan de lokale bouw, GEZIEN)
- stem: Kokoro (Apache 2.0), want Pro-scripts krijgen Kokoro (`scripts/volgorde-stem.md`, ja Daan). Geen ElevenLabs-opname nodig.
- stem_tekst: `commercie/filmpjes/regisseur-14/pro-robot-delen-stem.txt`
- figuur: eigen robot-actiefiguur van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`, zelf gebouwd, geen licentie van derden)
- lengte: 47,4 s, 1080 x 1920 (ffprobe, GEZIEN)
- geluid_check: GOED, gemiddeld -16,5 dB, piek -1,3 dB (GEZIEN)
- synchroon: GOED, 13 van 13 zinnen binnen 0,3 s, grootste 0,18 s (synchroon2.py met faster-whisper, GEZIEN)
- beelden: 30 beelden zelf bekeken, eerste beeld groot: de robot op een sokkel, geen getallen, kop "One solid piece?" (GEZIEN). Opname gecontroleerd: 9 gewrichten (4 hinge, 5 ball), knie stop 119,96 graden "from rig", 7 rode vlakken voorbij de stop ("+12° past limit" in beeld), 10 bestanden geëxporteerd, geen vangnet-regels in het log (film-pro.json en opname-pro.log, GEZIEN).
- hersteld na de eerste montage (GEZIEN): zin 2, 4, 5 en 11 sneden het hoofd van de robot af; zin 5 en 6 lieten een leeg menu zien in plaats van de lijst (de lijst staat alleen in beeld 339 tot 358, in het deel knie); zin 7 te ver weg; zin 8 "+12° past limit" afgesneden; zin 9 liet het paneel zien in plaats van de robot uit elkaar. Nu: zin 5 de robot met alle gewrichtlabels, zin 6 de echte lijst (Hinge bij ellebogen en knieën, Ball bij de rest), zin 8 de rode lijn met "+12° past limit" boven de ondertitel, zin 9 de robot die uit elkaar gaat.
- kan nog beter: de kop "One solid piece?" raakt de bovenkant van het hoofd in beeld 1 (de render staat vast; een nieuwe render met meer ruimte boven vraagt een nieuwe opname)
- tijd: voorstel 2026-12-09T17:00:00+01:00, niet eerder dan 7 dec: de Short "One click: rig to 10 printable parts" (22 nov) heeft dezelfde kernbelofte. Verschil: de nieuwe robot, een vraag als hook (recept v3), voice-over, en de knie tot de stop met rood. De hoofdchat kiest.
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 14 (24 nov 2026)
- vorige: 2026-11-22-yt-short-rig-naar-10-delen.md (zelfde belofte, ander figuur, zonder stem)

## Titel
Turn your rigged figure into printable parts in one click 🔥 | Blender

## Tekst
```
Rigged your figure already? One button cuts it into printable parts.
1. Select your rigged figure and press Figure from rig.
2. Check the list: hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck.
3. Bend a knee to its stop, then Fit and export writes every part as its own file.

Every printer is different. Print a test joint first.
Click Joints Pro: dortus.com/yt
```

## Voice-over (zin voor zin, Engels)
1. Is your figure still one solid piece?
2. This robot has a rig, but it is one solid mesh.
3. Select it, and press one button: Figure from rig.
4. It cuts the robot into parts, each with its own joint.
5. It reads your rig and lists every joint it placed.
6. Elbows and knees get a hinge with an end stop, the rest a ball joint.
7. Click the lower leg and drag Bend to the stop.
8. Past the stop, red shows where parts would hit.
9. Exploded view pulls the parts apart.
10. Then step three, Fit and export, writes every part as its own file.
11. Exporting is in the free Click Joints too. The one-click figure is Pro.
12. Every printer is different. Print a test joint first.
13. Click Joints Pro, on Gumroad.

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 3, 4, 6: "press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint" (`platformen/blender-2/gumroad-1.1.md` r. 25).
- Zin 5 en 6: "Figure from rig reads the bones you made" (gumroad-1.1.md r. 28) en de lijst in het paneel (r. 39); in de opname "9 joints · 2 rig · 2 mirror · 5 preset" met Hinge bij ellebogen en knieën en Ball bij nek, schouders en heupen (GEZIEN). Geen aantal uitgesproken, zoals het script vraagt.
- Zin 7 en 8: "hinge with end stop and pose slider, red where parts hit past the stop" (gumroad-1.1.md r. 43); in beeld uit de opname: `knie_rood_vlakken` 7, `knie_pose_rood` 132 graden, label "+12° past limit" (film-pro.json, GEZIEN).
- Zin 9: klik op Exploded view (muis in film-pro.json, beeld 790) en de delen uit elkaar in beeld 805 tot 840 (GEZIEN).
- Zin 10 en 11: script week 49 nr. 1 (keuring Daan A1: exporteren zit in de gratis bestanden, Figure from rig in `betaald/`).
- Zin 13: kop van de winkeltekst (gumroad-1.1.md r. 19).
- Geen prijs, geen "holds a pose", geen slicer-naam. Opname met Pro 1.2.0 (tag click-joints-pro-v1.2.0, de versie in `platformen/blender/pro-1.2.0.md`; alles in beeld komt uit die versie, GEZIEN).

## Licenties
- Stem: Kokoro-82M v1.0, stem af_heart (Apache-2.0, hexgrad/Kokoro-82M; kokoro-onnx MIT).
- Figuur: eigen robot (studio-3), geen licentie van derden. Software in beeld: Blender 5.3.0 (GPL) met Click Joints Pro 1.2.0 (van ons).
