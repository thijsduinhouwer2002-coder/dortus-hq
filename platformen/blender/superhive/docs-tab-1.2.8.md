# Superhive Docs-tab voor Pro 1.2.8 (Bram, 26 nov 2026, issue #119)

Vervangt `docs-tab-1.2.5.md` (nooit geplakt). Plakken door de hoofdchat op https://superhivemarket.com/products/click-joints-pro/docs (tab Documentation), na het ja van Daan.

**Waarom (geld, vóór de sale van vr 27 nov):** de tab zegt nu nog "Pick click_joints_pro-1.0.1.zip" (GEZIEN, curl op de docs-pagina, 26 nov ±02:15 NL), terwijl in de download `click_joints_pro-1.2.8.zip` zit. Een saleskoper die de docs volgt zoekt een bestand dat niet bestaat. Effect op verkoop: GOK, klein; elke vastgelopen koper is een terugbetaling of geen review.

## Waar elke naam vandaan komt (GEZIEN)
- Bestandsnaam: `click_joints_pro-1.2.8.zip`, zo geüpload op Superhive (`commercie/geplaatst.md` regel 48, zip uit e2e 45526260663; de e2e noemt hem `click_joints_pro-${PRO_VERSIE}.zip`, `.github/workflows/blender-gewrichten-e2e.yml` regel 123).
- Naam in de lijst van add-ons: "Click Joints Pro"; de gratis heet "Click Joints" (`e2e/maak_zip.sh` regel 26, zelfde id `click_joints`).
- Melding als de gratis aan staat: "Disable the free Click Joints first. Your settings stay in the .blend file." (`betaald/__init__.py` regel 15, code van 1.2.8 = commit 239b063).
- Tabblad "Click Joints" (`paneel.py` regel 53); stappen "1  Place", "2  Joint", "3  Fit and export"; veld "Clearance (mm)" (`eigenschappen.py` regel 26).
- Vak "Print this first" met "Fit test: ball" en "Fit test: hinge", vijf gewrichten 0.10 tot 0.30 mm in collectie "Fit test" (`betaald/testkaart.py`).
- Paneel "Figure joints" met "Figure from rig", "More bones (ankles too)" en "Or put the 3D cursor on a joint, then:" (`betaald/figuur.py`). Figure from rig vraagt een mesh met een Armature-modifier of een armature als parent (`betaald/rig.py` regel 657).
- Checklist: alleen wat al op de productpagina staat (200 mm, Fit test, 0.2 mm, lijst met reden, rood voorbij de stop, mm per deel; GEZIEN met curl, 26 nov ±02:15 NL).
- **Bewust weggelaten:** speling voor resin tegen FDM. Geen bron in de lat (`organisatie/lat/click-joints-pro.md` noemt alleen dat Cleave en NB Figure Joints een keuze resin/FDM hebben, geen getallen) en niet in onze eigen docs. De Fit test strip geeft het antwoord per printer.

## Tekst voor de tab (Engels, vervangt alles op de tab)
Opmaak: de woorden voor de dubbele punt aan het begin van een alinea vet, net als nu (Install:, Coming from the free version:, enz.). Knoppen en tabnamen mogen vet zoals nu.

```
Getting started

Install: in Blender 4.2 or newer, go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right and choose Install from Disk. Pick click_joints_pro-1.2.8.zip from your Superhive download (do not unzip it). Updating from an older Pro? Install the new zip the same way.

Coming from the free version: turn the free one off first. In Edit > Preferences > Add-ons, search "Click Joints" and untick "Click Joints" (not "Click Joints Pro"). Your joints and settings stay in the .blend file.

Open the panel: in the 3D viewport press N and open the Click Joints tab.

First click, with a rig: select the mesh that has an armature (Armature modifier or armature parent). In the Figure joints panel click Figure from rig. Elbows and knees become hinges with an end stop; shoulders, hips and neck become ball joints. More bones (ankles too) adds ankles (Blender 5.2 and newer). The list shows each joint with its type and range. A joint that does not fit is skipped, and the list says why.

First click, no rig: put the 3D cursor on a knee (Shift + right click on the skin). In Figure joints, under "Or put the 3D cursor on a joint, then:", click Knee. The other presets: Shoulder, Hip, Neck, Elbow, Ankle.

By hand, on any part: 1 Place: select the mesh, set the 3D cursor, click Check mesh (Make watertight or Convert to mm if it asks). 2 Joint: set Clearance (mm), then Place joint for a ball, or Place hinge, bends up to 90°, 115° or 135°. 3 Fit and export: pick a folder, STL or 3MF, and click Export.

Print the Fit test strip first: at the top of the Pro part, under Print this first, click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm clearance, each with its number, in a collection called Fit test. Print them, pick the one that turns smoothly without wobble, and set Clearance (mm) in step 2 to that number before you place your joints.

Figure printing checklist
- Figure about 200 mm tall or more, with separate arms and legs.
- Fit test strip printed, Clearance (mm) set to the joint that fit (default 0.2 mm).
- Every joint in the list placed, or skipped with a reason you have read.
- Show bend range on: drag Bend and check that nothing turns red before the pose you want.
- Exported in millimeters, one file per part.

Support
Questions or bugs: github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com. Please mention your Blender version.
```

## Wat anders is dan de tab van nu
- Bestandsnaam 1.2.8 in plaats van 1.0.1; regel voor wie bijwerkt.
- Gratis versie uitzetten: nu met de plek (Add-ons, zoeken, vinkje uit) en welke van de twee.
- Nieuw: Figure from rig, de presets zonder rig, de Fit test strip, de checklist.
- De drie stappen zijn ingekort tot één alinea "By hand"; de fitkleur en Show bend range staan in de checklist.
- Printtip "Print one small joint first" vervangen door de Fit test strip.
