"""Bezoekcijfers van dortus.com uit Amami, voor scorebord.py. Vera, 16 nov 2026 (opdracht hoofdchat 20:35).

De sleutel komt alleen uit de omgeving (AMAMI_API_KEY, GitHub-secret) en wordt nooit geprint of
opgeslagen. API: Umami-compatibel, adres en paden uit het npm-pakket amami-analytics-mcp.
"""
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Dortus scorebord; 1 keer per dag)"
AMAMI_API = "https://analytics.amami.dev/api"  # uit het npm-pakket amami-analytics-mcp (Umami-API)
AMAMI_DAGEN = 6
AMAMI_START = "2026-11-16"  # Amami staat sinds 16 nov ±20:30 op dortus.com; eerdere dagen zouden nullen geven
AMAMI_PAUZE = 7
# productpagina's op dortus.com; alles eronder telt bij dat product
PAGINAS = {"/click-joints": "Click Joints", "/ebb": "Ebb", "/rollwright": "Rollwright", "/bison-flex": "Bison & Flex", "/tt": "TikTok-adres", "/yt": "YouTube-adres"}


# Bezoekcijfers dortus.com: (datum, product, maat, waarde); datum is de bezoekdag, niet de meetdag
BEZOEK = []
BEZOEK_DAGEN = set()
VANDAAG_TOT_NU = {}  # alleen in scorebord.md, niet in de csv: de dag is nog niet om


def amami_get(pad, params, sleutel):
    url = f"{AMAMI_API}{pad}?{urllib.parse.urlencode(params)}"
    koppen = [{"Authorization": f"Bearer {sleutel}"}, {"x-umami-api-key": sleutel}]  # docs noemen beide
    code, k = None, 0
    for p in range(4):
        time.sleep(AMAMI_PAUZE)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json", **koppen[k]})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            code = e.code
            if code == 401 and k == 0:
                k = 1  # andere kop proberen
                continue
            if code in (401, 403, 404):
                break
            time.sleep(15 * (p + 1) if code == 429 else 3)
        except Exception as e:  # noqa: BLE001
            code = type(e).__name__
            time.sleep(3)
    # de sleutel zit in de kop, niet in de url, dus deze regel lekt hem niet
    print(f"  Amami niet gelukt: {pad.split('/')[-1]} ({code})", file=sys.stderr)
    return None


def getal_uit(v):
    """Umami geeft soms 5 en soms {"value": 5, "prev": 3}."""
    if isinstance(v, dict):
        v = v.get("value")
    return v if isinstance(v, (int, float)) else None


def pagina_van(pad):
    pad = (pad or "").split("?")[0].split("#")[0]
    pad = re.sub(r"/index\.html?$", "/", pad).rstrip("/") or "/"
    if pad == "/":
        return "voorpagina"
    for begin, naam in PAGINAS.items():
        if pad == begin or pad.startswith(begin + "/"):
            return naam
    return "overig"


def dortus_bezoek(al_gemeten, haal, noten):
    sleutel = os.environ.get("AMAMI_API_KEY", "").strip()
    if not sleutel:
        noten.append("dortus.com: geen AMAMI_API_KEY in de omgeving, bezoekcijfers overgeslagen.")
        return
    html = haal("https://dortus.com/", json_=False) or ""
    m = re.search(r'data-website-id="([0-9a-f-]{36})"', html)
    if not m:
        noten.append("dortus.com: geen Amami website-id in de html gevonden.")
        return
    site = m.group(1)
    from zoneinfo import ZoneInfo
    tz = ZoneInfo("Europe/Amsterdam")
    vandaag = dt.datetime.now(tz).date()
    for terug in range(AMAMI_DAGEN, -1, -1):
        dag = vandaag - dt.timedelta(days=terug)
        if dag.isoformat() in al_gemeten or dag.isoformat() < AMAMI_START:
            continue
        begin = dt.datetime.combine(dag, dt.time(0), tz)
        eind = min(dt.datetime.combine(dag + dt.timedelta(days=1), dt.time(0), tz), dt.datetime.now(tz))
        bereik = {"startAt": int(begin.timestamp() * 1000), "endAt": int(eind.timestamp() * 1000) - 1}
        doel = BEZOEK if terug > 0 else None
        stats = amami_get(f"/websites/{site}/stats", bereik, sleutel)
        if not isinstance(stats, dict):
            noten.append(f"dortus.com: bezoekcijfers van {dag} niet leesbaar.")
            continue
        metr = amami_get(f"/websites/{site}/metrics", dict(bereik, type="path", limit=500), sleutel)
        rijen = metr.get("data", []) if isinstance(metr, dict) else metr
        if not isinstance(rijen, list):
            noten.append(f"dortus.com: cijfers per pagina van {dag} niet leesbaar, alleen het totaal.")
            rijen = []
        d = dag.isoformat()
        uit = []
        for maat in ("visitors", "visits", "pageviews"):
            w = getal_uit(stats.get(maat))
            if w is not None:
                uit.append((d, "dortus.com", {"visitors": "bezoekers", "visits": "bezoeken", "pageviews": "weergaven"}[maat], int(w)))
        per = {}
        for r in rijen:
            if isinstance(r, dict) and getal_uit(r.get("y")) is not None:
                naam = pagina_van(r.get("x"))
                per[naam] = per.get(naam, 0) + int(getal_uit(r.get("y")))
        if metr is not None:
            for naam in ["voorpagina", *PAGINAS.values(), "overig"]:
                uit.append((d, naam, "pagina", per.get(naam, 0)))
        if doel is None:  # vandaag: alleen tonen
            VANDAAG_TOT_NU.update({(p, m): w for _, p, m, w in uit})
            VANDAAG_TOT_NU["tijd"] = f"{dag} tot {eind:%H:%M}"
            continue
        if not any(m == "bezoekers" for _, _, m, _ in uit):
            noten.append(f"dortus.com: geen bezoekersgetal voor {dag} in het antwoord, dag niet opgeslagen.")
            continue
        doel.extend(uit)
        BEZOEK_DAGEN.add(d)



def tekst(w):
    return "?" if w in (None, "") else str(w)


def bezoek_tabel(alles):
    rijen = [r for r in alles if r["platform"] == "dortus.com"]
    kop = ["", "## Bezoekers dortus.com (Amami, per dag, Amsterdamse tijd)", ""]
    if not rijen and not VANDAAG_TOT_NU:
        return kop + ["Nog geen cijfers. Ze komen zodra de workflow met AMAMI_API_KEY heeft gedraaid "
                      f"(eerste hele dag: {AMAMI_START}, Amami staat er sinds ±20:30)."]
    cel = {(r["datum"], r["product"], r["maat"]): r["waarde"] for r in rijen}
    dagen = sorted({r["datum"] for r in rijen}, reverse=True)[:14]
    kolommen = ["voorpagina", *PAGINAS.values(), "overig"]
    regels = kop + [
        "Bezoekers, bezoeken en weergaven gelden voor de hele site. Per pagina: het getal dat Amami per pad geeft "
        "(Umami-metrics), opgeteld per product inclusief subpagina's. Amami bewaart cijfers 7 dagen; "
        "oudere dagen staan alleen hier en in de csv.",
        "",
        "| Dag | Bezoekers | Bezoeken | Weergaven | " + " | ".join(kolommen) + " |",
        "|---|---|---|---|" + "---|" * len(kolommen),
    ]
    if VANDAAG_TOT_NU:
        v = VANDAAG_TOT_NU
        totaal = [tekst(v.get(("dortus.com", m))) for m in ("bezoekers", "bezoeken", "weergaven")]
        per = [tekst(v.get((k, "pagina"))) for k in kolommen]
        regels.append(f"| {v['tijd']} (nog niet om, niet in de csv) | " + " | ".join(totaal + per) + " |")
    for d in dagen:
        totaal = [tekst(cel.get((d, "dortus.com", m))) for m in ("bezoekers", "bezoeken", "weergaven")]
        per = [tekst(cel.get((d, k, "pagina"))) for k in kolommen]
        regels.append(f"| {d} | " + " | ".join(totaal + per) + " |")
    return regels

