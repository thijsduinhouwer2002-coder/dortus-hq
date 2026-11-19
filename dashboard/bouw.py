#!/usr/bin/env python3
"""Dortus-dashboard: de stand per project, de echte cijfers en de ploeg in data.json en index.html.

Draait elk half uur in GitHub Actions (geen Claude, geen tokens). Leest alleen de repo
(organisatie/projecten.json, scorebord, lijst-thijs, bord, git log) en de openbare GitHub-API.
Gebruik: python3 dashboard/bouw.py <uitvoermap>
"""
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dashboard", "uit")
REPO = "thijsduinhouwer2002-coder/dortus-hq"
NU = dt.datetime.now(dt.timezone.utc)
AMS = dt.timezone(dt.timedelta(hours=1))  # wintertijd; zomertijd is +2, klein verschil voor een dashboard


def lees(pad):
    try:
        with open(os.path.join(ROOT, pad), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def haal(url, token=False):
    req = urllib.request.Request(url, headers={"User-Agent": "dortus-dashboard"})
    if token and os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except Exception:  # noqa: BLE001  (geen netwerk: dan zonder dat stuk)
        return None


def schoon(tekst, max_len=220):
    t = re.sub(r"\*\*|`|~~", "", tekst)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip(" -")
    return t if len(t) <= max_len else t[: max_len - 1].rsplit(" ", 1)[0] + "…"


def iso(t):
    return t.astimezone(AMS).isoformat(timespec="minutes")


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True).stdout.strip()


def repo_link(pad):
    if pad.startswith("http"):
        return pad
    soort = "tree" if os.path.isdir(os.path.join(ROOT, pad)) else "blob"
    return f"https://github.com/{REPO}/{soort}/main/{pad}"


config = json.loads(lees("dashboard/ploeg.json") or "{}")
mensen = config.get("mensen", [])


def van_wie(onderwerp, auteur):
    s = onderwerp.lower()
    for p in mensen:
        for k in p["sleutels"]:
            if s.startswith(k.lower()):
                return p["naam"]
    if auteur == "Dortus":
        return "Hoofdchat"
    return None


def commits(*paden, n=None, since=None):
    args = ["log", "--format=%H|%ct|%an|%s"]
    if n:
        args.append(f"-n{n}")
    if since:
        args.append(f"--since={since}")
    if paden:
        args += ["--", *paden]
    uit = []
    for regel in git(*args).splitlines():
        try:
            h, ts, auteur, onderwerp = regel.split("|", 3)
        except ValueError:
            continue
        t = dt.datetime.fromtimestamp(int(ts), dt.timezone.utc)
        wie = van_wie(onderwerp, auteur)
        wat = onderwerp.split(":", 1)[-1] if wie and ":" in onderwerp[:40] else onderwerp
        if not wie and auteur in ("Claude", "github-actions[bot]"):
            auteur = "Ploeg" if auteur == "Claude" else "Workflow"
        uit.append({"hash": h[:7], "t": t, "tijd": iso(t), "wie": wie or auteur, "wat": schoon(wat, 170)})
    return uit


# ---------- scorebord: waarde, bron en reeks per sleutel ----------
scorebord_md = lees("organisatie/scorebord.md")
m = re.search(r"Gemeten op (\d{4}-\d{2}-\d{2}) om (\d{2}:\d{2}) UTC", scorebord_md)
gemeten = f"{m.group(1)}T{m.group(2)}+00:00" if m else None
rijen = {}
for r in scorebord_md.splitlines():
    if not r.startswith("| ") or r.startswith("| Product") or r.startswith("|---"):
        continue
    d = [c.strip() for c in r.strip().strip("|").split("|")]
    if len(d) == 9:
        rijen[f"{d[0]}|{d[1]}|{d[2]}"] = {"vandaag": d[3], "gisteren": d[4], "stand": d[7], "bron": d[8]}

reeksen = {}
try:
    with open(os.path.join(ROOT, "organisatie/scorebord-data.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                w = float(r["waarde"])
            except (TypeError, ValueError):
                continue
            reeksen.setdefault(f"{r['product']}|{r['platform']}|{r['maat']}", {})[r["datum"]] = w
except OSError:
    pass


def cijfer(sleutel):
    product, platform, maat = (sleutel.split("|") + ["", "", ""])[:3]
    rij = rijen.get(sleutel, {})
    reeks = sorted(reeksen.get(sleutel, {}).items())
    vandaag = rij.get("vandaag") or (f"{reeks[-1][1]:g}" if reeks else "?")
    bron = rij.get("bron", "")
    label = bron.split(",")[0].strip() if bron.split(",")[0].strip() in ("GEZIEN", "DERDEN", "GOK") else "GEZIEN"
    toon_maat = "bezoekers per dag" if (platform, maat) == ("dortus.com", "pagina") else maat
    return {"sleutel": sleutel, "product": product, "platform": platform, "maat": toon_maat,
            "waarde": vandaag, "gisteren": rij.get("gisteren", ""), "stand": rij.get("stand", ""),
            "bron": re.sub(r"^(GEZIEN|DERDEN|GOK),\s*", "", bron) or ("bezoekers per dag op deze pagina van dortus.com (Amami), uit scorebord-data.csv" if platform == "dortus.com" else "organisatie/scorebord-data.csv"),
            "label": label, "gemeten": gemeten if rij else (reeks[-1][0] if reeks else None),
            "reeks": [[d, w] for d, w in reeks]}


# ---------- keuringen: kop en laatste "Akkoord:" ----------
def keuring(pad):
    tekst = lees(pad)
    if not tekst:
        return None
    kop, akkoord, kop_akkoord = "", "", ""
    laatste_kop = ""
    for r in tekst.splitlines():
        if r.startswith("#"):
            laatste_kop = r.lstrip("# ").strip()
            kop = kop or laatste_kop
        if r.lower().startswith("akkoord:") or r.lower().startswith("**akkoord"):
            akkoord, kop_akkoord = r, laatste_kop
    ts = git("log", "-1", "--format=%ct", "--", pad)
    oordeel = "ja" if re.match(r"\W*akkoord\W*\s*\**ja", akkoord, re.I) else ("nee" if re.match(r"\W*akkoord\W*\s*\**nee", akkoord, re.I) else "")
    return {"pad": pad, "link": repo_link(pad), "kop": schoon(kop_akkoord or kop, 140),
            "akkoord": schoon(re.sub(r"^\**akkoord\**:\**\s*(?:\**(?:ja|nee)\**[,.:]?\s*)?", "", akkoord, flags=re.I), 260),
            "oordeel": oordeel,
            "tijd": iso(dt.datetime.fromtimestamp(int(ts), dt.timezone.utc)) if ts else None}


# ---------- projecten ----------
pj = json.loads(lees("organisatie/projecten.json") or '{"projecten": []}')


def midden(v):
    if isinstance(v, list) and len(v) == 2:
        return (v[0] + v[1]) / 2
    return v if isinstance(v, (int, float)) else None


def volgorde(p):
    if p.get("voor") == "Thijs-zelf":
        return (3, 0)
    v = midden((p.get("prognose") or {}).get("verwacht"))
    if v is None:
        hoog = (p.get("prognose") or {}).get("hoog")
        return (1, -(hoog or 0))
    return (0, -v) if v > 0 else (2, 0)


projecten = []
for p in sorted(pj.get("projecten", []), key=volgorde):
    p = dict(p)
    p["links"] = [{"naam": l["naam"], "url": repo_link(l["url"])} for l in p.get("links", [])]
    p["cijfers"] = [cijfer(s) for s in p.get("cijfers", [])]
    p["keuringen"] = [k for k in (keuring(x) for x in p.get("keuringen", [])) if k]
    gezien, recent = set(), []
    for c in commits(*p.get("mappen", []), n=12) if p.get("mappen") else []:
        if c["hash"] in gezien:
            continue
        gezien.add(c["hash"])
        recent.append({k: c[k] for k in ("hash", "tijd", "wie", "wat")})
    p["recent"] = recent[:6]
    for veld in ("kans", "prognose"):
        if p.get(veld) and p[veld].get("bron"):
            p[veld]["bron_link"] = repo_link(p[veld]["bron"])
    projecten.append(p)

# ---------- jij moet doen: lijst-thijs plus projecten ----------
lijst = lees("organisatie/lijst-thijs.md")
nu_deel = lijst.split("## Nu", 1)[-1].split("\n## ", 1)[0] if "## Nu" in lijst else ""
doen = []
for r in nu_deel.splitlines():
    mm = re.match(r"\s*(?:\d+\.|-)\s+(.*)", r)
    if not mm:
        continue
    tekst = mm.group(1)
    if re.search(r"vervallen|afgehandeld|^~~", tekst, re.I):
        continue
    kop = re.match(r"\*\*(.+?)\*\*", tekst)
    titel = schoon(kop.group(1) if kop else tekst, 160)
    klein = bool(re.search(r"mag wachten|klein|later", titel, re.I))
    titel = re.sub(r"^\((?:klein, )?mag wachten\)\s*|^\(klein[^)]*\)\s*", "", titel, flags=re.I)
    titel = re.sub(r",?\s*vóór (?:ma|di|wo|do|vr|za|zo) \d{1,2} \w+\s*$", "", titel)
    doen.append({"titel": titel, "uitleg": schoon(tekst[kop.end():] if kop else "", 200),
                 "bron": "lijst", "klein": klein, "project": None, "voor": None})


def woorden(s):
    return {w for w in re.findall(r"[a-zà-ÿ']{5,}", s.lower())}


for p in projecten:
    t = p.get("thijs")
    if not t or not t.get("doen"):
        continue
    hit = next((d for d in doen if len(woorden(d["titel"]) & woorden(t["doen"])) >= 2), None)
    if hit:
        hit["project"], hit["voor"] = p["id"], t.get("voor")
        continue
    doen.append({"titel": schoon(t["doen"], 160), "uitleg": "", "bron": "project", "klein": False,
                 "project": p["id"], "voor": t.get("voor")})
doen.sort(key=lambda d: (d["klein"], d["voor"] or "9999"))

# ---------- ploeg: bord (aan/uit, focus) plus git log ----------
bord = lees("organisatie/bord.md")
agenten_deel = bord.split("## 2. Agents", 1)[-1].split("\n## ", 1)[0] if "## 2. Agents" in bord else ""
bord_rij = {}
for r in agenten_deel.splitlines():
    if not r.startswith("| ") or r.startswith("| Agent") or r.startswith("|---"):
        continue
    d = [c.strip() for c in r.strip().strip("|").split("|")]
    if len(d) >= 4:
        for naam in re.split(r",\s*", d[0]):
            bord_rij[naam.strip()] = {"aan": d[1].lower().startswith("aan"), "schema": schoon(d[2], 60), "focus": schoon(d[3], 200)}

alle = commits(since="21 days ago")
vandaag_start = NU.astimezone(AMS).replace(hour=0, minute=0, second=0, microsecond=0)
ploeg = []
for p in mensen:
    eigen = [c for c in alle if c["wie"] == p["naam"]]
    laatste = eigen[0] if eigen else None
    b = bord_rij.get(p["naam"], {})
    ploeg.append({
        "naam": p["naam"], "rol": p["rol"], "team": p["team"],
        "aan": b.get("aan", p.get("actief", False)), "schema": b.get("schema") or p.get("schema", ""),
        "focus": b.get("focus") or p.get("focus", ""),
        "projecten": [q["id"] for q in projecten if p["naam"].lower() in [a.lower() for a in q.get("agents", [])] or (q.get("eigenaar") or "").lower() == p["naam"].lower()],
        "vandaag": sum(1 for c in eigen if c["t"] >= vandaag_start),
        "laatst": laatste["tijd"] if laatste else None,
        "laatst_wat": laatste["wat"] if laatste else "",
        "laatst_hash": laatste["hash"] if laatste else "",
    })
ploeg.sort(key=lambda x: (not x["aan"], -(dt.datetime.fromisoformat(x["laatst"]).timestamp() if x["laatst"] else 0)))

feed = [{k: c[k] for k in ("tijd", "wie", "wat", "hash")} for c in alle[:25]]

# ---------- workflows (GitHub Actions) ----------
runs = haal(f"https://api.github.com/repos/{REPO}/actions/runs?per_page=60&branch=main", token=True)
tests = []
if isinstance(runs, dict):
    gezien = set()
    for r in runs.get("workflow_runs", []):
        naam = r.get("name", "")
        if naam in gezien or naam.lower().startswith("dashboard"):
            continue
        gezien.add(naam)
        tests.append({"naam": naam, "uitkomst": r.get("conclusion") or r.get("status"), "tijd": iso(dt.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")))})

# ---------- totaal en deadlines ----------
lo = hi = 0
for p in projecten:
    v = (p.get("prognose") or {}).get("verwacht")
    if p.get("voor") == "Thijs-zelf" or v is None:
        continue
    a, b = (v if isinstance(v, list) else [v, v])
    lo, hi = lo + a, hi + b
zonder = [p["naam"] for p in projecten if p.get("voor") != "Thijs-zelf" and (p.get("prognose") or {}).get("verwacht") is None and not (p.get("prognose") or {}).get("samen")]
vandaag = NU.astimezone(AMS).date().isoformat()
deadlines = sorted(
    [{"datum": p["deadline"]["datum"], "tijd": p["deadline"].get("tijd"), "wat": p["deadline"].get("wat", ""), "project": p["id"], "naam": p["kort"] or p["naam"]}
     for p in projecten if p.get("deadline") and p["deadline"].get("datum", "") >= vandaag],
    key=lambda d: (d["datum"], d.get("tijd") or ""))

data = {
    "gebouwd": iso(NU),
    "projecten_bijgewerkt": pj.get("bijgewerkt", {}),
    "repo": REPO,
    "totaal": {"laag": lo, "hoog": hi, "label": "GOK", "zonder_schatting": zonder},
    "doen": doen,
    "deadlines": deadlines,
    "projecten": projecten,
    "ploeg": ploeg,
    "feed": feed,
    "tests": tests[:12],
    "scorebord_gemeten": gemeten,
}

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

sjabloon = lees("dashboard/sjabloon.html")
pagina = sjabloon.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(pagina)
print(f"dashboard gebouwd: {len(projecten)} projecten, {len(ploeg)} mensen, {len(doen)} punten voor Thijs")
