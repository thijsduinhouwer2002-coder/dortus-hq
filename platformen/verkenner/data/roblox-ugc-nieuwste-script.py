import json,subprocess,sys,time
cur='';out=[];cat=sys.argv[1];maxp=int(sys.argv[2])
for p in range(maxp):
    u=f"https://catalog.roblox.com/v2/search/items/details?Category={cat}&SortType=3&Limit=120&IncludeNotForSale=false"+(f"&Cursor={cur}" if cur else "")
    r=subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout
    try: d=json.loads(r)
    except: print('fout',r[:200],file=sys.stderr); time.sleep(10); continue
    if 'data' not in d: print('fout',r[:200],file=sys.stderr); time.sleep(10); continue
    out+=d['data']; cur=d.get('nextPageCursor')
    if p%5==0: print(p,len(out),d['data'][-1]['itemCreatedUtc'][:16],file=sys.stderr)
    if not cur: break
    time.sleep(2)
json.dump(out,open(sys.argv[3],'w'))
print('klaar',len(out),out[-1]['itemCreatedUtc'],file=sys.stderr)
