import random, re, json, subprocess, sys, concurrent.futures as cf, time
random.seed(91109)
ids = random.sample(range(15400000, 16900000), int(sys.argv[1]))
def get(i):
    time.sleep(0.3)
    r = subprocess.run(["curl","-sL","-m","30","-A","Mozilla/5.0 (compatible; DortusResearch/1.0)","-w","\n%{http_code}",f"https://www.teacherspayteachers.com/Product/{i}"],capture_output=True,text=True,errors="ignore")
    t, code = r.stdout.rsplit("\n",1)
    d={"id":i,"code":code}
    m=re.search(r'"Product:%d":\{'%i,t)
    if not m or code!="200": d["product"]=False; return d
    d["product"]=True
    def f(p):
        x=re.search(p,t); return x.group(1) if x else None
    d["release"]=f(r'"releaseDate":"([^"]*)')
    d["price"]=f(r'"offers":\{[^}]*"price":"([^"]*)')
    d["ratings"]=f(r'"evaluationRating":\{"__typename":"AggregateRatingResult","count":(\d+)')
    d["score"]=f(r'"evaluationRating":\{[^}]*"scoreAverage":"([^"]*)')
    d["store"]=f(r'"Store:(\d+)":\{')
    d["followers"]=f(r'"Store:\d+":\{[^{]*?"followerCount":(\d+)')
    d["brand"]=f(r'"brand":\{"@type":"Brand","name":"([^"]*)')
    return d
with cf.ThreadPoolExecutor(3) as ex, open(sys.argv[2],"w") as out:
    for d in ex.map(get, ids): out.write(json.dumps(d)+"\n")
