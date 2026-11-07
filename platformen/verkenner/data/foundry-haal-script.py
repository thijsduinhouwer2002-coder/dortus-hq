# Haalt alle modules uit de Forge Bazaar (open API, geen sleutel) en bewaart de velden die we nodig hebben.
# "installs" is het percentage Forge-gebruikers dat de module heeft; stap 0,00136% = 1 gebruiker (±73.500 gebruikers).
import json, subprocess, datetime
url = "https://forge-vtt.com/api/bazaar/modules"
d = json.loads(subprocess.run(["curl", "-s", url], capture_output=True, check=True).stdout)["packages"]
keep = ["id", "title", "authors", "url", "installs", "firstPublishAt", "created", "updated", "tags"]
out = [{k: p.get(k) for k in keep} for p in d]
dag = datetime.date.today().isoformat()
json.dump(out, open(f"foundry-forge-modules-{dag}.json", "w"), ensure_ascii=False)
print(len(out), "modules")
