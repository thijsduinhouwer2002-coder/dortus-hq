import glob,re,json,os
L=sorted(os.path.basename(f) for f in glob.glob('fr/f-*.png'))
FR={};GL={}
for n in L:
    m=re.match(r'f-\d+-(.+?)-(voor|rust|(\d+)ms)\.png',n)
    if m:
        lab,k,ms=m.group(1),m.group(2),m.group(3)
        v=-1 if k=='voor' else (99999 if k=='rust' else int(ms))
        FR.setdefault(lab,[]).append([v,n]); continue
    m=re.match(r'f-\d+-(glij\d)-(\d+)\.png',n)
    if m: GL.setdefault(m.group(1),[]).append([int(m.group(2)),n])
for k in FR:
    FR[k].sort()
    if FR[k][-1][0]==99999: FR[k][-1][0]=FR[k][-2][0]+120
for k in GL: GL[k]=[n for _,n in sorted(GL[k])]
json.dump({'FR':FR,'GL':GL},open('frames.json','w'))
print({k:len(v) for k,v in FR.items()},{k:len(v) for k,v in GL.items()})
