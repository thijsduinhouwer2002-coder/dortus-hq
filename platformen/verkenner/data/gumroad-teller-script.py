import re,json,subprocess,sys,concurrent.futures as cf,time,html
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
def get(u):
    time.sleep(0.3)
    r=subprocess.run(["curl","-sL","-m","25","-A","Mozilla/5.0","-w","\n%{http_code}",u],capture_output=True,text=True,errors="ignore")
    t,code=r.stdout.rsplit("\n",1); t=html.unescape(t)
    def f(p):
        m=re.search(p,t); return m.group(1) if m else None
    return {"url":u,"code":code,"sales":f(r'"sales_count":(null|\d+)'),"ratings":f(r'"ratings":\{"count":(\d+)'),"avg":f(r'"ratings":\{"count":\d+,"average":([\d.]+)')}
with cf.ThreadPoolExecutor(4) as ex, open(sys.argv[2],"w") as o:
    for d in ex.map(get,urls): o.write(json.dumps(d)+"\n")
