# Leest itch.io-pagina's: publicatiedatum, aantal ratings, prijs, tags, AI-melding. Gebruik: python3 -I itch-pagina-script.py URLS.txt UIT.jsonl
# 9 nov run 08:31: LET OP, het veld pub is meestal de Updated-datum (veel pagina's tonen geen rij Published). Gebruik voor de publicatiedatum de RSS (pubDate = createDate), zie vtuber-itch-analyse-script.py, titel uit <title>, ratings uit aggregateRating.
# Rustig blijven: bij te snel lezen geeft itch 429.
import json,subprocess,re,time,sys,html as H
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
f=open(sys.argv[2],'a')
def rij(h,naam):
    m=re.search(r'<td>'+naam+r'</td><td>(.*?)</td>',h,re.S)
    return m.group(1) if m else ''
for u in urls:
    for t in range(3):
        r=subprocess.run(["curl","-s","-m","30","-A","Mozilla/5.0 DortusVerkenner",u],capture_output=True,text=True)
        if '429 Too Many' not in r.stdout: break
        time.sleep(15)
    h=r.stdout
    pan=h[h.find('<div class="game_info_panel_widget'):] if 'class="game_info_panel_widget' in h else ''
    pub=re.search(r'<td>Published</td><td><abbr title="([^"]+)"',pan) or re.search(r'abbr title="([^"]+)"',pan)
    upd=re.search(r'<td>Updated</td><td><abbr title="([^"]+)"',pan)
    rc=re.search(r'"ratingCount":(\d+)',h) or re.search(r'\((\d[\d,]*) total ratings?\)',h)
    avg=re.search(r'"ratingValue":"?([\d.]+)',h)
    price=re.search(r'"price":"([\d.]+)"',h)
    pwyw=('name your own price' in h.lower())
    free=bool(re.search(r'download_btn|>Download Now<',h)) and not price
    title=re.search(r'<title>([^<]*)',h)
    tags=re.findall(r'href="https://itch.io/[^"]*tag-[^"]*">([^<]+)</a>',rij(h,'Tags'))
    ai=re.sub(r'<[^>]+>','',rij(h,'AI Disclosure')).strip()
    f.write(json.dumps({'url':u,'title':H.unescape(title.group(1)) if title else None,'pub':pub.group(1) if pub else None,'upd':upd.group(1) if upd else None,
      'ratings':int(rc.group(1).replace(',','')) if rc else 0,'avg':avg.group(1) if avg else None,'price':price.group(1) if price else None,'pwyw':pwyw,
      'tags':tags,'ai':ai,'len':len(h)},ensure_ascii=False)+"\n"); f.flush()
    time.sleep(1.5)
