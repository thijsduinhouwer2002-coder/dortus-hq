"""Sanne 17 nov ±07:50 UTC (Iris keuring 19 punt 2): waarom hol 10 in de duurtest van main later komt dan in Brams .exe-run,
en wanneer hol 10 tot 12 komen met de oude en de nieuwe drempels. Alleen echte runs, geen sim (de sim zei hol 12 op 58 min,
beide echte runs zijn trager). Faam = aantal gevangen helden (kern/afloop.gd: +1 per val), dus tempo = vangsten per minuut.
Draai: python3 -I platformen/steam/data/hol-tempo/tempo.py"""
# hol-niveau: tijd in s. main = duurtest 44030107525 (main b935c75, editor, zaad 1794860558), hol.log op tak schermen
# steam-hol-duur/main-zaad-1794860558-1920x1080/; exe = Brams run 44018723753 (e6ad9be plus meetcode, .exe, zelfde zaad).
DREMPEL = [0, 3, 5, 7, 12, 17, 25, 31, 39, 53, 69, 88]
RUNS = {
    "main editor": {2: 79.1, 3: 182.1, 4: 296.3, 5: 561.0, 6: 876.9, 7: 1322.8, 8: 1591.7, 9: 1917.1, 10: 2964.3},
    "exe Bram":    {2: 79, 4: 307, 6: 665, 8: 1321, 9: 1770, 10: 2348},
}
NIEUW = {10: 49, 11: 60, 12: 72}
for naam, r in RUNS.items():
    t9 = r[9] / 60
    # tempo vanaf hol 6 tot het laatste gemeten niveau: lang genoeg om de toevalsdip (30 tot 40 min in main) uit te middelen
    laatst = max(r)
    tempo = (DREMPEL[laatst - 1] - DREMPEL[5]) / ((r[laatst] - r[6]) / 60)
    print("%-12s hol 9 op %.1f min, vangsten per min vanaf hol 6: %.2f" % (naam, t9, tempo))
    for niv in (10, 11, 12):
        oud = t9 + (DREMPEL[niv - 1] - 39) / tempo
        nw = t9 + (NIEUW[niv] - 39) / tempo
        echt = " (echt %.1f)" % (r[niv] / 60) if niv in r else ""
        print("   hol %d: oude drempel %d -> %.1f min%s, nieuwe drempel %d -> %.1f min" % (niv, DREMPEL[niv - 1], oud, echt, NIEUW[niv], nw))
