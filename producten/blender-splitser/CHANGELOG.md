# Click Cuts changelog

## 1.0.0 (candidate, 25 Nov 2026)
First version.
- Split to fit: one button cuts the selected model into parts that fit your printer bed, with pins, pin holes and part numbers.
- Printer list with usable bed size, or your own size.
- Fit test: print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material.
- Check: every part is green (fits, watertight, enough wall around the holes), orange or red, with the reason.
- Free cut: an extra cut at any angle through one part.
- Color per part in the exploded view.
- Export all parts and pins as STL or 3MF in millimeters.
- Lay parts flat (on by default, in Export): every part is exported lying on a cut face (the largest one that still fits your printer), so it goes on the bed the right way up without supports under that face. A part with no cut face that fits keeps its own way up. Pins are not changed.
- Wrong unit (a millimeter model in a meter scene) is caught at once, with Convert to mm.
- Blender 4.2 and newer, tested in 4.2 and 5.3.
