"""Bram 15 nov 2026: delen van de workflow in delen (steam-hol-modellen.yml) bij elkaar brengen.

  python3 samen.py pak <naam> <map>    na het renderen van één sprite: <naam>.png, .png.import, de kijkbeelden
                                       en de regel uit godot/kunst/3d/sprites.json (<naam>.regel.json) in <map>
  python3 samen.py zet <map> ...       alles uit die mappen terug in godot/kunst/3d/ en de regels in sprites.json

Waarom: elke sprite rendert in een eigen job tegelijk met de rest (was alles na elkaar, ±28 min voor alles).
Elke job ziet alleen zijn eigen blad; deze stap zet ze weer in één map en één sprites.json.
"""
import glob, json, os, shutil, sys

HIER = os.path.dirname(os.path.abspath(__file__))
DOEL = os.path.join(os.path.dirname(HIER), "godot", "kunst", "3d")
UIT = os.path.join(HIER, "uit")
INDEX = os.path.join(DOEL, "sprites.json")


def lees_index():
    return json.load(open(INDEX)) if os.path.exists(INDEX) else {}


def pak(naam, map_):
    index = lees_index()
    if naam not in index:
        raise SystemExit(f"FOUT: {naam} staat niet in {INDEX}")
    os.makedirs(map_, exist_ok=True)
    for f in (f"{naam}.png", f"{naam}.png.import"):
        shutil.copy2(os.path.join(DOEL, f), os.path.join(map_, f))
    with open(os.path.join(map_, f"{naam}.regel.json"), "w") as f:
        json.dump({naam: index[naam]}, f, indent=1, sort_keys=True)
    for k in glob.glob(os.path.join(UIT, f"{naam}*-kijk.png")):
        shutil.copy2(k, os.path.join(map_, "kijk-" + os.path.basename(k)))
    print(f"{naam}: gepakt in {map_}")


def zet(mappen):
    index = lees_index()
    namen = []
    for m in mappen:
        for r in sorted(glob.glob(os.path.join(m, "*.regel.json"))):
            regel = json.load(open(r))
            for naam, waarde in regel.items():
                for f in (f"{naam}.png", f"{naam}.png.import"):
                    bron = os.path.join(m, f)
                    if not os.path.exists(bron):
                        raise SystemExit(f"FOUT: {bron} ontbreekt naast {r}")
                    shutil.copy2(bron, os.path.join(DOEL, f))
                index[naam] = waarde
                namen.append(naam)
        os.makedirs(UIT, exist_ok=True)
        for k in glob.glob(os.path.join(m, "kijk-*")):
            shutil.copy2(k, os.path.join(UIT, os.path.basename(k)[5:]))
    with open(INDEX, "w") as f:
        json.dump(index, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"gezet: {', '.join(namen) or 'niets'}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["pak"] and len(sys.argv) == 4:
        pak(sys.argv[2], sys.argv[3])
    elif sys.argv[1:2] == ["zet"] and len(sys.argv) >= 3:
        zet(sys.argv[2:])
    else:
        raise SystemExit(__doc__)
