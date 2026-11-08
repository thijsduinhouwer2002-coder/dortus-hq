#!/usr/bin/env python3
"""Herhaalmeting Superhuman Go Store (Noor, pionier).
Haalt de openbare Store-pagina op, telt connectors per maker en schrijft
een regel in superhuman-go.csv plus een momentopname superhuman-go-<datum>.json.
Kijkt ook of de hulppagina over betaalde Packs nog "paused" zegt.
Gebruik: python3 superhuman-go-meet.py
"""
import json, re, csv, datetime, os, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (dortus-onderzoek)"}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode()
hier = os.path.dirname(os.path.abspath(__file__))
h = get("https://superhuman.com/store/connectors")
d = json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S).group(1))
items = d["props"]["pageProps"]["requestData"]["extras"]["connectorStore"]["items"]
eigen = sum(1 for i in items if (i.get("supportEmail") or "").endswith(("superhuman.com", "coda.io")))
modes = sorted(set(i.get("distributionMode") for i in items))
a = json.loads(get("https://help.superhuman.com/api/v2/help_center/en-us/articles/46210104500749.json"))["article"]
gepauzeerd = "paused" in a["body"]
vandaag = datetime.date.today().isoformat()
json.dump([{k: i.get(k) for k in ("packId", "name", "makers", "supportEmail", "agentShortDescription", "distributionMode")} for i in items],
          open(os.path.join(hier, f"superhuman-go-{vandaag}.json"), "w"), indent=1, ensure_ascii=False)
pad = os.path.join(hier, "superhuman-go.csv")
nieuw = not os.path.exists(pad)
with open(pad, "a", newline="") as f:
    w = csv.writer(f)
    if nieuw:
        w.writerow(["datum", "connectors", "van_superhuman", "van_anderen", "hoogste_packId", "distributionModes", "betaalde_packs_gepauzeerd", "hulppagina_bijgewerkt"])
    w.writerow([vandaag, len(items), eigen, len(items) - eigen, max(i["packId"] for i in items), "|".join(map(str, modes)), gepauzeerd, a["updated_at"]])
print(f"{vandaag}: {len(items)} connectors, {eigen} van Superhuman, modes {modes}, betaald gepauzeerd: {gepauzeerd}")
if not gepauzeerd:
    print("LET OP: de hulppagina zegt niet meer 'paused'. Lees hem en weeg Superhuman opnieuw.")
