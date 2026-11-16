import re,random,subprocess,time,json,sys,os
D=sys.argv[2] if len(sys.argv)>2 else 'cws'  # gebruik: python3 -I script.py <aantal> <map met shard0.xml>
urls=re.findall(r'<loc>(https://chromewebstore.google.com/detail/[^<]+)</loc>',open(D+'/shard0.xml').read())
random.seed(42); samp=random.sample(urls,int(sys.argv[1]))
pat=re.compile(r',(\d+),(?:1|null),(?:null|"[^"]*"),\[(1[3-9]\d{8}),\d+\],"\{')
out=open(D+'/cws_sample.jsonl','a'); rel=open(D+'/cws_related.jsonl','a')
for u in samp:
    t0=time.time()
    try:
        h=subprocess.run(['curl','-sS','-m','30',u+'?hl=en'],capture_output=True,text=True).stdout
    except Exception as e: h=''
    ms=pat.findall(h)
    m=re.search(r'>([\d,]+) users?<',h)
    upd=re.search(r'Updated</div><div[^>]*>([^<]+)<',h)
    iap='Offers in-app purchases' in h
    rec={'url':u,'users_text':m.group(1) if m else None,'main':ms[0] if ms else None,'iap':iap,'len':len(h)}
    out.write(json.dumps(rec)+'\n'); out.flush()
    for x in ms[1:]: rel.write(json.dumps({'from':u,'users':x[0],'ts':x[1]})+'\n')
    rel.flush()
    time.sleep(max(0,1.1-(time.time()-t0)))
