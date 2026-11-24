# Pro-Short: Add ankle joints to your 3D printed figure 🔥

- status: wacht (laten vallen tot Pro enkels zet; Regisseur run 17, 24 nov: Pro zet op de robot geen enkels; de video zou iets beloven wat niet gebeurt)
- reden (GEZIEN, release regisseur-17, run 45345175105, opname-pro.log regel 24): de klik op "More bones (ankles too)" werkte (knop op 1531/323), maar Pro meldt `9 joints · 2 rig · 2 mirror · 5 preset. Skipped: Left ankle (Tight: cheek too stiff to click. Try a thicker spot); Right ankle (idem)`. Meting `enkels` = []. Gemeld bij Olaf. Opnieuw proberen als een figuur met dikkere enkels (of een fix in Pro) de enkels wel in de lijst krijgt.
- kanaal: yt-short
- soort: video
- soort_reeks: Pro (script week 49 nr. 5, hook 5A, `commercie/filmpjes/scripts/week-49-click-joints.md`, ja Daan; Pro-lijst nr. 13 in `scripts/volgorde-stem.md`)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-17/pro-enkels-geluid.mp4 (nog niet nagekeken)
- stem: Kokoro (Apache 2.0), Pro-reeks (`scripts/volgorde-stem.md`). Geen ElevenLabs-opname nodig.
- stem_tekst: `commercie/filmpjes/regisseur-17/pro-enkels-stem.txt`
- figuur: eigen robot van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`), rig uit `producten/blender-gewrichten/e2e/proef_mens.py` (maak_rig, met voetbotten), geen licentie van derden
- geluid_check, lengte, synchroon, beelden: nog niet (volgende run). Lengte GOK ±47 s (130 woorden; pro-botnamen 144 woorden gaf 51,9 s, GEZIEN).
- tijd: voorstel 2026-12-11T17:00:00+01:00, niet op dezelfde dag als pro-botnamen (zelfde robot)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 16 (24 nov 2026)

## Waarom deze en niet Pro-lijst nr. 3
Nr. 3 (figuur met AI gemaakt) vraagt een figuur waarvan de benen tegen elkaar zitten en een eerlijke AI-bron; die opname hebben we niet. Nr. 5 past op de bewezen robot-opname (regisseur-14) met één andere klik, dus kan nu. Nr. 3 blijft de volgende als Olaf een figuur uit `proeven/studio-figuren-2026-11-23/` vrijgeeft.

## Titel
Add ankle joints to your 3D printed figure 🔥 | Blender

## Tekst
```
Does your figure stand on stiff feet?
1. Figure from rig gives shoulders, elbows, hips, knees and the neck.
2. Press More bones (ankles too), right under it, and the ankles join the list.
3. N panel > Click Joints > Figure joints. Select the rigged mesh first.
4. No rig? Use the Ankle preset: put the 3D cursor on the ankle.

Measured in Blender, not print tested by us yet. Print a test joint first.
Click Joints Pro: dortus.com/yt
```

## Voice-over (zin voor zin, Engels)
1. Does your figure stand on stiff feet?
2. Figure from rig gives shoulders, elbows, hips, knees and the neck by default.
3. For the ankles too, press More bones, right under Figure from rig.
4. It cuts the robot into parts, with a joint at each one.
5. Select the rigged mesh first, then press it, and the ankles join the list.
6. You find it in the N panel, under Click Joints, in Figure joints.
7. No rig? There is an Ankle preset: put the 3D cursor on the ankle.
8. Drag Bend on the knee, and it stops at the angle from your rig.
9. Exploded view pulls the parts apart.
10. Measured in Blender, not print tested by us yet. Print a test joint first.
11. Click Joints Pro. Elbows and knees stop where your rig stops.

## Afwijkingen van het script (voor de keurder)
- Hook 5A, niet 5B.
- Zin 4, 8 en 9 zijn erbij (uit de gekeurde scripts van pro-robot-delen en pro-botnamen), anders is het filmpje korter dan 40 s.
- Het soort gewricht en de hoek van de enkel worden niet uitgesproken (Sanne: staat niet in de bronnen); het beeld toont de lijst. Toont de lijst geen enkel ("enkels" leeg in film-pro.json), dan gaat deze Short niet door.
- Zin 7 (preset): in beeld de knop Ankle in het paneel, niet een klik erop (de opname doet geen preset).

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 2 en 3: "a joint at every shoulder, elbow, hip, knee and neck" en "Ankles via More bones" (`platformen/blender-2/gumroad-1.1.md` r. 25 en 37). Knop "More bones (ankles too)" onder Figure from rig in Pro 1.2.0: GEZIEN, ruwe opname regisseur-16 beeld 100.
- Zin 5 en 6: "N panel › Click Joints › Figure joints › Figure from rig (or More bones (ankles too)). Select the rigged mesh first." (`platformen/blender/superhive/where-to-find-it.md`, gekeurde winkeltekst).
- Zin 7: "Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle ... Place the 3D cursor and click the body part." (gumroad-1.1.md r. 42).
- Zin 8: "If a bone has a Limit Rotation constraint, the hinge stops at that angle" (gumroad-1.1.md r. 38); knie stop 119,96 "from rig" (GEZIEN, film-pro.json regisseur-16).
- Geen prijs, geen "holds a pose". Opname met Pro 1.2.0 (tag click-joints-pro-v1.2.0, `platformen/blender/pro-1.2.0.md`).

## Licenties
- Stem: Kokoro-82M v1.0, stem af_heart (Apache-2.0, hexgrad/Kokoro-82M; kokoro-onnx MIT).
- Figuur en rig: van ons. Software in beeld: Blender 5.3.0 (GPL) met Click Joints Pro 1.2.0 (van ons).
