# Click Joints Pro 1.1 "Rig to Figure": winkeltekst en changelog (Ruben, 17 nov 2026, run 28)

Concept voor Daan. Nog niet plakken: eerst CI groen in 4.2, 5.2 en 5.3 op de tak, dan ja van Daan, dan zet de hoofdchat het op Gumroad (en Superhive na goedkeuring van Pro). Volgt de pagina-regels van 17 nov en `organisatie/lanceerlijst.md`: geen "clicks", "never", "all" of "print tested"; niemand van ons heeft het geprint. Elke zin hieronder heeft rechts in de tabel onderaan zijn toets.

## Kop en eerste regel (zoekwoord vooraan)
**Rig to printable figure: elbows and knees stop where your rig stops.**

Pick your rigged figure, press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint. Next to each joint you see how far it bends, in degrees, before you print.

## Wat je krijgt
- **Figure from rig.** One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. With "More bones", ankles on human figures become hinges too (Blender 5.2 and newer).
- **The end stop comes from your rig.** If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part.
- **Every range in one view.** A small degree arc at each joint with its number, and a list in the panel: name, type, range and where the range came from (from rig, mirror or preset).
- **Honest when it can not.** A joint that does not fit is skipped, and the list tells you why and what to try (for example: "no room on this 38 mm bone for a ball joint next to the knee, place it by hand or give the knee a smaller range").
- **Recognises common bone names:** Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
- **No rig? Six presets:** Shoulder, Hip, Neck, Elbow, Knee and Ankle, each with its own icon. Place the 3D cursor and click the body part.
- **Everything from Pro 1.0:** hinge with end stop and pose slider, red where parts hit past the stop, green fit band, spacing checks, ball joints with a fit colour, split into parts, export to STL or 3MF.

## Nieuwe blokken (Bram 19 nov, opdracht hoofdchat punt 2; plan `platformen/blender/click-joints-plan-2026-11-19.md` regel 121 tot 125)
Onder "Wat je krijgt", in deze volgorde. Geen "holds a pose", geen "clicks", geen namen van andere add-ons.

**From rig to a figure that moves.**
> Rigged your character already? Then the hard part is done. Figure from rig reads the bones you made, puts a hinge at every elbow and knee and a ball joint at shoulders, hips and neck, and gives each hinge the same limit your rig has. One button, then you check the list.

**Split with anything. Make it move.**
> Already split your model into printable parts with another tool? Keep those parts. Open one, put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge or a ball joint right there, with the clearance you set and the range in degrees. Splitting makes it fit on the bed. Click Joints makes it move.

**Why not a ball joint by hand?**
> You can. A sphere, a boolean and some offset get you a joint. What you only find out after the print is that the knee bends backwards, the wall next to the socket is 0.4 mm thin, or the ball is stuck. Click Joints shows all three before you print: an end stop on every hinge, the wall and clearance as a number, and the range in degrees.

Toetsen: "same limit your rig has" = `rig.py` (Limit Rotation, 30 tot 150, anders gespiegeld of preset; de tekst zegt "the same limit", dus geldt voor botten met grens; de lijst toont de rest). "wall ... as a number" = paneel Fit (wand en speling in mm, `architectuur.md`). "Open one, put the 3D cursor" = elk los onderdeel is een eigen mesh; Place joint snijdt alleen het lid bij de cursor (0.1.1, `toetsen_een_lid.py`).

## Goed om te weten
- Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so.
- On AI-made figures where the legs touch (trousers, tunic), hips are skipped with a reason; knees still work. Hips on such figures are planned for 1.2.
- Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which).
- Tested in Blender (4.2, 5.2 and 5.3) on a MakeHuman figure, a Rigify metarig and three AI-made figures. Not print tested by us: print a test joint first, every printer is different.
- Clearance 0.2 mm by default.
- Already bought Pro? Every 1.x update is free.
- Support: https://github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com

## Changelog 1.1.0
```
1.1.0 "Rig to Figure"
- New: Figure from rig. One button turns a rigged figure into printable parts: hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck.
- New: the end stop comes from Limit Rotation in your rig (30° to 150°); a side without a limit takes the other side.
- New: a degree arc and number at every joint, and a joint list with where each range came from.
- New: six body-part presets with icons for figures without a rig.
- New: recognises Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz bone names.
- Fixed: a hinge on a one-piece figure no longer leaves the rest of the limb behind as a loose piece.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```

## Onderschrift winkelplaatje (Daan, 17 nov)
`One button. Every joint. How far it bends.` Alleen als onderschrift op het plaatje, niet in de add-on (Daan 19 nov kan 3: geen "click", er is nog geen print die klikt).

## Prijs (besluit, ja van Thijs 19 nov)
$19, Supporter $24 (zelfde download), Studio $59. De hoofdchat zet het op Gumroad bij het uitbrengen van 1.1.0. Superhive blijft tot na 2 dec zoals het is (Cyber Sale 35%: $19 wordt $12,35).

## Toetsen achter elke zin
| Zin | Toets (e2e, CI op de tak) |
|---|---|
| Figure from rig, hinges en ball joints op de mens | `toetsen_mens.py` (5.x: beide schouders en heupen minstens ±15, knieën en ellebogen from rig en mirror) |
| Stop uit Limit Rotation, 30 tot 150 | `toetsen_vrije_stop.py`, `toetsen_rig.py` |
| Mirrored | `toetsen_rig.py`, `toetsen_meshy_rig.py` |
| Elleboog haalt de rig-stop | `toetsen_zwaai.py` (115 en 90 gemeten) |
| Reden bij overslaan | `toetsen_meshy_rig.py`, `toetsen_rig_armen.py` |
| Botnamen | `toetsen_rig.py` (namen), `toetsen_mens.py` met `CJ_RIG_NAMEN=arp` |
| Zes presets met icoon | `toetsen_figuur.py` |
| Rigify metarig | `toetsen_rigify.py` |
| AI-figuren, knieën ja, heupen met reden | `toetsen_meshy_rig.py`, `toetsen_meshy_voet.py` |
| 4.2 soms met de hand | `toetsen_rig_armen.py` (4.2: minstens 4 van 8, elk met reden) |
| Losse stuk opgelost | `toetsen_meshy_voet.py` (oude code FOUT) |
