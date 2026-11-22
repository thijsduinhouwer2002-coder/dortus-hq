"""Een driehoek volgen van de eerste meting met winst tot hij weg is, en er één regel van maken.

"Bevestigd" (keuring moet 1): op twee metingen die minstens MIN_DUUR seconden uit elkaar liggen, en op alle
metingen daartussen, lag er minstens MIN_DIEPTE euro met winst. De winst die telt, is die van de latere meting:
wat er na MIN_DUUR seconden nog stond (wij meten elke paar seconden, dus dat is op zijn best wat wij kunnen pakken).
Rapport.py gebruikt dezelfde grenzen (het kan dit bestand niet importeren, het draait met python3 -I).
"""
import statistics
import time

MIN_DIEPTE = 100
MIN_DUUR = 3
VERDACHT = 0.05      # meer dan 5% winst per rondje: bijna altijd een dode markt of een foute ticker
SCENARIO = ("laag", "hoog")


def iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def nieuw(meta, t):
    g = dict(meta, begin=t, eind=t, checks=0, winsten=[])
    for s in SCENARIO:
        g[s] = None
    return g


def _kort(r, t):
    return {"t": t, "winst_eur": r["winst_eur"], "diepte_eur": r["diepte_eur"], "pct": r["pct"],
            "best_eur": r["best_eur"], "min_inleg_eur": r["min_inleg_eur"], "winst_bij": r["winst_bij"]}


def meting(g, uitslag, t):
    """uitslag = {"laag": curve of None, "hoog": curve of None}. Een scenario zonder winst breekt zijn reeks."""
    g["eind"] = t
    g["checks"] += 1
    for s in SCENARIO:
        r = uitslag.get(s)
        o = g[s]
        if r is None:
            if o is not None:
                o["reeks"].append({"t": t, "diepte_eur": 0, "winst_eur": 0})
            continue
        if o is None:
            o = g[s] = {"begin": t, "eind": t, "checks": 0, "reeks": [], "beste": None}
        o["eind"] = t
        o["checks"] += 1
        k = _kort(r, t)
        o["reeks"].append(k)
        if o["beste"] is None or k["winst_eur"] > o["beste"]["winst_eur"]:
            o["beste"] = k
        if s == "hoog":
            g["winsten"].append(r["winst_eur"])


def bevestigd(reeks, min_diepte=MIN_DIEPTE, min_duur=MIN_DUUR):
    """De eerste meting die min_duur seconden na het begin van een ononderbroken reeks metingen met elk minstens
    min_diepte euro diepte ligt, of None. Geeft (die meting, hoe lang de langste reeks duurde)."""
    begin, gevonden, langst = None, None, 0.0
    for m in reeks:
        if m["diepte_eur"] >= min_diepte and m["winst_eur"] > 0:
            if begin is None:
                begin = m["t"]
            langst = max(langst, m["t"] - begin)
            if gevonden is None and m["t"] - begin >= min_duur:
                gevonden = m
        else:
            begin = None
    return gevonden, langst


def regel(g, reden):
    """Maak van een gesloten driehoek één regel voor driehoeken.jsonl."""
    w = g.pop("winsten")
    for s in SCENARIO:
        o = g[s]
        if not o:
            continue
        na, langst = bevestigd(o.pop("reeks"))
        b = o.pop("beste")
        o.update(duur_s=round(o["eind"] - o["begin"], 1), begin=iso(o["begin"]), eind=iso(o["eind"]),
                 duur_100_s=round(langst, 1),
                 winst_eur=b["winst_eur"], diepte_eur=b["diepte_eur"], pct=b["pct"], best_eur=b["best_eur"],
                 min_inleg_eur=b["min_inleg_eur"], winst_bij=b["winst_bij"])
        if na:
            na = dict(na, t=iso(na["t"]))
        o["na_3s"] = na
    g["winst_mediaan_eur"] = round(statistics.median(w), 4) if w else 0.0
    g["duur_s"] = round(g["eind"] - g["begin"], 1)
    g["begin"], g["eind"] = iso(g["begin"]), iso(g["eind"])
    g["eind_reden"] = reden
    g["verdacht"] = bool((g["laag"] or {}).get("pct", 0) > VERDACHT * 100)
    return g
