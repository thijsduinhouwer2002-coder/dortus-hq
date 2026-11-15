import re,html,urllib.request,json
from concurrent.futures import ThreadPoolExecutor
urls=[html.unescape(u) for u in re.findall(r'<loc>([^<]*)</loc>',open('/tmp/stripe/sitemap-apps.xml').read())]
lm=re.findall(r'<lastmod>([^<]*)</lastmod>',open('/tmp/stripe/sitemap-apps.xml').read())
def one(u):
    try: s=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode()
    except Exception as e: return {'url':u,'err':str(e)}
    g=lambda p:(re.search(r'<meta property="og:'+p+r'" content="([^"]*)"',s) or [None,None])[1]
    return {'url':u,'title':html.unescape(g('title') or ''),'desc':html.unescape(g('description') or '')}
with ThreadPoolExecutor(4) as ex: out=list(ex.map(one,urls))
json.dump({'lastmod_count':len(lm),'apps':out},open('/tmp/stripe/apps.json','w'))
print(len(out),sum('err' in o for o in out),len(lm))
