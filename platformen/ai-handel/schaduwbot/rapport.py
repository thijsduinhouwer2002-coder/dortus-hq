#!/usr/bin/env python3
"""Rapport van de schaduwbot: geschatte beloning, verlies op vullingen, netto, per dag, per markt en in totaal.

Gebruik:
  python3 rapport.py <datamap>             # map met dag/<datum>/... (zoals de uitmap van schaduwbot.py)
  python3 rapport.py --tak                 # haalt de tak ai-handel-data op uit deze git-repo
  python3 rapport.py --tak --schrijf rapport.md
Opties: --koers 1.0 (dollar per euro), --dagen 90, --inleg 2000,5000, --geen-uitslag (niets ophalen).

Labels: GEZIEN = zelf gemeten uit openbare data (trades, boeken). GOK = schatting (de beloning is een schatting
met de formule van Polymarket en twee grenzen voor de concurrentie; alles wat naar dagen of maanden is opgeschaald).
Alleen standaardbibliotheek. Leest alleen; plaatst niets.
"""
import argparse
import bisect
import csv
import glob
import gzip
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from collections import defaultdict

GAMMA = "https://gamma-api.polymarket.com"
KOPPEN = {"User-Agent": "Mozilla/5.0 (schaduwbot-rapport, alleen lezen)", "Accept-Encoding": "gzip"}


def lees_csv(pad):
    with gzip.open(pad, "rt", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_van(pad):
    naam = os.path.basename(pad)
    return naam.split("-", 1)[1].rsplit("-", 1)[0]


def laad(map_, soort="dag"):
    bovenmap = soort
    d = {"markten": {}, "runs": {}, "beloning": [], "minuut": [], "vullingen": [], "midden": defaultdict(list)}
    for pad in sorted(glob.glob(os.path.join(map_, soort, "*", "meta-*.json"))):
        with open(pad, encoding="utf-8") as f:
            meta = json.load(f)
        d["markten"].update(meta.get("markten") or {})
        r = d["runs"].setdefault(str(meta["run"]), [meta["van"], meta["tot"]])
        r[0], r[1] = min(r[0], meta["van"]), max(r[1], meta["tot"])
    for soort in ("beloning", "minuut", "vullingen"):
        for pad in sorted(glob.glob(os.path.join(map_, bovenmap, "*", f"{soort}-*.csv.gz"))):
            for rij in lees_csv(pad):
                rij["run"] = run_van(pad)
                d[soort].append(rij)
    for pad in sorted(glob.glob(os.path.join(map_, bovenmap, "*", "midden-*.csv.gz"))):
        run = run_van(pad)
        for rij in lees_csv(pad):
            d["midden"][(run, rij["markt"])].append((int(rij["ts"]), float(rij["midden"])))
    for k in d["midden"]:
        d["midden"][k].sort()
    return d


def midden_op(d, markt, t):
    """Gemeten midden op tijdstip t, of None als er toen geen run liep. Alleen binnen dezelfde run vooruit
    invullen (het midden wordt alleen opgeslagen als het verandert)."""
    for run, (van, tot) in d["runs"].items():
        if van <= t <= tot:
            reeks = d["midden"].get((run, markt)) or []
            i = bisect.bisect_right(reeks, (t, 2.0)) - 1
            if i >= 0:
                return reeks[i][1]
    return None


def haal_uitslagen(d, sleutels):
    """markt-sleutel -> 1.0 of 0.0 voor JA, als de markt beslist is. Eén verzoek per event (Gamma, openbaar)."""
    events = sorted({d["markten"][s]["event"] for s in sleutels if s in d["markten"]})
    uit = {}
    for slug in events:
        try:
            r = urllib.request.urlopen(urllib.request.Request(f"{GAMMA}/events?slug={slug}", headers=KOPPEN),
                                       timeout=30)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            for e in json.loads(b):
                for m in e.get("markets") or []:
                    prijzen = json.loads(m.get("outcomePrices") or "[]")
                    if m.get("closed") and prijzen and prijzen[0] in ("0", "1"):
                        uit[m["conditionId"][2:12]] = float(prijzen[0])
        except Exception as ex:  # zonder uitslag gaat het rapport door, met minder cijfers
            print(f"(uitslag {slug} niet opgehaald: {ex})", file=sys.stderr)
    return uit


def dag_van(ts):
    import datetime as dt
    return dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).strftime("%Y-%m-%d")


def geld(x):
    return f"${x:,.2f}" if abs(x) < 100 else f"${x:,.0f}"


def maak(d, uitslag, koers, dagen, inlegs):
    regels = []
    w = regels.append
    varianten = sorted({r["variant"] for r in d["minuut"]})
    # --- per dag en variant: gemeten minuten, kapitaal, beloning
    dagen_map = defaultdict(lambda: {"min": set(), "kap": 0.0, "hoog": 0.0, "laag": 0.0, "markten": 0})
    for r in d["minuut"]:
        k = (dag_van(r["ts"]), r["variant"])
        x = dagen_map[k]
        x["min"].add(int(r["ts"]) // 60)
        x["kap"] += float(r["kapitaal"])
        x["hoog"] += float(r["beloning_hoog"])
        x["laag"] += float(r["beloning_laag"])
        x["markten"] += int(r["markten"])
    # --- vullingen met verlies tegen 1 uur later en tegen de uitslag
    vul = []
    for r in d["vullingen"]:
        ts, prijs, aantal = int(r["ts"]), float(r["prijs"]), float(r["aantal"])
        teken = 1 if r["kant"] == "bod" else -1      # bod: we kochten JA; laat: we verkochten JA
        later = midden_op(d, r["markt"], ts + 3600)
        vijf = midden_op(d, r["markt"], ts + 300)
        u = uitslag.get(r["markt"])
        vul.append({**r, "ts": ts, "dag": dag_van(ts), "geld": prijs * aantal,
                    "uur": teken * aantal * (later - prijs) if later is not None else None,
                    "vijf": teken * aantal * (vijf - prijs) if vijf is not None else None,
                    "uitslag": teken * aantal * (u - prijs) if u is not None else None,
                    "streng": r["streng"] == "1"})

    w("# Schaduwbot Polymarket: rapport")
    w("")
    w("Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. "
      "Beloning = GOK (formule van Polymarket, twee grenzen voor de concurrentie: laag en hoog). "
      "Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.")
    w("")
    runs = d["runs"]
    if runs:
        totaal_min = sum(len(x["min"]) for (dg, v), x in dagen_map.items() if v == varianten[0]) if varianten else 0
        w(f"Gemeten: {len(runs)} runs, {totaal_min} minuten ({totaal_min / 60:.1f} uur) (GEZIEN). "
          f"Markten in de data: {len(d['markten'])}. Uitslag bekend voor {len(uitslag)} markten.")
        w("")

    for v in varianten:
        w(f"## Variant {v} (orders op {v.rstrip('c')} cent van het midden)")
        w("")
        w("| Dag (UTC) | Minuten gemeten | Markten gem. | Kapitaal gem. | Beloning laag tot hoog (GOK) | "
          "Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | "
          "Netto (laag tot hoog, 1 uur later) |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        tot = defaultdict(float)
        alle_dagen = sorted({dg for (dg, vv) in dagen_map if vv == v} | {f["dag"] for f in vul if f["variant"] == v})
        for dg in alle_dagen:
            x = dagen_map.get((dg, v), {"min": set(), "kap": 0.0, "hoog": 0.0, "laag": 0.0, "markten": 0})
            n_min = len(x["min"]) or 1
            fv = [f for f in vul if f["variant"] == v and f["dag"] == dg]
            uur = sum(f["uur"] for f in fv if f["uur"] is not None)
            zonder = sum(1 for f in fv if f["uur"] is None)
            ui = [f["uitslag"] for f in fv if f["uitslag"] is not None]
            w(f"| {dg} | {len(x['min'])} | {x['markten'] / n_min:.0f} | {geld(x['kap'] / n_min)} | "
              f"{geld(x['laag'])} tot {geld(x['hoog'])} | {len(fv)} / {sum(f['streng'] for f in fv)} | "
              f"{geld(sum(f['geld'] for f in fv))} | {geld(uur)}" + (f" ({zonder} nog zonder prijs)" if zonder else "")
              + f" | {geld(sum(ui))} ({len(ui)} van {len(fv)} beslist) | "
              f"{geld(x['laag'] + uur)} tot {geld(x['hoog'] + uur)} |")
            tot["min"] += len(x["min"])
            tot["kapmin"] += x["kap"]
            tot["laag"] += x["laag"]
            tot["hoog"] += x["hoog"]
            tot["uur"] += uur
            tot["ui"] += sum(ui)
            tot["n"] += len(fv)
            tot["streng"] += sum(f["streng"] for f in fv)
            tot["geld"] += sum(f["geld"] for f in fv)
        n_min = tot["min"] or 1
        w(f"| **Totaal** | {int(tot['min'])} | | {geld(tot['kapmin'] / n_min)} | {geld(tot['laag'])} tot "
          f"{geld(tot['hoog'])} | {int(tot['n'])} / {int(tot['streng'])} | {geld(tot['geld'])} | {geld(tot['uur'])} | "
          f"{geld(tot['ui'])} | {geld(tot['laag'] + tot['uur'])} tot {geld(tot['hoog'] + tot['uur'])} |")
        w("")
        f5 = [f for f in vul if f["variant"] == v and f["vijf"] is not None]
        if f5:
            g5 = sum(f["geld"] for f in f5)
            w(f"Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): {geld(sum(f['vijf'] for f in f5))} "
              f"over {len(f5)} vullingen en {geld(g5)}, dus {100 * sum(f['vijf'] for f in f5) / g5:+.2f}% per gevulde "
              f"dollar.")
            w("")
        fs = [f for f in vul if f["variant"] == v and f["uur"] is not None]
        if fs:
            g = sum(f["geld"] for f in fs)
            w(f"Verlies per gevulde dollar, 1 uur later: {100 * sum(f['uur'] for f in fs) / g:+.2f}% "
              f"over {geld(g)} (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle "
              f"makers in temperatuurmarkten). Alleen strenge vullingen: "
              + (f"{100 * sum(f['uur'] for f in fs if f['streng']) / max(1e-9, sum(f['geld'] for f in fs if f['streng'])):+.2f}%"
                 if any(f["streng"] for f in fs) else "geen") + ".")
            w("")
        # --- opschalen
        if tot["min"] >= 60:
            k_gem = tot["kapmin"] / n_min
            per_dag_laag = (tot["laag"] + tot["uur"]) / n_min * 1440
            per_dag_hoog = (tot["hoog"] + tot["uur"]) / n_min * 1440
            w(f"**Opgeschaald (GOK):** per dag {geld(per_dag_laag)} tot {geld(per_dag_hoog)} netto met gemiddeld "
              f"{geld(k_gem)} aan orders op het boek (gemeten minuten × 1440 / {int(tot['min'])}).")
            w("")
            w(f"| Inleg | Op de boeken (× {koers} $/€, hooguit wat de bot gebruikte) | Netto over {dagen} dagen (GOK) |")
            w("|---|---|---|")
            for inleg in inlegs:
                eff = min(inleg * koers, k_gem) if k_gem > 0 else 0
                f = eff / k_gem if k_gem > 0 else 0
                w(f"| €{inleg:,} | {geld(eff)} | {geld(per_dag_laag * f * dagen)} tot {geld(per_dag_hoog * f * dagen)} |")
            w("")
            w("Opschalen gaat lineair met het geld op de boeken, en nooit boven wat de bot echt gebruikte: meer geld "
              "in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, "
              "mogelijk) en het verbod in Nederland staan hier niet in; zie README.")
            w("")

    # --- per markt (variant 1c als die er is, anders de eerste)
    if varianten:
        v = "1c" if "1c" in varianten else varianten[0]
        per = defaultdict(lambda: defaultdict(float))
        for r in d["beloning"]:
            if r["variant"] == v:
                p = per[r["markt"]]
                p["min"] += int(r["minuten"])
                p["laag"] += float(r["beloning_laag"])
                p["hoog"] += float(r["beloning_hoog"])
        for f in vul:
            if f["variant"] == v:
                p = per[f["markt"]]
                p["n"] += 1
                p["uur"] += f["uur"] or 0.0
                p["ui"] += f["uitslag"] or 0.0
        def naam(s):
            m = d["markten"].get(s) or {}
            ev = (m.get("event") or s).replace("-temperature-in-", " ").replace("-2026", "")
            return f"{ev} {m.get('vakje', '')}".strip()
        rijen = sorted(per.items(), key=lambda kv: kv[1]["laag"] + kv[1]["uur"])
        w(f"## Per markt (variant {v})")
        w("")
        w("Slechtste 10 en beste 10 op netto (beloning laag plus resultaat 1 uur later).")
        w("")
        w("| Markt | Minuten | Beloning laag tot hoog (GOK) | Vullingen | 1 uur later | Tegen uitslag |")
        w("|---|---|---|---|---|---|")
        keuze = rijen[:10] + ([("...", None)] if len(rijen) > 20 else []) + rijen[-10:] if len(rijen) > 20 else rijen
        for s, p in keuze:
            if p is None:
                w("| ... | | | | | |")
                continue
            w(f"| {naam(s)} | {int(p['min'])} | {geld(p['laag'])} tot {geld(p['hoog'])} | {int(p['n'])} | "
              f"{geld(p['uur'])} | {geld(p['ui'])} |")
        w("")
        # per stad
        stad = defaultdict(lambda: defaultdict(float))
        for s, p in per.items():
            ev = (d["markten"].get(s) or {}).get("event", "")
            sl = ev.split("-temperature-in-")[-1].rsplit("-on-", 1)[0] if ev else "?"
            soort = ev.split("-", 1)[0] if ev else "?"
            for k2, val in p.items():
                stad[f"{sl} ({soort})"][k2] += val
        w(f"## Per stad (variant {v})")
        w("")
        w("| Stad | Beloning laag tot hoog (GOK) | Vullingen | 1 uur later | Netto laag |")
        w("|---|---|---|---|---|")
        for s, p in sorted(stad.items(), key=lambda kv: -(kv[1]["laag"] + kv[1]["uur"])):
            w(f"| {s} | {geld(p['laag'])} tot {geld(p['hoog'])} | {int(p['n'])} | {geld(p['uur'])} | "
              f"{geld(p['laag'] + p['uur'])} |")
        w("")
    w("Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet "
      "openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat "
      "(de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert "
      "iets te laat. Dit is meten, geen advies.")
    return "\n".join(regels) + "\n"


def haal_tak(repo):
    tmp = tempfile.mkdtemp(prefix="schaduwbot-")
    subprocess.run(["git", "-C", repo, "fetch", "-q", "origin", "ai-handel-data"], check=True)
    tar = subprocess.run(["git", "-C", repo, "archive", "FETCH_HEAD"], check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(tar)) as t:
        try:
            t.extractall(tmp, filter="data")
        except TypeError:  # Python ouder dan 3.12
            t.extractall(tmp)
    return tmp


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("map", nargs="?", help="datamap met dag/<datum>/")
    ap.add_argument("--tak", nargs="?", const=".", help="haal de tak ai-handel-data op vanuit deze git-repo")
    ap.add_argument("--schrijf", help="schrijf het rapport ook naar dit bestand")
    ap.add_argument("--koers", type=float, default=1.0, help="dollar per euro (standaard 1,0: GOK, zelf invullen)")
    ap.add_argument("--dagen", type=int, default=90)
    ap.add_argument("--inleg", default="2000,5000")
    ap.add_argument("--geen-uitslag", action="store_true")
    ap.add_argument("--soort", choices=["dag", "proef"], default="dag", help="dag = echte meting, proef = test")
    ap.add_argument("--zet-op-tak", action="store_true",
                    help="met --tak: zet het rapport als <soort>/rapport.md op de tak ai-handel-data")
    a = ap.parse_args()
    map_ = a.map or (haal_tak(a.tak) if a.tak else None)
    if not map_:
        ap.error("geef een datamap of --tak")
    d = laad(map_, a.soort)
    gevuld = {r["markt"] for r in d["vullingen"]}
    uitslag = {} if a.geen_uitslag else haal_uitslagen(d, gevuld)
    tekst = maak(d, uitslag, a.koers, a.dagen, [int(x) for x in a.inleg.split(",") if x.strip()])
    print(tekst)
    if a.schrijf:
        with open(a.schrijf, "w", encoding="utf-8") as f:
            f.write(tekst)
    if a.zet_op_tak and a.tak:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import schaduwbot
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, a.soort))
            with open(os.path.join(tmp, a.soort, "rapport.md"), "w", encoding="utf-8") as f:
                f.write(tekst)
            schaduwbot.zet_op_tak(a.tak, tmp, [f"{a.soort}/rapport.md"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
