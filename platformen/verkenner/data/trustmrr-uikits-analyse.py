import re,os,json
def num(s): return float(s.replace('$','').replace(',',''))
rows=[]
for f in sorted(os.listdir('tm')):
    t=open('tm/'+f,errors='ignore').read()
    if '## Profile' not in t: continue
    g=lambda k:(re.search(r'\n- '+k+r': (.*)',t) or [None,''])[1].strip()
    r=dict(slug=f[:-3],name=g('Name'),desc=g('Description'),founded=g('Founded date'))
    for p,k in [('Last 30 days','d30'),('Last 6 months','m6'),('Last 12 months','m12'),('All time','tot')]:
        m=re.search(r'\| '+p+r' \| (\$[\d,\.]+)',t); r[k]=num(m[1]) if m else None
    rows.append(r)
json.dump(rows,open('rows.json','w'),indent=0)
ui=re.compile(r'(?i)shadcn|tailwind|\bcomponents?\b|\bblocks\b|ui kit|ui library|design system|figma kit')
sel=[r for r in rows if ui.search(r['desc']+' '+r['name'])]
print('profielen',len(rows),'UI-kits',len(sel))
for r in sorted(sel,key=lambda r:-(r['tot'] or 0)): print(r['founded'][:7],r['tot'],r['m6'],r['d30'],r['slug'],'|',r['desc'][:90])
