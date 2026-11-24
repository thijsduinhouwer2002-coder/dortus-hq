# Click Joints Pro 1.1.0 op Gumroad: alles klaar voor de hoofdchat (Bram, 19 nov 2026 ±16:20 UTC)

Opdracht hoofdchat 19 nov 14:00 NL, punt 1: zip, releasenotes en nieuwe Gumroad-tekst klaarzetten. De hoofdchat zet hem op Gumroad en zet daar tegelijk de prijs (ja van Thijs 19 nov).

## 1. De zip
- Uit e2e-run 44545370400 op main (commit f727466), groen in Blender 4.2.23, 5.2.3 en 5.3.0 (GEZIEN, Actions-API). Daan akkoord ja op die run: `platformen/blender-2/keuring/2026-11-19-pro-1.1-plaatje-19-herkeuring-3-daan.md`.
- Ophalen: uitgave-run 44563401805 van `click-joints-pro-uitgave.yml` (groen, GEZIEN), https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/44563401805 . sha256 `bcc14122a1b4e599288cc3fe0f6ce3d069bddbec94f042beb362b03b5296a324`. Artefact verloopt zo 22 nov 16:12 UTC; daarna de uitgave-workflow opnieuw starten met run_id 44545370400. Artefact `click-joints-pro-zip-1.1.0` (149 kB), bestand `click_joints_pro-1.1.0.zip`. Niet openbaar (besluit Thijs 15 nov).
- Release met de zes winkelplaatjes en SHA256SUMS: tag `click-joints-pro-v1.1.0`.
- Op Gumroad: het bestand `click_joints_pro-1.0.2.zip` vervangen door `click_joints_pro-1.1.0.zip`. Kopers van 1.0 krijgen hem zo gratis (de tekst belooft dat).

## 2. Prijs (ja van Thijs 19 nov)
| Versie | Prijs | Download |
|---|---|---|
| Personal | $19 | zip 1.1.0 |
| Supporter (same download, supports development) | $24 | zelfde zip |
| Studio (up to 5 people) | $59 | zelfde zip |

## 3. Samenvatting (veld "summary", één regel)
Rig to printable figure: elbows and knees stop where your rig stops.

## 4. Beschrijving (plakken, in deze volgorde)

**Rig to printable figure: elbows and knees stop where your rig stops.**

Pick your rigged figure, press one button, and Click Joints Pro cuts it into printable parts with a joint at every shoulder, elbow, hip, knee and neck. Elbows and knees get a hinge with an end stop; shoulders, hips and neck get a ball joint. Next to each joint you see how far it bends, in degrees, before you print.

**From rig to a figure that moves.**
Rigged your character already? Then the hard part is done. Figure from rig reads the bones you made, puts a hinge at every elbow and knee and a ball joint at shoulders, hips and neck, and gives each hinge the limit your rig sets, where it sets one. One button, then you check the list.

**Split with anything. Make it move.**
Already split your model into printable parts with another tool? Keep those parts. Open one, put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge or a ball joint right there, with the clearance you set and the range in degrees. Splitting makes it fit on the bed. Click Joints makes it move.

**Why not a ball joint by hand?**
You can. A sphere, a boolean and some offset get you a joint. What you only find out after the print is that the knee bends backwards, the wall next to the socket is 0.4 mm thin, or the ball is stuck. Click Joints shows all three before you print: an end stop on every hinge, the wall and clearance as a number, and the range in degrees.

**What you get**
- Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints.
- The end stop comes from your rig. If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part.
- Every range in one view. A small degree arc at each joint with its number, and a list in the panel: name, type, range and where the range came from (from rig, mirror or preset).
- Honest when it can not. A joint that does not fit is skipped, and the list tells you why and what to try.
- Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
- No rig? Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle, each with its own icon. Place the 3D cursor and click the body part.
- Everything from Pro 1.0: hinge with end stop and pose slider, red where parts hit past the stop, green fit band, spacing checks, ball joints with a fit colour, split into parts, export to STL or 3MF.

**Good to know**
- Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so.
- On AI-made figures where the legs touch (trousers, tunic), hips are skipped with a reason; knees still work.
- Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which).
- Tested in Blender 4.2, 5.2 and 5.3 on a MakeHuman figure, a Rigify metarig and three AI-made figures. Not print tested by us yet: print a test joint first, every printer is different.
- Clearance 0.2 mm by default.
- Already bought Pro? 1.1 is a free update: download it again from your Gumroad library.
- Support: https://github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com

**Versions**
Personal is for one person. Supporter is the same download and helps us keep building. Studio is for a team of up to 5 people.

## 5. Releasenotes (bij de update op Gumroad, of als bericht aan bestaande kopers)
```
Click Joints Pro 1.1.0 "Rig to Figure"
- New: Figure from rig. One button turns a rigged figure into printable parts: hinges with an end stop at elbows and knees, ball joints at shoulders, hips and neck.
- New: the end stop comes from Limit Rotation in your rig (30° to 150°); a side without a limit takes the other side.
- New: a degree arc and number at every joint, and a joint list with where each range came from.
- New: six body-part presets with icons for figures without a rig.
- New: recognises Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, Biped and Daz bone names.
- Fixed: a hinge on a one-piece figure no longer leaves the rest of the limb behind as a loose piece.
- Tested on Blender 4.2 LTS, 5.2 LTS and 5.3.
```
Een bericht aan bestaande kopers via Gumroad gaat naar buiten: alleen na de keuring van de tekst door een ander, en de hoofdchat verstuurt.

## 6. Omslag en plaatjes
Uit de release `click-joints-pro-v1.1.0`, in deze volgorde: `1-figuur-uit-rig.png` (nieuwe eerste omslag, Daan ja), `2-poster-3.png`, `3-knie-met-boog.png`, `4-rood-voorbij-de-stop.png`, `5-kogel-passing.png`, `6-kogel-rood.png`. De oude omslag met "click" en "Pro on Superhive" kan dan weg (open punt op het bord).

## Wat anders is dan de gekeurde winkeltekst (`winkeltekst-1.1.md`)
- Daans kan 1 verwerkt: "the same limit your rig has" werd "the limit your rig sets, where it sets one".
- "AI-made figures" blijft: dat gaat over wat de koper erin stopt (zoals Cleave "Made for Meshy, Tripo"), niet over hoe wij het maakten; er staat geen "built with the help of AI tools" meer in (opdracht hoofdchat). Als de hoofdchat dat anders leest: vervang door "figures". De regel "Hips on such figures are planned for 1.2" weggelaten: geen belofte zonder plan.
- "Not print tested by us" blijft eerlijk staan (met "yet"); nergens "clicks" of "holds a pose".
- Blok "Versions" erbij voor de drie prijzen. "from rig, mirror or preset" blijft zo: de lijst in de add-on zegt precies dat (plaatje 1, GEZIEN).
