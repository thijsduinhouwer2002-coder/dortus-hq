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
    hoeden.bouw(nr, plek=(x, y, z), schaal=1.0, kantel=0, draai=0, hap=False)
  plek   = midden van de onderrand van de hoed (zet die 1 spelpixel ín de kruin, anders zweeft hij)
  schaal = 1.0 past op een hoofd met straal ±0,4 (Gloop, en held.py op schaal 1)
  kantel = graden om de as naar de camera (scheef op de toren)
  draai  = graden om de staande as, net als `draai` in held.py (positief kijkt naar rechts). Geef de
           draai van de held mee, dan wijzen klep, steel, slip, pluim en veer mee met het gezicht.
  hap    = True: Gloop heeft een hap uit de hoed genomen (drie tandbogen bovenaan opzij, naar de camera;
           aan de kant waar klep, steel of slip het minst uitsteekt).
           Voor de stand hap van Gloop en voor de toren na een hap. Zonder hap is niets veranderd.
  Alle objecten heten hoed_<naam>_..., de ouder hoed_<naam>.

Los draaien (proefblad, alle 10 naast elkaar):
    <venv>/bin/python hoeden.py <uit.png> <breedte> <hoogte> <samples> [nr] [draai] [hap]
  bijvoorbeeld `... uit.png 1600 260 64 alle 30 hap`: alle 10, 30 graden gedraaid, met hap
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


def _hap(ouder, naam):
    """Daan 13 nov: drie bollen in een boog rechtsboven uit de hoed snijden, zodat er een tekenfilmhap
    met tandbogen in zit. Plaats volgt de maat van de hoed zelf, dus het werkt voor alle 10."""
    import mathutils
    delen = [o for o in ouder.children_recursive if o.type == "MESH" and not o.hide_render]
    # het lijf van de hoed = het deel met het grootste blok (niet de pluim, klep of steel)
    def blok(o):
        # echte hoekpunten in de wereld (een gedraaid blok steekt verder uit dan de ronde hoed)
        v = [o.matrix_world @ p.co for p in o.data.vertices]
        return (min(p.x for p in v), max(p.x for p in v), min(p.z for p in v), max(p.z for p in v),
                max(p.y for p in v) - min(p.y for p in v))
    lijf = max(delen, key=lambda o: (lambda b: (b[1] - b[0]) * (b[3] - b[2]) * b[4])(blok(o)))
    x0, x1, z0, z1, _ = blok(lijf)
    h = z1 - z0
    sch = ouder.scale[0]
    # kant: waar klep, steel of slip het minst uitsteekt (anders hapt Gloop de klep van de pet doormidden)
    alle = [blok(o) for o in delen]
    uit_r = max(b[1] for b in alle) - x1
    uit_l = x0 - min(b[0] for b in alle)
    kant = 1 if uit_r <= uit_l + 0.01 else -1
    pz = z0 + h * 0.64
    # rand = buitenste punt op de hoogte van de hap, over alle delen (koksmuts: de zijwolk, anders bleef
    # er een los stukje wolk zweven)
    op = [b for b in alle if b[2] <= pz <= b[3]] or [blok(lijf)]
    rand = max(b[1] for b in op) if kant == 1 else min(b[0] for b in op)
    # drie tanden op een boog rond een punt net buiten de rand: de binnenkant wordt geschulpt
    px = rand + kant * 0.16 * sch
    snij = []
    for i, a in enumerate((-50, 0, 50)):
        ah = math.radians(a)
        loc = (px - kant * 0.25 * sch * math.cos(ah), ouder.location[1], pz + 0.25 * sch * math.sin(ah))
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=1.0)
        b = bpy.context.object
        b.name = "hoed_" + naam + "_hapsnij%d" % i
        b.hide_render = True; b.hide_viewport = True
        b.parent = ouder
        b.matrix_parent_inverse.identity()
        # in de wereld: bol van 0,14 rond, 4x zo diep naar de camera, zodat hij dwars door de hoed snijdt
        r = 0.15 * sch
        b.matrix_world = (mathutils.Matrix.Translation(loc) @
                          mathutils.Matrix.Diagonal((r, 4 * r, r, 1.0)))
        snij.append(b)
    for o in delen:
        for b in snij:
            m = o.modifiers.new("hap", "BOOLEAN"); m.object = b; m.operation = "DIFFERENCE"
            m.solver = "EXACT"


def bouw(nr, plek=(0, 0, 0), schaal=1.0, kantel=0, draai=0, hap=False):
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
    elif nr == 3:   # pet: felrode koepel, klep naar voren en iets opzij, witte knoop (ronde 2: verdween in het haar)
        ro = g.mat("pet", "e8402e", rough=0.55)
        _halve_bol(ouder, (0, 0, 0), (0.43, 0.43, 0.34), ro)
        _kegel(ouder, (0, 0, 0.03), 0.435, 0.435, 0.05, g.mat("petband", "f4f1ea", rough=0.7))
        bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.32, depth=0.045, location=(0.36, -0.26, 0.05))
        k = bpy.context.object; k.scale = (1.0, 0.62, 1.0); k.rotation_euler = (R(-8), R(-8), R(-38))
        _zet(k, ouder, g.mat("klep", "b8281c", rough=0.55))
        _bol(ouder, (0, 0, 0.34), (0.06, 0.06, 0.04), g.mat("petknoop", "f4f1ea", rough=0.7), segs=12)
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
        # ronde 2: hoger, lichter hout met zichtbare duigen, donkere banden (las als oranje pan)
        hout = g.mat("emmer", "b07a45", rough=0.75)
        band = g.mat("emmerband", "4a4652", rough=0.35, metaal=0.7)
        _kegel(ouder, (0, 0, 0.32), 0.42, 0.3, 0.64, hout, verts=10)
        bpy.ops.object.shade_flat()
        _kegel(ouder, (0, 0, 0.1), 0.43, 0.415, 0.07, band, verts=10)
        _kegel(ouder, (0, 0, 0.5), 0.345, 0.335, 0.07, band, verts=10)
        _kegel(ouder, (0, 0, 0.645), 0.29, 0.29, 0.015, g.mat("bodem", "8a5a33", rough=0.8), verts=10)
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
        # ronde 2: steel schuin omhoog (vlak las hij als bolhoed met een stokje)
        _kegel(ouder, (-0.6, 0, 0.32), 0.055, 0.045, 0.42, g.mat("steel", "9a5a2a", rough=0.6), rot=(0, R(-50), 0), verts=16)
        _kegel(ouder, (-0.42, 0, 0.17), 0.03, 0.03, 0.12, pan, rot=(0, R(-50), 0), verts=12)
        _bol(ouder, (0, -0.0, 0.19), (0.32, 0.32, 0.02), g.mat("panglans", "6a6670", rough=0.2, metaal=0.9), segs=32)
    else:   # veermuts: blauwe baret met een rode veer
        bl = g.mat("veermuts", "4a7fd6", rough=0.7)
        _bol(ouder, (0.05, 0, 0.12), (0.47, 0.44, 0.17), bl, segs=40)
        _kegel(ouder, (0, 0, 0.04), 0.4, 0.4, 0.08, g.mat("mutsrand", "3a66b2", rough=0.7))
        veer = g.mat("veer", "rood", rough=0.7)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=(0.3, 0.05, 0.42))
        v = bpy.context.object; v.scale = (0.06, 0.025, 0.3); v.rotation_euler = (0, R(28), 0)
        _zet(v, ouder, veer)
        _bol(ouder, (0.2, -0.02, 0.2), (0.05, 0.05, 0.05), g.mat("veerknop", "goud", rough=0.3, metaal=0.6), segs=12)

    # list(): hernoemen tijdens het doorlopen liet Blender hetzelfde object vaker langskomen (namen tot 63 tekens)
    for o in list(bpy.data.objects):
        if o not in voor and o is not ouder and o.type not in ("CAMERA", "LIGHT"):
            o.name = "hoed_" + naam + "_" + o.name
    ouder.location = plek
    ouder.scale = (schaal, schaal, schaal)
    # XYZ: eerst kantelen (toren), dan draaien om de staande as (held.py: positief kijkt naar rechts)
    ouder.rotation_euler = (0, math.radians(kantel), math.radians(-draai))
    if hap:
        # na het plaatsen, zodat de hap altijd recht naar de camera wijst, ook als de hoed gedraaid is
        bpy.context.view_layer.update()
        _hap(ouder, naam)
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    g.leeg()
    nr = sys.argv[5] if len(sys.argv) > 5 else "alle"
    dr = float(sys.argv[6]) if len(sys.argv) > 6 else 0
    hp = len(sys.argv) > 7 and sys.argv[7] == "hap"
    if nr != "alle":
        bouw(int(nr), (0, 0, 0.0), draai=dr, hap=hp)
        g.camera(hoogte_midden=0.35, schaal=1.6)
    else:
        for i in range(10):
            bouw(i, ((i - 4.5) * 1.3, 0, 0.0), draai=dr, hap=hp)
        g.camera(hoogte_midden=0.35, schaal=13.5)
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
    print("klaar", uit)
