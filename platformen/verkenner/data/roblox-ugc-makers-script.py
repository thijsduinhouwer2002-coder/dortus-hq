import json,subprocess,sys,time,random,urllib.parse
d=json.load(open(sys.argv[1]))
mk={}
for x in d: mk[(x['creatorName'],x['creatorType'],x['creatorTargetId'])]=1
mk=list(mk); random.seed(8); random.shuffle(mk); mk=mk[:int(sys.argv[2])]
out={}
for (n,t,i) in mk:
    items=[];cur=''
    for p in range(4):
        u=f"https://catalog.roblox.com/v2/search/items/details?Category=1&CreatorName={urllib.parse.quote(n)}&CreatorType={2 if t=='Group' else 1}&SortType=3&Limit=120&IncludeNotForSale=true"+(f"&Cursor={cur}" if cur else "")
        r=subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout
        try: j=json.loads(r)
        except: time.sleep(5); continue
        if 'data' not in j: print('fout',n,r[:120],file=sys.stderr); time.sleep(8); break
        items+=[{k:x.get(k) for k in ('id','name','itemCreatedUtc','price','favoriteCount','creatorName','creatorType','taxonomy','saleLocationType')} for x in j['data']]
        cur=j.get('nextPageCursor'); time.sleep(2)
        if not cur or (items and items[-1]['itemCreatedUtc']<'2026-04-01'): break
    out[n]=items
    print(n,len(items),items[-1]['itemCreatedUtc'][:10] if items else '-',file=sys.stderr)
json.dump(out,open(sys.argv[3],'w'))
