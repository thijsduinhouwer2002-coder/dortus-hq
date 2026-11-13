# Vera 13 nov 2026: steekproef Snapchat-lenzen.
# Gebruik: python3 -I snap-lenzen-steekproef-script.py <map met ids-*.txt> <aantal> <uit.jsonl>
# Leest willekeurige lenspagina's uit de sitemap (www.snapchat.com/lens/sitemap-N.xml,
# robots.txt staat Claude-User toe) en daarna het openbare profiel van de maker:
# volgers (subscriberCount), aanmaakdatum profiel, lenzen met lastUpdatedEpoch.
# Rustig: 2 tegelijk, pauze tussen verzoeken.
import sys, re, json, random, glob, time, subprocess
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (compatible; Claude-User; Dortus onderzoek)"

def haal(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                           capture_output=True, timeout=40)
        s = r.stdout.decode("utf-8", "replace")
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', s, re.S)
        return json.loads(m.group(1))["props"]["pageProps"] if m else None
    except Exception:
        return None

def een(url):
    time.sleep(random.uniform(0.5, 1.5))
    pp = haal(url)
    if not pp:
        return {"lens": url, "fout": "lens"}
    li = pp.get("lensDisplayInfo") or {}
    uit = {"lens": url, "naam": li.get("lensName"), "maker": li.get("lensCreatorUsername"),
           "officieel": li.get("isOfficialSnapLens"), "lensId": li.get("lensId")}
    if not uit["maker"]:
        return uit
    time.sleep(random.uniform(0.5, 1.5))
    pr = haal("https://www.snapchat.com/@" + uit["maker"])
    if not pr:
        uit["fout"] = "profiel"
        return uit
    info = (pr.get("userProfile") or {}).get("publicProfileInfo") or {}
    ct = info.get("creationTimestampMs") or {}
    uit["volgers"] = info.get("subscriberCount")
    uit["profiel_sinds"] = ct.get("value") if isinstance(ct, dict) else None
    lz = pr.get("lenses") or []
    uit["lenzen_op_profiel"] = len(lz)
    uit["meer_lenzen"] = bool(pr.get("lensCursor"))
    uit["lens_epochs"] = [l.get("lastUpdatedEpoch") for l in lz]
    return uit

def main():
    ids = []
    for f in sorted(glob.glob(sys.argv[1] + "/ids-*.txt")):
        ids += open(f).read().split()
    ids = sorted(set(ids))
    random.seed(13112026)
    keuze = random.sample(ids, int(sys.argv[2]))
    with open(sys.argv[3], "w") as out, ThreadPoolExecutor(2) as ex:
        for r in ex.map(een, keuze):
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
            out.flush()

main()
