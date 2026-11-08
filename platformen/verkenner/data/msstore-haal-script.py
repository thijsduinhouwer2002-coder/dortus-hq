import sys,re,json,random,subprocess,concurrent.futures as cf,time
ids=[l.strip() for l in open(sys.argv[1])]
random.seed(int(sys.argv[3])); s=random.sample(ids,int(sys.argv[2]))
F=['releaseDateUtc','ratingCount','averageRating','price','displayPrice','publisherName','publisherId','categoryId','productType','hasAddOns','hasThirdPartyIAPs','hasFreeTrial','title','mediaType','lastUpdateDateUtc','productFamilyName']
def get(i):
    try:
        h=subprocess.run(['curl','-sS','--compressed','-m','30',f'https://apps.microsoft.com/detail/{i}?hl=en-US&gl=US'],capture_output=True,text=True).stdout
    except Exception as e: return {'id':i,'err':str(e)}
    r={'id':i,'len':len(h)}
    for f in F:
        m=re.search(r'"%s":("(?:[^"\\]|\\.)*"|[^,}\]]*)'%f,h)
        if m:
            try:r[f]=json.loads(m.group(1))
            except: r[f]=m.group(1)
    time.sleep(0.6); return r
with cf.ThreadPoolExecutor(int(sys.argv[5]) if len(sys.argv)>5 else 3) as ex, open(sys.argv[4],'w') as o:
    for r in ex.map(get,s): o.write(json.dumps(r)+'\n')
