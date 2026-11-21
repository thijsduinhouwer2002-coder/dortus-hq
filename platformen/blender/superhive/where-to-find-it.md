# "Where to find it" in de Pro-tekst (Bram, 21 nov 2026 ±14:00 UTC)

Opdracht Afkijker 21 nov 13:10 NL: onder elke functie in "What you get" één regel "Where to find it", plus één regel bij installeren. Voorbeeld: Split 3D Print (`platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-split-3dprint.md`).
Keuring: Daan (skill keuren). Daarna zet de hoofdchat het live (inloggen). Prijs en de rest van de tekst blijven gelijk.

## Waar de namen vandaan komen (GEZIEN in de code van de live zip)
Pro 1.1.0 is gebouwd uit commit f727466 (`platformen/blender-2/gumroad-1.1.md`). Ik las de bestanden op die commit via de GitHub-API, en ze zijn gelijk aan main op deze punten:
- Tabblad in de zijbalk: `bl_category = "Click Joints"` (`paneel.py`, `betaald/figuur.py`).
- Paneel "Click Joints" met de stappen "1  Place", "2  Joint" (knop "Place joint"), "3  Fit and export" (knop "Export STL" of "Export 3MF") (`paneel.py`).
- Daaronder in hetzelfde paneel: "Place hinge, bends up to:" met 90°, 115°, 135° (`betaald/scharnier.py`), en bij een scharnierdeel het vak "Hinge" met "Show bend range" en de schuif "Bend" (`betaald/scharnier_boog.py`).
- Eigen paneel "Figure joints": knop "Figure from rig" (alleen als de mesh een armature heeft), knop "More bones (ankles too)", dan "Or put the 3D cursor on a joint, then:" met Shoulder, Elbow, Hip, Knee, Ankle, Neck, en daaronder de lijst (`betaald/figuur.py`).
- Overgeslagen gewrichten: melding "Skipped: ..." onderin het venster na Figure from rig (`betaald/rig.py` regel 758). **Niet in de lijst.** De live tekst zegt nu "the list tells you why"; dat klopt niet helemaal. Hieronder recht gezet.
- "Fit test" zit niet in 1.1.0, dus niet genoemd.

## Nieuwe regel bovenaan, direct onder de eerste alinea (Gumroad en Superhive)
**After installing:** press N in the 3D viewport and open the Click Joints tab.

## Nieuw blok "What you get" (vervangt het blok van nu, Gumroad en Superhive gelijk)

**What you get**
- Figure from rig. One button reads your armature. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. Ankles via "More bones".
  Where to find it: N panel › Click Joints › Figure joints › Figure from rig (or More bones (ankles too)). Select the rigged mesh first.
- The end stop comes from your rig. If a bone has a Limit Rotation constraint, the hinge stops at that angle (30° to 150°). No limit on one side? It takes the other side (mirrored). No limit at all: a preset per body part.
  Where to find it: your rig's Bone Constraints › Limit Rotation. Click Joints reads it when you press Figure from rig.
- Every range in one view. A small degree arc at each joint with its number, and a list in the panel: name, type, range and where the range came from (from rig, mirror or preset).
  Where to find it: the arcs in the 3D viewport; the list in N panel › Click Joints › Figure joints, under the buttons.
- Honest when it can not. A joint that does not fit is skipped, and Blender tells you which one and why.
  Where to find it: the "Skipped: ..." message at the bottom of the window after Figure from rig.
- Recognises common bone names: Rigify, Mixamo, Auto-Rig Pro, Unreal, Character Creator, VRoid, 3ds Max Biped and Daz.
  Where to find it: nothing to set; Figure from rig finds the bones by name.
- No rig? Six presets: Shoulder, Hip, Neck, Elbow, Knee and Ankle, each with its own icon. Place the 3D cursor and click the body part.
  Where to find it: N panel › Click Joints › Figure joints › "Or put the 3D cursor on a joint, then:".
- Everything from Pro 1.0: hinge with end stop and pose slider, red where parts hit past the stop, green fit band, spacing checks, ball joints with a fit colour, split into parts, export to STL or 3MF.
  Where to find it: N panel › Click Joints › Place hinge, bends up to: 90° 115° 135° (the Bend slider shows up under Hinge); ball joints under 2 Joint › Place joint; export under 3 Fit and export.

## Wat anders is dan de live tekst (GEZIEN met curl op superhivemarket.com/products/click-joints-pro, 21 nov ±13:55 UTC)
1. Regel "After installing" erbij.
2. Onder elk van de 7 punten één regel "Where to find it".
3. "and the list tells you why and what to try" werd "and Blender tells you which one and why": de reden staat in de melding, niet in de lijst (code hierboven). "what to try" is weg: de melding geeft de reden, niet altijd een oplossing.

Opmaak: op Gumroad en Superhive de regel "Where to find it" als tweede regel van hetzelfde punt (Shift+Enter), of als losse regel in cursief eronder als de editor geen tweede regel in een punt toelaat.
