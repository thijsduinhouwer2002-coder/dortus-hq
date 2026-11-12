# Winkelbeelden Ebb v5 (Gijs, run 63, 12 nov 2026; nummer 5 van besluit Thijs 11:50): poster en vijf kaarten uit de
# echte schermen met de werelden in de ademsessie. Tekent niets zelf: gebruikt Mila's poster_v4.py en winkel_v4.py
# (ontwerp/garmin/bron op main) met de opnames van de fenix 8 47 mm uit de plaatjesrun (map namen/).
# Belooft nergens dat elk dier een eigen wereld heeft; geen timer van het inhouden op de poster (besluit 11 nov 23:25).
#   python3 maak_winkel_v5.py <ontwerp/garmin/bron> <map met de beelden op naam> <uitmap>
import sys, os
bron, m, uit = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, bron)
import winkel_v4
H = 'fenix847mm'
def beeld(naam):
    p = os.path.join(m, '%s-%s.png' % (naam, H))
    if not os.path.exists(p):
        sys.exit('ONTBREEKT: ' + p)
    return p
KAARTEN = [
    ('sessie-krab-in-dag', '1-breathe.png', 'Breathe in. The sea rises.', 'sea rises', 'Deep breaths at a steady pace, with your sea friend.'),
    ('sessie-schild-hold-dag', '2-hold.png', 'Hold. Go under water.', 'under water', 'Hold only while it feels easy. Press START to breathe.'),
    ('calm-einde-krab', '3-new-friend.png', 'Come back. Meet a crab.', 'crab', 'New sea friends for sessions and weeks in a row.'),
    ('sealog-1', '4-sea-log.png', 'Fill your sea log.', 'sea log', '24 sea friends to find. Who is that shadow?'),
    ('einde-sea-complete', '5-sea-complete.png', 'Find all 24.', 'all 24', 'Your sea is complete. Your weeks keep counting.')]
for naam, uitnaam, kop, geel, onder in KAARTEN:
    winkel_v4.kaart(beeld(naam), kop, geel, onder, os.path.join(uit, uitnaam))
code = open(os.path.join(bron, 'poster_v4.py')).read()
assert "'Hold your breath.'" in code
code = code.replace("'Hold your breath.'", "'Breathe.'").replace('os.path.abspath(__file__)', repr(os.path.join(os.path.abspath(bron), 'poster_v4.py')))
ruimte = {'__name__': 'poster_v5'}
exec(compile(code, 'poster_v4.py', 'exec'), ruimte)
ruimte['poster'](beeld('sessie-krab-in-dag'), os.path.join(uit, '0-poster-v5.png'))
for f in sorted(os.listdir(uit)):
    if f.endswith('.png'):
        print(f, os.path.getsize(os.path.join(uit, f)), 'bytes', '(boven 150 KB!)' if os.path.getsize(os.path.join(uit, f)) > 150000 and not f.startswith('0-') else '')
