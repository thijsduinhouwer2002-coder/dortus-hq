import json,sys,urllib.request
from concurrent.futures import ThreadPoolExecutor
r=json.load(open(sys.argv[1]))
sub=[x for x in r if sys.argv[2]<=x['created'][:7]<=sys.argv[3]]
def f(x):
    try:
        with urllib.request.urlopen(f"https://catalog.roblox.com/v1/favorites/assets/{x['id']}/count",timeout=10) as h: x['fav']=int(h.read())
    except Exception: x['fav']=None
with ThreadPoolExecutor(4) as ex: list(ex.map(f,sub))
json.dump(sub,open(sys.argv[4],'w'),ensure_ascii=False)
print(sum(1 for x in sub if x['fav'] is not None),len(sub))
