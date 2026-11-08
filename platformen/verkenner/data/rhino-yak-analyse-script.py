import json,statistics as st,collections,re,sys
R=[json.loads(l) for l in open(sys.argv[1])]
print('totaal',len(R),'fout',sum(1 for x in R if 'fout' in x))
R=[x for x in R if 'eerste' in x]
c=collections.Counter(x['eerste'][:4] for x in R); print(sorted(c.items()))
c2=collections.Counter(x['eerste'][:7] for x in R if x['eerste']>='2025-07'); print(sorted(c2.items()))
def stats(L,lab):
    d=sorted(x['download_count'] for x in L); n=len(d)
    if not n: print(lab,0); return
    p=lambda t: round(100*sum(1 for v in d if v>=t)/n,1)
    print(f"{lab}: n={n} mediaan={st.median(d)} 100+={p(100)}% 500+={p(500)}% 1000+={p(1000)}% 5000+={p(5000)}% top={d[-5:]}")
stats([x for x in R if '2026-05'<=x['eerste'][:7]<='2026-08'],'eerste versie mei-aug 2026')
stats([x for x in R if '2026-03'<=x['eerste'][:7]<='2026-06'],'mrt-jun 2026')
stats([x for x in R if '2025-07'<=x['eerste'][:7]<='2025-12'],'jul-dec 2025')
stats([x for x in R if x['eerste'][:4]=='2024'],'2024')
pay=re.compile(r'licen[cs]e key|trial|subscription|purchase|buy |gumroad|pricing|paid|premium|pro version|\$\d',re.I)
coh=[x for x in R if '2025-07'<=x['eerste'][:7]<='2026-08']
p=[x for x in coh if pay.search((x.get('desc') or '')+' '+(x.get('homepage') or ''))]
print('jul25-aug26',len(coh),'met betaalwoorden',len(p)); stats(p,'betaalwoorden')
for x in sorted(p,key=lambda x:-x['download_count'])[:15]: print(x['download_count'],x['eerste'][:10],x['name'],'|',x['authors'][:30],'|',(x.get('homepage') or '')[:50])
ai=[x for x in coh if re.search(r'\bAI\b|LLM|Claude|GPT|MCP',x.get('desc') or '')]; print('AI-woorden',len(ai)); stats(ai,'AI')
