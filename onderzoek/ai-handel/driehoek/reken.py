"""De rekensom van de driehoek-meter: driehoeken zoeken, doorrekenen tegen de beste prijzen en tegen het boek.
Geen netwerk; alles wat hier staat, is met verzonnen boeken te testen (test_driehoek.py)."""
import itertools

from kosten import afronden, vaste_kosten_eur

VOORKEUR = ("EUR", "USDT", "USDC", "USD", "BTC", "ETH")
VASTE = (100, 150, 200, 500, 1000, 2000, 5000, 10000)
BEDRAGEN = sorted({round(10 * 1.25 ** i, 2) for i in range(41)} | set(VASTE))   # €10 tot ±€75.000
KLEIN = (100, 150, 200)
EURK = {}            # gedeelde euro-koersen (munt -> euro per munt), gevuld door alle draden


def loop(kant, bedrag, koop):
    """Loop één kant van het boek af. koop: bedrag in quote, kant = laten, uit = basismunt.
    Verkoop: bedrag in basismunt, kant = biedingen, uit = quote. None als het opgehaalde boek te dun is."""
    uit = 0.0
    for prijs, hv in kant:
        if koop:
            k = prijs * hv
            if bedrag <= k:
                return uit + bedrag / prijs
            uit += hv
            bedrag -= k
        else:
            if bedrag <= hv:
                return uit + bedrag * prijs
            uit += hv * prijs
            bedrag -= hv
    return None


def rondje(stappen, boeken, x, scen, x_eur=None):
    """Stuur x begin-munten door de drie stappen. Geeft (terug na kosten, past, deel) of (None, False, 0).
    past = elke stap haalt de minimale ordergrootte (munten, quote-bedrag, en bij Bitget de waarde in USDT, via
    x_eur benaderd). deel = welk deel van x echt rondging: het aantal munten wordt per stap naar beneden afgerond
    op de stapgrootte van de beurs; wat niet rondgaat, blijft liggen en telt niet als winst of verlies."""
    a, past, deel = x, True, 1.0
    for st in stappen:
        mn = st.get("min") or {}
        bied, laat = boeken[st["paar"]]
        if st["koop"]:
            ruw = loop(laat, a, True)
            if ruw is None:
                return None, False, 0.0
            munten = afronden(ruw, mn.get("stap"))
            deel *= munten / ruw if ruw > 0 else 0.0
            quote = a * (munten / ruw if ruw > 0 else 0.0)
            b = munten
        else:
            munten = afronden(a, mn.get("stap"))
            deel *= munten / a if a > 0 else 0.0
            b = loop(bied, munten, False)
            if b is None:
                return None, False, 0.0
            quote = b
        if munten <= 0 or munten < mn.get("base", 0) or quote < mn.get("quote", 0):
            past = False
        if mn.get("usdt") and x_eur is not None and x_eur < mn["usdt"] * EURK.get("USDT", 1.0):
            past = False
        a = b * (1 - st[scen])
    return a, past, deel


def top(stappen, prijzen, scen):
    """Opbrengst per 1 begin-munt tegen de beste prijzen (bovengrens: verder in het boek wordt het slechter)."""
    m = 1.0
    for st in stappen:
        p = prijzen.get(st["sleutel"])
        if not p:
            return 0.0
        bod, laat = p
        if bod <= 0 or laat <= 0:
            return 0.0
        m *= (1 / laat if st["koop"] else bod) * (1 - st[scen])
    return m


def curve(stappen, boeken, eur_per_munt, scen):
    """Winst in euro bij elk bedrag van BEDRAGEN, na kosten, afronding en vaste kosten per order.
    None als er nergens winst is (of geen enkel bedrag de minimale ordergrootte haalt), anders een dict."""
    vast = sum(st.get("vast_eur", 0.0) for st in stappen)
    punten = []
    for e in BEDRAGEN:
        x = e / eur_per_munt
        terug, past, deel = rondje(stappen, boeken, x, scen, e)
        if terug is None:
            break
        punten.append((e, (terug - x * deel) * eur_per_munt - vast, past))
    goed = [p for p in punten if p[2]]
    if not goed:
        return None
    best_e, best_w, _ = max(goed, key=lambda p: p[1])
    if best_w <= 0:
        return None
    winst_bij = {}
    for s in VASTE:
        w = [p[1] for p in goed if p[0] <= s and p[1] > 0]
        winst_bij[str(s)] = round(max(w), 4) if w else 0.0
    return {"winst_eur": round(best_w, 4), "best_eur": best_e,
            # diepte: het kleinste bedrag waarmee je (bijna) alle winst pakt; meer erin levert niets meer op
            "diepte_eur": min(p[0] for p in goed if p[1] >= 0.99 * best_w),
            "min_inleg_eur": min(p[0] for p in goed),
            "pct": round(100 * best_w / best_e, 4), "boek_op": len(punten) < len(BEDRAGEN),
            "winst_bij": winst_bij}


def min_inleg(stappen, prijzen, eur_per_munt):
    """Kleinste bedrag uit BEDRAGEN waarbij alle drie stappen de minimale ordergrootte halen, tegen de beste
    prijzen (boek met oneindige diepte). None als het niet te rekenen is."""
    boeken = {}
    for st in stappen:
        p = prijzen.get(st["sleutel"])
        if not p or p[0] <= 0 or p[1] <= 0:
            return None
        boeken[st["paar"]] = ([(p[0], float("inf"))], [(p[1], float("inf"))])
    for e in BEDRAGEN:
        terug, past, _ = rondje(stappen, boeken, e / eur_per_munt, "hoog", e)
        if terug is not None and past:
            return e
    return None


def driehoeken(paren):
    """Alle driehoeken van 3 munten waarvan elk paar op de beurs bestaat, in beide richtingen.
    Geeft lijst van [begin, m2, m3] (begin > m2 > m3 > begin); begin volgens VOORKEUR (EUR eerst)."""
    buren = {}
    for (b, q) in paren:
        buren.setdefault(b, set()).add(q)
        buren.setdefault(q, set()).add(b)
    gezien = set()
    for a in buren:
        for x, y in itertools.combinations(sorted(buren[a]), 2):
            if y in buren.get(x, ()):
                gezien.add(frozenset((a, x, y)))
    uit = []
    for d in sorted(gezien, key=sorted):
        s, x, y = sorted(d, key=lambda m: (VOORKEUR.index(m) if m in VOORKEUR else len(VOORKEUR), m))
        uit.append([s, x, y])
        uit.append([s, y, x])
    return uit


def maak_stappen(volgorde, paren, kosten_van, mins=None, beurs=""):
    st = []
    for van, naar in zip(volgorde, volgorde[1:] + volgorde[:1]):
        if (van, naar) in paren:
            sl, koop = (van, naar), False          # verkoop van basismunt tegen het bod
        elif (naar, van) in paren:
            sl, koop = (naar, van), True           # koop van basismunt tegen de laat
        else:
            return None
        hoog, laag, _ = kosten_van[sl]
        st.append({"sleutel": sl, "paar": paren[sl]["id"], "koop": koop, "hoog": hoog, "laag": laag,
                   "min": (mins or {}).get(sl) or {}, "vast_eur": vaste_kosten_eur(beurs, sl)})
    return st


def mid(p):
    return (p[0] + p[1]) / 2 if p and p[0] > 0 and p[1] > 0 else None


def eur_koers(munt, prijzen):
    if munt == "EUR":
        return 1.0
    m = mid(prijzen.get((munt, "EUR")))
    if m:
        return m
    m = mid(prijzen.get(("EUR", munt)))
    if m:
        return 1 / m
    if EURK.get(munt):
        return EURK[munt]
    for q in ("USDT", "USDC", "USD", "BTC", "ETH"):
        m = mid(prijzen.get((munt, q)))
        if m and q != munt and EURK.get(q):
            return m * EURK[q]
    return None
