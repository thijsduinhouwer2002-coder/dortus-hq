"""Gedeelde hulp voor de achtergrondtest: loggen, toetsen tellen, gewricht plaatsen en meten.

Alle maten in het log zijn in mm, ook als de scene in meters staat: u is het aantal
Blender-eenheden per mm (1 in de mm-scene, 0,001 in de meterscene)."""
import math
import os
import tempfile
import time
from importlib import import_module

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

import figuren

fouten = []


def log(tekst):
    print(f"[cj-e2e] {tekst}", flush=True)


def stap(naam, ok):
    log(f"{'OK  ' if ok else 'FOUT'} {naam}")
    if not ok:
        fouten.append(naam)


def u():
    """Blender-eenheden per mm in de huidige scene."""
    return 1.0 / (bpy.context.scene.unit_settings.scale_length * 1000.0)


def addon(module):
    """Een module van de geïnstalleerde add-on, bijvoorbeeld addon("gewricht")."""
    naam = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return import_module(f"{naam}.{module}")


def meting(ob):
    """(foute randen, volume in mm3) van de mesh van een object, in zijn eigen coördinaten."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True) / u() ** 3
    bm.free()
    return fout, vol


def delen():
    return [o for o in bpy.context.scene.objects if o.get("cj_deel") and o.visible_get()]


def gesloten_delen(label, lijst):
    stap(f"{label}: precies twee delen (gevonden {len(lijst)})", len(lijst) == 2)
    for d in lijst:
        fout, vol = meting(d)
        log(f"{label}: deel {d.name} foute_randen={fout} volume={vol:.2f}mm3 passing={d.get('cj_passing')} "
            f"wand={d.get('cj_wand_mm')}mm")
        stap(f"{label}: {d.name} gesloten", fout == 0 and vol > 0)
        toets_ring(label, d)


def toets_ring(label, d):
    """Passingkleur als ring rond de snede (punt 2 van Daan): het materiaal van cj_passing zit in een eigen
    vak; elk vlak binnen 2,9 mm van het snijvlak en elk vlak op kogel of kom heeft dat vak, en bij de arm
    het grootste deel van het oppervlak niet (het figuur houdt zijn eigen materiaal)."""
    verwacht = addon("passing").KLEUREN.get(d.get("cj_passing"))
    mats = list(d.data.materials)
    vak = next((i for i, m in enumerate(mats) if m is not None and m.name.startswith("Click Joints ")), None)
    kleur_ok = vak is not None and verwacht is not None and all(
        abs(a - b) < 1e-3 for a, b in zip(mats[vak].diffuse_color, verwacht))
    as_r = Vector(d["cj_as"]).normalized()
    p0, c, r = Vector(d["cj_snijpunt"]), Vector(d["cj_centrum"]), d["cj_kogel_r"]
    s = d.get("cj_speling_mm", 0.0) * u()
    met = binnen = binnen_met = bol = bol_met = 0
    opp = opp_met = 0.0
    for f in d.data.polygons:
        heeft = f.material_index == vak
        met += heeft
        opp += f.area
        opp_met += f.area if heeft else 0.0
        if abs((f.center - p0).dot(as_r)) <= 2.9 * u():
            binnen += 1
            binnen_met += heeft
        afst = (f.center - c).length
        if d.get("cj_soort") == "KOGEL" and min(abs(afst - r), abs(afst - r - s)) < 0.02 * r:
            bol += 1
            bol_met += heeft
    n = len(d.data.polygons)
    log(f"RING {label}: {d.name} vak={vak} {mats[vak].name if vak is not None else None} met_passing={met}/{n} "
        f"({100 * met / max(n, 1):.1f}%) ring={binnen_met}/{binnen} kogel_of_kom={bol_met}/{bol} "
        f"oppervlak_met_passing={100 * opp_met / max(opp, 1e-12):.1f}% addon_deel={d.get('cj_ring_deel')}")
    stap(f"{label}: {d.name} passingmateriaal in kleur {d.get('cj_passing')}", kleur_ok)
    if str(d.get("cj_bron", "")).startswith("arm"):  # groot figuur; bij de kleine pop is de ring bijna het hele deel
        # oppervlak in plaats van aantal: de kogel heeft veel kleine vlakjes, een grove arm weinig grote
        stap(f"{label}: {d.name} minder dan de helft van het oppervlak in passingkleur", opp_met < 0.5 * opp)
    stap(f"{label}: {d.name} alle vlakken binnen de ring in passingkleur", binnen > 0 and binnen_met == binnen)
    stap(f"{label}: {d.name} kogel of kom in passingkleur", bol_met == bol)


def toets_uit_elkaar(lijst, label="UIT ELKAAR"):
    """Opengewerkt beeld (punt 4 van Daan): deel B staat in de weergave 1,5 keer de kogeldiameter langs de as
    verschoven, de mesh en location niet; de STL van deel B is gelijk met en zonder."""
    import struct
    inst = bpy.context.scene.click_joints
    b = next(d for d in lijst if d["cj_deel"] == "B")
    bestanden = {}
    for aan in (True, False):
        inst.uit_elkaar = aan
        bpy.context.view_layer.update()
        verschuiving = (b.matrix_world.translation - b.location).dot(Vector(b["cj_as"]).normalized()) / u()
        verwacht = 1.5 * 2 * b["cj_kogel_r"] / u() if aan else 0.0
        log(f"{label} aan={aan}: deel B verschoven {verschuiving:.3f} mm langs de as (verwacht {verwacht:.3f}), "
            f"location={tuple(round(x, 4) for x in b.location)}")
        stap(f"{label} aan={aan}: verschuiving klopt", abs(verschuiving - verwacht) < 1e-3)
        toets_stl(lijst, f"STL uit_elkaar={aan}")
        with open(b["cj_stl"], "rb") as f:
            data = f.read()
        bestanden[aan] = [struct.unpack_from("<12f", data, 84 + 50 * i) for i in range((len(data) - 84) // 50)]
        stap(f"{label} aan={aan}: na export staat deel B weer zoals ingesteld",
             abs((b.matrix_world.translation - b.location).length / u() - verwacht) < 1e-3)
    m, z = bestanden[True], bestanden[False]
    verschil = max((abs(x - y) for p, q in zip(m, z) for x, y in zip(p[3:], q[3:])), default=1e9)
    log(f"{label}: STL deel B driehoeken {len(m)} en {len(z)}, grootste verschil {verschil:.6f} mm")
    stap(f"{label}: STL van deel B gelijk met en zonder opengewerkt beeld", len(m) == len(z) > 0 and verschil < 1e-4)
    inst.uit_elkaar = True


def toets_materiaal(label, d):
    """Passingkleur in de standaard Solid-weergave: elk materiaalvak heeft het materiaal van cj_passing,
    met diffuse_color gelijk aan de passingkleur."""
    verwacht = addon("passing").KLEUREN.get(d.get("cj_passing"))
    mats = [v.material for v in d.material_slots]
    kleuren = [tuple(round(c, 3) for c in m.diffuse_color) if m else None for m in mats]
    log(f"KLEUR {label}: {d.name} passing={d.get('cj_passing')} materialen={[m.name if m else None for m in mats]} "
        f"diffuse={kleuren}")
    ok = bool(mats) and verwacht is not None and all(
        m is not None and all(abs(a - b) < 1e-3 for a, b in zip(m.diffuse_color, verwacht)) for m in mats)
    stap(f"{label}: {d.name} materiaal in passingkleur {d.get('cj_passing')}", ok)


def weg(lijst):
    for o in lijst:
        me = o.data
        bpy.data.objects.remove(o)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)


def plaats(label, ob, punt, as_richting, speling=0.2, kogel=5.0, soort="KOGEL", as_bron="CURSOR"):
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron = speling, kogel, soort, as_bron
    inst.kogel_auto = False  # deze toetsen kiezen de diameter zelf (Auto staat in toetsen_auto.py)
    figuren.zet_cursor(punt, as_richting)
    figuren.maak_actief(ob)
    t0 = time.perf_counter()
    uitslag = bpy.ops.click_joints.plaats()
    duur = time.perf_counter() - t0
    lijst = delen()
    if lijst:
        stap(f"{label}: na plaatsen niets geselecteerd", not any(o.select_get() for o in bpy.context.view_layer.objects))
    solver = lijst[0].get("cj_solver") if lijst else "-"
    if solver == "MANIFOLD":
        stap(f"{label}: Manifold onder 5 s ({duur:.2f}s)", duur < 5.0)
    log(f"TIJD {label}: {duur:.2f}s solver={solver} driehoeken_bron={sum(len(p.vertices) - 2 for p in ob.data.polygons)} "
        f"uitslag={uitslag}")
    return lijst


def speling_meten(lijst, ingesteld, label="SPELING"):
    """Speling in mm van kogelpunten naar het komdeel. Geeft het gemiddelde of None."""
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    c, as_r, r = Vector(a["cj_centrum"]), Vector(a["cj_as"]), a["cj_kogel_r"]
    bm = bmesh.new()
    bm.from_mesh(b.data)
    bvh = BVHTree.FromBMesh(bm)
    bm.free()
    afst = []
    for v in a.data.vertices:
        rel = v.co - c
        if abs(rel.length - r) < 1e-3 * u() and rel.dot(as_r) > -0.4 * r:
            hit = bvh.find_nearest(v.co)
            if hit[0] is not None:
                afst.append(hit[3] / u())
    if not afst:
        stap(f"{label} {ingesteld}: kogelpunten gevonden", False)
        return None
    gem = sum(afst) / len(afst)
    afw = abs(gem - ingesteld)
    log(f"{label} ingesteld={ingesteld} gemeten_gem={gem:.4f} afwijking={afw:.4f} "
        f"max={max(afst):.4f} min={min(afst):.4f} punten={len(afst)} addon_meting={a.get('cj_speling_gemeten_mm')}")
    stap(f"{label} {ingesteld}: minstens 500 punten", len(afst) >= 500)
    stap(f"{label} {ingesteld}: gemiddelde afwijking < 0,02 mm", afw < 0.02)
    return gem


def toets_opening(lijst, label):
    """Klikopening gemeten in de mesh: tussen 0,80 en 0,90 keer de kogeldiameter, en de nek past erdoor."""
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    c, as_r, r = Vector(a["cj_centrum"]), Vector(a["cj_as"]).normalized(), a["cj_kogel_r"]

    loodrecht = as_r.orthogonal().normalized()

    def stralen(ob, z0, z1):
        """Stralen vanaf de as, loodrecht naar buiten, op 8 hoogtes en 32 richtingen: afstand tot de wand.
        (De cilinderwand heeft alleen punten aan zijn uiteinden, daarom meten met stralen.)"""
        bm = bmesh.new()
        bm.from_mesh(ob.data)
        bvh = BVHTree.FromBMesh(bm)
        bm.free()
        uit = []
        for i in range(8):
            o = c + as_r * (r * (z0 + (z1 - z0) * (i + 0.5) / 8))
            for k in range(32):
                d = Matrix.Rotation(2 * math.pi * k / 32, 3, as_r) @ loodrecht
                hit = bvh.ray_cast(o, d)
                if hit[0] is not None:
                    uit.append(hit[3] / u())
        return uit

    gat = stralen(b, -1.35, -0.8)   # tussen snijvlak en kom: alleen de opening en de buitenkant
    nek = stralen(a, -1.35, -1.05)  # onder de kogel: alleen de nek
    if not gat or not nek:
        stap(f"{label}: opening en nek gevonden", False)
        return
    opening, nek_d, kogel_d = 2 * min(gat), 2 * max(nek), 2 * r / u()
    log(f"OPENING {label}: opening={opening:.3f}mm ({opening / kogel_d:.3f} x kogel) nek={nek_d:.3f}mm "
        f"kogel={kogel_d:.3f}mm")
    stap(f"{label}: opening tussen 0,80 en 0,90 x kogeldiameter", 0.80 <= opening / kogel_d <= 0.90)
    stap(f"{label}: nek past door de opening", nek_d < opening)
    return kogel_d


def toets_stl(lijst, label="STL"):
    """Export via de add-on (altijd mm) en terug importeren zonder schaal: maat in mm gelijk binnen 0,01 mm."""
    bpy.context.scene.click_joints.exportmap = os.path.join(tempfile.gettempdir(), "cj_export") + os.sep
    bpy.ops.click_joints.exporteer()
    for d in lijst:
        pad = d.get("cj_stl", "")
        stap(f"{label} {os.path.basename(pad)} bestaat", bool(pad) and os.path.getsize(pad) > 84)
        voor = set(bpy.context.scene.objects)
        bpy.ops.wm.stl_import(filepath=pad, global_scale=1.0, use_scene_unit=False)
        nieuw = [o for o in bpy.context.scene.objects if o not in voor]
        if len(nieuw) != 1:
            stap(f"{label} {d.name}: opnieuw geïmporteerd", False)
            continue
        maat_a = [x / u() for x in d.dimensions]  # Blender-eenheden naar mm
        maat_b = nieuw[0].dimensions              # de STL zelf is in mm
        verschil = max(abs(x - y) for x, y in zip(maat_a, maat_b))
        log(f"{label} {d.name}: maat {tuple(round(x, 3) for x in maat_a)} mm, terug {tuple(round(x, 3) for x in maat_b)} "
            f"mm, verschil {verschil:.5f} mm, driehoeken {len(nieuw[0].data.polygons)}")
        stap(f"{label} {d.name}: zelfde maat binnen 0,01 mm", verschil < 0.01)
        weg(nieuw)
