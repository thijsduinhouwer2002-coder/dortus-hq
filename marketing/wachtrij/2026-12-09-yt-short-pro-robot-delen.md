# Pro-Short: Turn your rigged figure into printable parts in one click 🔥

- status: wacht (workflow regisseur-14 neemt op; de Regisseur kijkt het releasebestand na en zet dan pas open)
- kanaal: yt-short
- soort: video
- soort_reeks: Pro (script week 49 nr. 1, `commercie/filmpjes/scripts/week-49-click-joints.md`, ja Daan; Pro-lijst nr. 1 in `scripts/volgorde-stem.md`)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-14/pro-robot-delen-geluid.mp4 (workflow regisseur-14, nog niet nagekeken)
- stem: Kokoro (Apache 2.0), want Pro-scripts krijgen Kokoro (`scripts/volgorde-stem.md`, ja Daan). Geen ElevenLabs-opname nodig.
- stem_tekst: `commercie/filmpjes/regisseur-14/pro-robot-delen-stem.txt`
- figuur: eigen robot-actiefiguur van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`, zelf gebouwd, geen licentie van derden)
- geluid_check, lengte, synchroon, beelden: nog niet (volgende run)
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

Measured in Blender, not print tested by us yet. Print a test joint first.
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
12. Measured in Blender, not print tested by us yet. Print a test joint first.
13. Click Joints Pro. Elbows and knees stop where your rig stops.

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 3, 4, 6: "press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint" (`platformen/blender-2/gumroad-1.1.md` r. 25).
- Zin 5: "Figure from rig reads the bones you made" (gumroad-1.1.md r. 28) en de lijst in het paneel (r. 39). Geen aantal gewrichten uitgesproken: de robot gaf 8 of 9 (studio LEESMIJ punt 7), zoals het script vraagt.
- Zin 7 en 8: "hinge with end stop and pose slider, red where parts hit past the stop" (gumroad-1.1.md r. 43); in beeld uit de opname (`knie_rood_vlakken` in film.json, volgende run nakijken).
- Zin 9: knop Exploded view in het paneel (opname, `exploded_ocr`).
- Zin 10 en 11: script week 49 nr. 1 (keuring Daan A1: exporteren zit in de gratis bestanden, Figure from rig in `betaald/`).
- Zin 13: kop van de winkeltekst (gumroad-1.1.md r. 19).
- Geen prijs, geen "holds a pose", geen slicer-naam. Opname met Pro 1.2.0 (tag click-joints-pro-v1.2.0, zelfde knoppen als 1.2.3 voor dit stuk: GOK, volgende run vergelijken met `platformen/blender/pro-1.2.0.md`).
