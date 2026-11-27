"""Toets 0.1.3 / Pro (issue 306): een knie van een figuur met tenen laat geen losse teenstukjes in deel A.

Figuur: Blender Human Base Meshes v1.4.1, `GEO-body_male_stylized` met zijn twee ogen (CC0, Blender Studio), samengevoegd
en geschaald naar 200 mm, normalen naar buiten. Kogel, Auto, as langs de 3D-cursor in de rechterknie (zoals het
Printables-beeld van de Beeldmaker, #297). Oorzaak: de tenen staan zo dicht op elkaar dat de verschoven huid van het
lid zichzelf tussen de tenen snijdt; de vereniging met het omhulsel liet dan stukjes tenen weg en die bleven in deel A.
Toetsen:
- deel A: het lijf en de twee ogen (met Exact soms één schil), geen schil kleiner dan 2% van het lijf;
- deel B: één stuk (de tenen zitten aan de voet);
- beide delen gesloten;
- de laagste punten van het rechterbeen (de voet) zitten in B, niet in A.
Gebruik: blender -b --factory-startup --python e2e/toetsen_tenen.py -- <zip> <human_base_meshes_bundle.blend>
"""
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

FOUT = []


def log(t):
    print(f"[cj-tenen] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def schillen(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.verts.ensure_lookup_table()
    gezien, uit = set(), []
    for v in bm.verts:
        if v.index in gezien:
            continue
        rij, n = [v], 0
        gezien.add(v.index)
        while rij:
            w = rij.pop()
            n += 1
            for e in w.link_edges:
                o = e.other_vert(w)
                if o.index not in gezien:
                    gezien.add(o.index)
                    rij.append(o)
        uit.append(n)
    open_ = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    laag = min((ob.matrix_world @ v.co).z for v in bm.verts)
    bm.free()
    return sorted(uit, reverse=True), open_, laag


def volume(o):
    bm = bmesh.new()
    bm.from_mesh(o.data)
    bm.transform(o.matrix_world)
    v = abs(bm.calc_volume(signed=True))
    bm.free()
    return v


def main():
    a = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, blend = a[0], a[1]
    bpy.ops.wm.open_mainfile(filepath=blend)
    ob = bpy.data.objects["GEO-body_male_stylized"]
    ogen = [bpy.data.objects[n] for n in ("GEO-body_male_stylized.eye.L", "GEO-body_male_stylized.eye.R")]
    for o in list(bpy.data.objects):
        if o is not ob and o not in ogen:
            bpy.data.objects.remove(o)
    sc = bpy.context.scene
    for o in [ob] + ogen:
        for m in list(o.modifiers):
            o.modifiers.remove(m)
        if o.name not in sc.collection.objects:
            sc.collection.objects.link(o)
        o.hide_set(False)
        o.hide_viewport = False
    for o in bpy.data.objects:
        o.select_set(o is ob or o in ogen)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.join()
    sc.unit_settings.system, sc.unit_settings.scale_length, sc.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
    V = [ob.matrix_world @ v.co for v in ob.data.vertices]
    lo = Vector([min(v[i] for v in V) for i in range(3)])
    hi = Vector([max(v[i] for v in V) for i in range(3)])
    f = 200.0 / (hi.z - lo.z)
    ob.matrix_world = Matrix.Scale(f, 4) @ Matrix.Translation(-Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z))) @ ob.matrix_world
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    bm.to_mesh(ob.data)
    bm.free()
    n0 = len(schillen(ob)[0])
    vol0 = volume(ob)
    log(f"Blender {bpy.app.version_string}, figuur {len(ob.data.vertices)} punten, {n0} schillen")

    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    inst = sc.click_joints
    inst.soort, inst.as_bron, inst.kogel_auto, inst.uit_elkaar = "KOGEL", "CURSOR", True, False
    V = [v.co.copy() for v in ob.data.vertices]

    def midden(z):
        p = [v for v in V if 1.0 * 200 / 180 <= v.x <= 30.0 * 200 / 180 and z - 1.5 <= v.z <= z + 1.5]
        return sum(p, Vector()) / len(p)
    z = 61.0 * 200 / 180
    p, q = midden(z), midden(z - 4.0 * 200 / 180)
    rot = (q - p).normalized().to_track_quat("Z", "Y").to_matrix().to_4x4()
    sc.cursor.matrix = Matrix.Translation(p) @ rot
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    try:
        r = bpy.ops.click_joints.plaats()
    except RuntimeError as e:
        r = f"fout {e}"
    delen = {o.get("cj_deel"): o for o in sc.objects if o.get("cj_deel")}
    lid = {}
    for naam, mod in sys.modules.items():
        if naam.endswith(".een_lid") and hasattr(mod, "LAATSTE"):
            lid = {k: mod.LAATSTE.get(k) for k in ("lussen", "lid", "h_soort", "h_pogingen", "h_voxel_buiten")}
    log(f"uitslag {r}, een_lid {lid}")
    A, B = delen.get("A"), delen.get("B")
    check(A is not None and B is not None, "twee delen")
    if A is None or B is None:
        log(f"KLAAR {len(FOUT)} FOUT")
        return
    sa, oa, _ = schillen(A)
    sb, ob_, laag_b = schillen(B)
    log(f"A schillen {sa[:12]} open {oa}; B schillen {sb[:12]} open {ob_} laagste {laag_b:.2f}")
    klein = [n for n in sa if n < 0.02 * sa[0]]
    # Met Exact (4.2) smelten de ogen soms met het hoofd samen (1 schil); dat is goed. Fout zijn kleine stukjes.
    check(len(sa) <= n0 and not klein, f"deel A: lijf en ogen, geen losse stukjes ({len(sa)} schillen, {n0} in het figuur, klein {klein[:10]})")
    check(len(sb) == 1, f"deel B één stuk ({len(sb)} schillen)")
    check(oa == 0 and ob_ == 0, f"beide delen gesloten (open A {oa}, B {ob_})")
    # Keuring #326 K1: de voxelvorm mag niet ongemerkt veel van het figuur wegeten. A + B is iets kleiner dan het
    # figuur (speling en gat rond de kogel); meer dan 6% verlies is fout.
    va, vb = volume(A), volume(B)
    verlies = 100.0 * (1 - (va + vb) / vol0) if vol0 > 0 else 100.0
    log(f"VOLUME figuur {vol0:.0f}, A {va:.0f} + B {vb:.0f}, verlies {verlies:.1f}% (h_soort {lid.get('h_soort')})")
    check(-0.5 <= verlies <= 6.0, f"volume A+B hooguit 6% onder het figuur (verlies {verlies:.1f}%)")
    laag_a_rechts = min(((A.matrix_world @ v.co).z for v in A.data.vertices if (A.matrix_world @ v.co).x > 2), default=99)
    check(laag_a_rechts > 20 and laag_b < 1.0, f"rechtervoet in B (A rechts laagste {laag_a_rechts:.1f}, B laagste {laag_b:.2f})")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
