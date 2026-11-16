# Leest de draadlijst van het Connect IQ Showcase-forum (openbaar, zonder inlog).
# Gebruik: python3 -I garmin-showcase-haal-script.py <paginas> uit.json   (1 pagina per 2 s)
import json, re, subprocess, sys, time, html
n, out = int(sys.argv[1]), sys.argv[2]
rows = {}
for p in range(1, n + 1):
    url = "https://forums.garmin.com/developer/connect-iq/f/showcase" + (f"?pifragment-293={p}" if p > 1 else "")
    t = subprocess.run(["curl", "-sL", "-m", "30", "-A", "Mozilla/5.0", url], capture_output=True, text=True).stdout
    blokken = re.split(r'<li class="content-item with-href', t)[1:]
    for b in blokken:
        tid = re.search(r'data-threadid="(\d+)"', b)
        if not tid: continue
        titel = re.search(r'class="ui-contentpeek internal-link view-post[^"]*"[^>]*>([^<]+)<', b)
        nums = re.findall(r'<span class="value">([\d,]+)</span>\s*<span class="description">\s*(views?|repl(?:y|ies))', b)
        d = {k[:4]: int(v.replace(",", "")) for v, k in nums}
        start = re.search(r'Started <span[^>]*data-dateutc="([^"]+)"', b)
        rows[tid.group(1)] = {"id": int(tid.group(1)), "titel": html.unescape(titel.group(1)).strip() if titel else "",
                              "views": d.get("view"), "replies": d.get("repl"), "gestart": start.group(1) if start else None}
    print(p, len(rows), file=sys.stderr)
    time.sleep(2)
json.dump(sorted(rows.values(), key=lambda r: -r["id"]), open(out, "w"), indent=0)
