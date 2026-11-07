import subprocess,re,json,sys,concurrent.futures as cf
us=[l.strip() for l in open(sys.argv[1]) if l.strip()]
def g(u):
    s=subprocess.run(['curl','-sL','--max-time','25',u],capture_output=True,text=True).stdout
    f=lambda p:(re.search(p,s) or [None,None])[1]
    return dict(url=u,reviews=f(r'"totalReviews":(\d+)'),price=f(r'"price":"([^"]*)"'),installs=f(r'"approximateInstalls":"([^"]*)"'),by=f(r'by ([^<]{2,60}?)</'),ok=len(s)>50000)
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(g,us))
json.dump(out,open(sys.argv[2],'w'),indent=0);print(len(out))
