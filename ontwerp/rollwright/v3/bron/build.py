import glob,re,json,os,sys
L=sorted(os.path.basename(f) for f in glob.glob('fr/f-*.png'))
FR={}
for n in L:
    m=re.match(r'f-\d+-(.+?)-(voor|rust|(\d+)ms)\.png',n)
    if not m: continue
    lab,k,ms=m.group(1),m.group(2),m.group(3)
    v=-1 if k=='voor' else (99999 if k=='rust' else int(ms))
    FR.setdefault(lab,[]).append([v,n])
for k in FR: FR[k].sort()
# rust shown after last ms: give it last_ms+120
for k,v in FR.items():
    if v[-1][0]==99999: v[-1][0]=v[-2][0]+120
meta=open('fr/meta.json').read()
for h in ['a','b']:
    s=open(h+'.html').read().replace('__FR__',json.dumps(FR)).replace('__META__',meta)
    open(h+'-r.html','w').write(s)
print({k:len(v) for k,v in FR.items()})
