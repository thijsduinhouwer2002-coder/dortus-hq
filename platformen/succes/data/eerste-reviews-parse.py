import re,sys,html,json,datetime as dt
MON={m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
def pdate(s):
    s=s.strip().rstrip('.')
    m=re.match(r'(\w+) (\d+)(?:, (\d{4}))?$',s) or None
    if m and m.group(1) in MON: return dt.date(int(m.group(3) or 2026),MON[m.group(1)],int(m.group(2)))
    m=re.match(r'(\d+) (\w+)(?:, (\d{4}))?$',s)
    if m and m.group(2) in MON: return dt.date(int(m.group(3) or 2026),MON[m.group(2)],int(m.group(1)))
    return None
def parse(h):
    out={}
    for card in h.split('class="apphub_Card ')[1:]:
        u=re.search(r'data-modal-content-url="([^"]*)"',card)
        t=re.search(r'<div class="title">([^<]*)</div>',card)
        if not u or not t: continue
        hr=re.search(r'([\d,.]+) hrs on record(?:\s*\(([\d,.]+) hrs at review time\))?',card)
        dp=re.search(r'<div class="date_posted">Posted: ([^<]*)</div>',card)
        f=lambda s: float(s.replace(',','')) if s else None
        d=pdate(dp.group(1)) if dp else None
        out[u.group(1)]={'up':t.group(1).strip()=='Recommended','gratis':'received_compensation' in card,
          'uur':f(hr.group(1)) if hr else None,'uur_bij_review':f(hr.group(2)) if hr else None,'datum':d.isoformat() if d else (dp.group(1) if dp else None)}
    return list(out.values())
if __name__=='__main__':
    r=parse(open(sys.argv[1]).read()); print(len(r)); 
    for x in sorted(r,key=lambda x:str(x['datum']))[:15]: print(x)
