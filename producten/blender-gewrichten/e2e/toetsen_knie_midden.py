"""Toets (Pro 1.2.8, Olaf 24 nov): een scharnier precies op het midden van de knie van de studio-robot.

Regisseur zag op 24 nov (regisseur-24, headless 5.3.0, GEZIEN): robot van 440 mm, met een vlak door de dijen
(z 200) gesplitst, linkerbeen actief, 3D-cursor precies op het midden van de knie, Z langs het been en de
scharnieras x: "Tight: too little limb past this joint to click." 12 mm hoger gaf wel een scharnier. Een koper
klikt juist op het midden van de knie, dus daar hoort een scharnier te komen.

Eisen: op het midden van beide knieën (as x, cursor zoals de koper hem met Shift + rechtsklik zet) komt een
scharnier, groen (Good fit), deel A en B gesloten en elk één stuk. Ook 12 mm hoger blijft het een scharnier (in Blender 4.2 mag
daar de nette melding "the mesh is unchanged" komen: dat deed 1.2.7 ook, de boolean van 4.2 snijdt daar niet).

Gebruik: blender -b --factory-startup --python e2e/toetsen_knie_midden.py -- <betaalde zip>
Uitslag: regels [cj-knie-toets], laatste regel "KLAAR n FOUT".
"""
import importlib
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

H = 440.0
os.environ.setdefault("CJ_VOXEL", "1.0")   # zoals regisseur-24: zelfde fijnheid per lengte als 0,5 bij 220 mm
SNEDE_Z = 100.0 * H / 220.0
HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
PM = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), PM)
A = PM["A"]
STUDIO = os.path.abspath(os.path.join(HIER, "..", "..", "..", "commercie", "filmpjes", "studio"))
FOUT = []


def log(t):
    print(f"[cj-knie-toets] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def splits(fig):
    """Zoals splits() in commercie/filmpjes/regisseur-24/pro_split_opname.py: vlak op SNEDE_Z bij de benen,
    snijvlakken dicht, losse delen Body, Leg.L (+x), Leg.R (-x)."""
    bm = bmesh.new()
    bm.from_mesh(fig.data)
    geom = [v for v in bm.verts if abs(v.co.x) < 0.2 * H and v.co.z < SNEDE_Z + 0.2 * H]
    geom = geom + list({e for v in geom for e in v.link_edges}) + list({f for v in geom for f in v.link_faces})
    res = bmesh.ops.bisect_plane(bm, geom=geom, plane_co=(0, 0, SNEDE_Z), plane_no=(0, 0, 1), dist=0.0005)
    bmesh.ops.split_edges(bm, edges=[e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge)])
    bmesh.ops.holes_fill(bm, edges=[e for e in bm.edges if e.is_boundary], sides=0)
    bm.to_mesh(fig.data)
    bm.free()
    bpy.ops.object.select_all(action="DESELECT")
    fig.select_set(True)
    bpy.context.view_layer.objects.active = fig
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.separate(type="LOOSE")
    bpy.ops.object.mode_set(mode="OBJECT")
    benen = {}
    for o in [o for o in bpy.context.scene.objects if o.type == "MESH"]:
        zs = [o.matrix_world @ v.co for v in o.data.vertices]
        if max(q.z for q in zs) < SNEDE_Z + 1.0 and len(zs) > 500:
            benen["Leg.L" if sum(q.x for q in zs) > 0 else "Leg.R"] = o
    for n, o in benen.items():
        o.name = o.data.name = n
    return benen


def plaats(been, punt, naam):
    """Kopie van het been, cursor op punt (Z omhoog langs het been, X = scharnieras), dan de Knee-knop."""
    k = been.copy()
    k.data = been.data.copy()
    bpy.context.scene.collection.objects.link(k)
    voor = set(bpy.context.scene.objects)
    sc = bpy.context.scene
    sc.cursor.matrix = Matrix.Translation(punt)
    A["actief"](k)
    try:
        r = bpy.ops.click_joints.plaats_preset(deel="KNEE")
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:200]}"
    nieuw = [o for o in sc.objects if o not in voor or o is k]
    ab = [o for o in nieuw if o.get("cj_deel") in ("A", "B") and o.visible_get()]
    a = next((o for o in ab if o.get("cj_deel") == "A"), None)
    melding = k.get("cj_weigering", "") if k.name in sc.objects else ""
    log(f"{naam}: uitslag {r}, delen {len(ab)}, passing {a.get('cj_passing') if a else None}, "
        f"zaag_diepte {round(float(a.get('cj_zaag_diepte', -1)), 2) if a else None}, weigering '{melding}'")
    return r, ab, a


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    A["installeer"](args[0])
    sys.path.insert(0, STUDIO)
    import figuur_laden as FL
    arm, fig, p = FL.laad_figuur("robot", H)
    for m in list(fig.modifiers):
        fig.modifiers.remove(m)
    bpy.data.objects.remove(arm)
    benen = splits(fig)
    check(set(benen) == {"Leg.L", "Leg.R"}, f"twee losse benen ({sorted(benen)})")
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.2, "CURSOR", False
    ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
    for kant, sleutel in (("Leg.L", "l-knee"), ("Leg.R", "r-knee")):
        if kant not in benen:
            continue
        knie = Vector(p[sleutel])
        for dz, wat in ((0.0, "midden"), (12.0 * H / 440.0, "12 mm hoger")):
            r, ab, a = plaats(benen[kant], knie + Vector((0, 0, dz)), f"{kant} {wat} {tuple(round(v, 1) for v in knie + Vector((0, 0, dz)))}")
            ok = r == {"FINISHED"} and len(ab) == 2 and a is not None and a.get("cj_passing") == "groen"
            if not ok and dz and bpy.app.version < (5, 0, 0) and "mesh is unchanged" in str(r) and not ab:
                # 4.2 (24 nov, run 45459661428 en lokaal GEZIEN): de boolean van 4.2 geeft 12 mm hoger geen gesloten
                # delen, ook met de code van main (1.2.7). Geen terugval van 1.2.8; eerlijke melding, mesh heel.
                check(True, f"{kant} knie {wat}: Blender 4.2 snijdt hier niet, nette melding 'the mesh is unchanged' (zoals 1.2.7)")
                continue
            check(ok, f"{kant} knie {wat}: scharnier geplaatst, Good fit")
            if ok:
                check(all(ges.is_gesloten(o)[0] for o in ab), f"{kant} {wat}: A en B gesloten")
                st = [A["mesh_staat"](o)["losse_stukken"] for o in ab]
                check(all(s == 1 for s in st), f"{kant} {wat}: elk deel één stuk ({st})")
            for o in ab:
                bpy.data.objects.remove(o, do_unlink=True)
    log(f"KLAAR {len(FOUT)} FOUT")


main()
