import re,sys,time,urllib.request,urllib.parse
a=sys.argv[1]; maxp=int(sys.argv[2])
def get(u):
    for t in range(3):
        try: return urllib.request.urlopen(u,timeout=30).read().decode('utf-8','replace')
        except Exception as e: time.sleep(5)
    return ''
h=get(f'https://steamcommunity.com/app/{a}/reviews/?browsefilter=mostrecent&p=1&l=english&filterLanguage=all')
out=[h]
for p in range(1,maxp):
    cur=re.search(r'name="userreviewscursor" value="([^"]*)"',h)
    if not cur or 'apphub_Card ' not in h: break
    q=urllib.parse.urlencode({'userreviewscursor':cur.group(1),'userreviewsoffset':10*p,'p':p+1,'numperpage':10,'browsefilter':'mostrecent','l':'english','appHubSubSection':10,'filterLanguage':'all','searchText':'','maxInappropriateScore':100,'forceanon':1})
    time.sleep(1.0); h=get(f'https://steamcommunity.com/app/{a}/homecontent/?{q}'); out.append(h)
print('\n<!--PAGE-->\n'.join(out))
