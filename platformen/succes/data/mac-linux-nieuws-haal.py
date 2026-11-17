import json,subprocess,time,re
top=json.load(open('top40.json'))
out=open('nieuws.jsonl','w')
for a in top:
    s=subprocess.run(['curl','-s','--compressed','-m','30',f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={a}&count=500&maxlength=0&feeds=steam_community_announcements'],capture_output=True,text=True).stdout
    try: items=json.loads(s)['appnews']['newsitems']
    except Exception: items=None
    hits=[]
    for it in items or []:
        txt=it['title']+' '+it.get('contents','')
        m=re.search(r'.{0,120}\b(mac ?os|macbook|mac version|on mac|for mac|mac support|apple silicon|linux|steam ?os|proton|steam deck)\b.{0,160}',txt,re.I|re.S)
        if m: hits.append({'datum':it['date'],'titel':it['title'],'stuk':re.sub(r'\s+',' ',m.group(0))})
    out.write(json.dumps({'appid':a,'aantal_posts':len(items) if items is not None else None,'treffers':hits})+'\n'); out.flush()
    time.sleep(1.2)
print('klaar')
