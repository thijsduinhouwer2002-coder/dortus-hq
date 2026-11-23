"""Proef (23 nov, Olaf): hele Figure from rig van Pro 1.2.0 op AI-figuren (Meshy) die nog niet in de e2e zitten.

Opdracht hoofdchat 23 nov: werkt Figure from rig op AI-gemaakte figuren, en waar valt een gewricht weg?
Zelfde opzet als proef_meshy_rig.py (150 mm, Make watertight, rig met Mixamo-namen uit doorsneden), maar met alle
gewrichten (geen CJ_ALLEEN) en met een draai vooraf: niet elke Meshy-figuur kijkt na het inladen naar +x zoals
proef_ai_model.laad aanneemt (man_cap_jeans_jacket keek opzij, GEZIEN in een render). Deze proef draait de figuur
zo dat de benen naast elkaar op de x-as staan en de voeten naar -y wijzen, voordat de rig erin komt (na Make watertight, want ervoor valt een doorsnede in losse snippers uiteen).

Gebruik: blender -b --factory-startup --python e2e/proef_ai_figuren.py -- <betaalde zip> <uitmap> <model.glb> [...]
Uitslag in het log, regels met [cj-mrig] en [cj-draai]. Beelden: blender -b <uit>/<naam>_rig.blend --python
e2e/kijk_figuur.py -- <uitmap>.
"""
import os

from mathutils import Vector

HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_meshy_rig.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
P = {"__name__": "proef_meshy_rig", "__file__": os.path.join(HIER, "proef_meshy_rig.py")}
exec(compile(_src, "proef_meshy_rig.py", "exec"), P)
A = P["A"]
_maak_rig = P["maak_rig"]


def _draai(ob, kwart):
    for _ in range(kwart % 4):
        for v in ob.data.vertices:
            v.co = Vector((v.co.y, -v.co.x, v.co.z))
    ob.data.update()


def _benen(ob):
    """Twee losse beenlussen op 20 tot 32% van de hoogte: (midden1, midden2) of None."""
    for p in (27, 25, 29, 23, 31, 20):
        ls = [l for l in A["lussen"](ob, p / 100.0 * A["HOOGTE_MM"]) if l[1] >= 5.0 and l[2] >= 5.0]
        if len(ls) >= 2:
            a, b = sorted(ls, key=lambda l: l[1] * l[2], reverse=True)[:2]
            return a[0], b[0]
    return None


def rig_rechtop(ob):
    """Na Make watertight (dan zijn de doorsneden schone lussen) de figuur draaien, daarna de rig van proef_meshy_rig."""
    H = A["HOOGTE_MM"]
    kwart = 0
    bn = _benen(ob)
    if bn is not None and abs((bn[0] - bn[1]).y) > abs((bn[0] - bn[1]).x):
        kwart = 1
        _draai(ob, 1)
    # voorkant: de tenen steken verder naar voren dan de enkel; vooraanzicht kijkt naar +y, dus voor = -y
    zool = [v.co.y for v in ob.data.vertices if v.co.z < 0.03 * H]
    enkel = [v.co.y for v in ob.data.vertices if 0.08 * H < v.co.z < 0.12 * H]
    if zool and enkel and min(zool) > min(enkel) - 0.5 and max(zool) > max(enkel) + 0.5:
        kwart += 2
        _draai(ob, 2)
    print(f"[cj-draai] {ob.name}: benen {'naast elkaar' if bn else 'niet los'}, gedraaid {90 * (kwart % 4)} graden",
          flush=True)
    return _maak_rig(ob)


P["maak_rig"] = rig_rechtop
P["main"]()
