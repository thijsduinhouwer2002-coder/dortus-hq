# Verhaal 23 (Fenna): nieuws-API van de 60 grootste uitgebrachte bureaubladspellen, zinnen over de demo.
# Gebruik: python3 -I demo-einde-nieuws.py <uitmap>
import csv,json,time,urllib.request,sys,os,re,html
S=sys.argv[1]; os.makedirs(S+'/news',exist_ok=True)
r=list(csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv')))
g=[x for x in r if x['binnenkort']!='True' and x['gratis']!='True' and x['soort_app']!='programma']
g=sorted(g,key=lambda x:-int(x['reviews_totaal'] or 0))[:60]
for x in g:
    a=x['appid']; p=f'{S}/news/{a}.json'
    if os.path.exists(p): continue
    try: o=urllib.request.urlopen(f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={a}&count=300&maxlength=0&feeds=steam_community_announcements',timeout=30).read()
    except Exception as e: o=b'{}'
    open(p,'wb').write(o); time.sleep(1)
