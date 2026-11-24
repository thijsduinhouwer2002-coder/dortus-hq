# Opnames vanavond met Max (ElevenLabs)

Regisseur run 27, 24 nov 2026 ±19:10 NL, op opdracht van de hoofdchat (18:05). Stem: "Max - Witty Commercial Actor", Eleven v4.

**Keuze: 5 filmpjes en 1 losse slotzin in plaats van 6 filmpjes.** Waarom: alle vijf hebben de eigen robot of een echt gewricht groot in beeld; de andere tip-Shorts openen met een kaal blokje of bolletje in een grijs venster (zelf bekeken, GEZIEN) en halen de lat "spectaculair" niet. De saleversies maak ik niet met een tweede volle opname: Max zegt de saleslotzin één keer los, en de workflow zet die achter elke gewone opname (`STEM_SLOT_MP3`, nieuw in `stem.py`). Zo krijgen alle vijf een saleversie voor 26 nov tot en met 1 dec, voor ±3.300 credits in plaats van ±6.500 (GOK: ±650 per Short, ±40 voor de losse zin).

**Hoe opnemen:** per filmpje één mp3, de zinnen precies zoals hieronder, in deze volgorde, met een korte pauze (±0,5 s) tussen de zinnen en geen lange pauze binnen een zin. Getallen staan uitgeschreven zoals Max ze moet zeggen. Zet de mp3 onder de naam die erbij staat in de repo; een push start de workflow vanzelf, die knipt de opname in zinnen en legt het beeld erop (beeld volgt stem). Ik kijk de uitslag na en zet het concept op open voor de Keurder.

Uploadvolgorde (voorstel): 25 nov de gewone versies; vanaf do 26 nov avond tot en met di 1 dec de saleversies (alleen als CYBER25 aanstaat).

## 1. pro-al-gesplitst
- wat: Pro, nieuw (Pro 1.2.7: Shift + rechtsklik). Hook: Already split your figure?
- eerste beeld: Studio-render van de eigen robot op een sokkel, knie gebogen, warm licht, groot in beeld; kop "Can it still bend?". Spectaculair genoeg (zelf bekeken, GEZIEN).
- mp3: `commercie/filmpjes/regisseur-24/pro-al-gesplitst-elevenlabs.mp3`
- saleversie: `pro-al-gesplitst-sale` uit dezelfde mp3 plus de saleslotzin

```
Already split your figure? Can that knee still bend?
This robot is already in parts: a body and two separate legs.
Click the leg you want to bend.
Turn the view to the side. The hinge turns around the way you look.
Shift and right click on the knee. The 3D cursor jumps there.
In Click Joints Pro, go to Figure joints and click Knee.
It cuts the leg in two and builds a hinge right at the cursor.
The panel shows how far it bends: zero to one hundred and thirty-five degrees.
Next, turn on Show bend range to see the whole swing.
Elbow and Ankle work the same way.
Your parts stay just as they are. Now that knee can bend.
Every printer is different. Print a test joint first.
Click Joints Pro, on Gumroad.
```

## 2. pro-robot-delen
- wat: Pro, de kern: één knop Figure from rig. Saleversie komt uit dezelfde opname plus de saleslotzin (onderaan).
- eerste beeld: Studio-render van de robot in één stuk op een sokkel, kop "One solid piece?" (GEZIEN).
- mp3: `commercie/filmpjes/regisseur-14/pro-robot-delen-elevenlabs.mp3`
- saleversie: `pro-robot-delen-sale` uit dezelfde mp3 plus de saleslotzin

```
Is your figure still one solid piece?
This robot has a rig, but it is one solid mesh.
Select it, and press one button: Figure from rig.
It cuts the robot into parts, each with its own joint.
It reads your rig and lists every joint it placed.
Elbows and knees get a hinge with an end stop, the rest a ball joint.
Click the lower leg and drag Bend to the stop.
Past the stop, red shows where parts would hit.
Exploded view pulls the parts apart.
Then step three, Fit and export, writes every part as its own file.
Exporting is in the free Click Joints too. The one-click figure is Pro.
Every printer is different. Print a test joint first.
Click Joints Pro, on Gumroad.
```

## 3. pro-botnamen
- wat: Pro: botnamen van acht rig-soorten.
- eerste beeld: Was een grijs Blender-venster met een kluwen botnamen. Nu omgebouwd (run 27): studio-render van de robot uit elkaar in losse delen (exploded), kop "Your bone names?".
- mp3: `commercie/filmpjes/regisseur-16/pro-botnamen-elevenlabs.mp3`
- saleversie: `pro-botnamen-sale` uit dezelfde mp3 plus de saleslotzin

```
Does your rig use different bone names?
This robot's rig uses Mixamo style bone names.
Click Joints Pro knows the bone names of the common rigs.
Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz.
Press Figure from rig, and it finds the elbows, knees, shoulders, hips and neck.
It cuts the robot into parts, with a joint at each one.
Does a bone have a Limit Rotation? Then the hinge stops at that angle.
No limit on one side? It takes the limit of the other side.
Drag Bend on the knee, and it stops at the angle from your rig.
Past the stop, red shows where parts would hit.
Exploded view pulls the parts apart.
Every printer is different. Print a test joint first.
Click Joints Pro, on Gumroad.
```

## 4. pro-enkels
- wat: Pro: enkels erbij met More bones.
- eerste beeld: Was een Blender-venster met de rig. Nu omgebouwd (run 27): studio-render van de robot met blauwe enkelringen, ingezoomd op benen en voeten, kop "Stiff feet?".
- mp3: `commercie/filmpjes/regisseur-17/pro-enkels-elevenlabs.mp3`
- saleversie: `pro-enkels-sale` uit dezelfde mp3 plus de saleslotzin

```
Does your figure stand on stiff feet?
Figure from rig gives shoulders, elbows, hips, knees and the neck by default.
For the ankles too, press More bones, right under Figure from rig.
It cuts the robot into parts, with a joint at each one.
Select the rigged mesh first, then press it: the ankles get a joint too.
You find it in the N panel, under Click Joints, in Figure joints.
No rig? There is an Ankle preset: put the 3D cursor on the ankle.
Drag Bend on the knee, and it stops at the angle from your rig.
Exploded view pulls the parts apart.
Every printer is different. Print a test joint first.
Click Joints Pro, on Gumroad.
```

## 5. tip-speling
- wat: Gratis tip (gemeten speling bij een kogelgewricht), slot naar Pro. Iris: beeld ja.
- eerste beeld: Kogel en kom in Blender met de gradenring; nu dichter op bal en kom ingezoomd (run 27, punt van Iris).
- mp3: `commercie/filmpjes/regisseur-18/tip-speling-elevenlabs.mp3`
- saleversie: `tip-speling-sale` uit dezelfde mp3 plus de saleslotzin

```
Is your gap really what you set?
Set a gap, cut, and check that the real gap matches.
Select your part, and put the three D cursor where the joint goes.
Pick Ball, keep Clearance at zero point two, and press Place joint.
Click Joints measures the gap between ball and socket after the cut.
It averages many points around the ball, and shows that in the panel.
Next to it you see the wall thickness, so a thin socket shows too.
Exploded view pulls the ball out of the socket, so you can check it.
Not sure which gap your printer likes? Print a fit test first.
The measured gap is in the free Click Joints, for every ball joint.
Every printer is different. Print a test joint first.
Click Joints is free. Want more? Click Joints Pro, on Gumroad.
```

## 6. Saleslotzin (één keer, los)
- mp3: `commercie/filmpjes/stem/slotzin-sale-elevenlabs.mp3`
- gebruikt door de saleversies van alle vijf hierboven (vervangt alleen de laatste zin). Bij tip-speling valt in de saleversie "Click Joints is free. Want more?" weg; ondertitel en stem zeggen dan alleen deze zin.

```
Click Joints Pro, twenty five percent off this week, on Gumroad.
```

## Wat er niet in staat (eerlijk)
- Geen "not print tested", geen AI, geen "holds a pose", geen url. Elke Short noemt "Every printer is different. Print a test joint first." (besluit Thijs 24 nov 15:32).
- Bronnen per bewering staan in de concepten in `marketing/wachtrij/` (pro-robot-delen, pro-botnamen, pro-enkels, tip-speling) en in `commercie/filmpjes/regisseur-24/concept-klad.md`.
