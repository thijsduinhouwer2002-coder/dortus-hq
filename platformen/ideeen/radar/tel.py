import json, time, urllib.request, urllib.parse, sys, os
TOPICS = """vscode-extension jetbrains-plugin intellij-plugin obsidian-plugin raycast-extension chrome-extension firefox-addon
figma-plugin blender-addon connectiq garmin-connect-iq hacs mcp-server claude-skills agent-skills claude-code-plugin
gemini-cli-extension openai-apps-sdk chatgpt-app telegram-mini-app farcaster bluesky roblox godot-plugin godot-addon
fabric-mod decky-plugin logseq-plugin zed-extension visionos meta-quest shopify-app wordpress-plugin stream-deck-plugin
n8n-community-node-package comfyui comfyui-nodes watchos pinescript minecraft-plugin""".split()
Q = [("2025Q1","2025-01-01","2025-03-31"),("2025Q2","2025-04-01","2025-06-30"),("2025Q3","2025-07-01","2025-09-30"),
     ("2025Q4","2025-10-01","2025-12-31"),("2026Q1","2026-01-01","2026-03-31"),("2026Q2","2026-04-01","2026-06-30"),
     ("2026Q3","2026-07-01","2026-09-30"),("2026Q4","2026-10-01","2026-11-17")]
out = "/tmp/radar/tellingen.json"
data = json.load(open(out)) if os.path.exists(out) else {}
for t in TOPICS:
    for q, a, b in Q:
        key = f"{t}|{q}"
        if key in data: continue
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": f"topic:{t} created:{a}..{b}", "per_page": 1})
        for poging in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept":"application/vnd.github+json","User-Agent":"radar"}), timeout=30) as r:
                    data[key] = json.load(r)["total_count"]; break
            except Exception as e:
                time.sleep(20)
        json.dump(data, open(out, "w"))
        time.sleep(2.2)
print("klaar", len(data))
