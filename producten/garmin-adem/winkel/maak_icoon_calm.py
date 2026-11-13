# Icoon Ebb Calm, voorstel van Gijs (run 88, 13 nov 2026) tot Mila een eigen icoon maakt. Tekent niets zelf: gebruikt
# Mila's icoon_v3.py (ontwerp/garmin/bron op main) met de vis (dier 0, het enige dier van Ebb Calm) in plaats van de
# walvis, en de paarse ochtendlucht van het ademscherm in plaats van de nacht. Zo hoort het bij Ebb (zelfde
# patrijspoort) en is het er naast Ebb toch niet mee te verwarren.
#   python3 maak_icoon_calm.py <ontwerp/garmin/bron> winkel <uit.png> [maat=500]
#   python3 maak_icoon_calm.py <ontwerp/garmin/bron> start <uit.png> <maat>
import sys
bron = sys.argv[1]
sys.path.insert(0, bron)
import icoon_v3
icoon_v3.WALVIS = 0
icoon_v3.NACHT = (85, 0, 170)
if sys.argv[2] == 'winkel':
    icoon_v3.winkel(sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 500)
else:
    icoon_v3.start(sys.argv[3], int(sys.argv[4]))
