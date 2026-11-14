# Haalt alle Railway-templates op via de open GraphQL-API (geen sleutel nodig).
# Gebruik: python3 -I railway-templates-haal-script.py uit.jsonl
import json, sys, time, urllib.request
URL = "https://backboard.railway.com/graphql/v2"
Q = """query($after:String){ templates(first:100, after:$after){ pageInfo{ hasNextPage endCursor }
 edges{ node{ id code name category createdAt updatedAt projects recentProjects activeProjects health
 totalPayout isVerified isApproved status workspaceId tags languages
 creator{ name username hasPublicProfile } maintainer{ name } } } } }"""
def post(after):
    body = json.dumps({"query": Q, "variables": {"after": after}}).encode()
    for poging in range(5):
        try:
            req = urllib.request.Request(URL, body, {"content-type": "application/json", "user-agent": "dortus-verkenner"})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            print("fout", e, file=sys.stderr); time.sleep(10 * (poging + 1))
    raise SystemExit("opgegeven")
uit = open(sys.argv[1], "w"); after = None; n = 0
while True:
    d = post(after)
    if "errors" in d: print(d["errors"], file=sys.stderr)
    t = d["data"]["templates"]
    for e in t["edges"]:
        uit.write(json.dumps(e["node"]) + "\n"); n += 1
    if not t["pageInfo"]["hasNextPage"]: break
    after = t["pageInfo"]["endCursor"]; time.sleep(1)
print("templates:", n)
