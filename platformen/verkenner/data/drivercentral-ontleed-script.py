import re,sys,glob,json,statistics as st,collections
rows=[]
for f in glob.glob(sys.argv[1]+'/*'):
    h=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); t=' '.join(re.sub(r'<[^>]+>',' ',t).split())
    m=re.search(r'MSRP:\s*\$([\d,\.]+)',t); prijs=float(m.group(1).replace(',','')) if m else None
    d=re.search(r'Developer:\s*(.+?)\s+(?:Return period|SKU|Please)',t); dev=d.group(1) if d else ''
    data=sorted(re.findall(r'v\d{6,8}[^ ]* - (\d{4}-\d{2}-\d{2})',t))
    nrev=0 if 'No posts found' in t else len(re.findall(r'ty-discussion-post__author|cp-disc__author|discussion-post',h))
    titel=re.search(r'<title>(.*?)</title>',h,flags=re.S)
    rows.append(dict(f=f.split('/')[-1],titel=(titel.group(1).strip() if titel else '')[:60],prijs=prijs,dev=dev,eerste=data[0] if data else '',laatste=data[-1] if data else '',reviews=nrev))
json.dump(rows,open(sys.argv[2],'w'),indent=0)
print(len(rows),'pagina',sum(1 for r in rows if r['eerste']),'met revisiedatum')
c=collections.Counter(r['eerste'][:7] for r in rows if r['eerste']); print(sorted(c.items())[-14:])
nw=[r for r in rows if r['eerste']>='2026-05-01']
print('sinds mei 2026:',len(nw),'met review:',sum(1 for r in nw if r['reviews']>0),'devs',collections.Counter(r['dev'] for r in nw).most_common(6))
print('prijzen nieuw', st.median([r['prijs'] for r in nw if r['prijs']]) if nw else '-')
print('alle met review', sum(1 for r in rows if r['reviews']>0))
