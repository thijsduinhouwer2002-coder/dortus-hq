"""Helden in 3D, eerste stand-in (Daan, 13 nov 2026).

Twee helden die het hol binnenlopen en hun hoed verliezen aan Gloops toren. Zelfde hoeden als in
gloop.py (helm en heksenhoed), zodat je ziet waar de toren vandaan komt.
  ridder = blauwe tuniek, stalen helm met neusstuk, zwaard, rond schild
  heks   = oranje jurk, brede heksenhoed met gouden band, staf met een lichtje

Speelgoedstijl zoals Gloop (3d-stijl.md, regel 2): groot hoofd, twee grote ogen met glimstip,
korte beentjes. Op ware grootte (120 px = 4,5 eenheden) is een held ±1,9 eenheden hoog, ±50 px:
iets groter dan Gloop, want hij komt binnen als bedreiging en wordt toch opgegeten.

Als module (Mila, hol.py):
    import held
    held.bouw("ridder", "stap1", plek=(-6.0, 0.2, 0.0), draai=35)
  draai = graden om de hoogte-as; positief kijkt naar rechts (naar de schat).
  stand = rust, stap1, stap2 (twee stappen om te lopen), schrik (armen omhoog boven de put)
  schaal = 1.0 geeft ±1,8 eenheden (ridder met helm). De gangen van hol.py zijn 1,5 hoog:
           gebruik daar schaal 0.75 (±36 px op ware grootte), zodat de hoed niet in het plafond zit.
  gloed  = 0 (uit) of bijvoorbeeld 25: een zacht lampje voor het gezicht, voor in de donkere gang.

Los renderen:
    <venv>/bin/python held.py <uit.png> <soort> <stand> <breedte> <hoogte> <samples>
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g

HUID = "f2c2a0"
HUID_D = "d89a7a"


def _kind(o, ouder):
    o.parent = ouder
    return o


def _bol(ouder, loc, schaal, m, rot=(0, 0, 0), segs=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = schaal
    bpy.ops.object.shade_smooth(); o.data.materials.append(m)
    return _kind(o, ouder)


def _cil(ouder, loc, r, d, m, rot=(0, 0, 0), r2=None, verts=32):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(m)
    return _kind(o, ouder)


def _blok(ouder, loc, maat, m, rot=(0, 0, 0), rond=0.02):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = maat
    if rond:
        b = o.modifiers.new("rond", "BEVEL"); b.width = rond; b.segments = 3
    o.data.materials.append(m)
    return _kind(o, ouder)


def bouw(soort="ridder", stand="rust", plek=(0, 0, 0), draai=30, schaal=1.0, gloed=0):
    """Bouwt één held met de voeten op plek. Geeft het ouderobject terug."""
    sc = bpy.context.scene
    ouder = bpy.data.objects.new("held_" + soort, None)
    sc.collection.objects.link(ouder)

    huid = g.mat("huid", HUID, rough=0.45, sss=0.2)
    blos = g.mat("hblos", "blos", rough=0.7)
    wit = g.mat("hwit", "oogwit", rough=0.2, spec=0.5)
    pupil = g.mat("hpupil", "pupil", rough=0.35)
    glim = g.mat("hglim", "oogwit", emis=4.0)
    laars = g.mat("laars", "4a2e2a", rough=0.6)
    if soort == "ridder":
        kleed = g.mat("tuniek", "4a86f0", rough=0.5)
        kleed_d = g.mat("tuniek_d", "2a4a94", rough=0.6)
    else:
        # jurk warm oranje, niet paars: paars op het pruimen hol viel weg (frisse kijker ronde 1)
        kleed = g.mat("jurk", "e8873a", rough=0.6)
        kleed_d = g.mat("jurk_d", "a8552a", rough=0.6)

    # benen: stap1 linkervoet naar voren, stap2 rechts; schrik op de tenen
    stap = {"rust": 0.0, "stap1": 1.0, "stap2": -1.0, "schrik": 0.0}.get(stand, 0.0)
    for kant in (-1, 1):
        dx = 0.13 * kant
        voor = -0.14 * stap * kant         # -y is naar voren (het gezicht kijkt naar -y)
        til = 0.07 if (stap * kant < 0) else 0.0
        _cil(ouder, (dx, voor, 0.2 + til), 0.075, 0.3, kleed_d)
        _bol(ouder, (dx, voor - 0.04, 0.06 + til), (0.1, 0.12, 0.075), laars)

    # lijf: rond, iets peervormig
    if soort == "ridder":
        _bol(ouder, (0, 0, 0.55), (0.3, 0.26, 0.3), kleed)
        _cil(ouder, (0, 0, 0.42), 0.27, 0.07, g.mat("riem", "4a2e2a", rough=0.5))
        _blok(ouder, (0, -0.27, 0.42), (0.08, 0.02, 0.07), g.mat("gesp", "goud", rough=0.2, metaal=0.9), rond=0.01)
    else:
        _cil(ouder, (0, 0, 0.45), 0.36, 0.6, kleed, r2=0.2)
        _bol(ouder, (0, 0, 0.75), (0.21, 0.19, 0.12), kleed)
        _cil(ouder, (0, 0, 0.62), 0.26, 0.05, g.mat("koord", "goud", rough=0.3, metaal=0.6))

    # hoofd: groot (speelgoed), met twee grote ogen en een kleine o-mond
    HZ = 1.18
    _bol(ouder, (0, 0, HZ), (0.36, 0.33, 0.34), huid, segs=48)
    for kant in (-1, 1):
        ox = 0.13 * kant
        _bol(ouder, (ox, -0.29, HZ + 0.02), (0.1, 0.05, 0.12), wit)
        kijk = 0.025 if stand != "schrik" else 0.0
        _bol(ouder, (ox + kijk, -0.33, HZ + 0.0), (0.06, 0.03, 0.075), pupil)
        _bol(ouder, (ox + kijk + 0.025, -0.355, HZ + 0.04), (0.02, 0.01, 0.02), glim, segs=12)
        _bol(ouder, (0.22 * kant, -0.26, HZ - 0.1), (0.06, 0.02, 0.035), blos, segs=16)
    if stand == "schrik":
        _bol(ouder, (0, -0.32, HZ - 0.15), (0.05, 0.02, 0.06), g.mat("hmond", "mond", rough=0.6), segs=16)
    else:
        # vastberaden: kleine glimlach (halve ring) en twee wenkbrauwen die naar binnen zakken
        # (frisse kijker ronde 1: de o-mond las als "verbaasd of leeg")
        bpy.ops.mesh.primitive_torus_add(major_radius=0.065, minor_radius=0.017, location=(0.02, -0.325, HZ - 0.12),
                                         rotation=(math.radians(90), 0, 0))
        lach = bpy.context.object; lach.data.materials.append(g.mat("hmond", "mond", rough=0.6)); _kind(lach, ouder)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0.02, -0.325, HZ - 0.07)); sn2 = bpy.context.object
        sn2.scale = (0.3, 0.2, 0.1); sn2.hide_render = True; sn2.hide_viewport = True; _kind(sn2, ouder)
        bl = lach.modifiers.new("snij", "BOOLEAN"); bl.object = sn2; bl.operation = "DIFFERENCE"
        brauw = g.mat("brauw", "5a3a2a", rough=0.6)
        for kant in (-1, 1):
            _blok(ouder, (0.13 * kant, -0.31, HZ + 0.15), (0.1, 0.02, 0.025), brauw,
                  rot=(0, math.radians(18 * kant), 0), rond=0.01)
    _bol(ouder, (0, -0.34, HZ - 0.05), (0.04, 0.03, 0.035), g.mat("neus", HUID_D, rough=0.5), segs=16)

    # armen en handen
    arm_z = 0.7
    if stand == "schrik":
        hoek_l, hoek_r = 150, 150
    else:
        hoek_l, hoek_r = 20 + 15 * stap, 20 - 15 * stap
    handen = {}
    for kant, hoek in ((-1, hoek_l), (1, hoek_r)):
        a = math.radians(hoek)
        hx = kant * (0.3 + 0.18 * math.sin(a))
        hz = arm_z - 0.22 * math.cos(a)
        _cil(ouder, ((kant * 0.29 + hx) / 2, 0, (arm_z + hz) / 2), 0.055, 0.24, kleed,
             rot=(0, kant * a, 0))
        _bol(ouder, (hx, -0.02, hz), (0.07, 0.07, 0.07), huid, segs=16)
        handen[kant] = (hx, hz)

    # spullen
    hx, hz = handen[1]
    if soort == "ridder":
        staal = g.mat("hstaal", "staal", rough=0.25, spec=0.8, metaal=0.85)
        goud = g.mat("hgoud", "goud", rough=0.2, metaal=0.9, emis=0.1)
        # zwaard rechtop in de rechterhand, iets schuin naar voren
        _blok(ouder, (hx, -0.06, hz + 0.33), (0.05, 0.015, 0.5), staal, rot=(0, math.radians(-12), 0), rond=0.008)
        _blok(ouder, (hx - 0.01, -0.06, hz + 0.06), (0.2, 0.04, 0.04), goud, rond=0.01)
        _bol(ouder, (hx + 0.005, -0.06, hz - 0.05), (0.035, 0.035, 0.035), goud, segs=12)
        # rond schild aan de linkerarm, voor het lijf
        lx, lz = handen[-1]
        _cil(ouder, (-0.27, -0.2, 0.6), 0.19, 0.05, g.mat("schild", "rood", rough=0.5),
             rot=(math.radians(90), 0, math.radians(-20)))
        _cil(ouder, (-0.27, -0.235, 0.6), 0.07, 0.04, goud,
             rot=(math.radians(90), 0, math.radians(-20)))
        # helm: zelfde als Gloops helm (koepel, rand, punt, neusstuk)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=(0, 0, HZ + 0.1))
        helm = bpy.context.object; helm.scale = (0.37, 0.35, 0.33)
        bpy.ops.object.shade_smooth(); helm.data.materials.append(staal); _kind(helm, ouder)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, HZ - 0.12)); sn = bpy.context.object
        sn.scale = (2, 2, 0.44); sn.hide_render = True; sn.hide_viewport = True; _kind(sn, ouder)
        bm = helm.modifiers.new("snij", "BOOLEAN"); bm.object = sn; bm.operation = "DIFFERENCE"
        _cil(ouder, (0, 0, HZ + 0.11), 0.385, 0.05, staal)
        _cil(ouder, (0, 0, HZ + 0.48), 0.05, 0.13, staal, r2=0.0)
        _blok(ouder, (0, -0.39, HZ + 0.07), (0.05, 0.03, 0.15), staal, rond=0.01)
        top = HZ + 0.6
    else:
        hout = g.mat("hout", "7a4a2a", rough=0.6)
        _cil(ouder, (hx, -0.04, hz + 0.2), 0.03, 0.85, hout)
        _bol(ouder, (hx, -0.04, hz + 0.66), (0.08, 0.08, 0.08), g.mat("lichtje", "a8f0cf", emis=6.0), segs=16)
        l = bpy.data.lights.new("staflicht", "POINT"); l.color = (0.6, 1.0, 0.85); l.energy = 3
        l.shadow_soft_size = 0.1
        lo = bpy.data.objects.new("staflicht", l); lo.location = (hx, -0.2, hz + 0.66)
        sc.collection.objects.link(lo); _kind(lo, ouder)
        # haar: twee paarse vlechten onder de hoed
        haar = g.mat("haar", "c8423b", rough=0.7)
        for kant in (-1, 1):
            _bol(ouder, (0.3 * kant, 0.02, HZ - 0.1), (0.08, 0.08, 0.16), haar, segs=16)
        # heksenhoed: zelfde als op Gloops toren
        pa = g.mat("hpaars", "paars", rough=0.65)
        _cil(ouder, (0, 0, HZ + 0.24), 0.55, 0.04, pa)
        _cil(ouder, (0, 0, HZ + 0.3), 0.32, 0.08, g.mat("hband", "goud", rough=0.3, metaal=0.6), r2=0.3)
        _cil(ouder, (0, 0.0, HZ + 0.6), 0.31, 0.65, pa, r2=0.05)
        _cil(ouder, (-0.13, 0, HZ + 0.98), 0.055, 0.2, pa, r2=0.0, rot=(0, math.radians(-35), 0))
        top = HZ + 1.05

    ouder.location = plek
    ouder.scale = (schaal, schaal, schaal)
    ouder.rotation_euler = (0, 0, math.radians(-draai))
    # gebouwd met het gezicht naar -y (de camera); draai positief kijkt naar rechts
    ouder["top"] = top * schaal
    if gloed:
        # eigen zacht licht voor het gezicht, voor in een donkere gang (zoals Mila's gloopgloed)
        gl = bpy.data.lights.new("heldgloed", "POINT"); gl.color = (1.0, 0.85, 0.65); gl.energy = gloed
        gl.shadow_soft_size = 0.6
        go = bpy.data.objects.new("heldgloed", gl); sc.collection.objects.link(go)
        go.location = (plek[0] + 0.3, plek[1] - 1.0, plek[2] + 1.3 * schaal)
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    SOORT, STAND = sys.argv[2], sys.argv[3]
    W, H, SAMPLES = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    g.leeg()
    h = bouw(SOORT, STAND, (0, 0, 0), draai=30)
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
    bpy.context.object.is_shadow_catcher = True
    top = h["top"]
    g.camera(hoogte_midden=top / 2 - 0.1, schaal=max(2.4, top * 1.25))
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
    print("klaar", uit)
