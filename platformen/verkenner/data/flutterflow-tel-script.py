import json, collections, statistics as st
from datetime import datetime as D
d=json.load(open('flutterflow-marketplace-items-2026-11-15.json'))
def t(s): return D.fromisoformat(s.replace('Z','+00:00')) if s else None
pub=[x for x in d if x.get('status')=='PUBLISHED']
for x in pub:
    x['p']=int(x.get('price_cents','0'))/100; x['n']=int(x.get('num_times_added','0'))
    x['c']=t(x.get('create_time')); x['pl']=t(x.get('price_last_updated')); x['pt']=t(x.get('publish_time'))
    r=x.get('ratings',{}).get('fields',{}) if isinstance(x.get('ratings'),dict) else {}
    x['nr']=sum(int(r[k]['integerValue']) for k in r if k.endswith('_count'))
paid=[x for x in pub if x['p']>0]
print('paid',len(paid),'met price_last_updated',sum(1 for x in paid if x['pl']))
# price changed after creation by >7 days?
ch=[x for x in paid if x['pl'] and (x['pl']-x['c']).days>7]
print('prijs >7d na aanmaak gewijzigd',len(ch), 'waarvan op $50:',sum(1 for x in ch if x['p']==50))
pm=collections.Counter(x['pl'].strftime('%Y-%m') for x in ch); print(sorted(pm.items()))
clean=[x for x in paid if not (x['pl'] and (x['pl']-x['c']).days>7)]
print('schoon',len(clean))
now=D.fromisoformat('2026-11-15T10:00:00+00:00')
def cohort(lst,a,b,label):
    c=[x for x in lst if a<=x['c'].strftime('%Y-%m')<=b]
    if not c: print(label,0); return
    ns=[x['n'] for x in c]; rev=[x['n']*x['p'] for x in c]
    print(f"{label}: n={len(c)} mediaan adds={st.median(ns)} %>=10 adds={100*sum(v>=10 for v in ns)/len(ns):.0f}% %>=1={100*sum(v>=1 for v in ns)/len(ns):.0f}% mediaan bruto=${st.median(rev):.0f} %>=$1000 bruto={100*sum(v>=1000 for v in rev)/len(rev):.0f}% som=${sum(rev):.0f} mediaan ratings={st.median([x['nr'] for x in c])}")
for lab,lst in (('schoon',clean),('alle betaald',paid)):
    cohort(lst,'2025-11','2026-05',lab+' aangemaakt nov25-mei26')
    cohort(lst,'2026-02','2026-07',lab+' aangemaakt feb-jul26')
    cohort(lst,'2025-01','2025-10',lab+' aangemaakt jan-okt25')
# makers
cr=collections.defaultdict(float)
for x in clean: cr[x['marketplace_creator_ref'].split('/')[-1]]+=x['n']*x['p']
v=sorted(cr.values(),reverse=True); print('makers schoon',len(v),'top10',[round(a) for a in v[:10]],'mediaan',st.median(v), '#>=$5000',sum(a>=5000 for a in v))
print('top schoon:')
for x in sorted(clean,key=lambda x:-x['n']*x['p'])[:15]: print(round(x['n']*x['p']),x['p'],x['n'],x['nr'],x['c'].strftime('%Y-%m'),x.get('sample_app_type'),x['type'],x['name'][:45],x['marketplace_creator_ref'].split('/')[-1][:6])
free=[x for x in pub if x['p']==0]; print('gratis',len(free),'mediaan adds',st.median([x['n'] for x in free]))
