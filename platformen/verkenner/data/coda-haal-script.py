import sys,json,re,subprocess,concurrent.futures as cf
def one(u):
    s=subprocess.run(["curl","-sL","-m","30",u],capture_output=True,text=True).stdout
    def g(k):
        m=re.search('"'+k+r'":("?)([^",}]*)',s); return m.group(2) if m else ''
    pr=re.search(r'"standardPackPlan":\{[^{}]*"pricing":(\{[^{}]*\})',s)
    emp=re.findall(r'"employer":("?[^",]*)',s)
    first=re.search(r'"createdAt":"([^"]*)"',s[s.find('"standardPackPlan"'):] if '"standardPackPlan"' in s else '')
    return dict(url=u,pricing=pr.group(1) if pr else '',laatste=g('lastReleasedAt')[:10],plan=first.group(1)[:10] if first else '',employer=emp[:2],cat=g('packCategoryType'),cert=g('certified'))
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(one,urls): print(json.dumps(r),flush=True)
