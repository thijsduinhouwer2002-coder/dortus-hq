# Telt bronnen (makers) op explore.alt.store per maand van aanmelden. Gebruik: python3 -I data/altstore-explore-meet.py
import json, urllib.request, collections, datetime
alle = []
for o in range(0, 1000, 80):
    with urllib.request.urlopen(f"https://explore.alt.store/api/v1/directory?limit=80&offset={o}&local=true&order=new", timeout=30) as r:
        d = json.load(r)
    if not d: break
    alle += d
per = collections.Counter(a["created_at"][:7] for a in alle)
print("accounts:", len(alle), "datum:", datetime.date.today())
for m in sorted(per): print(m, per[m])
json.dump([{k: a[k] for k in ("username", "created_at", "followers_count", "statuses_count", "last_status_at")} for a in alle],
          open(f"altstore-explore-{datetime.date.today()}.json", "w"), indent=0)
