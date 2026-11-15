"""Proef: werkt Click Joints Pro op een figuur die een AI-generator maakte (Meshy)?

Aanleiding: voorstel Lars 15 nov (platformen/succes/verhalen.md, Cleave): een blok "Made for AI-generated figures"
op de Superhive-pagina mag pas als we het zelf zagen werken. Dit script laat dat zien of niet, zonder iets te
beloven. Het meet per model: hoeveel losse stukken en open randen de AI-mesh heeft, en of de knie (Pro-scharnier)
en de nek (gratis kogel) twee gesloten delen geven.

Gebruik (echte Blender, achtergrond):
  blender -b --factory-startup --python e2e/proef_ai_model.py -- <zip> <uitmap> <model.glb> [<model.glb> ...]
Per model komt er <uitmap>/<naam>.blend bij, voor een beeld. Uitslag in het log, regels met [cj-ai].
"""
import math
import os
import sys
import time

import bmesh
import bpy
from mathutils import Matrix, Vector

HOOGTE_MM = float(os.environ.get("CJ_HOOGTE", "150"))  # standaard een actiefiguur van 15 cm


def log(t):
    print(f"[cj-ai] {t}", flush=True)


def installeer(zip_pad):
    if "plaats_scharnier" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    log(f"Pro geladen: {'plaats_scharnier' in dir(bpy.ops.click_joints)}")


def leeg():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"


def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def laad(pad):
    """GLB inladen, alle meshes tot één object, transformaties vast, 150 mm hoog, voeten op z=0, midden op x=y=0."""
    bpy.ops.import_scene.gltf(filepath=pad)
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    for o in bpy.context.scene.objects:
        o.select_set(o.type == "MESH")
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    ob = bpy.context.view_layer.objects.active
    for o in list(bpy.context.scene.objects):
        if o is not ob and o.type != "MESH":
            bpy.data.objects.remove(o)
    ob.parent = None
    actief(ob)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # Meshy-figuren kijken na het inladen naar +x (GEZIEN in een render); draai ze een kwartslag zodat ze naar -y
    # kijken zoals in Blenders vooraanzicht: dan is x links-rechts en y voor-achter.
    for v in ob.data.vertices:
        v.co = Vector((v.co.y, -v.co.x, v.co.z))
    ob.data.update()
    hoeken = [ob.matrix_world @ Vector(h) for h in ob.bound_box]
    lo = Vector((min(h.x for h in hoeken), min(h.y for h in hoeken), min(h.z for h in hoeken)))
    hi = Vector((max(h.x for h in hoeken), max(h.y for h in hoeken), max(h.z for h in hoeken)))
    f = HOOGTE_MM / (hi.z - lo.z)
    me = ob.data
    for v in me.vertices:
        v.co = Vector(((v.co.x - (lo.x + hi.x) / 2) * f, (v.co.y - (lo.y + hi.y) / 2) * f, (v.co.z - lo.z) * f))
    me.update()
    ob.name = me.name = os.path.splitext(os.path.basename(pad))[0]
    return ob


def mesh_staat(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    open_r = sum(1 for e in bm.edges if len(e.link_faces) < 2)
    veel_r = sum(1 for e in bm.edges if len(e.link_faces) > 2)
    # losse stukken tellen
    gezien, stukken = set(), 0
    for v in bm.verts:
        if v.index in gezien:
            continue
        stukken += 1
        rij = [v]
        gezien.add(v.index)
        while rij:
            w = rij.pop()
            for e in w.link_edges:
                o = e.other_vert(w)
                if o.index not in gezien:
                    gezien.add(o.index)
                    rij.append(o)
    tri = sum(len(f.verts) - 2 for f in bm.faces)
    bm.free()
    return {"driehoeken": tri, "open_randen": open_r, "randen_3plus": veel_r, "losse_stukken": stukken}


def lussen(ob, z):
    """Doorsnede van het object op hoogte z als losse lussen: [(midden, breedte_x, breedte_y)], in wereldmaat."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.transform(ob.matrix_world)
    geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
    snee = bmesh.ops.bisect_plane(bm, geom=geom, plane_co=(0, 0, z), plane_no=(0, 0, 1))
    randen = [e for e in snee["geom_cut"] if isinstance(e, bmesh.types.BMEdge)]
    punten = {v for e in randen for v in e.verts}
    buren = {v: [] for v in punten}
    for e in randen:
        buren[e.verts[0]].append(e.verts[1])
        buren[e.verts[1]].append(e.verts[0])
    uit, gezien = [], set()
    for v in punten:
        if v in gezien:
            continue
        rij, lus = [v], []
        gezien.add(v)
        while rij:
            w = rij.pop()
            lus.append(w.co.copy())
            for o in buren[w]:
                if o not in gezien:
                    gezien.add(o)
                    rij.append(o)
        if len(lus) >= 6:
            c = sum(lus, Vector()) / len(lus)
            uit.append((c, max(p.x for p in lus) - min(p.x for p in lus), max(p.y for p in lus) - min(p.y for p in lus)))
    bm.free()
    return uit


def doorsnede(ob, z, kant):
    """Midden en breedte van een been aan één kant (x<0 of x>0) op hoogte z: een losse lus van 8 tot 35 mm breed."""
    kand = [l for l in lussen(ob, z) if (l[0].x < -1.0 if kant < 0 else l[0].x > 1.0) and 8.0 <= l[1] <= 35.0
            and 8.0 <= l[2] <= 35.0]
    if not kand:
        return None, 0.0
    beste = min(kand, key=lambda l: abs(l[0].x))  # het been ligt het dichtst bij het midden (niet hand of zwaard)
    return beste[0], beste[1]


def delen(naam):
    return [o for o in bpy.context.scene.objects if o.get("cj_deel") and o.name.startswith(naam)]


def gesloten(lijst):
    uit = []
    for d in lijst:
        bm = bmesh.new()
        bm.from_mesh(d.data)
        fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
        vol = bm.calc_volume(signed=True)
        bm.free()
        uit.append((d.name, fout, round(vol, 1)))
    return uit


def knie(ob):
    """Pro-scharnier in de linkerknie (x<0); scharnieras links-rechts, buigkant achter (+y). Probeert hoogtes van
    24 tot 32% van de figuur, zoals een koper de cursor een stukje verschuift als de add-on "Try a thicker spot" zegt."""
    for pct in (27, 25, 29, 24, 31, 32):
        lijst = knie_op(ob, pct / 100.0 * HOOGTE_MM)
        if lijst:
            return lijst
    return None


def knie_op(ob, z):
    c, breed = doorsnede(ob, z, -1)
    if c is None:
        log(f"{ob.name} knie: geen been gevonden op z={z:.1f}")
        return None
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    m.col[3][:3] = c
    cur = bpy.context.scene.cursor
    cur.rotation_mode = "QUATERNION"
    cur.matrix = m
    inst = bpy.context.scene.click_joints
    inst.as_bron, inst.uit_elkaar = "CURSOR", True
    actief(ob)
    t0 = time.perf_counter()
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        uitslag = f"fout: {str(fout).strip()[:200]}"
    duur = time.perf_counter() - t0
    lijst = delen(ob.name)
    a = next((d for d in lijst if d.get("cj_deel") == "A"), None)
    log(f"{ob.name} KNIE op ({c.x:.1f}, {c.y:.1f}, {c.z:.1f}) beenbreedte {breed:.1f} mm: uitslag={uitslag} "
        f"tijd={duur:.1f}s delen={gesloten(lijst)} bereik={a.get('cj_bereik_graden') if a else None} "
        f"knokkel_r={a.get('cj_knokkel_r') if a else None} melding={a.get('cj_melding') if a else None}")
    return lijst


def nek(ob_naam):
    """Gratis kogel in de nek: de smalste lus in het midden tussen 76 en 90% van de hoogte, as omhoog."""
    kandidaten = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.name.startswith(ob_naam)
                  and o.visible_get()]
    beste = None
    for pct in range(76, 91, 2):
        z = pct / 100.0 * HOOGTE_MM
        for o in kandidaten:
            for c, bx, by in lussen(o, z):
                if abs(c.x) < 15.0 and bx >= 6.0 and (beste is None or bx < beste[2]):
                    beste = (o, c, bx)
    if beste is None:
        log(f"{ob_naam} NEK: geen nek gevonden")
        return
    doel, c, _ = beste
    cur = bpy.context.scene.cursor
    cur.location = c
    cur.rotation_mode = "QUATERNION"
    cur.rotation_quaternion = Vector((0, 0, 1)).to_track_quat("Z", "Y")
    inst = bpy.context.scene.click_joints
    inst.soort, inst.as_bron, inst.kogel_auto = "KOGEL", "CURSOR", True
    voor = set(o.name for o in bpy.context.scene.objects)
    actief(doel)
    t0 = time.perf_counter()
    try:
        uitslag = bpy.ops.click_joints.plaats()
    except RuntimeError as fout:
        uitslag = f"fout: {str(fout).strip()[:200]}"
    duur = time.perf_counter() - t0
    nieuw = [o for o in bpy.context.scene.objects if o.name not in voor and o.get("cj_deel")]
    log(f"{ob_naam} NEK op ({c.x:.1f}, {c.y:.1f}, {c.z:.1f}) in {doel.name}: uitslag={uitslag} tijd={duur:.1f}s "
        f"kogel_mm={inst.kogel_mm:.1f} nieuwe_delen={gesloten(nieuw)}")


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, uit = args[0], args[1]
    os.makedirs(uit, exist_ok=True)
    installeer(zip_pad)
    for pad in args[2:]:
        leeg()
        ob = laad(pad)
        st = mesh_staat(ob)
        log(f"{ob.name} MESH {st}")
        if st["open_randen"] or st["randen_3plus"]:
            # wat een koper doet: de knop Make watertight (voxel 0,5 mm, standaard) en verder met de kopie
            actief(ob)
            t0 = time.perf_counter()
            try:
                uitslag = bpy.ops.click_joints.maak_gesloten()
            except RuntimeError as fout:
                uitslag = f"fout: {str(fout).strip()[:200]}"
            nieuw = bpy.context.view_layer.objects.active
            log(f"{ob.name} MAKE WATERTIGHT: uitslag={uitslag} tijd={time.perf_counter() - t0:.1f}s "
                f"kopie={nieuw.name} {mesh_staat(nieuw)}")
            if nieuw is not ob:
                ob = nieuw
        naam = ob.name
        knie(ob)
        nek(naam)
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, naam + ".blend"))
    log("KLAAR")


main()
