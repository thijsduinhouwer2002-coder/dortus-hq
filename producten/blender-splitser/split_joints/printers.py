"""Printer presets: build volume in millimeters (X, Y, Z).

Source for every number: the printer profiles of OrcaSlicer (resources/profiles/<vendor>/machine/*.json,
printable_area and printable_height), read on 23 Nov 2026. No bpy here, so the test can import it directly."""

# key, label, (x, y, z) in mm
PRINTERS = (
    ("A1MINI", "Bambu Lab A1 mini", (180.0, 180.0, 180.0)),
    ("A1", "Bambu Lab A1", (256.0, 256.0, 256.0)),
    ("X1P1", "Bambu Lab X1 / P1 series", (256.0, 256.0, 250.0)),
    ("H2D", "Bambu Lab H2D", (350.0, 320.0, 325.0)),
    ("MK4", "Prusa MK4", (250.0, 210.0, 220.0)),
    ("COREONE", "Prusa Core One", (250.0, 220.0, 270.0)),
    ("MINI", "Prusa MINI", (180.0, 180.0, 180.0)),
    ("ENDER3", "Creality Ender 3 / Ender 3 V3 SE", (220.0, 220.0, 250.0)),
    ("K1", "Creality K1", (220.0, 220.0, 250.0)),
)

EIGEN = "CUSTOM"


def items():
    """Items for the EnumProperty: every preset plus Custom."""
    lijst = [(k, naam, f"{naam}: {x:g} x {y:g} x {z:g} mm") for k, naam, (x, y, z) in PRINTERS]
    lijst.append((EIGEN, "Custom size", "Type your own build volume"))
    return lijst


def maat(sleutel, eigen=(200.0, 200.0, 200.0)):
    """Build volume (x, y, z) in mm for a preset key, or the custom size."""
    for k, _naam, m in PRINTERS:
        if k == sleutel:
            return m
    return tuple(float(v) for v in eigen)


def bruikbaar(bed, marge):
    """Build volume minus the margin on every side in X and Y, and on top in Z."""
    x, y, z = bed
    return (max(1.0, x - 2 * marge), max(1.0, y - 2 * marge), max(1.0, z - marge))


def past(afmeting, bed):
    """True if a box with these dimensions fits in the build volume in some 90 degree orientation."""
    return all(a <= b + 1e-6 for a, b in zip(sorted(afmeting), sorted(bed)))
