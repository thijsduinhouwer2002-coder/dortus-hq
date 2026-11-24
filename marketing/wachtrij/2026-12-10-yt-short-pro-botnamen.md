# Pro-Short: Your rig, your bone names: printable joints in one click 🦴

- status: open
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-16).
- nagekeken run 25 (GEZIEN, release regisseur-16, run 45430298648): lengte 48,8 s, geluid GOED (-16,6 dB), synchroon GOED 13 van 13 (0,197 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- kanaal: yt-short
- soort: video
- soort_reeks: Pro (script week 48 nr. 6, hook 6B, `commercie/filmpjes/scripts/week-48-click-joints.md`, ja Daan; Pro-lijst nr. 2 in `scripts/volgorde-stem.md`)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-16/pro-botnamen-geluid.mp4 (nagekeken run 17)
- stem: Kokoro (Apache 2.0), Pro-reeks (`scripts/volgorde-stem.md`). Geen ElevenLabs-opname nodig.
- stem_tekst: `commercie/filmpjes/regisseur-16/pro-botnamen-stem.txt`
- figuur: eigen robot van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`), rig met Mixamo-botnamen uit `producten/blender-gewrichten/e2e/proef_mens.py` (maak_rig), geen licentie van derden
- eerste release (run 45338202840, 24 nov) nagekeken in run 16: 51,9 s, geluid GOED (-16,4 dB), synchroon 13 van 13 (grootste 0,23 s), 9 gewrichten, knie stop 119,96 "from rig", 10 bestanden (GEZIEN). Afgekeurd door mij: er stond geen enkele botnaam in beeld (overlay show_text stond uit, dat verbergt ook de namen; zelf getoetst in Blender 5.3.0, GEZIEN), de kop van de hook liep over het venster, de kop bij HONEST over het hoofd van de robot. Hersteld in `regisseur-16/opname.py` en `pro-botnamen.json`; workflow neemt opnieuw op. Volgende run: namen leesbaar in hook en zin 2, dan pas open.
- tweede release (run 45344790631, 24 nov) nagekeken in run 17 (GEZIEN): 51,9 s, geluid_check GOED (-16,4 dB, piek -1,4 dB), synchroon 13 van 13 (grootste 0,207 s), log `KORT namen in beeld: show_text aan`, 9 gewrichten, knie stop 119,96 "from rig", 7 rode vlakken, 10 bestanden, geen vangnet. 17 beelden bekeken, eerste beeld groot: robot met oranje botten en mixamorig-namen leesbaar, kop "Your bone names?" op één regel, geen zwevende getallen. Kan beter: in de hook overlappen een paar namen (RightShoulder/Spine2, RightUpLeg/LeftUpLeg); bij HONEST loopt de ondertitel over de romp (niet meer over het hoofd).
- tijd: voorstel 2026-12-10T17:00:00+01:00, niet in dezelfde week als pro-robot-delen als de hoofdchat dat te veel van hetzelfde beeld vindt (zelfde robot en deels dezelfde stappen; ander onderwerp: botnamen en de stop uit je eigen rig)
- doel: dortus.com/yt (over te typen)
- gemaakt_door: Regisseur run 15 (24 nov 2026)

## Titel
Your rig, your bone names: printable joints in one click 🦴 | Blender

## Tekst
```
Does your rig use different bone names? Click Joints Pro reads the common ones.
1. Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
2. Press Figure from rig: a joint at every shoulder, elbow, hip, knee and neck.
3. A bone with Limit Rotation? The hinge stops at that angle. No limit on one side? It takes the other side.

Every printer is different. Print a test joint first.
Click Joints Pro: dortus.com/yt
```

## Voice-over (zin voor zin, Engels)
1. Does your rig use different bone names?
2. This robot's rig uses Mixamo style bone names.
3. Click Joints Pro knows the bone names of the common rigs.
4. Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz.
5. Press Figure from rig, and it finds the elbows, knees, shoulders, hips and neck.
6. It cuts the robot into parts, with a joint at each one.
7. Does a bone have a Limit Rotation? Then the hinge stops at that angle.
8. No limit on one side? It takes the limit of the other side.
9. Drag Bend on the knee, and it stops at the angle from your rig.
10. Past the stop, red shows where parts would hit.
11. Exploded view pulls the parts apart.
12. Every printer is different. Print a test joint first.
13. Click Joints Pro, on Gumroad.

## Afwijkingen van het script (voor de keurder)
- Hook 6B, niet 6A, en geen "Mixamo" in de titel: Sanne's "Let op" (geen echte Mixamo-figuur getest, Adobe-account kunnen we niet gebruiken). In beeld staat onze eigen robot met een rig die Mixamo-botnamen heeft (mixamorig:LeftForeArm enzovoort); zin 2 zegt precies dat.
- Script-zin 7 ("when a joint does not fit, the list tells you why") is weggelaten: bij de robot past elk gewricht, dus er is geen beeld van. In de plaats: zin 9 (knie tot de stop uit de rig), zin 10 (rood) en zin 11 (uit elkaar).

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 3 en 4: "Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz." (`platformen/blender-2/gumroad-1.1.md` r. 41).
- Zin 2: rig van de robot = `maak_rig` in `producten/blender-gewrichten/e2e/proef_mens.py` (botnaam "mixamorig:" + naam); de opname logt de namen ("KORT namen aan").
- Zin 5 en 6: "a joint at every shoulder, elbow, hip, knee and neck" (gumroad-1.1.md r. 25).
- Zin 7 en 8: "If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored)." (gumroad-1.1.md r. 38). In de rig: Limit Rotation op linker knie 120 en elleboog 140, rechts niets; in de lijst van run 14 "Left knee · Hinge · 0–120° · from rig" en "Right knee · ... · mirror" (GEZIEN, film-pro.json regisseur-14).
- Zin 9 en 10: knie stop 119,96 "from rig", rood voorbij de stop (regisseur-14, GEZIEN; regisseur-16 nakijken).
- Geen prijs, geen "holds a pose". Opname met Pro 1.2.0 (tag click-joints-pro-v1.2.0, `platformen/blender/pro-1.2.0.md`).

## Licenties
- Stem: Kokoro-82M v1.0, stem af_heart (Apache-2.0, hexgrad/Kokoro-82M; kokoro-onnx MIT).
- Figuur en rig: van ons. Software in beeld: Blender 5.3.0 (GPL) met Click Joints Pro 1.2.0 (van ons).

## Keuring
- keurder: Iris, 24 nov 2026 ±16:50 UTC, `marketing/keuring/2026-11-24-yt-short-cc-fit-na-botnamen-enkels-speling-es-iris.md`
- beeld en plezier: akkoord **ja**, Moet geen
- Kan: ondertitel bij zin 7 en 8 niet over de onderste regels van de lijst.
