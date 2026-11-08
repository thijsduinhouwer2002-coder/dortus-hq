import sys,re,subprocess,urllib.parse,html,time,json
def curl(u): return subprocess.run(['curl','-s','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
def txt(t):
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t)))
out=[]
for q in sys.argv[1:]:
    t=curl('https://superhivemarket.com/search?'+urllib.parse.urlencode({'search[q]':q,'search[category_id]':6,'sort_sales':'desc','page':1}))
    slugs=[]
    for m in re.finditer(r'/products/([A-Za-z0-9\-_]+)',t):
        if m.group(1) not in slugs: slugs.append(m.group(1))
    for s in slugs[:12]:
        x=txt(curl('https://superhivemarket.com/products/'+s)); time.sleep(0.5)
        g=lambda k: (re.search(k+r' (\S+(?: \S+){0,2})',x) or [None,None])[1]
        sales=(re.search(r'Sales (\d[\d,]*\+)',x) or [None,'-'])[1]
        pub=(re.search(r'Published (.+?) Blender',x) or [None,'-'])[1]
        price=(re.search(r'\$(\d+(?:\.\d+)?)',x) or [None,'-'])[1]
        print(q,'|',s,'|',sales,'|',pub,'|',price,flush=True)
