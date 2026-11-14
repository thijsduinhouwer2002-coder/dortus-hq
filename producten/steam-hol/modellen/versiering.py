"""Versiering van het hol in 3D (Daan, 14 nov 2026). Vervangt kunst/versiering.png en kunst/maaiveld.png.

Namen zoals in godot/hol/hol_3d.gd:
  gang (op de vloer):      paddenstoel, lichtzwam, ton, krat, schedel, kristal
  gang (aan het plafond):  spinrag, stut, vaandel
  maaiveld (op het gras):  bloemen, struik, steen, bordje, vliegenzwam
Zelfde schaal, camera en hoek als hol.py (120 px = 4,5 eenheden, één spelpixel = 0,1125), zachte vormen, mat zoals de kist,
geen zwarte randen. Elk ding is dikker en eenvoudiger dan in het echt, zodat het op 120 px (3 px per spelpixel) leest.

Als module (bv. in hol.py):
    import versiering as v
    v.bouw(naam, x, z, y=0.35)   # staand: (x, z) is het voetpunt; hangend (HANGT): het hangpunt aan het plafond
  Alle objecten heten "deco_<naam>..." zodat de pijplijn ze met HOL_ALLEEN ["deco_"] los kan renderen.
Los: alles in één beeld van 240 x 40 spelpixels op de plekken van het hol (gang op de gangvloer, maaiveld op het gras):
    <venv>/bin/python versiering.py <uit.png> <breedte> <hoogte> <samples>
  Schrijft ook <uit>_vakken.json: per naam het vak [x, y, b, h] en het voet- of hangpunt, in spelpixels van dat beeld.
"""
import sys, os, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g

SPX = 4.5 / 40
HANGT = ("spinrag", "stut", "vaandel")
GANG = ("paddenstoel", "lichtzwam", "ton", "krat", "schedel", "kristal", "spinrag", "stut", "vaandel")
MAAIVELD_NAMEN = ("bloemen", "struik", "steen", "bordje", "vliegenzwam")
GANG_HOOG = 16 * SPX * 0.966 / 0.966  # 16 spelpixels gang (vloer z 0 tot plafond)

_M = {}
SCHAAL = {"ton": 0.78, "krat": 0.82}


def m(naam, kleur, **kw):
    if naam not in _M:
        _M[naam] = g.mat("deco_" + naam, kleur, **kw)
    return _M[naam]


def _af(o, mat, ouder, naam, glad=True):
    o.name = naam
    o.data.materials.append(mat)
    o.parent = ouder
    if glad:
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.shade_smooth()
    return o


def bol(ouder, naam, loc, schaal, mat, segs=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=max(8, segs // 2), location=loc)
    o = bpy.context.object; o.scale = schaal
    return _af(o, mat, ouder, naam)


def cil(ouder, naam, loc, r, d, mat, rot=(0, 0, 0), verts=24, r2=None, glad=True):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    return _af(bpy.context.object, mat, ouder, naam, glad)


def blok(ouder, naam, loc, maat, mat, rond=0.03, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = maat
    if rond:
        b = o.modifiers.new("rond", "BEVEL"); b.width = rond; b.segments = 3; b.limit_method = "NONE"
    return _af(o, mat, ouder, naam, glad=False)


def hoed_zwam(ouder, pre, x, hoog, r, hoedmat, steelmat, stippen=True, scheef=0.0):
    """Paddenstoel: steel en een bolle hoed, witte stippen op de voorkant."""
    cil(ouder, pre + "_steel", (x, 0, hoog / 2), r * 0.42, hoog, steelmat, r2=r * 0.34)
    h = bol(ouder, pre + "_hoed", (x, 0, hoog), (r, r, r * 0.62), hoedmat, 32)
    h.rotation_euler = (0, scheef, 0)
    # onderkant van de hoed: lichte plaat, zodat hij niet zweeft
    cil(ouder, pre + "_plaat", (x, 0, hoog - r * 0.05), r * 0.92, r * 0.08, steelmat)
    if stippen:
        wit = m("stip", "fff4e6", rough=0.5)
        for dx, dz, s in ((-0.45, 0.3, 0.2), (0.35, 0.42, 0.17), (0.0, 0.55, 0.15), (0.62, 0.12, 0.13)):
            bol(ouder, pre + "_stip", (x + dx * r, -r * 0.62, hoog + dz * r * 0.62), (s * r, s * r * 0.5, s * r), wit, 12)


def bouw(naam, x, z, y=0.35):
    ouder = bpy.data.objects.new("deco_" + naam, None)
    bpy.context.scene.collection.objects.link(ouder)
    p = "deco_" + naam
    s = SPX
    hout = m("hout", "8a4b2a", rough=0.7, spec=0.2)
    hout_d = m("hout_d", "6e4632", rough=0.75, spec=0.2)
    ijzer = m("ijzer", "4a4452", rough=0.45, metaal=0.7)
    room = m("room", "f3e6cf", rough=0.6)
    if naam == "paddenstoel":
        rood = m("rood", "d9483b", rough=0.45, spec=0.4)
        hoed_zwam(ouder, p + "_a", -1.6 * s, 4.6 * s, 3.0 * s, rood, room)
        hoed_zwam(ouder, p + "_b", 2.9 * s, 2.6 * s, 1.8 * s, rood, room, scheef=0.25)
    elif naam == "lichtzwam":
        munt = m("munt", "4fd8b0", rough=0.35, emis=0.45)
        steel = m("steel_licht", "bfe8da", rough=0.5, emis=0.1)
        hoed_zwam(ouder, p + "_a", -1.8 * s, 6.0 * s, 2.2 * s, munt, steel, stippen=False)
        hoed_zwam(ouder, p + "_b", 1.6 * s, 3.4 * s, 1.6 * s, munt, steel, stippen=False, scheef=-0.2)
        hoed_zwam(ouder, p + "_c", 3.9 * s, 2.0 * s, 1.0 * s, munt, steel, stippen=False, scheef=0.3)
        l = bpy.data.lights.new(p + "_licht", "POINT"); l.color = (0.55, 1.0, 0.85); l.energy = 4; l.shadow_soft_size = 0.2
        lo = bpy.data.objects.new(p + "_licht", l); lo.location = (0, -0.25, 4 * s); lo.parent = ouder
        bpy.context.scene.collection.objects.link(lo)
    elif naam == "ton":
        # bolle ton: cilinder met dikke buik (bevel en schaal), twee ijzeren banden, deksel donkerder
        bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=4.6 * s, depth=11 * s, location=(0, 0, 5.5 * s))
        o = bpy.context.object
        sd = o.modifiers.new("buik", "SIMPLE_DEFORM"); sd.deform_method = "TAPER"; sd.factor = 0.0
        _af(o, hout, ouder, p + "_lijf")
        bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.subdivide(number_cuts=4); bpy.ops.object.mode_set(mode="OBJECT")
        for v in o.data.vertices:
            t = v.co.z / (5.5 * s)  # -1 .. 1
            f = 1.0 + 0.16 * (1 - t * t)
            v.co.x *= f; v.co.y *= f
        for zz in (2.6 * s, 8.4 * s):
            cil(ouder, p + "_band", (0, 0, zz), 5.15 * s, 0.9 * s, ijzer)
        cil(ouder, p + "_deksel", (0, 0, 11 * s), 4.3 * s, 0.3 * s, hout_d)
        for i in range(-2, 3):  # duigen als lichte naden op de voorkant
            blok(ouder, p + "_naad", (i * 1.8 * s, -5.05 * s * (1 - 0.1 * abs(i)), 5.5 * s), (0.18 * s, 0.2 * s, 9.6 * s), hout_d, rond=0)
    elif naam == "krat":
        blok(ouder, p + "_kist", (0, 0, 4.8 * s), (9.6 * s, 8 * s, 9.6 * s), hout, rond=0.5 * s)
        for sx in (-1, 1):  # rand
            blok(ouder, p + "_rand", (sx * 4.2 * s, -4.1 * s, 4.8 * s), (1.3 * s, 0.6 * s, 9.6 * s), hout_d, rond=0.2 * s)
        for sz in (0.55, 9.05):
            blok(ouder, p + "_rand", (0, -4.1 * s, sz * s), (9.6 * s, 0.6 * s, 1.3 * s), hout_d, rond=0.2 * s)
        blok(ouder, p + "_kruis", (0, -4.15 * s, 4.8 * s), (11 * s, 0.5 * s, 1.3 * s), hout_d, rond=0.2 * s,
             rot=(0, math.radians(45), 0))
    elif naam == "schedel":
        bot = m("bot", "eee6d8", rough=0.55)
        gat = m("gat", "2a1832", rough=0.9)
        bol(ouder, p + "_kop", (-0.8 * s, 0, 3.6 * s), (3.0 * s, 2.7 * s, 2.7 * s), bot, 32)
        blok(ouder, p + "_kaak", (-0.8 * s, -0.4 * s, 1.0 * s), (3.6 * s, 3.2 * s, 1.8 * s), bot, rond=0.7 * s)
        for sx in (-1, 1):
            bol(ouder, p + "_oog", (-0.8 * s + sx * 1.15 * s, -2.45 * s, 3.4 * s), (0.85 * s, 0.4 * s, 0.95 * s), gat, 16)
        bol(ouder, p + "_neus", (-0.8 * s, -2.55 * s, 2.2 * s), (0.35 * s, 0.25 * s, 0.45 * s), gat, 12)
        # botje ernaast
        cil(ouder, p + "_bot", (3.6 * s, -0.6 * s, 0.55 * s), 0.45 * s, 3.4 * s, bot, rot=(0, math.radians(90), math.radians(-20)))
        for dx in (-1.7, 1.7):
            bol(ouder, p + "_knobbel", (3.6 * s + dx * s * 0.94, -0.6 * s + dx * s * 0.34, 0.6 * s), (0.7 * s, 0.7 * s, 0.6 * s), bot, 12)
    elif naam == "kristal":
        groen = m("kristal", "2fb889", rough=0.12, spec=0.8, emis=0.25)
        licht = m("kristal_l", "5fe0b0", rough=0.1, spec=0.8, emis=0.3)
        voet = m("kristal_voet", "4e3158", rough=0.85)
        bol(ouder, p + "_steen", (0, 0.1, 0.4 * s), (4.6 * s, 2.6 * s, 1.4 * s), voet, 16)
        for i, (dx, hoog, r, kant, mt) in enumerate(((0, 9.0, 1.7, 0, groen), (-2.4, 6.4, 1.4, -26, licht),
                                                     (2.4, 7.0, 1.45, 24, groen), (-4.4, 3.8, 1.0, -48, groen),
                                                     (4.4, 4.2, 1.0, 46, licht))):
            a = math.radians(kant)
            z0 = 0.6 * s
            # zeskantige zuil met een punt, plat gearceerd zodat de vlakken glinsteren
            lang = hoog * 0.72 * s
            cx, cz = dx * s + math.sin(a) * lang / 2, z0 + math.cos(a) * lang / 2
            cil(ouder, p + f"_zuil{i}", (cx, -0.2 * s, cz), r * s, lang, mt, rot=(0, a, 0), verts=6, glad=False)
            px, pz = dx * s + math.sin(a) * (lang + hoog * 0.14 * s), z0 + math.cos(a) * (lang + hoog * 0.14 * s)
            cil(ouder, p + f"_punt{i}", (px, -0.2 * s, pz), r * s, hoog * 0.28 * s, mt, rot=(0, a, 0), verts=6, r2=0.0, glad=False)
        l = bpy.data.lights.new(p + "_licht", "POINT"); l.color = (0.5, 1.0, 0.75); l.energy = 3; l.shadow_soft_size = 0.2
        lo = bpy.data.objects.new(p + "_licht", l); lo.location = (0, -0.35, 5 * s); lo.parent = ouder
        bpy.context.scene.collection.objects.link(lo)
    elif naam == "spinrag":
        web = m("web", "ddd4e8", rough=0.6, emis=0.12)
        zw = m("spin", "2a1832", rough=0.6)
        oog = m("spinoog", "ff6a5a", rough=0.3, emis=1.0)
        # waaier van draden vanuit de linkerbovenhoek, met twee bogen dwars
        mid = (-6.5 * s, -0.1, 0)
        for k in range(5):
            a = math.radians(-90 + k * 22.5)
            lang = 7.5 * s
            cil(ouder, p + "_draad", (mid[0] + math.cos(a) * lang / 2 + lang / 2 * 0, mid[1], mid[2] + math.sin(a) * lang / 2 * 0.9),
                0.18 * s, lang, web, rot=(0, -a + math.pi / 2, 0), verts=6)
        for rr in (3.0, 5.6):
            for k in range(4):
                a1, a2 = math.radians(-90 + k * 22.5), math.radians(-90 + (k + 1) * 22.5)
                x1, z1 = math.cos(a1) * rr * s, math.sin(a1) * rr * s * 0.9
                x2, z2 = math.cos(a2) * rr * s, math.sin(a2) * rr * s * 0.9
                dx, dz = x2 - x1, z2 - z1
                cil(ouder, p + "_boog", (mid[0] + (x1 + x2) / 2, mid[1], (z1 + z2) / 2), 0.14 * s, math.hypot(dx, dz) * 1.1,
                    web, rot=(0, math.atan2(dx, dz), 0), verts=6)
        # spin aan een draadje
        cil(ouder, p + "_hangdraad", (1.5 * s, -0.1, -3.2 * s), 0.12 * s, 6.4 * s, web, verts=6)
        bol(ouder, p + "_lijf", (1.5 * s, -0.12, -7.0 * s), (1.5 * s, 1.2 * s, 1.5 * s), zw, 16)
        for sx in (-1, 1):
            bol(ouder, p + "_oog", (1.5 * s + sx * 0.55 * s, -0.12 - 1.15 * s, -7.0 * s), (0.35 * s,) * 3, oog, 8)
            for k in range(3):
                a = math.radians(-30 + k * 30)
                cil(ouder, p + "_poot", (1.5 * s + sx * 1.9 * s, -0.12, -7.0 * s + math.sin(a) * 1.2 * s),
                    0.2 * s, 2.4 * s, zw, rot=(0, sx * (math.pi / 2 - a * 0.6), 0), verts=6)
    elif naam == "stut":
        # twee palen tot op de vloer en een balk eronder tegen het plafond; hangpunt = midden bovenkant
        for sx in (-1, 1):
            blok(ouder, p + "_paal", (sx * 5.6 * s, 0, -8.6 * s), (1.9 * s, 1.9 * s, 15.2 * s), hout_d, rond=0.4 * s)
        blok(ouder, p + "_balk", (0, -0.1 * s, -1.2 * s), (14.4 * s, 2.2 * s, 2.2 * s), hout, rond=0.5 * s)
        for sx in (-1, 1):  # schoorhoutjes
            blok(ouder, p + "_schoor", (sx * 4.0 * s, -0.2 * s, -3.2 * s), (0.9 * s, 1.2 * s, 3.4 * s), hout_d, rond=0.2 * s,
                 rot=(0, sx * math.radians(40), 0))
        # spijkerkoppen
        for sx in (-1, 1):
            bol(ouder, p + "_spijker", (sx * 5.6 * s, -1.2 * s, -1.2 * s), (0.35 * s, 0.2 * s, 0.35 * s), ijzer, 8)
    elif naam == "vaandel":
        rood = m("vaandel", "c8423a", rough=0.75)
        goud = m("goud", "goud", rough=0.25, spec=0.8, metaal=0.8, emis=0.05)
        cil(ouder, p + "_stok", (0, -0.1 * s, -0.8 * s), 0.55 * s, 11.5 * s, hout_d, rot=(0, math.radians(90), 0))
        for sx in (-1, 1):
            bol(ouder, p + "_knop", (sx * 5.9 * s, -0.1 * s, -0.8 * s), (0.8 * s,) * 3, goud, 12)
        # doek met een zwaluwstaart onderaan, licht bol
        vb = [(-4.2, -1.6), (4.2, -1.6), (4.2, -10.5), (0, -8.4), (-4.2, -10.5)]
        me = bpy.data.meshes.new(p + "_doek")
        me.from_pydata([(x * s, 0, z * s) for x, z in vb], [], [list(range(5))])
        o = bpy.data.objects.new(p + "_doek", me); bpy.context.scene.collection.objects.link(o)
        o.location = (0, -0.1 * s, 0)
        md = o.modifiers.new("dik", "SOLIDIFY"); md.thickness = 0.5 * s
        bv = o.modifiers.new("rond", "BEVEL"); bv.width = 0.2 * s; bv.segments = 2
        _af(o, rood, ouder, p + "_doek", glad=False)
        # gouden embleem: een kroontje (spel over een slijm met een kroon)
        bol(ouder, p + "_embleem", (0, -0.6 * s, -5.0 * s), (1.6 * s, 0.4 * s, 1.6 * s), goud, 20)
        for dx in (-1.0, 0, 1.0):
            cil(ouder, p + "_kroonpunt", (dx * s, -0.6 * s, -3.3 * s), 0.35 * s, 1.1 * s, goud, r2=0.0, verts=8)
    elif naam == "bloemen":
        stengel = m("stengel", "3b8f3a", rough=0.9)
        for i, (dx, hoog, kl) in enumerate(((-3.8, 4.6, "ffd84a"), (-0.6, 6.0, "f08a9a"), (2.4, 4.0, "fff4e6"), (4.6, 5.2, "ffd84a"))):
            hm = m("blad" + kl, kl, rough=0.5, emis=0.15)
            cil(ouder, p + f"_stengel{i}", (dx * s, 0, hoog * s / 2), 0.3 * s, hoog * s, stengel, verts=6)
            for k in range(5):
                a = math.radians(90 + 72 * k)
                bol(ouder, p + f"_blad{i}", (dx * s + math.cos(a) * 0.8 * s, -0.4 * s, hoog * s + math.sin(a) * 0.8 * s),
                    (0.75 * s, 0.35 * s, 0.75 * s), hm, 10)
            bol(ouder, p + f"_hart{i}", (dx * s, -0.7 * s, hoog * s), (0.55 * s, 0.3 * s, 0.55 * s), m("hart", "e8a23a", rough=0.5), 8)
            bol(ouder, p + f"_blaadje{i}", (dx * s + 0.8 * s, 0, hoog * s * 0.4), (0.9 * s, 0.3 * s, 0.4 * s), stengel, 8)
    elif naam == "struik":
        groen = m("struik", "4fae45", rough=0.9)
        groen_d = m("struik_d", "3b8f3a", rough=0.9)
        bes = m("bes", "e0453a", rough=0.3, spec=0.6)
        for dx, dz, r, mt in ((-3.0, 2.2, 2.9, groen_d), (2.9, 2.2, 3.0, groen_d), (0, 3.0, 3.8, groen), (-1.6, 4.4, 2.4, groen), (1.8, 4.2, 2.3, groen)):
            bol(ouder, p + "_bol", (dx * s, 0, dz * s), (r * s, r * s * 0.8, r * s * 0.85), mt, 20)
        for dx, dz in ((-2.2, 3.4), (1.2, 5.6), (3.4, 2.8), (-0.4, 2.2)):
            bol(ouder, p + "_bes", (dx * s, -3.0 * s, dz * s), (0.7 * s,) * 3, bes, 10)
    elif naam == "steen":
        grijs = m("steen", "8e8698", rough=0.7, spec=0.25)
        grijs_l = m("steen_l", "aaa3b4", rough=0.65)
        o = bol(ouder, p + "_groot", (-0.8 * s, 0, 1.4 * s), (3.6 * s, 2.6 * s, 2.0 * s), grijs, 12)
        o.rotation_euler = (0, math.radians(-8), 0)
        bol(ouder, p + "_klein", (3.0 * s, -0.6 * s, 0.8 * s), (1.6 * s, 1.4 * s, 1.1 * s), grijs_l, 10)
    elif naam == "bordje":
        wit = m("verf", "f3e6cf", rough=0.6)
        blok(ouder, p + "_paal", (0, 0, 2.2 * s), (1.2 * s, 1.2 * s, 4.4 * s), hout_d, rond=0.3 * s)
        blok(ouder, p + "_plank", (0, -0.7 * s, 5.4 * s), (6.0 * s, 0.9 * s, 4.0 * s), hout, rond=0.4 * s)
        # pijl recht omlaag (hier gaat het hol in), geen tekst: leest in elke taal
        pv = [(-0.7, 7.0), (0.7, 7.0), (0.7, 5.6), (1.7, 5.6), (0, 3.9), (-1.7, 5.6), (-0.7, 5.6)]
        me = bpy.data.meshes.new(p + "_pijl")
        me.from_pydata([(x * s, 0, z * s) for x, z in pv], [], [list(range(7))])
        pp = bpy.data.objects.new(p + "_pijl", me); bpy.context.scene.collection.objects.link(pp)
        pp.location = (0, -1.2 * s, 0)
        md = pp.modifiers.new("dik", "SOLIDIFY"); md.thickness = 0.3 * s
        _af(pp, wit, ouder, p + "_pijl", glad=False)
    elif naam == "vliegenzwam":
        rood = m("rood", "d9483b", rough=0.45, spec=0.4)
        hoed_zwam(ouder, p + "_a", 0, 4.4 * s, 3.4 * s, rood, room)
    else:
        raise SystemExit("onbekende versiering: " + naam)
    ouder.location = (x, y, z)
    k = SCHAAL.get(naam, 1.0)  # op ware grootte nagekeken: ton en krat waren even hoog als een held
    ouder.scale = (k, k, k)
    return ouder


if __name__ == "__main__":
    from bpy_extras.object_utils import world_to_camera_view
    from mathutils import Vector
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    g.leeg()
    HOOGTE = 4.5
    BREED = HOOGTE * W / H
    CAM_MIDDEN, MAAIVELD, GANG_TOP = 2.025, 3.423, 1.559
    LINKS = -BREED / 2
    KOL = 16 * SPX
    plek = {}
    for i, n in enumerate(GANG):
        x = LINKS + (i + 0.5) * KOL * 1.3 + KOL * 0.3
        plek[n] = (x, GANG_TOP if n in HANGT else 0.0)
    for i, n in enumerate(MAAIVELD_NAMEN):
        plek[n] = (LINKS + (i + 0.5) * KOL * 1.3 + KOL * 0.3, MAAIVELD)
    ouders = {n: bouw(n, x, z) for n, (x, z) in plek.items()}
    cam = g.camera(hoogte_midden=CAM_MIDDEN, schaal=BREED)
    g.licht()
    # zelfde egale warme lamp als in hol.py (tegellicht), zodat de dingen zo licht zijn als in het hol
    sc = bpy.context.scene
    tl = bpy.data.lights.new("tegellicht", "AREA"); tl.shape = "RECTANGLE"; tl.size = BREED + 40; tl.size_y = 3.0
    tl.color = (1.0, 0.82, 0.86); tl.energy = 300 * (BREED + 40) / 10.0
    tlo = bpy.data.objects.new("tegellicht", tl); tlo.location = (0.0, -3.0, 4.6)
    tlo.rotation_euler = (math.radians(52), 0, 0); sc.collection.objects.link(tlo)
    sc.render.resolution_x, sc.render.resolution_y = W, H
    bpy.context.view_layer.update()
    vakken = {}
    for n, o in ouders.items():
        pts = []
        for k in [o] + list(o.children_recursive):
            if k.type == "MESH":
                dg = bpy.context.evaluated_depsgraph_get()
                e = k.evaluated_get(dg)
                pts += [e.matrix_world @ v.co for v in e.data.vertices]
        sp = [world_to_camera_view(sc, cam, p) for p in pts]
        xs = [p.x * 240 for p in sp]; ys = [(1 - p.y) * 40 for p in sp]
        a = world_to_camera_view(sc, cam, Vector((plek[n][0], 0.35, plek[n][1])))
        x0, y0 = math.floor(min(xs)) - 1, math.floor(min(ys)) - 1
        x1, y1 = math.ceil(max(xs)) + 1, math.ceil(max(ys)) + 1
        vakken[n] = {"vak": [x0, y0, x1 - x0, y1 - y0],
                     ("hang" if n in HANGT else "voet"): [round(a.x * 240 - x0, 1), round((1 - a.y) * 40 - y0, 1)]}
    with open(os.path.splitext(uit)[0] + "_vakken.json", "w") as f:
        json.dump(vakken, f, indent=1)
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
