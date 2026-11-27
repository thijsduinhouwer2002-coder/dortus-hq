import re, subprocess, json, sys, concurrent.futures as cf
def get(url):
    return subprocess.run(["curl","-s","-A","Mozilla/5.0","--max-time","40",url],capture_output=True,text=True).stdout
pages=int(sys.argv[1])
def page(n):
    h=get(f"https://superhivemarket.com/categories/addons/browse?sort_sales=desc&page={n}")
    slugs=[]
    for s in re.findall(r'href="/products/([^"?/]+)"',h):
        if s not in slugs: slugs.append(s)
    return n,slugs
out={}
with cf.ThreadPoolExecutor(4) as ex:
    for n,s in ex.map(page,range(1,pages+1)): out[n]=s
order=[]
for n in sorted(out):
    for s in out[n]:
        if s not in order: order.append(s)
json.dump(order,open("./order.json","w"))
print(len(order))
