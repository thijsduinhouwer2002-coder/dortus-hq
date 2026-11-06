# Haalt de openbare gegevens van alle bots op discordbotlist.com (sitemap + API per bot, geen sleutel).
# Gebruik: python3 -I discord-dbl-script.py <slugs.txt> <uitvoer.json>
import json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
slugs = [s.strip() for s in open(sys.argv[1]) if s.strip()]
def get(s):
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request("https://discordbotlist.com/api/v1/bots/"+s, headers={"User-Agent":"dortus-verkenner"}), timeout=30) as r:
                d = json.load(r)
                return {"slug":s,"id":d.get("id") or d.get("client_id"),"name":(d.get("profile") or {}).get("username"),
                        "created_at":d.get("created_at"),"guilds":(d.get("stats") or {}).get("guilds"),
                        "upvotes":d.get("upvotes"),"invites":(d.get("metrics") or {}).get("invites"),
                        "tags":d.get("tags"),"short":d.get("short_description")}
        except urllib.error.HTTPError as e:
            if e.code == 404: return {"slug":s,"fout":404}
            time.sleep(3+5*t)
        except Exception:
            time.sleep(3+5*t)
    return {"slug":s,"fout":"mislukt"}
out = []
with ThreadPoolExecutor(10) as ex:
    for i, r in enumerate(ex.map(get, slugs)):
        out.append(r)
        if i % 1000 == 0: print(i, flush=True)
json.dump(out, open(sys.argv[2], "w"))
print("klaar", len(out))
