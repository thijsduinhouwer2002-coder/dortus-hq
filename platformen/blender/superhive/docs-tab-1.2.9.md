# Superhive Docs-tab en hoofdpaginaregel voor Pro 1.2.9 (Bram, 26 nov 2026, keuring #157)

Vervangt `docs-tab-1.2.8.md` zodra 1.2.9 live is. **Plakken pas vanaf ma 30 nov, samen met de upload van 1.2.9**, door de hoofdchat op https://superhivemarket.com/products/click-joints-pro/docs (tab Documentation) en op de productpagina, na het ja van Daan.

**Waarom:** in 1.2.9 zet Pro de gratis Click Joints zelf uit (#114, op main in 99a3c69, e2e 45773325191 groen in 4.2.23, 5.2.3 en 5.3.0, GEZIEN). De zin "turn the free one off first" klopt dan niet meer en laat een koper iets doen wat niet hoeft. Het paneel van 1.2.9 staat ook anders (Figure from rig bovenaan, Fit test in stap 2, hinge-knoppen onder Place joint).

## Waar elke naam vandaan komt (GEZIEN, main c469536)
- Bestandsnaam `click_joints_pro-1.2.9.zip`: de e2e noemt hem `click_joints_pro-${PRO_VERSIE}.zip` (`.github/workflows/blender-gewrichten-e2e.yml`); VERSIE gaat op 30 nov naar 1.2.9 (`platformen/blender/pro-1.2.9.md`, kop Zip).
- Regel als Pro de gratis uitzet: "Free Click Joints was turned off; Pro includes everything in it." (`click_joints/betaald/__init__.py` regel 24), bovenaan het paneel (regel 175).
- Vak bovenaan bij een rig: "Rig found: <naam>", knop "Figure from rig", knop "More bones (ankles too)" (`betaald/figuur.py` regels 219 tot 223).
- Stappen "1  Place", "2  Joint", "3  Fit and export"; "Check mesh"; "Place joint" (`click_joints/paneel.py` regels 79, 94, 97, 104, 109).
- Veld "Clearance (mm)" (`eigenschappen.py` regel 28); daaronder "Not sure? Print a fit test first:" met "Fit test: ball" en "Fit test: hinge" (`betaald/testkaart.py` regels 213 tot 216); collectie "Fit test" (regel 153).
- Onder Place joint: "Or a hinge that bends up to:" met 90°, 115°, 135° (`betaald/scharnier.py` regel 327 en verder).
- Stap 3 na een scharnier: "Hinge placed" (`betaald/scharnier.py` regel 290). Exportknop "Export STL" of "Export 3MF" (`paneel.py` regel 140).
- Paneel "Figure joints" met "Or put the 3D cursor on a joint, then:" (met rig) of "Put the 3D cursor on a joint, then:" (zonder rig) en de presets (`betaald/figuur.py` regels 228 en 243).
- Checklist en Support: gelijk aan de tab van 1.2.8 (gekeurd, Daan #130).

## Tekst voor de tab (Engels, vervangt alles op de tab)
Opmaak zoals nu: de woorden voor de dubbele punt aan het begin van een alinea vet.

```
Getting started

Install: in Blender 4.2 or newer, go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right and choose Install from Disk. Pick click_joints_pro-1.2.9.zip from your Superhive download (do not unzip it). Updating from an older Pro? Install the new zip the same way.

Coming from the free version: just enable Pro. It turns the free Click Joints off for you, and the top of the panel says "Free Click Joints was turned off; Pro includes everything in it." Nothing is deleted, and your joints and settings stay in the .blend file.

Open the panel: in the 3D viewport press N and open the Click Joints tab.

Print the Fit test strip first: in step 2, under Clearance (mm), click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm clearance, each with its number, in a collection called Fit test. Print them, pick the one that turns smoothly without wobble, and set Clearance (mm) to that number. Then place your joints.

First click, with a rig: select the mesh that has an armature (Armature modifier or armature parent). "Rig found" appears at the top of the panel: click Figure from rig. Elbows and knees become hinges with an end stop; shoulders, hips and neck become ball joints. More bones (ankles too) adds ankles (Blender 5.2 and newer). The list shows each joint with its type and range. A joint that does not fit is skipped, and the list says why.

First click, no rig: put the 3D cursor on a knee (Shift + right click on the skin). In the Figure joints panel, under "Put the 3D cursor on a joint, then:", click Knee. The other presets: Shoulder, Hip, Neck, Elbow, Ankle.

By hand, on any part: 1 Place: select the mesh, set the 3D cursor, click Check mesh (Make watertight or Convert to mm if it asks). 2 Joint: set Clearance (mm), then Place joint for a ball, or under "Or a hinge that bends up to:" click 90°, 115° or 135°. 3 Fit and export: check the fit (after a hinge it says Hinge placed with its bend range), pick a folder, STL or 3MF, and click Export STL (or Export 3MF).

Figure printing checklist
- Figure about 200 mm tall or more, with separate arms and legs.
- Fit test strip printed, Clearance (mm) set to the joint that fit (default 0.2 mm).
- Every joint in the list placed, or skipped with a reason you have read.
- Show bend range on: drag Bend and check that nothing turns red before the pose you want.
- Exported in millimeters, one file per part.

Support
Questions or bugs: github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com. Please mention your Blender version.
```

## Regel op de productpagina (Superhive, tab Overview)
Nu staat er (GEZIEN, curl op de productpagina, 26 nov ±10:10 NL):
"The free Click Joints (Blender Extensions) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file."

Vervangen door:
```
Coming from the free Click Joints (Blender Extensions)? Just enable Pro: it turns the free one off for you. Nothing is deleted, and your settings stay in the .blend file.
```

## Wat anders is dan de tab van 1.2.8
- Bestandsnaam 1.2.9.
- "Coming from the free version": geen vinkje meer uitzetten; Pro doet het zelf en zegt het in het paneel.
- Fit test staat nu in stap 2 onder Clearance (mm), niet meer onder "Print this first".
- Figure from rig staat bovenaan bij "Rig found", niet meer in het paneel Figure joints.
- Hinges onder "Or a hinge that bends up to:" in stap 2; stap 3 zegt "Hinge placed".
