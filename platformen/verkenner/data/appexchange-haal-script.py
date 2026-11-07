import subprocess,re,json,sys,random,concurrent.futures as cf
us=[l.strip() for l in open(sys.argv[1]) if 'appxListingDetail?listingId=' in l]
random.seed(7); us=random.sample(us,int(sys.argv[3]))
def g(u):
    s=subprocess.run(['curl','-sL','--max-time','30',u],capture_output=True,text=True).stdout
    f=lambda p:(re.search(p,s) or [None,None])[1]
    return dict(url=u,pub=f(r'"publishedDate":"([^"]*)"'),rev=f(r'"aggregateRating":\{[^}]*"reviewCount":(\d+)'),model=f(r'"price_model_type":"([^"]*)"'),price=f(r'"price":([\d.]+)'),publisher=f(r'"publisher":\{"id":"[^"]*","name":"([^"]*)"'),type=f(r'"listingType":"([^"]*)"') or f(r'"technology":"([^"]*)"'),title=f(r'<title>([^<|]*)'),ok=len(s)>50000)
with cf.ThreadPoolExecutor(10) as ex: out=list(ex.map(g,us))
json.dump(out,open(sys.argv[2],'w'),indent=0);print(len(out),sum(x['ok'] for x in out))
