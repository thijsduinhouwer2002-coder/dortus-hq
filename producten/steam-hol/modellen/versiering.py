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
HANGT = ("spinrag", "stut", "vaandel", "wortels_a", "wortels_b", "wand_wortels")
GANG = ("paddenstoel", "lichtzwam", "ton", "krat", "schedel", "kristal", "spinrag", "stut", "vaandel")
MAAIVELD_NAMEN = ("bloemen", "struik", "steen", "bordje", "vliegenzwam")
# Mila 26 nov (issue 96, Gemini "too basic"): dingen in de aardwand die het verhaal vertellen. Staand (voet onderaan):
# bot, helm en zwaard van gevallen helden half in de aarde, een grote koele steen voor de diepe rij, twee kiezelgroepjes.
# Hangend (hangpunt bovenaan): wortels onder het gras. Het spel kiest per kolom welk ding, zodat de aarde niet elke 16
# spelpixels hetzelfde is.
WAND_STAAND = ("bot", "helm", "zwaard", "steen_diep", "kiezels_a", "kiezels_b")
WAND_HANG = ("wortels_a", "wortels_b")
# Mila 26 nov (issue 146, Iris "weg na het graven"): voor de achterwand van een gegraven gang of kamer. Stenen die half
# in de wand zitten (plat, met een donkere kom eromheen, koel grijs) en korte wortels die uit het plafond hangen; laag
# genoeg (±6 spelpixels) dat ze boven de hoofden van de helden blijven.
ACHTERWAND = ("wand_steen", "wand_wortels")
GANG_HOOG = 16 * SPX * 0.966 / 0.966  # 16 spelpixels gang (vloer z 0 tot plafond)

_M = {}
SCHAAL = {"bot": 1.4, "helm": 1.5, "zwaard": 1.2, "steen_diep": 1.1,  # Daan #133: helm groter dan het bot (M2), bot groter (K2)
           "ton": 0.78, "krat": 0.82, "kristal": 0.75, "schedel": 0.85}  # kristal en schedel: frisse kijker 14 nov, te groot en te fel


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


def kluit(ouder, naam, loc, maat):
    """Kluit aarde voor een ding dat half in de wand zit: donkerder dan de wand, zodat het ding erin zakt."""
    k = bol(ouder, naam, loc, maat, m("kluit", "5e3328", rough=0.95), 14)
    return k


def brok(ouder, naam, loc, b, h, d, mat, zaad=0, scheef=0.0):
    """Hoekige steen met een platte onderkant (Daan #133 M1: de ronde paarse stenen lazen als naaktslakken).
    Onder een onregelmatige zeshoek, boven een kleinere vijfhoek die iets opzij staat; daarover het omhulsel, vlak
    gearceerd, zodat je op 120 px twee of drie vlakken ziet en geen glanzende bult."""
    import bmesh
    rnd = [((zaad * 7919 + i * 104729) % 1000) / 1000.0 for i in range(24)]
    pts = []
    for i in range(6):
        a = math.tau * (i + 0.35 * rnd[i]) / 6
        pts.append((math.cos(a) * b * (0.8 + 0.25 * rnd[i + 6]), math.sin(a) * d * (0.8 + 0.25 * rnd[i + 12]), 0.0))
    for i in range(5):
        a = math.tau * (i + 0.5 * rnd[i + 18]) / 5 + 0.4
        pts.append((math.cos(a) * b * 0.55 + scheef * b, math.sin(a) * d * 0.55, h * (0.85 + 0.15 * rnd[i + 1])))
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    for q in pts:
        bm.verts.new(q)
    bmesh.ops.convex_hull(bm, input=bm.verts)
    bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(naam, me); bpy.context.scene.collection.objects.link(o)
    o.location = loc
    return _af(o, mat, ouder, naam, glad=False)


def wortel(ouder, naam, x, z, lengte, dik, buig, mat, tip):
    """Wortel die van boven schuin naar beneden hangt: dik bij de aarde, spits aan de punt (de punt donkerder).
    Let op: bij een kegel is radius1 de onderkant (-z), dus de dunne punt."""
    bx, bz = x + math.sin(buig) * lengte * 0.75, z - math.cos(buig) * lengte * 0.75
    cil(ouder, naam + "_lijf", ((x + bx) / 2, 0, (z + bz) / 2), dik * 0.35, lengte * 0.78, mat, rot=(0, -buig, 0),
        verts=12, r2=dik)
    b2 = buig * 1.8
    ex, ez = bx + math.sin(b2) * lengte * 0.25, bz - math.cos(b2) * lengte * 0.25
    cil(ouder, naam + "_tip", ((bx + ex) / 2, 0, (bz + ez) / 2), dik * 0.08, lengte * 0.28, tip, rot=(0, -b2, 0),
        verts=10, r2=dik * 0.38)
    # zijworteltje halverwege
    hx, hz = x + math.sin(buig) * lengte * 0.35, z - math.cos(buig) * lengte * 0.35
    zb = buig - 0.9 if buig >= 0 else buig + 0.9
    l2 = lengte * 0.3
    cil(ouder, naam + "_zij", (hx + math.sin(zb) * l2 / 2, 0, hz - math.cos(zb) * l2 / 2), dik * 0.08, l2, mat,
        rot=(0, -zb, 0), verts=8, r2=dik * 0.35)


def kronkel(ouder, naam, x, z, lengte, dik, buig, mat, zaad=0):
    """Dunne wortel die kronkelend naar beneden hangt (Daan #153 M1): een ketting van korte stukjes die om en om
    een andere kant op buigen, bijna even dik tot de punt, een ronde punt en een zijtak op ongeveer een derde."""
    n = 6
    stuk = lengte / n
    px, pz, hoek = x, z, buig * 0.4
    zij = None
    for i in range(n):
        hoek += (0.55 if (i + zaad) % 2 == 0 else -0.55) + buig * 0.12
        nx, nz = px + math.sin(hoek) * stuk, pz - math.cos(hoek) * stuk
        r = dik * (1.0 - 0.35 * i / n)
        cil(ouder, naam + f"_{i}", ((px + nx) / 2, 0, (pz + nz) / 2), r * 0.9, stuk * 1.12, mat, rot=(0, -hoek, 0),
            verts=10, r2=r)
        bol(ouder, naam + f"_k{i}", (nx, 0, nz), (r * 0.9, r * 0.9, r * 0.9), mat, 10)
        if i == 2:
            zij = (nx, nz, hoek, r)
        px, pz = nx, nz
    zx, zz, zh, zr = zij
    zh2 = zh + (0.9 if buig < 0 else -0.9)
    for j in range(3):
        zh2 += -0.5 if j % 2 == 0 else 0.5
        ex, ez = zx + math.sin(zh2) * stuk * 0.7, zz - math.cos(zh2) * stuk * 0.7
        cil(ouder, naam + f"_z{j}", ((zx + ex) / 2, 0, (zz + ez) / 2), zr * 0.5, stuk * 0.78, mat, rot=(0, -zh2, 0),
            verts=8, r2=zr * 0.6)
        zx, zz = ex, ez


def wand(ouder, p, naam, s):
    bot = m("bot", "c8b8a2", rough=0.7)
    if naam == "bot":
        # dijbeen schuin in de aarde, het rechtereind in een kluit
        a = math.radians(-26)   # Daan #133 K2: schuiner, leest meer als bot dan als streepje
        cil(ouder, p + "_schacht", (0, 0, 1.6 * s), 0.62 * s, 6.4 * s, bot, rot=(0, math.radians(90) + a, 0), verts=14)
        for zx in (-1, 1):
            for dz in (-0.55, 0.55):
                bol(ouder, p + "_knobbel", (zx * 3.2 * s * math.cos(a), -0.05 * s, 1.6 * s - zx * 3.2 * s * math.sin(a) + dz * s),
                    (0.95 * s, 0.75 * s, 0.85 * s), bot, 14)
        kluit(ouder, p + "_kluit", (3.6 * s, -0.5 * s, 0.9 * s), (2.0 * s, 0.9 * s, 1.3 * s))
    elif naam == "helm":
        ijzer = m("helm", "8f98ae", rough=0.32, metaal=0.65, spec=0.6)
        ijzer_d = m("helm_d", "5d6478", rough=0.4, metaal=0.6)
        gat = m("gat", "2a1832", rough=0.9)
        bol(ouder, p + "_kap", (0, 0, 2.9 * s), (3.1 * s, 2.2 * s, 2.9 * s), ijzer, 24)
        blok(ouder, p + "_kam", (0, -0.2 * s, 5.0 * s), (0.7 * s, 2.6 * s, 2.2 * s), ijzer_d, rond=0.25 * s, rot=(0, 0, 0))
        blok(ouder, p + "_spleet", (0, -2.05 * s, 3.0 * s), (4.2 * s, 0.4 * s, 0.55 * s), gat, rond=0.15 * s)
        blok(ouder, p + "_neus", (0, -2.15 * s, 2.3 * s), (0.6 * s, 0.4 * s, 1.6 * s), ijzer_d, rond=0.15 * s)
        # Daan #133 M2: de pluim is wat de helm op 120 px herkenbaar maakt; groter, waaiert naar achter
        pl = m("pluim", "d8402f", rough=0.8)
        for i, (dx, dz, r) in enumerate(((0.6, 6.0, 1.15), (1.9, 6.5, 1.05), (3.0, 6.1, 0.9))):
            bol(ouder, p + f"_pluim{i}", (dx * s, 0.4 * s, dz * s), (r * s, 0.8 * s, r * 0.95 * s), pl, 12)
        # onderkant in de aarde: een brede lage kluit voor de kap
        kluit(ouder, p + "_kluit", (0.2 * s, -1.4 * s, 0.9 * s), (4.4 * s, 1.4 * s, 1.3 * s))
    elif naam == "zwaard":
        staal = m("staal", "c3cad6", rough=0.22, metaal=0.8, spec=0.8)
        goud = m("goud", "e8b73a", rough=0.3, metaal=0.8, spec=0.7)
        greep = m("greep", "5a2e1c", rough=0.8)
        a = math.radians(24)
        def op(d):   # punt op afstand d langs het zwaard vanaf de punt in de kluit
            return (math.sin(a) * d, math.cos(a) * d)
        x, z = op(3.4 * s); blok(ouder, p + "_kling", (x, 0, z + 0.4 * s), (0.9 * s, 0.3 * s, 5.6 * s), staal, rond=0.12 * s, rot=(0, a, 0))
        x, z = op(6.4 * s); blok(ouder, p + "_stang", (x, -0.1 * s, z + 0.4 * s), (3.8 * s, 0.6 * s, 0.75 * s), goud, rond=0.2 * s, rot=(0, a, 0))
        x, z = op(7.7 * s); cil(ouder, p + "_greep", (x, -0.1 * s, z + 0.4 * s), 0.38 * s, 2.2 * s, greep, rot=(0, a, 0), verts=10)
        x, z = op(9.0 * s); bol(ouder, p + "_knop", (x, -0.1 * s, z + 0.4 * s), (0.65 * s,) * 3, goud, 12)
        kluit(ouder, p + "_kluit", (0.3 * s, -0.6 * s, 0.8 * s), (2.4 * s, 1.0 * s, 1.1 * s))
    elif naam == "steen_diep":
        # Daan #133 M1: twee ongelijke hoekige grijze stenen met een platte onderkant, niet paars, geen glans
        k = m("steen_k", "4a4b52", rough=0.85, spec=0.15)
        kl = m("steen_kl", "686a72", rough=0.8, spec=0.15)
        brok(ouder, p + "_groot", (-0.9 * s, 0, 0), 3.0 * s, 4.4 * s, 1.6 * s, kl, zaad=3, scheef=-0.15)
        brok(ouder, p + "_klein", (2.6 * s, -0.3 * s, 0), 1.9 * s, 2.5 * s, 1.2 * s, k, zaad=11, scheef=0.2)
    elif naam in ("kiezels_a", "kiezels_b"):
        # Daan #133 K1: grijzer en hoekig, zodat ze niet als kruimels of maden lezen
        warm = m("kiezel_w", "7c7068", rough=0.8, spec=0.15)
        koel = m("kiezel_k", "585a61", rough=0.8, spec=0.15)
        rij = ([(-2.6, 1.2, warm), (-0.4, 0.9, koel), (1.8, 1.5, warm)]
               if naam == "kiezels_a" else
               [(-2.0, 1.4, koel), (0.6, 1.0, warm)])
        for i, (dx, r, mt) in enumerate(rij):
            brok(ouder, p + f"_k{i}", (dx * s, -0.3 * s, 0), r * 1.1 * s, r * 1.2 * s, r * 0.8 * s, mt, zaad=i + 5 * len(rij))
        if naam == "kiezels_b":
            cil(ouder, p + "_botje", (2.6 * s, -0.4 * s, 0.5 * s), 0.4 * s, 2.4 * s, bot, rot=(0, math.radians(70), 0), verts=10)
    elif naam == "wand_steen":
        # Daan #153 M2: stenen die echt half in de achterwand zitten. Twee hoekige stenen, een grote en een kleine, met de
        # platte kant naar voren en weinig diepte, in een donkere kom aarde die er rondom net onder uitkomt (een lichte aardrand eronder las als een plankje); donker
        # koel grijs zodat ze bij de koele gang horen en niet als los puin lezen. Het spel kiest maat, hoogte en spiegelen.
        k = m("wsteen_k", "6e6863", rough=0.9, spec=0.1)
        kl = m("wsteen_kl", "817a73", rough=0.9, spec=0.1)
        kom = m("wsteen_kom", "5a3027", rough=0.95)
        bol(ouder, p + "_kom", (0.5 * s, 0.25 * s, 1.35 * s), (3.4 * s, 0.4 * s, 1.35 * s), kom, 16)
        for i, (dx, dz, b, h, mt, z, rx) in enumerate([(-0.9, 1.5, 2.6, 1.0, kl, 41, 84), (2.2, 1.1, 1.5, 0.8, k, 43, 78)]):
            o = brok(ouder, p + f"_s{i}", (dx * s, 0.05 * s, dz * s), b * s, h * s, b * 0.7 * s, mt, zaad=z,
                     scheef=0.12 * (1 - 2 * i))
            o.rotation_euler = (math.radians(rx), math.radians(12 - 26 * i), 0)
    elif naam == "wand_wortels":
        # Daan #153 M1: geen spitse driehoeken meer (die lazen als de stekels van de put). Dunne, kronkelige wortels
        # in licht beige, overal bijna even dik met een ronde punt, en elk met een zijtak; ze komen uit een kleine
        # donkere kluit in het plafond.
        wm = m("wwortel", "c9ab86", rough=0.8)
        wd = m("wwortel_d", "a88a68", rough=0.85)
        kluit(ouder, p + "_kluit", (0.2 * s, 0.2 * s, -0.05 * s), (3.2 * s, 0.6 * s, 0.45 * s))
        for i, (dx, l, d, b, mt) in enumerate([(-1.8, 5.2, 0.36, 0.35, wm), (0.4, 6.4, 0.40, -0.25, wm),
                                               (2.3, 3.6, 0.32, 0.5, wd)]):
            kronkel(ouder, p + f"_w{i}", dx * s, -0.2 * s, l * s, d * s, b, mt, zaad=i * 3 + 1)
    elif naam in ("wortels_a", "wortels_b"):
        wm = m("wortel", "9a7352", rough=0.85)
        tip = m("wortel_tip", "5e4434", rough=0.9)
        rij = ([(-2.4, 7.5, 0.6, 0.22), (0.2, 9.5, 0.72, -0.14), (2.6, 5.0, 0.5, 0.3)]
               if naam == "wortels_a" else
               [(-1.6, 6.0, 0.55, -0.25), (1.4, 8.5, 0.7, 0.18)])
        for i, (dx, l, d, b) in enumerate(rij):
            wortel(ouder, p + f"_w{i}", dx * s, 0, l * s, d * s, b, wm, tip)
        # donkere vochtige plek waar ze uit de aarde komen
        kluit(ouder, p + "_kluit", (0, 0.2 * s, 0.1 * s), (4.0 * s, 0.8 * s, 1.0 * s))


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
        bot = m("bot", "c8b8a2", rough=0.7)  # frisse kijker 14 nov: was te wit en te fel
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
        groen = m("kristal", "4f8fd0", rough=0.15, spec=0.7, emis=0.08)  # ijsblauw, niet Gloops muntgroen
        licht = m("kristal_l", "86b8e6", rough=0.12, spec=0.7, emis=0.1)
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
        l = bpy.data.lights.new(p + "_licht", "POINT"); l.color = (0.6, 0.78, 1.0); l.energy = 1.2; l.shadow_soft_size = 0.2
        lo = bpy.data.objects.new(p + "_licht", l); lo.location = (0, -0.35, 5 * s); lo.parent = ouder
        bpy.context.scene.collection.objects.link(lo)
    elif naam == "spinrag":
        web = m("web", "9a95a3", rough=0.7)  # grijzer en dikker: was op ware grootte een wit krasje; 14 nov nog een tikje grijzer (Daan kan 1)
        zw = m("spin", "3a2a4c", rough=0.3, spec=0.8)  # Bram 15 nov (kan Daan 10:40): iets lichter met glans op de rug, was 2a1832 mat
        oog = m("spinoog", "ff6a5a", rough=0.3, emis=1.0)
        # Bram 15 nov: het oude hoekweb (waaier uit de linkerbovenhoek, rechte draad omlaag links en de spin aan een rechte
        # draad rechts) hing midden in de gang zonder muur erachter en las op 96 als een ingelijst vierkant. Nu een web dat
        # aan het plafond hangt: een rond web dat door het plafond wordt afgesneden, naaf onder het plafond, drie spaken
        # omhoog, vijf omlaag, doorhangende ringen, en een kleine spin rechtsonder op het web. Geen rechte rand meer.
        def draad(a, b, r):
            dx, dz = b[0] - a[0], b[1] - a[1]
            cil(ouder, p + "_draad", ((a[0] + b[0]) / 2, -0.1, (a[1] + b[1]) / 2), r * s, math.hypot(dx, dz) * 1.04,
                web, rot=(0, math.atan2(dx, dz), 0), verts=6)
        # Ronde 2 (frisse kijker op het ronde web: 5 tegen 8 voor het oude, "zweeft als los stempel, spin valt erin weg"):
        # een halve waaier die vanaf het plafond omlaag hangt (naaf op het plafond, geen rechte paal), en de spin weer los
        # aan een eigen draad ernaast, met een eigen silhouet; de draad lichter en dikker.
        R = 5.6
        spaken = [196, 228, 260, 292, 324, 352]

        def punt(a, r):
            return (-1.2 * s + math.cos(math.radians(a)) * r * s, math.sin(math.radians(a)) * r * s * 1.35)  # dieper: de camera kijkt schuin
        draad(punt(180, 0.6), punt(0, 4.6), 0.3)  # plafondlijn waar het web aan vast zit
        for a in spaken:
            draad(punt(a, 0), punt(a, R), 0.26)
        for rr in (2.0, 3.8, R):
            for a1, a2 in zip(spaken, spaken[1:]):
                q1, q2 = punt(a1, rr), punt(a2, rr)
                qm = punt((a1 + a2) / 2, rr * 0.86)
                draad(q1, qm, 0.21)
                draad(qm, q2, 0.21)
        draad_l = m("draad_l", "ddd8e6", rough=0.6)  # lichter dan het web, zodat de spin zichtbaar ergens aan hangt
        sx0, sz0 = 5.0 * s, -7.4 * s  # iets los van de rand van het web (frisse kijker: draad las als paal)
        cil(ouder, p + "_hangdraad", (sx0, -0.1, sz0 / 2), 0.22 * s, -sz0, draad_l, verts=6)
        bol(ouder, p + "_lijf", (sx0, -0.12, sz0 - 0.4 * s), (1.5 * s, 1.2 * s, 1.5 * s), zw, 16)
        for sx in (-1, 1):
            bol(ouder, p + "_oog", (sx0 + sx * 0.55 * s, -0.12 - 1.15 * s, sz0 - 0.4 * s), (0.35 * s,) * 3, oog, 8)
            for j in range(3):
                a = math.radians(-30 + j * 30)
                cil(ouder, p + "_poot", (sx0 + sx * 1.9 * s, -0.12, sz0 - 0.4 * s + math.sin(a) * 1.2 * s),
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
    elif naam in WAND_STAAND or naam in WAND_HANG or naam in ACHTERWAND:
        wand(ouder, p, naam, s)
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
    # Bram 14 nov: 1,6 kolom (25,6 spelpixels) tussen de middens in plaats van 1,3, en een marge van 2 spelpixels om
    # elk vak. Met 1,3 en marge 1 lag er een randje van het stuk zelf (de vervaging bij het verkleinen) in de buitenste
    # kolom van het vak, en de pijplijn trekt die kolom door in de rand van het blad: Daans oranje streepje naast de stut
    # en het stipje naast de vliegenzwam. Alleen de plek in de proefrender verandert, niet het stuk.
    STAP = KOL * 1.6
    plek = {}
    for i, n in enumerate(GANG):
        x = LINKS + (i + 0.5) * STAP + KOL * 0.2
        plek[n] = (x, GANG_TOP if n in HANGT else 0.0)
    for i, n in enumerate(MAAIVELD_NAMEN):
        plek[n] = (LINKS + (i + 0.5) * STAP + KOL * 0.2, MAAIVELD)
    for i, n in enumerate(WAND_STAAND):
        plek[n] = (LINKS + (i + 0.5) * STAP + KOL * 0.2, 1.75)
    for i, n in enumerate(WAND_HANG):
        plek[n] = (LINKS + (i + 6.5) * STAP + KOL * 0.2, MAAIVELD - 0.12)
    # achterwand (issue 146): op de vrije plekken rechts; de steen in de wandrij iets hoger, want onder vak 8 hangt het vaandel
    plek["wand_steen"] = (LINKS + 8.5 * STAP + KOL * 0.2, 2.1)
    plek["wand_wortels"] = (LINKS + 8.5 * STAP + KOL * 0.2, MAAIVELD + 0.55)
    WAND = WAND_STAAND + WAND_HANG + ACHTERWAND
    ouders = {n: bouw(n, x, z, y=0.0 if n in WAND else 0.35) for n, (x, z) in plek.items()}
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
        a = world_to_camera_view(sc, cam, Vector((plek[n][0], 0.0 if n in WAND else 0.35, plek[n][1])))
        x0, y0 = math.floor(min(xs)) - 2, math.floor(min(ys)) - 2
        x1, y1 = math.ceil(max(xs)) + 2, math.ceil(max(ys)) + 2
        vakken[n] = {"vak": [x0, y0, x1 - x0, y1 - y0],
                     ("hang" if n in HANGT else "voet"): [round(a.x * 240 - x0, 1), round((1 - a.y) * 40 - y0, 1)]}
    with open(os.path.splitext(uit)[0] + "_vakken.json", "w") as f:
        json.dump(vakken, f, indent=1)
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
