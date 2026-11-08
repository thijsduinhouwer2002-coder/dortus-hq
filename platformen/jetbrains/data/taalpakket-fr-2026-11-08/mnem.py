import sys,os,glob,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tel_parse import parse
def has_mn(s):
    if s.lstrip().startswith('<html>'): return False
    t=s.replace('&&','')
    t=re.sub(r'\\&','',t)
    t=re.sub(r'&[a-zA-Z]+;|&#\d+;','',t)
    return bool(re.search(r'&\w',t))
base,lang=sys.argv[1],sys.argv[2]; tot=0; lost=[]; dup=0
for f in sorted(glob.glob(base+'/en/*.properties')):
    n=os.path.basename(f); en=parse(f); tr=parse(f'{base}/{lang}j/messages/{n}')
    for k,v in en.items():
        if k in tr and has_mn(v):
            tot+=1
            if not has_mn(tr[k]): lost.append((n,k,v,tr[k]))
print('met sneltoets:',tot,'kwijt:',len(lost))
for x in lost: print(' | '.join(x))
