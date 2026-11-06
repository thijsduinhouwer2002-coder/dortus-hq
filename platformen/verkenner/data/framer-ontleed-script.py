import re,json,glob,os,sys
S=sys.argv[1]
rows=[];bad=[]
def g(p,s):
    m=re.search(p,s,flags=re.S); return m[1] if m else None
for f in glob.glob(S+'/pages/*.html'):
    t=open(f,errors='ignore').read()
    d=''.join(re.findall(r'self.__next_f.push\(\[1,"(.*?)"\]\)',t,flags=re.S))
    d=d.encode().decode('unicode_escape',errors='ignore')
    i=d.find('"resource":{"id":"')
    if i<0: bad.append(f);continue
    w=d[i:i+6000]
    a=w.find('"author":')
    rows.append(dict(slug=os.path.basename(f)[:-5],id=int(g(r'"id":"(\d+)"',w)),title=g(r'"title":"(.*?)"',w),
      author=g(r'"name":"(.*?)"',w[a:]),authorslug=g(r'"slug":"(.*?)"',w[a:]),badges=g(r'"badges":\[(.*?)\]',w[a:]),
      created=g(r'"createdAt":"([^"]*)"',w),published=g(r'"publishedAt":"([^"]*)"',w),paid=g(r'"paid":(true|false)',w)=='true'))
json.dump(rows,open(S+'/framer-plugins.json','w'),ensure_ascii=False,indent=0)
print(len(rows),len(bad),bad[:3])
