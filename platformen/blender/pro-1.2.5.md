# Click Joints Pro 1.2.5: releasenote (1.2.4 en 1.2.5 samen) en de enkel-zin terug (Bram, 24 nov 2026)

**Waarom (geld):** de sale begint do 26 nov. Met 1.2.5 doet "More bones" eindelijk wat de knop belooft: enkels op een mensfiguur. Dat mag weer in de winkeltekst, maar alleen zo ver als getoetst. Effect op verkoop: GOK, klein; vooral geen terugbetaling.

**Opdracht:** hoofdchat 24 nov ±12:15 NL. Zip `click_joints_pro-1.2.5.zip` uit uitgave-run 45380984015 op e2e-run 45372957961 (GEZIEN door de hoofdchat). 1.2.4 is nooit in een winkel geweest, dus één note voor beide.

## Bewijs voor de enkel-zin (GEZIEN, logs van e2e-run 45372957961 op main)
- Stap met `CJ_MEER=1` op de MakeHuman-figuur (`e2e/toetsen_mens.py`, workflow r. 229) draait in alle drie de versies; job groen in 4.2.23, 5.2.3 en 5.3.0.
- **5.2.3 en 5.3.0:** "Left ankle · Hinge · 0–90°" en "Right ankle · Hinge · 0–90°" geplaatst, knieën nog 0 tot 120.
- **4.2.23:** beide enkels overgeslagen met reden "the cut parts overlap before they move here; place it by hand a few mm along the bone, or use a newer Blender such as 5.2". De toets eist de enkels pas vanaf 4.5 (`oud = bpy.app.version < (4, 5, 0)`), dus groen is daar geen bewijs van enkels.
- Niet getoetst: de robot en andere rigs met `meer=True` (Daan K1). Daarom "on human figures", niet "on any figure" of "most figures".

## 1. Winkeltekst: zin terug, met grens (Gumroad én Superhive)
Bullet "Figure from rig", woord voor woord:
```
Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. With "More bones", ankles on human figures become hinges too (Blender 5.2 and newer).
```
En Daan K2 (keuring 1.2.4-tekst): `Already bought Pro? 1.1 is a free update` wordt `Already bought Pro? Every 1.x update is free` (rest van de regel gelijk).
Aangepast in `platformen/blender-2/gumroad-1.1.md` r. 37 en 51, `superhive-1.1.md` r. 50 en 65, `winkeltekst-1.1.md` r. 11 en 39.

## 2. Releasenote 1.2.5 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.5
- "More bones" now gives ankles on human figures: a hinge from shin to foot that bends 0 to 90 degrees, while the knees keep 0 to 120. Needs Blender 5.2 or newer; in 4.2 the ankles are skipped with the reason shown.
- When Figure from rig can not cut a joint, the list now shows the real reason and what you can do, instead of "Try a spot further from the end".
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Achter elke regel: regel 1 is eef0792 (enkel met de assen van de scheen, afstandsregel nooit strenger dan voorheen, Daan ja `keuring/2026-11-24-pro-1.2.5-enkels-daan.md`), 0–90 en 0–120 uit de logs hierboven. Regel 2 is d0cfb6e uit 1.2.4 (Daan ja `keuring/2026-11-24-pro-1.2.4-knie-daan.md`, tekst al gekeurd in `keuring/2026-11-24-pro-1.2.4-tekst-daan.md`). Regel 3: e2e 45372957961 groen in alle drie.
Bewust niet: "right knee in 4.2 works now" (de 1.2.4-fix geeft alleen de goede reden) en geen enkels op de robot.

## 3. Update log Superhive (bovenaan erbij)
```
1.2.5 (<dag van upload> Nov 2026): "More bones" now gives ankles on human figures (Blender 5.2+). Clearer reason when Figure from rig can not cut a joint.
```
1.2.4 krijgt geen eigen regel: die stond nooit in de winkel.

## Stand
- 24 nov ±12:25 NL: teksten klaar, keuring gevraagd aan Daan. Na zijn ja plakt de hoofdchat dit samen met de 1.2.5-zip. `pro-1.2.4.md` vervalt hiermee.
