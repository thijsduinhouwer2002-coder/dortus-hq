#!/usr/bin/env python3
"""YouTube Shorts reeks 5 (22 nov 2026, Chris): 2 staande Shorts van 40 tot 60 s uit de monster-opname (opname.py).
Gebruikt kort.py van reeks 4 (zelfde uitsnede, muis, ondertitels, geluid) met eigen teksten per Short; alleen wat de
opname meet komt in beeld (aantal gewrichten en de stop van de knie uit film.json).
    CJ_MONSTER=Yeti python3 kort.py <map met opname-ruw.mkv en film.json> <uitmap>"""
import os
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
BRON = HIER.parent / "youtube-shorts-4" / "kort.py"
src = BRON.read_text(encoding="utf-8")

SHORTS = r'''
MON = os.environ.get("CJ_MONSTER") or MT.get("monster", "monster")
EEN = "an" if MON[:1].lower() in "aeiou" else "a"
SHORTS = {
    (1, f"{MON.lower()}-posable"): [
        ("@render-1.png", 0, H, 1, None, (f"Make {EEN} {MON}", "posable for 3D printing", YH)),
        ("heel", 0, None, 1, "knop", ("1. Select the", "rigged model")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("2. Press", "Figure from rig")),
        ("lijst", 0, None, 1, "lijst", (f"{N_GEW} joints, each", "with its range")),
        ("knie", 0, None, 1, None, ("3. Bend the knee", "to its end stop")),
        ("knie_stop", 0, None, 1, "knie", (f"End stop:", f"{K_STOP}°")),
        ("knie_rood", 0, 96, 1, "knie", ("Past the stop: red arc", f"and +{VOORBIJ}° past limit")),
        ("knie_rood", 96, None, 1, "knie", None),
        ("pose", 0, None, 1, "knie", ("Pose it", "and check the fit")),
        ("uitelkaar", 0, 168, 1, None, ("4. Exploded view:", "see every part")),
        ("export", 0, None, 1, None, ("5. Export every part", "as 3MF")),
        ("held", 0, 120, 1, "held", ("Print a test joint", "first")),
    ],
    (2, f"{MON.lower()}-printable-parts"): [
        ("@render-3.png", 0, H, 1, None, (f"{MON} into", "printable parts", YH)),
        ("heel", 0, None, 2, "knop", ("Free CC0 model", "with its own rig")),
        ("kies", 0, None, 2, "knop", None),
        ("knop", 0, None, 2, "knop", ("Press", "Figure from rig")),
        ("lijst", 0, 100, 2, "lijst", ("Cut into parts", f"with {N_GEW} joints")),
        ("uitelkaar", 0, 168, 2, None, ("Exploded view:", "every part apart")),
        ("uitelkaar", 168, None, 2, None, ("Check each joint", "up close")),
        ("export", 0, None, 2, None, ("Pick 3MF,", "then Export")),
        ("@render-4.png", 0, 105, 1, None, ("One 3MF file", "per part", YH)),
    ],
}
'''
a = src.index("SHORTS = {")
b = src.index("\nmeting = {}")
src = src[:a] + SHORTS + src[b:]
src = "import os\n" + src
sys.argv = [str(BRON)] + sys.argv[1:]
g = {"__name__": "__main__", "__file__": str(BRON)}
exec(compile(src, str(BRON), "exec"), g)   # noqa: S102 (eigen code uit de repo)
