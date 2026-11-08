#!/usr/bin/env python3
"""Analyse van tiktokshop-apps-meet.py. Gebruik: python3 -I data/tiktokshop-apps-analyse.py <bestand.json>
De aanmaakdatum komt uit service_id (TikTok-id: de bovenste 32 bits zijn unix-seconden)."""
import json, sys, datetime, collections as C
D = json.load(open(sys.argv[1])); apps = D["apps"]
def maand(a): return datetime.datetime.fromtimestamp(int(a["service_id"]) >> 32, datetime.timezone.utc).strftime("%Y-%m")
print(D["regio"], "apps", len(apps))
pj = C.Counter(maand(a)[:4] for a in apps); print("per jaar", sorted(pj.items()))
pm = C.Counter(maand(a) for a in apps); print("per maand", sorted(pm.items())[-18:])
def cat(a):
    l = (a.get("extra") or {}).get("fe_category_list") or []
    l2 = [c["en_name"] for c in l if c.get("level") == 2]; l3 = [c["en_name"] for c in l if c.get("level") == 3]
    return (l2[0] if l2 else "-"), (l3[0] if l3 else "-")
pr = C.Counter(); prijzen = []
for a in apps:
    p = a.get("price_info") or {}
    pr[(p.get("price_type"), p.get("paid_per"))] += 1
    if (p.get("start_price") or -1) > 0: prijzen.append(p["start_price"])
print("prijssoort (price_type, paid_per)", pr.most_common())
prijzen.sort(); n = len(prijzen)
if n: print("met prijs", n, "mediaan vanaf", prijzen[n//2], "p25", prijzen[n//4], "p75", prijzen[3*n//4])
print("proef", sum(1 for a in apps if (a.get("price_info") or {}).get("is_free_trial")))
pa = C.Counter(a.get("partner_name") for a in apps); print("makers", len(pa), pa.most_common(8))
c2 = C.Counter(cat(a)[0] for a in apps); c3 = C.Counter(cat(a) for a in apps)
nieuw = C.Counter(cat(a) for a in apps if maand(a) >= "2026-01")
print("\ncategorie (niveau 2 / 3): totaal, nieuw in 2026")
for k, v in sorted(c3.items(), key=lambda x: (-c2[x[0][0]], -x[1])): print(f"  {k[0][:28]:28} | {k[1][:34]:34} {v:4} {nieuw[k]:4}")
print("\neerste 15 in de standaardvolgorde (sort 3):")
for i, a in enumerate(apps[:15]): print(i+1, a["service_name"][:45], "|", a.get("partner_name","")[:25], "|", maand(a), "|", cat(a)[1])
