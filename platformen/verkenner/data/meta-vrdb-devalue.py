import json,sys
def unflatten(arr):
    cache={}
    def h(i):
        if i==-1: return None
        if i in (-2,-3,-4,-5,-6): return None
        if i in cache: return cache[i]
        v=arr[i]
        if isinstance(v,list):
            if v and isinstance(v[0],str) and v[0] in('Date','Set','Map','BigInt','RegExp'):
                r=v[1] if len(v)>1 else None
            else:
                r=[]; cache[i]=r
                for x in v: r.append(h(x))
        elif isinstance(v,dict):
            r={}; cache[i]=r
            for k,x in v.items(): r[k]=h(x)
        else: r=v
        cache[i]=r; return r
    return h(0)
def apps(path):
    d=json.load(open(path))
    for n in d['nodes']:
        if n and n.get('type')=='data' and 'streamed' in json.dumps(n['data'][:1]):
            o=unflatten(n['data'])
            return o['streamed']['apps']
