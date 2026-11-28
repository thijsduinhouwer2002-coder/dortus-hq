# Click Cuts: Docs-tab voor Superhive (en de pagina na het kopen op Gumroad)

Productbouwer, do 26 nov 2026 ±10:45 NL, issue #168. Plakken bij de lancering (week van 30 nov) door de hoofdchat, na het ja van Daan: op Superhive in de tab Documentation, op Gumroad in het vak dat de koper na het kopen ziet ("Content"). Eén tekst voor beide winkels.

**Waarom:** een koper moet na het kopen niets hoeven zoeken. Cleave heeft op zijn Docs-tab een lijst van elke functie met één regel uitleg (GEZIEN, curl op `superhivemarket.com/products/cleave/docs`, 26 nov ±10:30 NL); Split 3D Print zet "Where to find it" bij elke functie (lat). Wij doen beide: eerst de weg van installeren tot de eerste print, dan elke knop met waar hij staat. Kopers zijn vaak nieuw in Blender (`concurrentie.md` r. 107), dus elke stap noemt de knop letterlijk.

Opmaak zoals de Docs-tab van Click Joints Pro: de woorden voor de dubbele punt aan het begin van een alinea vet, koppen als kop. Amerikaanse spelling, zoals de add-on.

## Tekst voor de tab (Engels, plakklaar)

```
Getting started

Install: open Blender 4.2 or newer. Drag click_cuts-1.1.0.zip into the Blender window and confirm. Do not unzip it. Or go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right, choose Install from Disk and pick the zip. Got a folder instead of a zip? See the FAQ. Updating later? Install the new zip the same way.

Open the panel: in the 3D viewport press N and open the Click Cuts tab.

Your first split:
1. Under Your printer, pick your printer. Not in the list? Pick Custom size and type your bed size in mm (X, Y, Z).
2. Click your model in the viewport. The panel shows its name and face count, for example "Statue: 500 faces".
3. Click Split to fit. Click Cuts plans the cuts, cuts the model into parts that fit your bed, adds pins and pin holes, and engraves a part number on the cut faces. The result box says, for example, "8 parts, all fit the bed" and "12 pins, 0.20 mm clearance".
4. Click Export parts (STL). Every part and the pins are written in millimeters, one file per part: piece_01.stl, piece_02.stl and so on, plus pins_5mm_x12.stl.

Where the files go: into a click_cuts folder next to your .blend file. Save your .blend first, or the files go to a temporary folder. To pick your own folder, open More settings, step 4, Folder.

Your original model is kept: it is hidden, not changed. The parts are in a new collection called Click Cuts pieces. Click Split to fit again and the old parts are replaced. Ctrl+Z undoes a split.

Open model? If the model has holes, Split to fit first makes a watertight copy (the panel then shows the name with "(closed)"). The original stays hidden and unchanged.

Wrong unit? If your model is 1000 times too big or too small (a model made in mm, in a scene in meters), Split to fit stops and tells you. Open More settings, step 2, and click Convert to mm. The model itself does not change.

Too big for your bed? If a model needs more than 200 parts, Split to fit stops and the panel says how big it is, for example "Too big: 2,000 x 2,000 x 2,000 mm". Scale it down (S) or pick a bigger printer. Trying it on the default cube? It is 2 m: press S, type 0.2 and press Enter first.


Print the fit test first

Every printer prints holes a little differently. The fit test tells you which clearance fits yours, so pins are not loose or stuck.

1. Open More settings, step 3. In the box Fit test: print this first, pick your Material.
2. Click Make fit test. You get a small block with four holes for your own pin, each with its clearance engraved in front of it, plus four pins. Until you save a fit test, the clearance starts at a value for your material (PLA 0.20 mm: holes at 0.15, 0.20, 0.25 and 0.30 mm; Resin 0.10 mm: holes at 0.05, 0.10, 0.15 and 0.20 mm; PETG and ABS / ASA 0.25 mm; TPU 0.30 mm).
3. Click Export fit test (STL) and print the block and the pins.
4. Push a pin into every hole. Under "Printed? Click the one that fits:", click the clearance where the pin goes in by hand and does not wobble.

Click Cuts remembers that clearance for this printer and material. Next time you pick the same printer and material, it is used again ("Saved for this printer: 0.20 mm").

All four too loose or too tight? Set Clearance (mm) a step lower or higher and make a new fit test: the four holes move with it.


Magnets instead of pins

Open More settings, step 3, and switch Joint to Magnets. Pick your magnet size under Magnet (mm): 5x2, 6x2, 6x3, 8x3 or 10x3 mm (diameter x thickness, for disc magnets). Then click Split to fit. Magnets are not included.

Each cut face gets a hole for a magnet on both sides, where it fits. The hole is as deep as the magnet plus 0.3 mm for glue, and has at least 1.2 mm of wall around it. Where a magnet does not fit, there is no hole and the notes tell you to glue that joint or pick a smaller magnet. The result box and step 4 count the magnets you need, for example "16 magnet holes of 6x2 mm (magnets not included)".

Clearance with magnets: the fit test uses a pin. With Magnets, your clearance goes on the diameter of the hole, half on each side: a 6 mm magnet with 0.20 mm clearance gets a hole of 6.2 mm across.

Gluing the magnets: glue the magnets with matching poles. Glue the first magnet in one part. Then stick the next magnet onto the one already glued, and press it into the other part while they hold together. Now the poles always match.


Choose where it cuts: Draw cut

Split to fit cuts along the X, Y and Z axes. Want a cut somewhere else, for example an arm at the shoulder, or a cut that stays out of a face?

1. After a split, click the part you want to cut.
2. Under the result, click Draw cut. Drag a line across the part where you want it cut. The cut goes along your line, straight away from you, and only as wide as the line.
3. The part that comes off lights up white, with an arrow that says "comes off". Wrong part? Click Flip side.
4. Click Cut piece. The part is cut in two, with pins (or magnet holes) and numbers like the other cuts.

Want to set the angle exactly? Move (G), turn (R) and scale (S) the cut plane before you click Cut piece. It only cuts what lies inside its rectangle. Add free cut (More settings, step 4) gives the same cut plane without drawing.


Lay parts flat

On by default (More settings, step 4). On export, every part is turned so a cut face lies on the bed, if it still fits your printer. A part with no cut face that fits keeps its own way up. Your parts in the scene do not move; only the files are turned. Pins are already flat.


The panel, step by step

Split to fit does everything below in one click. Open More settings to change it.

1 Printer: Margin (mm), the room kept free on every side of the bed (default 2 mm). The panel shows the usable size.

2 Cuts: Make watertight (a closed copy, with Voxel (mm) for the detail). Plan cuts places the cut planes so every part fits with as few parts as possible. Each cut has its own row, for example Cut X (mm): drag or type to move it, or remove it with the X. Add cut: X, Y or Z adds one. Moved a cut? Click Split to fit again: your moved cuts are kept.

3 Joints and numbers: Joint (Pins or Magnets). For pins: Pin diameter (mm) (default 5), Smaller pins on small faces (down to 3 mm, on by default) and Pin length (mm) (default 12; each hole is half this deep plus 0.3 mm). Clearance (mm) (default 0.20) and the fit test. Min. wall (mm), the least material around every hole (default 1.2). Engrave numbers: the cut faces get their part number and its neighbor, for example 3-5 on part 3 where it meets part 5, with Number depth (mm) (default 0.6). Split cuts again with these settings.

4 Check and export: every part with its size and a color. Green: it fits the bed, is watertight and has enough wall around its holes. Orange: the wall around a hole is thinner than Min. wall. Red: too big for the bed, not watertight, or less than 0.8 mm of wall; the row says which. Colors: Per piece (every part its own color, pins in gold) or Check. Exploded view shows the parts a little apart, only in the viewport. Free cut. Notes from the last split (for example a joint to glue). STL or 3MF, Lay parts flat, Folder, and Export.


Big models

Models with a million faces or more show a time estimate under Split to fit, and a memory line when they need 8 GB or more. Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine). In Blender 4.2 to 4.4 the same scan takes about 3 minutes and needs about twice the memory, so for very big scans use a newer Blender.


Support

Questions or bugs: send a message through the store or mail thijs@dortus.com. Please mention your Blender version and, if you can, send the model or a screenshot of the panel.
```

## Waar elke naam, standaard en maat vandaan komt (main na ae41e48, GEZIEN in de code)

| In de tekst | Code |
|---|---|
| Slepen naar het Blender-venster (issue #250, Daan ja #254) | Blender 4.2 handboek: "Use the drop-down menu in the top right, or drag-and-drop an extension .zip package into Blender" (DERDEN, https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html); werkt dus vanaf onze minimumversie |
| Blender 4.2 or newer, Install from Disk, zip niet uitpakken | `blender_manifest.toml` `blender_version_min = "4.2.0"`; zelfde installatiezin als de gekeurde Docs-tab van Pro (`platformen/blender/superhive/docs-tab-1.2.9.md`, Daan #130) |
| `click_cuts-1.1.0.zip` | zipnaam volgt de versie; versie 1.1.0 in het manifest (`blender_manifest.toml` r. 3) |
| N, tab Click Cuts | `paneel.py` `bl_category = "Click Cuts"`, `bl_region_type = "UI"` |
| Your printer, Custom size, X Y Z, "Bed size in mm" | `paneel.py` r. 32 tot 39; `printers.py` `EIGEN` label "Custom size" |
| "Statue: 500 faces", "(closed)" | `in_een_klik.model_tekst`; "(closed)" voor de dichte kopie |
| Click your model | `in_een_klik.GEEN_MODEL` "Click your model in the viewport"; Split to fit pakt het actieve mesh (`kies_model`) |
| "8 parts, all fit the bed", "12 pins, 0.20 mm clearance" | `in_een_klik.uitslag_tekst` (getallen als voorbeeld) |
| Export parts (STL) | `paneel.py` r. 77 `f"Export parts ({inst.formaat})"` |
| piece_01.stl, pins_5mm_x12.stl, millimeters | `exporteer.bestandsnaam`: `piece_{:02d}`, `pins_{d:g}mm_x{n}` met punt naar liggend streepje (5 wordt `5mm`) |
| click_cuts-map naast de .blend, anders tijdelijke map, Folder | `exporteer.STANDAARD = "//click_cuts/"`, `exportmap`, `hint` ("Saves to a temporary folder"); `eigenschappen.exportmap` name "Folder" |
| Origineel verborgen, niet veranderd; collectie Click Cuts pieces; oude delen weg bij opnieuw | `splitsen.py` r. 392 `ob.hide_set(True)`, `STUKKEN = "Click Cuts pieces"`, `ruim_oud_op` |
| Ctrl+Z | `split_to_fit` en `split` hebben `bl_options = {"REGISTER", "UNDO"}` |
| Dichte kopie bij een open model, origineel verborgen | `in_een_klik` r. 152 tot 158; `gesloten.py` r. 86 `bron.hide_set(True)`, description "The original is kept, hidden" |
| Wrong unit, Convert to mm, model verandert niet | `in_een_klik` r. 148 ("Wrong unit? Open More settings and use Convert to mm"); `schaal.py` label "Convert to mm", description "The model does not change"; knop staat in stap 2 (`paneel.py` r. 93 tot 97) |
| Fit test: print this first, Material, Make fit test, 4 gaten, 4 pennen | `passingproef.teken` r. 276 tot 297; `passing.AANTAL = 4`; `SPLIT_JOINTS_OT_passing_maak` description |
| 0.15, 0.20, 0.25, 0.30 bij 0.20 | `passing.spelingen(0.2)`: start 0,2 min 0,05, stap 0,05 |
| Export fit test (STL), "Printed? Click the one that fits:" | `passingproef.teken` r. 290 en 292 |
| Onthouden per printer en materiaal, "Saved for this printer: 0.20 mm" | `passing.sleutel(printer, materiaal)`, `pas_toe` bij wisselen van printer of materiaal, `teken` r. 281 |
| Speling lager of hoger, gaten schuiven mee | `teken` r. 285: Make fit test gebruikt `passing.spelingen(inst.speling_mm)` |
| Joint Pins/Magnets, Magnet (mm), 5x2 tot 10x3 | `eigenschappen.verbinder`, `magneet`; `verbinders.MAGNETEN` |
| Diepte magneet + 0,3 mm, minstens 1,2 mm wand | `verbinders.MAGNEET_LUCHT_MM = 0.3`, `MAGNEET_WAND_MM = 1.2`, `magneet_opties` |
| Geen gat waar het niet past, lijmen of kleinere magneet | `ontwerp.md` deel 16 (melding "too small for a magnet ... Glue this joint or pick a smaller magnet") |
| "16 magnet holes of 6x2 mm (magnets not included)" | `paneel.py` r. 151 (getal als voorbeeld) |
| Speling op de diameter, half per kant, 6,2 mm | `magneet_opties`: `speling / 2` per kant; paneelregel "Magnets use half: clearance on the diameter"; proef gebruikt pen (`passing_maak` met `inst.pen_mm`) |
| Polen gelijk lijmen | `ontwerp.md` deel 16 "Wat het niet doet"; FAQ-zin in de gekeurde winkeltekst |
| Free cut: stuk aanklikken, Add free cut, G R S, rechthoek, pijl, Cut piece | `vrije_snede.py` r. 307 tot 336 (poll: actief object is een stuk; description met G, R, S, rechthoek en lokale Z) |
| Draw cut onder de uitslag, lijn slepen, langs de lijn, recht van je af, zo breed als de lijn | `paneel.py` rij na het uitslagvak (alleen na een split met stukken); `SPLIT_JOINTS_OT_vrije_snede_tekenen` bl_description; `lijn.vlak_uit_lijn` (1.1, tak `claude/click-cuts-1.1`) |
| Wit oplichten, "comes off", Flip side | changelog 1.1 en `SPLIT_JOINTS_OT_vrije_snede_om` ("Flip side", description "the arrow and the lit part change side") |
| Startspeling per materiaal, Resin 0,05 tot 0,20 | `passing.py` startwaarden (#227); e2e `toetsen_passing.py` meet de vier harsgaten |
| Lay parts flat, aan, snijvlak, anders eigen stand, scène blijft staan, pennen al plat | `eigenschappen.plat` (default True); `plat.kies_stand(alleen_snijvlak=True)`; `exporteer.py` `finally` zet `matrix_basis` terug; "pin plates are already flat" |
| Margin (mm) 2, usable | `eigenschappen.marge_mm` default 2.0; `paneel.py` r. 85 |
| Make watertight, Voxel (mm), Plan cuts, Cut X (mm), X-knop, Add cut: X Y Z, verschoven sneden blijven | `paneel.py` r. 92 tot 120; `snedes.py` description Plan cuts; `in_een_klik` r. 160 ("kept your moved cuts") |
| Pin diameter 5, Smaller pins tot 3 mm aan, Pin length 12, gat half + 0,3 | `eigenschappen.pen_mm`, `pen_auto`, `pen_lengte_mm` (description "half this deep plus 0.3 mm") |
| Clearance 0.20, Min. wall 1.2, Engrave numbers 3-5, Number depth 0.6 | `eigenschappen.speling_mm`, `wand_mm`, `labels`, `label_diepte_mm`; `paneel.py` r. 139 |
| Oranje bij wand onder Min. wall, rood bij te groot, niet dicht of wand onder 0,8 mm; rij noemt "too big", "not watertight", "wall 0.6" | `controle.status_uit`, `ROOD_WAND_MM = 0.8`, `controle.tekst` |
| Groen, oranje, rood, Colors Per piece / Check, pennen goud, Exploded view alleen viewport | `eigenschappen.kleur` en `uit_elkaar` descriptions |
| Tijdschatting vanaf 1M, geheugen vanaf 8 GB | `in_een_klik.ZWAAR_VLAKKEN = 1_000_000`, `GEHEUGEN_GRENS_GB = 8` |
| 40 seconden, 3 minuten, twee keer het geheugen | gekeurde FAQ in `platformen/blender/superhive/click-cuts-winkeltekst.md` (GEZIEN: 42 s in 5.3, 186 s in 4.2.23 op 2 kernen; geheugen 9.220 MB tegen 4.741 MB bij 3M, run 45367520845); 4.3 en 4.4 volgen uit `splitsen.solver_naam` (Manifold pas vanaf 4.5) |
| Support via de winkel en thijs@dortus.com | zelfde adres als in `blender_manifest.toml` (maintainer) en de Docs-tab van Pro |

## Bewust niet in de tekst
- Geen belofte dat het klikt of dat wij printten (CLAUDE.md regel 5). "goes in by hand and does not wobble" is de keuze die de koper zelf maakt, uit `passing.py` r. 4 tot 6.
- "very big scans use a newer Blender" zonder versienummer: 4.5 zelf is niet gemeten (GOK), 5.3 wel.
- Geen deuvels, klikpennen, zwaluwstaart of snijden langs de vorm.
