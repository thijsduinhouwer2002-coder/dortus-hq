# Winkelbeelden Ebb Calm (Gijs, run 88, 13 nov 2026): vijf kaarten van 800x800 uit de echte schermen van Ebb Calm
# (plaatjesjob van garmin-calm.yml, fenix 8 47 mm). Tekent niets zelf: gebruikt Mila's winkel_v4.py (ontwerp/garmin/bron
# op main), dezelfde kaart als bij Ebb. Belooft alleen wat in Ebb Calm zit: Calm 4-7-8, trillen, opslaan, gratis.
# Geen inhoudrondes, geen dieren om te verzamelen, geen medische claims.
#   python3 maak_winkel_calm.py <ontwerp/garmin/bron> <map met calm-<naam>-fenix847mm.png> <uitmap>
import sys, os
bron, m, uit = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, bron)
import winkel_v4
KAARTEN = [
    ('calm-in', '1-breathe-in.png', 'Breathe in. The sea rises.', 'sea rises', 'Calm 4-7-8: in 4, hold 7, out 8. The water shows the way.'),
    ('calmcheck', '2-eyes-closed.png', 'Sit down. Close your eyes.', 'Close your eyes', 'A buzz tells you each phase. No sound, no screen needed.'),
    ('einde-4min', '3-calm-done.png', 'A few calm minutes.', 'calm', 'Save it to Garmin Connect as breathwork, with heart rate.'),
    ('pauze', '4-pause.png', 'Pause. The sea waits.', 'waits', 'Resume, save or discard. Any time.'),
    ('menu', '5-free.png', 'Free. One button.', 'Free', 'No account, no ads. Ebb Calm collects nothing.')]
os.makedirs(uit, exist_ok=True)
for naam, uitnaam, kop, geel, onder in KAARTEN:
    p = os.path.join(m, 'calm-%s-fenix847mm.png' % naam)
    if not os.path.exists(p):
        sys.exit('ONTBREEKT: ' + p)
    winkel_v4.kaart(p, kop, geel, onder, os.path.join(uit, uitnaam))
for f in sorted(os.listdir(uit)):
    if f.endswith('.png'):
        g = os.path.getsize(os.path.join(uit, f))
        print(f, g, 'bytes', '(boven 150 KB!)' if g > 150000 and not f.startswith('icoon') else '')
