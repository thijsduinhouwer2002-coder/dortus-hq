# Pro-Short: Add ankle joints to your 3D printed figure 🔥

- status: vervallen (hoofdchat 27 nov 16:20, Thijs koos "1": marketing weer aan alleen voor nieuw gekeurd werk; oud werk gaat niet meer uit)
- bijgewerkt: Regisseur run 25 (24 nov 2026): eerlijkheidszin vervangen door "Every printer is different" (besluit Thijs 24 nov 15:32) en slotzin in beeld en stem "Click Joints Pro, on Gumroad." (opdracht hoofdchat 24 nov 16:05). Alleen opnieuw gemonteerd uit dezelfde ruwe opname (workflow regisseur-17).
- nagekeken run 25 (GEZIEN, release regisseur-17, run 45430298655): lengte 41,6 s, geluid GOED (-16,5 dB), synchroon GOED 11 van 11 (0,18 s). Eerlijkheidszin en slotzin staan in beeld en stem.
- opname (GEZIEN, release regisseur-17, runs 45397504004 en 45400996121, opname-pro.log): klik op More bones (1531, 323) echt; Pro meldt 11 gewrichten, waarvan `Left ankle · Hinge · 0–90° · preset` en `Right ankle · Hinge · 0–90° · preset`; statusbalk "11 joints · 2 rig · 2 mirror · 7 preset." (eerdere poging run 17 met 1.2.0: enkels overgeslagen).
- kanaal: youtube-short
- soort: video
- soort_reeks: Pro (script week 49 nr. 5, hook 5A, `commercie/filmpjes/scripts/week-49-click-joints.md`, ja Daan; Pro-lijst nr. 13 in `scripts/volgorde-stem.md`)
- product: click-joints-pro
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-17/pro-enkels-geluid.mp4 (sha256 in SHA256SUMS.txt van de release)
- saleversie: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/regisseur-17/pro-enkels-sale-geluid.mp4, slotzin en eindkaart "Click Joints Pro, 25% off this week, on Gumroad". Alleen do 26 nov avond tot en met di 1 dec en alleen als CYBER25 aanstaat.
- herbouw Regisseur run 27 (24 nov ±19:20 NL): eerste beeld nu studio-render van de robot met de blauwe enkelringen, ingezoomd op benen en voeten (render-3) in plaats van het grijze Blender-venster (opdracht hoofdchat 18:05: eerste beeld spectaculair). Alleen montage, zelfde opname en tekst.
- stem: nu Kokoro (Apache 2.0) als proef. **Niet plaatsen zonder Max** (hoofdchat 24 nov 18:05); opname staat op `commercie/filmpjes/stem/opnames-vanavond.md`, de workflow bouwt dan beide versies opnieuw.
- stem_tekst: `commercie/filmpjes/regisseur-17/pro-enkels-stem.txt`
- figuur: eigen robot van studio-3 (`commercie/filmpjes/studio/figuur_robot.py`), rig uit `producten/blender-gewrichten/e2e/proef_mens.py` (maak_rig, met voetbotten), geen licentie van derden
- lengte 44,7 s (ffprobe, GEZIEN); geluid_check GOED (-16,3 dB, piek -1,4 dB); synchroon GOED 11 van 11, grootste 0,22 s (`synchroon-pro-enkels.md`); 17 beelden zelf bekeken, eerste beeld groot: hele robot met rig, kop en voeten in beeld, vraag in de kop.
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

Every printer is different. Print a test joint first.
Click Joints Pro: dortus.com/yt
```

## Voice-over (zin voor zin, Engels)
1. Does your figure stand on stiff feet?
2. Figure from rig gives shoulders, elbows, hips, knees and the neck by default.
3. For the ankles too, press More bones, right under Figure from rig.
4. It cuts the robot into parts, with a joint at each one.
5. Select the rigged mesh first, then press it: the ankles get a joint too.
6. You find it in the N panel, under Click Joints, in Figure joints.
7. No rig? There is an Ankle preset: put the 3D cursor on the ankle.
8. Drag Bend on the knee, and it stops at the angle from your rig.
9. Exploded view pulls the parts apart.
10. Every printer is different. Print a test joint first.
11. Click Joints Pro, on Gumroad.

## Afwijkingen van het script (voor de keurder)
- Zin 5 toont de voeten van dichtbij na de snede (groene ring van de add-on bij de enkel), niet de lijst: in 1.2.6 staat de lijst van gewrichten niet open in het paneel, alleen kort de statusbalk "11 joints". Kan voor een volgende versie: de enkel zelf laten buigen in plaats van de knie (zin 8 toont de knie; de Bend-schuif staat niet in beeld, de opname buigt via het vangnet, log `vangnet knie`).
- Hook 5A, niet 5B.
- Zin 4, 8 en 9 zijn erbij (uit de gekeurde scripts van pro-robot-delen en pro-botnamen), anders is het filmpje korter dan 40 s.
- Het soort gewricht en de hoek van de enkel worden niet uitgesproken (Sanne: staat niet in de bronnen); het beeld toont de lijst. Toont de lijst geen enkel ("enkels" leeg in film-pro.json), dan gaat deze Short niet door.
- Zin 7 (preset): in beeld de knop Ankle in het paneel, niet een klik erop (de opname doet geen preset).

## Bronnen (alleen voor de keurder, niet voor kijkers)
- Zin 2 en 3: "a joint at every shoulder, elbow, hip, knee and neck" en "Ankles via More bones" (`platformen/blender-2/gumroad-1.1.md` r. 25 en 37). Knop "More bones (ankles too)" onder Figure from rig in Pro 1.2.0: GEZIEN, ruwe opname regisseur-16 beeld 100.
- Zin 5 en 6: "N panel › Click Joints › Figure joints › Figure from rig (or More bones (ankles too)). Select the rigged mesh first." (`platformen/blender/superhive/where-to-find-it.md`, gekeurde winkeltekst).
- Zin 7: "Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle ... Place the 3D cursor and click the body part." (gumroad-1.1.md r. 42).
- Zin 8: "If a bone has a Limit Rotation constraint, the hinge stops at that angle" (gumroad-1.1.md r. 38); knie stop 119,96 "from rig" (GEZIEN, film-pro.json regisseur-16).
- Geen prijs, geen "holds a pose". Opname met Pro 1.2.6 (main a1e868b, CHANGELOG 1.2.6 "enkels via More bones ook op de studio-robot"; e2e 45384569641 toets `e2e/toetsen_robot_meer.py`, Olaf 24 nov). Knop More bones bestaat sinds 1.2.0 (`platformen/blender/pro-1.2.0.md`).

## Licenties
- Stem: Kokoro-82M v1.0, stem af_heart (Apache-2.0, hexgrad/Kokoro-82M; kokoro-onnx MIT).
- Figuur en rig: van ons. Software in beeld: Blender 5.3.0 (GPL) met Click Joints Pro 1.2.6 (van ons, main a1e868b).

## Keuring
- keurder: Iris, 24 nov 2026 ±16:50 UTC, `marketing/keuring/2026-11-24-yt-short-cc-fit-na-botnamen-enkels-speling-es-iris.md`
- beeld en plezier: akkoord **ja**, Moet geen
- Kan: grootste punt: het buigmoment is de knie, niet de enkel, en de lijst met de enkels staat niet in beeld (alleen de groene ringen); eerste beeld dichter op de voeten; Exploded view bij zin 9 nauwelijks uit elkaar.
