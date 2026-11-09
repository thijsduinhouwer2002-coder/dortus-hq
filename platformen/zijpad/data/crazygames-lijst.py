import re,json,subprocess,time,sys
out=[]
for p in range(1,int(sys.argv[1])+1):
    url='https://www.crazygames.com/new' + ('' if p==1 else f'/{p}')
    h=subprocess.run(['curl','-sL',url],capture_output=True,text=True).stdout
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    if not m: print('fail',p); continue
    pp=json.loads(m.group(1))["props"]["pageProps"]
    if "games" not in pp: print("nogames",p); time.sleep(3); continue
    items=pp["games"]["items"]
    for it in items: it['_page']=p
    out+=items
    time.sleep(0.5)
json.dump(out,open('lijst.json','w'))
print(len(out))
