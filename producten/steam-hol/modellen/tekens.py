"""Tekens boven het hoofd van een held in 3D (Daan, 14 nov 2026). Vervangt kunst/tekens.png (8 x 8 pixels).

Volgorde zoals tekens.png: 0 boos, 1 uitroep, 2 zweet, 3 zzz, 4 ster. Erbij (14 nov 02:40): 5 noot, het
muzieknootje van de bard en de liedheld (nu `NOOT_PIX` in held_beeld.gd). Dat is geen wolkje maar een los
gouden achtste noot met een donkere rug, zodat hij op lucht en aarde leest zonder pixelrand.
Erbij (14 nov 08:40): 6 laars, de laars die Gloop uitspuugt (nu kunst/laars.png, `HB.teken_3d(self, "laars")` in
slijm.gd). Achteraan, want 0 tot 5 liggen vast in de toetsen. Zijaanzicht met de neus naar rechts, zool op de
bodem van de cel (onder-midden), met een omgeslagen kraag en een donkere rug zoals de noot.
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

NAMEN = ["boos", "uitroep", "zweet", "zzz", "ster", "noot", "laars", "veer"]
GROOT = 0.86  # maat van de laars (Daan 08:55)
TIL = 0.08    # laars omhoog zodat de onderkant van de rug gelijk ligt met de punt van de staartjes
BOOS_AF = float(os.environ.get("TEKEN_BOOS_AF", "0.16"))     # was 0.21 (Mila 16 nov)
BOOS_DIK = float(os.environ.get("TEKEN_BOOS_DIK", "0.07"))   # was 0.04
ZWEET_GROOT = float(os.environ.get("TEKEN_ZWEET_GROOT", "1.3"))  # was 1.0
ZWEET_KLEUR = os.environ.get("TEKEN_ZWEET_KLEUR", "3a86d8")    # was 5aa8e8
BOOS_VORM = os.environ.get("TEKEN_BOOS_VORM", "wolk")      # "wolk" (rood met frons) of "ader" (vier bogen)
BOOS_SCHUIN = float(os.environ.get("TEKEN_BOOS_SCHUIN", "32"))
BOOS_RAND = os.environ.get("TEKEN_BOOS_RAND", "1") == "1"   # Mila 16 nov (Daan 15:32): lichte rand om het rode wolkje
SCHUIF = -0.095 # laars naar links, zodat hij in het midden van de cel staat en de cel 8 breed blijft


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
    if naam in ("noot", "laars", "veer"):
        {"noot": _noot, "laars": _laars, "veer": _veer}[naam](ouder)
        ouder.location = (x, y, z)
        ouder.scale = (schaal, schaal, schaal)
        return ouder
    room = g.mat(f"teken_room_{naam}", "fbf3df", rough=0.55, spec=0.3)
    if naam == "boos" and BOOS_VORM == "wolk" and BOOS_RAND:
        # Mila 16 nov (Daan 15:32, kans 1): op ware grootte zakte het rode wolkje weg in de roodbruine aarde. Nu blijft
        # het buitenste wolkje en het staartje room, zoals bij de andere tekens, en ligt er een kleiner rood wolkje
        # voor: een lichte rand van ±0,8 spelpixel. Zelfde buitenmaat, dus de cel en de schaal van alle tekens blijven.
        rood = g.mat("teken_rood_wolk", "d8423b", rough=0.45, spec=0.35)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, location=(0, -0.03, 0.635))
        b = _obj(bpy.context.object, "teken_boos_binnen", rood, ouder)
        b.scale = (0.335, 0.14, 0.295); bpy.ops.object.shade_smooth()
    elif naam == "boos" and BOOS_VORM == "wolk":
        # Mila 16 nov: Daan's tweede voorstel. Een rood wolkje (boos = rood, ook als je de vorm niet ziet) met
        # twee dikke donkere gefronste wenkbrauwen \ / erop. Leest op 8 x 8 als kwaad gezicht.
        room = g.mat("teken_rood_wolk", "d8423b", rough=0.45, spec=0.35)
    # wolkje: platte bol met staartje, net iets naar de camera
    bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, location=(0, 0.02, 0.62))
    w = _obj(bpy.context.object, f"teken_{naam}_wolk", room, ouder)
    w.scale = (0.42, 0.16, 0.38); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.12, radius2=0.0, depth=0.26,
                                    location=(0.0, 0.02, 0.2), rotation=(math.radians(180), 0, 0))
    t = _obj(bpy.context.object, f"teken_{naam}_staart", room, ouder)
    t.scale = (1, 0.6, 1); bpy.ops.object.shade_smooth()
    voor = -0.16  # symbool op de voorkant van het wolkje
    if naam == "boos" and BOOS_VORM == "wolk":
        donker = g.mat("teken_frons", "2a1810", rough=0.6)
        for kant in (1, -1):
            # binnenkant laag, buitenkant hoog: \ / (draaien om y met min, want +y draait rechts omlaag)
            o = _blok(ouder, f"teken_boos_frons_{kant}", donker, (0.0, 0.0, 0.0), (0.12, 0.04, 0.048), rond=0.03)
            o.rotation_euler = (0, math.radians(-BOOS_SCHUIN * kant), 0)
            o.location = (0.13 * kant, voor - 0.04, 0.66)
    elif naam == "boos":
        rood = g.mat("teken_rood", "d8423b", rough=0.4)
        # vier bogen, elk in een eigen hoek en bol naar het midden (de bekende boze ader)
        import bmesh
        for i, (sx, sz) in enumerate(((1, 1), (-1, 1), (-1, -1), (1, -1))):
            # Mila 16 nov (Daan, Iris keuring 2): dikker en dichter bij het midden, zodat het op 8 x 8 één rode
            # knoop leest in plaats van een vizier (was 0.21 en 0.04)
            cx, cz = BOOS_AF * sx, BOOS_AF * sz
            bpy.ops.mesh.primitive_torus_add(major_radius=0.14, minor_radius=BOOS_DIK, major_segments=48,
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
        # Mila 16 nov (Daan, Iris keuring 2): druppel 1,3x groter en donkerder blauw (was 5aa8e8), want de
        # lichtblauwe stip viel op ware grootte weg in het room. Midden van de druppel blijft op z 0.62.
        Z = ZWEET_GROOT
        blauw = g.mat("teken_blauw", ZWEET_KLEUR, rough=0.25, spec=0.6)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=(0, voor, 0.62 - 0.06 * Z))
        d = _obj(bpy.context.object, "teken_zweet_bol", blauw, ouder); d.scale = (0.15 * Z, 0.06, 0.15 * Z)
        bpy.ops.object.shade_smooth()
        bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=0.142 * Z, radius2=0.0, depth=0.26 * Z,
                                        location=(0, voor, 0.62 + 0.08 * Z))
        k = _obj(bpy.context.object, "teken_zweet_punt", blauw, ouder); k.scale = (1, 0.42, 1)
        bpy.ops.object.shade_smooth()
        bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8,
                                             location=(-0.05 * Z, voor - 0.05, 0.62 - 0.02 * Z))
        gl = _obj(bpy.context.object, "teken_zweet_glans", g.mat("teken_glans", "ffffff", rough=0.2, emis=0.6), ouder)
        gl.scale = (0.03 * Z, 0.01, 0.045 * Z)
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


def _noot(ouder):
    """Achtste noot: schuin ovaal kopje, steel rechts omhoog, vlag naar rechts omlaag.
    Goud zoals de ster, met een donkerbruine rug er net achter en iets groter: die geeft op ware grootte
    de rand die het pixelnootje met losse pixels had (leesbaar op lucht en op de paarse aarde)."""
    goud = g.mat("teken_noot_goud", "ffd25a", rough=0.3, spec=0.6, metaal=0.25)
    rug = g.mat("teken_noot_rug", "2a1810", rough=0.7)
    for laag, m, dik, y0 in (("rug", rug, 1.0, 0.07), ("voor", goud, 0.0, 0.0)):
        e = 0.035 * dik  # rug iets dikker rondom (was 0.05; frisse kijker: groot te zwaar)
        # kopje: platte ellips, 25 graden gekanteld
        bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, location=(-0.1, y0, 0.2))
        k = _obj(bpy.context.object, f"teken_noot_{laag}_kop", m, ouder)
        k.scale = (0.2 + e, 0.09, 0.14 + e); k.rotation_euler = (0, math.radians(25), 0)
        bpy.ops.object.shade_smooth()
        # steel
        bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.045 + e, depth=0.62 + e,
                                            location=(0.075, y0, 0.52))
        st = _obj(bpy.context.object, f"teken_noot_{laag}_steel", m, ouder)
        st.scale = (1, 0.7, 1); bpy.ops.object.shade_smooth()
        # vlag: dikke gebogen staart van de top van de steel naar rechtsonder
        cu = bpy.data.curves.new(f"teken_noot_{laag}_vlag", "CURVE")
        cu.dimensions = "3D"; cu.bevel_depth = 0.045 + e; cu.bevel_resolution = 4
        sp = cu.splines.new("BEZIER"); sp.bezier_points.add(1)
        a, b = sp.bezier_points
        a.co = (0.075, y0, 0.8); a.handle_left = (0.075, y0, 0.9); a.handle_right = (0.12, y0, 0.66)
        b.co = (0.3, y0, 0.42); b.handle_left = (0.32, y0, 0.58); b.handle_right = (0.28, y0, 0.36)
        sp.use_cyclic_u = False
        o = bpy.data.objects.new(f"teken_noot_{laag}_vlag", cu)
        bpy.context.scene.collection.objects.link(o)
        o.data.materials.append(m); o.parent = ouder
        # glansje op het kopje (alleen voor)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, location=(-0.16, -0.08, 0.25))
    gl = _obj(bpy.context.object, "teken_noot_glans", g.mat("teken_glans", "ffffff", rough=0.2, emis=0.6), ouder)
    gl.scale = (0.05, 0.01, 0.025)


def _blok(ouder, naam, m, loc, maat, rond=0.04, seg=3):
    """Afgerond blok: kubus met bevel, maat is de halve breedte, diepte, hoogte."""
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = _obj(bpy.context.object, naam, m, ouder)
    o.scale = maat
    bpy.context.view_layer.objects.active = o
    bpy.ops.object.transform_apply(scale=True)
    b = o.modifiers.new("rond", "BEVEL"); b.width = rond; b.segments = seg
    bpy.ops.object.shade_smooth()
    return o


def _laars(ouder):
    """Laars in zijaanzicht, neus naar rechts. Hout-bruin zoals de pixellaars (8a5b33), zodat hij op de paarse
    vloer leest; zool en hak donkerder, kraag lichter omgeslagen; schacht kort en neus lang (een duidelijke L). Onderkant zool op z 0.07, net als de punt van de
    staartjes, zodat hij in het blad op de bodem van de cel staat."""
    leer = g.mat("laars_leer", "b07a43", rough=0.5, spec=0.35)
    kraag = g.mat("laars_kraag", "e8b673", rough=0.55, spec=0.3)
    zool = g.mat("laars_zool", "5c3720", rough=0.7)
    # schacht: rond (cilinder), iets naar achteren, smaller dan de kraag
    bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=0.19, depth=0.62, location=(-0.14, 0, 0.53))
    sc = _obj(bpy.context.object, "laars_schacht", leer, ouder)
    b = sc.modifiers.new("rond", "BEVEL"); b.width = 0.05; b.segments = 3
    bpy.ops.object.shade_smooth()
    # voet: lange ronde neus naar rechts
    bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, location=(0.24, 0, 0.21))
    v = _obj(bpy.context.object, "laars_neus", leer, ouder)
    v.scale = (0.34, 0.16, 0.15); bpy.ops.object.shade_smooth()
    _blok(ouder, "laars_wreef", leer, (0.0, 0, 0.23), (0.24, 0.155, 0.14), rond=0.08, seg=4)
    # zool en hak
    _blok(ouder, "laars_zool", zool, (0.13, 0, 0.1), (0.46, 0.165, 0.035), rond=0.03)
    _blok(ouder, "laars_hak", zool, (-0.23, 0, 0.14), (0.1, 0.16, 0.065), rond=0.025)
    # omgeslagen kraag bovenaan: een bredere, platte ring, iets schuin naar achteren
    bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=0.24, depth=0.16, location=(-0.14, 0, 0.88),
                                        rotation=(0, math.radians(-6), 0))
    kr = _obj(bpy.context.object, "laars_kraagband", kraag, ouder)
    b = kr.modifiers.new("rond", "BEVEL"); b.width = 0.06; b.segments = 4
    bpy.ops.object.shade_smooth()
    # geen slijm en geen gesp: op 7 x 8 spelpixels werden die ruis (frisse kijker 08:58, groen las als sjaal of lampje)
    # donkere rug net achter de laars en iets dikker rondom, net als bij de noot: op ware grootte geeft die de rand
    # die de pixellaars had, anders verdwijnt de lichte kraag tegen de roze schatkamer (Daan 08:50, gemeten op f395)
    rug = g.mat("laars_rug", "22121a", rough=0.7)
    for o in list(ouder.children):
        k = o.copy(); k.data = o.data.copy(); k.name = o.name + "_rug"
        bpy.context.scene.collection.objects.link(k)
        k.parent = ouder; k.data.materials.clear(); k.data.materials.append(rug)
        k.location = (k.location[0], k.location[1] + 0.09, k.location[2] - 0.035)
        d = k.modifiers.new("dik", "DISPLACE"); d.mid_level = 0.0; d.strength = 0.035
    # maat en hoogte zo dat het blad 8 x 8 spelpixels blijft en de andere tekens even groot (eenheid_px gelijk)
    for o in ouder.children:
        o.location = (SCHUIF + o.location[0] * GROOT, o.location[1], 0.07 + TIL + (o.location[2] - 0.07) * GROOT)
        o.scale = tuple(v * GROOT for v in o.scale)


def _veer(ouder):
    """Mila 25 nov (issue #76): de veer onder Bouncy Gloop. Na de koop staat Gloop op twee gouden veren, zodat je
    zonder tekst ziet dat hij nu verende sprongen maakt. Zijaanzicht van een schroefveer: 3 slagen goud draad tussen
    een donkere voetplaat en een donker plaatje bovenop, met een donkere rug erachter zoals de noot en de laars,
    zodat de veer op de roodbruine vloer en tegen het groen een rand houdt. Onderkant op de bodem van de cel."""
    goud = g.mat("teken_veer_goud", "ffd25a", rough=0.25, spec=0.8, metaal=0.6, emis=0.25)
    donker = g.mat("teken_veer_plaat", "2a1810", rough=0.6)
    r, hoog, slagen, draad = 0.2, 0.5, 3.0, 0.045
    z0 = 0.16   # voetplaat net boven z 0.07, de punt van de staartjes: dan blijft de maat van het blad gelijk
    for laag, m, e, y0 in (("rug", donker, 0.015, 0.08), ("voor", goud, 0.0, 0.0)):
        cu = bpy.data.curves.new(f"teken_veer_{laag}", "CURVE")
        cu.dimensions = "3D"; cu.bevel_depth = draad + e; cu.bevel_resolution = 4
        sp = cu.splines.new("POLY")
        n = int(slagen * 32)
        sp.points.add(n)
        for i in range(n + 1):
            a = 2 * math.pi * slagen * i / n
            sp.points[i].co = (r * math.cos(a), y0 + r * 0.45 * math.sin(a), z0 + hoog * i / n, 1.0)
        o = bpy.data.objects.new(f"teken_veer_{laag}", cu)
        bpy.context.scene.collection.objects.link(o)
        o.data.materials.append(m); o.parent = ouder
    _blok(ouder, "veer_voet", donker, (0, 0, z0 - 0.035), (0.27, 0.12, 0.035), rond=0.02)
    _blok(ouder, "veer_top", donker, (0, 0, z0 + hoog + 0.025), (0.24, 0.1, 0.025), rond=0.015)


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    keuze = sys.argv[5] if len(sys.argv) > 5 else "alle"
    g.leeg()
    nrs = range(len(NAMEN)) if keuze == "alle" else [int(keuze)]
    nrs = list(nrs)
    for i, nr in enumerate(nrs):
        bouw(nr, ((i - (len(nrs) - 1) / 2) * 1.1, 0, 0))
    g.camera(hoogte_midden=0.55, schaal=1.1 * len(nrs) + 0.2)
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
