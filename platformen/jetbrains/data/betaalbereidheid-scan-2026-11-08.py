# Betaalbereidheid-scan 8 nov 2026. Alleen lezen via de openbare Marketplace-API, met curl.
# Stap 1: alle PAID en FREEMIUM plugins via /api/searchPlugins (max=20 per pagina).
# Stap 2: per plugin /updates (eerste 100 versies, nieuwste eerst) en /rating.
# Uitvoer: betaalbereidheid-scan-2026-11-08.tsv (ruwe lijst) en alle.json (kladmap).
import json, subprocess, sys, time, datetime, concurrent.futures as cf

BASE = "https://plugins.jetbrains.com"
NOW = datetime.date(2026, 11, 8)

def get(path):
    for _ in range(3):
        r = subprocess.run(["curl", "-sL", "--max-time", "30", BASE + path], capture_output=True, text=True)
        try:
            return json.loads(r.stdout)
        except Exception:
            time.sleep(1)
    return None

def d(ms):
    return datetime.datetime.utcfromtimestamp(int(ms) / 1000).date()

def buildnum(s):
    # "263.*" -> 263.999 ; "" -> 9999 (open)
    if not s:
        return 9999
    p = s.split(".")
    try:
        major = int(p[0])
    except ValueError:
        return 0
    return major + (0.999 if len(p) > 1 and p[1] == "*" else 0)

def lijst():
    out = {}
    for model in ("PAID", "FREEMIUM"):
        off = 0
        while True:
            r = get(f"/api/searchPlugins?max=20&offset={off}&pricingModels={model}&orderBy=downloads")
            ps = (r or {}).get("plugins", [])
            for p in ps:
                out[p["id"]] = p
            if len(ps) < 20:
                break
            off += 20
            time.sleep(0.1)
    return list(out.values())

def detail(p):
    pid = p["id"]
    ups = get(f"/api/plugins/{pid}/updates?page=1&size=100") or []
    time.sleep(0.05)
    rat = get(f"/api/plugins/{pid}/rating") or {}
    time.sleep(0.05)
    ups = [u for u in ups if isinstance(u, dict) and u.get("cdate")]
    ups.sort(key=lambda u: int(u["cdate"]), reverse=True)
    last = ups[0] if ups else {}
    maxuntil = max((buildnum(u.get("until", "")) for u in ups), default=0)
    r90 = sum(u.get("downloads", 0) for u in ups if (NOW - d(u["cdate"])).days <= 90)
    r365 = sum(u.get("downloads", 0) for u in ups if (NOW - d(u["cdate"])).days <= 365)
    votes = rat.get("votes", {}) or {}
    nvotes = sum(votes.values())
    avg = round(sum(int(k) * v for k, v in votes.items()) / nvotes, 2) if nvotes else ""
    low = votes.get("1", 0) + votes.get("2", 0)
    return {
        "id": pid, "naam": p["name"], "model": p.get("pricingModel"), "downloads": p.get("downloads"),
        "tags": ",".join(t for t in p.get("tags", []) if t != "Paid"),
        "maker": (p.get("vendor") or {}).get("name", ""),
        "versies_gezien": len(ups),
        "laatste_versie": last.get("version", ""), "laatste_datum": str(d(last["cdate"])) if last else "",
        "laatste_until": last.get("until", ""), "max_until": maxuntil,
        "werkt_262": maxuntil >= 262, "werkt_263": maxuntil >= 263,
        "dl_versies_90d": r90, "dl_versies_365d": r365,
        "sterren_stemmen": nvotes, "sterren_gem": avg, "stemmen_1_2": low,
        "votes": json.dumps(votes), "preview": (p.get("preview") or "").replace("\t", " ").replace("\n", " ")[:160],
    }

if __name__ == "__main__":
    outdir = sys.argv[1]
    ps = lijst()
    print("plugins", len(ps), file=sys.stderr)
    with cf.ThreadPoolExecutor(3) as ex:
        rows = list(ex.map(detail, ps))
    json.dump(rows, open(f"{outdir}/alle.json", "w"))
    cols = list(rows[0].keys())
    with open(f"{outdir}/betaalbereidheid-scan-2026-11-08.tsv", "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in sorted(rows, key=lambda r: -r["dl_versies_90d"]):
            f.write("\t".join(str(r[c]) for c in cols) + "\n")
