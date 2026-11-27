# YouTube-beschrijvingen Click Joints: zonder de oude testzin, versie 1.2.8, met saleregel (Bram, vr 27 nov 2026, issue #244)

**Status:** Daan ja (8, #246, 27 nov ±05:00). Zijn twee kan-punten verwerkt (27 nov 06:20 NL): in de saleregel van de Shorts de dubbele "Type dortus.com/yt" weg (die staat al onderaan), en in 65JiRlDupNc de saleregel direct na de eerste zin. Klaar om te plakken voor de hoofdchat (YouTube Studio, per video "Details", hele beschrijving vervangen).

**Waarom (geld en eerlijkheid):** 7 van onze 10 Click Joints-filmpjes hadden de oude zin dat wij nog niet testten met printen, en 2 een kortere vorm daarvan, tegen het besluit van Thijs van 24 nov 15:32 (harde regel 5). Samen hebben de 10 filmpjes 7.670 weergaven (GEZIEN, RSS van ons kanaal, curl 27 nov ±04:10 NL), het meeste verkeer dat we hebben. Geen enkele noemde de sale. Effect op verkoop: GOK, klein maar zeker niet negatief.

**Wat er verandert per beschrijving:**
- Die zin is overal weg, zonder om te draaien. Er staat nu: "Measured in Blender. Print a test joint first: every printer is different." (dezelfde woorden als op dortus.com na #160, Daan ja).
- Het oude versienummer achter "Click Joints Pro" wordt "Click Joints Pro (now version 1.2.8)": de opname is met een oudere versie gemaakt; zo beweren we niet dat het 1.2.8 was. In de lange video: "The current version is 1.2.8. Already bought Pro? 1.2.8 is a free update."
- De eerste regel blijft de haak van dat filmpje (bij de twee lange video's de link dortus.com/yt). De saleregel staat direct na de eerste zin, zodat hij in de ingeklapte beschrijving te zien is.
- Shorts: links in een Shorts-beschrijving zijn niet aanklikbaar, dus de regel zegt "type dortus.com/yt" en noemt de code. dortus.com/yt linkt nu naar de gewone Gumroad-pagina, waar de korting niet vanzelf aan staat (sale-controle.sh 27 nov ±04:15: salelink `"valid":true`, gewone pagina `null`, GEZIEN). Daarom staat de code CYBER25 in elke regel; zo werkt het ook als /yt later de salelink krijgt.
- Lange video's (4-3l3MZZWPc, m3sNvDOJYQ0): daar zijn links wel aanklikbaar, dus de salelink met code en `utm_source=yt`.
- Klein erbij, alleen waar het al over Pro ging: de Fit test strip (sinds 1.2.0, vijf testgewrichten van 0,10 tot 0,30 mm, `platformen/blender/pro-winkeltekst-b3.md`), want die is nieuw sinds de opname en past bij "print a test joint first".
- Titels en hashtags blijven gelijk (de emoji in de titels laat ik weg in de koppen hieronder, de titel zelf verandert niet).

**Feiten in de saleregel:** CYBER25, 25%, Personal $19 wordt $14.25 ("from $14.25", want de duurdere licenties kosten meer), loopt tot `2026-12-01T22:59:00Z` = di 1 dec 23:59 CET (GEZIEN, salelink 27 nov ±04:15 NL); CET is de tijd in Nederland in december.

**Weghalen:** op wo 2 dec elke beschrijving vervangen door het blok "Na de sale". Een verlopen saleregel maakt een kijker wantrouwig.

**Controle na het plakken:** `curl -s "https://www.youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg" | grep -ci "print.test\|printed.yet\|Pro 1\.1"` moet 0 geven. Het Ebb-filmpje (sgcC965GVps) hoort niet bij Click Joints en blijft zoals het is.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 1. awtDyH5hOPI: Rigged character to poseable 3D print in Blender: one button
https://studio.youtube.com/video/awtDyH5hOPI/edit (weergaven 27 nov ±04:10 NL: 387, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
From a rigged character to a poseable figure for 3D printing.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

One button, Figure from rig, cuts hinges at elbows and knees and ball joints at shoulders, hips and neck from the figure itself. Then check the whole pose before you print. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
From a rigged character to a poseable figure for 3D printing.

One button, Figure from rig, cuts hinges at elbows and knees and ball joints at shoulders, hips and neck from the figure itself. Then check the whole pose before you print. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 2. lcUBuWMaJ_A: How far can a 3D printed knee bend? Check it in Blender
https://studio.youtube.com/video/lcUBuWMaJ_A/edit (weergaven 27 nov ±04:10 NL: 1293, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
How far can a 3D printed knee bend?

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

This knee stops at 120 degrees, read from the rig. Bend past it and the arc turns red and says how far. Back inside the stop, the red is gone. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
How far can a 3D printed knee bend?

This knee stops at 120 degrees, read from the rig. Bend past it and the arc turns red and says how far. Back inside the stop, the red is gone. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 3. pCyyQ4Qa9Gw: Your rigged character as printable parts with joints | Blender
https://studio.youtube.com/video/pCyyQ4Qa9Gw/edit (weergaven 27 nov ±04:10 NL: 846, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
From one rigged character to separate printable parts with joints, in Blender.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

1. Select the rigged figure and press Figure from rig.
2. It is cut into parts with 9 joints.
3. Exploded view moves the parts apart along each joint: you see the ball and socket at the shoulder and at the hip.
4. Pick 3MF and press Export: one file per part (10 files here).

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
From one rigged character to separate printable parts with joints, in Blender.

1. Select the rigged figure and press Figure from rig.
2. It is cut into parts with 9 joints.
3. Exploded view moves the parts apart along each joint: you see the ball and socket at the shoulder and at the hip.
4. Pick 3MF and press Export: one file per part (10 files here).

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 4. eQsepIbHdgU: Make your rigged character poseable for 3D printing | Blender
https://studio.youtube.com/video/eQsepIbHdgU/edit (weergaven 27 nov ±04:10 NL: 649, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
Make your rigged character poseable for 3D printing, step by step in Blender.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

1. Select your rigged character.
2. Press Figure from rig: hinges at elbows and knees, ball joints at shoulders, hips and neck.
3. Check the list: every joint with its range in degrees.
4. Bend a knee to its end stop. Past the stop you see a red arc and how far past the limit you went.
5. Exploded view shows the ball joints, then export every part as 3MF.

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
Make your rigged character poseable for 3D printing, step by step in Blender.

1. Select your rigged character.
2. Press Figure from rig: hinges at elbows and knees, ball joints at shoulders, hips and neck.
3. Check the list: every joint with its range in degrees.
4. Bend a knee to its end stop. Past the stop you see a red arc and how far past the limit you went.
5. Exploded view shows the ball joints, then export every part as 3MF.

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 5. I78weVdhwdw: One click: rig to 10 printable parts in Blender
https://studio.youtube.com/video/I78weVdhwdw/edit (weergaven 27 nov ±04:10 NL: 1147, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
One button turns a rigged figure into printable parts.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

Hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck. 9 joints, 10 parts, and every joint shows its range in degrees. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
One button turns a rigged figure into printable parts.

Hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck. 9 joints, 10 parts, and every joint shows its range in degrees. Measured in Blender. Print a test joint first: every printer is different.

Real recording in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8), on a MakeHuman figure (CC0).
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 6. Ij-jc6t4WNo: How far can this knee bend? Check it before you print | Blender
https://studio.youtube.com/video/Ij-jc6t4WNo/edit (weergaven 27 nov ±04:10 NL: 613, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
How far can the knee of your 3D printed figure bend? Check it in Blender before you print.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

1. Our rig has a Limit Rotation of 120° on the left knee.
2. Select the figure and press Figure from rig.
3. The list shows the left knee 0 to 120° from your rig; the right knee without a limit takes the same range (mirrored).
4. Bend the knee with the Bend slider. At 120° it is at the end stop; past it you see a red arc and "+12° past limit".

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

**Na de sale (plak wo 2 dec):**
```
How far can the knee of your 3D printed figure bend? Check it in Blender before you print.

1. Our rig has a Limit Rotation of 120° on the left knee.
2. Select the figure and press Figure from rig.
3. The list shows the left knee 0 to 120° from your rig; the right knee without a limit takes the same range (mirrored).
4. Bend the knee with the Bend slider. At 120° it is at the end stop; past it you see a red arc and "+12° past limit".

Measured in Blender. Print a test joint first: every printer is different.

Real screen recording and viewport render in Blender 5.3 with our add-on Click Joints Pro (now version 1.2.8). Figure: MakeHuman base mesh (CC0 1.0, github.com/makehumancommunity/makehuman), colours and rig added by us.
Click Joints Pro: type dortus.com/yt in your browser.

#blender #3dprinting #b3d #blenderaddon #shorts
```

## 7. 4-3l3MZZWPc: Blender rig to 3D printable figure: one button, hinges and ball joints | Click Joints Pro
https://studio.youtube.com/video/4-3l3MZZWPc/edit (weergaven 27 nov ±04:10 NL: 14, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
https://dortus.com/yt/

Cyber Week: Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25. This link applies the code: https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=yt

Got a rigged figure in Blender? Click Joints Pro turns it into printable parts with one button. Figure from rig puts a hinge with an end stop at every elbow and knee, and a ball joint at shoulders, hips and neck. Next to each joint you see how far it bends, in degrees.

The end stop comes from Limit Rotation in your rig. No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part. Drag Bend to check a hinge: past the stop the arc turns red and shows how far you went. Then Exploded view, and export every part as STL or 3MF.

Measured in Blender. Print a test joint first: every printer is different. Pro has a Fit test strip for that: five test joints from 0.10 to 0.30 mm, so you see which gap fits your printer. Recorded in Blender 5.3 with the add-on itself, on a MakeHuman figure (CC0) with a simple 20-bone rig. Works best on figures with separate arms and legs, about 200 mm tall or more.

0:00 What it does
0:10 Start with a rigged figure
0:24 One button, every joint
0:40 Every range in degrees
0:56 Bend to the stop
1:07 Past the stop
1:19 Exploded view
1:37 Export STL or 3MF
1:49 Good to know
2:03 Where to get it

Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
The current version is 1.2.8. Already bought Pro? 1.2.8 is a free update.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

**Na de sale (plak wo 2 dec):**
```
https://dortus.com/yt/

Got a rigged figure in Blender? Click Joints Pro turns it into printable parts with one button. Figure from rig puts a hinge with an end stop at every elbow and knee, and a ball joint at shoulders, hips and neck. Next to each joint you see how far it bends, in degrees.

The end stop comes from Limit Rotation in your rig. No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part. Drag Bend to check a hinge: past the stop the arc turns red and shows how far you went. Then Exploded view, and export every part as STL or 3MF.

Measured in Blender. Print a test joint first: every printer is different. Pro has a Fit test strip for that: five test joints from 0.10 to 0.30 mm, so you see which gap fits your printer. Recorded in Blender 5.3 with the add-on itself, on a MakeHuman figure (CC0) with a simple 20-bone rig. Works best on figures with separate arms and legs, about 200 mm tall or more.

0:00 What it does
0:10 Start with a rigged figure
0:24 One button, every joint
0:40 Every range in degrees
0:56 Bend to the stop
1:07 Past the stop
1:19 Exploded view
1:37 Export STL or 3MF
1:49 Good to know
2:03 Where to get it

Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
The current version is 1.2.8. Already bought Pro? 1.2.8 is a free update.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

## 8. m3sNvDOJYQ0: Blender hinge for 3D printing that stops at 115° | Click Joints Pro
https://studio.youtube.com/video/m3sNvDOJYQ0/edit (weergaven 27 nov ±04:10 NL: 22, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
https://dortus.com/yt/

Cyber Week: Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25. This link applies the code: https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=yt

We make Click Joints, a Blender add-on that cuts a part into joints for 3D printed figures. This video shows the hinge from Click Joints Pro: pick an end stop of 90°, 115° or 135°, click Place hinge, and drag Bend to see how far it goes. Push past the stop and the arc turns red and shows how far you went, so you see the limit before you print.

Measured in Blender. Print a test joint first: every printer is different. Recorded in Blender 5.3 with the add-on itself; the colours and the arc come from the add-on.

0:00 What it does
0:10 Place a hinge
0:30 Bend to the stop
0:44 Past the stop
1:02 90°, 115° or 135°
1:32 Ball joints too
1:42 Where to get it

Also in Pro (now version 1.2.8): Figure from rig, ball joints with the green fit band, the Fit test strip, Exploded view, export as STL or 3MF.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

**Na de sale (plak wo 2 dec):**
```
https://dortus.com/yt/

We make Click Joints, a Blender add-on that cuts a part into joints for 3D printed figures. This video shows the hinge from Click Joints Pro: pick an end stop of 90°, 115° or 135°, click Place hinge, and drag Bend to see how far it goes. Push past the stop and the arc turns red and shows how far you went, so you see the limit before you print.

Measured in Blender. Print a test joint first: every printer is different. Recorded in Blender 5.3 with the add-on itself; the colours and the arc come from the add-on.

0:00 What it does
0:10 Place a hinge
0:30 Bend to the stop
0:44 Past the stop
1:02 90°, 115° or 135°
1:32 Ball joints too
1:42 Where to get it

Also in Pro (now version 1.2.8): Figure from rig, ball joints with the green fit band, the Fit test strip, Exploded view, export as STL or 3MF.
There is a free version with ball joints on extensions.blender.org (search "Click Joints").

#blender #3dprinting #b3d
```

## 9. WqgDSDL5twg: Blender add-on: a hinge for knees and elbows with an end stop at 115°
https://studio.youtube.com/video/WqgDSDL5twg/edit (weergaven 27 nov ±04:10 NL: 1479, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
We made a Blender add-on that places a hinge with an end stop for knees and elbows: in Blender it bends to 115° and stops there, instead of flopping backwards.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25.

Bend it past the stop and the overshoot shows in red. Ball joints are free on Blender Extensions; the hinge is in Click Joints Pro. Measured in Blender. Print a test joint first: every printer is different. #blender #3dprinting #b3d #blenderaddon #articulated

Click Joints Pro: dortus.com/yt
The link is also at the top of our channel page.
```

**Na de sale (plak wo 2 dec):**
```
We made a Blender add-on that places a hinge with an end stop for knees and elbows: in Blender it bends to 115° and stops there, instead of flopping backwards.

Bend it past the stop and the overshoot shows in red. Ball joints are free on Blender Extensions; the hinge is in Click Joints Pro. Measured in Blender. Print a test joint first: every printer is different. #blender #3dprinting #b3d #blenderaddon #articulated

Click Joints Pro: dortus.com/yt
The link is also at the top of our channel page.
```

## 10. 65JiRlDupNc: See how far a joint bends before you 3D print it (free Blender add-on)
https://studio.youtube.com/video/65JiRlDupNc/edit (weergaven 27 nov ±04:10 NL: 1220, GEZIEN, RSS)

**In de sale (plak vr 27 nov, weg op wo 2 dec):**
```
See how far a joint bends, before you print.

Click Joints Pro is 25% off until Tuesday 1 December, 23:59 CET: from $14.25 instead of $19 with code CYBER25 at dortus.com/yt

Click Joints is a free Blender add-on for articulated, poseable 3D prints. Get it: in Blender, open Edit, Preferences, Get Extensions and search "Click Joints".

Want a whole figure that moves? Click Joints Pro reads your rig and puts a hinge with an end stop at every elbow and knee: dortus.com/yt

#blender #3dprinting #articulated #blenderaddon
```

**Na de sale (plak wo 2 dec):**
```
See how far a joint bends, before you print. Click Joints is a free Blender add-on for articulated, poseable 3D prints. Get it: in Blender, open Edit, Preferences, Get Extensions and search "Click Joints".

Want a whole figure that moves? Click Joints Pro reads your rig and puts a hinge with an end stop at every elbow and knee: dortus.com/yt

#blender #3dprinting #articulated #blenderaddon
```
