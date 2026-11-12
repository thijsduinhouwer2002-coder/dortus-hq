# Winkelbeelden Ebb v4.1 (Gijs, run 58, 12 nov 2026): poster en kaart 1 met het echte ademscherm in plaats van
# het inhoudscherm (besluit 11 nov 23:25: kop "Breathe. Make sea friends.", geen timer van het inhouden op de poster).
# Tekent niets zelf: gebruikt Mila's poster_v4.py en winkel_v4.py (ontwerp/garmin/bron op main) met een andere kop
# en een andere echte opname (fenix 8 47 mm, scène ademen-in, plaatjesrun 43167720322, code 9f66378).
#   python3 maak_winkel_v41.py <ontwerp/garmin/bron> <ademen-in-fenix847mm.png> <uitmap>
import sys, os
bron, sim, uit = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, bron)
import winkel_v4
winkel_v4.kaart(sim, 'Breathe in. The sea rises.', 'sea rises', 'Deep breaths at a steady pace, drawn as water.', os.path.join(uit, '1-breathe.png'))
code = open(os.path.join(bron, 'poster_v4.py')).read()
assert "'Hold your breath.'" in code
code = code.replace("'Hold your breath.'", "'Breathe.'").replace('os.path.abspath(__file__)', repr(os.path.join(os.path.abspath(bron), 'poster_v4.py')))
ruimte = {'__name__': 'poster_v41'}
exec(compile(code, 'poster_v4.py', 'exec'), ruimte)
ruimte['poster'](sim, os.path.join(uit, '0-poster-v41.png'))
# Kaart 2, 3 en 5 opnieuw uit de opnames van nu (het dier op het eindscherm is in de app kleiner dan op de kaarten v4);
# koppen ongewijzigd. Kaart 4 (sea complete) is pixel voor pixel gelijk gebleven en blijft staan.
#   vierde argument: map met fenix847mm-scene34.png, -scene4.png en -scene33.png van dezelfde run
if len(sys.argv) > 4:
    m = sys.argv[4]
    for k, naam, t, g, o in [
        (34, '2-new-friend.png', 'Come back. Meet a crab.', 'crab', 'New sea friends for sessions and weeks in a row.'),
        (4, '3-sea-log.png', 'Fill your sea log.', 'sea log', '24 sea friends to find. Who is that shadow?'),
        (33, '5-sea-cucumber.png', 'Back? Meet a bonus friend.', 'bonus friend', 'The sea cucumber greets you after a break.')]:
        winkel_v4.kaart(os.path.join(m, 'fenix847mm-scene%d.png' % k), t, g, o, os.path.join(uit, naam))
