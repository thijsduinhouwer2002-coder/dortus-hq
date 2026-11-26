# Click Cuts changelog

## Unreleased (1.1, after the launch of 1.0.0)
- Start clearance per material: until you save a fit test for your printer and material, Click Cuts starts at a clearance that suits the material: Resin 0.10, PLA 0.20, PETG and ABS / ASA 0.25, TPU 0.30 mm. The fit test tests around that value (Resin 0.05 to 0.20 mm), so the one that fits is on the block. A saved fit test or a clearance you typed yourself always comes first. The fit test box says "Start value for Resin: print the fit test" until you pick one. After a Split, the result box keeps naming the clearance the parts were cut with; when you change it (also by picking another material) it says "Clearance changed: press Split to fit again". (Docs tab, Fit test step 2, gets the resin example when 1.1 goes out.)

## 1.0.0 (candidate, 25 Nov 2026)
First version.
- Split to fit: one button cuts the selected model into parts that fit your printer bed, with pins, pin holes and part numbers.
- Printer list with usable bed size, or your own size.
- Fit test: print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material.
- Check: every part is green (fits, watertight, enough wall around the holes), orange or red, with the reason.
- Free cut: an extra cut at any angle through one part.
- Color per part in the exploded view.
- Magnets (Joint: Pins / Magnets): holes for disc magnets instead of pins, sizes 5x2, 6x2, 6x3, 8x3 and 10x3 mm (you buy the magnets). Each hole gets your clearance on the diameter and 0.3 mm extra depth for glue. A joint with less than 1.2 mm wall around the hole gets no hole and a message to glue it or pick a smaller magnet.
- Export all parts and pins as STL or 3MF in millimeters.
- Lay parts flat (on by default, in Export): every part is exported lying on a cut face (the largest one that still fits your printer), so it goes on the bed the right way up without supports under that face. A part with no cut face that fits keeps its own way up. Pins are not changed.
- Wrong unit (a millimeter model in a meter scene) is caught at once, with Convert to mm.
- Blender 4.2 and newer, tested in 4.2 and 5.3.
