# Views, likes en antwoorden per maand van gestart. Gebruik: python3 -I plekken-analyse-script.py uit.json 2026-06,2026-07,2026-08
import json,sys,statistics as st
rows=[r for r in json.load(open(sys.argv[1])) if not r['pinned']]
def stats(sel,label):
    v=sorted(r['views'] for r in sel); l=[r['like_count'] for r in sel]; p=[r['posts_count']-1 for r in sel]
    if not v: print(label,'leeg'); return
    q=lambda a,f: sorted(a)[int(f*(len(a)-1))]
    print(f"{label}: n={len(v)} views mediaan {st.median(v)} p25 {q(v,.25)} p75 {q(v,.75)} p90 {q(v,.9)} | 500+ {sum(x>=500 for x in v)/len(v):.0%} 1000+ {sum(x>=1000 for x in v)/len(v):.0%} | likes mediaan {st.median(l)} | antwoorden mediaan {st.median(p)}, 0 antw {sum(x==0 for x in p)/len(p):.0%}")
months={}
for r in rows: months.setdefault(r['created_at'][:7],[]).append(r)
for m in sorted(months): stats(months[m],m)
stats([r for r in rows if r['created_at'][:7] in sys.argv[2].split(',')],'lichting '+sys.argv[2])
for r in sorted(rows,key=lambda r:-r['views'])[:8]: print(r['views'],r['like_count'],r['created_at'][:10],r['title'][:80])
