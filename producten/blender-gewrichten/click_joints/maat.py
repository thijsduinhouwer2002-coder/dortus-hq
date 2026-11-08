"""Maten van het gewricht: kogel, nek per hoekstand, klikopening, bolnaad, Auto-diameter en afstand tot een
ander gewricht. Afgesplitst uit gewricht.py (bestand bleef zo onder ±400 regels)."""
import math

from mathutils import Vector

from . import passing

SCHUIF_MM = 0.0137
BODEM_MM = 1.55  # minimale bodem van deel B naast de klikopening: net boven de grens van Good fit (1,5 mm)
# Klikopening van de kom: 0,85 keer de kogeldiameter, zodat twee los geprinte delen met wat druk
# in elkaar klikken. Zonder extra speling: anders komt de opening bij kleine kogels boven 0,90 keer de diameter.
OPENING = 0.85
# Vorm v0.3 (8 nov, Bram): onder de klikrand een trechter (halve tophoek = grens + MARGE_HOEK), zodat de nek
# over het hele bereik vrij blijft. De naad tussen deel A en B is een bol om het kogelmidden (straal: grootste
# straal van het figuur rond de as plus NAAD_MARGE_MM).
# Regel Daan (8 nov, ronde j): drie vaste hoekstanden per gewricht, 30, 25 of 20 graden. Per stand rekenen we
# de nek uit zodat de grens (nek tegen klikrand) precies die hoek is: t = acos(n/(r+s)) - atan2(d, a), dus
# n = (r+s) * cos(t + atan2(d, a)). Bij r 2,5 en s 0,2 is dat zonder marge 0,40r (30), 0,49r (25) en 0,57r (20);
# met de marge van 0,5 graad (zie onder) 0,39r, 0,48r en 0,56r.
HOEKEN = (30, 25, 20)
NEK_PEN = 0.40
RANG = {"groen": 2, "oranje": 1, "rood": 0}
MARGE_HOEK = 3.0
MARGE_STAND = 0.5  # graden: berekende grens = stand + 0,5
NAAD_MARGE_MM = 0.5
TE_DUN = "Too thin here for a ball joint. Try a thicker spot."


def maten(inst, u, kogel_mm=None, hoek=HOEKEN[0]):
    r = (inst.kogel_mm if kogel_mm is None else kogel_mm) / 2 * u
    s = inst.speling_mm * u
    maat = {"r": r, "s": s, "nek_r": NEK_PEN * r, "open_r": OPENING * r, "schuif": SCHUIF_MM * u,
            "onder_z": -0.4 * r, "midden_z": 1.4 * r, "top_z": 2.2 * r}
    if inst.soort == "PEN":
        maat["midden_z"] = maat["top_z"] / 2
        return maat
    # Ronde g: bij kleine kogels zet het kogelmidden zo hoog dat de bodem van deel B BODEM_MM is.
    rk, open_r = r + s, maat["open_r"]
    d_lip = math.sqrt(max(rk * rk - open_r * open_r, 0.0))
    maat["midden_z"] = max(maat["midden_z"], d_lip + maat["schuif"] + BODEM_MM * u)
    # Nek per hoekstand, gerekend voor de stand plus MARGE_STAND: precies op de stand raakt de nek de klikrand al
    # (beweegproef run 42475385547: stap 30 botste, gemeten 27,5). Zo is de stand zelf echt vrij.
    maat["nek_r"] = rk * math.cos(math.radians(hoek + MARGE_STAND) + math.atan2(d_lip, open_r))
    grens = math.degrees(math.acos(min(maat["nek_r"] / rk, 1.0)) - math.atan2(d_lip, open_r))
    maat["lip_d"] = d_lip            # klikrand: zo ver onder het kogelmidden
    maat["hoek"] = hoek              # gekozen stand
    maat["grens_graden"] = grens     # rekensom: nek tegen klikrand (minstens de stand)
    maat["trechter_graden"] = grens + MARGE_HOEK
    return maat


def zet_naad(maat, bvh, frame, u):
    """Straal van de bolnaad: grootste afstand van de as tot de huid (snijvlak en kogelmidden) plus marge.
    Zonder treffer (punt buiten het figuur) blijft de naad weg; de passing geeft dan toch rood."""
    straal = passing.grootste_straal(bvh, frame, (maat["schuif"] * 2, maat["midden_z"]))
    if straal is None:
        return maat
    maat["naad_r"] = max(straal + (NAAD_MARGE_MM * u) + maat["s"], maat["r"] + maat["s"] + 1.0 * u)
    maat["onder_z"] = min(maat["onder_z"], maat["midden_z"] - maat["naad_r"] - 0.4 * maat["r"])
    return maat


def beste_maat(inst, u, bvh, frame, kogel_mm=None):
    """(maat, kleur, wand, uitleg). Kogel: de grootste hoekstand (30, 25, 20) met Good fit; geen Good fit,
    dan de grootste met Tight; ook geen Tight, dan de stand 20 (rood: niet snijden, melding TE_DUN)."""
    if inst.soort != "KOGEL":
        m = maten(inst, u, kogel_mm)
        return (m,) + tuple(passing.beoordeel(bvh, frame, m, inst.soort, u))
    krap = laatste = None
    for hoek in HOEKEN:
        m = zet_naad(maten(inst, u, kogel_mm, hoek), bvh, frame, u)
        kleur, wand, uitleg = passing.beoordeel(bvh, frame, m, inst.soort, u)
        if kleur == "groen":
            return m, kleur, wand, uitleg
        laatste = (m, kleur, wand, uitleg)
        if kleur == "oranje" and krap is None:
            krap = laatste
    return krap or laatste


def kies_auto(inst, u, bvh, frame, breedte_mm):
    """Automatische diameter (Daan, tussenreactie 2): de grootste kogel met Good fit (bij welke hoekstand ook).

    Begint bij 0,6 keer de smalste breedte (afgerond op 0,5 mm, de bovengrens) en zakt in stappen van
    0,5 mm tot 2 mm, tot de passing groen is. Lukt groen nergens, dan de grootste met Tight; is ook dat er
    niet, dan de 0,6-regel (die geeft rood en er wordt niet gesneden).
    Geeft (diameter in mm, keuze): keuze is "goed", "krap" of "regel"."""
    boven = passing.auto_diameter(breedte_mm)
    kandidaten = []
    d = boven
    while d >= passing.AUTO_MIN_MM - 1e-9:
        kandidaten.append(round(d, 3))
        d -= passing.AUTO_STAP_MM
    eerste_krap = None
    for d in kandidaten:
        _, kleur, _, _ = beste_maat(inst, u, bvh, frame, d)
        if kleur == "groen":
            return d, "goed"
        if kleur == "oranje" and eerste_krap is None:
            eerste_krap = d
    if eerste_krap is not None:
        return eerste_krap, "krap"
    return boven, "regel"


def te_dicht(bron, centrum, richting, maat, u):
    """Nodige afstand in mm (naar boven afgerond) als het nieuwe gewricht te dicht bij het gewricht op `bron`
    ligt, anders None. Rekensom (afstand tussen de kogelmiddens):
    - nieuw: de bolnaad (naad_r) en de nek eronder (tot naad_r + 0,4r onder het kogelmidden);
    - oud, aan de kant van de kom (boven het oude kogelmidden langs de oude as): kom r + s;
    - oud, aan de kant van het snijvlak: trechter en nek tot de oude bolnaad, naad_r + 0,4r.
    Komt de bolnaad van het nieuwe gewricht in kom of trechter van het oude, dan gaan de delen stuk
    (run 42471820202: tweede gewricht 8 mm verder gaf 0 delen)."""
    if "cj_centrum" not in bron or bron.get("cj_soort", "KOGEL") != "KOGEL" or "naad_r" not in maat:
        return None
    oud_c, oud_as = Vector(bron["cj_centrum"]), Vector(bron["cj_as"])
    oud_r = bron.get("cj_kogel_r", 0.0)
    oud_s = bron.get("cj_speling_mm", 0.2) * u
    oud_naad = bron.get("cj_naad_r", -1.0)
    verschil = centrum - oud_c
    if verschil.dot(oud_as) >= 0 or oud_naad < 0:
        oud_bereik = oud_r + oud_s
    else:
        oud_bereik = oud_naad + 0.4 * oud_r
    nieuw_bereik = maat["naad_r"] + 0.4 * maat["r"]
    nodig = (oud_bereik + nieuw_bereik) / u
    if verschil.length / u >= nodig:
        return None
    return math.ceil(nodig - 1e-9)
