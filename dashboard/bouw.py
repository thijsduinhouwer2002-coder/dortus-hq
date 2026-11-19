#!/usr/bin/env python3
"""Dortus-dashboard: de stand per project, de echte cijfers en de ploeg in data.json en index.html.

Draait in GitHub Actions bij elke push en elk half uur (geen Claude, geen tokens). Leest alleen de
repo (organisatie/projecten.json, scorebord, lijst-thijs, bord, git log) en de openbare GitHub-API.
Gebruik: python3 dashboard/bouw.py <uitvoermap>
"""
import base64
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "dashboard"))
from controle import controleer  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dashboard", "uit")
REPO = "thijsduinhouwer2002-coder/dortus-hq"
NU = dt.datetime.now(dt.timezone.utc)
AMS = dt.timezone(dt.timedelta(hours=1))  # wintertijd; zomertijd is +2, klein verschil voor een dashboard
RUIS = re.compile(r"niets (zinvols |nieuws )?te doen|^logboek\b|logboek run|stand bij afsluiten|^run \d", re.I)


def lees(pad):
    try:
        with open(os.path.join(ROOT, pad), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def haal(url):
    req = urllib.request.Request(url, headers={"User-Agent": "dortus-dashboard"})
    if os.environ.get("GITHUB_TOKEN"):
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
    soort = "tree" if git("cat-file", "-t", f"HEAD:{pad.rstrip('/')}") == "tree" else "blob"
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


# ---------- projecten.json: eerst controleren ----------
pj, fouten = controleer(lees("organisatie/projecten.json") or "")
for r in fouten:
    print("projecten.json:", r, file=sys.stderr)

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
    vandaag = rij.get("vandaag") or (f"{reeks[-1][1]:g}" if reeks else "")
    gelezen = bool(re.match(r"^-?\d+([.,]\d+)?$", vandaag.strip()))
    bron = rij.get("bron", "")
    label = bron.split(",")[0].strip() if bron.split(",")[0].strip() in ("GEZIEN", "DERDEN", "GOK") else "GEZIEN"
    return {"sleutel": sleutel, "product": product, "platform": platform,
            "maat": "bezoekers per dag" if (platform, maat) == ("dortus.com", "pagina") else maat,
            "waarde": vandaag if gelezen else None, "gisteren": rij.get("gisteren", ""), "stand": rij.get("stand", ""),
            "bron": re.sub(r"^(GEZIEN|DERDEN|GOK),\s*", "", bron) or ("bezoekers per dag op deze pagina van dortus.com (Amami), uit scorebord-data.csv" if platform == "dortus.com" else "organisatie/scorebord-data.csv"),
            "label": label if gelezen else None, "gemeten": gemeten if rij else (reeks[-1][0] if reeks else None),
            "reeks": [[d, w] for d, w in reeks]}


# ---------- keuringen: kop en laatste "Akkoord:" ----------
def keuring(pad):
    tekst = lees(pad)
    if not tekst:
        return None
    kop, akkoord, kop_akkoord, laatste_kop = "", "", "", ""
    for r in tekst.splitlines():
        if r.startswith("#"):
            laatste_kop = r.lstrip("# ").strip()
            kop = kop or laatste_kop
        if r.lower().startswith("akkoord:") or r.lower().startswith("**akkoord"):
            akkoord, kop_akkoord = r, laatste_kop
    ts = git("log", "-1", "--format=%ct", "--", pad)
    oordeel = "ja" if re.match(r"\W*akkoord\W*\s*\**ja", akkoord, re.I) else ("nee" if re.match(r"\W*akkoord\W*\s*\**nee", akkoord, re.I) else "")
    titel = (kop_akkoord or kop).split(",")[0]  # "Keuring X, 19 nov 2026, keurder (...)" wordt "Keuring X"
    return {"pad": pad, "link": repo_link(pad), "kop": schoon(titel, 120),
            "akkoord": schoon(re.sub(r"^\**akkoord\**:\**\s*(?:\**(?:ja|nee)\**[,.:]?\s*)?", "", akkoord, flags=re.I), 240),
            "oordeel": oordeel,
            "tijd": iso(dt.datetime.fromtimestamp(int(ts), dt.timezone.utc)) if ts else None}


# ---------- projecten ----------
def midden(v):
    if isinstance(v, list) and len(v) == 2:
        return (v[0] + v[1]) / 2
    return v if isinstance(v, (int, float)) else None


def volgorde(p):
    if p.get("voor") == "Thijs-zelf":
        return (3, 0)
    g = p.get("prognose") or {}
    v = midden(g.get("verwacht"))
    if v is None:
        return (1, -(g.get("hoog") or 0))
    return (0, -v) if v > 0 else (2, 0)


projecten = []
for p in sorted(pj.get("projecten", []), key=volgorde):
    p = dict(p)
    p["links"] = [{"naam": l.get("naam", "link"), "url": repo_link(l["url"])} for l in p.get("links") or [] if isinstance(l, dict) and l.get("url")]
    p["cijfers"] = [cijfer(s) for s in p.get("cijfers") or [] if isinstance(s, str)]
    p["keuringen"] = [k for k in (keuring(x) for x in p.get("keuringen") or [] if isinstance(x, str)) if k]
    gezien, recent = set(), []
    for c in commits(*p.get("mappen"), n=30) if p.get("mappen") else []:
        if c["hash"] in gezien or RUIS.search(c["wat"]):
            continue
        gezien.add(c["hash"])
        recent.append({k: c[k] for k in ("hash", "tijd", "wie", "wat")})
    p["recent"] = recent[:6]
    for veld in ("kans", "prognose"):
        if p.get(veld) and p[veld].get("bron"):
            p[veld]["bron_link"] = repo_link(p[veld]["bron"])
    projecten.append(p)

# ---------- jij moet doen: lijst-thijs plus de punten uit projecten.json, zonder dubbelingen ----------
lijst = lees("organisatie/lijst-thijs.md")
nu_deel = lijst.split("## Nu", 1)[-1].split("\n## ", 1)[0] if "## Nu" in lijst else ""
MAANDNR = {m: i + 1 for i, m in enumerate(["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"])}
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
    klein = bool(re.search(r"mag wachten|\bklein\b|later", titel, re.I))
    titel = re.sub(r"^\((?:klein, )?mag wachten\)\s*|^\(klein[^)]*\)\s*", "", titel, flags=re.I)
    voor = None
    dm = re.search(r"vóór (?:ma|di|wo|do|vr|za|zo) (\d{1,2}) (\w{3})", tekst)
    if dm and dm.group(2) in MAANDNR:
        voor = f"{NU.year}-{MAANDNR[dm.group(2)]:02d}-{int(dm.group(1)):02d}"
    titel = re.sub(r",?\s*vóór (?:ma|di|wo|do|vr|za|zo) \d{1,2} \w+\s*$", "", titel)
    vm = re.match(r"(?i)^(?:vóór\s+)?(?:ma|di|wo|do|vr|za|zo)\s+(\d{1,2})\s+([a-z]{3})\w*:\s*", titel)
    if vm and vm.group(2).lower() in MAANDNR:
        voor = voor or f"{NU.year}-{MAANDNR[vm.group(2).lower()]:02d}-{int(vm.group(1)):02d}"
        titel = titel[vm.end():]
    elif re.match(r"(?i)^(vandaag|morgen):\s*", titel):
        extra = 1 if titel.lower().startswith("morgen") else 0
        voor = voor or (NU.astimezone(AMS).date() + dt.timedelta(days=extra)).isoformat()
        titel = re.sub(r"(?i)^(vandaag|morgen):\s*", "", titel)
    titel = titel[:1].upper() + titel[1:]
    doen.append({"titel": titel, "bron": "lijst", "klein": klein, "project": None, "voor": voor})


def woorden(s):
    return {w for w in re.findall(r"[a-zà-ÿ']{5,}", s.lower())}


for p in projecten:
    for t in p.get("thijs") or []:
        def zelfde(d):
            n = len(woorden(d["titel"]) & woorden(t["doen"]))
            return n >= 2 or (n >= 1 and d["voor"] and d["voor"] == t.get("voor"))
        hit = next((d for d in doen if zelfde(d)), None)
        if hit:
            hit["project"] = hit["project"] or p["id"]
            hit["voor"] = hit["voor"] or t.get("voor")
            continue
        doen.append({"titel": schoon(t["doen"], 160), "bron": "project", "klein": False, "project": p["id"], "voor": t.get("voor")})
doen.sort(key=lambda d: (d["klein"], d["voor"] or "9999"))

# ---------- ploeg: aan of uit en focus uit het bord, laatste commit uit git log ----------
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
    b = bord_rij.get(p["naam"])
    if p.get("vast"):
        groep = "vast"
    elif b:
        groep = "aan" if b["aan"] else "uit"
    else:  # niet op het bord: alleen "bezig" als er de laatste 3 uur iets van hem op GitHub kwam
        groep = "bezig" if laatste and (NU - laatste["t"]).total_seconds() < 3 * 3600 else "uit"
    ploeg.append({
        "naam": p["naam"], "rol": p["rol"], "team": p["team"], "groep": groep, "op_bord": bool(b),
        "schema": (b or {}).get("schema") or p.get("schema", ""), "focus": (b or {}).get("focus") or p.get("focus", ""),
        "projecten": [q["id"] for q in projecten if p["naam"].lower() in [a.lower() for a in q.get("agents") or []] or (q.get("eigenaar") or "").lower() == p["naam"].lower()],
        "vandaag": sum(1 for c in eigen if c["t"] >= vandaag_start),
        "laatst": laatste["tijd"] if laatste else None,
        "laatst_wat": schoon(laatste["wat"], 110) if laatste else "",
    })
ploeg.sort(key=lambda x: (["aan", "bezig", "vast", "uit"].index(x["groep"]), -(dt.datetime.fromisoformat(x["laatst"]).timestamp() if x["laatst"] else 0)))
feed = [{k: c[k] for k in ("tijd", "wie", "wat", "hash")} for c in alle[:25]]

# ---------- workflows: alleen runs waarin echt werk draaide ----------
# Veel workflows starten bij elke push; de job "klok" beslist dan dat er niets te doen is en de run
# heet toch "success". Daarom per workflow de nieuwste run zoeken waarin een andere job dan de klok
# echt draaide (of iets rood werd).
runs = haal(f"https://api.github.com/repos/{REPO}/actions/runs?per_page=100&branch=main")
tests, budget, klaar = [], 45, set()
if isinstance(runs, dict):
    for r in runs.get("workflow_runs", []):
        naam = r.get("name", "")
        if naam in klaar or naam.lower().startswith(("dashboard", "actions-log")) or r.get("status") != "completed":
            continue
        if r.get("conclusion") in ("failure", "timed_out"):
            klaar.add(naam)
            tests.append({"naam": naam, "uitkomst": "failure", "tijd": iso(dt.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))), "url": r.get("html_url")})
            continue
        if budget <= 0:
            continue
        budget -= 1
        jobs = haal(f"https://api.github.com/repos/{REPO}/actions/runs/{r['id']}/jobs")
        if not isinstance(jobs, dict):
            continue
        werk = [j for j in jobs.get("jobs", []) if j.get("name", "").lower() != "klok" and j.get("conclusion") in ("success", "failure")]
        if werk:
            klaar.add(naam)
            fout = any(j["conclusion"] == "failure" for j in werk)
            tests.append({"naam": naam, "uitkomst": "failure" if fout else "success", "tijd": iso(dt.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))), "url": r.get("html_url")})

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
    [{"datum": p["deadline"]["datum"], "tijd": p["deadline"].get("tijd"), "wat": p["deadline"].get("wat", ""), "project": p["id"], "naam": p.get("kort") or p["naam"]}
     for p in projecten if p.get("voor") != "Thijs-zelf" and p.get("deadline") and p["deadline"]["datum"] >= vandaag],
    key=lambda d: (d["datum"], d.get("tijd") or ""))

bijgewerkt = dict(pj.get("bijgewerkt") or {})
try:
    bijgewerkt["iso"] = dt.datetime.strptime(bijgewerkt.get("datum", ""), "%Y-%m-%d %H:%M").replace(tzinfo=AMS).isoformat(timespec="minutes")
except ValueError:
    bijgewerkt["iso"] = None

data = {
    "gebouwd": iso(NU),
    "projecten_bijgewerkt": bijgewerkt,
    "fouten": fouten,
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


def letter(bestand):
    try:
        with open(os.path.join(ROOT, "dashboard", "letter", bestand), "rb") as f:
            return "data:font/woff;base64," + base64.b64encode(f.read()).decode()
    except OSError:
        return ""


stijl = lees("dashboard/stijl.css").replace("/*LETTER600*/", letter("barlow-condensed-semibold.woff")).replace("/*LETTER500*/", letter("barlow-condensed-medium.woff"))
pagina = (lees("dashboard/sjabloon.html")
          .replace("/*STIJL*/", stijl)
          .replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(pagina)
print(f"dashboard gebouwd: {len(projecten)} projecten, {len(ploeg)} mensen, {len(doen)} punten voor Thijs, {len(fouten)} fouten in projecten.json")
