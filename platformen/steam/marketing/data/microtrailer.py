# Haalt per spel de microtrailer (6 s, door Steam gemaakt uit de eerste video) op via IStoreBrowseService/GetItems.
# Gebruik: python3 microtrailer.py winkeltekst-2026-11-16.csv uit.csv  (filmpjes in ./microtrailers/, niet in de repo)
# Beelden daarna met ffmpeg op 0.5, 1.7, 2.9, 4.1, 5.3, 6.5 s en met het oog ingedeeld: microtrailer-beelden-2026-11-17.csv
import csv,json,subprocess,time,urllib.parse,os,sys
rows=list(csv.DictReader(open(sys.argv[1])))
os.makedirs("microtrailers",exist_ok=True)
out=[]
ids=[r['appid'] for r in rows]
for i in range(0,len(ids),20):
    q={"ids":[{"appid":int(a)} for a in ids[i:i+20]],"context":{"language":"english","country_code":"US"},"data_request":{"include_trailers":True}}
    u="https://api.steampowered.com/IStoreBrowseService/GetItems/v1/?input_json="+urllib.parse.quote(json.dumps(q))
    d=json.loads(subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout)
    for it in d['response']['store_items']:
        tr=it.get('trailers',{}); hs=tr.get('highlights',[])+tr.get('other_trailers',[])
        first=hs[0] if hs else None
        mt=None
        if first:
            for f in first.get('microtrailer',[]):
                if f['filename'].endswith('.mp4'): mt=f['filename']
        out.append({'appid':it['appid'],'naam':it.get('name'),'trailers':len(hs),'eerste':first['trailer_name'] if first else '','mt':mt})
    time.sleep(1)
soort={r['appid']:r['soort'] for r in rows}
w=csv.writer(open(sys.argv[2],'w'))
w.writerow(['soort','appid','naam','trailers','eerste_trailer','microtrailer'])
for o in out:
    w.writerow([soort[str(o['appid'])],o['appid'],o['naam'],o['trailers'],o['eerste'],o['mt'] or ''])
    if o['mt']:
        p=f"microtrailers/{o['appid']}.mp4"
        if not os.path.exists(p):
            subprocess.run(['curl','-s','-o',p,"https://video.akamai.steamstatic.com/store_trailers/"+o['mt']]); time.sleep(0.5)
print(len(out))
