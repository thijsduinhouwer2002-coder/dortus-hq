# Zes Short-scripts Click Joints Pro, week 49 (30 nov tot 6 dec 2026)

Door Sanne, 23 nov 2026. Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL. Zelfde bouw als `week-48-click-joints.md` (zin 1 = hook A of B, max 7 woorden, vraag over het probleem van de kijker; daarna zinnen van 11 tot 16 woorden, 4 tot 6 s; printzin altijd; "Voice: AI text to speech (Kokoro)" in de beschrijving). Bronnen: `platformen/blender-2/gumroad-1.1.md` en `platformen/blender/pro-1.2.0.md`; script 4 rust ook op `platformen/blender/pro-1.2.1.md` (zie daar).

## Wat ik meenam uit de keuringen van 23 nov
- **Geen knie in beeld als hoofdzaak** (B3 stem-Short, B1 Daan knie-hook): vier knie-Shorts in een week is genoeg. Waar een buigend deel nodig is, neem ik de elleboog.
- **Kop korter dan de gesproken vraag** (C1), zodat hij niet twee keer letterlijk staat.
- **Getallen**: in de kop als cijfer ("150 mm"), uitgeschreven alleen in het json-veld `uitspraak` ("one hundred fifty millimetres").
- **Hook moet als vraag klinken** (A4 Daan): elke hook eindigt op een vraagteken en begint waar het kan met "Is", "Does" of "Still", zodat Kokoro de toon laat stijgen. Klinkt hij toch vlak, neem de B-versie.
- Nieuwe onderwerpen: geen enkel script hieronder staat al in de wachtrij of in week 48 (knie, Fit test, splitsen, scharnier of kogel, monster, Mixamo zijn al bezet).

---

## 1. Twintig delen exporteren? Eén knop
Titel: Export every part of your figure for 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Still exporting every part one by one? | One by one? | Blender met de lijst van tien delen, muis die er één selecteert en File, Export kiest (nieuw) |
| 1B | Is exporting your figure taking forever? | Taking forever? | zelfde beeld |
| 2 | This figure is cut into ten parts, each with its own joint already. | Ten parts | de gekleurde figuur in delen (studio-1) |
| 3 | In Click Joints Pro, step three is Fit and export, at the bottom. | Step 3 | paneel, inzoomen op "3 Fit and export" |
| 4 | Pick STL or 3MF with the two buttons right above the export button. | STL or 3MF | klik op 3MF, de knop wordt "Export 3MF" |
| 5 | Click once, and every part becomes its own file, ready for your slicer. | One file per part | map met de bestanden (opname, nieuw) |
| 6 | Every hinge and ball joint stays in its part, so nothing gets lost. | Joints stay in | delen apart naast elkaar |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render van de delen |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3 en 4: knoppen "3 Fit and export", STL | 3MF en "Export STL / Export 3MF" (gumroad-1.1.md: "split into parts, export to STL or 3MF"; knopnamen uit `paneel.py` r. 119, GEZIEN door Daan in eerdere keuring). Zin 5: één bestand per deel, uit de beschrijving van `exporteer.py` ("elk zichtbaar deel", één bestand per deel in mm). Zin 2: tien delen is de studio-figuur ("rig to 10 printable parts", eerdere Short). **Let op:** zin 6 is een gevolg van splitsen met het gewricht erin; de Regisseur laat in beeld een deel met zijn kogel of scharnier zien, anders zin 6 weglaten. Geen slicer-naam noemen of tonen.

---

## 2. Te kleine figuur? Dan past er geen scharnier
Titel: Why your small 3D printed figure can't have joints 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Is your figure too small for joints? | Too small? | dunne arm met een scharnier dat er niet in past (nieuw, render) |
| 2B | Printing your figure at 150 millimetres? | 150 mm? | zelfde beeld, liniaal ernaast |
| 2 | A hinge needs room: a pin, a wall around it, and a gap. | A hinge needs room | doorsnede van een elleboog |
| 3 | On a realistic figure at 150 millimetres, the arms are simply too thin. | Arms too thin | figuur op 150 mm, arm in beeld |
| 4 | Click Joints Pro does not force it. The list tells you why it skipped. | The list says why | lijst met een overgeslagen gewricht en reden |
| 5 | Our tip: scale the figure to about 200 millimetres or more first. | 200 mm or more | schaal in Blender, maat in beeld |
| 6 | It also works best when the arms and legs stand apart from the body. | Arms and legs apart | figuur in A-pose |
| 7 | Then press Figure from rig again, and check the list for every joint. | Check again | klik, lijst vult zich |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3, 5 en 6 uit "Good to know": "Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so." Zin 4: "Honest when it can not. A joint that does not fit is skipped, and the list tells you why and what to try." **Let op:** dat het op 200 mm bij dezelfde figuur wél lukt is GOK; de Regisseur neemt beide maten op met dezelfde figuur en toont alleen wat echt gebeurt. Lukt 200 mm niet, dan zin 7 weg en eindigen op zin 6. `uitspraak` zin 1B en 3: "one hundred fifty millimetres", zin 5: "two hundred millimetres".

---

## 3. Figuur met AI gemaakt? Zo krijgt hij gewrichten
Titel: Make your AI-generated figure poseable for 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 3A | Made your figure with an AI tool? | Made with AI? | AI-figuur in één stuk in Blender, draait rond (een van de drie geteste figuren) |
| 3B | Are your figure's legs stuck together? | Legs stuck? | broek of tuniek waar de benen tegen elkaar zitten, rood omcirkeld (nieuw) |
| 2 | We tested Click Joints Pro on three AI-made figures, in three Blender versions. | Tested on three | de drie figuren naast elkaar |
| 3 | Give the figure a rig, then press Figure from rig, and check the list. | Rig, then one button | klik op Figure from rig |
| 4 | Where the legs touch, like trousers or a tunic, the hips are skipped. | Hips skipped | lijst met de heup en de reden |
| 5 | The list tells you why, so you are not guessing what went wrong. | No guessing | inzoomen op de reden |
| 6 | The knees still work, and so do the elbows and the shoulders. | The rest still works | arm buigt bij de elleboog (geen knie als hoofdbeeld) |
| 7 | Our tip: make the figure with the legs a little apart if you can. | Legs apart | figuur in A-pose |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2 en 4: "Tested in Blender 4.2, 5.2 and 5.3 on a MakeHuman figure, a Rigify metarig and three AI-made figures" en "On AI-made figures where the legs touch (trousers, tunic), hips are skipped with a reason; knees still work." Zin 5: "the list tells you why and what to try". **Let op:** zin 6 zegt "elbows and shoulders": dat staat niet letterlijk in de bron. Alleen houden als de opname van die figuur ellebogen en schouders echt OK toont (Olaf, `producten/blender-gewrichten/proeven/studio-figuren-2026-11-23/uitslag.md`); anders zin 6 wordt "The knees still work, and the list shows each joint it placed." Zin 3: hoe je een AI-figuur een rig geeft laten we buiten dit filmpje; wie geen rig heeft, krijgt script 5 van week 48 (presets). Geen naam van een AI-dienst noemen.

---

## 4. Te veel getallen in beeld? Het nieuwe schone zicht (alleen na 1.2.1 live)
Titel: A cleaner way to check your joints before 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 4A | Too many numbers on your screen? | Too many numbers? | figuur met Labels All: alle bogen en getallen tegelijk (opname, 1.2.1) |
| 4B | Can't see which part hits first? | Which part hits? | zelfde beeld, muis zoekt |
| 2 | Click Joints Pro 1.2.1 shows only the joint you select, with its name. | Only what you select | klik op de linkerelleboog, de rest van de labels valt weg |
| 3 | You see its arc and its range, and the rest of the figure stays clean. | Clean figure | boog en bereik van de elleboog |
| 4 | Drag the Bend slider past the stop, and the whole part turns red. | Whole part red | elleboog voorbij de stop, onderarm rood (geen knie) |
| 5 | Want every joint at once? Set Labels to All, like the old view. | Labels: All | keuze Selected, All, None in het paneel |
| 6 | Or set Labels to None when you just want to look at your model. | Labels: None | figuur zonder labels |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: `platformen/blender/pro-1.2.1.md`, releasenotes 1.2.1: "new Labels setting in Figure joints (Selected, All or None). Selected is the new default: only the joint you select shows its arc and range, with its name. Set Labels to All for the old view, or None for a clean viewport" en "On a figure, past the end stop the whole moving part turns red". **Let op:** dit script staat buiten de twee vaste bronnen en mag pas als 1.2.1 de zip op Gumroad is (stand: `pro-1.2.1.md`, uitgave na Daans ja). Zolang Gumroad 1.2.0 heeft: dit script niet plaatsen, een koper zou het niet terugzien. Het rode deel geldt alleen op een figuur, niet op een los scharnier.

---

## 5. Voeten die niet bewegen? De enkels erbij
Titel: Add ankle joints to your 3D printed figure 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 5A | Does your figure stand on stiff feet? | Stiff feet? | figuur in delen, de voet vast aan het onderbeen (nieuw) |
| 5B | Forgot the ankles on your figure? | No ankles? | lijst van Figure from rig zonder enkels |
| 2 | Figure from rig gives shoulders, elbows, hips, knees and the neck by default. | Five body parts | lijst na één klik |
| 3 | For the ankles too, press More bones, right under Figure from rig. | More bones | klik op "More bones (ankles too)" |
| 4 | You find it in the N panel, under Click Joints, in Figure joints. | Where to find it | N-paneel open, pad in beeld |
| 5 | Select the rigged mesh first, then press it, and the ankles join the list. | Ankles in the list | lijst met Left ankle en Right ankle |
| 6 | No rig? There is an Ankle preset: put the 3D cursor on the ankle. | Ankle preset | cursor op de enkel, klik op Ankle |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2 en 3: "a joint at every shoulder, elbow, hip, knee and neck" en "Ankles via More bones" (gumroad-1.1.md). Zin 6: "Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle ... Place the 3D cursor and click the body part." Zin 4 en 5: "N panel › Click Joints › Figure joints › Figure from rig (or More bones (ankles too)). Select the rigged mesh first." (`platformen/blender/superhive/where-to-find-it.md`, gekeurde winkeltekst). **Let op:** welk soort gewricht de enkel krijgt en hoe ver hij buigt staat niet in de bronnen: niet uitspreken, de opname laat het zien. Werkt More bones niet op de gekozen figuur (te dunne enkel, zie script 2), dan een andere figuur kiezen; niet tonen wat niet lukt. Ook de namen "Left ankle"/"Right ankle" zijn GOK: neem over wat de lijst echt zegt.

---

## 6. Gewricht geweigerd? Zo lees je waarom
Titel: Why a joint won't place on your 3D print model 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Is a joint missing, with no reason? | Missing joint? | figuur met één gewricht minder in de lijst (nieuw) |
| 6B | Still finding bad joints after printing? | After printing? | mislukte print-tekening of tekst, geen nep-foto (nieuw) |
| 2 | Click Joints Pro only places a joint when the fit is good. | Only a good fit | gewricht verschijnt |
| 3 | When it is placed, the seam turns green, so you know it fits. | Green seam | inzoomen op de groene naad |
| 4 | Ball joints get a fit colour too, right around the cut. | Fit colour | ring rond de kogel |
| 5 | Two joints too close together? It refuses them, with a clear message. | Too close | melding in beeld (opname, nieuw) |
| 6 | And when a joint does not fit, the list tells you why and what to try. | Why, and what to try | regel in de lijst met reden |
| 7 | So you fix it in Blender, not after a failed print. | Fix it first | figuur, groene naden |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2 en 3: "Green fit band. A joint is only placed when the fit is good; the seam turns green." (Pro 1.0, in gumroad-1.1.md samengevat als "green fit band"). Zin 4: "ball joints with a fit colour". Zin 5: "spacing checks" (gumroad-1.1.md), uitgelegd in de Pro 1.0-tekst: "hinges and ball joints too close together are refused with a clear message". Zin 6: "Honest when it can not ...". **Let op:** zin 7 belooft niet dat de print dan lukt, alleen dat je de fout eerder ziet; zo laten. De echte meldtekst van de spacing check in beeld opnemen en niet uitspreken (die ken ik niet letterlijk).

---

## Volgorde voorstel (geld eerst)
6 en 1 eerst: die laten zien wat Pro je bespaart (minder mislukte prints, minder klikwerk) en raken de grootste groep, iedereen die al print. Dan 3 (AI-figuren: grote groep die nu instroomt), 2, 5, en 4 pas als 1.2.1 op Gumroad staat. De Regisseur kiest.
