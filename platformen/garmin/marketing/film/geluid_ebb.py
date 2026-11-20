#!/usr/bin/env python3
"""Zelf gemaakt geluid onder de twee Roep-filmpjes van Ebb (filmmaker-hoofdchat, 20 nov 2026).

Gebruikt geluid.py en toets.py van Chris (commercie/filmpjes/geluid/) ongewijzigd: dit script zet alleen
de tijden van deze twee filmpjes erbij. Alles met code gemaakt (sinustonen en ruis), geen nummer van een
ander, geen AI. Het beeld wordt 1 op 1 gekopieerd.

Gebruik:
  python3 geluid_ebb.py maak  <filmpje.mp4> <uit-geluid.mp4>
  python3 geluid_ebb.py toets <filmpje.mp4> <uit-geluid.mp4> <golf.png>
"""
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "..", "commercie", "filmpjes", "geluid"))
import geluid  # noqa: E402

geluid.GELUID.update({
    # ebb-roep-1.json: ebb-film.mp4 vanaf 1,5 s. In die film (commercie/ebb/maak.py, 12 fps):
    # in tot 0,7 s, overvloeien naar uit 0,7 tot 2,0, in vanaf 2,4, uit vanaf 4,1, naar onder water 5,7 tot 6,3.
    # Daarna de dieren (7,8), het veiligheidsscherm (10,4) en het menu (13,0).
    "ebb-roep-1-porthole": {
        "duur": 15.6,
        "bed": "ebb",
        "adem": [("in", 0.0, 0.7), ("uit", 0.7, 1.7), ("in", 2.4, 1.7), ("uit", 4.1, 1.6),
                 ("rust", 5.7, 2.1), ("in", 7.8, 2.6), ("uit", 10.4, 2.6), ("in", 13.0, 2.6)],
        "zoem": [0.0, 0.7, 2.4, 4.1, 5.7],
        "tik": [8.4, 9.0, 9.6, 10.4, 13.0],
    },
    # ebb-roep-2.json: onder water (0 tot 2,6), zes dieren van 0,4 s, nieuw dier (5,0), sea log (7,7),
    # veiligheidsscherm (10,0), menu (12,6). De zee ademt rustig mee als achtergrond.
    "ebb-roep-2-sea-friends": {
        "duur": 15.2,
        "bed": "ebb",
        "adem": [("rust", 0.0, 2.6), ("in", 2.6, 2.4), ("uit", 5.0, 2.7), ("in", 7.7, 2.3),
                 ("uit", 10.0, 2.6), ("in", 12.6, 2.6)],
        "zoem": [0.0, 5.0],
        "tik": [2.6, 3.0, 3.4, 3.8, 4.2, 4.6, 7.7, 10.0, 12.6],
    },
})

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("maak", "toets"):
        sys.exit(__doc__)
    soort = sys.argv.pop(1)
    if soort == "maak":
        geluid.main()
    else:
        import toets  # noqa: E402
        toets.main()
