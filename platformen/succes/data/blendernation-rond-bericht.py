import json,sys,html
from datetime import date,timedelta
sys.path.insert(0,'..')
from bn_vers import versions
TODAY=date(2026,11,17)
def daily(vs):
    vs=sorted(vs,key=lambda v:v[2])
    ser={}
    for i,(ver,n,d) in enumerate(vs):
        a=date.fromisoformat(d); b=date.fromisoformat(vs[i+1][2]) if i+1<len(vs) else TODAY
        days=max((b-a).days,1)
        for k in range(days): ser[a+timedelta(k)]=ser.get(a+timedelta(k),0)+n/days
    return ser
def win(ser,p,lo,hi):
    xs=[ser[p+timedelta(k)] for k in range(lo,hi+1) if p+timedelta(k) in ser]
    return (sum(xs)/len(xs), len(xs)) if xs else (None,0)
if __name__=='__main__':
    bn=json.load(open('bn_addons3.json'))
    rows=[]
    for x in bn:
        for s in x['match']:
            vs=versions(s)
            if not vs: print('geen',s); continue
            p=date.fromisoformat(x['date'])
            ser=daily(vs)
            first=min(date.fromisoformat(v[2]) for v in vs)
            b=win(ser,p,-14,-1); a1=win(ser,p,0,6); a2=win(ser,p,7,20); a3=win(ser,p,28,55)
            f=lambda w: f"{w[0]:.0f}({w[1]})" if w[0] is not None else "-"
            print(x['date'],s,'eerste',first,'nver',len(vs),'voor',f(b),'wk1',f(a1),'wk2-3',f(a2),'wk5-8',f(a3),'tot',sum(v[1] for v in vs),'|',html.unescape(x['title'])[:40])
