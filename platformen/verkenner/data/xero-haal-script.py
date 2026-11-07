# Leest per app-pagina: listedDate, eigen reviewSummary (appEntryId moet bij de slug horen), revenueTypeCode, proef, uitgelicht, maker
import subprocess,re,json,sys,concurrent.futures as cf
sl=json.load(open(sys.argv[1]))
L=json.load(open(sys.argv[3]))['per_regio']
reg={}
for r,v in L.items():
    for x in v: reg.setdefault(x,[]).append(r)
def g(s_):
  for r in ['']+[x+'/' for x in reg.get(s_,[])][:3]:
    u=f'https://apps.xero.com/{r}app/{s_}'
    s=subprocess.run(['curl','-sL','--max-time','40',u],capture_output=True,text=True).stdout
    if '"listedDate"' in s: break
  return lees(s_,s,r)
def lees(s_,s,r):
    f=lambda p:(re.search(p,s) or [None,None])[1]
    eid=f(r'"entryId":"([^"]*)"')
    rv=re.search(r'"reviewSummary":\{"appEntryId":"([^"]*)","count":(\d+)',s)
    return dict(slug=s_,regio=r,entryId=eid,listed=f(r'"listedDate":"([^"]*)"'),
      rev=int(rv[2]) if rv else None,rev_eid=rv[1] if rv else None,
      revtype=f(r'"revenueTypeCode":"?([A-Za-z]*)"?'),trial=f(r'"hasFreeTrial":(true|false)'),
      featured=f(r'"isFeaturedApp":(true|false)'),dev=f(r'"developer":\{"name":"([^"]*)"'),
      title=f(r'"seoTitle":null,|"title":"([^"]*)"'),ok=len(s)>50000)
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(g,sl))
json.dump(out,open(sys.argv[2],'w'),indent=0);print(len(out),sum(x['ok'] for x in out),sum(1 for x in out if x['listed']))
