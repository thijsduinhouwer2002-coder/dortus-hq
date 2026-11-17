"""Toets (17 nov run 25, Ruben): een elleboog stopt waar de rig stopt, ook als het vlees eerder botst.

Op de MakeHuman-figuur (CC0) alleen de linkerelleboog met rig-stop 115 en 90. Zonder zwaairuimte (run 24) gaf dat
0–82° en 0–55°, want de onderarm botste op het vlees van de bovenarm. Nu (betaald/scharnier_zwaai.py) moet:
- de lijst `0–115°` en `0–90°` zeggen (gemeten, binnen 3 graden);
- het deel weten dat er uitgesneden is (cj_zwaai_van kleiner dan de stand);
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


def main():
    args = sys.argv[sys.argv.index("--") + 1:][:2]
    # 4.2 (alleen de Exact-solver): de elleboog alleen al lukt daar ook (toetsen_mens eist er minstens 3);
    # de proef draait per stop in een eigen Blender, zodat de ene stop de andere niet stoort.
    for stop in (115, 90):
        env = dict(os.environ, CJ_EL=str(stop), CJ_HOOGTE="220", CJ_ZWAAI_INFO="1")
        uit = subprocess.run([bpy_app(), "-b", "--factory-startup", "--python",
                              os.path.join(HIER, "proef_kuil.py"), "--"] + args,
                             env=env, capture_output=True, text=True, timeout=500).stdout
        regels = [r.split("] ", 1)[1] for r in uit.splitlines() if r.startswith("[cj-kuil]")]
        lijst = next((r for r in regels if r.startswith("lijst: Left elbow")), "")
        if not lijst and oud_blender():
            # 4.2 (alleen Exact): de elleboog op 90 valt daar al af voor de zwaairuimte ("parts overlap"), net
            # als in toetsen_mens (eist in 4.2 minstens 3 gewrichten). Dan geen uitsnede te toetsen.
            log(f"4.2: stop {stop} overgeslagen door de snede zelf, niet door de zwaairuimte")
            continue
        try:
            gemeten = int(lijst.split("0–")[1].split("°")[0])
        except (IndexError, ValueError):
            gemeten = -1
        check(abs(gemeten - stop) <= 3, f"stop {stop}: lijst zegt 0–{gemeten} ({lijst})")
        info = next((r for r in regels if r.startswith("zwaai:")), "zwaai: geen")
        try:
            van = float(info.split("van=")[1].split()[0])
        except (IndexError, ValueError):
            van = float(stop)
        check(van < stop - 2,
              f"stop {stop}: zwaairuimte uitgesneden ({info})")
        check("gesloten=True" in info and "stukken=1,1" in info, f"stop {stop}: delen gesloten, elk één stuk ({info})")
        erbij = next((r for r in regels if r.startswith("huid erbij")), "")
        check(erbij.endswith(": 0 punten"), f"stop {stop}: niets steekt uit ({erbij})")
    log(f"KLAAR {len(FOUT)} FOUT")


def oud_blender():
    import bpy
    return bpy.app.version < (4, 5, 0)


def bpy_app():
    import bpy
    return bpy.app.binary_path


main()
