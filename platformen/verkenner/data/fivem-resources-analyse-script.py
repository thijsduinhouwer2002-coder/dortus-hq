import json,glob,collections,re
R=[json.loads(open(f).read()) for f in glob.glob('single/*.json')]
R=[r for r in R if 'res' in r]
print('servers',len(R))
c=collections.Counter()
for r in R:
    for x in set(x.lower() for x in r['res']): c[x]+=1
fw={'qb-core':0,'es_extended':0,'qbx_core':0,'vrp':0,'ox_lib':0,'ox_inventory':0}
for k in fw: fw[k]=c.get(k,0)
print('frameworks',fw)
print('mediaan resources',sorted(len(r['res']) for r in R)[len(R)//2])
for k,v in c.most_common(400)[:400]:
    pass
# known paid prefixes
pref=['qs-','okok','jg-','rcore_','0r-','0r_','codem-','rtx_','lb-','17mov','wasabi_','kq_','cd_','loaf_','lation_','brutal_','origen_','ak47_','jim-','renewed','ps-','mri_','zsx_','vms_','envi-','tgiann','qbx_','bl_','fd_','p_','lc_','mt-','sn_','gfx','dusa','nass_','av_','pug-','tk_','yseries','lunar','qf_']
for p in pref:
    n=sum(1 for r in R if any(x.lower().startswith(p) for x in r['res']))
    print(p,n,end=' | ')
print()
json.dump(c.most_common(),open('res-telling.json','w'))
