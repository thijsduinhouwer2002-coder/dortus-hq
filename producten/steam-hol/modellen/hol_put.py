"""Hol met de stekelput van een gekochte stap (Bram 14 nov 2026, voor de pijplijn).

Draait Daans `ontwerp/steam/put-3d/put_stappen.py` (Mila's hol.py met alleen de put aangepast) met STAP uit het
laatste argument: dezelfde args als hol.py plus de stap. De pijplijn knipt daaruit `put_1` en `put_2` op de plek van
`put`, zodat `hol_3d.gd` `put_stuk()` ze vanzelf vindt. HOL_VERBERG werkt zoals bij hol.py.

Gebruik: python hol_put.py <uit> <w> <h> <samples> <gloop> <hoeden> <stap>
"""
import os, sys, runpy

HIER = os.path.dirname(os.path.abspath(__file__))
os.environ["STAP"] = sys.argv[-1]
sys.argv = [os.path.join(HIER, "hol.py")] + sys.argv[1:-1]
runpy.run_path(os.path.join(HIER, "..", "..", "..", "ontwerp", "steam", "put-3d", "put_stappen.py"), run_name="__main__")
