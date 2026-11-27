# Click Cuts 1.0.0: FAQ-tab voor Superhive

Productbouwer, do 26 nov 2026 ±10:50 NL, issue #168. Plakken bij de lancering (week van 30 nov) door de hoofdchat, na het ja van Daan, op Superhive in de tab FAQ (één vraag per vak, vraag vet). Op Gumroad onderaan de pagina, onder de korte FAQ.

**Hoe gemaakt:** de vragen die al gekeurd zijn in de winkeltekst (`platformen/blender/superhive/click-cuts-winkeltekst.md`, Daan #110 en #131) staan hier woord voor woord, zodat pagina en tab hetzelfde zeggen. Nieuw zijn de vragen die een koper na het kopen stelt: installeren, waar de bestanden staan, opnieuw beginnen, pen te los of te strak, rood stuk, verkeerde maat, proef bij magneten, prints verkopen. Cleave heeft 8 vragen op zijn FAQ-tab, met installeren, ongedaan maken en verkopen erbij (GEZIEN, curl op `superhivemarket.com/products/cleave/faq`, 26 nov ±10:30 NL); wij hebben ze ook, plus de vragen over passen en magneten die bij ons voordeel horen.

Bronnen per antwoord: zie de tabel in `winkel/docs.md` (zelfde code, zelfde regels). Nieuwe bronnen staan onder de tekst.

## Tekst voor de tab (Engels, plakklaar)

```
Which Blender versions does it work with?
4.2 and newer, as an extension. Tested in Blender 4.2 and 5.3 on every change.

How do I install it?
Drag click_cuts-1.0.0.zip into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Then press N in the 3D viewport and open the Click Cuts tab.

The install failed or I got a folder instead of a zip. What now?
Safari on a Mac can unzip downloads by itself, and Blender cannot install a folder. Download it again with another browser, such as Chrome or Firefox, and drag the zip into Blender without opening it. Also check your Blender version: click the Blender logo at the top left, then About Blender. Click Cuts needs Blender 4.2 or newer and does not install in older versions. Still stuck? Send a message through the store with your Blender version and a screenshot of the error.

Why not just use my slicer's cut tool?
A slicer cuts one plane at a time, and you set every cut and connector yourself. Click Cuts plans all the cuts so every part fits your bed, checks each part (green fits, orange or red tells you why), numbers the parts, and uses the clearance from your own fit test print.

Which connectors?
Round pins, or holes for disc magnets (5x2, 6x2, 6x3, 8x3 or 10x3 mm; you buy the magnets). The magnet hole gets your clearance on the diameter and 0.3 mm extra depth for glue. No dovetails or snap keys.

How do I glue the magnets?
Glue the magnets with matching poles: stick a magnet to the one already glued before you press it in.

My pins are too loose or too tight. What do I do?
Print the fit test first (More settings, step 3, Make fit test): one small block with your own pin at four clearances. Click the clearance where the pin goes in by hand and does not wobble. Click Cuts remembers it for that printer and material and uses it for every split after that. All four wrong? Set Clearance (mm) a step lower or higher and make a new fit test.

Does the fit test work for magnets?
The fit test uses a pin. With Magnets, the same clearance goes on the diameter of the magnet hole, half on each side: a 6 mm magnet with 0.20 mm clearance gets a hole of 6.2 mm across.

Can I choose where it cuts, so it does not go through a character's face?
Partly. Split to fit cuts along the X, Y and Z axes. After splitting, Free cut adds a cut at any angle through one part, for example an arm at the shoulder, with pins and numbers like the other cuts.

Can I move the cuts?
Yes. Open More settings, step 2: every cut has a row, for example Cut X (mm). Drag or type to move it, or remove it. Then click Split to fit again: your moved cuts are kept.

Do parts lie flat for printing?
Yes. Lay parts flat (on by default) turns every part on export so a flat face, usually a cut face, lies on the bed, if it still fits your printer. Otherwise the part keeps its own way up.

A part is red. What now?
The row in More settings, step 4 says why: too big (pick the right printer, or add a cut), not watertight (try Make watertight with a larger Voxel (mm)), or too little wall around a hole (a smaller pin or magnet, or a higher Min. wall (mm) so holes stay further from the edge). Orange means the wall around a hole is thinner than Min. wall (mm).

Thin or hollow models?
Some joints have no room for a pin or magnet; Click Cuts tells you which ones to glue.

Does it fix broken meshes?
Make watertight makes a closed copy (voxel remesh). Very large or detailed models may need to be cleaned first.

Split to fit says "Wrong unit?"
Your model is 1000 times too big or too small for the scene, usually a model made in mm in a scene in meters. Open More settings, step 2, and click Convert to mm. It sets the scene unit; your model does not change.

Where are my files?
In a click_cuts folder next to your .blend file, one file per part (piece_01.stl and so on) plus the pins, in millimeters. If the .blend is not saved yet, they go to a temporary folder: save first, or pick a Folder in More settings, step 4.

Is my original model changed?
No. It is hidden, not changed, and the parts go into a new collection called Click Cuts pieces. Split again and the old parts are replaced. Ctrl+Z undoes a split.

How fast is it?
Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine). In Blender 4.2 to 4.4 the same scan takes about 3 minutes. Big models show a time estimate under Split to fit.

How much memory?
Very large models (3 million faces) need a lot of memory in Blender 4.2 to 4.4: about 9 GB. Blender 5.3 needs about 5 GB. With 8 GB of memory, use Blender 5.3 for models that big.

Does it work with Click Joints Pro?
Yes, side by side. Splitting makes it fit on the bed. Click Joints Pro makes it move.

Can I sell what I print with it?
The Click Cuts license covers the add-on, not your models or prints. What you may do with a model depends on that model's own license.

Something does not work?
Send a message through the store or mail thijs@dortus.com, with your Blender version and, if you can, the model or a screenshot of the panel.
```

## Bronnen voor de nieuwe vragen (GEZIEN in de code op main, zelfde regels als `winkel/docs.md`)
- **Installeren:** zelfde zin als de Docs-tab (installatieweg van de gekeurde Pro-tab), zipnaam uit `blender-splitser-e2e.yml` r. 121.
- **Slepen (issue #250):** Blender 4.2 handboek: "drag-and-drop an extension .zip package into Blender" (DERDEN, https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html, curl 27 nov ±08:35 NL).
- **Map in plaats van zip (issue #250):** Apple: "Safari decompresses files such as .zip files after it downloads them" (DERDEN, https://support.apple.com/en-gb/guide/safari/sfri40598/mac, curl 27 nov ±08:45 NL). Wij schrijven "can", want het hangt af van de instelling. De naam van die instelling kon ik niet bij Apple nalezen, dus die noemen we niet; we geven de weg die altijd werkt (andere browser). Install from Disk vraagt om een .zip (handboek, zelfde pagina).
- **Ouder dan 4.2:** `blender_manifest.toml` `blender_version_min = "4.2.0"` en geen `bl_info` in `split_joints/__init__.py` (GEZIEN, grep 0), dus het oude add-on-menu kan hem niet laden. Versie zien: Blender-logo linksboven > About Blender (DERDEN, https://docs.blender.org/manual/en/4.2/interface/window_system/topbar.html).
- **Waarom deze vraag:** bij CAD Sketcher gaan 17 van de 25 lage beoordelingen over installeren of "werkt niet" (GEZIEN, `organisatie/lat/broncode/cad-sketcher.md`).
- **Te los of te strak:** `passingproef.teken` en `passing.py` r. 4 tot 6; onthouden per printer en materiaal en gebruikt bij elke split via `pas_toe`, ook in een nieuw bestand (`sj_laden`, behalve waar de koper zelf een speling typte).
- **Proef bij magneten:** `verbinders.magneet_opties` (`speling / 2` per kant), `passing_maak` gebruikt `inst.pen_mm`.
- **Sneden verschuiven:** `paneel.py` r. 100 tot 108 (`sj_plek_mm` "Cut X (mm)", X-knop), `in_een_klik` r. 160 ("kept your moved cuts").
- **Rood stuk:** `controle.status_uit` (rood bij niet passen, niet dicht of wand onder 0,8 mm; oranje bij wand onder Min. wall), rijtekst `controle.tekst`. De uitwegen zijn instellingen die er zijn (printer, Add cut, Make watertight met Voxel (mm), Pin diameter, Magnet (mm), Min. wall); geen belofte dat ze het altijd oplossen.
- **Wrong unit:** `in_een_klik` r. 148, `schaal.py` (10 tot 3000 mm, "The model does not change").
- **Bestanden, origineel:** `exporteer.py` (`STANDAARD`, `bestandsnaam`, `exportmap`), `splitsen.py` r. 392 en `STUKKEN`, `bl_options` UNDO.
- **Verkopen:** licentie GPL-3.0-or-later (`blender_manifest.toml`); de GPL gaat over de add-on, niet over wat je ermee maakt. Geen juridisch advies, alleen dat onze licentie hun modellen niet raakt; zelfde strekking als Cleave (DERDEN, hun FAQ).
- **Lay parts flat:** de gekeurde zin zegt "usually a cut face". De code is sinds Daans M1 (24 nov) strenger: alleen een snijvlak (`plat.kies_stand(alleen_snijvlak=True)`). De zin belooft dus niet te veel; ik laat hem woord voor woord staan zodat pagina en tab gelijk blijven.
- **Geen refund-vraag:** terugbetalen is een geldkeuze voor Thijs, niet voor mij.
