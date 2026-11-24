# Click Joints Pro 1.2.6: releasenote (1.2.4 tot en met 1.2.6 samen) (Bram, 24 nov 2026)

**Waarom (geld):** de sale begint do 26 nov. Met 1.2.6 krijgt ook een figuur met blokvoeten (de studio-robot uit onze filmpjes) enkels via "More bones". Dan klopt wat de Regisseur in de enkel-Short laat zien met wat de koper krijgt. Effect op verkoop: GOK, klein; vooral geen terugbetaling.

**Opdracht:** Olaf 24 nov ±14:05 NL. Alleen gebruiken als de 1.2.6-zip er vóór do 27 nov 03:08 is; anders geldt `pro-1.2.5.md`. 1.2.4 en 1.2.5 zijn nooit in een winkel geweest, dus één note voor alle drie.

## Bewijs (GEZIEN, logs van e2e-run 45384569641 op tak `claude/blender-pro-1.2.6-robot-enkels`, stap `toetsen_robot_meer.py`)
- **5.2.3 en 5.3.0:** robot met "More bones": 11 gewrichten, "Left ankle · Hinge · 0–90°" en "Right ankle · Hinge · 0–90°", knieën 0–120°, KLAAR 0 FOUT.
- **4.2.23:** robot 7 gewrichten, rechterenkel en linkerknie overgeslagen met reden ("use a newer Blender such as 5.2"). Groen is daar geen bewijs van enkels, dus de grens "Blender 5.2 or newer" blijft.
- Code: a1e868b (bol van het vangnet krijgt de maat van het scheenbot), Daan ja 13:55 (bovenaan `producten/blender-gewrichten/ontwerp.md`).
- E2e op main 0b76311 (run 45394571001) liep nog bij het schrijven. De hoofdchat plakt pas na groen en de uitgave-run, zoals bij 1.2.5.
- Niet getoetst: andere rigs dan de MakeHuman-figuur en de robot. Daarom "human figures, including blocky feet", niet "any figure".

## 1. Winkeltekst (Gumroad én Superhive), bullet "Figure from rig"
Alleen het laatste stuk verandert ten opzichte van `pro-1.2.5.md` deel 1:
```
Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. With "More bones", ankles become hinges too, also on blocky feet (Blender 5.2 and newer).
```
Daan K2 (`Every 1.x update is free`) blijft zoals in `pro-1.2.5.md`.

## 2. Releasenote 1.2.6 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.6
- "More bones" now gives ankles: a hinge from shin to foot that bends 0 to 90 degrees, while the knees keep their own range. Works on human figures and on blocky feet, like a robot. Needs Blender 5.2 or newer; in 4.2 the ankles are skipped with the reason shown.
- When Figure from rig cannot cut a joint, the list now shows the real reason and what you can do, instead of "Try a spot further from the end".
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Achter elke regel: regel 1 is eef0792 (1.2.5, MakeHuman, zie `pro-1.2.5.md`) plus a1e868b (1.2.6, robot), 0–90 en 0–120 uit de logs hierboven. Regel 2 is d0cfb6e uit 1.2.4 (al gekeurd). Regel 3: e2e 45384569641 groen in alle drie; op main nog na te kijken (45394571001).

## 3. Update log Superhive (bovenaan erbij)
```
1.2.6 (<dag van upload> Nov 2026): "More bones" now gives ankles on human figures and blocky feet (Blender 5.2+). Clearer reason when Figure from rig cannot cut a joint.
```
Geen aparte regels voor 1.2.4 en 1.2.5: die stonden nooit in de winkel.

## Stand
- 24 nov ±14:20 NL: tekst klaar, keuring gevraagd aan Daan. Na zijn ja en groene e2e op main plakt de hoofdchat dit met de 1.2.6-zip in plaats van `pro-1.2.5.md`.
