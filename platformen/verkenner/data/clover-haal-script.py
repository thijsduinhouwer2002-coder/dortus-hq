import json,subprocess,time,sys
out=open('clover-apps.jsonl','w'); off=0; n=0
while True:
    url=f"https://www.clover.com/v3/apps?limit=100&offset={off}"
    r=subprocess.run(['curl','-sS','--compressed','-m','60','-A','Mozilla/5.0 DortusResearch',url],capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception as e: print('fout',off,r.stdout[:200]); break
    el=d.get('elements',[])
    for e in el:
        e.pop('description',None); e.pop('locales',None)
        out.write(json.dumps(e)+'\n')
    n+=len(el); print(off,len(el),flush=True)
    if len(el)<100: break
    off+=100; time.sleep(1)
print('totaal',n)
