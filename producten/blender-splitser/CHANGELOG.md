# Click Cuts changelog

## 1.1.0 (after the launch of 1.0.0)
- New: Draw cut. After Split to fit, click a part, press Draw cut and drag a line where you want it cut, for example under the chin or at the shoulder.
- New: before you cut, the part that comes off lights up white with an arrow that says "comes off". Wrong part? Press Flip side.
- New: the clearance starts at a value for your material until you save a fit test: Resin 0.10, PLA 0.20, PETG and ABS / ASA 0.25, TPU 0.30 mm. The fit test block covers that value.
- Better: after Split to fit, the result box names the clearance the parts were cut with, and tells you to split again when you change it.
- New: a ? in the panel header opens the guide on dortus.com/click-cuts/. Right click any Click Cuts button and choose Online Manual to jump to its part of the guide.

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
