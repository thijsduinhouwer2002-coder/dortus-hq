# Zes Short-scripts Click Joints Pro, week 49 (30 nov tot 6 dec 2026)

**Stand: akkoord, Daan 23 nov** (`marketing/keuring/2026-11-23-scripts-week-49-daan.md` en `-herkeuring-daan.md`). Script 4 pas als 1.2.1 of nieuwer op Gumroad staat.

Door Sanne, 23 nov 2026. Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL. Zelfde bouw als `week-48-click-joints.md` (zin 1 = hook A of B, max 7 woorden, vraag over het probleem van de kijker; daarna zinnen van 11 tot 16 woorden, 4 tot 6 s; printzin altijd; "Voice: AI text to speech (Kokoro)" in de beschrijving). Bronnen: `platformen/blender-2/gumroad-1.1.md` en `platformen/blender/pro-1.2.0.md`; script 4 rust ook op `platformen/blender/pro-1.2.1.md` (zie daar).

## Wat ik meenam uit de keuringen van 23 nov
- **Geen knie in beeld als hoofdzaak** (B3 stem-Short, B1 Daan knie-hook): vier knie-Shorts in een week is genoeg. Waar een buigend deel nodig is, neem ik de elleboog.
- **Kop korter dan de gesproken vraag** (C1), zodat hij niet twee keer letterlijk staat.
- **Getallen**: in de kop als cijfer ("150 mm"), uitgeschreven alleen in het json-veld `uitspraak` ("one hundred fifty millimetres").
- **Hook moet als vraag klinken** (A4 Daan): elke hook eindigt op een vraagteken en begint waar het kan met "Is", "Does" of "Still", zodat Kokoro de toon laat stijgen. Klinkt hij toch vlak, neem de B-versie.
- Nieuwe onderwerpen: geen enkel script hieronder staat al in de wachtrij of in week 48 (knie, Fit test, splitsen, scharnier of kogel, monster, Mixamo zijn al bezet).

---

## 1. Figuur nog in één stuk? Eén knop maakt delen met gewrichten
Titel: Turn your rigged figure into printable parts in one click 🔥 | Blender

*Herzien 23 nov na keuring Daan (moet 1 en 3): de Pro-reden is Figure from rig, exporteren is het gevolg en zit ook in de gratis Click Joints. Beeld: de robot van studio-2, niet het mensfiguur van studio-1.*

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Still cutting your figure into parts yourself? | Cutting it yourself? | robot van studio-2 in één stuk in Blender, muis met een boolean-blok bij de schouder (nieuw) |
| 1B | Is your figure still one solid piece? | One solid piece? | robot van studio-2 in één stuk, draait rond (nieuw) |
| 2 | One button, Figure from rig, cuts this robot into parts, each with its own joint. | One button | klik op Figure from rig, de delen verschijnen (opname studio-2) |
| 3 | It reads the rig you already made: shoulders, elbows, hips, knees and the neck. | From your own rig | lijst van Figure from rig, gewricht voor gewricht |
| 4 | Elbows and knees get a hinge with an end stop, the rest a ball joint. | Hinge or ball | inzoomen op een elleboogscharnier en een schouderkogel |
| 5 | Then step three, Fit and export, writes every part as its own file. | Step 3 | paneel "3 Fit and export", klik, map met de bestanden |
| 6 | Exporting is in the free Click Joints too. The one-click figure is Pro. | One click is Pro | delen van de robot apart naast elkaar |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render van de robot in delen (studio-2) |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2, 3 en 4: "press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint" en "Figure from rig reads the bones you made" (gumroad-1.1.md). Zin 5: knop "3 Fit and export" en één bestand per deel (`paneel.py` r. 119, `exporteer.py`). Zin 6: exporteren zit in de gratis bestanden `exporteer.py` en `paneel.py` (keuring Daan A1, GEZIEN in de code); Figure from rig zit in `betaald/`. **Let op:** geen aantal delen uitgesproken: de robot gaf lokaal 9 gewrichten en in CI soms 8 (`commercie/filmpjes/studio/LEESMIJ.md`). Wil de Regisseur een getal in de kop, dan het getal uit de eigen opname. Toont de opname geen nek of mist een gewricht, dan wordt zin 3 "It reads the rig you already made, and lists every joint it placed." Geen slicer-naam noemen of tonen.

---

## 2. Te kleine figuur? Dan past er geen scharnier
Titel: Why your small 3D printed figure can't have joints 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Is your figure too small for joints? | Too small? | dunne arm met een scharnier dat er niet in past (nieuw, render) |
| 2B | Arms too thin for a hinge? | Arms too thin? | zelfde beeld, liniaal ernaast |
| 2 | A hinge needs room: a pin, a wall around it, and a gap. | A hinge needs room | doorsnede van een elleboog |
| 3 | On a realistic figure at 150 millimetres, the arms are simply too thin. | 150 mm: too thin | figuur op 150 mm, arm in beeld |
| 4 | Click Joints Pro does not force it. The list tells you why it skipped. | The list says why | lijst met een overgeslagen gewricht en reden |
| 5 | Our tip: scale the figure to about 200 millimetres or more first. | 200 mm or more | schaal in Blender, maat in beeld |
| 6 | It also works best when the arms and legs stand apart from the body. | Arms and legs apart | figuur in A-pose |
| 7 | Then press Figure from rig again, and check the list for every joint. | Check again | klik, lijst vult zich |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3, 5 en 6 uit "Good to know": "Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so." Zin 4: "Honest when it can not. A joint that does not fit is skipped, and the list tells you why and what to try." **Let op:** dat het op 200 mm bij dezelfde figuur wél lukt is GOK; de Regisseur neemt beide maten op met dezelfde figuur en toont alleen wat echt gebeurt. Lukt 200 mm niet, dan zin 7 weg en eindigen op zin 6. Hook 2B is de kan van Daan (23 nov). `uitspraak` zin 3: "one hundred fifty millimetres", zin 5: "two hundred millimetres".

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

## 6. Goed, krap of te dun? Zo lees je de passing
Titel: Check every joint's fit before you 3D print 🔥 | Blender

*Herzien 23 nov na keuring Daan (moet 2): een krap gewricht wordt wel gesneden, alleen te dun niet.* *Neem 6B als eerste versie (kan Daan bij de herkeuring), 6A als tweede.*

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Is a joint missing, with no reason? | Missing joint? | figuur met één gewricht minder in de lijst (nieuw) |
| 6B | Still finding bad joints after printing? | After printing? | mislukte print-tekening of tekst, geen nep-foto (nieuw) |
| 2 | Click Joints Pro checks the fit of every joint before you print. | Fit check | gewricht verschijnt met zijn kleur |
| 3 | Green is a good fit. Yellow is tight, but it is still cut. | Green, yellow | inzoomen op een groene en een gele naad, paneel met "Good fit" en "Tight: wall ... mm" |
| 4 | Red is too thin, so that joint is not cut at all. | Red: not cut | paneel met "Too thin" en het rode icoon |
| 5 | Two joints too close together? It refuses them, with a clear message. | Too close | melding in beeld (opname, nieuw) |
| 6 | And the list tells you why, and what to try instead. | Why, and what to try | regel in de lijst met reden |
| 7 | So you fix it in Blender, not after a failed print. | Fix it first | figuur na de fix, naden groen |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2, 3 en 4 uit de code: `passing.py` r. 137 tot 141 (wand onder 0,8 mm = rood, onder 1,5 mm = krap, anders groen) en r. 182 tot 189 (paneeltekst "Good fit", "Tight: wall ... mm", "Too thin: ..."); keuring Daan A2: Tight wordt gesneden, alleen rood niet. Zin 5: "spacing checks" (gumroad-1.1.md) en de Pro 1.0-tekst "too close together are refused with a clear message". Zin 6: "Honest when it can not ... the list tells you why and what to try". **Kleur:** "Yellow" klopt (herkeuring Daan 23 nov): (1.0, 0.823, 0.0) is lineair, op het scherm RGB 255, 234, 0. Geen GOK meer. De opname moet een groen en een krap gewricht tonen; lukt dat niet, dan wordt zin 3 "Green is a good fit, and the panel says so in words." Zin 7 belooft niet dat de print dan lukt, alleen dat je de fout eerder ziet. De echte meldtekst van de spacing check in beeld opnemen en niet uitspreken.

---

## Volgorde voorstel (geld eerst)
Volgorde: **6, 1, 3, 5, 2, 4** (4 pas als 1.2.1 op Gumroad staat). 6 en 1 eerst: die laten zien wat Pro je bespaart (minder mislukte prints, een hele figuur in één klik) en raken de grootste groep, iedereen die al print. Dan 3 (AI-figuren: grote groep die nu instroomt). 2, 3 en 6 gaan over wat niet lukt; daarom staan ze niet vlak na elkaar (kan 2 van Daan), met 1 en 5 ertussen. De Regisseur kiest.
