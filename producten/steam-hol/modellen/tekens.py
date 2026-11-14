"""Tekens boven het hoofd van een held in 3D (Daan, 14 nov 2026). Vervangt kunst/tekens.png (8 x 8 pixels).

Volgorde zoals tekens.png: 0 boos, 1 uitroep, 2 zweet, 3 zzz, 4 ster.
Elk teken is een rond, room-kleurig wolkje met een staartje naar beneden (naar het hoofd) en het
symbool er dik op, zodat het op ±8 spelpixels leest tegen de paarse aarde. Zelfde licht en camera als
alle modellen (gedeeld.py), mat zoals de kist, geen lijnen.

Als module:
    import tekens
    tekens.bouw(nr, plek=(x, y, z), schaal=1.0)   # plek = punt van het staartje
Los (proefblad, alle 5 naast elkaar, of één):
    <venv>/bin/python tekens.py <uit.png> <breedte> <hoogte> <samples> [nr|alle]
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g

NAMEN = ["boos", "uitroep", "zweet", "zzz", "ster"]


def _obj(o, naam, m, ouder):
    o.name = naam
    o.data.materials.append(m)
    o.parent = ouder
    return o


def _tekst(txt, loc, grootte, m, naam, ouder, dik=0.06):
    bpy.ops.object.text_add(location=loc, rotation=(math.radians(90), 0, 0))
    o = bpy.context.object
    o.data.body = txt
    o.data.size = grootte
    o.data.extrude = dik
    o.data.bevel_depth = 0.012
    o.data.align_x = "CENTER"
    o.data.align_y = "CENTER"
    return _obj(o, naam, m, ouder)


def bouw(nr, plek=(0, 0, 0), schaal=1.0):
    naam = NAMEN[nr]
    x, y, z = plek
    ouder = bpy.data.objects.new(f"teken_{naam}", None)
    bpy.context.scene.collection.objects.link(ouder)
    room = g.mat(f"teken_room_{naam}", "fbf3df", rough=0.55, spec=0.3)
    # wolkje: platte bol met staartje, net iets naar de camera
    bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, location=(0, 0.02, 0.62))
    w = _obj(bpy.context.object, f"teken_{naam}_wolk", room, ouder)
    w.scale = (0.42, 0.16, 0.38); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.12, radius2=0.0, depth=0.26,
                                    location=(0.0, 0.02, 0.2), rotation=(math.radians(180), 0, 0))
    t = _obj(bpy.context.object, f"teken_{naam}_staart", room, ouder)
    t.scale = (1, 0.6, 1); bpy.ops.object.shade_smooth()
    voor = -0.16  # symbool op de voorkant van het wolkje
    if naam == "boos":
        rood = g.mat("teken_rood", "d8423b", rough=0.4)
        # vier bogen, elk in een eigen hoek en bol naar het midden (de bekende boze ader)
        import bmesh
        for i, (sx, sz) in enumerate(((1, 1), (-1, 1), (-1, -1), (1, -1))):
            cx, cz = 0.21 * sx, 0.21 * sz
            bpy.ops.mesh.primitive_torus_add(major_radius=0.14, minor_radius=0.04, major_segments=48,
                                             minor_segments=12, location=(cx, voor, 0.62 + cz),
                                             rotation=(math.radians(90), 0, 0))
            o = _obj(bpy.context.object, f"teken_boos_{i}", rood, ouder)
            naar = math.atan2(-cz, -cx)
            bm = bmesh.new(); bm.from_mesh(o.data); bm.verts.ensure_lookup_table()
            weg = [v for v in bm.verts
                   if abs((math.atan2(v.co.y, v.co.x) - naar + math.pi) % (2 * math.pi) - math.pi) > math.radians(48)]
            bmesh.ops.delete(bm, geom=weg, context="VERTS")
            bm.to_mesh(o.data); bm.free()
            bpy.context.view_layer.objects.active = o; bpy.ops.object.shade_smooth()
    elif naam == "uitroep":
        oranje = g.mat("teken_oranje", "e8742a", rough=0.4)
        _tekst("!", (0, voor, 0.62), 0.62, oranje, "teken_uitroep_teken", ouder, dik=0.05)
    elif naam == "zweet":
        blauw = g.mat("teken_blauw", "5aa8e8", rough=0.25, spec=0.6)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=(0, voor, 0.56))
        d = _obj(bpy.context.object, "teken_zweet_bol", blauw, ouder); d.scale = (0.15, 0.06, 0.15)
        bpy.ops.object.shade_smooth()
        bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=0.142, radius2=0.0, depth=0.26,
                                        location=(0, voor, 0.70))
        k = _obj(bpy.context.object, "teken_zweet_punt", blauw, ouder); k.scale = (1, 0.42, 1)
        bpy.ops.object.shade_smooth()
        bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, location=(-0.05, voor - 0.05, 0.6))
        gl = _obj(bpy.context.object, "teken_zweet_glans", g.mat("teken_glans", "ffffff", rough=0.2, emis=0.6), ouder)
        gl.scale = (0.03, 0.01, 0.045)
    elif naam == "zzz":
        paars = g.mat("teken_paars", "6b4fbf", rough=0.4)
        _tekst("Z", (-0.12, voor, 0.54), 0.36, paars, "teken_zzz_1", ouder, dik=0.04)
        _tekst("z", (0.14, voor, 0.74), 0.28, paars, "teken_zzz_2", ouder, dik=0.04)
    elif naam == "ster":
        goud = g.mat("teken_goud", "f2b632", rough=0.3, spec=0.6, metaal=0.3)
        punten = []
        for i in range(10):
            a = math.radians(90 + 36 * i)
            r = 0.27 if i % 2 == 0 else 0.12
            punten.append((r * math.cos(a), 0, r * math.sin(a)))
        me = bpy.data.meshes.new("teken_ster")
        me.from_pydata(punten, [], [list(range(10))])
        o = bpy.data.objects.new("teken_ster_vorm", me)
        bpy.context.scene.collection.objects.link(o)
        o.location = (0, voor, 0.6)
        o.data.materials.append(goud); o.parent = ouder
        bpy.context.view_layer.objects.active = o
        mod = o.modifiers.new("dik", "SOLIDIFY"); mod.thickness = 0.07
        bev = o.modifiers.new("rond", "BEVEL"); bev.width = 0.02; bev.segments = 3
    ouder.location = (x, y, z)
    ouder.scale = (schaal, schaal, schaal)
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    keuze = sys.argv[5] if len(sys.argv) > 5 else "alle"
    g.leeg()
    nrs = range(5) if keuze == "alle" else [int(keuze)]
    nrs = list(nrs)
    for i, nr in enumerate(nrs):
        bouw(nr, ((i - (len(nrs) - 1) / 2) * 1.1, 0, 0))
    g.camera(hoogte_midden=0.55, schaal=1.1 * len(nrs) + 0.2)
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
