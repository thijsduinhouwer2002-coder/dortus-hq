# Leest itch.io-pagina's: publicatiedatum, aantal ratings, prijs. Gebruik: python3 -I itch-pagina-script.py URLS.txt UIT.jsonl
# LET OP (9 nov): veel itch-pagina's tonen geen rij Published en de titel-regex mist vaak; volgende keer de eerste <abbr title> in game_info_panel_widget als datum nemen en de titel uit <title>. Rustig blijven: bij te snel lezen geeft itch 429.
import json,subprocess,re,time,sys
urls=[u.strip() for u in open(sys.argv[1]) if u.strip()]
f=open(sys.argv[2],'a')
for u in urls:
    for t in range(3):
        r=subprocess.run(["curl","-s","-m","30","-A","Mozilla/5.0 DortusVerkenner",u],capture_output=True,text=True)
        if '429 Too Many' not in r.stdout: break
        time.sleep(15)
    h=r.stdout
    pub=re.search(r'<td>Published</td><td><abbr title="([^"]+)"',h)
    upd=re.search(r'<td>Updated</td><td><abbr title="([^"]+)"',h)
    rat=re.search(r'\((\d[\d,]*) total ratings?\)',h)
    avg=re.search(r'ratingValue"?[:=]\s*"?([\d.]+)',h)
    price=re.search(r'<span class="dollars[^"]*"[^>]*>([^<]+)</span>',h)
    pwyw='Name your own price' in h or 'name your own price' in h
    title=re.search(r'<h1 class="game_title"[^>]*>([^<]+)',h)
    f.write(json.dumps({'url':u,'title':title.group(1) if title else None,'pub':pub.group(1) if pub else None,'upd':upd.group(1) if upd else None,
      'ratings':int(rat.group(1).replace(',','')) if rat else 0,'avg':avg.group(1) if avg else None,'price':price.group(1) if price else None,'pwyw':pwyw,'len':len(h)})+"\n"); f.flush()
    time.sleep(1.5)
