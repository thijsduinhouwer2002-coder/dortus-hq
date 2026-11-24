# Gedeelde hulpcode voor Blender-opnames (Olaf, 24 nov 2026)

Voor de Regisseur: elke `regisseur-N/tip_opname.py` had ±300 regels gekopieerde hulpcode. `blender_opname.py` is die
code (gelijk aan regisseur-12) op één plek, plus:

- `menu_pad(vak, ["File", "Export", "STL"], "meet")`: menu, submenu en item met de echte muis, met de lessen van run 7
  en 12 erin (wachten tot het menu getekend is, muis een tikje bewegen, eerst horizontaal het submenu in). Geeft False
  na twee keer Escape als iets niet raakte: dan je eigen vangnet.
- `knop(tekst, vak)`: OCR met drempels 35, 60 en 75 % (witte tekst op een blauwe knop).
- `typ("1000")`: zichtbaar typen, teken voor teken.
- `start(verloop)` en `einde()`: de timer, film.json bij een fout, KORT klaar.
- `bovenbalk()`, `dubbelklik()`, `zet_scherm(mm=False)` voor Unit Scale 1, `maat_mm(ob, per_eenheid)`.

Een nieuwe opname begint zo:

```python
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403
zet_naam("tip13")

def verloop():
    a = zet_scherm()
    ...
    deel("eind")
    einde()

start(verloop)
```

**Let op in de workflow:** neem dit bestand mee in de sha van "Ruwe opname hergebruiken", anders blijft na een wijziging
hier een oude opname staan:

```bash
nu=$(cat commercie/filmpjes/regisseur-13/tip_opname.py commercie/filmpjes/opname/blender_opname.py | sha256sum | cut -c1-64)
```

Bewijs dat het hetzelfde doet: `proef_tip12.py` is de opname van regisseur-12 op deze code (198 regels in plaats van
547). Workflow `opname-gedeeld-proef.yml` neemt hem op en vergelijkt delen en metingen met release regisseur-12; uitslag
onderaan `../regisseur-log.md`.

Oude opnames (regisseur-3 tot en met 12) blijven zoals ze zijn; niets daarvan hoeft om.
