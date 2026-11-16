"""Toets 0.1.1 / Pro 1.0.2: een gewricht in één knie snijdt alleen dat been (fout uit de proef met Meshy-figuren).

Figuur uit één stuk: twee benen (cilinders r 7 mm, 18 mm uit elkaar, voet naar voren) aan een romp. Knie links
op z = 30 mm. Toetsen, elk met gratis kogel en Pro-scharnier (als Pro geladen is):
- deel A is één stuk en ligt alleen links (x < 0);
- deel B bevat het rechterbeen heel (laagste punt rechts op z ~ 0) en is één stuk;
- beide delen gesloten, volume A + B iets onder het figuur (alleen de speling weg);
- twee voeten op één voetstuk: niet snijden, melding "joined to another part".
Gebruik: blender -b --factory-startup --python e2e/toetsen_een_lid.py -- <zip>
"""
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

FOUT = []
MAAT = {"r": 7.0, "x": 9.0}  # beenstraal en afstand tot het midden; de kogel krijgt dikkere benen


def log(t):
    print(f"[cj-lid] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def leeg():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"


def figuur(voetstuk=False):
    bm = bmesh.new()
    for x in (-MAAT["x"], MAAT["x"]):
        m = Matrix.Translation((x, 0, 30))
        bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=MAAT["r"], radius2=MAAT["r"], depth=60, matrix=m)
        bmesh.ops.create_cube(bm, size=1, matrix=Matrix.Translation((x, -4, 2)) @ Matrix.Diagonal((11, 16, 4, 1)))
    bmesh.ops.create_cube(bm, size=1, matrix=Matrix.Translation((0, 0, 75)) @ Matrix.Diagonal((34, 16, 34, 1)))
    if voetstuk:
        bmesh.ops.create_cube(bm, size=1, matrix=Matrix.Translation((0, -2, -1)) @ Matrix.Diagonal((44, 24, 4, 1)))
    me = bpy.data.meshes.new("broek_bron")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("broek_bron", me)
    bpy.context.scene.collection.objects.link(ob)
    # Eén gesloten stuk via remesh (zoals Make watertight)
    r = ob.modifiers.new("vox", "REMESH")
    r.mode, r.voxel_size = "VOXEL", 0.5
    dg = bpy.context.evaluated_depsgraph_get()
    me2 = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    bpy.data.objects.remove(ob)
    uit = bpy.data.objects.new("broek", me2)
    bpy.context.scene.collection.objects.link(uit)
    return uit


def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def stukken(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.transform(ob.matrix_world)
    gezien, n = set(), 0
    for v in bm.verts:
        if v.index in gezien:
            continue
        n += 1
        rij = [v]
        gezien.add(v.index)
        while rij:
            w = rij.pop()
            for e in w.link_edges:
                o = e.other_vert(w)
                if o.index not in gezien:
                    gezien.add(o.index)
                    rij.append(o)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True)
    xs = [v.co.x for v in bm.verts]
    laag_rechts = min((v.co.z for v in bm.verts if v.co.x > 2), default=None)
    bm.free()
    return n, fout, vol, min(xs), max(xs), laag_rechts


def cursor(z, soort):
    m = Matrix.Identity(4)
    m.col[3][:3] = Vector((-MAAT["x"] + 0.031, 0.137, z + 0.071))  # niet precies op het voxelraster (stralen langs een rand missen)
    cur = bpy.context.scene.cursor
    cur.rotation_mode = "QUATERNION"
    cur.matrix = m
    inst = bpy.context.scene.click_joints
    inst.as_bron, inst.uit_elkaar = "CURSOR", False
    if soort == "KOGEL":
        inst.soort, inst.kogel_auto = "KOGEL", True


def proef(soort, voetstuk=False):
    leeg()
    ob = figuur(voetstuk)
    vol0 = stukken(ob)[2]
    cursor(30.0, soort)
    actief(ob)
    try:
        if soort == "KOGEL":
            r = bpy.ops.click_joints.plaats()
        else:
            r = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as e:
        r = f"fout {e}"
    delen = {o.get("cj_deel"): o for o in bpy.context.scene.objects if o.get("cj_deel")}
    from click_joints import een_lid  # noqa (extensie-pad)
    return r, delen, vol0, dict(een_lid.LAATSTE)


def main():
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    import importlib
    global click_joints
    sys.modules.setdefault("click_joints", importlib.import_module("bl_ext.user_default.click_joints"))
    pro = "plaats_scharnier" in dir(bpy.ops.click_joints)
    log(f"Blender {bpy.app.version_string}, Pro {pro}")
    for soort in (["KOGEL", "SCHARNIER"] if pro else ["KOGEL"]):
        MAAT.update(r=10.0, x=12.0) if soort == "KOGEL" else MAAT.update(r=7.0, x=9.0)
        r, delen, vol0, lid = proef(soort)
        log(f"{soort}: uitslag {r}, een_lid {lid}")
        a, b = delen.get("A"), delen.get("B")
        check(a is not None and b is not None, f"{soort}: twee delen")
        if a is None or b is None:
            continue
        na, fa, va, xa0, xa1, _ = stukken(a)
        nb, fb, vb, _, _, laag = stukken(b)
        log(f"{soort}: A stukken {na} open {fa} vol {va:.0f} x {xa0:.1f}..{xa1:.1f}; B stukken {nb} open {fb} "
            f"vol {vb:.0f} laagste rechts {laag}; figuur {vol0:.0f}")
        check(na == 1 and fa == 0, f"{soort}: deel A één gesloten stuk")
        check(xa1 < -0.5, f"{soort}: deel A alleen links (max x {xa1:.2f})")
        check(nb == 1 and fb == 0, f"{soort}: deel B één gesloten stuk")
        check(laag is not None and laag < 0.6, f"{soort}: rechterbeen heel in B (laagste {laag})")
        check(0.93 * vol0 < va + vb < vol0 + 1, f"{soort}: volume A+B {va + vb:.0f} bij figuur {vol0:.0f}")
        r, delen, _, lid = proef(soort, voetstuk=True)
        log(f"{soort} voetstuk: uitslag {r}, een_lid {lid}")
        check(not delen and lid.get("lid") is None, f"{soort} voetstuk: niet gesneden")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
