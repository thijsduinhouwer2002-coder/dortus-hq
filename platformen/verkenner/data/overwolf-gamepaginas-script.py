import sys,re,json,subprocess,time
games=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
for g in games:
    h=subprocess.run(['curl','-sL','-m','25','-A','Mozilla/5.0','https://www.overwolf.com/browse-by-game/'+g],capture_output=True,text=True).stdout.replace('\\"','"')
    apps=[]
    for m in re.finditer(r'"appId":"([^"]+)"',h):
        seg=h[max(0,m.start()-3000):m.end()+3000]
        apps.append(m.group(1))
    # pull app objects by seoName
    items=[]
    for m in re.finditer(r'\{[^{}]*"seoName":"([^"]+)"[^{}]*\}',h):
        o=m.group(0)
        def f(p):
            x=re.search(p,o); return x.group(1) if x else None
        items.append({'seo':m.group(1),'title':f(r'"title":"([^"]*)"'),'author':f(r'"author":"([^"]*)"'),
          'ratings':f(r'"totalRatings":(\d+)'),'avg':f(r'"avgReviewRate":([\d.]+)'),'ads':f(r'"doesContainsAds":(\w+)'),
          'premium':f(r'"isPremium":(\w+)'),'desc':f(r'"shortDescription":"([^"]*)"')})
    out[g]={'n_appid':len(set(apps)),'items':items}
    print(g,len(set(apps)),len(items),file=sys.stderr)
    time.sleep(0.5)
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
