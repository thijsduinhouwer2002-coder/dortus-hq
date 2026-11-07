import subprocess,re,json,sys,concurrent.futures as cf
us=[l.strip() for l in open(sys.argv[1]) if '/app/' in l]
def g(u):
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    f=lambda p:(re.search(p,s) or [None,None])[1]
    return dict(url=u,listed=f(r'"listedDate":"([^"]*)"'),rev=f(r'"reviewSummary":\{"appEntryId":"[^"]*","count":(\d+)'),trial=f(r'"hasFreeTrial":(true|false)'),xbilling=f(r'"(?:isXeroAppStoreBilling|hasAppStoreBilling|usesXeroBilling|isAppStoreSubscription)":(true|false)'),ok=len(s)>50000)
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(g,us))
json.dump(out,open(sys.argv[2],'w'),indent=0);print(len(out),sum(x['ok'] for x in out))
