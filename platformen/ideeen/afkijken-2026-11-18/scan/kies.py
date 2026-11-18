import json,time,urllib.request,urllib.parse
TOPICS=["blender-addon","obsidian-plugin","intellij-plugin","vscode-extension","chrome-extension","figma-plugin","raycast-extension",
"wordpress-plugin","shopify-app","godot-game","stream-deck-plugin","hacs","n8n-community-node-package","mcp-server","claude-code-plugin"]
out=[]
for t in TOPICS:
    q=f"topic:{t} pushed:>2025-11-01 stars:>30"
    url="https://api.github.com/search/repositories?"+urllib.parse.urlencode({"q":q,"sort":"stars","order":"desc","per_page":20})
    d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"scan"}),timeout=30))
    for r in d["items"]:
        out.append({"topic":t,"repo":r["full_name"],"sterren":r["stargazers_count"],"forks":r["forks_count"],"issues_open":r["open_issues_count"],
          "licentie":(r.get("license") or {}).get("spdx_id"),"gemaakt":r["created_at"][:10],"push":r["pushed_at"][:10],"homepage":r.get("homepage") or "",
          "beschrijving":(r.get("description") or "")[:200],"branch":r["default_branch"]})
    print(t,len(d["items"]),flush=True); time.sleep(2.3)
json.dump(out,open("/tmp/scan/repos.json","w"),indent=1); print("totaal",len(out))
