"""Hoedenwand (Mila, 16 nov 2026): een hoed van een opgegeten held, scheef half begraven in de aardwand.
Rendert alleen holte + hoed + aardrand op een doorzichtige achtergrond, zodat het spel hem op de wand boven de gang legt.
Zelfde camera en licht als alle 3D (gedeeld.py). Hoeden uit producten/steam-hol/modellen/hoeden.py.
    <venv>/bin/python hoedenwand.py <uit.png> <breedte> <hoogte> <samples> <nr> <kantel>
"""
import sys, os, math
M = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../producten/steam-hol/modellen'))
sys.path.insert(0, M)
import bpy
import gedeeld as g
import hoeden

def bol(naam, loc, schaal, mat, segs=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc)
    o = bpy.context.active_object; o.name = naam; o.scale = schaal
    o.data.materials.append(mat); bpy.ops.object.shade_smooth()
    return o

def _mat_kleur(naam, hexkleur):
    """Kleur van een bestaand hoedmateriaal veranderen (alleen in de wand, hoeden.py blijft gelijk)."""
    m = bpy.data.materials.get(naam)
    if m:
        m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*g.hex2(hexkleur), 1)

PET_KLEP_LOC = (0.25, -0.38, 0.12)
PET_KLEP_ROT = (-60, 0, -25)

def wand_beter(nr, h):
    """Moets van Daan (16 nov 09:50) voor de hoedenwand, alleen hier:
    kap (2): punt bovenop en donkere rand, anders leest hij als een klodder slijm;
    pet (3): witte klep die goed uitsteekt, anders lijkt hij op de rode paddenstoel;
    hoge hoed (7) en pan (8): warm randlicht van boven en een lichtere holte, anders verdwijnen ze in het gat."""
    R = math.radians
    if nr == 2:
        donker = g.mat("kaprand_wand", "1f3a17", rough=0.8)
        for o in h.children_recursive if hasattr(h, "children_recursive") else h.children:
            if o.active_material and o.active_material.name.startswith("kaprand"):
                o.active_material = donker
                o.scale = (o.scale[0] * 1.03, o.scale[1] * 1.03, o.scale[2] * 2.2)
        _mat_kleur("kap", "4a7a2a")
        # punt: een kegel bovenop die iets naar rechts knakt (een kap van een woudloper, geen bolletje)
        bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=0.2, radius2=0.0, depth=0.42, location=(0.08, 0.04, 0.55))
        k = bpy.context.object; k.rotation_euler = (0, R(18), 0)
        k.data.materials.append(bpy.data.materials["kap"]); bpy.ops.object.shade_smooth()
        k.parent = h

        # leren band om de kap, net boven de aardrand: donkere rand die je wel ziet (stof, geen slijm)
        bpy.ops.mesh.primitive_torus_add(major_radius=0.47, minor_radius=0.045, location=(0, 0.04, 0.12))
        n = bpy.context.object; n.scale = (0.97, 0.97, 1.0)
        n.data.materials.append(donker); bpy.ops.object.shade_smooth(); n.parent = h
    elif nr == 3:
        _mat_kleur("klep", "f4f1ea")
        for o in h.children:
            if o.active_material and o.active_material.name == "klep":
                o.scale = (o.scale[0] * 1.05, o.scale[1] * 1.05, o.scale[2] * 1.6)
                o.location = PET_KLEP_LOC
                o.rotation_euler = tuple(R(x) for x in PET_KLEP_ROT)
            if o.active_material and o.active_material.name == "petknoop":
                o.hide_render = True   # witte stip bovenop maakt hem een paddenstoel
    elif nr in (7, 8):
        bpy.data.materials["holte"].node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*g.hex2("4a2a1e"), 1)
        lamp = bpy.data.lights.new("randlicht", "AREA"); lamp.energy = 260; lamp.size = 1.2
        lamp.color = (1.0, 0.62, 0.32)
        lo = bpy.data.objects.new("randlicht", lamp); bpy.context.scene.collection.objects.link(lo)
        lo.location = (0.4, 1.4, 2.2); lo.rotation_euler = (R(-35), 0, 0)

def maak(nr, kantel):
    g.leeg()
    g.camera(hoogte_midden=0.3, schaal=2.7)
    g.licht()
    holte = g.mat("holte", "2e1712", rough=0.95, spec=0.05)
    aarde = g.mat("aarde", "684033", rough=0.9, spec=0.1)
    aarde_l = g.mat("aarde_l", "8e5949", rough=0.85, spec=0.15)
    steen = g.mat("steen", "c69383", rough=0.6, spec=0.3)
    # holte: donkere platte schaal net achter de hoed
    bol("holte", (0, 0.35, 0.28), (0.78, 0.12, 0.52), holte)
    # de hoed, scheef, een stuk naar achteren zodat hij IN de wand zit
    hoeden.bouw(nr, plek=(0, 0.05, 0.02), schaal=1.25, kantel=0, draai=0)
    h = bpy.data.objects["hoed_" + hoeden.NAMEN[nr % 10]]
    h.rotation_euler[1] = math.radians(kantel)   # zijwaarts om, zoals een hoed die viel en bleef steken
    bpy.context.view_layer.update()
    wand_beter(nr, h)
    # aardrand voor de onderkant: plat (dat is het wandvlak), met een kam van kluitjes langs de bovenrand en steentjes
    bol("rand", (0, -0.45, -0.22), (1.0, 0.08, 0.36), aarde)
    import random; random.seed(nr)
    for i in range(11):
        x = -0.85 + i * 0.17 + random.uniform(-0.03, 0.03)
        z = 0.1 - abs(x) * 0.18 + random.uniform(-0.03, 0.03)
        r = random.uniform(0.08, 0.12)
        bol("kluit", (x, -0.5, z), (r, r * 0.7, r * 0.8), aarde_l if i % 3 else aarde, segs=16)
    for x, z, r in [(-0.6, -0.15, 0.05), (0.5, -0.1, 0.045), (0.1, -0.3, 0.04)]:
        bol("steen", (x, -0.56, z), (r, r * 0.8, r * 0.85), steen, segs=16)

if __name__ == "__main__":
    uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    maak(int(sys.argv[5]), float(sys.argv[6]))
    g.render(uit, W, H, S, doorzichtig=True)
