# Superhive Docs-tab voor 1.2.5, "Start here.txt" en de foto-zin (Bram, 24 nov 2026)

**Opdracht:** Afkijker 24 nov ±14:35 NL, volgorde hoofdchat 12:45. Plakken door de hoofdchat, samen met de 1.2.5-zip, na het ja van Daan.
**Waarom (geld):** de Docs-tab zegt nu "Pick click_joints_pro-1.0.1.zip" en noemt Figure from rig, More bones en de Fit test niet (GEZIEN met curl, https://superhivemarket.com/products/click-joints-pro/docs , 24 nov ±13:10 NL). Een koper die vastloopt vraagt zijn geld terug of geeft geen review. Bij Surface Lab gaan 2 van 5 reviews over gemak en uitleg (GEZIEN, Afkijker). Effect op verkoop: GOK, klein maar €0.

## Waar de namen vandaan komen (GEZIEN in de code op main, 4bf764f)
- Tabblad `bl_category = "Click Joints"`; paneel "Click Joints" met "1  Place" (knoppen Check mesh, Make watertight, Convert to mm), "2  Joint" (Place joint, Clearance (mm), Diameter (mm), Auto), "3  Fit and export" (Folder, Format, Export) (`paneel.py`, `gesloten.py`, `schaal.py`, `exporteer.py`).
- Pro-deel bovenaan: vak "Print this first" met knoppen "Fit test: ball" en "Fit test: hinge", vijf gewrichten van 0.10 tot 0.30 mm in een collectie "Fit test" (`betaald/testkaart.py`).
- "Place hinge, bends up to:" 90°, 115°, 135°, "Flip bend", vak "Hinge" met "Show bend range", schuif "Bend", knop "Reset bend" (`betaald/scharnier.py`, `waaier.py`).
- Paneel "Figure joints": "Figure from rig" (alleen met armature), "More bones (ankles too)", "Or put the 3D cursor on a joint, then:" met zes presets, de lijst, schakelaar "Labels" (`betaald/figuur.py`, `betaald/labels.py`).
- Enkels via More bones: alleen getoetst op een mensfiguur, Blender 5.2 en nieuwer (`pro-1.2.5.md`, e2e 45372957961). Daarom dezelfde grens als in de winkeltekst.
- Bewust niet: een link naar de Fit test op dortus.com. Die pagina staat nog niet live (`/click-joints/fit-test-strip.stl` gaf 404, GEZIEN 24 nov). De knop in de add-on doet hetzelfde.

## 1. Docs-tab "Getting started" (Engels, vervangt alles op de tab)
De eerste regel (video) alleen plakken als de video guide van Chris echt bij het product staat. Anders weglaten.

```
Short video guide: in your download (Click Joints Pro video guide).

Getting started

Install: in Blender 4.2 or newer, go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right and choose Install from Disk. Pick the click_joints_pro zip you downloaded here (do not unzip it). Is the free Click Joints enabled? Disable it first; the two cannot be on at the same time. Updating? Install the new zip the same way; your settings stay in the .blend file.

Open the panel: in the 3D viewport press N and open the Click Joints tab.

Print this first: at the top of the Pro part, click Fit test: ball or Fit test: hinge. You get five joints from 0.10 to 0.30 mm clearance in a collection called Fit test. Export and print them, and use the clearance of the one that turns smoothly without wobble.

Rigged figure (fastest way): select the mesh that has an armature. In the Figure joints panel click Figure from rig. Elbows and knees become hinges with an end stop, shoulders, hips and neck become ball joints. More bones (ankles too) adds ankles on human figures (Blender 5.2 and newer). The list under the buttons shows each joint with its type and range. A joint that does not fit is skipped, and the message at the bottom of the window tells you which one and why.

No rig: set the 3D cursor on the joint (Shift + right click), then in Figure joints click the body part under "Or put the 3D cursor on a joint, then:" (Shoulder, Elbow, Hip, Knee, Ankle, Neck).

By hand, step by step:
1 Place: select your mesh and set the 3D cursor where the joint goes. Click Check mesh. If the mesh is not watertight, use Make watertight. If the size looks wrong (expected 5 to 500 mm), click Convert to mm.
2 Joint: for a ball joint, pick the diameter (or Auto) and the clearance, then click Place joint. For a hinge, use Place hinge, bends up to and pick 90°, 115° or 135°. Flip bend makes it bend the other way.
3 Fit and export: the fit colour tells you if the joint is good. Turn on Show bend range and drag Bend to check the pose; parts that hit turn red. Reset bend puts it back. Choose a folder, STL or 3MF, and click Export. The pose does not change the export.

Printing tips
The default clearance is 0.2 mm. Use the Fit test above to find the right one for your printer.
Exported files are in millimeters, one file per part.

Support
Questions or bugs: github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com. Please mention your Blender version.
```

Wat anders is dan de tab van nu: geen versienummer in de bestandsnaam; regel "Updating?"; nieuw blok "Print this first"; nieuw blok "Rigged figure" en "No rig"; de drie stappen heten nu "By hand"; printtip verwijst naar de Fit test. Opmaak: de vette woorden van nu (Install:, Open the panel:, 1 Place: enz.) blijven vet, de nieuwe koppen (Print this first:, Rigged figure (fastest way):, No rig:) ook.

## 2. "Start here.txt" (bij de video-download, Engels)
Alleen als de clips bij het product komen. Bestandsnamen zoals in `commercie/blender-click-joints/pro-uitleg/`.

```
Click Joints Pro video guide

The clips have no sound; the text is in the picture.

1-figure-from-rig.mp4 (45 s): watch this first. From a rigged figure to printable parts with one button: Figure from rig, the bend range per joint, red past the stop, export.
2-fit-test.mp4 (16 s): watch this before your first print. Print five small joints and keep the clearance that fits your printer.

Where is the panel? In the 3D viewport press N and open the Click Joints tab. The Fit test buttons are under "Print this first", Figure from rig is in the Figure joints panel.

Written steps: the Documentation tab on the product page.
Stuck? github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com. Please mention your Blender version.
```

Komt clip 3 van de Regisseur erbij, dan voeg ik één regel toe.

## 3. Eén zin onderaan de productpagina (Gumroad en Superhive)
```
Printed a figure with Click Joints? Email a photo to thijs@dortus.com and, with your OK, we show it here.
```
Kanaal: hetzelfde adres dat al als support op de pagina staat (geen account van Thijs, geen nieuw kanaal). "with your OK": we tonen geen foto zonder toestemming van de maker. Willen we echt tonen? Ja: we hebben nog geen enkele printfoto van een koper, en elke echte foto is beter dan onze renders (GOK). Wie mailt, ziet de hoofdchat via Gmail lezen; plaatsen op de pagina doet de hoofdchat.

## Stand
- 24 nov ±13:15 NL: tekst klaar, keuring gevraagd aan Daan. Na zijn ja plakt de hoofdchat 1 (en 3) mee met 1.2.5; 2 pas als de clips gekeurd zijn.
