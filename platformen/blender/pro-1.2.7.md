# Click Joints Pro 1.2.7: releasenote (1.2.4 tot en met 1.2.7 samen) (Bram, 24 nov 2026)

**Waarom (geld):** de plak gebeurt pas bij de volgende sessie op de werklaptop, dus we plakken meteen 1.2.7 in plaats van 1.2.6 (hoofdchat-ronde 24 nov ±16:50 NL). Zo hoeft een koper die clip 3 volgt (Shift + rechtsklik) niet tegen een knop aan te lopen die weigert. Effect op verkoop: GOK, klein; vooral geen terugbetaling.

**Verschil met `pro-1.2.6.md` (door Daan gekeurd, ja 15:40):** alleen één regel erbij in de note (deel 2) en een paar woorden in de update log (deel 3). Winkeltekst blijft gelijk. Alleen die stukken hoeven herkeurd.

## Bewijs
- Alles uit het bewijsblok van `pro-1.2.6.md` blijft gelden (robot-enkels, 4.2-zin).
- Shift + rechtsklik: fix van Olaf op tak `claude/blender-pro-1.2.7-shift` (b105332). Daan ja voor de code (`platformen/blender/keuring/2026-11-24-daan-avond.md` deel 3); A2: Knee en de andere figuurknoppen lopen via `plaats_scharnier`, dus de reparatie geldt voor Knee, Elbow, Ankle en de hinge-knoppen. De zin is Daans kan-punt K2, met Elbow en Ankle erbij uit de melding van Olaf.
- E2e run 45424594725 op b105332: 5.2.3 success, 5.3.0 success, 4.2.23 liep nog (GEZIEN, Actions-API, 24 nov ±17:10 NL). Regel "Tested on ... 4.2 LTS" pas plakken als 4.2.23 ook groen is (moet 1 van Daan).

## 1. Winkeltekst (Gumroad én Superhive), bullet "Figure from rig"
Alleen het laatste stuk verandert ten opzichte van `pro-1.2.5.md` deel 1:
```
Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. With "More bones", ankles become hinges too, also on blocky feet (Blender 5.2 and newer).
```
Daan K2 (`Every 1.x update is free`) blijft zoals in `pro-1.2.5.md`.

## 2. Releasenote 1.2.7 (Engels, Gumroad en Superhive)
```
Click Joints Pro 1.2.7
- "More bones" now gives ankles: a hinge from shin to foot that bends 0 to 90 degrees, while the knees keep their own range. Works on human figures and on blocky feet, like a robot. Needs Blender 5.2 or newer for both ankles; in 4.2 one or both may be skipped, each with the reason shown.
- Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons.
- When Figure from rig cannot cut a joint, the list now shows the real reason and what you can do, instead of "Try a spot further from the end".
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Nieuw is alleen regel 2. De andere regels staan letterlijk zo in `pro-1.2.6.md`.

## 3. Update log Superhive (bovenaan erbij)
```
1.2.7 (<dag van upload> Nov 2026): "More bones" now gives ankles on human figures and blocky feet (Blender 5.2+). Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons. Clearer reason when Figure from rig cannot cut a joint.
```
Geen aparte regels voor 1.2.4, 1.2.5 en 1.2.6: die stonden nooit in de winkel.

## 4. Blok bovenaan Superhive: "New in Pro 1.2" wordt "New in Pro 1.2.7" (vervangt het hele blok)
**Waarom (geld):** live staat nu in de tweede zin "Needs Blender 4.5 or newer." (GEZIEN, curl 24 nov ±17:20 en ±18:00 NL). Los gelezen zegt dat: Pro werkt pas vanaf 4.5. Een koper op 4.2 LTS haakt daar af, terwijl twee regels verder 4.2 als getest staat. Drie dagen voor de Cyber Sale is dit wat een koper als eerste leest (opdracht hoofdchat 17:25). Effect: GOK, klein maar zonder kosten.
```
New in Pro 1.2.7
- "More bones" now gives ankles, also on blocky feet like a robot (Blender 5.2 and newer).
- Shift + right click on the skin now works with Knee, Elbow, Ankle and the hinge buttons.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.

Also new in 1.2
- Fit test strip: print this first. Five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer.
- Figure from rig now places elbows on rigs where the elbow would otherwise bend upward, for example Quaternius characters (Blender 4.5 and newer).
```
- Regel 1 en 2 komen uit de note in deel 2 (Daan ja 17:40), ingekort. Regel 3 idem.
- "Also new in 1.2" (kan K1 Daan, was "since") en niet alles onder "1.2.7": de teststrip en de elleboog kwamen in 1.2.0, dus onder een kop 1.2.7 zou dat niet kloppen.
- De elleboogzin: de grens 4.5 staat nu tussen haakjes bij die ene functie, niet meer als losse zin. Feit uit `pro-1.2.0.md` (Daan ja 22 nov): op 4.2 tot 4.4 vraagt hij de elleboog met de hand.
- Het blok "Already bought Pro? ..." onder Good to know: "1.2" mag blijven, 1.2.7 valt eronder.
- Niet gedaan (kan van de hoofdchat): een regel met alle versies die in de winkel stonden. Later, als er tijd is; geen ritme beloven.

## Stand
- 24 nov ±17:15 NL: tekst klaar, herkeuring van regel 2 en de update log gevraagd aan Daan. Plakken met de 1.2.7-zip in plaats van `pro-1.2.6.md`, na Daans ja, groene e2e in alle drie en de uitgave-run van Olaf.
- 24 nov ±18:05 NL: deel 4 (blok bovenaan Superhive, de 4.5-zin) erbij. Losse herkeuring van alleen deel 4 gevraagd aan Daan, vóór 21:00, zodat het in dezelfde plak mee kan.
