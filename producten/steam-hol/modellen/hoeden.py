"""De 10 hoeden van Hats of the Fallen in 3D (Daan, 13 nov 2026, keuze A van Bram).

Elke held krijgt in het spel een willekeurige hoed (`hoed_nr` in held.gd) en precies die hoed belandt op
Gloops toren. Daarom rendert de pijplijn de helden zonder hoed (HOL_VERBERG ["hoed"], zie held.py) en
komt de hoed uit dit model. Volgorde en kleuren zoals held.gd en kunst/held_hoeden.png, zodat niets
van wat spelers al kennen verandert:
  0 helm (staal, rode pluim)     5 koksmuts (wit, bol)
  1 puntmuts (paars, gouden band, punt knakt; zelfde als de heks)
  2 kap (groen, met slip)        6 emmer (hout, twee banden, hengsel)
  3 pet (rood, klep opzij)       7 hoge hoed (antraciet, rode band)
  4 kroon (goud, drie punten)    8 pan (zwart, houten steel)
                                 9 veermuts (blauw, rode veer)

Als module:
    import hoeden
    hoeden.bouw(nr, plek=(x, y, z), schaal=1.0, kantel=0)
  plek   = midden van de onderrand van de hoed (zet die 1 spelpixel ín de kruin, anders zweeft hij)
  schaal = 1.0 past op een hoofd met straal ±0,4 (Gloop, en held.py op schaal 1)
  kantel = graden om de as naar de camera (scheef op de toren)
  Alle objecten heten hoed_<naam>_..., de ouder hoed_<naam>.

Los draaien (proefblad, alle 10 naast elkaar):
    <venv>/bin/python hoeden.py <uit.png> <breedte> <hoogte> <samples> [nr]
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g

NAMEN = ["helm", "puntmuts", "kap", "pet", "kroon", "koksmuts", "emmer", "hoge_hoed", "pan", "veermuts"]


def _zet(o, ouder, m, glad=True):
    if glad:
        bpy.ops.object.shade_smooth()
    if m is not None:
        o.data.materials.append(m)
    o.parent = ouder
    return o


def _bol(ouder, loc, schaal, m, segs=32, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = schaal
    return _zet(o, ouder, m)


def _kegel(ouder, loc, r1, r2, h, m, rot=(0, 0, 0), verts=48):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2, depth=h, location=loc, rotation=rot)
    return _zet(bpy.context.object, ouder, m)


def _ring(ouder, loc, r, dik, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=r, minor_radius=dik, location=loc, rotation=rot,
                                     major_segments=48, minor_segments=12)
    return _zet(bpy.context.object, ouder, m)


def _halve_bol(ouder, loc, schaal, m):
    """Koepel: bol met de onderste helft weggesneden (helm, pet, kap)."""
    o = _bol(ouder, loc, schaal, m, segs=48)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(loc[0], loc[1], loc[2] - 1.0))
    sn = bpy.context.object; sn.scale = (4, 4, 2); sn.hide_render = True; sn.hide_viewport = True
    sn.parent = ouder
    b = o.modifiers.new("snij", "BOOLEAN"); b.object = sn; b.operation = "DIFFERENCE"
    return o


def bouw(nr, plek=(0, 0, 0), schaal=1.0, kantel=0):
    nr = int(nr) % len(NAMEN)
    naam = NAMEN[nr]
    voor = set(bpy.data.objects)
    ouder = bpy.data.objects.new("hoed_" + naam, None)
    bpy.context.scene.collection.objects.link(ouder)
    R = math.radians

    if nr == 0:   # helm: zelfde koepel als Gloops helm, rode pluim (de ridder)
        staal = g.mat("staal", "staal", rough=0.32, spec=0.7, metaal=0.8)
        _halve_bol(ouder, (0, 0, 0), (0.42, 0.42, 0.46), staal)
        _kegel(ouder, (0, 0, 0.02), 0.45, 0.45, 0.07, staal)
        pl = g.mat("pluim", "rood", rough=0.7)
        for px, pz, ps in [(0.0, 0.5, 0.13), (0.09, 0.6, 0.12), (0.19, 0.65, 0.1), (0.29, 0.63, 0.08)]:
            _bol(ouder, (px, 0, pz), (ps, ps * 0.8, ps), pl, segs=16)
    elif nr == 1:   # puntmuts: de heksenhoed van gloop.py en held.py
        pa = g.mat("paars", "paars", rough=0.65)
        _kegel(ouder, (0, 0, 0.025), 0.56, 0.56, 0.05, pa)
        _kegel(ouder, (0, 0, 0.09), 0.34, 0.32, 0.09, g.mat("band", "goud", rough=0.3, metaal=0.6))
        _kegel(ouder, (-0.02, 0, 0.42), 0.33, 0.05, 0.68, pa)
        _kegel(ouder, (-0.13, 0, 0.82), 0.06, 0.0, 0.2, pa, rot=(0, R(-35), 0))
    elif nr == 2:   # kap: groene kap om het achterhoofd met een slip die opzij hangt
        gr = g.mat("kap", "4f9a3a", rough=0.8)
        _halve_bol(ouder, (0, 0.04, -0.06), (0.47, 0.47, 0.5), gr)
        _kegel(ouder, (0, 0.02, -0.03), 0.47, 0.47, 0.06, g.mat("kaprand", "3c7a2c", rough=0.8))
        # slip: dik begin bovenop, hangt los naar links omlaag (in 2D was de slip het herkenningsteken)
        _kegel(ouder, (-0.36, 0.08, 0.2), 0.17, 0.05, 0.42, gr, rot=(0, R(-125), 0), verts=24)
        _kegel(ouder, (-0.62, 0.08, 0.0), 0.06, 0.02, 0.24, gr, rot=(0, R(-165), 0), verts=16)
        _bol(ouder, (-0.65, 0.08, -0.13), (0.055, 0.055, 0.055), g.mat("kapknop", "goud", rough=0.3, metaal=0.6), segs=12)
    elif nr == 3:   # pet: rode koepel, klep schuin naar rechts voor (leest ook in silhouet)
        ro = g.mat("pet", "rood", rough=0.6)
        _halve_bol(ouder, (0, 0, 0), (0.42, 0.42, 0.3), ro)
        bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.3, depth=0.04, location=(0.3, -0.2, 0.03))
        k = bpy.context.object; k.scale = (1.0, 0.65, 1.0); k.rotation_euler = (0, R(-6), R(-35))
        _zet(k, ouder, g.mat("klep", "a8322d", rough=0.6))
        _bol(ouder, (0, 0, 0.3), (0.05, 0.05, 0.035), ro, segs=12)
    elif nr == 4:   # kroon: zelfde als op Gloops toren
        kr = g.mat("kroon", "goud", rough=0.16, spec=1.0, metaal=0.9, emis=0.1)
        _kegel(ouder, (0, 0, 0.12), 0.40, 0.42, 0.24, kr)
        for a_g in (215, 270, 325):
            a = R(a_g)
            px, py = 0.36 * math.cos(a), 0.36 * math.sin(a)
            hoog = 0.42 if a_g == 270 else 0.34
            _kegel(ouder, (px, py, 0.24 + hoog / 2), 0.15, 0.0, hoog, kr, verts=24)
            _bol(ouder, (px, py, 0.25 + hoog), (0.06, 0.06, 0.06), kr, segs=16)
        _bol(ouder, (0, -0.43, 0.12), (0.08, 0.04, 0.08), g.mat("robijn", "rood", rough=0.1, emis=0.3), segs=16)
    elif nr == 5:   # koksmuts: witte band en een bolle wolk erop
        wit = g.mat("koks", "f4f1ea", rough=0.85, spec=0.2)
        _kegel(ouder, (0, 0, 0.12), 0.38, 0.4, 0.24, wit)
        for x, y, z, s in [(0, 0, 0.42, 0.3), (-0.22, 0, 0.36, 0.22), (0.22, 0, 0.36, 0.22), (0, -0.18, 0.36, 0.2),
                           (0, 0.18, 0.38, 0.2)]:
            _bol(ouder, (x, y, z), (s, s, s * 0.85), wit, segs=24)
    elif nr == 6:   # emmer: omgekeerde houten emmer met twee banden en een hengsel
        hout = g.mat("emmer", "8a5a33", rough=0.75)
        band = g.mat("emmerband", "8d97a6", rough=0.35, metaal=0.7)
        _kegel(ouder, (0, 0, 0.25), 0.42, 0.33, 0.5, hout, verts=14)
        _kegel(ouder, (0, 0, 0.08), 0.425, 0.42, 0.06, band, verts=14)
        _kegel(ouder, (0, 0, 0.4), 0.37, 0.365, 0.06, band, verts=14)
        # hengsel weg: op het hoofd hing hij als een ring om het gezicht; een oortje links en rechts blijft
        for kant in (-1, 1):
            _bol(ouder, (0.4 * kant, 0, 0.2), (0.035, 0.05, 0.05), band, segs=12)
    elif nr == 7:   # hoge hoed: antraciet met rode band en brede rand
        zw = g.mat("hogehoed", "3a3440", rough=0.45, spec=0.5)
        _kegel(ouder, (0, 0, 0.025), 0.55, 0.55, 0.05, zw)
        _kegel(ouder, (0, 0, 0.36), 0.31, 0.33, 0.66, zw)
        _kegel(ouder, (0, 0, 0.13), 0.325, 0.325, 0.12, g.mat("hoedband", "rood", rough=0.5))
    elif nr == 8:   # pan: omgekeerde koekenpan, houten steel naar links
        pan = g.mat("pan", "2e2c33", rough=0.35, metaal=0.8)
        _kegel(ouder, (0, 0, 0.08), 0.46, 0.38, 0.16, pan)
        _kegel(ouder, (0, 0, 0.17), 0.38, 0.38, 0.02, pan)
        _kegel(ouder, (-0.62, 0, 0.12), 0.05, 0.04, 0.38, g.mat("steel", "7a4a2a", rough=0.6), rot=(0, R(-82), 0), verts=16)
        _kegel(ouder, (-0.42, 0, 0.1), 0.03, 0.03, 0.1, pan, rot=(0, R(-82), 0), verts=12)
    else:   # veermuts: blauwe baret met een rode veer
        bl = g.mat("veermuts", "4a7fd6", rough=0.7)
        _bol(ouder, (0.05, 0, 0.12), (0.47, 0.44, 0.17), bl, segs=40)
        _kegel(ouder, (0, 0, 0.04), 0.4, 0.4, 0.08, g.mat("mutsrand", "3a66b2", rough=0.7))
        veer = g.mat("veer", "rood", rough=0.7)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=(0.3, 0.05, 0.42))
        v = bpy.context.object; v.scale = (0.06, 0.025, 0.3); v.rotation_euler = (0, R(28), 0)
        _zet(v, ouder, veer)
        _bol(ouder, (0.2, -0.02, 0.2), (0.05, 0.05, 0.05), g.mat("veerknop", "goud", rough=0.3, metaal=0.6), segs=12)

    for o in bpy.data.objects:
        if o not in voor and o is not ouder and o.type not in ("CAMERA", "LIGHT"):
            o.name = "hoed_" + naam + "_" + o.name
    ouder.location = plek
    ouder.scale = (schaal, schaal, schaal)
    ouder.rotation_euler = (0, math.radians(kantel), 0)
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    g.leeg()
    if len(sys.argv) > 5:
        bouw(int(sys.argv[5]), (0, 0, 0.0))
        g.camera(hoogte_midden=0.35, schaal=1.6)
    else:
        for i in range(10):
            bouw(i, ((i - 4.5) * 1.3, 0, 0.0))
        g.camera(hoogte_midden=0.35, schaal=13.5)
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
    print("klaar", uit)
