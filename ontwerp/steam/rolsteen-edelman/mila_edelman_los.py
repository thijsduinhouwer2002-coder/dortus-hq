"""Edelman standen elk los in het midden gerenderd, zoals de pijplijn ze maakt (Mila 17 nov).
In de brede strook staat de fakkel (x 2,8) links van de rechterste figuren, dan lijkt het gezicht donkerder
dan in het spel. Dit blad zet elke stand op x 0 en plakt ze daarna naast elkaar.
<venv>/bin/python mila_edelman_los.py uitmap stand [stand ...]   -> uitmap/<stand>.png (300 x 420)"""
import sys, os, math
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen"))
import gedeeld as g
import held
import hoeden as hd

if __name__ == "__main__":
    uit = sys.argv[1]
    for st in sys.argv[2:]:
        g.leeg()
        o = held.bouw("edelman", st, plek=(0, 0, 0), draai=30)
        voor = o.get("hoed_voor", 0.0)
        a = math.radians(30)
        dx, dy = -voor * math.sin(a), -voor * math.cos(a)
        hd.bouw(10, (dx, dy, 1.6 - o.get("hoed_zak", 0.0)), schaal=0.9, kantel=0, draai=30, voorover=o.get("hoed_voorover", 0.0))
        g.camera(hoogte_midden=1.15, schaal=2.1)
        g.licht()
        g.render(os.path.join(uit, st + ".png"), 300, 420, 32, doorzichtig=True)
