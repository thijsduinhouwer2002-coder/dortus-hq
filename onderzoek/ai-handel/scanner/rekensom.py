"""Rekensom van de koersverschil-scanner: twee orderboeken tegelijk aflopen en de winst na takerkosten en
opnamekosten uitrekenen. Losgehaald uit scanner.py (keuring, kan-punt: onder de ±400 regels); scanner.py zet
dezelfde namen door, zodat scanner.vul, scanner.bereken en scanner.is_kans blijven werken (radar.py).
"""

VERDACHT = 0.15          # bruto verschil boven 15%: bijna altijd een andere munt of een dode markt
PLAFONDS_EUR = (100, 500, 1000, 2500)   # winst uitgerekend bij deze bedragen per kans
RUIMTE_MAX_EUR = 20000   # hoe ver we het boek aflopen om de winstgevende ruimte te meten


def vul(laten, biedingen, fee_koop, fee_verkoop, plafond_quote):
    """Loop de laten van de koopbeurs en de biedingen van de verkoopbeurs tegelijk af, zolang kopen (met
    takerkosten) goedkoper is dan verkopen (met takerkosten), tot plafond_quote is uitgegeven.
    Geeft (munten, uitgegeven, ontvangen), alles in de quote. Zonder opnamekosten."""
    i = j = 0
    la = [list(x) for x in laten]
    bi = [list(x) for x in biedingen]
    munten = uit = ontvangen = 0.0
    while i < len(la) and j < len(bi) and uit < plafond_quote:
        pk, qk = la[i]
        pv, qv = bi[j]
        kost = pk * (1 + fee_koop)
        krijg = pv * (1 - fee_verkoop)
        if kost >= krijg:
            break
        q = min(qk, qv, (plafond_quote - uit) / kost)
        if q <= 0:
            break
        munten += q
        uit += q * kost
        ontvangen += q * krijg
        la[i][1] -= q
        bi[j][1] -= q
        if la[i][1] <= 1e-15:
            i += 1
        if bi[j][1] <= 1e-15:
            j += 1
    return munten, uit, ontvangen


def bereken(laten, biedingen, fee_koop, fee_verkoop, opname_munt, eur_per_quote):
    """Winst na alle kosten bij elk plafond, en de winstgevende ruimte op het boek. Bedragen in euro.
    opname_munt: opnamekosten in munten (één opname per kans), of None als onbekend (dan 0, en dat staat erbij)."""
    if not laten or not biedingen or eur_per_quote <= 0:
        return None
    fee_m = opname_munt or 0.0
    beste_bod = biedingen[0][0]
    uit = {}
    for p in PLAFONDS_EUR:
        m, kost, krijg = vul(laten, biedingen, fee_koop, fee_verkoop, p / eur_per_quote)
        uit[f"winst{p}"] = round((krijg - kost - fee_m * beste_bod) * eur_per_quote, 4) if m > 0 else None
    m, kost, krijg = vul(laten, biedingen, fee_koop, fee_verkoop, RUIMTE_MAX_EUR / eur_per_quote)
    uit["ruimte_eur"] = round(kost * eur_per_quote, 2)
    uit["winst_ruimte"] = round((krijg - kost - fee_m * beste_bod) * eur_per_quote, 4) if m > 0 else None
    uit["opname_eur"] = round(fee_m * beste_bod * eur_per_quote, 4)
    uit["bruto_pct"] = round((biedingen[0][0] / laten[0][0] - 1) * 100, 4)
    return uit


def is_kans(r):
    """Er ligt na alle kosten winst op het boek (bij de volle winstgevende ruimte), en het verschil op het boek is
    niet groter dan de grens voor "verdacht" (die geldt ook op het boek, niet alleen op de ticker; keuring A8)."""
    return bool(r) and r["winst_ruimte"] is not None and r["winst_ruimte"] > 0 and r["bruto_pct"] <= VERDACHT * 100
