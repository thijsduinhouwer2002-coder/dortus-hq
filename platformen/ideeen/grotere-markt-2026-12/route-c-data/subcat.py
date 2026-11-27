import re, subprocess, json, time
def get(url):
    return subprocess.run(["curl","-s","-A","Mozilla/5.0","--max-time","40",url],capture_output=True,text=True).stdout
cats=["animation-scripts-and-addons","asset-management","import-export","interface","materials-and-shading-addons","modeling","rendering-scripts-and-addons","rigging-scripts-and-addons","vse","presets"]
out={}
for c in cats:
    out[c]=[]
    for p in range(1,7):
        h=get(f"https://superhivemarket.com/categories/{c}/browse?sort_sales=desc&page={p}")
        s=[x for x in re.findall(r'href="/products/([^"?/]+)"',h)]
        if not s:
            time.sleep(5); h=get(f"https://superhivemarket.com/categories/{c}/browse?sort_sales=desc&page={p}"); s=re.findall(r'href="/products/([^"?/]+)"',h)
        for x in s:
            if x not in out[c]: out[c].append(x)
        time.sleep(0.5)
    print(c,len(out[c]))
json.dump(out,open("./subcats.json","w"))
