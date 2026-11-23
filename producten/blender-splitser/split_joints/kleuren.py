"""Color per piece: every piece gets its own bright color, neighbors never share one.

Two looks (scene.split_joints.kleur):
PIECE: a color per piece from PALET, pins in gold. This is the look for the shop pictures and Shorts.
CHECK: green, orange or red from the check (controle.py), pins in green.
The color sits on a material of the piece mesh and on the object color, so it shows in Solid view with
Material and with Object color. The status (sj_status) and the export do not change.
The pure logic (verdeel, lineair) does not need bpy, so test_logica.py can test it."""

# Brand colors of Click Cuts first (merk/LEESMIJ.md: coral, cobalt, lilac), then bright colors that differ
# clearly from each other and from the gold of the pins: every pair at least 29 apart in CIELAB (keuring
# 23 nov K1: the old red, green and purple were 14 to 17 from coral, teal and lilac). sRGB hex.
PALET = ("FF5B3A", "3D5BFF", "A58CFF", "2EC4B6", "FF7AB8", "8BD346",
         "FF9F1C", "4CC9F0", "F2EBD9", "B5651D", "E040FB", "6A4C93")
GOUD = "FFD25C"
NAAM = "Click Cuts piece {:02d}"


def lineair(hex_):
    """sRGB hex to linear RGBA, the way Blender stores colors."""
    uit = []
    for i in (0, 2, 4):
        c = int(hex_[i:i + 2], 16) / 255.0
        uit.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (uit[0], uit[1], uit[2], 1.0)


def buren(a, b):
    """Two cells touch with a face: equal on two axes, one step apart on the third."""
    verschil = [abs(int(x) - int(y)) for x, y in zip(a, b)]
    return sorted(verschil) == [0, 0, 1]


def verdeel(cellen, n_kleuren=len(PALET)):
    """cellen: list of (i, j, k) in piece order. Gives a color index per piece.
    Greedy: each piece takes the color that no neighbor has and that is used least so far (ties: lowest
    index), so a few pieces get the brand colors and many pieces spread over the whole palette.
    A cell has at most 6 face neighbors, so with 7 or more colors no neighbor ever shares a color."""
    keuze = []
    gebruikt = [0] * n_kleuren
    for i, c in enumerate(cellen):
        bezet = {keuze[j] for j in range(i) if buren(c, cellen[j])}
        vrij = [k for k in range(n_kleuren) if k not in bezet] or list(range(n_kleuren))
        k = min(vrij, key=lambda x: (gebruikt[x], x))
        keuze.append(k)
        gebruikt[k] += 1
    return keuze


def _materiaal(naam, kleur):
    import bpy
    mat = bpy.data.materials.get(naam)
    if mat is None:
        mat = bpy.data.materials.new(naam)
        mat.use_nodes = True
    mat.diffuse_color = kleur
    bsdf = mat.node_tree.nodes.get("Principled BSDF") if mat.node_tree else None
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = kleur
    return mat


def _geef(ob, mat, kleur):
    ob.data.materials.clear()
    ob.data.materials.append(mat)
    for p in ob.data.polygons:
        p.material_index = 0
    ob.color = kleur


def zet(scene):
    """Colors all pieces and pin plates of the scene in the chosen look."""
    from . import controle
    stukken = sorted((o for o in scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])
    pennen = [o for o in scene.objects if o.get("sj_pennen")]
    if scene.split_joints.kleur == "CHECK":
        for o in stukken:
            status = o.get("sj_status", "groen")
            _geef(o, controle.materiaal(status), controle.KLEUREN[status])
            o["sj_kleur"] = -1
        for o in pennen:
            _geef(o, controle.materiaal("groen"), controle.KLEUREN["groen"])
        return
    cellen = [tuple(o.get("sj_cel", (o["sj_stuk"], 0, 0))) for o in stukken]
    for o, k in zip(stukken, verdeel(cellen)):
        kleur = lineair(PALET[k])
        _geef(o, _materiaal(NAAM.format(int(o["sj_stuk"])), kleur), kleur)
        o["sj_kleur"] = k
    goud = lineair(GOUD)
    for o in pennen:
        _geef(o, _materiaal("Click Cuts pins", goud), goud)
