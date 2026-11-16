# Kit uitbreiden met kleine MIP-horloges (Mila, 16 nov 2026), vraag van Gijs:
# Forerunner 55 (208 px) en Forerunner 245 (240 px). Zelfde regels als gloop_spel_kit.py, bestaande mappen blijven.
#   python3 gloop_spel_kit_klein.py <rendermap> <kitmap>
import sys, os, json
R, KIT = sys.argv[1], sys.argv[2]
sys.argv = ['x', R, KIT]
import gloop_spel_v2 as v2
import gloop_spel_kit as k
info = json.load(open(os.path.join(KIT, 'kit.json')))
for W in (208, 240):
    v2.MIP = True
    stuks, i = k.kit(W, True)
    info[f'{W}-mip'] = i
    print(W, {n: s for n, s in i.items() if n.startswith('gloop-rust') or n.startswith('hoed-04')})
json.dump(info, open(os.path.join(KIT, 'kit.json'), 'w'), indent=1)
