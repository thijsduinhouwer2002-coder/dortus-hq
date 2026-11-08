# TrustMRR per platform: welke platformen geven nieuwe kleine makers (start 2025 of later) geverifieerde omzet?
# Gebruik: python3 -I trustmrr-platform-analyse.py data/trustmrr-alle-2026-11-08.jsonl [platform]
import json, re, sys, statistics as st, collections

P = {  # platform: (domeinen, sterke zinnen in naam/beschrijving)
 'iOS/iPhone-app': (['apps.apple.com'], [r'\bios app\b', r'\biphone app\b', r'\bfor iphone\b', r'\bon the app store\b']),
 'Android-app': (['play.google.com'], [r'\bandroid app\b', r'\bon google play\b']),
 'Mac-app': ([], [r'\bmac ?os\b', r'\bmac app\b', r'\byour mac\b', r'\bmenu ?bar app\b', r'\bfor mac\b', r'\bnative mac']),
 'Chrome-extensie': (['chromewebstore.google.com', 'chrome.google.com'], [r'\bchrome extension\b', r'\bbrowser extension\b']),
 'Shopify-app': (['apps.shopify.com'], [r'\bshopify app\b', r'\bfor shopify\b', r'\bshopify stores?\b', r'\bshopify merchants?\b']),
 'Telegram': (['t.me'], [r'\btelegram bot\b', r'\btelegram mini ?app\b', r'\bon telegram\b', r'\bin telegram\b']),
 'Discord': ([], [r'\bdiscord bot\b', r'\bdiscord app\b', r'\bfor discord\b', r'\bdiscord servers?\b']),
 'Whop': (['whop.com'], [r'\bwhop app\b', r'\bon whop\b']),
 'Slack': ([], [r'\bslack app\b', r'\bslack bot\b', r'\bin slack\b', r'\bfor slack\b']),
 'Google Workspace': ([], [r'\bgoogle sheets? add-?on\b', r'\bgmail add-?on\b', r'\bgoogle docs add-?on\b', r'\bworkspace add-?on\b', r'\bin google sheets\b', r'\bgmail extension\b']),
 'Microsoft (Excel/Outlook/Teams)': ([], [r'\bexcel add-?in\b', r'\boutlook add-?in\b', r'\bteams app\b', r'\bfor microsoft teams\b', r'\bword add-?in\b']),
 'Figma': (['figma.com'], [r'\bfigma plugin\b', r'\bfigma community\b']),
 'Notion': ([], [r'\bnotion template\b', r'\bnotion integration\b', r'\bfor notion\b']),
 'WordPress': (['wordpress.org'], [r'\bwordpress plugin\b', r'\bwordpress theme\b', r'\bwoocommerce\b']),
 'VS Code/IDE': (['marketplace.visualstudio.com'], [r'\bvs ?code extension\b', r'\bvscode extension\b', r'\bjetbrains\b', r'\bintellij\b']),
 'Obsidian': ([], [r'\bobsidian plugin\b', r'\bobsidian\.md\b', r'\bfor obsidian\b']),
 'Raycast': ([], [r'\braycast\b']),
 'Webflow/Framer': ([], [r'\bwebflow app\b', r'\bframer plugin\b', r'\bframer template\b', r'\bwebflow template\b', r'\bfor webflow\b', r'\bfor framer\b']),
 'Etsy-verkopers': ([], [r'\betsy sellers?\b', r'\betsy shops?\b', r'\bfor etsy\b']),
 'Steam/games': ([], [r'\bon steam\b', r'\bsteam game\b', r'\bindie game\b']),
 'Minecraft/Roblox': ([], [r'\bminecraft\b', r'\broblox\b']),
 'Apple Watch': ([], [r'\bapple watch\b', r'\bwatchos\b']),
 'ChatGPT/GPT-app': ([], [r'\bchatgpt app\b', r'\bcustom gpt\b', r'\bgpt store\b', r'\bchatgpt plugin\b']),
 'Zapier/Make': ([], [r'\bzapier integration\b', r'\bmake\.com\b']),
 'Claude/MCP': ([], [r'\bmcp server\b', r'\bclaude code\b', r'\bclaude skill', r'\bcursor extension\b']),
 'HubSpot/Salesforce': ([], [r'\bhubspot app\b', r'\bfor hubspot\b', r'\bsalesforce app\b']),
 'Canva/Adobe': ([], [r'\bcanva app\b', r'\bcanva plugin\b', r'\bphotoshop plugin\b', r'\bpremiere pro\b', r'\bafter effects\b', r'\blightroom presets?\b']),
 'Blender/3D': ([], [r'\bblender\b', r'\bunity asset\b', r'\bunreal engine\b']),
 'TradingView/MT': ([], [r'\btradingview\b', r'\bmetatrader\b', r'\bmt[45] (ea|indicator|expert)']),
}

def dom(w):
    m = re.search(r'https?://([^/\]\)]+)', w or '')
    return m.group(1).lower().replace('www.', '') if m else ''

def classify(x):
    t = ((x.get('name') or '') + ' . ' + (x.get('desc') or '')).lower()
    d = dom(x.get('web'))
    out = []
    for p, (ds, pats) in P.items():
        if any(d == z or d.endswith('.' + z) for z in ds) or any(re.search(q, t) for q in pats):
            out.append(p)
    return out

rows = [json.loads(l) for l in open(sys.argv[1])]
new = [x for x in rows if '2025-01-01' <= (x.get('founded') or '') <= '2026-11-08' and x['slug'] != 'pastel']
show = sys.argv[2] if len(sys.argv) > 2 else None
by = collections.defaultdict(list)
for x in new:
    for p in classify(x):
        by[p].append(x)
if show:
    for x in sorted(by[show], key=lambda x: -(x['d30'] or 0)):
        print(f"{x['d30'] or 0:>9.0f} | {x['founded']} | {x['provider'][:12]} | {dom(x['web'])} | {x['slug']} | {(x['desc'] or '')[:110]}")
    sys.exit()
print(f"makers sinds 2025: {len(new)}")
def q(v):
    v = [y['d30'] or 0 for y in v]
    return len(v), st.median(v), sum(a >= 100 for a in v), sum(a >= 300 for a in v), sum(a >= 1000 for a in v)
print(f"{'platform':34} {'n':>4} {'med30':>6} {'>=100':>6} {'>=300':>6} {'>=1000':>6}")
for p, v in sorted(by.items(), key=lambda kv: -q(kv[1])[3]):
    n, m, a, b, c = q(v)
    print(f"{p:34} {n:>4} {m:>6.0f} {a:>6} {b:>6} {c:>6}")
n, m, a, b, c = q(new)
print(f"{'ALLE makers sinds 2025':34} {n:>4} {m:>6.0f} {a:>6} {b:>6} {c:>6}")
