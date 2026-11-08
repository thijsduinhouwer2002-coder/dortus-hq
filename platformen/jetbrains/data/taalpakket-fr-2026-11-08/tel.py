# Onafhankelijke parser volgens java.util.Properties.load
import sys, os, re, glob, json
def logical_lines(txt):
    lines = txt.replace('\r\n','\n').replace('\r','\n').split('\n')
    out=[]; buf=None
    for ln in lines:
        s = ln.lstrip(' \t\f') if buf is not None else ln
        if buf is None:
            st = s.lstrip(' \t\f')
            if not st or st[0] in '#!': continue
            s = st
        # aantal backslashes aan het eind
        n = len(s) - len(s.rstrip('\\'))
        if n % 2 == 1:
            buf = (buf or '') + s[:-1]; continue
        out.append((buf or '') + s); buf=None
    if buf is not None: out.append(buf)
    return out
ESC={'t':'\t','n':'\n','r':'\r','f':'\f'}
def unesc(s):
    r=[];i=0
    while i<len(s):
        c=s[i]
        if c=='\\' and i+1<len(s):
            d=s[i+1]
            if d=='u' and re.match(r'[0-9a-fA-F]{4}',s[i+2:i+6]): r.append(chr(int(s[i+2:i+6],16))); i+=6; continue
            r.append(ESC.get(d,d)); i+=2; continue
        r.append(c); i+=1
    return ''.join(r)
def parse(path):
    d={}
    if not os.path.exists(path): return d
    txt=open(path,encoding='utf-8',errors='strict').read()
    for l in logical_lines(txt):
        i=0; k=[]
        while i<len(l):
            c=l[i]
            if c=='\\': k.append(l[i:i+2]); i+=2; continue
            if c in '=: \t\f': break
            k.append(c); i+=1
        while i<len(l) and l[i] in ' \t\f': i+=1
        if i<len(l) and l[i] in '=:': i+=1
        while i<len(l) and l[i] in ' \t\f': i+=1
        d[unesc(''.join(k))]=unesc(l[i:])
    return d
def mf_args(s):
    # MessageFormat: tekst tussen enkele quotes is letterlijk, '' is een quote
    res=[];i=0;q=False
    while i<len(s):
        c=s[i]
        if c=="'":
            if i+1<len(s) and s[i+1]=="'": i+=2; continue
            q=not q; i+=1; continue
        if not q and c=='{':
            m=re.match(r'\{\s*(\d+)',s[i:])
            if m: res.append(m.group(1))
        i+=1
    return sorted(set(res))
def mnem(s):
    t=s.replace('&&','')
    t=re.sub(r'&[a-zA-Z]+;|&#\d+;','',t)
    return '&' in t or bool(re.search(r'(?<![_\w])_\w',t)) and False
base=sys.argv[1]; lang=sys.argv[2]
tot=dict(keys=0,missing=0,leeg=0,same_all=0,same_zin=0,ph=0,ph_set=0,mnem=0,extra=0)
lst={k:[] for k in ['missing','same_zin','ph_set','mnem']}
for f in sorted(glob.glob(f'{base}/en/*.properties')):
    n=os.path.basename(f); en=parse(f); tr=parse(f'{base}/{lang}j/messages/{n}')
    tot['extra']+=len(set(tr)-set(en))
    for k,v in en.items():
        tot['keys']+=1
        if k not in tr: tot['missing']+=1; lst['missing'].append((n,k,v)); continue
        w=tr[k]
        if not w.strip() and v.strip(): tot['leeg']+=1
        if w==v and re.search('[A-Za-z]',v):
            tot['same_all']+=1
            if re.search(r'[a-z]{3,} [a-z]{3,}',v): tot['same_zin']+=1; lst['same_zin'].append((n,k,v))
        uses_mf = bool(re.search(r'\{\d',v))
        if sorted(re.findall(r'\{(\d+)',w))!=sorted(re.findall(r'\{(\d+)',v)): tot['ph']+=1
        if mf_args(w)!=mf_args(v): tot['ph_set']+=1; lst['ph_set'].append((n,k,v,w))
        if mnem(v) and not mnem(w): tot['mnem']+=1; lst['mnem'].append((n,k,v,w))
print(json.dumps(tot,indent=1))
json.dump(lst,open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
