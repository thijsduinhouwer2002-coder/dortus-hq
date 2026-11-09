"""Toets van de sleuf bij een taps lid (controleur punt 2), aangeroepen vanuit toetsen_neus_kort.py.

Staaf 10 mm (figuren.taps_staaf) die vanaf H naar deel A toe taps toeloopt langs de buigkant, zijvlak 20 graden
van de lidas, uiteinde 12 mm onder H. Vroeger telde een straal vlak bij de rand die het schuine zijvlak al op
±0,7 mm onder H raakte als onderkant, dus Tight. Nu telt een vlak buiten het midden alleen als het minstens 10
graden verder naar onder kijkt dan het zijvlak bij H; bij een taps lid is dat niet zo. Eigen rekensom: diepte
in het midden 12, t = 5 - (5/3 - 0,1) - 0,2 = 3,233, L = min(0,65 x 10, 12 - 3,233) = 6,5, klikdiepte 0,25,
rek 1,5 x 3,233 x 0,25 / 6,5^2 = 2,870 procent (zelfde als de rechte staaf). Deel A één stuk, A en B gesloten."""
import bpy
from mathutils import Vector

import figuren
from hulp_neus import TOL_MM, eilanden


def toets(stap, cursor, eig, neus, gesloten):
    straal, onder, hoek, s = 5.0, 12.0, 20.0, 0.2
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    lid = figuren.taps_staaf("taps", straal, onder, hoek)
    figuren.maak_actief(lid)
    # H = wereld-Y, buigkant = wereld-Z (daar loopt het lid taps), lidas = wereld-X (deel A naar -X).
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    u = eig.eenheid_per_mm(bpy.context.scene)
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        uitslag = f"fout: {fout}"
    a, b = bpy.data.objects.get("taps_A"), bpy.data.objects.get("taps_B")
    tw = straal / 3 - s / 2
    t = straal - tw - s
    lip_eigen = min(0.65 * 2 * straal, onder - max(t, 0.8))
    k_eigen = min(neus.H_MM, 0.03 * lip_eigen ** 2 / (1.5 * t))
    rek_eigen = 1.5 * t * k_eigen / lip_eigen ** 2
    if not (a and b):
        print(f"[cj-betaald] METING taps lid: {uitslag}")
        stap("taps lid (zijvlak 20 graden): scharnier geplaatst, geen Tight", False, str(uitslag))
        return
    diepte = float(b.get("cj_zaag_diepte", -1)) / u
    lip, klik, rek = float(b.get("cj_lip", -1)) / u, float(b.get("cj_neus_klik", -1)) / u, float(b.get("cj_rek", -1))
    ga, gb = gesloten.is_gesloten(a), gesloten.is_gesloten(b)
    print(f"[cj-betaald] METING taps lid (20 graden): diepte {diepte:.3f} mm, L {lip:.3f} (eigen {lip_eigen:.3f}), "
          f"klikdiepte {klik:.4f} (eigen {k_eigen:.4f}), rek {rek * 100:.3f} procent (eigen {rek_eigen * 100:.3f}), "
          f"delen A {eilanden(a)}, open randen A {ga[1]} B {gb[1]}")
    stap("taps lid (zijvlak 20 graden): scharnier geplaatst, geen Tight", uitslag == {"FINISHED"}, str(uitslag))
    stap("taps lid: diepte in het midden (12) en L, klikdiepte en rek gelijk aan de eigen rekensom",
         abs(diepte - onder) <= TOL_MM and abs(lip - lip_eigen) <= TOL_MM and abs(klik - k_eigen) <= TOL_MM
         and abs(rek - rek_eigen) <= 1e-4, f"diepte {diepte:.3f} L {lip:.3f} k {klik:.4f} rek {rek:.5f}")
    stap("taps lid: deel A één stuk, A en B gesloten", eilanden(a) == 1 and ga[0] and gb[0],
         f"{eilanden(a)} stuk, A {ga[1]} B {gb[1]}")
