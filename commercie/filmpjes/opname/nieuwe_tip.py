"""Nieuwe tip-opname klaarzetten (Olaf, 24 nov 2026): workflow plus een kaal opnamescript op de gedeelde hulpcode.

    python3 commercie/filmpjes/opname/nieuwe_tip.py 13 tip-bed "tip-reeks 11: ..." k_mooi k_menu k_klaar

Maakt `.github/workflows/regisseur-13.yml` (afgeleid van regisseur-12.yml, met blender_opname.py in de sha) en
`commercie/filmpjes/regisseur-13/tip_opname.py` (kaal verloop met de opgegeven delen). Bestaat een van de twee al, dan
stopt het. Pas zelf de stap "Eindbeeld uit de opname" aan (die snijdt het eindbeeld van regisseur-12 uit), of haal
hem weg. Een wijziging in blender_opname.py start geen nieuwe opname vanzelf; bij de volgende push in je map wel. De scène-json (`<naam>.json`) en de voorleestekst schrijf je zelf, zoals altijd.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
BRON = "12"


def workflow(n, naam, titel, delen):
    s = open(os.path.join(ROOT, f".github/workflows/regisseur-{BRON}.yml")).read()
    kop_eind = s.index("\non:")
    kop = (f'name: "Regisseur {n} ({titel})"\n\n# Gemaakt met commercie/filmpjes/opname/nieuwe_tip.py uit regisseur-{BRON}.yml. '
         f'Opname commercie/filmpjes/regisseur-{n}/tip_opname.py op de gedeelde hulpcode\n# (opname/blender_opname.py). '
         f'ElevenLabs-mp3 ({naam}-elevenlabs.mp3) wordt vanzelf gebruikt, anders Kokoro. Niets geplaatst.\n')
    s = s[kop_eind:]
    s = s.replace(f"regisseur-{BRON}", f"regisseur-{n}").replace(f"Regisseur {BRON}", f"Regisseur {n}")
    s = s.replace(f"cj_tip{BRON}", f"cj_tip{n}").replace("tip-export", naam)
    s = s.replace(f"nu=$(sha256sum commercie/filmpjes/regisseur-{n}/tip_opname.py | cut -c1-64)",
                  f"nu=$(cat commercie/filmpjes/regisseur-{n}/tip_opname.py commercie/filmpjes/opname/blender_opname.py"
                  f" | sha256sum | cut -c1-64)")
    s = re.sub(r"for d in [a-z_ ]+; do grep -q \"KORT OK", "for d in " + " ".join(delen) + '; do grep -q "KORT OK', s)
    s = re.sub(r'--title "Regisseur %s \([^"]*\)"' % n, f'--title "Regisseur {n} ({titel})"', s)
    s = re.sub(r'echo "Regisseur %s: [^"]*"' % n, f'echo "Regisseur {n}: {titel}. Concepten: marketing/wachtrij/. '
               f'Niets geplaatst."', s)
    assert "blender_opname.py | sha256sum" in s, "sha-regel niet gevonden in de bron-workflow"
    assert f"regisseur-{BRON}" not in s
    return kop + s


def script(n, naam, titel, delen):
    stukken = "\n".join(f'    deel("{d}")\n    yield from houd(30)      # TODO\n    log("KORT OK {d}")\n' for d in delen)
    return f'''"""Opname {naam} (regisseur-{n}): {titel}. Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, geen add-on.
Hulpcode: ../opname/blender_opname.py (LEESMIJ daar).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python tip_opname.py -- <uitmap>"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402

zet_naam("tip{n}")
MAP = "/tmp/tip{n}"


def verloop():
    a = zet_scherm()
    os.makedirs(MAP, exist_ok=True)
    yield 1.0
    film["metingen"]["weergave"] = regio_rect(a)
    balk = bovenbalk()
    film["metingen"]["bovenbalk"] = balk
    # voorbeeld menupad: ok = yield from menu_pad(balk, ["File", "Export", "STL"], "menu"); bij False je vangnet
    yield from muis_naar(*zachte_muis_in_beeld(), 4)

{stukken}
    deel("eind")
    einde()


start(verloop)
'''


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    n, naam, titel, delen = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    wf = os.path.join(ROOT, f".github/workflows/regisseur-{n}.yml")
    sc = os.path.join(ROOT, f"commercie/filmpjes/regisseur-{n}/tip_opname.py")
    for p in (wf, sc):
        if os.path.exists(p):
            sys.exit(f"bestaat al: {p}")
    w, s = workflow(n, naam, titel, delen), script(n, naam, titel, delen)
    os.makedirs(os.path.dirname(sc), exist_ok=True)
    open(wf, "w").write(w)
    open(sc, "w").write(s)
    print(f"klaar: {wf}\n       {sc}\nnog zelf: {naam}.json (scènes), {naam}-stem.txt, het verloop in tip_opname.py")


if __name__ == "__main__":
    main()
