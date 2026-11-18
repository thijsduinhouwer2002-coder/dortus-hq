import json,subprocess,re,os,sys
from concurrent.futures import ThreadPoolExecutor
repos=json.load(open("/tmp/scan/repos.json"))
WINKELS={"VS Code Marketplace":r"vsce publish|publish-vscode-extension|@vscode/vsce","Open VSX":r"ovsx|open-vsx","JetBrains":r"publishPlugin|intellij-platform-plugin|PUBLISH_TOKEN",
"Chrome Web Store":r"chrome-webstore-upload|chrome-extension-upload|wext/action|publish-browser-extension","Firefox AMO":r"web-ext sign|amo|firefox-addon",
"npm":r"npm publish|pnpm publish|changesets/action|JS-DevTools/npm-publish","PyPI":r"pypa/gh-action-pypi-publish|twine upload|uv publish",
"itch.io":r"butler push|butler-publish","Steam":r"steam-deploy|steamcmd","Blender extensions":r"extensions\.blender\.org|blender --command extension",
"WordPress.org":r"wordpress-plugin-deploy|svn.wp-plugins","Docker":r"docker/build-push-action|docker push","GitHub Release":r"softprops/action-gh-release|gh release create|release-please|goreleaser|semantic-release|actions/create-release",
"Homebrew":r"homebrew|brew tap","Microsoft Store/winget":r"winget|msstore","App stores":r"fastlane|upload_to_app_store|upload-google-play"}
GELD={"GitHub Sponsors":r"github\.com/sponsors|FUNDING\.yml","Ko-fi":r"ko-fi\.com","Buy Me a Coffee":r"buymeacoffee\.com|buymeacoff\.ee","Patreon":r"patreon\.com",
"Gumroad":r"gumroad\.com","Polar":r"polar\.sh","Lemon Squeezy":r"lemonsqueezy","Paddle":r"paddle\.com","Stripe":r"stripe\.com|buy\.stripe","Superhive/Blender Market":r"superhivemarket|blendermarket",
"Open Collective":r"opencollective","Pro/Premium-versie":r"\b(pro version|premium|upgrade to pro|pro plan|pricing|license key|paid plan)\b"}
AI=["CLAUDE.md","AGENTS.md",".cursorrules",".cursor/",".claude/",".github/copilot-instructions.md",".windsurfrules","GEMINI.md"]
def sh(cmd,cwd=None):
    return subprocess.run(cmd,cwd=cwd,shell=True,capture_output=True,text=True,timeout=120).stdout
def doe(r):
    d=f"/tmp/scan/k/{r['repo'].replace('/','__')}"
    try:
        if not os.path.exists(d):
            subprocess.run(f"git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/{r['repo']}.git {d}",shell=True,timeout=120,capture_output=True)
        files=sh("git ls-tree -r HEAD --name-only",d).splitlines()
        wf=[f for f in files if f.startswith(".github/workflows/") and f.endswith((".yml",".yaml"))]
        wtext="\n".join(sh(f"git show HEAD:'{f}'",d) for f in wf[:15])
        readme=next((f for f in files if re.fullmatch(r"(?i)readme(\.[a-z]+)?",f)),None)
        rtext=sh(f"git show HEAD:'{readme}'",d) if readme else ""
        fund=sh("git show HEAD:.github/FUNDING.yml",d) if ".github/FUNDING.yml" in files else ""
        top=rtext[:3000].lower()
        r["workflows"]=len(wf)
        r["winkels"]=[k for k,p in WINKELS.items() if re.search(p,wtext,re.I)]
        r["geld"]=[k for k,p in GELD.items() if re.search(p,rtext+"\n"+fund+"\nFUNDING.yml"*bool(fund),re.I)]
        r["ai"]=[a for a in AI if any(f==a or f.startswith(a) or f.endswith("/"+a) for f in files)]
        r["beeld_boven"]=bool(re.search(r"\.(gif|png|jpg|jpeg|webp|mp4)|<img|!\[",top))
        r["gif_boven"]=".gif" in top or ".mp4" in top
        r["discord"]=bool(re.search(r"discord\.(gg|com)",rtext,re.I))
        r["changelog"]=any(re.fullmatch(r"(?i)(changelog|changes|history)(\.[a-z]+)?",os.path.basename(f)) for f in files)
        r["docs_map"]=any(f.startswith(("docs/","website/","wiki/")) for f in files)
        r["tests"]=bool(re.search(r"\b(test|pytest|vitest|jest|gut)\b",wtext,re.I))
        r["readme_regels"]=rtext.count("\n")
        r["ok"]=True
    except Exception as e:
        r["ok"]=False; r["fout"]=str(e)[:100]
    return r
os.makedirs("/tmp/scan/k",exist_ok=True)
with ThreadPoolExecutor(8) as ex: res=list(ex.map(doe,repos))
json.dump(res,open("/tmp/scan/resultaat.json","w"),indent=1)
print("klaar",sum(r.get("ok",False) for r in res),"van",len(res))
