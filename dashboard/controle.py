"""Controle van organisatie/projecten.json vóór de bouw van het dashboard.

controleer(tekst) geeft (data, fouten): data is altijd bruikbaar voor de bouw (foute velden zijn
weggehaald of leeg gemaakt), fouten is een lijst van zinnen in gewone woorden die het dashboard
bovenaan de pagina toont. Ook los te draaien: python3 dashboard/controle.py [pad]
"""
import json
import re
import sys

SOORTEN = {"product", "geldroute", "meetproject"}
VOOR = {"Dortus", "Thijs-zelf"}
KLEUREN = {"op-koers", "let-op", "risico", "stil"}
LABELS = {"GEZIEN", "DERDEN", "GOK"}
DATUM = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def _getal(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and x >= 0


def _verwacht_ok(v):
    if v is None or _getal(v):
        return True
    return isinstance(v, list) and len(v) == 2 and all(_getal(x) for x in v) and v[0] <= v[1]


def thijs_lijst(t):
    """Het veld thijs als lijst: null, één punt (oude vorm) of een lijst punten."""
    if t is None:
        return []
    if isinstance(t, dict):
        return [t]
    return t if isinstance(t, list) else None


def controleer(tekst):
    fouten = []
    try:
        data = json.loads(tekst)
    except json.JSONDecodeError as e:
        return {"projecten": []}, [f"projecten.json is geen geldige JSON (regel {e.lineno}, kolom {e.colno}: {e.msg}). Het dashboard toont daarom geen projecten tot dit is opgelost."]
    if not isinstance(data, dict) or not isinstance(data.get("projecten"), list):
        return {"projecten": []}, ["projecten.json mist de lijst 'projecten'. Het dashboard toont daarom geen projecten."]
    b = data.get("bijgewerkt")
    if not (isinstance(b, dict) and isinstance(b.get("datum"), str) and re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", b["datum"])):
        fouten.append("'bijgewerkt' bovenaan moet een datum hebben als \"JJJJ-MM-DD UU:MM\" en 'door'.")
    goed, ids = [], set()
    for i, p in enumerate(data["projecten"]):
        if not isinstance(p, dict):
            fouten.append(f"Project {i + 1} is geen blok met velden; overgeslagen.")
            continue
        naam = p.get("naam") or p.get("id") or f"project {i + 1}"
        if not (isinstance(p.get("id"), str) and ID.match(p["id"])):
            fouten.append(f"{naam}: 'id' ontbreekt of heeft andere tekens dan kleine letters, cijfers en streepjes; overgeslagen.")
            continue
        if p["id"] in ids:
            fouten.append(f"{naam}: de id '{p['id']}' staat er twee keer; de tweede is overgeslagen.")
            continue
        ids.add(p["id"])
        if not isinstance(p.get("naam"), str) or not p["naam"].strip():
            fouten.append(f"{p['id']}: 'naam' ontbreekt.")
            p["naam"] = p["id"]
        if p.get("soort") not in SOORTEN:
            fouten.append(f"{naam}: 'soort' moet product, geldroute of meetproject zijn.")
        if p.get("voor") not in VOOR:
            fouten.append(f"{naam}: 'voor' moet Dortus of Thijs-zelf zijn; ik reken het tot Dortus.")
            p["voor"] = "Dortus"
        s = p.get("status")
        if not (isinstance(s, dict) and isinstance(s.get("woord"), str) and s.get("kleur") in KLEUREN):
            fouten.append(f"{naam}: 'status' moet een woord, een zin en een kleur (op-koers, let-op, risico of stil) hebben.")
            p["status"] = {"woord": (s or {}).get("woord", "onbekend") if isinstance(s, dict) else "onbekend", "kleur": "stil", "zin": (s or {}).get("zin", "") if isinstance(s, dict) else ""}
        for veld in ("kans", "prognose"):
            x = p.get(veld)
            if x is None:
                continue
            if not isinstance(x, dict):
                fouten.append(f"{naam}: '{veld}' moet een blok met velden zijn; weggelaten.")
                p[veld] = None
                continue
            if x.get("label") not in LABELS:
                fouten.append(f"{naam}: '{veld}' heeft geen label GEZIEN, DERDEN of GOK.")
        k = p.get("kans")
        if isinstance(k, dict):
            if (k.get("laag") is not None or k.get("hoog") is not None) and not (_getal(k.get("laag")) and _getal(k.get("hoog")) and k["laag"] <= k["hoog"] <= 100):
                fouten.append(f"{naam}: kans 'laag' en 'hoog' moeten getallen van 0 tot 100 zijn, laag niet boven hoog; kans weggelaten.")
                p["kans"] = None
        g = p.get("prognose")
        if isinstance(g, dict):
            if not _verwacht_ok(g.get("verwacht")):
                fouten.append(f"{naam}: prognose 'verwacht' moet een getal of [van, tot] zijn (nu {json.dumps(g.get('verwacht'), ensure_ascii=False)}); weggelaten.")
                g["verwacht"] = None
            for r in ("laag", "hoog"):
                if g.get(r) is not None and not _getal(g[r]):
                    fouten.append(f"{naam}: prognose '{r}' moet een getal zijn; weggelaten.")
                    g[r] = None
        d = p.get("deadline")
        if d is not None and not (isinstance(d, dict) and isinstance(d.get("datum"), str) and DATUM.match(d["datum"])):
            fouten.append(f"{naam}: 'deadline' moet een datum als JJJJ-MM-DD hebben; weggelaten.")
            p["deadline"] = None
        t = thijs_lijst(p.get("thijs"))
        if t is None:
            fouten.append(f"{naam}: 'thijs' moet een lijst zijn (of null); weggelaten.")
            t = []
        schoon_t = []
        for punt in t:
            if not (isinstance(punt, dict) and isinstance(punt.get("doen"), str) and punt["doen"].strip()):
                fouten.append(f"{naam}: een punt in 'thijs' mist 'doen'; overgeslagen.")
                continue
            if punt.get("voor") is not None and not (isinstance(punt["voor"], str) and DATUM.match(punt["voor"])):
                fouten.append(f"{naam}: 'voor' bij een punt voor Thijs moet JJJJ-MM-DD zijn; datum weggelaten.")
                punt = {**punt, "voor": None}
            schoon_t.append(punt)
        p["thijs"] = schoon_t
        for veld in ("agents", "cijfers", "mappen", "keuringen", "links"):
            if p.get(veld) is not None and not isinstance(p[veld], list):
                fouten.append(f"{naam}: '{veld}' moet een lijst zijn; weggelaten.")
                p[veld] = []
        goed.append(p)
    data["projecten"] = goed
    return data, fouten


if __name__ == "__main__":
    pad = sys.argv[1] if len(sys.argv) > 1 else "organisatie/projecten.json"
    with open(pad, encoding="utf-8") as f:
        _, fouten = controleer(f.read())
    for r in fouten:
        print("FOUT:", r)
    print("projecten.json: OK" if not fouten else f"projecten.json: {len(fouten)} fout(en)")
    sys.exit(1 if fouten else 0)
