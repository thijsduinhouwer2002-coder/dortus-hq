# Zes Short-scripts Click Joints Pro, week 48 (23 tot 29 nov 2026)

Door Sanne, 23 nov 2026. Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL: 6 scripts per week voor Chris en de Regisseur, zinnen van 4 tot 6 s, elk klopt met `platformen/blender-2/gumroad-1.1.md` en `platformen/blender/pro-1.2.0.md`, recept v2 en v3 (`platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md`).

## Zo zijn ze gebouwd
- **Zin 1 is de hook** (recept v3): een vraag aan de kijker over zijn probleem, max 7 woorden, gesproken én als grote kop vanaf beeld 1, met het probleem in beeld. Per script twee hooks, A en B; de rest is gelijk, en het hook-beeld ook (dan meet je alleen de woorden). Nooit de productnaam in zin 1.
- **Zin 2 tot het eind**: 11 tot 16 woorden per zin, dat is 4 tot 6 s bij Kokoro op snelheid 0,95 (GOK: ±2,7 woorden per seconde, gemeten aan proef-1: 15 zinnen, 58,4 s). De workflow meet het echt.
- **Recept v2**: eerste beeld na de hook = het mooie eindresultaat (gekleurd figuur, uit studio-1 zodra die er is), echt Blender-scherm met bewegende muis, een les die je kunt nadoen, Click Joints als gereedschap.
- **Altijd** de printzin: "Measured in Blender, not print tested by us yet. Print a test joint first." Geen vermelding van AI of de stem in titel of beschrijving; alleen het vinkje "Altered content" in YouTube Studio (besluit Thijs 23 nov 20:28 NL, vervangt de oude regel "Voice: AI text to speech" in de beschrijving).
- Geen prijs, geen korting, geen "holds a pose", geen "clicks". Alleen wat in de twee bronnen staat. Waar een zin op een bron rust, staat het bij "Bron".
- Vorm voor de stem-machine: elke zin kan zo een scène in een json van `commercie/filmpjes/stem/` worden (tekst, label, kop). Het beeld dat ik voorstel moet de Regisseur nog opnemen of uit een bestaande opname halen; "nieuw" betekent dat er nog geen opname van is.

---

## 1. Monster met ellebogen die goed buigen (Pro 1.2.0, Orc van Quaternius)
Titel: Make a rigged monster poseable for 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Does your monster's elbow bend upward? | Elbow bends upward? | elleboog van de Orc die omhoog buigt in een losse rig (nieuw) |
| 1B | Still cutting joints into monsters by hand? | Joints by hand? | Orc in Blender met een boolean-bol op de elleboog (nieuw) |
| 2 | Here's a rigged orc in Blender, and we want to print it in parts. | A rigged orc | de Orc gekleurd, in een pose (studio-1) |
| 3 | Select the character and press Figure from rig in Click Joints Pro. | One button | klik op Figure from rig |
| 4 | It reads the bones you made and puts a joint where they bend. | Reads your rig | het skelet licht op, dan de delen |
| 5 | On this orc that gives four joints, and the list shows each one. | Four joints | de lijst in het paneel |
| 6 | Some rigs make the elbow bend upward. Version 1.2 now turns it forward. | Elbows bend forward | elleboog die naar voren buigt, Bend-schuif |
| 7 | That fix needs Blender 4.5 or newer. On older versions, place the elbow by hand. | Blender 4.5 or newer | tekst in beeld |
| 8 | Drag the Bend slider to see how far each elbow goes before you print. | Check the bend | schuif, boog met graden |
| 9 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render van de delen |
| 10 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3, 4 en 10 uit gumroad-1.1.md ("Figure from rig reads the bones you made", samenvatting). Zin 5: Orc 4 gewrichten (pro-1.2.0.md, GEZIEN door Daan in Blender 5.3.0). Zin 6 en 7: releasenotes 1.2.0 ("elbow now bends forward. Needs Blender 4.5 or newer; on 4.2 to 4.4 it still asks you to place the elbow by hand"). Zin 8: "Next to each joint you see how far it bends, in degrees". **Let op:** welke vier gewrichten de Orc krijgt staat niet in pro-1.2.0.md; zeg dus "four joints" en laat in beeld zien welke. Zeg niet "every Quaternius character".

---

## 2. Fit test strip: welke speling past bij jouw printer (Pro 1.2.0)
Titel: Find the right joint clearance for your 3D printer 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Not sure which gap your printer needs? | Which gap fits? | kogel die klem zit naast een kogel die rammelt (render, nieuw) |
| 2B | Testing the fit with a whole figure? | Testing with a whole figure? | hele figuur op een printbed in Blender (nieuw) |
| 2 | Before you print a figure, print this small fit test strip first. | Print this first | de strip in Blender |
| 3 | In Click Joints Pro, press Fit test: ball, or Fit test: hinge. | Two buttons | klik op de knop bovenaan het Pro-deel |
| 4 | You get five joints, from zero point one to zero point three millimetres clearance. | 0.10 to 0.30 mm | strip in beeld, inzoomen |
| 5 | Each joint has its number on it, so you know which one is which. | Every joint numbered | nummer op elk gewricht |
| 6 | Print the strip, try each joint, and pick the gap that works for you. | Pick your gap | hand-tekening of tekst, geen nep-print |
| 7 | Then set that clearance before you cut the joints in your figure. | Use it on your figure | Clearance-veld, 0.20 standaard |
| 8 | We have not print tested it ourselves yet. Every printer is different. | Every printer is different | tekst in beeld |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2 tot 6 uit de releasenotes 1.2.0 ("Print this first: five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer") en de knopnamen "Fit test: ball" en "Fit test: hinge" (pro-1.2.0.md). Zin 7: "Clearance 0.2 mm by default" (gumroad-1.1.md). Zin 8: "Not print tested by us yet ... every printer is different". **Let op:** geen foto van een geprinte strip tonen, die hebben we niet. Uitspraak: schrijf in de json `uitspraak` met "zero point one" zoals hier, en in de kop "0.10 to 0.30 mm".

---

## 3. Al in delen gesplitst? Zo gaat het bewegen
Titel: Split your model, then make it move for 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 3A | Split your model, but nothing moves? | Split, but stiff? | losse delen die stijf aan elkaar zitten (nieuw) |
| 3B | Your printed parts fit, but can't bend? | Fits, but can't bend? | zelfde beeld |
| 2 | Already split your model into parts with another tool? Keep those parts. | Keep your parts | figuur in losse delen |
| 3 | Open one part and put the 3D cursor on the knee or the elbow. | Cursor on the knee | 3D-cursor op de knie zetten |
| 4 | Click Joints Pro cuts a hinge or a ball joint right there. | A joint right there | klik, het gewricht verschijnt |
| 5 | You set the clearance, and you see the range in degrees. | Clearance and range | paneel met Clearance en de boog |
| 6 | Elbows and knees get a hinge with an end stop, so they stop bending. | Hinge with end stop | Bend-schuif tot de stop |
| 7 | Go past the stop and the parts that hit turn red, before you print. | Red means it hits | rood voorbij de stop (bestaande opname knie_rood) |
| 8 | Splitting makes it fit on the bed. Click Joints makes it move. | Fit, then move | delen op het bed, dan buigen |
| 9 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 10 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2 tot 5 en 8 bijna letterlijk uit "Split with anything. Make it move." (gumroad-1.1.md). Zin 6 en 7: "Elbows and knees get a hinge with an end stop" en "red where parts hit past the stop" (Pro 1.0 in gumroad-1.1.md). Geen naam van het andere gereedschap noemen.

---

## 4. Kogelgewricht met de hand? Dit zie je pas na het printen
Titel: Why your 3D printed ball joint fails (and how to see it first) 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 4A | Still making ball joints by hand? | Ball joints by hand? | een bol plus boolean op een schouder in Blender (nieuw) |
| 4B | Socket wall too thin? | Wall too thin? | doorsnede met een dunne wand, rood omcirkeld (nieuw) |
| 2 | You can. A sphere, a boolean and some offset get you a joint. | Sphere plus boolean | de handmatige stappen kort |
| 3 | But some problems you only find out after the print is done. | Found out too late | tekst in beeld |
| 4 | The knee bends backwards, the wall is too thin, or the ball is stuck. | Three problems | drie kleine plaatjes na elkaar |
| 5 | Click Joints Pro shows all three in Blender, before you print. | See it first | paneel |
| 6 | Every hinge gets an end stop, so the knee can't bend backwards. | End stop | knie tot de stop |
| 7 | The wall and the clearance show as a number next to the joint. | Wall and gap as numbers | paneel met wand en speling, groen of oranje |
| 8 | And every joint shows its range in degrees, with a small arc. | Range in degrees | de boog met getal |
| 9 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 10 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: hele script uit het blok "Why not a ball joint by hand?" in gumroad-1.1.md ("A sphere, a boolean and some offset get you a joint ... the knee bends backwards, the wall next to the socket is 0.4 mm thin, or the ball is stuck. Click Joints shows all three before you print"). Zin 8: "A small degree arc at each joint with its number". **Let op:** hook 4B vraagt naar de wand; zin 7 moet dan in beeld echt een wandgetal tonen. Het getal 0,4 mm niet uitspreken als meting van ons, het is een voorbeeld uit de tekst.

---

## 5. Geen rig? Toch een knie die stopt
Titel: Add a knee joint for 3D printing, no rig needed 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 5A | No rig on your character? | No rig? | figuur zonder skelet, de knie buigt niet (nieuw) |
| 5B | A knee joint without a rig? | Knee without a rig? | zelfde beeld |
| 2 | No problem. Click Joints Pro has six presets for the main body parts. | Six presets | de zes knoppen met icoon |
| 3 | Shoulder, hip, neck, elbow, knee and ankle, each with its own icon. | One per body part | inzoomen op de iconen |
| 4 | Put the 3D cursor right on the knee of your figure, where it should bend. | Cursor on the knee | cursor zetten |
| 5 | Then click Knee, and it cuts a hinge with an end stop. | Click Knee | klik, scharnier verschijnt |
| 6 | Shoulders, hips and the neck get a ball joint instead of a hinge. | Ball joints too | klik op Shoulder, kogel |
| 7 | Drag the Bend slider and see how far it goes, in degrees. | Check the range | schuif en boog |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 2, 3 en 4 uit "No rig? Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle, each with its own icon. Place the 3D cursor and click the body part." Zin 5 en 6: "Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint". Zin 7: graden naast elk gewricht. **Let op:** zonder rig komt de stop uit de preset per lichaamsdeel, niet uit de rig; zeg daarom in dit script niet "where your rig stops" behalve op de eindkaart (die zin hoort bij het product). Wil de Regisseur dat strak: eindkaart-zin dan "Hinges with an end stop, before you print."

---

## 6. Mixamo, Rigify of Daz: de stop komt uit je eigen rig
Titel: Your Mixamo character, ready for 3D printing 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Want to print your Mixamo character? | Mixamo to print? | Mixamo-figuur in Blender, in één stuk (nieuw) |
| 6B | Does your rig use different bone names? | Different bone names? | Outliner met mixamorig:LeftForeArm en andere namen (nieuw) |
| 2 | Click Joints Pro knows the bone names of the common rigs. | Knows your rig | lijst met namen |
| 3 | Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz. | Eight rig types | de namen in beeld, één voor één |
| 4 | Press Figure from rig, and it finds the elbows, knees, shoulders, hips and neck. | Finds every joint | klik, delen verschijnen |
| 5 | Does a bone have a Limit Rotation? Then the hinge stops at that angle. | Your limit, your stop | Limit Rotation in het Bone-paneel, dan de stop |
| 6 | No limit on one side? It takes the limit of the other side. | Mirrored | lijst: "mirror" |
| 7 | And when a joint does not fit, the list tells you why and what to try. | Honest list | regel in de lijst die zegt waarom |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3: "Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz." Zin 4: "a joint at every shoulder, elbow, hip, knee and neck". Zin 5 en 6: "If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored)." Zin 7: "A joint that does not fit is skipped, and the list tells you why and what to try." **Let op:** getest is alleen op MakeHuman, een Rigify-metarig en drie AI-figuren (gumroad-1.1.md, "Tested in ..."). Een echte Mixamo-figuur in beeld moet dus eerst door Olaf of de Regisseur getest zijn; lukt dat niet, neem dan hook 6B met de Rigify-metarig in beeld en laat "Mixamo" uit de titel. Licentie van de figuur nakijken (Mixamo-figuren hebben eigen voorwaarden).

---

## Volgorde voorstel (geld eerst)
1, 4 en 3 eerst: die laten het meeste zien van wat een koper krijgt en hebben het duidelijkste probleem in de hook. Dan 2 (nieuw in 1.2.0, geeft een reden om nu te kopen), 5 en 6 (6 pas na een test op een Mixamo-figuur). Dit is een voorstel; de Regisseur kiest.
