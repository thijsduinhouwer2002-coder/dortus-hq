"""Haalt reviews van de openbare communitypagina van Steam (16 = aanbevolen, 17 = niet aanbevolen), met uren op dat moment.
Gebruik: python3 -I haal.py uit.json pagina's appid ..."""
import re,html,json,sys,time,urllib.request,urllib.parse
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf-8','replace')
def kaarten(h):
    out=[]
    for blok in re.split(r'class="apphub_Card modalContentLink',h)[1:]:
        t=re.search(r'apphub_CardTextContent">\s*<div class="date_posted">[^<]*</div>(.*?)</div>',blok,re.S)
        if not t: continue
        u=re.search(r'([\d,.]+) hrs on record',blok)
        tekst=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',html.unescape(t.group(1)))).strip()
        out.append({'uren':float(u.group(1).replace(',','')) if u else None,'tekst':tekst})
    return out
uit,pag=sys.argv[1],int(sys.argv[2]);R={}
for a in sys.argv[3:]:
    R[a]={}
    for sub,naam in((17,'neg'),(16,'pos')):
        alle=[];cur='*';off=0
        for p in range(1,pag+1):
            q=dict(userreviewscursor=cur,userreviewsoffset=off,p=p,numperpage=10,browsefilter='toprated',appid=a,appHubSubSection=sub,l='english',filterLanguage='default',searchText='',maxInappropriateScore=100)
            h=get(f'https://steamcommunity.com/app/{a}/homecontent/?'+urllib.parse.urlencode(q))
            k=kaarten(h)
            if not k: break
            alle+=k;off+=10
            m=re.search(r'name="userreviewscursor" value="([^"]*)"',h)
            if not m: break
            cur=m.group(1);time.sleep(1.2)
        # ontdubbelen
        seen=set();R[a][naam]=[x for x in alle if not (x['tekst'][:80] in seen or seen.add(x['tekst'][:80]))]
        print(a,naam,len(R[a][naam]),flush=True)
json.dump(R,open(uit,'w'))
