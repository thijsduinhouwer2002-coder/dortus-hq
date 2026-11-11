# Maakt de json van dieren v8.3 en de horlogetoets (nabootsing van DierenData.mc) op 260 en 454.
# Gebruik: python3 maak_v83.py
import sys, os, runpy, io, contextlib, json
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import ebb_dieren_v83  # noqa: eerst, zodat v8 de nieuwe dieren tekent
G = os.path.join(HIER, '..'); J = os.path.join(G, 'ebb-dieren-v83-data.json')
oud = sys.argv; sys.argv = ['exporteer_dieren_v8.py', J]
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf): runpy.run_path(os.path.join(HIER, 'exporteer_dieren_v8.py'), run_name='__main__')
finally: sys.argv = oud
j = json.load(open(J)); j['bron'] = 'ontwerp/garmin/bron/ebb_dieren_v83.py (op v8.2 en v8)'
j['ogen'] = {'maat_onder_60': 'een zwart vierkantje, zijde e = max(2, (8 * maat + 50) / 100) (2 px op 260, 3 px op 454): '
                             'fillRectangle(x - e / 2, y - e / 2, e, e), kleur 0x000000, geen wit',
             'maat_vanaf_60': 'rond zwart oog fillCircle(x, y, r) met r = max(3, maat / 20), kleur 0x000000, '
                              'plus 1 wit pixel drawPoint(x - 1, y - 1) als glimp'}
json.dump(j, open(J, 'w'), indent=0)
os.makedirs(os.path.join(G, 'dieren83'), exist_ok=True)
open(os.path.join(G, 'dieren83', 'export-v83.txt'), 'w').write(buf.getvalue())
print(buf.getvalue())
