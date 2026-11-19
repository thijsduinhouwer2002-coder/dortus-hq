#!/usr/bin/env python3
"""Schaduwbot voor Polymarket: meet wat een makerbot in jonge temperatuurmarkten HAD verdiend en verloren.

Alleen openbare gegevens. Geen account, geen sleutel, geen wallet, geen orders, geen geld.
Er wordt nooit iets geplaatst of getekend: dit script doet alleen GET-verzoeken plus POST /books (een openbaar
leesverzoek voor orderboeken, zonder account).

Wat het doet (zie README.md):
  elke 10 minuten   temperatuurmarkten (Gamma) + beloningsinstellingen (CLOB /rewards/markets/current)
  elke minuut       orderboeken (POST /books), per markt en per variant een denkbeeldig bod en laat rond het midden,
                    beloning schatten met de formule van Polymarket (twee grenzen: hoog en laag)
  elke minuut       nieuwe trades (Data API v2, per 20 events) -> denkbeeldige vullingen
  elke 30 minuten   ruwe metingen als gzip-CSV naar de map uit/ en (met --git) naar de tak ai-handel-data

Gebruik:
  python3 schaduwbot.py --duur 10 --uit /tmp/sb-uit                  # lokaal 10 minuten, alleen bestanden
  python3 schaduwbot.py --duur 345 --uit uit --git                   # in de workflow, met opslaan op de tak
Alleen standaardbibliotheek (Python 3.9+, zoneinfo).
"""
import argparse
import csv
import datetime as dt
import gzip
import io
import json
import math
import os
import random
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

UTC = dt.timezone.utc
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
DATA = "https://data-api.polymarket.com"
TAK = "ai-handel-data"
KOPPEN = {"User-Agent": "Mozilla/5.0 (schaduwbot, alleen lezen)", "Accept-Encoding": "gzip",
          "Accept": "application/json"}

# Vaste instellingen. Een andere keuze = een nieuwe meting, dus niet tussendoor schuiven.
VASTE_GROOTTE = 20          # aandelen per order; hoger als de markt een grotere minimale grootte eist
VARIANTEN = {"1c": 0.01, "3c": 0.03}   # afstand van het midden; "1c" is waar B het grootste verlies mat
MAX_SPREAD_BOEK = 0.05      # alleen markten met een strak boek (D run 5): beste bod en laat hooguit 5 cent uit elkaar
MAX_VOORRAAD = 2            # rem uit B punt 40: nooit meer dan 2 keer de ordergrootte netto aan één kant
NA_STOP_VOLGEN = 2 * 3600   # na de stop nog 2 uur het midden volgen, voor de prijs 1 uur na een vulling
PLAN_BEWAREN = 120          # minuten aan plannen bewaren voor trades die laat in de Data API staan

STEDEN = {  # slug -> tijdzone van het meetstation (de markt rekent in lokale tijd van het station)
    "amsterdam": "Europe/Amsterdam", "ankara": "Europe/Istanbul", "atlanta": "America/New_York",
    "austin": "America/Chicago", "beijing": "Asia/Shanghai", "buenos-aires": "America/Argentina/Buenos_Aires",
    "busan": "Asia/Seoul", "cape-town": "Africa/Johannesburg", "chengdu": "Asia/Shanghai",
    "chicago": "America/Chicago", "chongqing": "Asia/Shanghai", "dallas": "America/Chicago",
    "denver": "America/Denver", "guangzhou": "Asia/Shanghai", "helsinki": "Europe/Helsinki",
    "hong-kong": "Asia/Hong_Kong", "houston": "America/Chicago", "istanbul": "Europe/Istanbul",
    "jeddah": "Asia/Riyadh", "jinan": "Asia/Shanghai", "karachi": "Asia/Karachi",
    "kuala-lumpur": "Asia/Kuala_Lumpur", "london": "Europe/London", "los-angeles": "America/Los_Angeles",
    "lucknow": "Asia/Kolkata", "madrid": "Europe/Madrid", "manila": "Asia/Manila",
    "mexico-city": "America/Mexico_City", "miami": "America/New_York", "milan": "Europe/Rome",
    "moscow": "Europe/Moscow", "munich": "Europe/Berlin", "nyc": "America/New_York",
    "panama-city": "America/Panama", "paris": "Europe/Paris", "qingdao": "Asia/Shanghai",
    "san-francisco": "America/Los_Angeles", "sao-paulo": "America/Sao_Paulo", "seattle": "America/Los_Angeles",
    "seoul": "Asia/Seoul", "shanghai": "Asia/Shanghai", "shenzhen": "Asia/Shanghai", "singapore": "Asia/Singapore",
    "taipei": "Asia/Taipei", "tel-aviv": "Asia/Jerusalem", "tokyo": "Asia/Tokyo", "toronto": "America/Toronto",
    "warsaw": "Europe/Warsaw", "wellington": "Pacific/Auckland", "wuhan": "Asia/Shanghai",
    "zhengzhou": "Asia/Shanghai", "berlin": "Europe/Berlin", "rome": "Europe/Rome", "dubai": "Asia/Dubai",
    "delhi": "Asia/Kolkata", "new-delhi": "Asia/Kolkata", "mumbai": "Asia/Kolkata", "sydney": "Australia/Sydney",
    "melbourne": "Australia/Melbourne", "phoenix": "America/Phoenix", "boston": "America/New_York",
    "philadelphia": "America/New_York", "washington-dc": "America/New_York", "vancouver": "America/Vancouver",
    "lagos": "Africa/Lagos", "cairo": "Africa/Cairo", "bangkok": "Asia/Bangkok", "jakarta": "Asia/Jakarta",
    "hanoi": "Asia/Bangkok", "lima": "America/Lima", "bogota": "America/Bogota", "santiago": "America/Santiago",
}
SLUG = re.compile(r"^(highest|lowest)-temperature-in-(.+)-on-([a-z]+)-(\d{1,2})-(\d{4})$")
MAANDEN = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                       "september", "october", "november", "december"], 1)}


def log(tekst):
    print(f"{dt.datetime.now(UTC):%H:%M:%S} {tekst}", flush=True)


# ---------------------------------------------------------------- openbare API's (alleen lezen)

def vraag(url, body=None, pogingen=4):
    """GET (of POST /books met body). Alleen lezen. Probeert opnieuw bij 429/5xx en netwerkfouten."""
    data = json.dumps(body).encode() if body is not None else None
    koppen = dict(KOPPEN)
    if data is not None:
        koppen["Content-Type"] = "application/json"
    for poging in range(pogingen):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, data=data, headers=koppen), timeout=30)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            return json.loads(b)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and poging < pogingen - 1:
                wacht = float(e.headers.get("Retry-After") or 2 ** poging)
                time.sleep(min(wacht, 20))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError):
            if poging < pogingen - 1:
                time.sleep(2 ** poging)
                continue
            raise


def haal_beloningen():
    """condition_id -> (dagbedrag, max afstand in cent, minimale grootte). Alleen actieve instellingen."""
    vandaag = dt.datetime.now(UTC).date().isoformat()
    uit, cursor = {}, ""
    for _ in range(100):
        d = vraag(f"{CLOB}/rewards/markets/current" + (f"?next_cursor={cursor}" if cursor else ""))
        for m in d.get("data") or []:
            dag = sum(float(c.get("rate_per_day") or 0) for c in m.get("rewards_config") or []
                      if (c.get("start_date") or "") <= vandaag <= (c.get("end_date") or "9999"))
            if dag > 0:
                uit[m["condition_id"]] = (dag, float(m.get("rewards_max_spread") or 0),
                                          float(m.get("rewards_min_size") or 0))
        cursor = d.get("next_cursor") or ""
        if not cursor or cursor == "LTE=":
            break
    return uit


def haal_temperatuur_events():
    evs = []
    for offset in range(0, 3000, 100):
        d = vraag(f"{GAMMA}/events?tag_slug=weather&closed=false&limit=100&offset={offset}"
                  "&order=createdAt&ascending=false")
        evs += d
        if len(d) < 100:
            break
    return [e for e in evs if SLUG.match(e.get("slug") or "")]


def dag_start_lokaal(slug):
    """Begin (00:00 lokale tijd van het meetstation) van de dag waarover de markt gaat, in UTC, of None."""
    m = SLUG.match(slug)
    if not m or m[2] not in STEDEN or m[3] not in MAANDEN:
        return None
    tz = ZoneInfo(STEDEN[m[2]])
    return dt.datetime(int(m[5]), MAANDEN[m[3]], int(m[4]), tzinfo=tz).astimezone(UTC)


def bouw_marktenlijst(nu):
    """Alle temperatuurmarkten met actieve beloning die we volgen (quoten tot de stop, daarna 2 uur het midden)."""
    beloning = haal_beloningen()
    markten, onbekend = {}, set()
    for e in haal_temperatuur_events():
        stop = dag_start_lokaal(e["slug"])
        if stop is None:
            onbekend.add(SLUG.match(e["slug"])[2])
            continue
        if nu.timestamp() > stop.timestamp() + NA_STOP_VOLGEN:
            continue
        aangemaakt = e.get("createdAt") or ""
        for m in e.get("markets") or []:
            b = beloning.get(m.get("conditionId"))
            if not b or not m.get("clobTokenIds") or m.get("closed"):
                continue
            try:
                ja = json.loads(m["clobTokenIds"])[0]
            except (ValueError, IndexError):
                continue
            markten[m["conditionId"]] = {
                "sleutel": m["conditionId"][2:12], "conditie": m["conditionId"], "token": ja,
                "event_id": str(e["id"]), "event": e["slug"], "vakje": m.get("groupItemTitle") or "",
                "aangemaakt": aangemaakt[:19], "stop": int(stop.timestamp()),
                "dagbedrag": b[0], "v": b[1], "min": b[2],
            }
    return markten, sorted(onbekend)


# ---------------------------------------------------------------- de formule (docs Liquidity Rewards)

def punten(v_cent, afstand_cent):
    """S(v, s) = ((v - s) / v)^2, 0 buiten de max afstand."""
    if v_cent <= 0 or afstand_cent >= v_cent:
        return 0.0
    return ((v_cent - afstand_cent) / v_cent) ** 2


def q_min(q1, q2, midden, c=3.0):
    """Minimum van de twee kanten; tussen 0,10 en 0,90 telt één kant ook, gedeeld door c."""
    if 0.10 <= midden <= 0.90:
        return max(min(q1, q2), max(q1 / c, q2 / c))
    return min(q1, q2)


def boek_niveaus(boek):
    bids = sorted(((float(x["price"]), float(x["size"])) for x in boek.get("bids") or []), key=lambda x: -x[0])
    asks = sorted(((float(x["price"]), float(x["size"])) for x in boek.get("asks") or []), key=lambda x: x[0])
    return bids, asks


def aangepast_midden(bids, asks, min_grootte):
    """Benadering van het 'size-cutoff-adjusted midpoint' (B punt 30, GOK): de beste bied- en laatprijs waar
    opgeteld minstens de minimale grootte staat. Valt terug op het gewone midden."""
    def grens(niveaus):
        som = 0.0
        for p, s in niveaus:
            som += s
            if som >= min_grootte:
                return p
        return None
    b, a = grens(bids), grens(asks)
    if b is None or a is None or b >= a:
        return (bids[0][0] + asks[0][0]) / 2
    return (b + a) / 2


def score_anderen(bids, asks, midden, v_cent, min_grootte):
    """Twee grenzen voor de score van alle andere makers samen (B punt 32).
    hoog-voor-ons: alleen niveaus met minstens de minimale grootte, regel van q_min op het hele boek.
    laag-voor-ons: alle niveaus, beide kanten opgeteld."""
    def kant(niveaus, filter_min):
        return sum(punten(v_cent, abs(p - midden) * 100) * s for p, s in niveaus
                   if not filter_min or s >= min_grootte)
    q1_f, q2_f = kant(bids, True), kant(asks, True)
    q1, q2 = kant(bids, False), kant(asks, False)
    return q_min(q1_f, q2_f, midden), q1 + q2


def plan_orders(bids, asks, midden, afstand, tick, grootte, voorraad):
    """Denkbeeldig bod en laat rond het midden, afgerond op de tick, nooit door het boek heen.
    voorraad = netto JA-aandelen (positief = we kochten). Bij te veel voorraad aan één kant zet hij die kant niet."""
    beste_bod, beste_laat = bids[0][0], asks[0][0]
    bod = math.floor(round((midden - afstand) / tick, 6)) * tick
    laat = math.ceil(round((midden + afstand) / tick, 6)) * tick
    bod = min(bod, beste_laat - tick)
    laat = max(laat, beste_bod + tick)
    bod = round(bod, 4) if bod >= tick else None
    laat = round(laat, 4) if laat <= 1 - tick else None
    grens = MAX_VOORRAAD * grootte
    if voorraad >= grens:
        bod = None
    if voorraad <= -grens:
        laat = None
    return bod, laat


def onze_score(bod, laat, midden, v_cent, grootte):
    q1 = punten(v_cent, (midden - bod) * 100) * grootte if bod is not None else 0.0
    q2 = punten(v_cent, (laat - midden) * 100) * grootte if laat is not None else 0.0
    return q_min(q1, q2, midden)


def vulling(trade_prijs_ja, kant_ja, plan):
    """Gaat deze trade door onze order? kant_ja = 'SELL' (taker verkoopt JA, raakt biedingen) of 'BUY'.
    Geeft (welke order, streng) of None. Los: de trade gaat op of door onze prijs; streng: er doorheen."""
    bod, laat = plan
    if kant_ja == "SELL" and bod is not None and trade_prijs_ja <= bod + 1e-9:
        return "bod", trade_prijs_ja < bod - 1e-9
    if kant_ja == "BUY" and laat is not None and trade_prijs_ja >= laat - 1e-9:
        return "laat", trade_prijs_ja > laat + 1e-9
    return None


def zoek_plan(plannen, tts):
    """Minuut van het plan dat gold op tijdstip tts: het laatste plan van vóór tts, hooguit 2 minuten oud
    (de bot meet op een willekeurige seconde, dus een plan geldt tot het volgende)."""
    m = int(tts // 60)
    for kandidaat in (m, m - 1, m - 2):
        p = plannen.get(kandidaat)
        if p and p[0] <= tts and tts - p[0] < 120:
            return kandidaat
    return None


def naar_ja(trade, ja_token):
    """Trade omzetten naar de JA-kant: NEE kopen tegen q is JA verkopen tegen 1 - q."""
    p, kant = float(trade["price"]), trade["side"]
    if trade["token_id"] == ja_token:
        return p, kant
    return 1 - p, ("SELL" if kant == "BUY" else "BUY")


# ---------------------------------------------------------------- opslag

class Opslag:
    """Houdt de ruwe metingen bij en schrijft ze elke flush als nieuwe gzip-CSV-stukjes (nooit overschrijven,
    zodat git elk stukje maar één keer opslaat)."""
    KOLOMMEN = {
        "beloning": ["uur", "markt", "variant", "minuten", "minuten_bod_en_laat", "beloning_hoog", "beloning_laag",
                     "aandeel_hoog_som", "kapitaal_som"],
        "vullingen": ["ts", "markt", "variant", "kant", "prijs", "aantal", "midden", "streng", "trade_prijs",
                      "trade_aantal", "voorraad_na"],
        "midden": ["ts", "markt", "midden", "bod", "laat"],
        "minuut": ["ts", "variant", "markten", "kapitaal", "beloning_hoog", "beloning_laag"],
    }

    def __init__(self, uitmap, run, soort="dag"):
        self.uitmap, self.run, self.stuk, self.soort = uitmap, run, 0, soort
        self.rijen = {k: [] for k in self.KOLOMMEN}
        self.uren = {}          # (uur, markt, variant) -> lijst sommen
        self.markten = {}       # sleutel -> info
        self.van = None

    def uur(self, ts, markt, variant, bod_en_laat, hoog, laag, aandeel, kapitaal):
        k = (dt.datetime.fromtimestamp(ts, UTC).strftime("%Y-%m-%dT%H"), markt, variant)
        r = self.uren.setdefault(k, [0, 0, 0.0, 0.0, 0.0, 0.0])
        r[0] += 1
        r[1] += 1 if bod_en_laat else 0
        r[2] += hoog
        r[3] += laag
        r[4] += aandeel
        r[5] += kapitaal

    def flush(self, tot, git_map=None, laatste=False):
        """Schrijft alles sinds de vorige flush. Geeft de lijst nieuwe bestanden (relatief pad)."""
        for (uur, markt, variant), r in sorted(self.uren.items()):
            self.rijen["beloning"].append([uur, markt, variant, r[0], r[1], round(r[2], 6), round(r[3], 6),
                                          round(r[4], 5), round(r[5], 2)])
        self.uren = {}
        dag = dt.datetime.fromtimestamp(tot, UTC).strftime("%Y-%m-%d")
        naam = f"{self.run}-{self.stuk:03d}"
        nieuw = []
        for soort, kolommen in self.KOLOMMEN.items():
            if not self.rijen[soort]:
                continue
            buf = io.StringIO()
            w = csv.writer(buf, lineterminator="\n")
            w.writerow(kolommen)
            w.writerows(self.rijen[soort])
            pad = f"{self.soort}/{dag}/{soort}-{naam}.csv.gz"
            self._schrijf(pad, gzip.compress(buf.getvalue().encode(), mtime=0))
            nieuw.append(pad)
            self.rijen[soort] = []
        meta = {"run": self.run, "stuk": self.stuk, "van": self.van, "tot": int(tot), "laatste": laatste,
                "instellingen": {"vaste_grootte": VASTE_GROOTTE, "varianten": VARIANTEN,
                                 "max_spread_boek": MAX_SPREAD_BOEK, "max_voorraad": MAX_VOORRAAD},
                "markten": self.markten}
        pad = f"{self.soort}/{dag}/meta-{naam}.json"
        self._schrijf(pad, json.dumps(meta, separators=(",", ":"), ensure_ascii=False).encode())
        nieuw.append(pad)
        self.stuk += 1
        self.van = int(tot)
        if git_map:
            zet_op_tak(git_map, self.uitmap, nieuw)
        return nieuw

    def _schrijf(self, pad, inhoud):
        vol = os.path.join(self.uitmap, pad)
        os.makedirs(os.path.dirname(vol), exist_ok=True)
        with open(vol, "wb") as f:
            f.write(inhoud)


def git(map_, *args, invoer=None, env=None):
    r = subprocess.run(["git", "-C", map_, *args], input=invoer, capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:2])}: {r.stderr.strip()[:300]}")
    return r.stdout.strip()


def zet_op_tak(repo, uitmap, paden, pogingen=5):
    """Nieuwe commit op de tak ai-handel-data met deze bestanden erbij, bovenop de stand van origin.
    Gewone push (nooit geforceerd); lukt hij niet, dan opnieuw ophalen en opnieuw proberen. Zelfde idee als
    organisatie/controle/klok.py. Raakt de werkmap en de index van main niet (eigen GIT_INDEX_FILE)."""
    env = dict(os.environ, GIT_AUTHOR_NAME="dortus-schaduwbot", GIT_COMMITTER_NAME="dortus-schaduwbot",
               GIT_AUTHOR_EMAIL="41898282+github-actions[bot]@users.noreply.github.com",
               GIT_COMMITTER_EMAIL="41898282+github-actions[bot]@users.noreply.github.com")
    blobs = {p: git(repo, "hash-object", "-w", os.path.join(os.path.abspath(uitmap), p)) for p in paden}
    for poging in range(1, pogingen + 1):
        uit = git(repo, "ls-remote", "origin", f"refs/heads/{TAK}")
        tip = uit.split()[0] if uit else None
        with tempfile.TemporaryDirectory() as tmp:
            ienv = dict(env, GIT_INDEX_FILE=os.path.join(tmp, "index"))
            if tip:
                git(repo, "fetch", "-q", "--depth=1", "--filter=blob:none", "origin", f"refs/heads/{TAK}")
                git(repo, "read-tree", tip, env=ienv)
            for p, blob in blobs.items():
                git(repo, "update-index", "--add", "--cacheinfo", f"100644,{blob},{p}", env=ienv)
            boom = git(repo, "write-tree", env=ienv)
        ouder = ["-p", tip] if tip else []
        commit = git(repo, "commit-tree", boom, *ouder, "-m", f"Schaduwbot: {len(paden)} bestanden", env=env)
        r = subprocess.run(["git", "-C", repo, "push", "-q", "origin", f"{commit}:refs/heads/{TAK}"],
                           capture_output=True, text=True)
        if r.returncode == 0:
            log(f"opgeslagen op tak {TAK}: {len(paden)} bestanden ({commit[:8]})")
            return True
        log(f"push naar {TAK} lukte niet (poging {poging}): {r.stderr.strip()[:200]}")
        time.sleep(3 * poging)
    log("LET OP: opslaan op de tak mislukte; bestanden staan nog in de uitmap")
    return False


# ---------------------------------------------------------------- de lus

class Schaduwbot:
    def __init__(self, opslag):
        self.opslag = opslag
        self.markten = {}
        self.voorraad = {}        # (conditie, variant) -> netto JA-aandelen
        self.plannen = {}         # (conditie, variant) -> {minuut: (bod, laat, midden, grootte)}
        self.laatste_midden = {}  # conditie -> (midden, bod, laat) laatst opgeslagen
        self.gezien = {}          # trade-sleutel -> ts
        self.vanaf = int(time.time())
        self.laatste_poll = self.vanaf
        self.tellers = {"minuten": 0, "trades": 0, "vullingen": 0, "fouten": 0}

    def ververs_markten(self):
        nu = dt.datetime.now(UTC)
        self.markten, onbekend = bouw_marktenlijst(nu)
        for m in self.markten.values():
            self.opslag.markten[m["sleutel"]] = {k: m[k] for k in ("conditie", "token", "event", "event_id",
                                                                  "vakje", "aangemaakt", "stop", "dagbedrag",
                                                                  "v", "min")}
        quoten = sum(1 for m in self.markten.values() if nu.timestamp() < m["stop"])
        pot = sum(m["dagbedrag"] for m in self.markten.values() if nu.timestamp() < m["stop"])
        log(f"marktenlijst: {len(self.markten)} gevolgd, {quoten} voor de stop, pot ${pot:,.0f} per dag"
            + (f"; steden zonder tijdzone overgeslagen: {', '.join(onbekend)}" if onbekend else ""))

    def minuut(self):
        ts = time.time()
        minuut = int(ts // 60)
        tokens = [m["token"] for m in self.markten.values()]
        boeken = {}
        for i in range(0, len(tokens), 400):
            for b in vraag(f"{CLOB}/books", [{"token_id": t} for t in tokens[i:i + 400]]) or []:
                boeken[b.get("asset_id")] = b
        totaal = {v: [0, 0.0, 0.0, 0.0] for v in VARIANTEN}
        for c, m in self.markten.items():
            boek = boeken.get(m["token"])
            if not boek:
                continue
            bids, asks = boek_niveaus(boek)
            if not bids or not asks:
                continue
            gewoon = (bids[0][0] + asks[0][0]) / 2
            vorige = self.laatste_midden.get(c)
            if vorige != (gewoon, bids[0][0], asks[0][0]):
                self.opslag.rijen["midden"].append([int(ts), m["sleutel"], round(gewoon, 4), bids[0][0], asks[0][0]])
                self.laatste_midden[c] = (gewoon, bids[0][0], asks[0][0])
            if ts >= m["stop"]:
                continue  # stopregel: middernacht lokale tijd van de dag zelf; daarna alleen het midden volgen
            if asks[0][0] - bids[0][0] > MAX_SPREAD_BOEK + 1e-9:
                continue  # leeg of los boek: niemand weet de prijs (D run 5)
            tick = float(boek.get("tick_size") or 0.01)
            grootte = max(VASTE_GROOTTE, m["min"])
            midden = aangepast_midden(bids, asks, m["min"])
            anderen_hoog, anderen_laag = score_anderen(bids, asks, midden, m["v"], m["min"])
            for variant, afstand in VARIANTEN.items():
                k = (c, variant)
                bod, laat = plan_orders(bids, asks, midden, afstand, tick, grootte, self.voorraad.get(k, 0.0))
                self.plannen.setdefault(k, {})[minuut] = (ts, bod, laat, midden, grootte)
                wij = onze_score(bod, laat, midden, m["v"], grootte)
                hoog = wij / (wij + anderen_hoog) if wij > 0 else 0.0
                laag = wij / (wij + anderen_laag) if wij > 0 else 0.0
                per_minuut = m["dagbedrag"] / 1440
                kapitaal = (bod * grootte if bod else 0.0) + ((1 - laat) * grootte if laat else 0.0)
                self.opslag.uur(ts, m["sleutel"], variant, bod is not None and laat is not None,
                                per_minuut * hoog, per_minuut * laag, hoog, kapitaal)
                t = totaal[variant]
                t[0] += 1
                t[1] += kapitaal
                t[2] += per_minuut * hoog
                t[3] += per_minuut * laag
        for variant, t in totaal.items():
            self.opslag.rijen["minuut"].append([int(ts), variant, t[0], round(t[1], 2), round(t[2], 5),
                                                round(t[3], 5)])
        grens = minuut - PLAN_BEWAREN
        for k in list(self.plannen):
            self.plannen[k] = {mi: p for mi, p in self.plannen[k].items() if mi > grens}
            if not self.plannen[k]:
                del self.plannen[k]
        self.tellers["minuten"] += 1
        return totaal

    def trades(self):
        nu = time.time()
        # events waarvan we de laatste 2 uur een plan hadden: trades staan soms even later in de Data API
        events = sorted({self.markten[c]["event_id"] for (c, _v) in self.plannen if c in self.markten})
        per_conditie = {}
        for i in range(0, len(events), 20):
            groep = ",".join(events[i:i + 20])
            cursor, pagina = None, 0
            while pagina < 20:
                url = f"{DATA}/v2/trades?event_id={groep}&limit=1000" + (f"&cursor={cursor}" if cursor else "")
                d = vraag(url)
                rijen = d.get("data") or []
                oudste = None
                for t in rijen:
                    tts = int(t.get("timestamp") or 0)
                    oudste = tts if oudste is None else min(oudste, tts)
                    sleutel = (t.get("transaction_hash"), t.get("token_id"), t.get("price"), t.get("size"),
                               t.get("proxy_wallet"), t.get("side"))
                    if tts < self.vanaf or sleutel in self.gezien:
                        continue
                    self.gezien[sleutel] = tts
                    per_conditie.setdefault(t.get("condition_id"), []).append(t)
                cursor = (d.get("pagination") or {}).get("next_cursor")
                pagina += 1
                if not cursor or oudste is None or oudste < max(self.vanaf, self.laatste_poll - 600):
                    break
        self.laatste_poll = int(nu)
        grens = nu - (PLAN_BEWAREN + 30) * 60
        self.gezien = {k: v for k, v in self.gezien.items() if v > grens}
        nieuw = 0
        for c, lijst in per_conditie.items():
            m = self.markten.get(c)
            if not m:
                continue
            for t in sorted(lijst, key=lambda x: int(x["timestamp"])):
                self.tellers["trades"] += 1
                prijs, kant = naar_ja(t, m["token"])
                tts = int(t["timestamp"])
                for variant in VARIANTEN:
                    k = (c, variant)
                    welke_minuut = zoek_plan(self.plannen.get(k, {}), tts)
                    if welke_minuut is None:
                        continue
                    _pts, bod, laat, midden, grootte = self.plannen[k][welke_minuut]
                    raak = vulling(prijs, kant, (bod, laat))
                    if not raak:
                        continue
                    welke, streng = raak
                    aantal = min(grootte, float(t["size"]))
                    v = self.voorraad.get(k, 0.0) + (aantal if welke == "bod" else -aantal)
                    self.voorraad[k] = v
                    # deze order is op voor de rest van de minuut; de bot zet hem pas de volgende minuut terug
                    self.plannen[k][welke_minuut] = (_pts, None if welke == "bod" else bod,
                                                     None if welke == "laat" else laat, midden, grootte)
                    self.opslag.rijen["vullingen"].append([tts, m["sleutel"], variant, welke,
                                                           bod if welke == "bod" else laat, aantal, round(midden, 4),
                                                           int(streng), round(prijs, 4), float(t["size"]),
                                                           round(v, 2)])
                    nieuw += 1
        self.tellers["vullingen"] += nieuw
        return nieuw


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--duur", type=float, default=345, help="minuten draaien (standaard 345 = 5 uur 45)")
    ap.add_argument("--uit", default="uit", help="map voor de ruwe metingen")
    ap.add_argument("--git", nargs="?", const=".", default=None,
                    help="ook opslaan op de tak ai-handel-data, vanuit deze git-map (standaard .)")
    ap.add_argument("--flush", type=float, default=30, help="minuten tussen het wegschrijven")
    ap.add_argument("--soort", choices=["dag", "proef"], default="dag",
                    help="bovenmap: dag (echte meting) of proef (korte test, telt niet mee in het rapport)")
    a = ap.parse_args()
    run = os.environ.get("GITHUB_RUN_ID") or f"lokaal{int(time.time())}"
    opslag = Opslag(a.uit, run, a.soort)
    bot = Schaduwbot(opslag)
    opslag.van = bot.vanaf
    begin = time.time()
    einde = begin + a.duur * 60
    volgende_lijst = 0.0
    volgende_flush = begin + a.flush * 60
    log(f"schaduwbot start: run {run}, {a.duur:.0f} minuten, varianten {VARIANTEN}, grootte {VASTE_GROOTTE}+")
    while time.time() < einde:
        try:
            if time.time() >= volgende_lijst:
                bot.ververs_markten()
                volgende_lijst = time.time() + 600
            # op een willekeurige seconde in de minuut, zoals Polymarket zelf meet
            nu = time.time()
            doel = (nu // 60 + 1) * 60 + random.uniform(0, 50)
            if bot.tellers["minuten"] == 0:
                doel = nu
            time.sleep(max(0.0, min(doel, einde) - time.time()))
            if time.time() >= einde:
                break
            totaal = bot.minuut()
            n = bot.trades()
            t = totaal.get("1c", [0, 0, 0, 0])
            log(f"minuut {bot.tellers['minuten']}: {t[0]} markten gequote (1c), kapitaal ${t[1]:,.0f}, "
                f"beloning deze minuut ${t[3]:.3f} tot ${t[2]:.3f}; {n} nieuwe vullingen")
        except Exception as e:  # één mislukte minuut mag de meting niet stoppen
            bot.tellers["fouten"] += 1
            log(f"fout (gaat door): {type(e).__name__}: {str(e)[:200]}")
            time.sleep(10)
        if time.time() >= volgende_flush:
            try:
                opslag.flush(time.time(), a.git)
            except Exception as e:
                log(f"fout bij wegschrijven (gaat door): {e}")
            volgende_flush = time.time() + a.flush * 60
    try:  # trades staan soms 1 tot 2 minuten later in de Data API: nog één keer ophalen voor het einde
        time.sleep(90)
        bot.trades()
    except Exception as e:
        log(f"fout bij de laatste trades (gaat door): {e}")
    opslag.flush(time.time(), a.git, laatste=True)
    log(f"klaar: {bot.tellers}")
    return 0 if bot.tellers["minuten"] > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
