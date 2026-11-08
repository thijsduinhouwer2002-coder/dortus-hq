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
