# Zes Short-scripts Click Joints, week 50 (7 tot 13 dec 2026)

Door Sanne, 23 nov 2026. Opdracht hoofdchat 23 nov ±12:05 en ±12:45 NL (recept v3: hook eerst). Zelfde bouw als week 48 en 49: zin 1 = hook A of B, max 7 woorden, een vraag over het probleem van de kijker, nooit de productnaam; daarna zinnen van 10 tot 16 woorden (4 tot 6 s); printzin altijd; "Voice: AI text to speech (Kokoro)" in de beschrijving; kop korter dan de gesproken vraag; getallen als cijfer in de kop en uitgeschreven alleen in het json-veld `uitspraak`. Bronnen: `platformen/blender-2/gumroad-1.1.md`, `platformen/blender/pro-1.2.0.md`, `platformen/blender/pro-1.2.2.md` en de code in `producten/blender-gewrichten/click_joints/` (regels genoemd per script).

**Stand: akkoord, Daan 23 nov, na moet M1 (script 5 zin 6)** (`marketing/keuring/2026-11-23-scripts-week-50-daan.md`). Script 3 pas als 1.2.2 op Gumroad staat.

## Wat anders is dan week 49
- **Drie tips die ook zonder Pro waarde hebben** (script 2, 4 en 5), zoals de tip-reeks van Thijs vraagt: wie de tip bewaart, kent ons daarna. Script 2 en 4 laten knoppen uit de gratis Click Joints zien; dat zeggen ze eerlijk.
- **Geen knie, geen MakeHuman-figuur, geen studio-1.** Beeld: de robot van studio-2, de Orc van Quaternius (week 48) of een kaal blok.
- **Hooksoorten gewisseld** (recept v3 punt 3): probleem (1B, 2A, 3A, 4A, 5B), oude manier (5A), "al gedaan?" (1A, 6A, 6B).
- Nieuwe onderwerpen: niets hieronder staat al in week 48, week 49 of `marketing/wachtrij/` (daar al bezet: knie, graden, pose, schouderkogel, nek, scharnier of kogel, splitsen, buigen, fit test, schoon zicht, enkels, AI-figuren, te klein, passingkleuren, Mixamo, Rigify, Daz, monster).

---

## 1. Grenzen al in je rig? Dan is dat de eindstop
Titel: Your rig's bone limits become the joint's end stop 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 1A | Already set bone limits in your rig? | Bone limits set? | tab Bone Constraints, Limit Rotation op de onderarm van de robot (nieuw) |
| 1B | Does your printed elbow bend too far? | Bends too far? | elleboog van de robot die door de bovenarm buigt (render, nieuw) |
| 2 | Click Joints Pro reads Limit Rotation on the X axis, and makes it the stop. | Limit = stop | Limit Rotation X, min en max in beeld |
| 3 | Set it in Local Space, because only there is X the bending axis. | Local Space | keuzelijst Owner space op Local |
| 4 | No Limit Rotation on the bone? Then it reads the IK limits instead. | Or IK limits | tab Bone, Inverse Kinematics, Limit X |
| 5 | Limit only the left elbow? The right elbow takes the same stop, mirrored. | Mirrored | lijst: rechter elleboog met "mirror" |
| 6 | No limit at all? Then it takes a preset, and the list says so. | Or a preset | lijst met "preset" |
| 7 | The stop is rounded, and kept between 30 and 150 degrees. | 30° to 150° | boog met getal bij de elleboog |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render robot in delen |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` zin 7: "thirty and one hundred fifty degrees".
Bron: zin 2, 5, 6 en 7 uit "What you get": "If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part." en "where the range came from (from rig, mirror or preset)" (gumroad-1.1.md). Zin 3 en 4 uit de code: `betaald/rig.py` r. 95 tot 103 (alleen Limit Rotation met Limit X, niet uitgeschakeld en in LOCAL telt; anders de IK-grenzen op X; GEZIEN) en r. 9 tot 12 (de grootste kant wordt de eindstop, afgerond, 30 tot 150). **Let op:** de robot van studio-2 heeft misschien geen Limit Rotation: de Regisseur zet er zelf een op de linker elleboog en laat zien dat de lijst "from rig" zegt bij links en "mirror" bij rechts. Zegt de lijst iets anders, dan neem je over wat er staat en schrap je de zin die niet klopt. Geen preset-getal uitspreken.

---

## 2. Gat na een snede? Eerst waterdicht maken
Titel: Make your mesh watertight before you cut a joint 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 2A | Boolean cut leaves holes in your model? | Holes after a cut? | doorsnede van een deel met een open rand (nieuw, opname) |
| 2B | Is your mesh really watertight? | Watertight? | model met een open rand, rand rood omcirkeld (nieuw) |
| 2 | A clean cut needs a closed mesh: every edge with exactly two faces. | Two faces per edge | inzoomen op een open rand in Edit Mode |
| 3 | Click Joints has a Check mesh button that counts the edges that break this. | Check mesh | klik op Check mesh, melding met het aantal randen |
| 4 | On an open mesh it will not cut, and the panel tells you why. | It will not cut | paneel met "Mesh is not watertight" |
| 5 | Press Make watertight, and you get a closed copy made with a voxel remesh. | Make watertight | klik, nieuwe kopie verschijnt |
| 6 | Your original stays in the scene, hidden, so nothing is lost. | Original kept | Outliner met het verborgen origineel |
| 7 | Smaller voxels keep more detail. If it fails, try a larger voxel size. | Voxel size | veld "Voxel (mm)" in het paneel |
| 8 | Both buttons are in the free Click Joints, so you can try this today. | Free | paneel |
| 9 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 10 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron (code, gratis deel, GEZIEN): `gesloten.py` r. 55 tot 69 (Check mesh: "every edge has exactly 2 faces", melding met het aantal randen), r. 75 tot 76 ("Make a watertight copy with a voxel remesh. The original is kept, hidden"), r. 107 ("Try a larger voxel size"); `gewricht.py` r. 209 (snijden weigert op een open mesh); `paneel.py` r. 71 tot 76 (knoppen en "Mesh is not watertight"); `eigenschappen.py` r. 44 tot 46 (Voxel (mm), standaard 0,5). Zin 7 eerste helft is algemene Blender-kennis (voxel remesh gooit detail kleiner dan een voxel weg). **Let op:** de knoppen staan alleen in beeld als de add-on het model al als open heeft gemarkeerd (r. 71); neem op wat het paneel echt laat zien. Geen getal randen uitspreken, alleen in beeld. Niet laten denken dat Make watertight in Pro zit.

---

## 3. Kapotte delen na een boolean? Probeer Exact (alleen na 1.2.2 live)
Titel: Blender boolean leaves broken parts? Try this 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 3A | Boolean giving you broken, open parts? | Broken parts? | deel na een snede met een gat (opname, nieuw) |
| 3B | Did "no watertight parts" stop your joint? | Stopped by an error? | foutmelding "The cut gave no watertight parts" onderin Blender |
| 2 | Blender's fast boolean solver sometimes leaves a part that is not closed. | Fast solver | Boolean-modifier, solver in beeld |
| 3 | Exact is slower, and it is the one to try when that happens. | Try Exact | solver op Exact, deel dicht |
| 4 | Click Joints Pro 1.2.2 does that for you: it cuts once more with Exact. | Retries with Exact | snede, melding, deel dicht |
| 5 | In Figure from rig, a failed spot now tries the next spot on that bone. | Next spot | lijst die een gewricht alsnog plaatst |
| 6 | Still no luck? It stops cleanly, and the figure stays in one piece. | Clean stop | figuur heel, melding in beeld |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` zin 4: "one point two point two".
Bron: releasenotes 1.2.2 (akkoord Daan): "if a cut with the fast solver leaves a part that is not watertight, Click Joints Pro cuts once more with the Exact solver before giving up" en "when a cut fails at one spot, it now tries the next spot on that bone instead of skipping the joint" (`platformen/blender/pro-1.2.2.md`). Zin 6: stand punt 1 daar ("operator weigert, figuur heel, geen hulpresten"). Foutmelding 3B: `gewricht.py` r. 297. **Let op:** pas maken als 1.2.2 op Gumroad staat. Olaf zag op MakeHuman dat Exact niets oplost (A4, logboek 23 nov): de Regisseur moet een echt geval opnemen waar de tweede snede met Exact het deel wél dicht krijgt. Vind je dat niet, dan zin 4 en 5 weg en wordt het een gewone Blender-tip (zin 2, 3, dan 7 en 8). Niets zeggen over processors. In Blender 4.2 heet de snelle solver "Fast", in nieuwere versies anders: daarom zegt zin 2 "fast solver" zonder naam in de kop.

---

## 4. Print komt piepklein uit? Zo exporteer je in millimeter
Titel: 3D print tiny in your slicer? Fix the export scale 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 4A | Is your part tiny in the slicer? | Tiny print? | piepklein deel op een leeg printbed (nieuw, tekening, geen merk) |
| 4B | Exported parts at the wrong size? | Wrong size? | twee keer hetzelfde deel, een veel kleiner (nieuw) |
| 2 | An STL file has no unit. Most slicers read every number as millimetres. | STL has no unit | tekst in beeld |
| 3 | Blender works in metres by default, so 0.2 metres can arrive as 0.2 millimetres. | 0.2 m → 0.2 mm | Scene Properties, Units, Unit Scale 1 |
| 4 | Click Joints exports every joint part in millimetres, whatever your scene uses. | Always in mm | klik op exporteren |
| 5 | Pick STL or 3MF in the panel, and every part gets its own file. | STL or 3MF | keuze in het paneel, map met bestanden |
| 6 | Check one part's size before you slice and print the whole figure. | Check one part | maat van één deel in beeld (N-paneel, Dimensions) |
| 7 | This export is part of the free Click Joints, so you can try it today. | Free | paneel |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` zin 3: "zero point two metres can arrive as zero point two millimetres".
Bron: zin 4 en 5 uit de code (gratis deel, GEZIEN): `exporteer.py` r. 1 en 38 ("Write every visible joint part as an STL or 3MF file in millimeters"), r. 51 (schaal uit de scène-eenheid naar mm), r. 79 tot 80 (STL zonder scene unit, met eigen schaal); gumroad-1.1.md "export to STL or 3MF". Zin 2 en 3 zijn algemene kennis: STL bewaart geen eenheid, en de standaard STL-export van Blender schrijft Blender-eenheden. **Let op:** zin 3 is GOK tot de Regisseur hem echt ziet: exporteer een deel van 0,2 m met de gewone Blender-export (File, Export, STL, standaard) en meet het bestand na (een python-regel die de grootste maat in het STL leest is genoeg). Is het niet 0,2, dan zin 3 weg. Geen slicer-naam noemen of tonen; 4A als tekening.

---

## 5. Nog op Blender 4.2? Dan plaats je soms een elleboog zelf
Titel: Which Blender version for printable figure joints? 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 5A | Still on Blender 4.2 LTS? | Still on 4.2? | Blender 4.2 openingsscherm met versienummer (opname) |
| 5B | Elbow left out on your game character? | Elbow left out? | Orc van Quaternius in 4.2, lijst zonder elleboog (opname) |
| 2 | Click Joints Pro works in 4.2, and we test it in 4.2, 5.2 and 5.3. | Tested in 3 versions | drie versienummers naast elkaar |
| 3 | But on some rigs the elbow would bend upward, like on Quaternius characters. | Bends upward | Orc, elleboog omhoog gebogen (render) |
| 4 | In Blender 4.5 and newer, Figure from rig turns that elbow to bend forward. | 4.5+: forward | Orc in 5.3, elleboog buigt naar voren |
| 5 | In 4.2 to 4.4, the list asks you to place that elbow by hand. | 4.2: by hand | lijst in 4.2 met de vraag |
| 6 | It is quick: put the 3D cursor on the elbow, then click Elbow. | Cursor, then Elbow | cursor op de elleboog, preset Elbow |
| 7 | So 4.2 works fine, but 4.5 or newer saves you that step. | 4.5 saves a step | Orc in delen |
| 8 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render Orc in delen |
| 9 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

`uitspraak` zin 2: "four point two, five point two and five point three"; zin 4: "four point five"; zin 5: "four point two to four point four"; zin 7: "four point two" en "four point five".
Bron: releasenotes 1.2.0: "Figure from rig now places elbows on rigs where the elbow would otherwise bend upward (for example Quaternius characters). The elbow now bends forward. Needs Blender 4.5 or newer; on 4.2 to 4.4 it still asks you to place the elbow by hand." en "Tested on Blender 4.2 LTS, 5.2 LTS and 5.3" (pro-1.2.0.md). Zin 6: "Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle ... Place the 3D cursor and click the body part." (gumroad-1.1.md). Gumroad: "Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which)." **Let op:** "one click" in zin 6 klopt alleen als het preset in één klik het gewricht maakt; laat het in de opname zien, anders "That is quick:". Wat de lijst in 4.2 precies zegt: overnemen in beeld, niet uitspreken. CI heeft 4.2.23 en 5.3.0, dus beide opnames kunnen in Actions.

---

## 6. Rig uit VRoid, Character Creator of Auto-Rig Pro? Geen bot hernoemen
Titel: VRoid or Auto-Rig Pro rig to a printable figure 🔥 | Blender

| # | gesproken | kop (groot) | beeld |
|---|---|---|---|
| 6A | Made your character in VRoid? | VRoid character? | botlijst met J_Bip-namen in de Outliner (nieuw) |
| 6B | Rigged with Auto-Rig Pro? | Auto-Rig Pro? | botlijst met forearm_stretch.l en thigh_ref.l (nieuw) |
| 2 | Figure from rig reads bone names from many rigs, not only from Mixamo. | Many rigs | Outliner met botnamen |
| 3 | It knows Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz names. | Six more rigs | namen van de rigs onder elkaar |
| 4 | So you do not rename a single bone before you press the button. | No renaming | klik op Figure from rig |
| 5 | It finds the shoulders, elbows, hips, knees and neck, and lists each one. | Every joint listed | lijst vult zich |
| 6 | A joint that does not fit is skipped, and the list tells you why. | Skipped, with why | regel met reden |
| 7 | Measured in Blender, not print tested by us yet. Print a test joint first. | Print a test joint first | render |
| 8 | Click Joints Pro. Elbows and knees stop where your rig stops. | (eindkaart) | eindkaart |

Bron: zin 3: "Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz." (gumroad-1.1.md); code `betaald/rig.py` r. 33 tot 49 (J_Bip_L_UpperArm, CC_Base_L_Upperarm, Bip01 L Thigh, forearm_stretch.l, GEZIEN). Zin 5 en 6: gumroad-1.1.md. **Let op:** de namen zijn in de code getoetst, maar een hele figuur uit zo'n rig hebben wij nog niet in een filmpje gehad (getest is MakeHuman, Rigify en drie AI-figuren). Het beeld 6A en 6B mag een kale armature met die botnamen zijn; zin 4 en 5 alleen houden als de opname op een echte figuur met zo'n rig echt alle vijf soorten gewrichten toont. Lukt dat niet, dan zin 5 wordt "It finds the joints it knows, and lists each one." Alleen een model met een vrije licentie (CC0 of eigen werk), geen model uit de VRoid-hub van een ander. Merknamen alleen als "werkt met", geen logo's.

---

## Volgorde voorstel (geld eerst)
Volgorde: **1, 4, 6, 2, 5, 3** (3 pas als 1.2.2 op Gumroad staat). 1 eerst: wie zelf grenzen in zijn rig zet, is precies de koper van Figure from rig. 4 en 2 zijn tips die mensen bewaren (zoals de BlenderSecrets-video met 714 keer bewaard, hoofdchat 23 nov), dus bereik bij precies de 3D-printers; ze staan niet vlak na elkaar en hebben er een Pro-script tussen. 6 opent nieuwe groepen (VRoid, Auto-Rig Pro). 5 en 3 zijn kleiner. De Regisseur kiest.
