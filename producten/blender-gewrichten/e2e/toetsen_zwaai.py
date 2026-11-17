"""Toets (17 nov run 25, Ruben): een elleboog stopt waar de rig stopt, ook als het vlees eerder botst.

Op de MakeHuman-figuur (CC0) alleen de linkerelleboog met rig-stop 115 en 90. Zonder zwaairuimte (run 24) gaf dat
0–82° en 0–55°, want de onderarm botste op het vlees van de bovenarm. Nu (betaald/scharnier_zwaai.py) moet:
- de lijst `0–115°` en `0–90°` zeggen (gemeten, binnen 3 graden);
- het deel weten dat er uitgesneden is (cj_zwaai_van staat erop);
- wat weg is bij de elleboog liggen (binnen 20 mm), en bij een mislukte uitsnede A ongewijzigd terugkomen;
- beide delen gesloten en elk één stuk zijn, en niets buiten de oude huid steken (> 0,3 mm).

Gebruik: blender -b --factory-startup --python e2e/toetsen_zwaai.py -- <betaalde zip> <base.obj>
Uitslag: regels [cj-zwaai-toets], laatste regel "KLAAR n FOUT".
"""
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
FOUT = []


def log(t):
    print(f"[cj-zwaai-toets] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def proef(stop, args, extra=None):
    """Draait proef_kuil.py voor één stop in een eigen Blender; geeft (regels, hele uitvoer) of (None, fout)."""
    env = dict(os.environ, CJ_EL=str(stop), CJ_HOOGTE="220", CJ_ZWAAI_INFO="1", **(extra or {}))
    try:
        uit = subprocess.run([bpy_app(), "-b", "--factory-startup", "--python",
                              os.path.join(HIER, "proef_kuil.py"), "--"] + args,
                             env=env, capture_output=True, text=True, timeout=500)
    except subprocess.TimeoutExpired:
        return None, "timeout na 500 s"
    alles = uit.stdout + uit.stderr
    return [r.split("] ", 1)[1] for r in uit.stdout.splitlines() if r.startswith("[cj-kuil]")], alles


def veld(info, naam, standaard=None):
    try:
        return info.split(f"{naam}=")[1].split()[0]
    except IndexError:
        return standaard


def main():
    args = sys.argv[sys.argv.index("--") + 1:][:2]
    getoetst, wees_normaal = 0, None
    for stop in (115, 90):
        regels, alles = proef(stop, args)
        if regels is None:
            check(False, f"stop {stop}: {alles}")
            continue
        lijst = next((r for r in regels if r.startswith("lijst: Left elbow")), "")
        if not lijst and oud_blender() and "KLAAR" in regels and "overlap before they move" in alles:
            # 4.2 (alleen Exact): de elleboog op 90 valt daar al af voor de zwaairuimte ("parts overlap"), net
            # als in toetsen_mens (eist in 4.2 minstens 3 gewrichten). Dan geen uitsnede te toetsen.
            log(f"4.2: stop {stop} overgeslagen door de snede zelf, niet door de zwaairuimte")
            continue
        getoetst += 1
        try:
            gemeten = int(lijst.split("0–")[1].split("°")[0])
        except (IndexError, ValueError):
            gemeten = -1
        check(abs(gemeten - stop) <= 3, f"stop {stop}: lijst zegt 0–{gemeten} ({lijst})")
        info = next((r for r in regels if r.startswith("zwaai:")), "zwaai: geen")
        check(veld(info, "van", "None") != "None", f"stop {stop}: zwaairuimte uitgesneden ({info})")
        check("gesloten=True" in info and "stukken=1,1" in info, f"stop {stop}: delen gesloten, elk één stuk ({info})")
        erbij = next((r for r in regels if r.startswith("huid erbij")), "")
        check(erbij.endswith(": 0 punten"), f"stop {stop}: niets steekt uit ({erbij})")
        # Controleur run 25, punt 11: wat weg is, ligt bij het gewricht (de uitsnede blijft binnen 1,5 x de
        # meetbol, op deze figuur ±18 mm).
        diep = next((r for r in regels if r.startswith("diepste punt")), "")
        try:
            afst = sum(float(c) ** 2 for c in diep.split("(")[1].split(")")[0].split(",")) ** 0.5
        except (IndexError, ValueError):
            afst = 99.0
        check(afst < 20.0, f"stop {stop}: diepste weggesneden punt {afst:.1f} mm van de elleboog")
        wees_normaal = veld(info, "wees")
    check(getoetst >= 1, f"minstens één stop echt getoetst ({getoetst})")
    # Controleur run 25, punt 12: mislukt de controle na de uitsnede, dan komt A ongewijzigd terug (bereik
    # zoals zonder uitsnede, geen cj_zwaai_van) en blijven er niet meer losse meshes achter dan normaal.
    regels, alles = proef(115, args, {"CJ_ZWAAI_MIS": "1"})
    if regels is None:
        check(False, f"terugzetten: {alles}")
    elif any(r.startswith("lijst: Left elbow") for r in regels):
        lijst = next(r for r in regels if r.startswith("lijst: Left elbow"))
        info = next((r for r in regels if r.startswith("zwaai:")), "zwaai: geen")
        try:
            gemeten = int(lijst.split("0–")[1].split("°")[0])
        except (IndexError, ValueError):
            gemeten = -1
        check(0 < gemeten < 113, f"terugzetten: bereik zonder uitsnede ({lijst})")
        check(veld(info, "van", "None") == "None", f"terugzetten: geen cj_zwaai_van ({info})")
        check("gesloten=True" in info, f"terugzetten: delen gesloten ({info})")
        check(wees_normaal is None or veld(info, "wees") == wees_normaal,
              f"terugzetten: losse meshes {veld(info, 'wees')}, normaal {wees_normaal}")
    else:
        check(oud_blender(), "terugzetten: elleboog niet geplaatst")
    log(f"KLAAR {len(FOUT)} FOUT")


def oud_blender():
    import bpy
    return bpy.app.version < (4, 5, 0)


def bpy_app():
    import bpy
    return bpy.app.binary_path


main()
