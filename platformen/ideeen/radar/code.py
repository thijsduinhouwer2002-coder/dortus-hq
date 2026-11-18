import json, time, urllib.request, urllib.parse
M = {"VS Code Marketplace":"\"vsce publish\"","Open VSX":"\"ovsx publish\"","JetBrains":"publishPlugin","Chrome Web Store":"chrome-webstore-upload",
"Firefox AMO":"\"web-ext sign\"","itch.io":"\"butler push\"","Steam":"steam-deploy","Garmin Connect IQ":"monkeyc","Shopify":"\"shopify app deploy\"",
"WordPress.org":"action-wordpress-plugin-deploy","App Store":"upload_to_app_store","Google Play":"upload-google-play","Microsoft Store":"msstore",
"Snap Store":"action-publish snapcore","HACS":"hacs/action","Thunderstore":"thunderstore","Modrinth":"modrinth","CurseForge":"curseforge"}
res={}
for naam,term in M.items():
    url="https://api.github.com/search/code?"+urllib.parse.urlencode({"q":f"{term} path:.github/workflows","per_page":1})
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"radar"}),timeout=30) as r:
            res[naam]=json.load(r)["total_count"]
    except Exception as e:
        res[naam]=f"fout {e}"
    print(naam,res[naam],flush=True)
    time.sleep(7)
json.dump(res,open("/tmp/radar/code.json","w"))
