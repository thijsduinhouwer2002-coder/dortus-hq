"""Wat telt als echte driehoek, en welke driehoeken samen één kans zijn. Gebruikt door rapport.py.

Echt: zie volgen.py en rapport.py (bevestigd na MIN_DUUR seconden met MIN_DIEPTE diepte, minstens MIN_WINST winst,
niet verdacht). Samen één kans (keuring H3): zelfde beurs, bevestigd binnen SAMEN_S seconden van elkaar, en minstens
één gedeeld paar dat geen paar van twee hoofdmunten is; geen ketting (een driehoek hoort alleen bij een groep als
hij met elk lid dezelfde kans is).
"""
import collections
import datetime as dt

MIN_DIEPTE = 100
MIN_DUUR = 3
MIN_WINST = 0.05
INLEGGEN = (100, 150, 200, 2000, 5000)
KLEIN = (100, 150, 200)
STAND_S = 300
VERGUND = {"MiCA", "MiCA-dochter"}
SOORTEN = (("alle", "Alle beurzen"), ("vergund", "MiCA (ook via EU-dochter)"), ("grijs", "Grijs"))


def soort(r):
    return "vergund" if r.get("status") in VERGUND else "grijs"


def van(rs, s):
    return rs if s == "alle" else [r for r in rs if soort(r) == s]


def na(r, scen="hoog"):
    """De meting die bevestigt dat hij bleef staan (na MIN_DUUR seconden, met MIN_DIEPTE diepte), of None."""
    return (r.get(scen) or {}).get("na_3s")


def echt(r, scen="hoog"):
    n = na(r, scen)
    return bool(n) and n.get("winst_eur", 0) >= MIN_WINST and n.get("diepte_eur", 0) >= MIN_DIEPTE \
        and not r.get("verdacht")


def wb(r, inleg):
    return (na(r) or {}).get("winst_bij", {}).get(str(inleg), 0) or 0


HOOFD = {"EUR", "USD", "USDT", "USDC", "BTC", "ETH"}
SAMEN_S = 5          # "tegelijk": bevestigd (na 3 s) binnen 5 seconden van elkaar, ongeveer één meetronde
VANAF = "2026-11-19T16:07"   # regels van eerder hebben geen meting na 3 s en tellen nooit als echt


def boekstukken(r):
    """De paren van een driehoek als munt-paren, zonder paren van twee hoofdmunten (zoals BTC/EUR of BTCUSDT):
    die zijn zo diep dat twee driehoeken die alleen zo'n paar delen, elkaar het boek niet afpakken."""
    m = r["driehoek"].split(">")[:3]
    stukken = {frozenset((m[i], m[(i + 1) % 3])) for i in range(3)}
    return {p for p in stukken if not p <= HOOFD}


def _tijd(r):
    t = (na(r) or {}).get("t", "")
    try:
        return dt.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ").timestamp()
    except ValueError:
        return None


def zelfde_kans(a, b):
    """Willen a en b hetzelfde stukje boek? Zelfde beurs, bevestigd binnen SAMEN_S seconden van elkaar, en minstens
    één gedeeld paar dat geen paar van twee hoofdmunten is."""
    ta, tb = _tijd(a), _tijd(b)
    return a["beurs"] == b["beurs"] and ta is not None and tb is not None and abs(ta - tb) <= SAMEN_S \
        and bool(boekstukken(a) & boekstukken(b))


def kansen(echte):
    """Groepeer driehoeken die dezelfde kans zijn, zonder doorketenen: de beste (hoogste winst na 3 s) begint een
    groep, en een driehoek komt er alleen bij als hij met **elk** lid van die groep dezelfde kans is. Zo worden A en
    C nooit samen één kans omdat ze allebei iets met B delen. Geeft een lijst groepen (elk een lijst driehoeken)."""
    groepen = []
    for r in sorted(echte, key=lambda r: -na(r)["winst_eur"]):
        for g in groepen:
            if all(zelfde_kans(r, x) for x in g):
                g.append(r)
                break
        else:
            groepen.append([r])
    return groepen


def los(echte):
    """Elke driehoek een eigen kans (bovengrens: soms willen er twee hetzelfde stukje boek)."""
    return [[r] for r in echte]


def opgeteld(groepen, inleg):
    """Winst bij een inleg, opgeteld over de groepen (per groep de beste), en per beurs."""
    per_b = collections.Counter()
    for g in groepen:
        r = beste(g, inleg)
        per_b[r["beurs"]] += wb(r, inleg)
    return sum(per_b.values()), per_b


def beste(groep, inleg=None):
    """De beste driehoek van een groep: bij een inleg de hoogste winst bij die inleg, anders de hoogste winst."""
    return max(groep, key=lambda r: wb(r, inleg) if inleg else na(r)["winst_eur"])
