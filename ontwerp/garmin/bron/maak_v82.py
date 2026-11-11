# Maakt alles van dieren v8.2 met de v8-scripts: overzicht, maten, json voor Gijs, omtrektoets en het blad.
# ebb_dieren_v82 vervangt delen_v8 en de tinten in ebb_dieren_v8, dus de v8-scripts tekenen meteen de v8.2-dieren.
# Gebruik: python3 maak_v82.py <pad naar BarlowCondensed-Medium.ttf>
import sys, os, runpy, shutil, json
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import ebb_dieren_v82  # noqa: eerst, zodat v8 de nieuwe dieren tekent
G = os.path.join(HIER, '..'); D82 = os.path.join(G, 'dieren82'); B82 = os.path.join(G, 'blad82')
os.makedirs(D82, exist_ok=True); os.makedirs(B82, exist_ok=True)

def run(script, *args):
    oud = sys.argv; sys.argv = [script] + list(args)
    try: runpy.run_path(os.path.join(HIER, script), run_name='__main__')
    finally: sys.argv = oud

import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf): run('overzicht_dieren_v8.py', os.path.join(D82, 'overzicht-v82-3x.png'), '3')
open(os.path.join(D82, 'maten-v82.txt'), 'w').write(buf.getvalue())
run('omtrek_toets_v8.py', D82)
buf = io.StringIO()
with contextlib.redirect_stdout(buf): run('exporteer_dieren_v8.py', os.path.join(G, 'ebb-dieren-v82-data.json'))
open(os.path.join(D82, 'export-v82.txt'), 'w').write(buf.getvalue())
j = json.load(open(os.path.join(G, 'ebb-dieren-v82-data.json'))); j['bron'] = 'ontwerp/garmin/bron/ebb_dieren_v82.py (op ebb_dieren_v8.py)'
json.dump(j, open(os.path.join(G, 'ebb-dieren-v82-data.json'), 'w'), indent=0)

# blad: het v8-blad schrijft naar dieren8/ en ebb-blad-v8.png; bewaar die en zet de nieuwe ernaast als v8.2
bewaar = {p: open(p, 'rb').read() for p in [os.path.join(G, 'ebb-blad-v8.png')] + [os.path.join(G, 'dieren8', n) for n in os.listdir(os.path.join(G, 'dieren8'))]}
bron = open(os.path.join(HIER, 'ebb_blad_v8.py')).read().replace('Ebb blad v8 (Mila): dieren v8 en', 'Ebb blad v8.2 (Mila): dieren v8.2 en')
oud = sys.argv; sys.argv = ['ebb_blad_v8.py', B82, sys.argv[1]]
try: exec(compile(bron, os.path.join(HIER, 'ebb_blad_v8.py'), 'exec'), {'__name__': '__main__', '__file__': os.path.join(HIER, 'ebb_blad_v8.py')})
finally: sys.argv = oud
shutil.move(os.path.join(G, 'ebb-blad-v8.png'), os.path.join(G, 'ebb-blad-v82.png'))
for n in os.listdir(B82):
    if n.startswith('ebb-v8-'): os.replace(os.path.join(B82, n), os.path.join(B82, n.replace('ebb-v8-', 'ebb-v82-')))
os.replace(os.path.join(B82, 'meting-v8.txt'), os.path.join(B82, 'meting-v82.txt'))
for p, data in bewaar.items(): open(p, 'wb').write(data)
print(open(os.path.join(D82, 'maten-v82.txt')).read()); print(open(os.path.join(D82, 'export-v82.txt')).read())
