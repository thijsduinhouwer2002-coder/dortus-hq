"""Color per piece (kleuren.py), called from test_kern.py after every split model.
Measured on the scene: every piece its own material and object color from the palette, face neighbors never
the same color, pins gold; Check gives green, orange or red from the status and pins green; back to Per piece
gives the same colors again; the mesh and the status do not change."""
import bpy

from hulp import log, pen_objecten, stap, stukken

def lineair(hex_):
    uit = []
    for i in (0, 2, 4):
        c = int(hex_[i:i + 2], 16) / 255.0
        uit.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return uit


def gelijk(a, b, tol=1e-3):
    return all(abs(x - y) < tol for x, y in zip(list(a)[:3], list(b)[:3]))


def buren(a, b):
    return sorted(abs(int(x) - int(y)) for x, y in zip(a, b)) == [0, 0, 1]


def toets(naam):
    inst = bpy.context.scene.split_joints
    lijst = stukken()
    pennen = pen_objecten()
    stap(f"{naam} kleur: standaard Per piece", inst.kleur == "PIECE", inst.kleur)
    vorm = {o.name: (len(o.data.vertices), len(o.data.polygons)) for o in lijst}
    status = {o.name: o.get("sj_status") for o in lijst}
    goed = True
    for o in lijst:
        mats = [m for m in o.data.materials if m]
        ok = len(mats) == 1 and mats[0].name == f"Click Cuts piece {int(o['sj_stuk']):02d}" and \
            gelijk(mats[0].diffuse_color, o.color) and int(o.get("sj_kleur", -1)) >= 0
        goed &= ok
        if not ok:
            log(f"{naam} kleur: stuk {o['sj_stuk']} materialen {[m.name for m in mats]}, kleur {list(o.color)}")
    stap(f"{naam} kleur: elk stuk een eigen materiaal met dezelfde objectkleur", goed)
    paren = [(a, b) for i, a in enumerate(lijst) for b in lijst[i + 1:] if buren(a["sj_cel"], b["sj_cel"])]
    zelfde = [(a["sj_stuk"], b["sj_stuk"]) for a, b in paren if gelijk(a.color, b.color)]
    stap(f"{naam} kleur: buren nooit dezelfde kleur", not zelfde, f"{len(paren)} paren buren, gelijk {zelfde}")
    soorten = {tuple(round(c, 3) for c in o.color[:3]) for o in lijst}
    stap(f"{naam} kleur: verschillende kleuren", len(soorten) >= min(len(lijst), 3), f"{len(soorten)} kleuren voor {len(lijst)} stukken")
    stap(f"{naam} kleur: pennen goud", all(gelijk(p.color, lineair("FFD25C")) for p in pennen), f"{len(pennen)} plaatjes")
    voor = {o.name: tuple(o.color) for o in lijst}

    inst.kleur = "CHECK"
    from_status = {"groen": (0.0, 0.84, 0.59), "oranje": (1.0, 0.55, 0.0), "rood": (1.0, 0.30, 0.30)}
    goed = all(gelijk(o.color, from_status[o["sj_status"]]) and o.data.materials[0].name in ("Click Cuts green", "Click Cuts orange", "Click Cuts red")
               for o in lijst)
    stap(f"{naam} kleur: Check geeft groen, oranje of rood per status", goed,
         f"{sorted({o['sj_status'] for o in lijst})}")
    stap(f"{naam} kleur: Check maakt pennen groen", all(gelijk(p.color, from_status["groen"]) for p in pennen))

    inst.kleur = "PIECE"
    stap(f"{naam} kleur: terug naar Per piece geeft dezelfde kleuren",
         all(gelijk(o.color, voor[o.name]) for o in lijst))
    stap(f"{naam} kleur: mesh en status blijven gelijk",
         all((len(o.data.vertices), len(o.data.polygons)) == vorm[o.name] and o.get("sj_status") == status[o.name]
             for o in lijst))
