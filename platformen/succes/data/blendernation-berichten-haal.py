import re,subprocess,json,time,sys
out=[]
for p in range(1,46):
    url="https://www.blendernation.com/category/blender/add-ons/" + ("" if p==1 else f"page/{p}/")
    h=subprocess.run(["curl","-sS",url],capture_output=True,text=True).stdout
    arts=h.split('<article')[1:]
    n=0
    for a in arts:
        m=re.search(r'card__title">(.*?)</h2>',a,re.S)
        u=re.search(r'href=(https://www.blendernation.com/20\d\d/\S+?)[\s>]',a)
        d=re.search(r'datetime=(\S+?)>',a)
        au=re.search(r'card__author>([^<]+)<',a)
        if m and d and u:
            out.append(dict(url=u.group(1),title=re.sub(r'<[^>]+>','',m.group(1)).strip(),date=d.group(1)[:10],author=au.group(1) if au else ""));n+=1
    print(p,n,out[-1]['date'] if out else "",file=sys.stderr)
    if n==0 or (out and out[-1]['date']<'2024-09-01'): break
    time.sleep(1.5)
json.dump(out,open('bn_addons.json','w'),indent=0)
print(len(out))
